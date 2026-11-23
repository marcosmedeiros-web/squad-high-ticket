"""banco.py: o banco local (SQLite, biblioteca padrão) onde fica o TRÂNSITO de cada fluxo.

Tabelas
  eventos     uma linha por evento que ENTROU (ramo decidido na entrada; chave de negócio deduplica)
  passos      o que cada evento manda fazer (Mautic, WhatsApp...), com estado e motivo
  recusas     tentativa de entrada recusada (rota errada, hottok errado): conta, sem corpo
  estado      modo de cada fluxo, armação, pontos de controle internos
  provas      prova de trânsito (evento de teste que passou inteiro) por versão do desenho
  episodios   alarmes do vigia: um aviso por episódio, um aviso na volta
  envios_wa   chat_key de quem já recebeu WhatsApp (para não mandar duas vezes no mesmo dia)

Dado pessoal (e-mail, telefone, texto) só existe em `passos.dados`, e sai depois de AF_RETENCAO_DIAS.
Todo o resto guarda digital (sha256 curto), nunca o dado.
"""
import json
import os
import sqlite3
import time
from pathlib import Path

ESQUEMA = """
CREATE TABLE IF NOT EXISTS eventos(
  id INTEGER PRIMARY KEY, fluxo TEXT NOT NULL, recebido INTEGER NOT NULL, ramo TEXT NOT NULL,
  chave TEXT NOT NULL, contato_h TEXT, modo TEXT NOT NULL, desenho TEXT NOT NULL, nota TEXT,
  UNIQUE(fluxo, chave));
CREATE INDEX IF NOT EXISTS ev_fluxo ON eventos(fluxo, recebido);
CREATE TABLE IF NOT EXISTS passos(
  id INTEGER PRIMARY KEY, evento_id INTEGER NOT NULL, fluxo TEXT NOT NULL, ordem INTEGER NOT NULL,
  tipo TEXT NOT NULL, depende INTEGER, estado TEXT NOT NULL, dados TEXT NOT NULL, criado INTEGER NOT NULL,
  atualizado INTEGER NOT NULL, proxima_em INTEGER NOT NULL DEFAULT 0, tentativas INTEGER NOT NULL DEFAULT 0,
  post_feito INTEGER NOT NULL DEFAULT 0, motivo TEXT, saida TEXT NOT NULL DEFAULT '{}', visto INTEGER NOT NULL DEFAULT 0);
CREATE INDEX IF NOT EXISTS pa_estado ON passos(estado, proxima_em);
CREATE TABLE IF NOT EXISTS recusas(fluxo TEXT, em INTEGER, motivo TEXT);
CREATE TABLE IF NOT EXISTS estado(chave TEXT PRIMARY KEY, valor TEXT);
CREATE TABLE IF NOT EXISTS provas(fluxo TEXT, desenho TEXT, evento_id INTEGER, em INTEGER);
CREATE TABLE IF NOT EXISTS episodios(
  fluxo TEXT, tipo TEXT, aberto INTEGER, detalhe TEXT, avisado INTEGER DEFAULT 0, tentativas INTEGER DEFAULT 0,
  ultima_tentativa INTEGER DEFAULT 0, fechado INTEGER, volta_avisada INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS envios_wa(chat_key TEXT, em INTEGER, fluxo TEXT);
"""

TERMINAIS = ('feito', 'falhou', 'incerto', 'pulado', 'seco', 'retido_teste', 'expirado')


