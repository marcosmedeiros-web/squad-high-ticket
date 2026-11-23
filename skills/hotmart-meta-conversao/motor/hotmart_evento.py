"""hotmart_evento.py: lê o corpo do webhook 2.0.0 da Hotmart e devolve SÓ os campos que o kit usa.

Lista branca, não lista negra: o payload de compra traz código de Pix, código de barras do boleto, CPF,
endereço completo e comissões. Nada disso é copiado. O que sai daqui é o mínimo para (1) deduplicar,
(2) montar o evento da API de Conversões e (3) dar à recuperação de carrinho o contato do abandono.

Nomes de evento (documentação oficial da Hotmart, webhook 2.0.0; ver references/fontes.md):
  compra:   PURCHASE_CANCELED, PURCHASE_COMPLETE, PURCHASE_BILLET_PRINTED, PURCHASE_APPROVED, PURCHASE_PROTEST,
            PURCHASE_REFUNDED, PURCHASE_CHARGEBACK, PURCHASE_EXPIRED, PURCHASE_DELAYED
  abandono: PURCHASE_OUT_OF_SHOPPING_CART  ("Outros: abandono de carrinho" no painel). NÃO é CHECKOUT_INITIATED
            nem PURCHASE_BILLET_PRINTED, que circulavam em guias antigos do kit.
Evento fora dessas listas não é erro de quem mandou: vai para a quarentena com 200, para a Hotmart não
desativar a URL, e aparece no `eventos.py status`.
"""
import json
import re

VERSAO_ACEITA = '2.0.0'
EVENTOS_COMPRA = frozenset({
    'PURCHASE_CANCELED', 'PURCHASE_COMPLETE', 'PURCHASE_BILLET_PRINTED', 'PURCHASE_APPROVED', 'PURCHASE_PROTEST',
    'PURCHASE_REFUNDED', 'PURCHASE_CHARGEBACK', 'PURCHASE_EXPIRED', 'PURCHASE_DELAYED'})
EVENTO_ABANDONO = 'PURCHASE_OUT_OF_SHOPPING_CART'
EVENTOS_COMPRA_CONFIRMADA = frozenset({'PURCHASE_APPROVED', 'PURCHASE_COMPLETE'})

_RE_NOME_EVENTO = re.compile(r'^[A-Z][A-Z0-9_]{2,60}$')
_RE_ID = re.compile(r'^[A-Za-z0-9-]{1,80}$')
_RE_PRODUTO = re.compile(r'^[0-9]{1,15}$')
_RE_TRANSACAO = re.compile(r'^[A-Z]{1,4}[0-9A-Z]{4,40}$')
_RE_STATUS = re.compile(r'^[A-Z_]{2,40}$')
_RE_CODIGO = re.compile(r'^[A-Za-z0-9_-]{1,40}$')
_RE_XCOD = re.compile(r'^[A-Za-z0-9_-]{8,64}$')
_RE_MOEDA = re.compile(r'^[A-Z]{3}$')


class EventoInvalido(ValueError):
    """Motivo curto e fechado; nunca leva trecho do corpo."""
    def __init__(self, motivo, nome_evento=None, versao=None):
        super().__init__(motivo)
        self.motivo = motivo
        self.nome_evento = nome_evento if isinstance(nome_evento, str) and _RE_NOME_EVENTO.match(nome_evento) else None
        self.versao = versao if isinstance(versao, str) and re.fullmatch(r'[0-9.]{1,10}', versao) else None


def _d(x, *chaves):
    for k in chaves:
        if not isinstance(x, dict):
            return None
        x = x.get(k)
    return x


def _txt(v, maximo=200):
    if isinstance(v, str):
        v = v.strip()
        return v[:maximo] if v else None
    return None


def _num(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str) and re.fullmatch(r'-?[0-9]{1,12}(\.[0-9]{1,6})?', v.strip()):
        return float(v)
    return None


def _ms(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, int) and v >= 0:
        return v
    if isinstance(v, str) and re.fullmatch(r'[0-9]{1,15}', v.strip()):
        return int(v)
    return None


def _codigo(v):
    return v if isinstance(v, str) and _RE_CODIGO.match(v) else None


def _produto(data):
    pid = _d(data, 'product', 'id')
    if isinstance(pid, bool) or not isinstance(pid, (int, str)):
        return None
    pid = str(pid).strip()
    return pid if _RE_PRODUTO.match(pid) else None


