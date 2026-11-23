"""apoio.py: caixa de areia dos testes. Nada aqui fala com a rede de fora: o receptor sobe em 127.0.0.1 numa porta
livre, a Meta é um transporte falso que grava o que receberia, e a Hotmart é um transporte falso também."""
import copy
import http.client
import json
import os
import shutil
import socket
import sys
import tempfile
import threading
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MOTOR = RAIZ / 'motor'
FIX = Path(__file__).resolve().parent / 'fixtures'
sys.path.insert(0, str(MOTOR))

import config      # noqa: E402
import receptor    # noqa: E402

HOTTOK = 'hottok-de-teste-' + 'a1b2c3d4e5f6'
TOKEN_META = 'token-meta-de-teste-' + 'f6e5d4c3b2a1'


def porta_livre():
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    p = s.getsockname()[1]
    s.close()
    return p


def fixture(nome):
    return json.loads((FIX / nome).read_text())


def compra_atual(transacao='HP02316330308193', evento='PURCHASE_APPROVED', id_evento=None, **mudar):
    """O exemplo oficial da Hotmart com datas de agora (o original é de 2009 e cairia em velho_demais)."""
    d = copy.deepcopy(fixture('hotmart-compra-aprovada-doc.json'))
    agora_ms = int(time.time() * 1000)
    d['id'] = id_evento or ('ev-' + transacao.lower() + '-' + evento.lower()[-8:].replace('_', ''))
    d['event'] = evento
    d['creation_date'] = agora_ms
    d['data']['purchase']['approved_date'] = agora_ms - 60000
    d['data']['purchase']['transaction'] = transacao
    d['data']['purchase']['status'] = 'APPROVED'
    d['data']['purchase']['recurrence_number'] = 1
    for k, v in mudar.items():
        alvo = d['data']
        partes = k.split('__')
        for p in partes[:-1]:
            alvo = alvo[p]
        alvo[partes[-1]] = v
    return d


def abandono_atual(id_evento='0d7aa966-b887-4617-8c56-9e865bfc8ce4', **mudar):
    d = copy.deepcopy(fixture('hotmart-abandono-doc.json'))
    d['id'] = id_evento
    d['creation_date'] = int(time.time() * 1000)
    for k, v in mudar.items():
        alvo = d['data']
        partes = k.split('__')
        for p in partes[:-1]:
            alvo = alvo[p]
        alvo[partes[-1]] = v
    return d


class Caixa:
    """Pasta temporária com perfil, segredos (600) e dados."""
    def __init__(self, **perfil):
        self.dir = Path(tempfile.mkdtemp(prefix='hm-teste-'))
        os.chmod(self.dir, 0o700)
        self.hottok = self.dir / 'hottok.env'
        self._segredo(self.hottok, f'HOTMART_HOTTOK={HOTTOK}\n')
        self.token = self.dir / 'meta.env'
        self._segredo(self.token, f'META_CAPI_TOKEN={TOKEN_META}\n')
        self.dados = self.dir / 'dados'
        self.porta = porta_livre()
        base = {
            'HM_DADOS_DIR': str(self.dados), 'HM_HOTTOK_ARQUIVO': str(self.hottok), 'HM_PORTA': str(self.porta),
            'HM_SITE_ORIGENS': 'https://site.exemplo.com.br',
            'HOTMART_PIXEL_NATIVO_COMPRA': 'desligado', 'HOTMART_PIXEL_NATIVO_CHECKOUT': 'desligado',
            'CAPI_MODO': 'seco', 'CAPI_PURCHASE': 'kit', 'CAPI_CHECKOUT': 'kit',
            'CAPI_PIXEL_ID': '123456789012345', 'CAPI_TOKEN_ARQUIVO': str(self.token),
            'CAPI_URL_PADRAO': 'https://site.exemplo.com.br/vendas',
        }
        base.update({k: v for k, v in perfil.items() if v is not None})
        for k in [k for k, v in perfil.items() if v is None]:
            base.pop(k, None)
        self.perfil_env = self.dir / 'perfil.env'
        self.perfil_env.write_text(''.join(f'{k}={v}\n' for k, v in base.items()))
        self.srv = None

    @staticmethod
    def _segredo(p, texto):
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write(texto)

    def perfil(self):
        return config.carregar(str(self.perfil_env))

    def subir(self):
        self.srv = receptor.criar_servidor(self.perfil())
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        return self.srv

    def post(self, rota, corpo, cabecalhos=None):
        if isinstance(corpo, (dict, list)):
            corpo = json.dumps(corpo).encode()
        elif isinstance(corpo, str):
            corpo = corpo.encode()
        c = http.client.HTTPConnection('127.0.0.1', self.porta, timeout=10)
        h = {'Content-Type': 'application/json', 'Content-Length': str(len(corpo))}
        h.update(cabecalhos or {})
        c.request('POST', rota, body=corpo, headers=h)
        r = c.getresponse()
        dados = r.read()
        c.close()
        return r.status, (json.loads(dados) if dados else None), dict(r.getheaders())

    def get(self, rota):
        c = http.client.HTTPConnection('127.0.0.1', self.porta, timeout=10)
        c.request('GET', rota)
        r = c.getresponse()
        dados = r.read()
        c.close()
        return r.status, json.loads(dados) if dados else None

    def hotmart(self, payload, hottok=HOTTOK):
        cab = {'X-HOTMART-HOTTOK': hottok} if hottok is not None else {}
        return self.post('/v1/hotmart', payload, cab)

    def fechar(self):
        if self.srv:
            self.srv.shutdown()
            self.srv.server_close()
        shutil.rmtree(self.dir, ignore_errors=True)


class MetaFalsa:
    """Transporte falso da Graph API. Grava cada chamada; responde o que a fila de respostas mandar."""
    def __init__(self, respostas=None):
        self.chamadas = []
        self.respostas = list(respostas or [])

    def __call__(self, url, corpo, timeout):
        from urllib.parse import parse_qs
        campos = {k: v[0] for k, v in parse_qs(corpo.decode()).items()}
        self.chamadas.append({'url': url, 'campos': campos, 'data': json.loads(campos['data'])})
        if self.respostas:
            r = self.respostas.pop(0)
            if isinstance(r, Exception):
                raise r
            return r
        return 200, json.dumps({'events_received': 1, 'messages': [], 'fbtrace_id': 'AbCdTeste'}).encode()
