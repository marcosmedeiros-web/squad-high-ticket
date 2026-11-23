"""Modulo (b): disparo de e-mail para segmento, no procedimento medido na operacao de origem.

Fatos do Mautic 7.1.2 que mandam neste desenho (medidos na fonte e em envio real):
- o UNICO gatilho de e-mail de segmento e `POST /api/emails/<id>/send`. Publicar nao envia; agendar por data
  tambem nao envia, porque o cron padrao da imagem nao roda `broadcasts:send`;
- o POST enfileira o lote inteiro dentro da propria requisicao e o worker drena em segundos: DEPOIS DO POST NAO HA
  FREIO. Despublicar nao tira nada da fila. Por isso o lote piloto (`limit`) vem antes do resto;
- a regua de destinatarios e a busca `email_pending:<id>`, a mesma consulta que o envio usa;
- quem entra no segmento depois do envio NAO recebe; o segundo POST so pega quem ainda esta pendente (sem duplicar).

Sequencia (cada passo exige o codigo do plano; mudou uma letra do e-mail depois do OK, o codigo muda e nada sai):
  plano  -> canario (so o contato do dono) -> lote piloto (limit) -> conferencia -> resto -> despublicado
Todo POST de segmento passa pela guarda do HTTPS (selo + medicao ao vivo). O modo do perfil manda:
  seco    = roda todas as conferencias e para antes de qualquer POST (padrao)
  canario = permite so o envio individual ao contato do dono
  lista   = permite o segmento, sempre atras da guarda do HTTPS
"""
import hashlib
import json
import os
import re
import time

from . import copy_risco, https_mod
from .saida import Recusa, info, motivo


def _registro_path(perfil, eid):
    d = os.path.join(perfil.estado_dir(), 'disparos', str(int(eid)))
    os.makedirs(d, mode=0o700, exist_ok=True)
    return os.path.join(d, 'registro.json')


def _ler(perfil, eid):
    try:
        with open(_registro_path(perfil, eid), encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _gravar(perfil, eid, reg):
    p = _registro_path(perfil, eid)
    fd = os.open(p + '.tmp', os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as f:
        json.dump(reg, f, indent=1, sort_keys=True)
    os.replace(p + '.tmp', p)


def _listas(e):
    out = []
    for x in e.get('lists') or []:
        out.append(int(x['id']) if isinstance(x, dict) else int(x))
    return sorted(out)


def codigo_do_email(e):
    base = {k: e.get(k) for k in ('subject', 'customHtml', 'fromAddress', 'fromName', 'replyToAddress',
                                  'emailType', 'preheaderText')}
    base['lists'] = _listas(e)
    return hashlib.sha256(json.dumps(base, sort_keys=True).encode()).hexdigest()[:10]


def _norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s or '')).strip().lower()


def conferir_email(perfil, e):
    """-> lista de (item, ok, detalhe). Nao toca rede."""
    html = e.get('customHtml') or ''
    itens = [
        ('tipo_segmento', e.get('emailType') == 'list', f"emailType={e.get('emailType')}"),
        ('tem_segmento', bool(_listas(e)), f'segmentos={_listas(e)}'),
        ('sem_agendamento', not e.get('publishUp'), 'agendar por data nao envia nesta instalacao'),
        ('descadastro_em_link', bool(re.search(r'href\s*=\s*["\']\{unsubscribe_url\}', html)),
         'href="{unsubscribe_url}" (o token de texto sai no idioma errado)'),
        ('empresa_no_rodape', _norm(perfil['EMK_EMPRESA_NOME']) in _norm(html), 'nome da empresa'),
        ('endereco_no_rodape', _norm(perfil['EMK_EMPRESA_ENDERECO']) in _norm(html), 'endereco fisico'),
        ('sem_travessao', '\u2014' not in html and '\u2014' not in (e.get('subject') or ''), ''),
    ]
    return itens


