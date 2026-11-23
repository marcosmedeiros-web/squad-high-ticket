"""Conferencia do DNS do remetente, por resolvedor publico (de fora).

Regras que vem de incidente ou de medicao na operacao de origem:
- UM registro SPF na raiz. Somar servico e EDITAR o registro que existe; criar um segundo invalida os dois
  (RFC 7208, permerror) e o e-mail de trabalho do dono vai para o spam em silencio.
- Registro de DKIM com proxy da Cloudflare ligado quebra o DKIM: o CNAME some e aparece IP da Cloudflare.
- DMARC tem que existir (Gmail e Yahoo exigem de quem manda volume). `p=none` passa, com aviso.
- Este comando so LE. Quem edita o DNS e o dono (ou o agente com a credencial do DNS do dono).
"""
import re

from . import rede
from .saida import info, motivo

_LOOKUP = re.compile(r'^(include:|a$|a:|a/|mx$|mx:|mx/|ptr|exists:|redirect=)', re.I)


def _spf(dom):
    txt = rede.doh(dom, 'TXT')
    if txt is None:
        return [('spf_raiz', 'nao_medido', 'resolvedor publico nao respondeu')]
    spfs = [t for t in txt if t.lower().startswith('v=spf1')]
    if len(spfs) > 1:
        return [('spf_raiz', 'falhou', f'{len(spfs)} registros SPF na raiz: junte num so (RFC 7208)')]
    if not spfs:
        return [('spf_raiz', 'aviso', 'sem SPF na raiz; o alinhamento fica so pelo DKIM')]
    termos = spfs[0].split()[1:]
    n = sum(1 for t in termos if _LOOKUP.match(t.lstrip('+-~?')))
    est = 'falhou' if n > 10 else 'ok'
    return [('spf_raiz', est, f'1 registro, {n} consultas diretas (limite 10, sem contar as aninhadas)')]


def _cname_ou_proxy(nome, sufixo):
    c = rede.doh(nome, 'CNAME')
    if c is None:
        return 'nao_medido', 'resolvedor publico nao respondeu'
    if any(v.lower().endswith(sufixo) for v in c):
        return 'ok', c[0]
    a = rede.doh(nome, 'A') or []
    if a:
        return 'falhou', 'responde IP em vez de CNAME: proxy ligado no DNS? DKIM tem que ficar sem proxy'
    return 'falhou', 'registro ausente'


def _dkim(perfil, dom, esp):
    itens = []
    if esp == 'resend':
        t = rede.doh(f'resend._domainkey.{dom}', 'TXT')
        if t is None:
            itens.append(('dkim', 'nao_medido', ''))
        else:
            itens.append(('dkim', 'ok' if any('p=' in v for v in t) else 'falhou', 'resend._domainkey'))
    elif esp == 'sendgrid':
        for s in ('s1', 's2'):
            est, det = _cname_ou_proxy(f'{s}._domainkey.{dom}', 'sendgrid.net')
            itens.append((f'dkim_{s}', est, det))
    else:
        toks = [t.strip() for t in (perfil.get('EMK_SES_DKIM_TOKENS') or '').split(',') if t.strip()]
        if len(toks) != 3:
            itens.append(('dkim', 'falhou', 'preencha EMK_SES_DKIM_TOKENS com os 3 tokens do Easy DKIM do SES'))
        for t in toks:
            est, det = _cname_ou_proxy(f'{t}._domainkey.{dom}', 'dkim.amazonses.com')
            itens.append((f'dkim_{t[:6]}', est, det))
    return itens


def _mailfrom(perfil, dom, esp):
    sub = perfil.get('EMK_MAILFROM_SUBDOMINIO') or ('send' if esp == 'resend' else '')
    if not sub:
        return []
    nome = f'{sub}.{dom}'
    t = rede.doh(nome, 'TXT')
    mx = rede.doh(nome, 'MX')
    if t is None or mx is None:
        return [('mail_from', 'nao_medido', nome)]
    ok = any(v.lower().startswith('v=spf1') for v in t) and bool(mx)
    return [('mail_from', 'ok' if ok else 'falhou', f'{nome}: SPF e MX do retorno')]


def _dmarc(dom):
    t = rede.doh(f'_dmarc.{dom}', 'TXT')
    if t is None:
        return [('dmarc', 'nao_medido', '')]
    d = [v for v in t if v.lower().startswith('v=dmarc1')]
    if not d:
        return [('dmarc', 'falhou', 'sem registro _dmarc (Gmail e Yahoo exigem de quem manda volume)')]
    pol = re.search(r'p=([a-z]+)', d[0].lower())
    if pol and pol.group(1) == 'none':
        return [('dmarc', 'aviso', 'p=none: monitora, nao protege; subir depois de 2 semanas limpas')]
    return [('dmarc', 'ok', d[0][:60])]


def conferir(perfil):
    perfil.exigir()
    dom = perfil['EMK_DOMINIO_REMETENTE']
    esp = perfil['EMK_ESP']
    itens = _spf(dom) + _dkim(perfil, dom, esp) + _mailfrom(perfil, dom, esp) + _dmarc(dom)
    for n, est, det in itens:
        info(f'[{est}] {n} {det}')
    if any(e == 'falhou' for _, e, _ in itens):
        return motivo('dns_reprovado', 1, dominio=dom, esp=esp)
    if any(e == 'nao_medido' for _, e, _ in itens):
        return motivo('dns_nao_medido', 2, dominio=dom)
    return motivo('dns_ok', 0, dominio=dom, esp=esp, avisos=sum(1 for _, e, _ in itens if e == 'aviso'))
