"""Cliente minimo da API do Mautic 7 (basic auth). A senha vem do cofre 600 e so existe no cabecalho em memoria."""
import base64
import json
import urllib.error
import urllib.parse
import urllib.request

from .perfil import ler_cofre
from .saida import Recusa


class Api:
    def __init__(self, base, usuario, senha, timeout=60):
        self.base = base.rstrip('/')
        tok = base64.b64encode(f'{usuario}:{senha}'.encode()).decode()
        self._auth = 'Basic ' + tok
        self.timeout = timeout

    @classmethod
    def do_perfil(cls, perfil):
        perfil.exigir('api')
        c = ler_cofre(perfil['EMK_API_ARQUIVO'], ('MAUTIC_API_USUARIO', 'MAUTIC_API_SENHA'))
        return cls(perfil['EMK_API_URL'], c['MAUTIC_API_USUARIO'], c['MAUTIC_API_SENHA'])

    def _req(self, metodo, caminho, corpo=None, tipo=None, params=None):
        url = self.base + caminho
        if params:
            url += '?' + urllib.parse.urlencode(params)
        h = {'Authorization': self._auth, 'Accept': 'application/json'}
        if tipo:
            h['Content-Type'] = tipo
        req = urllib.request.Request(url, data=corpo, method=metodo, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                st, raw = r.status, r.read()
        except urllib.error.HTTPError as e:
            st, raw = e.code, e.read() or b''
        except (urllib.error.URLError, OSError) as e:
            raise Recusa('api_inalcancavel', rc=2, erro=type(getattr(e, 'reason', e)).__name__)
        try:
            d = json.loads(raw.decode() or '{}')
        except ValueError:
            raise Recusa('api_resposta_ilegivel', rc=2, http=st, caminho=caminho.split('?')[0])
        if st in (401, 403):
            raise Recusa('api_sem_permissao', rc=2, http=st)
        return st, d

    def get(self, caminho, params=None):
        return self._req('GET', caminho, params=params)

    def post_form(self, caminho, dados=None):
        return self._req('POST', caminho, urllib.parse.urlencode(dados or {}).encode(),
                         'application/x-www-form-urlencoded')

    def post_json(self, caminho, dados):
        return self._req('POST', caminho, json.dumps(dados).encode(), 'application/json')

    def patch_json(self, caminho, dados):
        return self._req('PATCH', caminho, json.dumps(dados).encode(), 'application/json')

    # ---------------------------------------------------------------- atalhos usados pelo disparo
    def email(self, eid):
        st, d = self.get(f'/api/emails/{eid}')
        if st == 404:
            raise Recusa('email_inexistente', rc=1, email_id=eid)
        if st != 200 or 'email' not in d:
            raise Recusa('api_email_ilegivel', rc=2, http=st)
        return d['email']

    def pendentes(self, eid):
        """Mesma consulta que o envio usa (email_pending:<id>): a regua de destinatarios."""
        st, d = self.get('/api/contacts', {'search': f'email_pending:{eid}', 'limit': 1, 'minimal': 'true'})
        if st != 200 or 'total' not in d:
            raise Recusa('api_pendentes_ilegivel', rc=2, http=st)
        return int(d['total'])

    def stats(self, eid):
        st, d = self.get('/api/stats/email_stats', {
            'where[0][col]': 'email_id', 'where[0][expr]': 'eq', 'where[0][val]': eid, 'limit': 100000})
        if st != 200 or 'stats' not in d:
            raise Recusa('api_stats_ilegivel', rc=2, http=st)
        return d['stats']

    def publicar(self, eid, sim):
        st, d = self.patch_json(f'/api/emails/{eid}/edit', {'isPublished': bool(sim)})
        if st != 200:
            raise Recusa('api_publicacao_falhou', rc=2, http=st)
        return d.get('email', {})
