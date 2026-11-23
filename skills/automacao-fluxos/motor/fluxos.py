#!/usr/bin/env python3
"""fluxos.py: a linha de comando do motor de automação. Perfil por --perfil <arquivo> ou AF_PERFIL.

  conferir                       perfil, segredos e cada desenho em AF_FLUXOS_DIR (nada é escrito)
  status [fluxo]                 modo, último evento, trânsito de 24 h, episódios abertos
  transito <fluxo> [--horas N]   quantos passaram por cada RAMO e cada PASSO (o contador de trânsito)
  modo <fluxo> desligado|seco|teste
  ligar <fluxo> --ok             real, só com prova de trânsito do desenho atual
  rota <fluxo>                   cria a rota secreta e grava a URL em <dados>/url-<fluxo>.txt (600) para o DONO abrir
  simular <fluxo> --json <arq>   manda o JSON pela URL PÚBLICA (Caddy, HTTPS, receptor), marcado como simulação
  esperar <fluxo> --minutos N [--rodar-ciclo]   espera um evento novo e o fim dos passos dele (teste de trânsito)
  lembrete-teste <fluxo>         lembrete-aula em teste: manda agora o lembrete da próxima aula ao grupo de teste
  ciclo                          o que o timer roda: passos devidos, lembretes, provas, vigia
  vigia                          só o vigia
  receptor                       o serviço HTTP (127.0.0.1:AF_PORTA)
  refazer <passo_id>             passo `falhou` sem POST volta para a fila
  visto <fluxo>                  marca como vistos os passos com problema e os lembretes perdidos (fecha o alarme)

Saída: 0 ok · 1 alarme/condição não atendida · 2 não consegui medir · 3 recusado por trava · 10 segredo · 11 perfil.
Toda recusa sai com MOTIVO=<slug> na primeira linha do stderr.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import modelos       # noqa: E402
import executor      # noqa: E402
import vigia         # noqa: E402
from base import Recusa, ler_perfil, ler_segredo  # noqa: E402
from versao import VERSAO  # noqa: E402


def _args(argv):
    perfil, resto, i = None, [], 0
    while i < len(argv):
        if argv[i] == '--perfil' and i + 1 < len(argv):
            perfil = argv[i + 1]
            i += 2
        else:
            resto.append(argv[i])
            i += 1
    return perfil, resto


def _opcao(resto, nome, padrao=None):
    if nome in resto:
        i = resto.index(nome)
        if i + 1 < len(resto):
            return resto[i + 1]
        raise Recusa('argumento_sem_valor', nome, rc=2)
    return padrao


def conferir(motor):
    p = motor.perfil
    linhas = [f'perfil: {p["arquivo"]} (versão do motor {VERSAO})']
    fluxos = motor.fluxos()
    if not fluxos:
        linhas.append(f'nenhum desenho em {p["af_fluxos_dir"]} (copie de modelos/ e preencha; o instalador cria a pasta)')
    usa_mautic = usa_wa = usa_hm = False
    for nome, cfg in fluxos.items():
        s = json.dumps(cfg)
        usa_mautic |= '"mautic"' in s
        usa_wa |= '"whatsapp"' in s or cfg['tipo'] == 'lembrete-aula'
        usa_hm |= cfg['tipo'] == 'venda-hotmart'
        linhas.append(f'fluxo {nome}: tipo {cfg["tipo"]}, modo {motor.modo_sem_escrever(nome)}, '
                      f'desenho {modelos.desenho(cfg)[:8]}')
    if usa_mautic:
        if not p['mautic_url']:
            raise Recusa('mautic_nao_configurado', 'um desenho usa Mautic e AF_MAUTIC_URL está vazio', rc=10)
        ler_segredo(p['mautic_cred'], ('MAUTIC_API_USUARIO', 'MAUTIC_API_SENHA'))
        linhas.append('Mautic: credencial ok (valor não exibido)')
    if usa_wa:
        if not (p['openwa_base'] and p['openwa_sessao']):
            raise Recusa('openwa_nao_configurado', 'um desenho usa WhatsApp e AF_OPENWA_BASE/SESSAO_ID estão vazios',
                         rc=10)
        ler_segredo(p['openwa_chave'], ('OPENWA_CHAVE',))
        linhas.append('WhatsApp (OpenWA): chave ok (valor não exibido)')
    if usa_hm:
        ler_segredo(p['hottok_arquivo'], ('HOTMART_HOTTOK',))
        linhas.append('Hotmart: hottok ok (valor não exibido)')
    if p['aviso_canal'] == 'arquivo':
        linhas.append(f'aviso: SECO, os alarmes ficam em {p["af_dados_dir"]}/avisos.jsonl')
    else:
        alvo = p['aviso_canal'].split(':', 1)[1]
        if not os.access(alvo, os.X_OK):
            raise Recusa('canal_ausente', f'o comando de aviso {alvo} não existe ou não é executável', rc=10)
        linhas.append(f'aviso: comando {alvo}')
    return linhas


def status(motor, so=None):
    agora = motor.relogio()
    out = {'parado': motor.parado(), 'fluxos': {}}
    for nome, cfg in motor.fluxos().items():
        if so and nome != so:
            continue
        ult = motor.banco.ultimo_evento(nome)
        out['fluxos'][nome] = {
            'tipo': cfg['tipo'], 'modo': motor.modo(nome),
            'armado': motor.armado_ok(cfg) if motor.modo(nome) == 'real' else None,
            'ultimo_evento_ha_min': (agora - ult) // 60 if ult else None,
            'transito_24h': motor.banco.transito(nome, agora - 86400)}
    out['alarmes_abertos'] = [f'{e["fluxo"]}:{e["tipo"]}' for e in motor.banco.episodios_abertos()]
    return out


def simular(motor, nome, arq):
    cfg = motor.fluxo(nome)
    corpo = Path(arq).read_bytes()
    json.loads(corpo)
    if b'PREENCHER' in corpo:
        raise Recusa('simulacao_incompleta', f'{arq} ainda tem PREENCHER', rc=2)
    h = {'Content-Type': 'application/json', 'X-Fluxos-Simulado': '1'}
    if cfg['tipo'] == 'venda-hotmart':
        h['X-HOTMART-HOTTOK'] = ler_segredo(motor.perfil['hottok_arquivo'], ['HOTMART_HOTTOK'])['HOTMART_HOTTOK']
        url = f'{motor.perfil["url_publica"]}/f/{nome}'
    else:
        tok = motor.token_rota(nome)
        if not tok:
            raise Recusa('sem_rota', f'rode `fluxos.py rota {nome}` antes', rc=3)
        url = f'{motor.perfil["url_publica"]}/f/{nome}/{tok}'
    local = os.environ.get('AF_SIMULAR_BASE', '')
    if local:   # laboratório: o receptor local direto, sem Caddy. Só 127.0.0.1, nunca outro destino
        if not re.fullmatch(r'http://127\.0\.0\.1:[0-9]{2,5}', local):
            raise Recusa('simular_base_invalida', 'AF_SIMULAR_BASE só aceita http://127.0.0.1:<porta>', rc=2)
        url = local + url[len(motor.perfil['url_publica']):]
    req = urllib.request.Request(url, data=corpo, method='POST', headers=h)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            st = r.status
    except urllib.error.HTTPError as e:
        st = e.code
    except (urllib.error.URLError, OSError) as e:
        raise Recusa('simular_inalcancavel', f'a URL pública não respondeu ({type(e).__name__}): DNS, Caddy ou '
                     'receptor fora', rc=1) from None
    return st


def esperar(motor, nome, minutos, rodar_ciclo):
    """Espera um evento NOVO deste fluxo e os passos dele terminarem. rc 0 = atravessou inteiro (todos feito)."""
    motor.fluxo(nome)
    ultimo = motor.banco.c.execute('SELECT coalesce(max(id), 0) m FROM eventos').fetchone()['m']
    limite = time.monotonic() + minutos * 60
    while True:
        if rodar_ciclo:
            motor.ciclo()
        ev = motor.banco.c.execute('SELECT * FROM eventos WHERE fluxo=? AND id>? ORDER BY id DESC LIMIT 1',
                                   (nome, ultimo)).fetchone()
        if ev:
            ps = motor.banco.passos_do_evento(ev['id'])
            if all(p['estado'] in ('feito', 'falhou', 'incerto', 'pulado', 'seco', 'expirado') for p in ps):
                res = {'evento': ev['id'], 'ramo': ev['ramo'], 'modo': ev['modo'],
                       'passos': [{'tipo': p['tipo'], 'estado': p['estado'], 'motivo': p['motivo']} for p in ps]}
                ok = bool(ps) and all(p['estado'] == 'feito' for p in ps) or (not ps and ev['ramo'].startswith(
                    ('palavra:', 'batida')))
                return (0 if ok else 1), res
        if time.monotonic() >= limite:
            return 1, {'evento': None, 'motivo': 'nenhum evento novo chegou no prazo: a origem não está batendo '
                                                 'na URL (fiação), ou o receptor está fora'}
        time.sleep(3)


def main(argv):
    os.umask(0o077)
    caminho, resto = _args(argv[1:])
    if not resto or resto[0] in ('-h', '--help', 'ajuda'):
        print(__doc__)
        return 0
    cmd, a = resto[0], resto[1:]
    try:
        perfil = ler_perfil(caminho)
        motor = executor.Motor(perfil)
        if cmd == 'conferir':
            print('\n'.join(conferir(motor)))
            return 0
        if cmd == 'status':
            print(json.dumps(status(motor, a[0] if a else None), ensure_ascii=False, indent=1))
            return 0
        if cmd == 'transito':
            h = int(_opcao(a, '--horas', '24'))
            print(json.dumps(motor.banco.transito(motor.fluxo(a[0])['nome'], motor.relogio() - h * 3600),
                             ensure_ascii=False, indent=1))
            return 0
        if cmd == 'modo':
            print(f'{a[0]}: {motor.mudar_modo(a[0], a[1])}')
            return 0
        if cmd == 'ligar':
            if '--ok' not in a:
                raise Recusa('ligar_sem_ok', 'ligar só com --ok, depois do OK do dono', rc=3)
            des = motor.ligar(a[0])
            print(f'{a[0]}: LIGADO (real), desenho {des[:8]}. Mudou o desenho = volta a esperar teste e OK')
            return 0
        if cmd == 'rota':
            p = motor.gerar_rota(a[0])
            print(f'URL gravada em {p} (600). Abra no SEU terminal (cat) e cole na ferramenta de origem; '
                  'não cole no chat.')
            return 0
        if cmd == 'simular':
            st = simular(motor, a[0], _opcao(a, '--json'))
            print(f'simulação: HTTP {st}')
            return 0 if st == 200 else 1
        if cmd == 'esperar':
            rc, res = esperar(motor, a[0], int(_opcao(a, '--minutos', '5')), '--rodar-ciclo' in a)
            print(json.dumps(res, ensure_ascii=False, indent=1))
            return rc
        if cmd == 'lembrete-teste':
            print(f'lembretes de teste criados: {len(motor.lembrete_teste(a[0]))}; rode `ciclo` (ou espere o timer)')
            return 0
        if cmd in ('ciclo', 'vigia'):
            res = motor.ciclo() if cmd == 'ciclo' else {}
            res['vigia'] = vigia.rodar(motor)
            print(json.dumps(res, ensure_ascii=False))
            return 1 if res['vigia']['estado'] != 'OK' else 0
        if cmd == 'receptor':
            from receptor import servidor
            srv = servidor(motor)
            print(f'af-receptor {VERSAO} em 127.0.0.1:{perfil["porta"]}', file=sys.stderr, flush=True)
            srv.serve_forever()
            return 0
        if cmd == 'refazer':
            motor.refazer(int(a[0]))
            print(f'passo {a[0]} de volta à fila')
            return 0
        if cmd == 'visto':
            print(f'{motor.visto(a[0])} passo(s) marcados como vistos')
            return 0
        raise Recusa('comando_desconhecido', cmd, rc=2)
    except Recusa as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        if e.detalhe:
            print(e.detalhe, file=sys.stderr)
        return e.rc
    except IndexError:
        print('MOTIVO=argumento_faltando', file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 2
    except Exception as e:   # noqa: BLE001 - banco ilegível etc.: "não consegui medir", nunca OK
        print(f'MOTIVO=nao_consegui_medir', file=sys.stderr)
        print(type(e).__name__, file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
