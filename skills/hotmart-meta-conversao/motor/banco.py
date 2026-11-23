"""banco.py: o banco local do receptor (SQLite, um arquivo 600 numa pasta 700).

O QUE FICA GUARDADO, E O QUE NÃO FICA
  evento       uma linha por evento da Hotmart aceito: id, nome, produto, sha256 da transação, status, valor,
               digital (HMAC local) do e-mail e do telefone. Sem nome, sem e-mail, sem telefone em claro.
  abandono     o lead do carrinho abandonado, COM o contato (nome, e-mail, telefone), porque a recuperação
               (ficha 2) precisa dele. O contato é apagado em HM_RETENCAO_CONTATO_DIAS (padrão 30).
  visita       o clique de checkout no site: fbp, fbc, IP, navegador. Apagada em 8 dias.
  capi_fila    o evento da API de Conversões, já em hash. O user_data some quando o envio tem desfecho.
  quarentena   o que chegou autenticado mas o kit não entendeu: só motivo, nome do evento, versão e sha256 do
               corpo. Nunca o corpo.
  recusa       requisição recusada (hottok errado, origem errada): hora, rota, motivo.

DEDUPE: a Hotmart reenvia o mesmo post até 5 vezes quando a URL falha, e o produtor pode reenviar à mão. O
evento entra uma vez só, por DUAS chaves: o id do evento e a chave de negócio (nome do evento + transação na
compra; nome + id no abandono). Reenvio manual com id novo cai na segunda.
"""
import json
import os
import secrets
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

import normaliza as nz

ESQUEMA = """
CREATE TABLE IF NOT EXISTS evento (
  id_evento TEXT PRIMARY KEY,
  chave_dedupe TEXT NOT NULL UNIQUE,
  nome TEXT NOT NULL,
  versao TEXT NOT NULL,
  recebido_em INTEGER NOT NULL,
  criado_em_ms INTEGER,
  produto_id TEXT,
  transacao_sha TEXT,
  status TEXT,
  recorrencia INTEGER,
  valor REAL,
  moeda TEXT,
  xcod TEXT,
  hmac_email TEXT,
  hmac_tel TEXT
);
CREATE INDEX IF NOT EXISTS evento_nome_t ON evento(nome, recebido_em);
CREATE INDEX IF NOT EXISTS evento_tx ON evento(transacao_sha);
CREATE TABLE IF NOT EXISTS abandono (
  id_evento TEXT PRIMARY KEY,
  recebido_em INTEGER NOT NULL,
  criado_em_ms INTEGER,
  produto_id TEXT,
  oferta TEXT,
  pais_iso TEXT,
  hmac_email TEXT,
  hmac_tel TEXT,
  estado TEXT NOT NULL DEFAULT 'aberto',
  resolvido_em INTEGER,
  nome TEXT,
  email TEXT,
  telefone TEXT,
  apagar_contato_em INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS abandono_estado ON abandono(estado, recebido_em);
CREATE TABLE IF NOT EXISTS visita (
  visita_id TEXT NOT NULL,
  event_id TEXT PRIMARY KEY,
  event_name TEXT NOT NULL,
  criado_em INTEGER NOT NULL,
  fbp TEXT, fbc TEXT, ip TEXT, ua TEXT, url TEXT
);
CREATE INDEX IF NOT EXISTS visita_id ON visita(visita_id, criado_em);
CREATE TABLE IF NOT EXISTS capi_fila (
  chave TEXT PRIMARY KEY,
  origem TEXT NOT NULL,
  criado_em INTEGER NOT NULL,
  event_time INTEGER NOT NULL,
  payload TEXT,
  estado TEXT NOT NULL,
  tentativas INTEGER NOT NULL DEFAULT 0,
  proxima_em INTEGER NOT NULL,
  ultimo_status TEXT,
  desfecho_em INTEGER
);
CREATE INDEX IF NOT EXISTS fila_estado ON capi_fila(estado, proxima_em);
CREATE TABLE IF NOT EXISTS quarentena (
  id INTEGER PRIMARY KEY AUTOINCREMENT, recebido_em INTEGER NOT NULL, motivo TEXT NOT NULL,
  nome_evento TEXT, versao TEXT, sha_corpo TEXT
);
CREATE TABLE IF NOT EXISTS recusa (
  id INTEGER PRIMARY KEY AUTOINCREMENT, recebido_em INTEGER NOT NULL, rota TEXT, motivo TEXT NOT NULL
);
"""
VISITA_TTL = 8 * 86400


