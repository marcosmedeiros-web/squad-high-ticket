"""Receptor: hottok, dedupe, quarentena, resposta rápida e banco sem dado pessoal em claro."""
import json
import os
import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apoio  # noqa: E402


class TestHottok(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        self.cx.subir()

    def tearDown(self):
        self.cx.fechar()

    def _n_eventos(self):
        return sqlite3.connect(self.cx.dados / 'eventos.sqlite3').execute('SELECT COUNT(*) FROM evento').fetchone()[0]

    def test_hottok_certo_grava(self):
        st, r, _ = self.cx.hotmart(apoio.compra_atual())
        self.assertEqual(st, 200)
        self.assertEqual(r['resultado'], 'novo')
        self.assertEqual(self._n_eventos(), 1)

    def test_hottok_errado_401_e_nada_gravado(self):
        st, _, _ = self.cx.hotmart(apoio.compra_atual(), hottok='outro-valor-qualquer')
        self.assertEqual(st, 401)
        self.assertEqual(self._n_eventos(), 0)

    def test_hottok_ausente_401(self):
        st, _, _ = self.cx.hotmart(apoio.compra_atual(), hottok=None)
        self.assertEqual(st, 401)
        self.assertEqual(self._n_eventos(), 0)

    def test_hottok_no_corpo_nao_vale(self):
        """Na versão 2.0.0 o hottok vem no CABEÇALHO. Hottok certo dentro do corpo não autentica."""
        p = apoio.compra_atual()
        p['hottok'] = apoio.HOTTOK
        st, _, _ = self.cx.hotmart(p, hottok=None)
        self.assertEqual(st, 401)

    def test_prefixo_do_hottok_nao_vale(self):
        st, _, _ = self.cx.hotmart(apoio.compra_atual(), hottok=apoio.HOTTOK[:-1])
        self.assertEqual(st, 401)

    def test_recusa_fica_contada_no_status(self):
        self.cx.hotmart(apoio.compra_atual(), hottok='errado-errado')
        st, s = self.cx.get('/saude')
        self.assertEqual(st, 200)
        self.assertEqual(s['recusas_24h'].get('hottok_errado'), 1)


class TestDedupeEQuarentena(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        self.cx.subir()
        self.db = self.cx.dados / 'eventos.sqlite3'

    def tearDown(self):
        self.cx.fechar()

    def _q(self, sql):
        return sqlite3.connect(self.db).execute(sql).fetchall()

    def test_reenvio_do_mesmo_post_entra_uma_vez(self):
        p = apoio.compra_atual()
        for _ in range(5):                     # a Hotmart reenvia até 5 vezes
            st, r, _ = self.cx.hotmart(p)
            self.assertEqual(st, 200)
        self.assertEqual(self._q('SELECT COUNT(*) FROM evento')[0][0], 1)
        self.assertEqual(self._q('SELECT COUNT(*) FROM capi_fila')[0][0], 1)

    def test_reenvio_manual_com_id_novo_entra_uma_vez(self):
        self.cx.hotmart(apoio.compra_atual(id_evento='id-a'))
        st, r, _ = self.cx.hotmart(apoio.compra_atual(id_evento='id-b'))
        self.assertEqual((st, r['resultado']), (200, 'duplicado'))
        self.assertEqual(self._q('SELECT COUNT(*) FROM evento')[0][0], 1)

    def test_eventos_diferentes_da_mesma_transacao_entram(self):
        self.cx.hotmart(apoio.compra_atual(evento='PURCHASE_BILLET_PRINTED'))
        self.cx.hotmart(apoio.compra_atual(evento='PURCHASE_APPROVED'))
        self.assertEqual(self._q('SELECT COUNT(*) FROM evento')[0][0], 2)

    def test_json_literal_da_documentacao_vai_para_quarentena_com_200(self):
        """O exemplo de compra publicado pela Hotmart tem vírgula sobrando (não é JSON válido). Autenticado e
        ilegível responde 200 (a Hotmart desativa URL que dá erro) e fica contado na quarentena."""
        literal = (apoio.FIX / 'hotmart-compra-aprovada-doc.literal.txt').read_text()
        st, r, _ = self.cx.hotmart(literal)
        self.assertEqual(st, 200)
        self.assertTrue(r['quarentena'])
        self.assertEqual(self._q('SELECT motivo FROM quarentena'), [('json_invalido',)])
        self.assertEqual(self._q('SELECT COUNT(*) FROM evento')[0][0], 0)

    def test_versao_1_vai_para_quarentena(self):
        p = apoio.compra_atual()
        p['version'] = '1.0.0'
        st, r, _ = self.cx.hotmart(p)
        self.assertEqual(st, 200)
        self.assertEqual(self._q('SELECT motivo, versao FROM quarentena'), [('versao_nao_suportada', '1.0.0')])

    def test_evento_desconhecido_vai_para_quarentena(self):
        p = apoio.compra_atual()
        p['event'] = 'SUBSCRIPTION_CANCELLATION'
        st, r, _ = self.cx.hotmart(p)
        self.assertEqual(st, 200)
        self.assertEqual(self._q('SELECT motivo, nome_evento FROM quarentena'),
                         [('evento_fora_da_lista', 'SUBSCRIPTION_CANCELLATION')])

    def test_quarentena_nao_guarda_corpo(self):
        literal = (apoio.FIX / 'hotmart-compra-aprovada-doc.literal.txt').read_text()
        self.cx.hotmart(literal)
        bruto = b''.join(p.read_bytes() for p in self.db.parent.glob('eventos.sqlite3*'))
        self.assertNotIn(b'buyer@email.com', bruto)

    def test_corpo_grande_demais_nao_derruba(self):
        st, r, _ = self.cx.hotmart('{"x":"' + 'a' * 600000 + '"}')
        self.assertEqual(st, 200)
        self.assertTrue(r['quarentena'])

    def test_produto_fora_da_lista(self):
        self.cx.fechar()
        self.cx = apoio.Caixa(HM_PRODUTOS='999')
        self.cx.subir()
        self.db = self.cx.dados / 'eventos.sqlite3'
        st, r, _ = self.cx.hotmart(apoio.compra_atual())
        self.assertEqual(st, 200)
        self.assertEqual(self._q('SELECT motivo FROM quarentena'), [('produto_fora_da_lista',)])


class TestSemDadoPessoalEmClaro(unittest.TestCase):
    def test_compra_nao_guarda_contato_pix_nem_boleto(self):
        cx = apoio.Caixa()
        try:
            cx.subir()
            cx.hotmart(apoio.compra_atual())
            db = cx.dados / 'eventos.sqlite3'
            bruto = b''.join(p.read_bytes() for p in db.parent.glob('eventos.sqlite3*'))
            for proibido in (b'buyer@email.com', b'Buyer Name', b'999999999',
                             b'00020101021226780014', b'03399.33335', b'Chateaubriand', b'123456789'):
                self.assertNotIn(proibido, bruto, proibido)
        finally:
            cx.fechar()

    def test_banco_e_pasta_com_permissao_fechada(self):
        cx = apoio.Caixa()
        try:
            cx.subir()
            self.assertEqual(cx.dados.stat().st_mode & 0o777, 0o700)
            self.assertEqual((cx.dados / 'eventos.sqlite3').stat().st_mode & 0o777, 0o600)
            self.assertEqual((cx.dados / 'chave-local').stat().st_mode & 0o777, 0o600)
        finally:
            cx.fechar()


class TestFalhaDoLadoDeCa(unittest.TestCase):
    @unittest.skipIf(hasattr(os, 'geteuid') and os.geteuid() == 0, 'como root a permissão 400 não impede escrita')
    def test_banco_que_nao_grava_responde_500_para_a_hotmart_reenviar(self):
        cx = apoio.Caixa()
        try:
            cx.subir()
            cx.hotmart(apoio.compra_atual(transacao='HP00000000000001'))
            for p in cx.dados.glob('eventos.sqlite3*'):
                p.chmod(0o400)
            st, _, _ = cx.hotmart(apoio.compra_atual(transacao='HP00000000000002'))
            self.assertEqual(st, 500)
        finally:
            for p in cx.dados.glob('eventos.sqlite3*'):
                p.chmod(0o600)
            cx.fechar()

    def test_hottok_sumiu_responde_500_e_nao_aceita(self):
        cx = apoio.Caixa()
        try:
            cx.subir()
            cx.hottok.unlink()
            st, _, _ = cx.hotmart(apoio.compra_atual())
            self.assertEqual(st, 500)
        finally:
            cx.fechar()


class TestRotas(unittest.TestCase):
    def test_rota_desconhecida_404_e_saude_sem_pii(self):
        cx = apoio.Caixa()
        try:
            cx.subir()
            st, _, _ = cx.post('/v1/outra', {})
            self.assertEqual(st, 404)
            cx.hotmart(apoio.compra_atual())
            st, s = cx.get('/saude')
            self.assertEqual(st, 200)
            self.assertNotIn('buyer', json.dumps(s))
            self.assertEqual(s['eventos'], {'PURCHASE_APPROVED': 1})
        finally:
            cx.fechar()


if __name__ == '__main__':
    unittest.main()
