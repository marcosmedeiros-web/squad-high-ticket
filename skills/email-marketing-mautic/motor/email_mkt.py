#!/usr/bin/env python3
"""email-mkt: Mautic proprio com HTTPS publico, gestor de disparo e troca de servico de envio.

A ultima linha de todo comando e `MOTIVO=<codigo> ... rc=<n>` (0 ok, 1 reprovado/recusado, 2 nao mediu, 3 perfil).
O perfil vem de --perfil ou da variavel EMK_PERFIL. Nenhum comando imprime chave, senha ou DSN.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from emk import VERSAO, binlog, copy_risco, disparo, dns_mod, envio, gestor, https_mod, vigias  # noqa: E402
from emk.cabecalho import conferir_eml  # noqa: E402
from emk.descobrir import conferir_perfil, descobrir  # noqa: E402
from emk.mautic_api import Api  # noqa: E402
from emk.perfil import Perfil  # noqa: E402
from emk.saida import Recusa, info, motivo  # noqa: E402


def _args():
    ap = argparse.ArgumentParser(prog='email-mkt', description=__doc__.splitlines()[0])
    ap.add_argument('--perfil')
    ap.add_argument('--versao', action='store_true')
    sub = ap.add_subparsers(dest='grupo')

    p = sub.add_parser('perfil').add_subparsers(dest='acao')
    p.add_parser('conferir')
    d = sub.add_parser('descobrir')
    d.add_argument('--docker', default=None)

    h = sub.add_parser('https').add_subparsers(dest='acao')
    c = h.add_parser('caddy')
    c.add_argument('--modo', required=True, choices=('container', 'host'))
    c.add_argument('--upstream', required=True)
    c.add_argument('--saida')
    c = h.add_parser('conferir')
    c.add_argument('--eml')
    c = h.add_parser('site-url')
    c.add_argument('--aplicar', action='store_true')

    n = sub.add_parser('dns').add_subparsers(dest='acao')
    n.add_parser('conferir')

    e = sub.add_parser('envio').add_subparsers(dest='acao')
    e.add_parser('mostrar')
    c = e.add_parser('aplicar')
    c.add_argument('--esp', choices=('ses', 'sendgrid', 'resend'))
    e.add_parser('reverter')
    e.add_parser('recuar')
    c = e.add_parser('teste')
    c.add_argument('--email-id', type=int, required=True)
    c = e.add_parser('conferir-eml')
    c.add_argument('--eml', required=True)

    s = sub.add_parser('segmentos').add_subparsers(dest='acao')
    s.add_parser('listar')
    c = s.add_parser('criar')
    c.add_argument('--arquivo', required=True)

    m = sub.add_parser('email').add_subparsers(dest='acao')
    c = m.add_parser('criar')
    for a in ('--nome', '--assunto', '--html'):
        c.add_argument(a, required=True)
    c.add_argument('--segmento', type=int, required=True)
    c.add_argument('--preheader')

    dp = sub.add_parser('disparo').add_subparsers(dest='acao')
    for a in ('plano', 'canario', 'lote', 'resto', 'estado'):
        c = dp.add_parser(a)
        c.add_argument('--email-id', type=int, required=True)
        if a in ('canario', 'lote', 'resto'):
            c.add_argument('--ok', required=True)

    b = sub.add_parser('binlog').add_subparsers(dest='acao')
    b.add_parser('conferir')
    c = b.add_parser('aplicar')
    c.add_argument('--executar', action='store_true')

    v = sub.add_parser('vigia').add_subparsers(dest='acao')
    v.add_parser('cron')
    v.add_parser('disco')
    return ap


def principal(argv=None):
    a = _args().parse_args(argv)
    if a.versao:
        info(VERSAO)
        return motivo('versao', 0)
    if a.grupo == 'descobrir':
        return descobrir((a.docker or os.environ.get('EMK_DOCKER') or 'docker').split())
    if not a.grupo or not getattr(a, 'acao', None):
        _args().print_help()
        return motivo('uso', 3)
    pf = Perfil.carregar(a.perfil)
    g, ac = a.grupo, a.acao
    if g == 'perfil':
        return conferir_perfil(pf)
    if g == 'https':
        if ac == 'caddy':
            return https_mod.gerar_caddy(pf, a.modo, a.upstream, a.saida)
        if ac == 'conferir':
            return https_mod.conferir(pf, a.eml)
        return https_mod.site_url(pf, a.aplicar)
    if g == 'dns':
        return dns_mod.conferir(pf)
    if g == 'envio':
        if ac == 'mostrar':
            return envio.mostrar(pf)
        if ac == 'aplicar':
            return envio.aplicar(pf, a.esp)
        if ac == 'reverter':
            return envio.reverter(pf)
        if ac == 'recuar':
            return envio.recuar(pf)
        if ac == 'teste':
            pf.exigir('disparo')
            cid = pf.int('EMK_CANARIO_CONTATO_ID')
            api = Api.do_perfil(pf)
            em = api.email(a.email_id)
            copy_risco.guarda_envio(pf['EMK_ESP'], em.get('subject'), em.get('customHtml'), 'teste')
            if pf.modo() == 'seco':
                info(f'SECO: faria POST /api/emails/{a.email_id}/contact/{cid}/send')
                return motivo('seco_nada_enviado', 0)
            st, d = api.post_json(f'/api/emails/{a.email_id}/contact/{cid}/send', {})
            if st != 200 or not d.get('success'):
                return motivo('teste_recusado_pela_api', 1, http=st)
            info('saiu para o contato do dono. Salve a mensagem como .eml e rode: email-mkt envio conferir-eml --eml X')
            return motivo('teste_enviado', 0)
        with open(os.path.expanduser(a.eml), 'rb') as f:
            ok, itens = conferir_eml(f.read(), pf['EMK_DOMINIO_MAUTIC'], pf['EMK_DOMINIO_REMETENTE'], pf['EMK_ESP'])
        for nome, bom, det in itens:
            info(f"[{'ok' if bom else 'falhou'}] {nome} {det}")
        return motivo('eml_ok' if ok else 'eml_reprovado', 0 if ok else 1)
    if g == 'segmentos':
        api = Api.do_perfil(pf)
        return gestor.segmentos_listar(api) if ac == 'listar' else gestor.segmento_criar(pf, api, a.arquivo)
    if g == 'email':
        return gestor.email_criar(pf, Api.do_perfil(pf), a.nome, a.assunto, a.html, a.segmento, a.preheader)
    if g == 'disparo':
        if ac == 'estado':
            return disparo.estado(pf, a.email_id)
        api = Api.do_perfil(pf)
        if ac == 'plano':
            return disparo.plano(pf, api, a.email_id)
        return getattr(disparo, ac)(pf, api, a.email_id, a.ok)
    if g == 'binlog':
        return binlog.conferir(pf) if ac == 'conferir' else binlog.aplicar(pf, a.executar)
    if g == 'vigia':
        return vigias.vigia_cron(pf) if ac == 'cron' else vigias.vigia_disco(pf)
    return motivo('uso', 3)


def main(argv=None):
    try:
        return principal(argv)
    except Recusa as r:
        return motivo(r.codigo, r.rc, **r.kv)
    except KeyboardInterrupt:
        return motivo('interrompido', 2)


if __name__ == '__main__':
    sys.exit(main())
