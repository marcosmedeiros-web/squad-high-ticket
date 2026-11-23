#!/usr/bin/env python3
"""capi_worker.py: esvazia a fila da API de Conversões. Roda a cada minuto pelo timer (oneshot).

DEGRAUS, e só sai chamada para a Meta com os dois de cima juntos:
  1. CAPI_MODO=teste ou real no perfil;
  2. HM_CAPI_ARMADO=1 no ambiente, que só existe no drop-in escrito por `instalar.sh --com-capi`.
  Sem os dois, o evento vira `seco`: o payload (já em hash) é copiado para dados/seco-capi.jsonl (600) para o
  dono ler o que iria, e nada sai. No modo teste o test_event_code vai junto, e os eventos aparecem só na aba
  "Testar eventos" do Gerenciador de Eventos.
  Freio de mão: o arquivo dados/PARAR-CAPI. Existindo, nada sai e nada é marcado; a fila espera.

RETENTATIVA: 429, 5xx, rede e os códigos transitórios da Graph API voltam para a fila com espera crescente
(1, 5, 15, 60 min, depois de hora em hora). Nunca passa de 7 dias do event_time: aí vira `velho_demais`.
4xx com erro de validação vira `rejeitado` na hora (repetir o mesmo corpo repetiria a mesma recusa).

Uso:
  capi_worker.py --ciclo                 processa o que venceu e purga o que passou da retenção
  capi_worker.py --evento-sintetico      SÓ no modo teste: põe na fila um Purchase sintético com hora de agora,
                                         para conferir na aba "Testar eventos" (o evento de teste do painel da
                                         Hotmart vem com data antiga e cairia em velho_demais)
"""
import json
import os
import secrets
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import banco as bco      # noqa: E402
import capi              # noqa: E402
import config            # noqa: E402
import segredo           # noqa: E402

ESPERAS = (60, 300, 900, 3600)


def log(_fato, **campos):
    partes = [f'{k}={v}' for k, v in campos.items() if v is not None]
    print(f'hm-capi {_fato} ' + ' '.join(partes), file=sys.stderr, flush=True)


def armado(perfil, ambiente=None):
    ambiente = os.environ if ambiente is None else ambiente
    return perfil['modo'] in ('teste', 'real') and ambiente.get('HM_CAPI_ARMADO') == '1'


def _seco(b, item):
    p = b.dir / 'seco-capi.jsonl'
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(fd, 'a') as f:
        f.write(json.dumps({'chave': item['chave'], 'origem': item['origem'],
                            'evento': json.loads(item['payload'])}, separators=(',', ':')) + '\n')


def ciclo(perfil, b=None, transporte=None, ambiente=None, agora=None):
    b = b or bco.Banco(perfil['dados_dir'])
    agora = int(agora or time.time())
    cont = {'enviado': 0, 'seco': 0, 'rejeitado': 0, 'velho_demais': 0, 'adiado': 0, 'parado': 0}
    if (b.dir / 'PARAR-CAPI').exists():
        cont['parado'] = len(b.fila_vencida(agora))
        log('parado', pendentes=cont['parado'])
        return cont
    fila = b.fila_vencida(agora)
    vai_de_verdade = armado(perfil, ambiente)
    token = None
    if fila and vai_de_verdade:
        try:
            token = segredo.ler(perfil['token_arquivo'], ['META_CAPI_TOKEN'])['META_CAPI_TOKEN']
        except segredo.SegredoErro as e:
            log('token_ilegivel', motivo=e.motivo)
            return cont
    for item in fila:
        ev = json.loads(item['payload']) if item['payload'] else None
        if ev is None:
            b.fila_desfecho(item['chave'], 'rejeitado', 'sem_payload')
            cont['rejeitado'] += 1
            continue
        if capi.velho_demais(ev, agora):
            b.fila_desfecho(item['chave'], 'velho_demais', 'event_time_mais_de_7_dias')
            cont['velho_demais'] += 1
            continue
        if not vai_de_verdade:
            _seco(b, item)
            b.fila_desfecho(item['chave'], 'seco', f'modo={perfil["modo"]}', apagar_payload=False)
            cont['seco'] += 1
            continue
        resultado, resumo = capi.enviar(ev, perfil, token, transporte)
        if resultado == 'enviado':
            b.fila_desfecho(item['chave'], 'enviado', resumo)
            cont['enviado'] += 1
        elif resultado == 'rejeitado':
            b.fila_desfecho(item['chave'], 'rejeitado', resumo)
            cont['rejeitado'] += 1
        else:
            espera = ESPERAS[min(item['tentativas'], len(ESPERAS) - 1)]
            b.fila_adiar(item['chave'], resumo, agora + espera)
            cont['adiado'] += 1
        log('envio', origem=item['origem'], resultado=resultado, resumo=resumo.replace(' ', ','))
    token = None
    pur = b.purgar(agora)
    log('ciclo', modo=perfil['modo'], armado=int(vai_de_verdade), **cont, **pur)
    return cont


def evento_sintetico(perfil, b=None):
    if perfil['modo'] != 'teste':
        log('recusa', motivo='sintetico_so_no_modo_teste')
        return None
    b = b or bco.Banco(perfil['dados_dir'])
    agora = int(time.time())
    ev = {'event_name': 'Purchase', 'event_time': agora, 'event_id': 'hm.TESTE' + secrets.token_hex(6).upper(),
          'action_source': perfil['origem_sem_navegador'] if perfil['origem_sem_navegador'] != 'website' else 'other',
          'user_data': {'external_id': [capi.nz.sha256('teste-' + secrets.token_hex(8))]},
          'custom_data': {'currency': 'BRL', 'value': 1.0, 'order_id': 'TESTE'}}
    b.enfileirar_avulso(f'Purchase|{ev["event_id"]}', 'sintetico', ev)
    log('sintetico_enfileirado', event_id=ev['event_id'])
    return ev['event_id']


def main(argv):
    os.umask(0o077)
    try:
        perfil = config.carregar()
    except config.PerfilRecusado as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        return 78
    if argv[1:] == ['--ciclo']:
        ciclo(perfil)
        return 0
    if argv[1:] == ['--evento-sintetico']:
        return 0 if evento_sintetico(perfil) else 2
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
