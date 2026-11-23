"""capi.py: monta o evento da API de Conversões da Meta e envia (transporte injetável para teste).

DEDUPLICAÇÃO CONTRA O PIXEL (documentação da Meta, "Deduplicate Pixel and Server Events", conferida em 18/10/2026)
  A Meta considera iguais dois eventos com o MESMO event_name e o MESMO event_id (no pixel, `eventID`, o quarto
  argumento do fbq), no mesmo pixel, em até 48 h. Por isso o event_id nunca é sorteado no servidor:
    * Purchase           event_id = "hm." + código da transação da Hotmart. O snippet do site usa a MESMA regra
                         na página de obrigado própria (`HMConversao.eventoCompraObrigado`).
    * clique de checkout event_id = o que o NAVEGADOR sorteou e já usou no fbq; chega ao servidor pelo aviso do
                         site (/v1/visita) e é repetido aqui sem mudança, junto com o mesmo event_name.
    * abandono           evento personalizado "CarrinhoAbandonado" (desligado por padrão), event_id =
                         "hm-abandono." + id do evento da Hotmart. Não tem par no navegador.

LIMITES DA META QUE VIRAM REGRA AQUI
  * event_time até 7 dias para trás; evento mais velho derruba o LOTE inteiro. Então cada requisição leva UM
    evento, e o que passou de 7 dias vira `velho_demais` sem chamada.
  * Purchase exige `currency` e `value` em custom_data. Compra sem os dois vira `rejeitado_local`.
  * client_user_agent é exigido para action_source=website. Sem a visita do site (sem navegador conhecido), a
    compra vai com CAPI_ORIGEM_SEM_NAVEGADOR (padrão "other").

O token NUNCA vai na URL nem em log: vai no corpo do POST (form), como no exemplo da Meta.
"""
import json
import time
import urllib.error
import urllib.parse
import urllib.request

import normaliza as nz

SETE_DIAS = 7 * 86400
MARGEM_VELHO = 600           # 10 min de folga antes do limite da Meta
EVENTO_ABANDONO_PERSONALIZADO = 'CarrinhoAbandonado'


class CapiErro(RuntimeError):
    pass


def event_id_compra(transacao):
    return 'hm.' + transacao


def _lista(v):
    return [v] if v else None


def user_data_compra(norm, visita=None):
    c = norm.get('comprador') or {}
    em = nz.email(c.get('email'))
    ph = nz.telefone(c.get('telefone'), c.get('ddd'), norm.get('pais_iso'))
    fn = nz.nome(c.get('nome')) or nz.nome((c.get('nome_completo') or '').split(' ')[0] or None)
    ln = nz.nome(c.get('sobrenome'))
    ud = {
        'em': _lista(em and nz.sha256(em)),
        'ph': _lista(ph and nz.sha256(ph)),
        'fn': _lista(fn and nz.sha256(fn)),
        'ln': _lista(ln and nz.sha256(ln)),
        'ct': _lista(nz.cidade(c.get('cidade')) and nz.sha256(nz.cidade(c.get('cidade')))),
        'st': _lista(nz.uf(c.get('uf')) and nz.sha256(nz.uf(c.get('uf')))),
        'zp': _lista(nz.cep(c.get('cep')) and nz.sha256(nz.cep(c.get('cep')))),
        'country': _lista(nz.pais(norm.get('pais_iso')) and nz.sha256(nz.pais(norm.get('pais_iso')))),
        'external_id': _lista(em and nz.sha256(em)),
    }
    if visita:
        ud.update({'fbp': visita.get('fbp'), 'fbc': visita.get('fbc'),
                   'client_ip_address': visita.get('ip'), 'client_user_agent': visita.get('ua')})
    return {k: v for k, v in ud.items() if v}


