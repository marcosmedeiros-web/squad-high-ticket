"""Rede vista de fora: um salto HTTP sem seguir redirecionamento, com certificado conferido, e DNS por resolvedor
publico (DNS sobre HTTPS), nunca o resolvedor local da VPS (cache e /etc/hosts mentem nos dois sentidos).

Os testes trocam `HOP` e `DOH` por funcoes falsas; o codigo de producao nao tem desvio de teste.
"""
import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

DOH_URL = 'https://dns.google/resolve'
TIPOS = {'A': 1, 'CNAME': 5, 'MX': 15, 'TXT': 16, 'AAAA': 28}


class _SemRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def hop_real(url, metodo='GET', timeout=15):
    ctx = ssl.create_default_context()
    abridor = urllib.request.build_opener(_SemRedirect, urllib.request.HTTPSHandler(context=ctx))
    req = urllib.request.Request(url, method=metodo, headers={'User-Agent': 'email-marketing-conferencia/1.0'})
    try:
        with abridor.open(req, timeout=timeout) as r:
            return {'classe': 'resposta', 'codigo': r.status, 'headers': dict(r.headers),
                    'corpo': r.read(65536).decode('utf-8', errors='replace')}
    except urllib.error.HTTPError as e:
        return {'classe': 'resposta', 'codigo': e.code, 'headers': dict(e.headers or {}),
                'corpo': (e.read(65536) or b'').decode('utf-8', errors='replace')}
    except ssl.SSLError as e:
        return {'classe': 'erro', 'erro': 'tls:' + type(e).__name__}
    except (urllib.error.URLError, OSError) as e:
        motivo = getattr(e, 'reason', e)
        if isinstance(motivo, ssl.SSLError):
            return {'classe': 'erro', 'erro': 'tls:' + type(motivo).__name__}
        return {'classe': 'erro', 'erro': type(motivo).__name__}


def doh_real(nome, tipo, timeout=10):
    """-> lista de valores (strings) ou None quando NAO mediu. Lista vazia = mediu e nao existe."""
    q = urllib.parse.urlencode({'name': nome, 'type': tipo})
    try:
        with urllib.request.urlopen(f'{DOH_URL}?{q}', timeout=timeout) as r:
            d = json.loads(r.read().decode())
    except (OSError, ValueError):
        return None
    if d.get('Status') not in (0, 3):
        return None
    alvo = TIPOS[tipo]
    out = []
    for a in d.get('Answer') or []:
        if a.get('type') == alvo:
            v = a.get('data', '')
            if tipo == 'TXT':
                v = ''.join(p for p in v.split('"') if p.strip() not in ('',)) if '"' in v else v
            out.append(v.rstrip('.') if tipo in ('CNAME', 'MX') else v)
    return out


HOP = hop_real
DOH = doh_real


def hop(url, metodo='GET', timeout=15):
    return HOP(url, metodo=metodo, timeout=timeout)


def doh(nome, tipo):
    return DOH(nome, tipo)
