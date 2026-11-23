"""vigia.py: o alarme de FALHA SILENCIOSA. Roda no mesmo timer do ciclo (a cada minuto) e olha o trânsito, não a
configuração: um fluxo perfeitamente cabeado que ninguém atravessa é o defeito que esta casa mais viu.

O QUE ACENDE (por fluxo; cada um é um EPISÓDIO: um aviso quando abre, um aviso quando volta)
  silencio          ligado (real) e nenhum evento há mais de `vigia.silencio_max_h` horas
                    (padrão: formulário 24, venda 72, batida 24; 0 desliga)
  palavra_muda      batida com `palavras`: uma palavra sem batida há `vigia.palavra_silencio_max_h` horas (0 desliga)
  sem_regra         ligado e entrou evento que o fluxo NÃO SABE tratar nas últimas 24 h (produto sem regra, formulário
                    sem e-mail nem telefone, palavra fora da lista, webhook de outra versão)
  recusas           3 ou mais entradas recusadas na última hora (hottok trocado, rota velha no formulário)
  travado           passo parado há mais de `vigia.travado_min` minutos (padrão 30), fora de janela de horário
  falhas            passo `falhou`, `incerto` ou `expirado` ainda não visto (`fluxos.py visto <fluxo>` depois de tratar)
  desenho_mudou     ligado, mas o desenho mudou depois do OK: o que entra fica `esperando_ok`
  teto              o teto diário de WhatsApp foi atingido hoje
  perdido           lembrete que passou da hora sem sair
  agenda_vazia      lembrete ligado sem aula nos próximos `vigia.agenda_minima_dias` dias (padrão 8; 0 desliga)
  receptor_fora     há fluxo recebendo evento e o receptor local não responde em /saude

Três estados de saída do vigia, nunca dois: OK, ALERTA (com a lista) e NAO_CONSEGUI_MEDIR (banco ilegível,
desenho torto). "Não consegui medir" nunca vira OK.
"""
import json
import urllib.request
from datetime import datetime, timedelta, timezone

import canais
import modelos

SILENCIO_PADRAO_H = {'lead-formulario': 24, 'venda-hotmart': 72, 'batida': 24}
RAMOS_SEM_REGRA = ('sem_regra', 'invalido', 'palavra_fora_da_lista')
TEXTOS = {
    'silencio': 'parou de passar evento: o último entrou há {h} h (limite {lim} h). Conferir a origem (formulário, '
                'webhook, ManyChat) e o receptor',
    'palavra_muda': 'a palavra "{p}" não passa há {h} h (limite {lim} h): conferir o gatilho dela',
    'sem_regra': '{n} evento(s) nas últimas 24 h que o fluxo não sabe tratar ({ramos})',
    'recusas': '{n} entrada(s) recusada(s) na última hora (credencial ou rota errada na origem)',
    'travado': '{n} passo(s) parado(s) há mais de {lim} min',
    'falhas': 'passo(s) com problema: {det}. Ver `fluxos.py transito {f}`; depois de tratar, `fluxos.py visto {f}`',
    'desenho_mudou': 'o desenho mudou depois do OK; {n} passo(s) esperando teste e novo `ligar --ok`',
    'teto': 'teto diário de WhatsApp atingido; o resto fica para amanhã',
    'perdido': '{n} lembrete(s) passaram da hora sem sair',
    'agenda_vazia': 'nenhuma aula nos próximos {d} dias: cadastre a próxima ou o lembrete para em silêncio',
    'receptor_fora': 'o receptor local não respondeu em /saude ({m})',
}


def _cfgv(cfg, chave, padrao):
    return int(cfg.get('vigia', {}).get(chave, padrao))