def plano(perfil, api, eid):
    perfil.exigir('disparo')
    e = api.email(eid)
    itens = conferir_email(perfil, e)
    for nome, ok, det in itens:
        info(f"[{'ok' if ok else 'falhou'}] {nome} {det}")
    if not all(ok for _, ok, _ in itens):
        return motivo('email_reprovado_no_plano', 1, email_id=eid, item=[n for n, ok, _ in itens if not ok][0])
    risco = copy_risco.guarda_envio(perfil['EMK_ESP'], e.get('subject'), e.get('customHtml'), 'plano')
    pend = api.pendentes(eid)
    if pend == 0:
        return motivo('nada_pendente', 1, email_id=eid)
    cod = codigo_do_email(e)
    reg = {'email_id': int(eid), 'plano': {'codigo': cod, 'pendentes': pend, 'quando': int(time.time()),
                                           'copy_risco': risco, 'esp': perfil['EMK_ESP']}}
    _gravar(perfil, eid, reg)
    info(f"assunto: {e.get('subject')}")
    info(f'destinatarios pendentes agora: {pend} (segmentos {_listas(e)})')
    info(f"proximo passo: email-mkt disparo canario --email-id {eid} --ok {cod}")
    return motivo('plano_pronto', 0, email_id=eid, pendentes=pend, codigo=cod)


def _checar_codigo(api, eid, ok, reg):
    if not reg.get('plano'):
        raise Recusa('sem_plano', rc=1, fazer=f'email-mkt disparo plano --email-id {eid}')
    if ok != reg['plano']['codigo']:
        raise Recusa('codigo_nao_e_o_do_plano', rc=1)
    e = api.email(eid)
    if codigo_do_email(e) != ok:
        raise Recusa('email_mudou_depois_do_ok', rc=1, fazer='refazer_o_plano_e_pedir_novo_OK')
    return e


def canario(perfil, api, eid, ok):
    perfil.exigir('disparo')
    reg = _ler(perfil, eid)
    e = _checar_codigo(api, eid, ok, reg)
    copy_risco.guarda_envio(perfil['EMK_ESP'], e.get('subject'), e.get('customHtml'), 'canario')
    cid = perfil.int('EMK_CANARIO_CONTATO_ID')
    if perfil.modo() == 'seco':
        info(f'SECO: faria POST /api/emails/{eid}/contact/{cid}/send (so o contato do dono)')
        return motivo('seco_nada_enviado', 0, passo='canario')
    st, d = api.post_json(f'/api/emails/{eid}/contact/{cid}/send', {})
    if st != 200 or not d.get('success'):
        raise Recusa('canario_recusado_pela_api', rc=1, http=st)
    reg['canario'] = {'codigo': ok, 'quando': int(time.time()), 'contato': cid}
    _gravar(perfil, eid, reg)
    info('o canario saiu. Abra a caixa do dono, salve a mensagem como .eml e rode:')
    info('  email-mkt https conferir --eml <arquivo.eml>   (libera a lista se tudo passar)')
    return motivo('canario_enviado', 0, email_id=eid)


def _pre_segmento(perfil, api, eid, ok, passo):
    perfil.exigir('disparo')
    reg = _ler(perfil, eid)
    e = _checar_codigo(api, eid, ok, reg)
    copy_risco.guarda_envio(perfil['EMK_ESP'], e.get('subject'), e.get('customHtml'), passo.replace(' ', '_'))
    https_mod.guarda(perfil)
    if perfil.modo() == 'seco':
        info('SECO: a guarda do HTTPS passou')
    elif (reg.get('canario') or {}).get('codigo') != ok:
        raise Recusa('canario_ausente_para_este_plano', rc=1, fazer=f'email-mkt disparo canario --email-id {eid}')
    if perfil.modo() == 'seco':
        info(f'SECO: guardas todas passaram; o POST de segmento ({passo}) nao foi feito')
        raise Recusa('seco_nada_enviado', rc=0, passo=passo.replace(' ', '_'))
    if perfil.modo() != 'lista':
        raise Recusa('modo_nao_permite_segmento', rc=1, modo=perfil.modo(), liberar='EMK_MODO=lista_no_perfil')
    return reg


