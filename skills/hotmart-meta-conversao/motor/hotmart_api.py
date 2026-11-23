"""hotmart_api.py: leitura mínima de vendas da API da Hotmart, só para o vigia comparar com o webhook.

Mesma disciplina do leitor que já roda em produção há semanas:
  * o ÚNICO POST é o do token (client_credentials), que não muda nada na conta; o token vive só em memória;
  * dado só por GET, só em /payments/api/v1/sales/history, host fixo; qualquer outra rota recusa antes da rede;
  * erro leva só etapa, código HTTP e nome de classe de exceção; nunca corpo (venda tem dado pessoal), nunca a
    URL do token (ela leva o client_secret na query, que é o formato que a Hotmart aceita);
  * paginação completa por IDENTIDADE: transação repetida entre páginas, item sem código ou total que muda no
    meio da leitura = leitura incompleta, nunca "nenhuma venda".

Gotchas medidos na API real e embutidos aqui:
  * o filtro de data do sales/history é pela data do PEDIDO, não da aprovação (boleto aprovado 2 a 5 dias depois
    só aparece na janela do pedido). O vigia lê uma janela maior que a de comparação;
  * sem `transaction_status`, só voltam APPROVED e COMPLETE. É o que o vigia quer.
"""
import json
import re
import urllib.error
import urllib.parse
import urllib.request

import segredo

URL_TOKEN = 'https://api-sec-vlc.hotmart.com/security/oauth/token'
HOST = 'https://developers.hotmart.com'
ROTA_VENDAS = '/payments/api/v1/sales/history'
_RE_TRANSACAO = re.compile(r'^[A-Z]{1,4}[0-9A-Z]{4,40}$')


class HotmartErro(RuntimeError):
    pass


def _rede(req, timeout):
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:   # noqa: S310 (host fixo)
            return r.status, r.read(20_000_000)
    except urllib.error.HTTPError as e:
        return e.code, b''


class Cliente:
    def __init__(self, cred_arquivo, abrir=None, timeout=45.0):
        self._cred = cred_arquivo
        self._abrir = abrir or _rede
        self._timeout = timeout
        self._token = None

    def __repr__(self):
        return 'Cliente(token=%s)' % ('em memória' if self._token else 'nenhum')

    def _obter_token(self):
        if self._token:
            return self._token
        try:
            c = segredo.ler(self._cred, ['HOTMART_CLIENT_ID', 'HOTMART_CLIENT_SECRET', 'HOTMART_BASIC'])
        except segredo.SegredoErro as e:
            raise HotmartErro(f'credencial:{e.motivo}') from None
        q = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': c['HOTMART_CLIENT_ID'],
                                    'client_secret': c['HOTMART_CLIENT_SECRET']})
        req = urllib.request.Request(f'{URL_TOKEN}?{q}', data=b'', method='POST',
                                     headers={'Authorization': f'Basic {c["HOTMART_BASIC"]}',
                                              'Accept': 'application/json'})
        del c, q
        try:
            st, corpo = self._abrir(req, self._timeout)
        except Exception as e:                                       # noqa: BLE001
            raise HotmartErro(f'token:rede:{type(e).__name__}') from None
        if st != 200:
            raise HotmartErro(f'token:http{st}')
        try:
            tok = json.loads(corpo.decode('utf-8', 'replace')).get('access_token')
        except (ValueError, AttributeError):
            raise HotmartErro('token:json') from None
        if not isinstance(tok, str) or not tok:
            raise HotmartErro('token:sem_access_token')
        self._token = tok
        return tok

    def _get(self, rota, params):
        if rota != ROTA_VENDAS:
            raise HotmartErro('rota_fora_da_lista')
        req = urllib.request.Request(f'{HOST}{rota}?{urllib.parse.urlencode(params)}', method='GET',
                                     headers={'Authorization': f'Bearer {self._obter_token()}',
                                              'Accept': 'application/json'})
        try:
            st, corpo = self._abrir(req, self._timeout)
        except Exception as e:                                       # noqa: BLE001
            raise HotmartErro(f'vendas:rede:{type(e).__name__}') from None
        if st != 200:
            raise HotmartErro(f'vendas:http{st}')
        try:
            d = json.loads(corpo.decode('utf-8', 'replace'))
        except ValueError:
            raise HotmartErro('vendas:json') from None
        if not isinstance(d, dict):
            raise HotmartErro('vendas:esquema')
        return d

    def vendas_confirmadas(self, inicio_ms, fim_ms, produto=None, max_paginas=200):
        """-> lista de {transacao, produto_id, aprovado_em_ms}. Levanta HotmartErro se a leitura não fechou."""
        params = {'start_date': int(inicio_ms), 'end_date': int(fim_ms), 'max_results': 500}
        if produto:
            params['product_id'] = produto
        vistos, saida, total, tokens = set(), [], None, set()
        for _ in range(max_paginas):
            d = self._get(ROTA_VENDAS, params)
            itens, info = d.get('items'), d.get('page_info') or {}
            if not isinstance(itens, list) or not isinstance(info, dict):
                raise HotmartErro('vendas:esquema')
            t = info.get('total_results')
            if not isinstance(t, int) or isinstance(t, bool):
                raise HotmartErro('vendas:sem_total')
            if total is None:
                total = t
            elif t != total:
                raise HotmartErro('vendas:total_mudou')
            for it in itens:
                compra = it.get('purchase') if isinstance(it, dict) else None
                tx = compra.get('transaction') if isinstance(compra, dict) else None
                if not isinstance(tx, str) or not _RE_TRANSACAO.match(tx):
                    raise HotmartErro('vendas:item_sem_transacao')
                if tx in vistos:
                    raise HotmartErro('vendas:transacao_repetida')
                vistos.add(tx)
                pid = (it.get('product') or {}).get('id')
                ap = compra.get('approved_date')
                saida.append({'transacao': tx, 'produto_id': str(pid) if pid is not None else None,
                              'aprovado_em_ms': ap if isinstance(ap, int) and not isinstance(ap, bool) else None,
                              'status': compra.get('status')})
            prox = info.get('next_page_token')
            if not prox:
                if total != len(saida):
                    raise HotmartErro('vendas:contagem_nao_fecha')
                return saida
            if not isinstance(prox, str) or prox in tokens:
                raise HotmartErro('vendas:laco_de_paginacao')
            tokens.add(prox)
            params['page_token'] = prox
        raise HotmartErro('vendas:paginas_demais')
