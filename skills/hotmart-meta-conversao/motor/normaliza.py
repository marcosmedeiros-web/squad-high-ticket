"""normaliza.py: normalização de dado pessoal no formato que a API de Conversões da Meta pede, e o hash.

Regras da Meta (Customer Information Parameters, conferido em 18/10/2026; ver references/fontes.md):
  em        sem espaço nas pontas, minúsculo, SHA-256
  ph        só dígitos, COM o código do país, sem zero à esquerda, SHA-256
  fn, ln    minúsculo, sem pontuação, UTF-8, SHA-256
  ct        minúsculo, sem pontuação e sem espaço, SHA-256
  st        minúsculo, sem pontuação e sem espaço, SHA-256
  zp        minúsculo, sem espaço e sem hífen, SHA-256
  country   ISO 3166-1 alfa-2 minúsculo, SHA-256
  client_ip_address, client_user_agent, fbp, fbc   NUNCA em hash

Telefone da Hotmart (gotcha medido na documentação dela):
  * na compra, `checkout_phone` vem sem o DDD quando `checkout_phone_code` existe (exemplo oficial: "999999999"
    e "31"); fora do Brasil o DDI vem junto do número;
  * no abandono, `phone` vem com DDD e sem o 55 (exemplo oficial: "31999999999").
  Por isso o 55 só é posto quando o país é BR (ou não veio) e o número tem 10 ou 11 dígitos.
"""
import hashlib
import hmac
import re
import unicodedata

_RE_EMAIL = re.compile(r'^[^@\s]{1,64}@[^@\s]{1,255}\.[a-z]{2,24}$')


def sha256(v):
    return hashlib.sha256(v.encode('utf-8')).hexdigest()


def email(v):
    if not isinstance(v, str):
        return None
    e = v.strip().lower()
    return e if _RE_EMAIL.match(e) else None


def telefone(numero, ddd=None, pais_iso=None):
    """-> só dígitos com código do país, ou None quando não dá para montar com segurança."""
    if not isinstance(numero, (str, int)):
        return None
    d = re.sub(r'\D', '', str(numero))
    dd = re.sub(r'\D', '', str(ddd)) if ddd is not None else ''
    pais = (pais_iso or '').strip().upper()
    if dd and len(d) in (8, 9) and len(dd) == 2:
        d = dd + d
    d = d.lstrip('0')
    if pais in ('', 'BR'):
        if len(d) in (10, 11):
            d = '55' + d
        elif not (d.startswith('55') and len(d) in (12, 13)):
            return None
    if not (8 <= len(d) <= 15):
        return None
    return d


def _so_letras(v, manter_espaco=False):
    if not isinstance(v, str):
        return None
    s = unicodedata.normalize('NFC', v.strip().lower())
    s = ''.join(ch for ch in s if ch.isalpha() or (manter_espaco and ch == ' '))
    return s or None


def nome(v):
    return _so_letras(v)


def cidade(v):
    return _so_letras(v)


def uf(v):
    return _so_letras(v)


def cep(v):
    if not isinstance(v, (str, int)):
        return None
    s = re.sub(r'[\s-]', '', str(v)).lower()
    return s if re.fullmatch(r'[a-z0-9]{3,10}', s) else None


def pais(v):
    if not isinstance(v, str):
        return None
    s = v.strip().lower()
    return s if re.fullmatch(r'[a-z]{2}', s) else None


def hmac_local(chave, valor):
    """Digital local (HMAC-SHA256 com a chave do próprio receptor). Serve só para juntar abandono e compra
    da mesma pessoa sem guardar o contato em claro na tabela de compras."""
    if not valor:
        return None
    return hmac.new(chave, valor.encode('utf-8'), hashlib.sha256).hexdigest()
