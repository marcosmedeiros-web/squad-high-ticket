"""canais.py: os clientes dos serviços do outro lado. Cada um com a lista FECHADA de rotas que pode usar.

  Mautic 7 (basic auth, o mesmo usuário de API do pacote de e-mail):
    POST /api/contacts/new                          cria ou atualiza o contato (o Mautic deduplica pelo e-mail)
    POST /api/segments/<sid>/contact/<cid>/add      põe no segmento
    GET  /api/contacts/<cid>/segments               RELEITURA: o contato está mesmo no segmento?
    POST /api/emails/<eid>/contact/<cid>/send       e-mail modelo para um contato
    GET  /api/stats/email_stats                     RELEITURA: a linha do envio existe?
  OpenWA do kit (chave operator escopada à sessão, só em 127.0.0.1):
    GET  /sessions/<id>                             sessão pronta?
    GET  /sessions/<id>/contacts/check/<número>     existe no WhatsApp? qual o @lid?
    GET  /sessions/<id>/groups                      o grupo é desta sessão?
    GET  /sessions/<id>/messages?chatId=...         RELEITURA da conversa (banco do gateway)
    POST /sessions/<id>/messages/send-text          o envio (uma vez por passo, nunca repetido às cegas)

A releitura existe porque "200" não prova nada: o Mautic pode responder sucesso e o contato não estar no
segmento, e o OpenWA devolve 201 até para número que não está no WhatsApp. O passo só vira `feito` quando a
releitura mostra o resultado na ponta.
"""
import base64
import json
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from base import Recusa, ler_segredo


class ServicoErro(Exception):
    """Falha de rede ou resposta fora do esperado. `transitorio` = vale tentar de novo mais tarde."""
    def __init__(self, motivo, transitorio=True, status=None):
        super().__init__(motivo)
        self.motivo = motivo
        self.transitorio = transitorio
        self.status = status


class _SemRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_abrir = urllib.request.build_opener(urllib.request.ProxyHandler({}), _SemRedirect()).open


def _http(metodo, url, cabecalhos, corpo=None, timeout=20.0):
    req = urllib.request.Request(url, data=corpo, method=metodo, headers=cabecalhos)
    try:
        with _abrir(req, timeout=timeout) as r:
            st, bruto = r.status, r.read()
    except urllib.error.HTTPError as e:
        st, bruto = e.code, (e.read() or b'')
    except (urllib.error.URLError, OSError) as e:
        raise ServicoErro(f'rede:{type(getattr(e, "reason", e)).__name__}') from None
    try:
        j = json.loads(bruto.decode('utf-8', 'replace')) if bruto else None
    except ValueError:
        j = None
    return st, j


# ------------------------------------------------------------------------------------------------ Mautic
_ROTAS_MAUTIC = (
    ('POST', re.compile(r'^/api/contacts/new$')),
    ('POST', re.compile(r'^/api/segments/[0-9]{1,9}/contact/[0-9]{1,12}/add$')),
    ('GET', re.compile(r'^/api/contacts/[0-9]{1,12}/segments$')),
    ('POST', re.compile(r'^/api/emails/[0-9]{1,9}/contact/[0-9]{1,12}/send$')),
    ('GET', re.compile(r'^/api/stats/email_stats$')),
)


