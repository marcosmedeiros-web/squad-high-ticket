"""Leitura de uma mensagem REAL entregue (arquivo .eml salvo da caixa do dono): a prova de fora.

O que se confere e o que chegou, nao a config: DKIM assinado pelo dominio do dono, DMARC, qual servico entregou,
List-Unsubscribe de um clique apontando para o endereco publico com HTTPS, e os links de descadastro, de "ver no
navegador" e de clique rastreado no mesmo endereco. Link embrulhado pelo rastreio do proprio servico de envio
(SendGrid, por exemplo) reprova: na origem ele confundiu o diagnostico do opt-in.

Nada aqui segue link. Visitar o link de rastreio conta clique e suja a metrica.
"""
import email
import email.policy
import re
from html.parser import HTMLParser


class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for k, v in attrs:
                if k.lower() == 'href' and v:
                    self.hrefs.append(v.strip())


def _html(msg):
    for parte in msg.walk():
        if parte.get_content_type() == 'text/html':
            try:
                return parte.get_content()
            except Exception:  # noqa: BLE001
                return parte.get_payload(decode=True).decode('utf-8', errors='replace')
    return ''


def conferir_eml(dados, dominio_mautic, dominio_remetente, esp=None):
    """-> (ok: bool, itens: list[(nome, bool, detalhe)])."""
    msg = email.message_from_bytes(dados, policy=email.policy.default)
    itens = []
    ar = ' '.join(str(v) for v in (msg.get_all('Authentication-Results') or [])).lower()
    dom = dominio_remetente.lower()
    # O Gmail grava header.i=@dominio, os outros header.d=dominio. O lookahead recusa dominio.golpe.com, que o \b aceitava.
    assinatura = re.search(r'dkim=pass[^;]*header\.(?:d=|i=[^@\s;]*@)' + re.escape(dom) + r'(?![a-z0-9.-])[^;]*', ar)
    itens.append(('dkim_pass_do_dominio', bool(assinatura), f'header.d={dom}'))
    itens.append(('dmarc_pass', 'dmarc=pass' in ar, ''))
    # O seletor vem da assinatura do dominio: o Gmail lista tambem a do servico de envio, e ela pode vir primeiro.
    sel = re.search(r'header\.s=([a-z0-9._-]+)', assinatura.group(0)) if assinatura else None
    seletor = sel.group(1) if sel else ''
    received = ' '.join(str(v) for v in (msg.get_all('Received') or [])).lower()
    if esp:
        if esp == 'resend':
            quem = seletor == 'resend'
        elif esp == 'sendgrid':
            quem = bool(msg.get('X-SG-EID')) or 'sendgrid.net' in received
        else:
            quem = 'amazonses.com' in received and seletor != 'resend'
        itens.append(('entregue_pelo_servico_esperado', quem, f'esp={esp} seletor={seletor or "-"}'))
    base = f'https://{dominio_mautic.lower()}/'
    lu = str(msg.get('List-Unsubscribe') or '')
    lu_https = [u for u in re.findall(r'<([^>]+)>', lu) if u.lower().startswith('http')]
    itens.append(('list_unsubscribe_https_no_endereco_publico', bool(lu_https) and all(
        u.lower().startswith(base) for u in lu_https), 'cabecalho List-Unsubscribe'))
    itens.append(('list_unsubscribe_um_clique', 'one-click' in str(msg.get('List-Unsubscribe-Post') or '').lower(),
                  'List-Unsubscribe-Post'))
    p = _Links()
    p.feed(_html(msg))
    hrefs = [h for h in p.hrefs if h.lower().startswith('http')]
    descad = [h for h in hrefs if '/email/unsubscribe/' in h.lower()]
    itens.append(('link_descadastro_https_publico', bool(descad) and all(h.lower().startswith(base) for h in descad),
                  f'{len(descad)} link(s)'))
    fora = [h for h in hrefs if not h.lower().startswith(base)]
    itens.append(('links_sem_embrulho_do_servico', not fora,
                  f'{len(fora)} link(s) fora do endereco publico' if fora else 'todos no endereco publico'))
    restos = re.findall(r'\{[a-z_]+\}', _html(msg))
    itens.append(('sem_token_nao_resolvido', not restos, ','.join(sorted(set(restos)))[:80]))
    return all(ok for _, ok, _ in itens), itens