def ler(corpo_bytes):
    """-> dict normalizado. Levanta EventoInvalido(motivo)."""
    try:
        d = json.loads(corpo_bytes.decode('utf-8'))
    except (UnicodeDecodeError, ValueError):
        raise EventoInvalido('json_invalido') from None
    if not isinstance(d, dict):
        raise EventoInvalido('json_nao_objeto')
    nome, versao = d.get('event'), d.get('version')
    if not isinstance(nome, str) or not _RE_NOME_EVENTO.match(nome):
        raise EventoInvalido('evento_sem_nome', None, versao)
    if versao != VERSAO_ACEITA:
        raise EventoInvalido('versao_nao_suportada', nome, versao)
    eid = d.get('id')
    if isinstance(eid, int) and not isinstance(eid, bool):
        eid = str(eid)
    if not isinstance(eid, str) or not _RE_ID.match(eid):
        raise EventoInvalido('evento_sem_id', nome, versao)
    data = d.get('data')
    if not isinstance(data, dict):
        raise EventoInvalido('evento_sem_data', nome, versao)
    base = {'id': eid, 'evento': nome, 'versao': versao, 'criado_em_ms': _ms(d.get('creation_date')),
            'produto_id': _produto(data)}
    if base['produto_id'] is None:
        raise EventoInvalido('evento_sem_produto', nome, versao)
    if nome in EVENTOS_COMPRA:
        return _compra(base, data)
    if nome == EVENTO_ABANDONO:
        return _abandono(base, data)
    raise EventoInvalido('evento_fora_da_lista', nome, versao)


def _compra(base, data):
    compra = data.get('purchase')
    if not isinstance(compra, dict):
        raise EventoInvalido('compra_sem_purchase', base['evento'], base['versao'])
    tx = compra.get('transaction')
    if not isinstance(tx, str) or not _RE_TRANSACAO.match(tx.strip()):
        raise EventoInvalido('compra_sem_transacao', base['evento'], base['versao'])
    status = compra.get('status')
    rec = compra.get('recurrence_number')
    comprador = data.get('buyer') if isinstance(data.get('buyer'), dict) else {}
    pais_iso = _txt(_d(compra, 'checkout_country', 'iso'), 2) or _txt(_d(comprador, 'address', 'country_iso'), 2)
    xcod = _txt(_d(compra, 'origin', 'xcod'), 64)
    preco, cheio = compra.get('price') or {}, compra.get('full_price') or {}
    moeda_p, moeda_c = _txt(_d(preco, 'currency_value'), 3), _txt(_d(cheio, 'currency_value'), 3)
    base.update({
        'tipo': 'compra',
        'transacao': tx.strip(),
        'status': status if isinstance(status, str) and _RE_STATUS.match(status) else None,
        'aprovado_em_ms': _ms(compra.get('approved_date')),
        'recorrencia': rec if isinstance(rec, int) and not isinstance(rec, bool) and rec >= 0 else None,
        'valor_preco': _num(_d(preco, 'value')),
        'moeda_preco': moeda_p if moeda_p and _RE_MOEDA.match(moeda_p) else None,
        'valor_cheio': _num(_d(cheio, 'value')),
        'moeda_cheio': moeda_c if moeda_c and _RE_MOEDA.match(moeda_c) else None,
        'oferta': _codigo(_d(compra, 'offer', 'code')),
        'xcod': xcod if xcod and _RE_XCOD.match(xcod) else None,
        'order_bump': _d(compra, 'order_bump', 'is_order_bump') is True,
        'pais_iso': pais_iso,
        'comprador': {
            'email': _txt(comprador.get('email'), 254),
            'nome': _txt(comprador.get('first_name'), 100),
            'sobrenome': _txt(comprador.get('last_name'), 100),
            'nome_completo': _txt(comprador.get('name'), 200),
            'telefone': _txt(comprador.get('checkout_phone'), 30),
            'ddd': _txt(comprador.get('checkout_phone_code'), 5),
            'cidade': _txt(_d(comprador, 'address', 'city'), 100),
            'uf': _txt(_d(comprador, 'address', 'state'), 60),
            'cep': _txt(_d(comprador, 'address', 'zipcode'), 12),
        },
    })
    return base


def _abandono(base, data):
    comprador = data.get('buyer') if isinstance(data.get('buyer'), dict) else {}
    base.update({
        'tipo': 'abandono',
        'oferta': _codigo(_d(data, 'offer', 'code')),
        'afiliado': data.get('affiliate') is True,
        'pais_iso': _txt(_d(data, 'checkout_country', 'iso'), 2),
        'ip': _txt(data.get('buyer_ip'), 45),
        'comprador': {
            'nome_completo': _txt(comprador.get('name'), 200),
            'email': _txt(comprador.get('email'), 254),
            'telefone': _txt(comprador.get('phone'), 30),
        },
    })
    return base