def preparar_pasta(dados_dir):
    d = Path(dados_dir)
    d.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(d, 0o700)
    return d


def _chave_local(d):
    p = d / 'chave-local'
    if not p.exists():
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write(secrets.token_hex(32))
    return bytes.fromhex(p.read_text().strip())


class Banco:
    def __init__(self, dados_dir):
        self.dir = preparar_pasta(dados_dir)
        self.arquivo = self.dir / 'eventos.sqlite3'
        novo = not self.arquivo.exists()
        if novo:
            os.close(os.open(self.arquivo, os.O_WRONLY | os.O_CREAT, 0o600))
        self.chave = _chave_local(self.dir)
        with self._usar() as c:
            c.executescript(ESQUEMA)

    def _con(self):
        c = sqlite3.connect(self.arquivo, timeout=10, isolation_level=None)
        c.execute('PRAGMA journal_mode=WAL')
        c.execute('PRAGMA busy_timeout=10000')
        c.row_factory = sqlite3.Row
        return c

    @contextmanager
    def _usar(self):
        c = self._con()
        try:
            yield c
        finally:
            c.close()

    # --------------------------------------------------------------------------------------- recebimento
    def recusa(self, rota, motivo):
        with self._usar() as c:
            c.execute('INSERT INTO recusa(recebido_em, rota, motivo) VALUES (?,?,?)', (int(time.time()), rota, motivo))

    def quarentena(self, motivo, nome_evento, versao, sha_corpo):
        with self._usar() as c:
            c.execute('INSERT INTO quarentena(recebido_em, motivo, nome_evento, versao, sha_corpo) VALUES (?,?,?,?,?)',
                      (int(time.time()), motivo, nome_evento, versao, sha_corpo))

    def visita_por_xcod(self, xcod):
        if not xcod:
            return None
        with self._usar() as c:
            r = c.execute('SELECT * FROM visita WHERE visita_id=? ORDER BY criado_em DESC LIMIT 1', (xcod,)).fetchone()
        return dict(r) if r else None

    def registrar_evento(self, norm, perfil, montar_capi):
        """Grava evento (+abandono, +resolução de abandono, +fila CAPI) numa transação só.
        -> 'novo' | 'duplicado'. `montar_capi(norm, visita)` -> (chave, origem, evento|None, motivo)."""
        agora = int(time.time())
        c_ = norm.get('comprador') or {}
        em = nz.email(c_.get('email'))
        tel = nz.telefone(c_.get('telefone'), c_.get('ddd'), norm.get('pais_iso'))
        h_em, h_tel = nz.hmac_local(self.chave, em), nz.hmac_local(self.chave, tel)
        if norm['tipo'] == 'compra':
            chave = f'{norm["evento"]}:{nz.sha256(norm["transacao"])}'
            tx_sha = nz.sha256(norm['transacao'])
            valor = norm.get('valor_cheio') if perfil['valor'] == 'cheio' else norm.get('valor_preco')
            moeda = norm.get('moeda_cheio') if perfil['valor'] == 'cheio' else norm.get('moeda_preco')
        else:
            chave = f'{norm["evento"]}:{norm["id"]}'
            tx_sha, valor, moeda = None, None, None
        visita = self.visita_por_xcod(norm.get('xcod'))
        con = self._con()
        try:
            con.execute('BEGIN IMMEDIATE')
            try:
                con.execute('INSERT INTO evento(id_evento, chave_dedupe, nome, versao, recebido_em, criado_em_ms, '
                            'produto_id, transacao_sha, status, recorrencia, valor, moeda, xcod, hmac_email, hmac_tel) '
                            'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                            (norm['id'], chave, norm['evento'], norm['versao'], agora, norm.get('criado_em_ms'),
                             norm['produto_id'], tx_sha, norm.get('status'), norm.get('recorrencia'), valor, moeda,
                             norm.get('xcod'), h_em, h_tel))
            except sqlite3.IntegrityError:
                con.execute('ROLLBACK')
                return 'duplicado'
            if norm['tipo'] == 'abandono':
                con.execute('INSERT INTO abandono(id_evento, recebido_em, criado_em_ms, produto_id, oferta, pais_iso, '
                            'hmac_email, hmac_tel, nome, email, telefone, apagar_contato_em) '
                            'VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                            (norm['id'], agora, norm.get('criado_em_ms'), norm['produto_id'], norm.get('oferta'),
                             norm.get('pais_iso'), h_em, h_tel, c_.get('nome_completo'), em, tel,
                             agora + perfil['retencao_contato_dias'] * 86400))
                # comprou ANTES do aviso de abandono chegar (a Hotmart confere o carrinho a cada 30 min)
                if h_em or h_tel:
                    ja = con.execute("SELECT 1 FROM evento WHERE nome IN ('PURCHASE_APPROVED','PURCHASE_COMPLETE') "
                                     "AND produto_id=? AND recebido_em>=? AND ((hmac_email IS NOT NULL AND "
                                     "hmac_email=?) OR (hmac_tel IS NOT NULL AND hmac_tel=?)) LIMIT 1",
                                     (norm['produto_id'], agora - 30 * 86400, h_em, h_tel)).fetchone()
                    if ja:
                        con.execute("UPDATE abandono SET estado='comprou', resolvido_em=? WHERE id_evento=?",
                                    (agora, norm['id']))
            if norm['tipo'] == 'compra' and norm['evento'] in ('PURCHASE_APPROVED', 'PURCHASE_COMPLETE'):
                if h_em or h_tel:
                    con.execute("UPDATE abandono SET estado='comprou', resolvido_em=? WHERE estado='aberto' "
                                "AND produto_id=? AND ((hmac_email IS NOT NULL AND hmac_email=?) OR "
                                "(hmac_tel IS NOT NULL AND hmac_tel=?))",
                                (agora, norm['produto_id'], h_em, h_tel))
            chave_fila, origem, ev, _motivo = montar_capi(norm, visita)
            if ev is not None:
                self._enfileirar(con, chave_fila, origem, ev, agora)
            con.execute('COMMIT')
            return 'novo'
        except BaseException:
            try:
                con.execute('ROLLBACK')
            except sqlite3.Error:
                pass
            raise
        finally:
            con.close()

    def _enfileirar(self, con, chave, origem, ev, agora):
        con.execute('INSERT OR IGNORE INTO capi_fila(chave, origem, criado_em, event_time, payload, estado, '
                    'proxima_em) VALUES (?,?,?,?,?,?,?)',
                    (chave, origem, agora, ev['event_time'], json.dumps(ev, separators=(',', ':')), 'pendente', agora))

    def registrar_visita(self, v, ev_capi=None):
        """-> 'novo' | 'duplicado'."""
        con = self._con()
        try:
            con.execute('BEGIN IMMEDIATE')
            try:
                con.execute('INSERT INTO visita(visita_id, event_id, event_name, criado_em, fbp, fbc, ip, ua, url) '
                            'VALUES (?,?,?,?,?,?,?,?,?)',
                            (v['visita_id'], v['event_id'], v['event_name'], v['criado_em'], v.get('fbp'),
                             v.get('fbc'), v.get('ip'), v.get('ua'), v.get('url')))
            except sqlite3.IntegrityError:
                con.execute('ROLLBACK')
                return 'duplicado'
            if ev_capi is not None:
                self._enfileirar(con, f'{ev_capi["event_name"]}|{ev_capi["event_id"]}', 'checkout', ev_capi,
                                 v['criado_em'])
            con.execute('COMMIT')
            return 'novo'
        finally:
            con.close()

    def enfileirar_avulso(self, chave, origem, ev):
        with self._usar() as c:
            self._enfileirar(c, chave, origem, ev, int(time.time()))

    # --------------------------------------------------------------------------------------- fila CAPI
    def fila_vencida(self, agora, limite=50):
        with self._usar() as c:
            return [dict(r) for r in c.execute("SELECT * FROM capi_fila WHERE estado='pendente' AND proxima_em<=? "
                                               "ORDER BY criado_em LIMIT ?", (agora, limite))]

    def fila_desfecho(self, chave, estado, status, apagar_payload=True):
        with self._usar() as c:
            c.execute('UPDATE capi_fila SET estado=?, ultimo_status=?, desfecho_em=?, tentativas=tentativas+1, '
                      'payload=CASE WHEN ? THEN NULL ELSE payload END WHERE chave=?',
                      (estado, status, int(time.time()), 1 if apagar_payload else 0, chave))

    def fila_adiar(self, chave, status, proxima_em):
        with self._usar() as c:
            c.execute('UPDATE capi_fila SET tentativas=tentativas+1, ultimo_status=?, proxima_em=? WHERE chave=?',
                      (status, proxima_em, chave))

    # --------------------------------------------------------------------------------------- leitura
    def abandonos(self, estado='aberto', desde=None, ate=None, com_contato=False):
        q = 'SELECT * FROM abandono WHERE 1=1'
        a = []
        if estado:
            q += ' AND estado=?'
            a.append(estado)
        if desde is not None:
            q += ' AND recebido_em>=?'
            a.append(desde)
        if ate is not None:
            q += ' AND recebido_em<=?'
            a.append(ate)
        q += ' ORDER BY recebido_em'
        with self._usar() as c:
            linhas = [dict(r) for r in c.execute(q, a)]
        if not com_contato:
            for l in linhas:
                for k in ('nome', 'email', 'telefone'):
                    l.pop(k, None)
        return linhas

    def compras_confirmadas_sha(self, desde):
        with self._usar() as c:
            return {r[0] for r in c.execute("SELECT transacao_sha FROM evento WHERE nome IN "
                                            "('PURCHASE_APPROVED','PURCHASE_COMPLETE') AND recebido_em>=?", (desde,))}

    def ultimo_evento_em(self):
        with self._usar() as c:
            r = c.execute('SELECT MAX(recebido_em) FROM evento').fetchone()
        return r[0]

    def status(self):
        agora = int(time.time())
        with self._usar() as c:
            def n(q, *a):
                return c.execute(q, a).fetchone()[0]
            return {
                'eventos': {r[0]: r[1] for r in c.execute('SELECT nome, COUNT(*) FROM evento GROUP BY nome')},
                'ultimo_evento_ha_s': (agora - n('SELECT MAX(recebido_em) FROM evento'))
                if n('SELECT MAX(recebido_em) FROM evento') else None,
                'abandonos': {r[0]: r[1] for r in c.execute('SELECT estado, COUNT(*) FROM abandono GROUP BY estado')},
                'fila_capi': {r[0]: r[1] for r in c.execute('SELECT estado, COUNT(*) FROM capi_fila GROUP BY estado')},
                'quarentena': {r[0]: r[1] for r in c.execute('SELECT motivo, COUNT(*) FROM quarentena GROUP BY motivo')},
                'recusas_24h': {r[0]: r[1] for r in c.execute('SELECT motivo, COUNT(*) FROM recusa WHERE recebido_em>=? '
                                                               'GROUP BY motivo', (agora - 86400,))},
            }

    # --------------------------------------------------------------------------------------- retenção
    def purgar(self, agora=None):
        agora = int(agora or time.time())
        with self._usar() as c:
            a = c.execute("UPDATE abandono SET nome=NULL, email=NULL, telefone=NULL, "
                          "estado=CASE WHEN estado='aberto' THEN 'expirado' ELSE estado END "
                          "WHERE apagar_contato_em<=? AND (nome IS NOT NULL OR email IS NOT NULL OR telefone IS NOT NULL "
                          "OR estado='aberto')", (agora,)).rowcount
            v = c.execute('DELETE FROM visita WHERE criado_em<?', (agora - VISITA_TTL,)).rowcount
            q = c.execute('DELETE FROM recusa WHERE recebido_em<?', (agora - 30 * 86400,)).rowcount
        return {'abandonos_sem_contato': a, 'visitas_apagadas': v, 'recusas_apagadas': q}