def _enviar_segmento(api, eid, ok, limite):
    api.publicar(eid, True)
    try:
        e = api.email(eid)
        if codigo_do_email(e) != ok or not e.get('isPublished'):
            raise Recusa('portao_reprovado_apos_publicar', rc=1)
        dados = {'limit': str(limite)} if limite else {}
        info('POST de segmento: a partir daqui nao ha freio (o lote entra inteiro na fila)')
        st, d = api.post_form(f'/api/emails/{eid}/send', dados)
    finally:
        api.publicar(eid, False)
    if st != 200 or not d.get('success'):
        raise Recusa('envio_recusado_pela_api', rc=1, http=st)
    return int(d.get('sentCount', -1)), int(d.get('failedRecipients', -1))


def _falhas(api, eid):
    return sum(1 for s in api.stats(eid) if str(s.get('is_failed', '0')) not in ('0', 'False', 'false', ''))


def lote(perfil, api, eid, ok):
    reg = _pre_segmento(perfil, api, eid, ok, 'lote piloto')
    n = perfil.int('EMK_LOTE_PILOTO')
    if n < 1 or n > 50:
        raise Recusa('lote_piloto_fora_da_faixa', rc=3, faixa='1-50')
    antes = api.pendentes(eid)
    esperado = min(n, antes)
    enviados, falhos = _enviar_segmento(api, eid, ok, n)
    depois = api.pendentes(eid)
    falhas_stats = _falhas(api, eid)
    reg['lote'] = {'codigo': ok, 'quando': int(time.time()), 'enviados': enviados, 'falhos': falhos,
                   'pendentes_antes': antes, 'pendentes_depois': depois, 'falhas_stats': falhas_stats}
    reg['lote']['ok'] = enviados == esperado and falhos == 0 and falhas_stats == 0 and depois == antes - enviados
    _gravar(perfil, eid, reg)
    info(f'lote piloto: enviados {enviados} de {esperado}, falhas {falhos}, falhas nas estatisticas {falhas_stats}, '
         f'pendentes {antes} -> {depois}')
    if not reg['lote']['ok']:
        return motivo('lote_piloto_reprovado_resto_segurado', 1, email_id=eid)
    info(f'confira a primeira abertura e a caixa do dono; depois: email-mkt disparo resto --email-id {eid} --ok {ok}')
    return motivo('lote_piloto_ok', 0, email_id=eid, enviados=enviados)


def resto(perfil, api, eid, ok):
    reg = _pre_segmento(perfil, api, eid, ok, 'resto')
    lt = reg.get('lote') or {}
    if lt.get('codigo') != ok or not lt.get('ok'):
        raise Recusa('lote_piloto_ausente_ou_reprovado', rc=1, fazer=f'email-mkt disparo lote --email-id {eid}')
    if _falhas(api, eid):
        raise Recusa('falha_nas_estatisticas_desde_o_lote', rc=1)
    antes = api.pendentes(eid)
    if antes == 0:
        return motivo('nada_pendente', 0, email_id=eid)
    enviados, falhos = _enviar_segmento(api, eid, ok, None)
    depois = api.pendentes(eid)
    falhas_stats = _falhas(api, eid)
    reg['resto'] = {'codigo': ok, 'quando': int(time.time()), 'enviados': enviados, 'falhos': falhos,
                    'pendentes_antes': antes, 'pendentes_depois': depois, 'falhas_stats': falhas_stats}
    _gravar(perfil, eid, reg)
    info(f'resto: enviados {enviados} de {antes}, falhas {falhos}, falhas nas estatisticas {falhas_stats}, '
         f'pendentes agora {depois} (quem entrou no segmento depois do POST nao recebe)')
    if enviados != antes or falhos or falhas_stats:
        return motivo('resto_com_divergencia', 1, email_id=eid)
    return motivo('disparo_concluido', 0, email_id=eid, total=lt['enviados'] + enviados)


def estado(perfil, eid):
    reg = _ler(perfil, eid)
    info(json.dumps(reg, indent=1, sort_keys=True) if reg else 'sem registro')
    return motivo('estado', 0, email_id=eid)