def medir(motor):
    """-> lista de (fluxo, tipo, detalhe). Levanta se não consegue medir."""
    b = motor.banco
    agora = motor.relogio()
    probs = []
    fluxos = motor.fluxos()
    recebe = False
    for nome, cfg in fluxos.items():
        modo = b.modo(nome)
        if modo == 'desligado':
            continue
        tipo = cfg['tipo']
        if tipo != 'lembrete-aula' and modo in ('teste', 'real'):
            recebe = True
        n = b.contar_recusas(nome, agora - 3600)
        if n >= 3:
            probs.append((nome, 'recusas', TEXTOS['recusas'].format(n=n)))
        if not motor.parado():
            lim = _cfgv(cfg, 'travado_min', 30)
            n = b.passos_presos(nome, agora - lim * 60)
            if n:
                probs.append((nome, 'travado', TEXTOS['travado'].format(n=n, lim=lim)))
        falhos = {r['estado']: r['n'] for r in b.passos_falhos(nome)}
        if falhos:
            det = ', '.join(f'{v} {k}' for k, v in sorted(falhos.items()))
            probs.append((nome, 'falhas', TEXTOS['falhas'].format(det=det, f=nome)))
        if modo != 'real':
            continue
        desde = int(b.get(f'ativo_desde:{nome}', agora))
        if not motor.armado_ok(cfg):
            probs.append((nome, 'desenho_mudou', TEXTOS['desenho_mudou'].format(n=b.esperando_ok(nome))))
        if tipo in SILENCIO_PADRAO_H:
            lim = _cfgv(cfg, 'silencio_max_h', SILENCIO_PADRAO_H[tipo])
            ult = max(b.ultimo_evento(nome) or 0, desde)
            if lim and agora - ult > lim * 3600:
                probs.append((nome, 'silencio', TEXTOS['silencio'].format(h=(agora - ult) // 3600, lim=lim)))
            r = b.c.execute('SELECT ramo, count(*) n FROM eventos WHERE fluxo=? AND recebido>=? AND ramo IN (%s) '
                            'GROUP BY ramo' % ','.join('?' * len(RAMOS_SEM_REGRA)),
                            (nome, agora - 86400, *RAMOS_SEM_REGRA)).fetchall()
            if r:
                probs.append((nome, 'sem_regra', TEXTOS['sem_regra'].format(
                    n=sum(x['n'] for x in r), ramos=', '.join(f'{x["ramo"]} {x["n"]}' for x in r))))
        if tipo == 'batida':
            lim = _cfgv(cfg, 'palavra_silencio_max_h', 0)
            if lim:
                for p in cfg.get('palavras', []):
                    ult = max(b.ultimo_evento(nome, [f'palavra:{modelos.norm(p)}']) or 0, desde)
                    if agora - ult > lim * 3600:
                        probs.append((nome, f'palavra_muda:{modelos.norm(p)}', TEXTOS['palavra_muda'].format(
                            p=modelos.norm(p), h=(agora - ult) // 3600, lim=lim)))
        if tipo == 'lembrete-aula':
            n = b.c.execute("SELECT count(*) n FROM eventos WHERE fluxo=? AND ramo='perdido' "
                            "AND coalesce(nota, '')!='visto'", (nome,)).fetchone()['n']
            if n:
                probs.append((nome, 'perdido', TEXTOS['perdido'].format(n=n)))
            dias = _cfgv(cfg, 'agenda_minima_dias', 8)
            prox = modelos.proxima_aula(cfg, agora)
            if dias and (prox is None or prox > agora + dias * 86400):
                probs.append((nome, 'agenda_vazia', TEXTOS['agenda_vazia'].format(d=dias)))
    tz = timezone(timedelta(hours=motor.perfil['fuso_utc']))
    hoje = datetime.fromtimestamp(agora, tz).strftime('%Y-%m-%d')
    if b.get(f'teto:{hoje}'):
        probs.append(('_whatsapp', 'teto', TEXTOS['teto']))
    if recebe:
        m = saude(motor.perfil['porta'])
        if m:
            probs.append(('_receptor', 'receptor_fora', TEXTOS['receptor_fora'].format(m=m)))
    return probs


def saude(porta):
    """None = respondeu; senão o motivo curto."""
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(
                f'http://127.0.0.1:{porta}/saude', timeout=5) as r:
            j = json.loads(r.read().decode() or '{}')
            return None if r.status == 200 and j.get('ok') else f'http_{r.status}'
    except Exception as e:   # noqa: BLE001 - qualquer falha aqui é "não respondeu", com o nome da classe
        return type(e).__name__


def rodar(motor, avisar=None):
    """Abre e fecha episódios e entrega os avisos. -> dict com estado, problemas e avisos entregues."""
    avisar = avisar or (lambda texto: canais.avisar(motor.perfil, texto, motor.dados))
    b = motor.banco
    agora = motor.relogio()
    probs = medir(motor)
    atuais = {(f, t): d for f, t, d in probs}
    for f, t in atuais:
        if not b.episodio_aberto(f, t):
            b.abrir_episodio(f, t, agora, atuais[(f, t)])
    for ep in b.episodios_abertos():
        if (ep['fluxo'], ep['tipo']) not in atuais:
            b.episodio_set(ep['rowid'], fechado=agora)
        else:
            b.episodio_set(ep['rowid'], detalhe=atuais[(ep['fluxo'], ep['tipo'])])
    entregues = 0
    for ep in b.episodios_abertos():
        if ep['avisado']:
            continue
        if ep['tentativas'] >= 10 and agora - ep['ultima_tentativa'] < 3600:
            continue
        texto = f'automacao-fluxos: {ep["fluxo"]}: {ep["detalhe"]}'
        ok = avisar(texto)
        b.episodio_set(ep['rowid'], tentativas=ep['tentativas'] + 1, ultima_tentativa=agora, avisado=1 if ok else 0)
        entregues += bool(ok)
    for ep in b.episodios_volta_pendente():
        tipo = ep['tipo'].split(':')[0]
        ok = avisar(f'automacao-fluxos: {ep["fluxo"]}: voltou ao normal ({tipo})')
        if ok:
            b.episodio_set(ep['rowid'], volta_avisada=1)
            entregues += 1
    b.c.execute('UPDATE episodios SET volta_avisada=1 WHERE fechado IS NOT NULL AND avisado=0')
    return {'estado': 'ALERTA' if probs else 'OK', 'problemas': [f'{f}:{t}' for f, t, _ in probs],
            'avisos_entregues': entregues}
