#!/usr/bin/env python3
"""receptor.py: o receptor do webhook da Hotmart e do aviso de clique do site. Só biblioteca padrão.

ROTAS
  POST /v1/hotmart   webhook 2.0.0 da Hotmart. Exige o cabeçalho X-HOTMART-HOTTOK igual ao hottok do dono.
  POST /v1/visita    aviso do snippet do site no clique de checkout (sendBeacon, text/plain). Exige Origin na
                     lista HM_SITE_ORIGENS. Público por natureza, como o próprio pixel: tem teto por IP e tamanho.
  GET  /saude        contagens, sem dado pessoal. O Caddyfile de exemplo NÃO expõe esta rota para fora.

COMO RESPONDE À HOTMART, E POR QUÊ
  A Hotmart desativa sozinha a configuração quando a URL dá erro, e reenvia até 5 vezes (Central de Ajuda,
  artigo 360001491352). Então:
    401  só para hottok ausente ou errado (é a resposta certa para quem não é a Hotmart);
    200  para tudo que veio autenticado, inclusive o que o kit não entende (vai para a quarentena e aparece no
         `eventos.py status`), e para o reenvio de um evento que já entrou ("duplicado");
    500  só quando o banco não gravou: aí o reenvio da Hotmart é exatamente o que se quer.
  O trabalho na requisição é ler, conferir e gravar (milissegundos). A chamada à Meta acontece fora, no
  `capi_worker.py`, para a Meta lenta ou fora do ar nunca atrasar a resposta à Hotmart.

O hottok nunca é logado nem comparado com `==` (comparação em tempo constante). O log do http.server é
desligado: a linha de log é nossa e não carrega cabeçalho, corpo, IP nem dado de comprador.
"""
import hashlib
import hmac
import json
import os
import re
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import banco as bco            # noqa: E402
import capi                    # noqa: E402
import config                  # noqa: E402
import hotmart_evento as he    # noqa: E402
import segredo                 # noqa: E402
from versao import VERSAO      # noqa: E402

TETO_CORPO_HOTMART = 512 * 1024
TETO_CORPO_VISITA = 4 * 1024
TETO_VISITAS_POR_MIN = 30
_RE_ID_SITE = re.compile(r'^[A-Za-z0-9._-]{8,80}$')
_RE_FBP = re.compile(r'^fb\.[0-9]\.[0-9]{10,13}\.[0-9]{1,30}$')
_RE_FBC = re.compile(r'^fb\.[0-9]\.[0-9]{10,13}\.[A-Za-z0-9_-]{1,500}$')


def log(_fato, **campos):
    """Uma linha por fato, chave=valor, só com campo de lista fechada."""
    partes = [f'{k}={v}' for k, v in campos.items() if v is not None]
    print(f'hm-receptor {_fato} ' + ' '.join(partes), file=sys.stderr, flush=True)


class Hottok:
    """Relê o arquivo quando ele muda (troca de hottok sem reiniciar)."""
    def __init__(self, caminho):
        self.caminho = caminho
        self._mtime = None
        self._valor = None
        self._trava = threading.Lock()

    def valor(self):
        with self._trava:
            m = os.stat(self.caminho).st_mtime_ns
            if m != self._mtime:
                self._valor = segredo.ler(self.caminho, ['HOTMART_HOTTOK'])['HOTMART_HOTTOK'].encode()
                self._mtime = m
            return self._valor