class Banco:
    def __init__(self, dados_dir):
        d = Path(dados_dir)
        d.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(d, 0o700)
        self.dir = d
        self.caminho = d / 'fluxos.sqlite3'
        novo = not self.caminho.exists()
        self.c = sqlite3.connect(str(self.caminho), timeout=20, isolation_level=None, check_same_thread=False)
        if novo:
            os.chmod(self.caminho, 0o600)
        self.c.row_factory = sqlite3.Row
        self.c.execute('PRAGMA journal_mode=WAL')
        self.c.execute('PRAGMA busy_timeout=20000')
        self.c.executescript(ESQUEMA)

    def fechar(self):
        self.c.close()

    # ------------------------------------------------------------------------------------------ estado
    def get(self, chave, padrao=None):
        r = self.c.execute('SELECT valor FROM estado WHERE chave=?', (chave,)).fetchone()
        return r['valor'] if r else padrao

    def set(self, chave, valor):
        if valor is None:
            self.c.execute('DELETE FROM estado WHERE chave=?', (chave,))
        else:
            self.c.execute('INSERT INTO estado(chave, valor) VALUES(?, ?) ON CONFLICT(chave) DO UPDATE SET valor=excluded.valor',
                           (chave, str(valor)))

    def modo(self, fluxo):
        return self.get(f'modo:{fluxo}', 'desligado')

    # ------------------------------------------------------------------------------------------ entrada
    def gravar_evento(self, fluxo, agora, ramo, chave, contato_h, modo, desenho, passos, nota=None):
        """Grava o evento e os passos numa transação. Devolve (evento_id, novo). Chave repetida = (id, False)."""
        with self.c:
            self.c.execute('BEGIN IMMEDIATE')
            r = self.c.execute('SELECT id FROM eventos WHERE fluxo=? AND chave=?', (fluxo, chave)).fetchone()
            if r:
                return r['id'], False
            cur = self.c.execute(
                'INSERT INTO eventos(fluxo, recebido, ramo, chave, contato_h, modo, desenho, nota) VALUES(?,?,?,?,?,?,?,?)',
                (fluxo, agora, ramo, chave, contato_h, modo, desenho, nota))
            eid = cur.lastrowid
            for p in passos:
                self.c.execute(
                    'INSERT INTO passos(evento_id, fluxo, ordem, tipo, depende, estado, dados, criado, atualizado, '
                    'proxima_em, motivo) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                    (eid, fluxo, p['ordem'], p['tipo'], p.get('depende'), p['estado'],
                     json.dumps(p['dados'], ensure_ascii=False), agora, agora, p.get('proxima_em', 0), p.get('motivo')))
            return eid, True

    def recusa(self, fluxo, agora, motivo):
        self.c.execute('INSERT INTO recusas(fluxo, em, motivo) VALUES(?,?,?)', (fluxo, agora, motivo))

    # ------------------------------------------------------------------------------------------ passos
    def devidos(self, agora, limite=200):
        return self.c.execute(
            "SELECT * FROM passos WHERE estado IN ('pendente', 'esperando', 'esperando_ok') AND proxima_em <= ? "
            'ORDER BY id LIMIT ?', (agora, limite)).fetchall()

    def passo(self, pid):
        return self.c.execute('SELECT * FROM passos WHERE id=?', (pid,)).fetchone()

    def passos_do_evento(self, eid):
        return self.c.execute('SELECT * FROM passos WHERE evento_id=? ORDER BY ordem', (eid,)).fetchall()

    def evento(self, eid):
        return self.c.execute('SELECT * FROM eventos WHERE id=?', (eid,)).fetchone()

    def atualizar_passo(self, pid, agora, **campos):
        if 'saida' in campos and not isinstance(campos['saida'], str):
            campos['saida'] = json.dumps(campos['saida'], ensure_ascii=False, sort_keys=True)
        campos['atualizado'] = agora
        sets = ', '.join(f'{k}=?' for k in campos)
        self.c.execute(f'UPDATE passos SET {sets} WHERE id=?', (*campos.values(), pid))

    def marcar_post(self, pid, agora):
        """Gravado ANTES do POST: se o processo morrer depois, o passo nunca é repetido às cegas."""
        self.c.execute('UPDATE passos SET post_feito=1, atualizado=? WHERE id=?', (agora, pid))

    def envio_wa_recente(self, chat_key, desde):
        return self.c.execute('SELECT 1 FROM envios_wa WHERE chat_key=? AND em>=? LIMIT 1',
                              (chat_key, desde)).fetchone() is not None

    def contar_wa(self, desde):
        return self.c.execute('SELECT count(*) n FROM envios_wa WHERE em>=?', (desde,)).fetchone()['n']

    def registrar_wa(self, chat_key, agora, fluxo):
        self.c.execute('INSERT INTO envios_wa(chat_key, em, fluxo) VALUES(?,?,?)', (chat_key, agora, fluxo))

    # ------------------------------------------------------------------------------------------ provas
    def gravar_prova(self, fluxo, desenho, eid, agora):
        self.c.execute('INSERT INTO provas(fluxo, desenho, evento_id, em) VALUES(?,?,?,?)', (fluxo, desenho, eid, agora))

    def prova(self, fluxo, desenho, desde):
        return self.c.execute('SELECT * FROM provas WHERE fluxo=? AND desenho=? AND em>=? ORDER BY em DESC LIMIT 1',
                              (fluxo, desenho, desde)).fetchone()

    # ------------------------------------------------------------------------------------------ leitura
    def ultimo_evento(self, fluxo, ramos=None):
        q = 'SELECT max(recebido) m FROM eventos WHERE fluxo=?'
        a = [fluxo]
        if ramos:
            q += ' AND ramo IN (%s)' % ','.join('?' * len(ramos))
            a += list(ramos)
        r = self.c.execute(q, a).fetchone()
        return r['m']

    def transito(self, fluxo, desde):
        ramos = {r['ramo']: r['n'] for r in self.c.execute(
            'SELECT ramo, count(*) n FROM eventos WHERE fluxo=? AND recebido>=? GROUP BY ramo', (fluxo, desde))}
        passos = {}
        for r in self.c.execute(
                'SELECT tipo, estado, count(*) n FROM passos WHERE fluxo=? AND criado>=? GROUP BY tipo, estado',
                (fluxo, desde)):
            passos.setdefault(r['tipo'], {})[r['estado']] = r['n']
        recusas = {r['motivo']: r['n'] for r in self.c.execute(
            'SELECT motivo, count(*) n FROM recusas WHERE fluxo=? AND em>=? GROUP BY motivo', (fluxo, desde))}
        return {'ramos': ramos, 'passos': passos, 'recusas': recusas}

    def contar_recusas(self, fluxo, desde):
        return self.c.execute('SELECT count(*) n FROM recusas WHERE fluxo=? AND em>=?', (fluxo, desde)).fetchone()['n']

    def passos_presos(self, fluxo, antes_de):
        return self.c.execute(
            "SELECT count(*) n FROM passos WHERE fluxo=? AND estado IN ('pendente', 'esperando') AND criado<? "
            "AND coalesce(motivo, '') NOT LIKE 'janela%'", (fluxo, antes_de)).fetchone()['n']

    def passos_falhos(self, fluxo):
        return self.c.execute(
            "SELECT estado, count(*) n FROM passos WHERE fluxo=? AND estado IN ('falhou', 'incerto', 'expirado') "
            'AND visto=0 GROUP BY estado', (fluxo,)).fetchall()

    def esperando_ok(self, fluxo):
        return self.c.execute("SELECT count(*) n FROM passos WHERE fluxo=? AND estado='esperando_ok'",
                              (fluxo,)).fetchone()['n']

    # ------------------------------------------------------------------------------------------ episódios
    def episodio_aberto(self, fluxo, tipo):
        return self.c.execute('SELECT rowid, * FROM episodios WHERE fluxo=? AND tipo=? AND fechado IS NULL',
                              (fluxo, tipo)).fetchone()

    def abrir_episodio(self, fluxo, tipo, agora, detalhe):
        self.c.execute('INSERT INTO episodios(fluxo, tipo, aberto, detalhe) VALUES(?,?,?,?)', (fluxo, tipo, agora, detalhe))
        return self.episodio_aberto(fluxo, tipo)

    def episodios_abertos(self):
        return self.c.execute('SELECT rowid, * FROM episodios WHERE fechado IS NULL').fetchall()

    def episodios_volta_pendente(self):
        return self.c.execute('SELECT rowid, * FROM episodios WHERE fechado IS NOT NULL AND avisado=1 '
                              'AND volta_avisada=0').fetchall()

    def episodio_set(self, rowid, **campos):
        sets = ', '.join(f'{k}=?' for k in campos)
        self.c.execute(f'UPDATE episodios SET {sets} WHERE rowid=?', (*campos.values(), rowid))

    # ------------------------------------------------------------------------------------------ retenção
    def purgar(self, agora, dias):
        limite = agora - dias * 86400
        n = self.c.execute("UPDATE passos SET dados='{}' WHERE criado<? AND dados!='{}' AND estado IN (%s)"
                           % ','.join('?' * len(TERMINAIS)), (limite, *TERMINAIS)).rowcount
        self.c.execute('DELETE FROM recusas WHERE em<?', (limite,))
        self.c.execute('DELETE FROM envios_wa WHERE em<?', (limite,))
        return n


def agora():
    return int(time.time())