class Mautic:
    def __init__(self, base, usuario, senha, timeout=30.0):
        self.base = base.rstrip('/')
        self.__auth = 'Basic ' + base64.b64encode(f'{usuario}:{senha}'.encode()).decode()
        self.timeout = timeout
        self.chamadas = 0

    def __repr__(self):
        return f'<Mautic {self.base} chamadas={self.chamadas}>'

    @classmethod
    def do_perfil(cls, perfil):
        if not perfil['mautic_url']:
            raise Recusa('mautic_nao_configurado', 'AF_MAUTIC_URL vazio no perfil', rc=10)
        c = ler_segredo(perfil['mautic_cred'], ('MAUTIC_API_USUARIO', 'MAUTIC_API_SENHA'))
        return cls(perfil['mautic_url'], c['MAUTIC_API_USUARIO'], c['MAUTIC_API_SENHA'])

    def _req(self, metodo, caminho, dados=None, params=None):
        if not any(m == metodo and r.match(caminho) for m, r in _ROTAS_MAUTIC):
            raise ServicoErro(f'rota_mautic_recusada:{metodo}', transitorio=False)
        url = self.base + caminho + ('?' + urllib.parse.urlencode(params) if params else '')
        h = {'Authorization': self.__auth, 'Accept': 'application/json'}
        corpo = None
        if dados is not None:
            corpo = json.dumps(dados, ensure_ascii=False).encode('utf-8')
            h['Content-Type'] = 'application/json'
        self.chamadas += 1
        st, j = _http(metodo, url, h, corpo, self.timeout)
        if st in (401, 403):
            raise ServicoErro(f'mautic_sem_permissao_{st}', transitorio=False, status=st)
        if st >= 500 or st == 429:
            raise ServicoErro(f'mautic_http_{st}', status=st)
        return st, j

    def contato(self, email, nome=None, telefone=None, tags=()):
        d = {'email': email, 'overwriteWithBlank': False}
        if nome:
            partes = nome.split()
            d['firstname'] = partes[0]
            if len(partes) > 1:
                d['lastname'] = ' '.join(partes[1:])
        if telefone:
            d['mobile'] = '+' + telefone
        if tags:
            d['tags'] = list(tags)
        st, j = self._req('POST', '/api/contacts/new', d)
        cid = (j or {}).get('contact', {}).get('id') if isinstance(j, dict) else None
        if st not in (200, 201) or not isinstance(cid, int):
            raise ServicoErro(f'mautic_contato_http_{st}', transitorio=st not in (400, 422), status=st)
        return cid

    def por_no_segmento(self, sid, cid):
        st, j = self._req('POST', f'/api/segments/{int(sid)}/contact/{int(cid)}/add')
        if st == 404:
            raise ServicoErro('mautic_segmento_inexistente', transitorio=False, status=st)
        if st != 200:
            raise ServicoErro(f'mautic_segmento_http_{st}', status=st)

    def segmentos_do_contato(self, cid):
        st, j = self._req('GET', f'/api/contacts/{int(cid)}/segments')
        if st != 200 or not isinstance(j, dict) or not isinstance(j.get('lists'), (dict, list)):
            raise ServicoErro(f'mautic_releitura_segmentos_http_{st}', status=st)
        ls = j['lists']
        itens = ls.values() if isinstance(ls, dict) else ls
        return {int(x['id']) for x in itens if isinstance(x, dict) and str(x.get('id', '')).isdigit()}

    def enviar_email(self, eid, cid):
        st, j = self._req('POST', f'/api/emails/{int(eid)}/contact/{int(cid)}/send')
        if st == 404:
            raise ServicoErro('mautic_email_inexistente', transitorio=False, status=st)
        if st != 200 or not isinstance(j, dict) or not j.get('success'):
            raise ServicoErro(f'mautic_email_http_{st}', transitorio=False, status=st)

    def email_registrado(self, eid, cid):
        st, j = self._req('GET', '/api/stats/email_stats', params={
            'where[0][col]': 'email_id', 'where[0][expr]': 'eq', 'where[0][val]': int(eid),
            'where[1][col]': 'lead_id', 'where[1][expr]': 'eq', 'where[1][val]': int(cid), 'limit': 10})
        if st != 200 or not isinstance(j, dict) or 'stats' not in j:
            raise ServicoErro(f'mautic_releitura_email_http_{st}', status=st)
        return len(j['stats'] or []) > 0


# ------------------------------------------------------------------------------------------------ OpenWA
_UUID = r'[0-9a-fA-F-]{36}'
_ROTAS_WA = (
    ('GET', re.compile(rf'^/sessions/{_UUID}$')),
    ('GET', re.compile(rf'^/sessions/{_UUID}/contacts/check/[0-9]{{10,15}}$')),
    ('GET', re.compile(rf'^/sessions/{_UUID}/groups$')),
    ('GET', re.compile(rf'^/sessions/{_UUID}/messages$')),
    ('POST', re.compile(rf'^/sessions/{_UUID}/messages/send-text$')),
)
RE_LID = re.compile(r'^[0-9]{5,20}@lid$')
RE_GRUPO = re.compile(r'^[0-9-]{10,40}@g\.us$')


