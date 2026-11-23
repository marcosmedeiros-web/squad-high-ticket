"""receptor.py: a porta de entrada dos fluxos. Ouve SÓ em 127.0.0.1:<AF_PORTA>; o HTTPS público é o Caddy do dono.

ROTAS
  POST /f/<fluxo>/<rota secreta>   formulário (lead-formulario) e batida (ManyChat, n8n, código do dono)
  POST /f/<fluxo>                  webhook 2.0.0 da Hotmart (venda-hotmart): exige o cabeçalho X-HOTMART-HOTTOK
  GET  /saude                      vivo? (o Caddyfile de exemplo NÃO expõe esta rota)

COMO RESPONDE
  404  rota desconhecida, fluxo desligado ou rota secreta errada (não conta a quem bate o que existe)
  401  só a Hotmart com hottok ausente ou errado
  200  tudo que entrou autenticado e foi GRAVADO, inclusive o que o fluxo não sabe tratar (vai para um ramo próprio
       e o vigia avisa) e o repetido. A Hotmart desativa sozinha a URL que dá erro: por isso o 200 é largo.
  500  só quando o banco não gravou (aí o reenvio da origem é o que se quer)
O trabalho da requisição é conferir e gravar; Mautic e WhatsApp acontecem no ciclo (timer), fora daqui.
Log: uma linha por fato, sem corpo, sem cabeçalho, sem IP, sem contato.
"""
import json
import re
import sys
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from base import Recusa, iguais, ler_segredo
from versao import VERSAO

TETO_CORPO = 256 * 1024
_RE_ROTA = re.compile(r'^/f/([a-z][a-z0-9-]{2,40})(?:/([A-Za-z0-9_-]{16,80}))?/?$')


def log(fato, **k):
    print('af-receptor ' + fato + ' ' + ' '.join(f'{a}={b}' for a, b in k.items() if b is not None),
          file=sys.stderr, flush=True)


def ler_corpo(tipo, bruto):
    t = (tipo or '').split(';')[0].strip().lower()
    if t in ('application/json', 'text/json', ''):
        return json.loads(bruto.decode('utf-8') or '{}')
    if t == 'application/x-www-form-urlencoded':
        q = urllib.parse.parse_qs(bruto.decode('utf-8'), keep_blank_values=True)
        return {k: (v[0] if len(v) == 1 else v) for k, v in q.items()}
    raise ValueError('tipo')


def servidor(motor, porta=None):
    trava = threading.Lock()

    class H(BaseHTTPRequestHandler):
        server_version = 'af-receptor'
        sys_version = ''
        protocol_version = 'HTTP/1.1'
        timeout = 15

        def log_message(self, *a):
            return

        def _r(self, st, corpo=None):
            d = json.dumps(corpo or {}, separators=(',', ':')).encode()
            self.send_response(st)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(d)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(d)

        def do_GET(self):   # noqa: N802
            if self.path.split('?')[0] == '/saude':
                with trava:
                    n = len(motor.fluxos())
                return self._r(200, {'ok': True, 'versao': VERSAO, 'fluxos': n})
            self._r(404, {'ok': False})

        def do_POST(self):   # noqa: N802
            m = _RE_ROTA.match(self.path.split('?')[0])
            try:
                n = int(self.headers.get('Content-Length', ''))
            except ValueError:
                self.close_connection = True
                return self._r(411, {'ok': False})
            if n < 0 or n > TETO_CORPO:
                self.close_connection = True
                return self._r(413, {'ok': False})
            bruto = self.rfile.read(n)
            if not m:
                return self._r(404, {'ok': False})
            nome, tok = m.group(1), m.group(2)
            with trava:
                try:
                    cfg = motor.fluxos().get(nome)
                except Recusa as e:
                    log('desenho_torto', motivo=e.motivo)
                    return self._r(500, {'ok': False})
                agora = motor.relogio()
                if not cfg or cfg['tipo'] == 'lembrete-aula':
                    return self._r(404, {'ok': False})
                if motor.modo(nome) == 'desligado':
                    motor.banco.recusa(nome, agora, 'fluxo_desligado')
                    return self._r(404, {'ok': False})
                if cfg['tipo'] == 'venda-hotmart':
                    if tok:
                        return self._r(404, {'ok': False})
                    try:
                        certo = ler_segredo(motor.perfil['hottok_arquivo'], ['HOTMART_HOTTOK'])['HOTMART_HOTTOK']
                    except Recusa as e:
                        log('hottok_ilegivel', fluxo=nome, motivo=e.motivo)
                        return self._r(500, {'ok': False})
                    veio = self.headers.get('X-HOTMART-HOTTOK') or ''
                    if not veio or not iguais(veio, certo):
                        motor.banco.recusa(nome, agora, 'hottok_errado')
                        log('recusa', fluxo=nome, motivo='hottok_errado')
                        return self._r(401, {'ok': False})
                else:
                    certo = motor.token_rota(nome)
                    if not tok or not certo or not iguais(tok, certo):
                        motor.banco.recusa(nome, agora, 'rota_errada')
                        log('recusa', fluxo=nome, motivo='rota_errada')
                        return self._r(404, {'ok': False})
                try:
                    corpo = ler_corpo(self.headers.get('Content-Type'), bruto)
                except (ValueError, UnicodeDecodeError):
                    corpo = None      # entra assim mesmo: vira ramo de "não entendi" e o vigia avisa
                simulado = self.headers.get('X-Fluxos-Simulado') == '1'
                try:
                    eid, novo, ramo = motor.receber(nome, corpo, simulado=simulado)
                except Recusa as e:
                    log('nao_gravou', fluxo=nome, motivo=e.motivo)
                    return self._r(500, {'ok': False})
                except Exception as e:   # noqa: BLE001 - banco travado, disco cheio: 500 para a origem reenviar
                    log('nao_gravou', fluxo=nome, erro=type(e).__name__)
                    return self._r(500, {'ok': False})
            log('evento', fluxo=nome, ramo=ramo, novo=int(novo), simulado=int(simulado) or None)
            self._r(200, {'ok': True})

    srv = ThreadingHTTPServer(('127.0.0.1', motor.perfil['porta'] if porta is None else porta), H)
    srv.daemon_threads = True
    return srv
