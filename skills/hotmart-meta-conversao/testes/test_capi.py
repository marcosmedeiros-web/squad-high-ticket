"""API de Conversões: formato, hash, event_id, degraus seco/teste/real, retentativa e limite de 7 dias.
A Meta aqui é sempre o transporte falso `apoio.MetaFalsa`. Nenhuma chamada sai."""
import hashlib
import io
import json
import sqlite3
import sys
import time
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apoio  # noqa: E402
import banco  # noqa: E402
import capi  # noqa: E402
import capi_worker  # noqa: E402
import hotmart_evento as he  # noqa: E402
import normaliza as nz  # noqa: E402

ARMADO = {'HM_CAPI_ARMADO': '1'}


def sha(v):
    return hashlib.sha256(v.encode()).hexdigest()


class TestMontagem(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        self.p = self.cx.perfil()

    def tearDown(self):
        self.cx.fechar()

    def _norm(self, **k):
        return he.ler(json.dumps(apoio.compra_atual(**k)).encode())

    def test_purchase_do_exemplo_oficial(self):
        ev, motivo = capi.evento_compra(self._norm(), self.p)
        self.assertEqual(motivo, 'ok')
        self.assertEqual(ev['event_name'], 'Purchase')
        self.assertEqual(ev['event_id'], 'hm.HP02316330308193')
        self.assertEqual(ev['custom_data']['currency'], 'BRL')
        self.assertEqual(ev['custom_data']['value'], 150.6)
        self.assertEqual(ev['custom_data']['order_id'], 'HP02316330308193')
        ud = ev['user_data']
        self.assertEqual(ud['em'], [sha('buyer@email.com')])
        # checkout_phone "999999999" + checkout_phone_code "31" + país BR = 5531999999999
        self.assertEqual(ud['ph'], [sha('5531999999999')])
        self.assertEqual(ud['fn'], [sha('buyer')])
        self.assertEqual(ud['ln'], [sha('name')])
        self.assertEqual(ud['ct'], [sha('belohorizonte')])
        self.assertEqual(ud['st'], [sha('mg')])
        self.assertEqual(ud['zp'], [sha('30150101')])
        self.assertEqual(ud['country'], [sha('br')])
        self.assertEqual(ev['action_source'], 'other')          # sem clique registrado, sem navegador
        self.assertEqual(ev['event_source_url'], 'https://site.exemplo.com.br/vendas')

    def test_nenhum_dado_pessoal_em_claro_no_evento(self):
        ev, _ = capi.evento_compra(self._norm(), self.p)
        texto = json.dumps(ev)
        for claro in ('buyer@email.com', 'Buyer', '999999999', 'Belo Horizonte', '30150101', 'CPF', 'pix'):
            self.assertNotIn(claro, texto)

    def test_valor_cheio(self):
        cx = apoio.Caixa(CAPI_VALOR='cheio')
        try:
            ev, _ = capi.evento_compra(self._norm(), cx.perfil())
            self.assertEqual(ev['custom_data']['value'], 134.0)
        finally:
            cx.fechar()

    def test_so_aprovacao_vira_purchase(self):
        for evento in ('PURCHASE_BILLET_PRINTED', 'PURCHASE_COMPLETE', 'PURCHASE_REFUNDED'):
            ev, motivo = capi.evento_compra(self._norm(evento=evento), self.p)
            self.assertIsNone(ev, evento)

    def test_recorrencia_2_nao_vira_purchase_por_padrao(self):
        ev, motivo = capi.evento_compra(self._norm(purchase__recurrence_number=2), self.p)
        self.assertEqual((ev, motivo), (None, 'recorrencia'))

    def test_purchase_sem_moeda_nao_vai(self):
        ev, motivo = capi.evento_compra(self._norm(purchase__price={'value': 10}), self.p)
        self.assertEqual((ev, motivo), (None, 'sem_valor_ou_moeda'))

    def test_purchase_desligado(self):
        cx = apoio.Caixa(CAPI_PURCHASE='desligado')
        try:
            ev, motivo = capi.evento_compra(self._norm(), cx.perfil())
            self.assertEqual((ev, motivo), (None, 'purchase_desligado'))
        finally:
            cx.fechar()

    def test_telefone_brasil_e_exterior(self):
        self.assertEqual(nz.telefone('31999999999', None, 'BR'), '5531999999999')
        self.assertEqual(nz.telefone('(31) 99999-9999', None, None), '5531999999999')
        self.assertEqual(nz.telefone('5531999999999', None, 'BR'), '5531999999999')
        self.assertEqual(nz.telefone('999999999', '31', 'BR'), '5531999999999')
        self.assertEqual(nz.telefone('+351 912 345 678', None, 'PT'), '351912345678')
        self.assertIsNone(nz.telefone('12345', None, 'BR'))

    def test_email_normalizado(self):
        self.assertEqual(nz.email('  John_Smith@Gmail.com '), 'john_smith@gmail.com')
        self.assertIsNone(nz.email('sem-arroba'))


class TestWorker(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa(CAPI_MODO='teste', CAPI_TEST_EVENT_CODE='TEST12345')
        self.cx.subir()
        self.p = self.cx.perfil()
        self.b = banco.Banco(self.p['dados_dir'])

    def tearDown(self):
        self.cx.fechar()

    def _ciclo(self, meta, ambiente=ARMADO, agora=None):
        err = io.StringIO()
        with redirect_stderr(err):
            c = capi_worker.ciclo(self.p, self.b, meta, ambiente, agora)
        return c, err.getvalue()

    def _fila(self):
        return sqlite3.connect(self.b.arquivo).execute('SELECT estado, payload, tentativas FROM capi_fila').fetchall()

    def test_envio_teste_vai_com_test_event_code_e_token_no_corpo(self):
        self.cx.hotmart(apoio.compra_atual())
        meta = apoio.MetaFalsa()
        c, log = self._ciclo(meta)
        self.assertEqual(c['enviado'], 1)
        ch = meta.chamadas[0]
        self.assertEqual(ch['url'], 'https://graph.facebook.com/v25.0/123456789012345/events')
        self.assertNotIn('access_token', ch['url'])
        self.assertEqual(ch['campos']['access_token'], apoio.TOKEN_META)
        self.assertEqual(ch['campos']['test_event_code'], 'TEST12345')
        self.assertEqual(len(ch['data']), 1)
        self.assertEqual(ch['data'][0]['event_id'], 'hm.HP02316330308193')
        self.assertNotIn(apoio.TOKEN_META, log)
        self.assertEqual(self._fila(), [('enviado', None, 1)])     # user_data apagado depois do desfecho

    def test_sem_drop_in_armado_fica_seco(self):
        self.cx.hotmart(apoio.compra_atual())
        meta = apoio.MetaFalsa()
        c, _ = self._ciclo(meta, ambiente={})
        self.assertEqual((c['seco'], meta.chamadas), (1, []))
        seco = (self.cx.dados / 'seco-capi.jsonl').read_text()
        self.assertIn('hm.HP02316330308193', seco)
        self.assertNotIn('buyer@email.com', seco)
        self.assertEqual((self.cx.dados / 'seco-capi.jsonl').stat().st_mode & 0o777, 0o600)

    def test_modo_seco_nao_chama_mesmo_armado(self):
        cx = apoio.Caixa(CAPI_MODO='seco')
        try:
            cx.subir()
            cx.hotmart(apoio.compra_atual())
            meta = apoio.MetaFalsa()
            with redirect_stderr(io.StringIO()):
                c = capi_worker.ciclo(cx.perfil(), None, meta, ARMADO)
            self.assertEqual((c['seco'], meta.chamadas), (1, []))
        finally:
            cx.fechar()

    def test_freio_de_mao(self):
        self.cx.hotmart(apoio.compra_atual())
        (self.cx.dados / 'PARAR-CAPI').touch()
        meta = apoio.MetaFalsa()
        c, _ = self._ciclo(meta)
        self.assertEqual((c['parado'], meta.chamadas), (1, []))
        self.assertEqual(self._fila()[0][0], 'pendente')

    def test_5xx_volta_para_fila_e_depois_vai(self):
        self.cx.hotmart(apoio.compra_atual())
        meta = apoio.MetaFalsa([(503, b''), (200, b'{"events_received":1}')])
        c, _ = self._ciclo(meta)
        self.assertEqual(c['adiado'], 1)
        c, _ = self._ciclo(meta)                     # ainda não venceu a espera
        self.assertEqual(len(meta.chamadas), 1)
        c, _ = self._ciclo(meta, agora=time.time() + 120)
        self.assertEqual(c['enviado'], 1)
        self.assertEqual(len(meta.chamadas), 2)

    def test_rede_fora_volta_para_fila(self):
        self.cx.hotmart(apoio.compra_atual())
        meta = apoio.MetaFalsa([OSError('rede')])
        c, _ = self._ciclo(meta)
        self.assertEqual(c['adiado'], 1)

    def test_400_de_validacao_vira_rejeitado(self):
        self.cx.hotmart(apoio.compra_atual())
        corpo = json.dumps({'error': {'message': 'Invalid parameter', 'code': 100, 'error_subcode': 2804003}}).encode()
        meta = apoio.MetaFalsa([(400, corpo)])
        c, log = self._ciclo(meta)
        self.assertEqual(c['rejeitado'], 1)
        self.assertIn('code=100', log)
        self.assertEqual(self._fila()[0][0], 'rejeitado')

    def test_evento_de_mais_de_7_dias_nao_e_enviado(self):
        """O exemplo oficial tem approved_date de 2009: vira velho_demais sem chamar a Meta (um evento velho
        derrubaria o lote inteiro)."""
        p = apoio.fixture('hotmart-compra-aprovada-doc.json')
        self.cx.hotmart(p)
        meta = apoio.MetaFalsa()
        c, _ = self._ciclo(meta)
        self.assertEqual((c['velho_demais'], meta.chamadas), (1, []))

    def test_teste_sem_test_event_code_recusa_o_perfil(self):
        import config
        with self.assertRaises(config.PerfilRecusado) as e:
            apoio.Caixa(CAPI_MODO='teste', CAPI_TEST_EVENT_CODE='').perfil()
        self.assertEqual(e.exception.motivo, 'campo_obrigatorio')

    def test_token_ilegivel_nao_envia(self):
        self.cx.hotmart(apoio.compra_atual())
        self.cx.token.chmod(0o644)
        meta = apoio.MetaFalsa()
        c, log = self._ciclo(meta)
        self.assertEqual(meta.chamadas, [])
        self.assertIn('permissao_segredo', log)

    def test_evento_sintetico_so_no_teste(self):
        with redirect_stderr(io.StringIO()):
            eid = capi_worker.evento_sintetico(self.p, self.b)
        self.assertTrue(eid.startswith('hm.TESTE'))
        meta = apoio.MetaFalsa()
        c, _ = self._ciclo(meta)
        self.assertEqual(c['enviado'], 1)
        cx = apoio.Caixa(CAPI_MODO='real')
        try:
            with redirect_stderr(io.StringIO()):
                self.assertIsNone(capi_worker.evento_sintetico(cx.perfil()))
        finally:
            cx.fechar()


if __name__ == '__main__':
    unittest.main()