class OpenWA:
    def __init__(self, base, chave, sessao_id, timeout=20.0):
        u = urllib.parse.urlsplit(base)
        if u.scheme != 'http' or u.hostname not in ('127.0.0.1', 'localhost'):
            raise Recusa('openwa_fora_da_maquina', 'o gateway tem que estar em 127.0.0.1', rc=10)
        self._origem = f'http://{u.hostname}:{u.port or 80}{u.path.rstrip("/")}'
        self.__chave = chave
        self.sessao_id = sessao_id
        self.timeout = timeout
        self.posts = 0

    def __repr__(self):
        return f'<OpenWA {self._origem} posts={self.posts}>'

    @classmethod
    def do_perfil(cls, perfil):
        if not (perfil['openwa_base'] and perfil['openwa_sessao']):
            raise Recusa('openwa_nao_configurado', 'AF_OPENWA_BASE e AF_OPENWA_SESSAO_ID no perfil', rc=10)
        c = ler_segredo(perfil['openwa_chave'], ('OPENWA_CHAVE',))
        return cls(perfil['openwa_base'], c['OPENWA_CHAVE'], perfil['openwa_sessao'])

    def _req(self, metodo, rota, params=None, corpo=None):
        if not any(m == metodo and r.match(rota) for m, r in _ROTAS_WA):
            raise ServicoErro(f'rota_openwa_recusada:{metodo}', transitorio=False)
        url = self._origem + rota + ('?' + urllib.parse.urlencode(params) if params else '')
        h = {'Accept': 'application/json', 'x-api-key': self.__chave}
        dados = None
        if corpo is not None:
            dados = json.dumps(corpo, ensure_ascii=False).encode('utf-8')
            h['Content-Type'] = 'application/json'
            self.posts += 1
        st, j = _http(metodo, url, h, dados, self.timeout)
        if st in (401, 403):
            raise ServicoErro(f'openwa_sem_permissao_{st}', transitorio=False, status=st)
        return st, j

    def sessao_pronta(self):
        st, s = self._req('GET', f'/sessions/{self.sessao_id}')
        if st != 200 or not isinstance(s, dict):
            raise ServicoErro(f'openwa_sessao_http_{st}', status=st)
        if s.get('restriction'):
            raise ServicoErro('openwa_sessao_com_restricao', transitorio=False)
        if s.get('status') != 'ready' or s.get('engineLoaded') is False:
            raise ServicoErro(f'openwa_sessao_{s.get("status")}')

    def lid(self, numero):
        st, r = self._req('GET', f'/sessions/{self.sessao_id}/contacts/check/{numero}')
        if st != 200 or not isinstance(r, dict) or not isinstance(r.get('exists'), bool):
            raise ServicoErro(f'openwa_check_http_{st}', status=st)
        if not r['exists']:
            return None
        return str(r.get('whatsappId') or '')

    def grupos(self):
        st, r = self._req('GET', f'/sessions/{self.sessao_id}/groups')
        if st != 200:
            raise ServicoErro(f'openwa_grupos_http_{st}', status=st)
        lista = r
        if isinstance(r, dict):
            lista = r.get('groups') or r.get('data') or []
        if not isinstance(lista, list):
            raise ServicoErro('openwa_grupos_fora_do_formato')
        ids = set()
        for g in lista:
            if isinstance(g, dict):
                for k in ('id', 'groupId', 'chatId'):
                    v = g.get(k)
                    if isinstance(v, dict):
                        v = v.get('_serialized')
                    if isinstance(v, str) and RE_GRUPO.match(v):
                        ids.add(v)
        return ids

    def conversa(self, chat_id, paginas=5):
        msgs = []
        for pag in range(paginas):
            st, c = self._req('GET', f'/sessions/{self.sessao_id}/messages',
                              params={'chatId': chat_id, 'limit': 100, 'offset': pag * 100})
            if st != 200:
                raise ServicoErro(f'openwa_mensagens_http_{st}', status=st)
            lote = c.get('messages') if isinstance(c, dict) else c
            if not isinstance(lote, list):
                raise ServicoErro('openwa_mensagens_fora_do_formato')
            msgs.extend(m for m in lote if isinstance(m, dict) and m.get('chatId') in (None, chat_id))
            if len(lote) < 100:
                return msgs
        raise ServicoErro('openwa_conversa_longa_leitura_truncada')

    def enviar(self, chat_id, texto):
        if not (RE_LID.match(chat_id or '') or RE_GRUPO.match(chat_id or '')):
            raise ServicoErro('destino_nao_lid_nem_grupo', transitorio=False)
        return self._req('POST', f'/sessions/{self.sessao_id}/messages/send-text',
                         corpo={'chatId': chat_id, 'text': texto})


# ------------------------------------------------------------------------------------------------ aviso
def avisar(perfil, texto, dados_dir):
    """Entrega um aviso ao dono. -> True só quando ENTREGUE (rc 0 do canal). `arquivo` é o modo seco."""
    canal = perfil['aviso_canal']
    if canal == 'arquivo':
        p = Path(dados_dir) / 'avisos.jsonl'
        with open(p, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'texto': texto}, ensure_ascii=False) + '\n')
        p.chmod(0o600)
        return True
    if canal == 'avisar-dono':
        cmd = ['bash', str(Path(perfil['head_turbo_home']) / 'vigias' / 'avisar-dono.sh'), texto]
    else:
        cmd = [canal.split(':', 1)[1], texto]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return r.returncode == 0
