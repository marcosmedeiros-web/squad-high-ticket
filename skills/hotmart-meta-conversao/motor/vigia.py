#!/usr/bin/env python3
"""vigia.py: o plano B do webhook. Pergunta "saiu venda que o webhook não trouxe?".

POR QUE EXISTE: a Hotmart desativa sozinha a configuração do webhook quando a URL dá erro (Central de Ajuda,
artigo 360001491352), e ninguém é avisado. Webhook desativado não dá erro em lugar nenhum do lado de cá: só
fica quieto. Quieto e "sem venda" são o mesmo silêncio, então o vigia compara com a leitura da API.

DUAS CONFERÊNCIAS
  silêncio   (VIGIA_SILENCIO_HORAS > 0) nenhum evento da Hotmart há mais que isso. Desligado por padrão,
             porque produto parado também é silêncio; ligue em semana de lançamento.
  comparação (precisa de HM_HOTMART_CRED_ARQUIVO) lê as vendas APROVADAS da API no período e procura cada uma
             entre as compras que o webhook entregou. Venda aprovada há mais de VIGIA_TOLERANCIA_MIN e ausente
             do banco = BURACO.

TRÊS ESTADOS, NUNCA DOIS (código de saída)
  0 COBERTO              mediu e não falta nada
  1 BURACO               mediu e falta venda (ou silêncio acima do limite); diz quantas, por hash8
  2 NAO_CONSEGUI_MEDIR   credencial, rede, HTTP, paginação que não fecha. Nunca vira COBERTO.
  O webhook "provavelmente desativado" é o BURACO sem nenhum evento recebido desde a venda mais antiga que faltou.

AVISO: uma vez por venda faltante (o hash8 fica no estado), e o NAO_CONSEGUI_MEDIR só na 3a rodada seguida.
Canal em HM_AVISO_CANAL: `arquivo:/caminho.jsonl` (uma linha JSON por aviso) ou `comando:/script` (recebe a linha
JSON na entrada padrão). Sem canal, só o log. O aviso nunca leva nome, e-mail, telefone nem o código cru da
transação: só hash8, produto e contagem.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import banco as bco        # noqa: E402
import config              # noqa: E402
import hotmart_api as ha   # noqa: E402
import normaliza as nz     # noqa: E402

RC_COBERTO, RC_BURACO, RC_NAO_MEDIU = 0, 1, 2
MARGEM_PEDIDO_MS = 10 * 86400 * 1000      # boleto aprovado dias depois do pedido
FALHAS_PARA_AVISAR = 3


def log(_fato, **campos):
    partes = [f'{k}={v}' for k, v in campos.items() if v is not None]
    print(f'hm-vigia {_fato} ' + ' '.join(partes), file=sys.stderr, flush=True)


def _estado(b):
    p = b.dir / 'vigia-estado.json'
    try:
        d = json.loads(p.read_text())
        if isinstance(d, dict):
            return d
    except (OSError, ValueError):
        pass
    return {'avisados': [], 'falhas_seguidas': 0}


def _gravar_estado(b, d):
    p = b.dir / 'vigia-estado.json'
    tmp = p.with_suffix('.tmp')
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as f:
        json.dump(d, f)
    os.replace(tmp, p)


def avisar(perfil, linha):
    canal = perfil.get('aviso_canal') or ''
    texto = json.dumps(linha, ensure_ascii=False, separators=(',', ':'))
    try:
        if canal.startswith('arquivo:'):
            fd = os.open(canal[len('arquivo:'):], os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            with os.fdopen(fd, 'a') as f:
                f.write(texto + '\n')
            return 'entregue'
        if canal.startswith('comando:'):
            r = subprocess.run([canal[len('comando:'):]], input=texto.encode(), timeout=30,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            return 'entregue' if r.returncode == 0 else f'comando_rc{r.returncode}'
    except (OSError, subprocess.SubprocessError) as e:
        return f'falhou:{type(e).__name__}'
    return 'sem_canal'


def medir(perfil, b, cliente=None, agora=None):
    agora = int(agora or time.time())
    res = {'estado': 'COBERTO', 'faltam': [], 'silencio': False, 'motivo': None, 'webhook_desativado_provavel': False}
    ultimo = b.ultimo_evento_em()
    if perfil['vigia_silencio_h'] and (ultimo is None or agora - ultimo > perfil['vigia_silencio_h'] * 3600):
        res['silencio'] = True
        res['estado'] = 'BURACO'
    if not perfil.get('hotmart_cred_arquivo'):
        res['comparacao'] = 'desligada'
        return res
    cliente = cliente or ha.Cliente(perfil['hotmart_cred_arquivo'])
    janela_ini = agora - perfil['vigia_janela_h'] * 3600
    limite = agora - perfil['vigia_tolerancia_min'] * 60
    try:
        vendas = []
        for prod in (perfil['produtos'] or [None]):
            vendas += cliente.vendas_confirmadas(janela_ini * 1000 - MARGEM_PEDIDO_MS, agora * 1000 + 86400000, prod)
    except ha.HotmartErro as e:
        return {'estado': 'NAO_CONSEGUI_MEDIR', 'motivo': str(e), 'faltam': [], 'silencio': res['silencio']}
    recebidas = b.compras_confirmadas_sha(janela_ini - 30 * 86400)
    faltam = []
    for v in vendas:
        ap = v['aprovado_em_ms']
        if ap is None:
            return {'estado': 'NAO_CONSEGUI_MEDIR', 'motivo': 'vendas:aprovacao_sem_data', 'faltam': [],
                    'silencio': res['silencio']}
        if not (janela_ini * 1000 <= ap <= limite * 1000):
            continue
        sha = nz.sha256(v['transacao'])
        if sha not in recebidas:
            faltam.append({'hash8': sha[:8], 'produto': v['produto_id'], 'aprovado_em': ap // 1000})
    res['comparacao'] = 'feita'
    res['vendas_na_janela'] = len(vendas)
    if faltam:
        res['estado'] = 'BURACO'
        res['faltam'] = sorted(faltam, key=lambda x: x['aprovado_em'])
        mais_antiga = res['faltam'][0]['aprovado_em']
        res['webhook_desativado_provavel'] = ultimo is None or ultimo < mais_antiga
    return res


def rodar(perfil, b=None, cliente=None, agora=None):
    b = b or bco.Banco(perfil['dados_dir'])
    res = medir(perfil, b, cliente, agora)
    est = _estado(b)
    avisos = []
    if res['estado'] == 'NAO_CONSEGUI_MEDIR':
        est['falhas_seguidas'] = int(est.get('falhas_seguidas') or 0) + 1
        if est['falhas_seguidas'] == FALHAS_PARA_AVISAR:
            avisos.append({'tipo': 'vigia_nao_mede', 'motivo': res['motivo'], 'rodadas': est['falhas_seguidas']})
    else:
        est['falhas_seguidas'] = 0
    avisados = set(est.get('avisados') or [])
    novos = [f for f in res.get('faltam', []) if f['hash8'] not in avisados]
    if novos:
        avisos.append({'tipo': 'venda_sem_webhook', 'quantas': len(novos), 'vendas': novos,
                       'webhook_desativado_provavel': res.get('webhook_desativado_provavel', False)})
        avisados.update(f['hash8'] for f in novos)
    if res.get('silencio') and not est.get('silencio_avisado'):
        avisos.append({'tipo': 'webhook_em_silencio', 'horas': perfil['vigia_silencio_h']})
        est['silencio_avisado'] = True
    if not res.get('silencio'):
        est['silencio_avisado'] = False
    est['avisados'] = sorted(avisados)[-5000:]
    entrega = [avisar(perfil, {'origem': 'hotmart-meta-vigia', **a}) for a in avisos]
    _gravar_estado(b, est)
    log('rodada', estado=res['estado'], faltam=len(res.get('faltam', [])), novos=len(novos),
        motivo=res.get('motivo'), comparacao=res.get('comparacao'), avisos=','.join(entrega) or None)
    rc = {'COBERTO': RC_COBERTO, 'BURACO': RC_BURACO}.get(res['estado'], RC_NAO_MEDIU)
    return rc, res


def main():
    os.umask(0o077)
    try:
        perfil = config.carregar()
    except config.PerfilRecusado as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        return 78
    rc, res = rodar(perfil)
    print(json.dumps(res, ensure_ascii=False))
    return rc


if __name__ == '__main__':
    sys.exit(main())
