"""Gestor: segmentos e criacao do e-mail no Mautic. Quem ESCREVE e o copywriter, quem revisa e o revisor;
aqui o texto aprovado vira um e-mail de segmento DESPUBLICADO. Criar nunca envia (ver disparo.py)."""
import json
import os

from . import copy_risco
from .disparo import codigo_do_email, conferir_email
from .saida import Recusa, info, motivo


def segmentos_listar(api):
    st, d = api.get('/api/segments', {'limit': 200, 'minimal': 'true'})
    if st != 200 or 'lists' not in d:
        raise Recusa('api_segmentos_ilegivel', rc=2, http=st)
    lst = d['lists'].values() if isinstance(d['lists'], dict) else d['lists']
    n = 0
    for s in sorted(lst, key=lambda x: int(x.get('id', 0))):
        n += 1
        info(f"{s.get('id')}\t{s.get('alias')}\t{s.get('name')}\tpublicado={s.get('isPublished')}")
    return motivo('ok', 0, segmentos=n)


def segmento_criar(perfil, api, arquivo):
    with open(os.path.expanduser(arquivo), encoding='utf-8') as f:
        corpo = json.load(f)
    for k in ('name', 'filters'):
        if k not in corpo:
            raise Recusa('segmento_sem_campo', rc=3, campo=k)
    corpo.setdefault('isPublished', True)
    if perfil.modo() == 'seco':
        info(f"SECO: faria POST /api/segments/new nome={corpo['name']} filtros={len(corpo['filters'])}")
        return motivo('seco_nada_criado', 0)
    st, d = api.post_json('/api/segments/new', corpo)
    if st not in (200, 201) or 'list' not in d:
        raise Recusa('segmento_nao_criado', rc=1, http=st)
    return motivo('segmento_criado', 0, id=d['list'].get('id'))


def email_criar(perfil, api, nome, assunto, html_arquivo, segmento, preheader=None):
    with open(os.path.expanduser(html_arquivo), encoding='utf-8') as f:
        html = f.read()
    corpo = {'name': nome, 'subject': assunto, 'customHtml': html, 'emailType': 'list',
             'lists': [int(segmento)], 'isPublished': False}
    if preheader:
        corpo['preheaderText'] = preheader
    itens = [i for i in conferir_email(perfil, corpo) if i[0] != 'sem_agendamento']
    for n, ok, det in itens:
        info(f"[{'ok' if ok else 'falhou'}] {n} {det}")
    if not all(ok for _, ok, _ in itens):
        return motivo('email_reprovado_antes_de_criar', 1, item=[n for n, ok, _ in itens if not ok][0])
    copy_risco.guarda_envio(perfil['EMK_ESP'], assunto, html, 'criar')
    if perfil.modo() == 'seco':
        info(f'SECO: faria POST /api/emails/new (segmento {segmento}, despublicado), codigo {codigo_do_email(corpo)}')
        return motivo('seco_nada_criado', 0)
    st, d = api.post_json('/api/emails/new', corpo)
    if st not in (200, 201) or 'email' not in d:
        raise Recusa('email_nao_criado', rc=1, http=st)
    eid = d['email'].get('id')
    info(f'criado despublicado. Proximo: email-mkt disparo plano --email-id {eid}')
    return motivo('email_criado', 0, email_id=eid)