def evento_compra(norm, perfil, visita=None):
    """-> (evento, motivo). evento None quando não deve ir (motivo diz por quê)."""
    if perfil['capi_purchase'] != 'kit':
        return None, 'purchase_desligado'
    if norm['evento'] != 'PURCHASE_APPROVED':
        return None, 'nao_e_aprovacao'
    if perfil['recorrencia'] == 'primeira' and (norm.get('recorrencia') or 1) > 1:
        return None, 'recorrencia'
    if perfil['valor'] == 'cheio':
        valor, moeda = norm.get('valor_cheio'), norm.get('moeda_cheio')
    else:
        valor, moeda = norm.get('valor_preco'), norm.get('moeda_preco')
    if valor is None or not moeda:
        return None, 'sem_valor_ou_moeda'
    quando_ms = norm.get('aprovado_em_ms') or norm.get('criado_em_ms')
    if not quando_ms:
        return None, 'sem_data'
    ud = user_data_compra(norm, visita)
    tem_navegador = bool(visita and visita.get('ua'))
    ev = {
        'event_name': 'Purchase',
        'event_time': int(quando_ms // 1000),
        'event_id': event_id_compra(norm['transacao']),
        'action_source': 'website' if tem_navegador else perfil['origem_sem_navegador'],
        'user_data': ud,
        'custom_data': {'currency': moeda, 'value': round(valor, 2), 'order_id': norm['transacao'],
                        'content_ids': [norm['produto_id']], 'content_type': 'product'},
    }
    url = (visita or {}).get('url') or perfil.get('url_padrao')
    if url:
        ev['event_source_url'] = url
    if ev['action_source'] == 'website' and not tem_navegador:
        return None, 'website_sem_user_agent'
    return ev, 'ok'


def evento_clique(visita, perfil):
    if perfil['capi_checkout'] != 'kit':
        return None, 'checkout_desligado'
    if visita.get('event_name') != perfil['evento_clique']:
        return None, 'nome_de_evento_diferente_do_perfil'
    ud = {k: v for k, v in {'fbp': visita.get('fbp'), 'fbc': visita.get('fbc'),
                            'client_ip_address': visita.get('ip'),
                            'client_user_agent': visita.get('ua')}.items() if v}
    if not ud.get('client_user_agent'):
        return None, 'website_sem_user_agent'
    ev = {'event_name': visita['event_name'], 'event_time': int(visita['criado_em']), 'event_id': visita['event_id'],
          'action_source': 'website', 'user_data': ud}
    if visita.get('url'):
        ev['event_source_url'] = visita['url']
    return ev, 'ok'


def evento_abandono(norm, perfil):
    if perfil['capi_abandono'] != 'personalizado':
        return None, 'abandono_desligado'
    c = norm.get('comprador') or {}
    em = nz.email(c.get('email'))
    ph = nz.telefone(c.get('telefone'), None, norm.get('pais_iso'))
    ud = {k: v for k, v in {'em': _lista(em and nz.sha256(em)), 'ph': _lista(ph and nz.sha256(ph)),
                            'client_ip_address': norm.get('ip')}.items() if v}
    if not ud:
        return None, 'sem_dado_de_cliente'
    quando = norm.get('criado_em_ms')
    if not quando:
        return None, 'sem_data'
    ev = {'event_name': EVENTO_ABANDONO_PERSONALIZADO, 'event_time': int(quando // 1000),
          'event_id': 'hm-abandono.' + norm['id'], 'action_source': perfil['origem_sem_navegador'],
          'user_data': ud, 'custom_data': {'content_ids': [norm['produto_id']], 'content_type': 'product'}}
    return ev, 'ok'


def velho_demais(ev, agora=None):
    agora = agora or time.time()
    return ev['event_time'] < agora - SETE_DIAS + MARGEM_VELHO


# ------------------------------------------------------------------------------------------------- envio
def _transporte_rede(url, corpo, timeout):
    req = urllib.request.Request(url, data=corpo, method='POST',
                                 headers={'Content-Type': 'application/x-www-form-urlencoded',
                                          'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:     # noqa: S310 (host fixo)
            return r.status, r.read(200_000)
    except urllib.error.HTTPError as e:
        try:
            return e.code, e.read(200_000)
        except Exception:                                            # noqa: BLE001
            return e.code, b''


def enviar(ev, perfil, token, transporte=None, timeout=20.0):
    """-> ('enviado'|'rejeitado'|'tentar_de_novo', resumo_curto). Resumo nunca leva token nem user_data."""
    transporte = transporte or _transporte_rede
    url = f'https://graph.facebook.com/{perfil["versao_graph"]}/{perfil["pixel_id"]}/events'
    campos = {'data': json.dumps([ev], separators=(',', ':')), 'access_token': token}
    if perfil['modo'] == 'teste':
        campos['test_event_code'] = perfil['test_event_code']
    corpo = urllib.parse.urlencode(campos).encode()
    del campos
    try:
        status, resp = transporte(url, corpo, timeout)
    except Exception as e:                                           # noqa: BLE001
        return 'tentar_de_novo', f'rede:{type(e).__name__}'
    finally:
        del corpo
    try:
        j = json.loads(resp.decode('utf-8', 'replace')) if resp else {}
    except ValueError:
        j = {}
    if status == 200 and isinstance(j, dict) and j.get('events_received') == 1:
        return 'enviado', f'http200 recebidos=1 fbtrace={str(j.get("fbtrace_id", ""))[:40]}'
    erro = j.get('error') if isinstance(j, dict) else None
    codigo = erro.get('code') if isinstance(erro, dict) else None
    sub = erro.get('error_subcode') if isinstance(erro, dict) else None
    resumo = f'http{status} code={codigo} sub={sub}'
    if status == 429 or status >= 500 or codigo in (1, 2, 4, 17, 341):
        return 'tentar_de_novo', resumo
    if status == 200:
        return 'tentar_de_novo', resumo + ' sem_events_received'
    return 'rejeitado', resumo