class Limitador:
    def __init__(self, por_min):
        self.por_min = por_min
        self._janela = {}
        self._trava = threading.Lock()

    def passa(self, chave):
        agora = int(time.time() // 60)
        with self._trava:
            if len(self._janela) > 10000:
                self._janela = {k: v for k, v in self._janela.items() if v[0] == agora}
            m, n = self._janela.get(chave, (agora, 0))
            if m != agora:
                m, n = agora, 0
            if n >= self.por_min:
                return False
            self._janela[chave] = (m, n + 1)
            return True


def montar_capi(perfil):
    def _m(norm, visita):
        if norm['tipo'] == 'compra':
            ev, motivo = capi.evento_compra(norm, perfil, visita)
            return (f'Purchase|{ev["event_id"]}' if ev else None), 'compra', ev, motivo
        ev, motivo = capi.evento_abandono(norm, perfil)
        return (f'{capi.EVENTO_ABANDONO_PERSONALIZADO}|{ev["event_id"]}' if ev else None), 'abandono', ev, motivo
    return _m


class Receptor(BaseHTTPRequestHandler):
    server_version = 'hm-receptor'
    sys_version = ''
    protocol_version = 'HTTP/1.1'
    timeout = 15

    def log_message(self, *a):          # o log padrão do http.server mostraria IP e caminho cru
        return

    # ------------------------------------------------------------------------------------ util
    def _resp(self, codigo, corpo=None, extra=None):
        dados = json.dumps(corpo or {}, separators=(',', ':')).encode()
        self.send_response(codigo)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(dados)))
        self.send_header('Cache-Control', 'no-store')
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(dados)

    def _corpo(self, teto):
        try:
            n = int(self.headers.get('Content-Length', ''))
        except ValueError:
            self.close_connection = True       # corpo não lido: a conexão não pode ser reaproveitada
            return None, 411
        if n < 0 or n > teto:
            self.close_connection = True
            return None, 413
        return self.rfile.read(n), None

    def _ip(self):
        ip = self.client_address[0]
        if self.server.perfil['confia_proxy'] and ip in ('127.0.0.1', '::1'):
            xff = self.headers.get('X-Forwarded-For', '')
            if xff:
                ip = xff.split(',')[-1].strip()
        return ip[:45]

    # ------------------------------------------------------------------------------------ rotas
    def do_GET(self):
        if self.path == '/saude':
            try:
                st = self.server.banco.status()
            except Exception as e:                       # noqa: BLE001
                log('saude_falhou', erro=type(e).__name__)
                return self._resp(500, {'ok': False})
            return self._resp(200, {'ok': True, 'versao': VERSAO, **st})
        return self._resp(404, {'erro': 'rota'})

    def do_OPTIONS(self):
        if self.path == '/v1/visita':
            origem = (self.headers.get('Origin') or '').lower()
            if origem in self.server.perfil['site_origens']:
                return self._resp(204, None, {'Access-Control-Allow-Origin': origem,
                                              'Access-Control-Allow-Methods': 'POST',
                                              'Access-Control-Allow-Headers': 'Content-Type',
                                              'Vary': 'Origin'})
        return self._resp(403, {'erro': 'origem'})

    def do_POST(self):
        if self.path == '/v1/hotmart':
            return self._hotmart()
        if self.path == '/v1/visita':
            return self._visita()
        return self._resp(404, {'erro': 'rota'})

    def _hotmart(self):
        bco_ = self.server.banco
        recebido = self.headers.get('X-HOTMART-HOTTOK')
        try:
            esperado = self.server.hottok.valor()
        except (segredo.SegredoErro, OSError) as e:
            log('hottok_ilegivel', motivo=getattr(e, 'motivo', type(e).__name__))
            return self._resp(500, {'erro': 'configuracao'})
        if not recebido or not hmac.compare_digest(recebido.strip().encode(), esperado):
            corpo, _ = self._corpo(TETO_CORPO_HOTMART)    # esvazia o socket; o corpo é descartado
            del corpo
            motivo = 'hottok_ausente' if not recebido else 'hottok_errado'
            try:
                bco_.recusa('/v1/hotmart', motivo)
            except Exception:                            # noqa: BLE001
                pass
            log('recusa', rota='hotmart', motivo=motivo)
            return self._resp(401, {'erro': 'nao_autorizado'})
        corpo, erro = self._corpo(TETO_CORPO_HOTMART)
        if erro:
            try:
                bco_.quarentena('corpo_grande_ou_sem_tamanho', None, None, None)
            except Exception as e2:                      # noqa: BLE001
                log('banco_falhou', erro=type(e2).__name__)
                return self._resp(500, {'erro': 'banco'})
            log('quarentena', motivo='corpo_grande_ou_sem_tamanho')
            return self._resp(200, {'ok': True, 'quarentena': True})
        sha = hashlib.sha256(corpo).hexdigest()
        try:
            norm = he.ler(corpo)
        except he.EventoInvalido as e:
            try:
                bco_.quarentena(e.motivo, e.nome_evento, e.versao, sha)
            except Exception as e2:                      # noqa: BLE001
                log('banco_falhou', erro=type(e2).__name__)
                return self._resp(500, {'erro': 'banco'})
            log('quarentena', motivo=e.motivo, evento=e.nome_evento, sha8=sha[:8])
            return self._resp(200, {'ok': True, 'quarentena': True})
        del corpo
        perfil = self.server.perfil
        if perfil['produtos'] and norm['produto_id'] not in perfil['produtos']:
            try:
                bco_.quarentena('produto_fora_da_lista', norm['evento'], norm['versao'], sha)
            except Exception as e2:                      # noqa: BLE001
                log('banco_falhou', erro=type(e2).__name__)
                return self._resp(500, {'erro': 'banco'})
            log('quarentena', motivo='produto_fora_da_lista', evento=norm['evento'], sha8=sha[:8])
            return self._resp(200, {'ok': True, 'quarentena': True})
        try:
            r = bco_.registrar_evento(norm, perfil, self.server.montar_capi)
        except Exception as e:                           # noqa: BLE001
            log('banco_falhou', erro=type(e).__name__, evento=norm['evento'])
            return self._resp(500, {'erro': 'banco'})
        log('evento', resultado=r, evento=norm['evento'], produto=norm['produto_id'], sha8=sha[:8])
        return self._resp(200, {'ok': True, 'resultado': r})

    def _visita(self):
        perfil = self.server.perfil
        origem = (self.headers.get('Origin') or '').lower()
        if origem not in perfil['site_origens']:
            self._corpo(TETO_CORPO_VISITA)
            try:
                self.server.banco.recusa('/v1/visita', 'origem')
            except Exception:                            # noqa: BLE001
                pass
            return self._resp(403, {'erro': 'origem'})
        cors = {'Access-Control-Allow-Origin': origem, 'Vary': 'Origin'}
        ip = self._ip()
        if not self.server.limitador.passa(ip):
            self._corpo(TETO_CORPO_VISITA)
            return self._resp(429, {'erro': 'muitas'}, cors)
        corpo, erro = self._corpo(TETO_CORPO_VISITA)
        if erro:
            return self._resp(erro, {'erro': 'tamanho'}, cors)
        try:
            d = json.loads(corpo.decode('utf-8'))
            assert isinstance(d, dict)
        except Exception:                                 # noqa: BLE001
            return self._resp(400, {'erro': 'json'}, cors)
        vid, eid, nome = d.get('visita_id'), d.get('event_id'), d.get('event_name')
        if not (isinstance(vid, str) and _RE_ID_SITE.match(vid) and isinstance(eid, str) and _RE_ID_SITE.match(eid)):
            return self._resp(400, {'erro': 'ids'}, cors)
        if nome not in ('InitiateCheckout', 'CliqueCheckout'):
            return self._resp(400, {'erro': 'evento'}, cors)
        fbp, fbc, url = d.get('fbp'), d.get('fbc'), d.get('url')
        v = {'visita_id': vid, 'event_id': eid, 'event_name': nome, 'criado_em': int(time.time()),
             'fbp': fbp if isinstance(fbp, str) and _RE_FBP.match(fbp) else None,
             'fbc': fbc if isinstance(fbc, str) and _RE_FBC.match(fbc) else None,
             'ip': ip, 'ua': (self.headers.get('User-Agent') or '')[:500] or None,
             'url': url[:1000] if isinstance(url, str) and url.lower().startswith(origem + '/') else None}
        ev, _motivo = capi.evento_clique(v, perfil)
        try:
            r = self.server.banco.registrar_visita(v, ev)
        except Exception as e:                           # noqa: BLE001
            log('banco_falhou', erro=type(e).__name__, rota='visita')
            return self._resp(500, {'erro': 'banco'}, cors)
        log('visita', resultado=r, evento=nome, capi='sim' if ev else 'nao')
        return self._resp(200, {'ok': True}, cors)


def criar_servidor(perfil):
    srv = ThreadingHTTPServer((perfil['escuta'], perfil['porta']), Receptor)
    srv.daemon_threads = True
    srv.perfil = perfil
    srv.banco = bco.Banco(perfil['dados_dir'])
    srv.hottok = Hottok(perfil['hottok_arquivo'])
    srv.limitador = Limitador(TETO_VISITAS_POR_MIN)
    srv.montar_capi = montar_capi(perfil)
    return srv


def main():
    os.umask(0o077)
    try:
        perfil = config.carregar()
        segredo.ler(perfil['hottok_arquivo'], ['HOTMART_HOTTOK'])
    except (config.PerfilRecusado, segredo.SegredoErro) as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        return 78
    srv = criar_servidor(perfil)
    log('no_ar', versao=VERSAO, escuta=perfil['escuta'], porta=perfil['porta'], modo_capi=perfil['modo'])
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
