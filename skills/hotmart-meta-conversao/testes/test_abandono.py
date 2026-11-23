"""Abandono de carrinho (PURCHASE_OUT_OF_SHOPPING_CART): fica disponível para a ficha 2, resolve quando a mesma
pessoa compra, e o contato some na retenção."""
import io
import json
import os
import subprocess
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


class TestAbandono(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        self.cx.subir()
        self.b = banco.Banco(self.cx.dados)

    def tearDown(self):
        self.cx.fechar()

    def test_nome_do_evento_e_o_da_documentacao(self):
        self.assertEqual(apoio.fixture('hotmart-abandono-doc.json')['event'], 'PURCHASE_OUT_OF_SHOPPING_CART')

    def test_abandono_oficial_fica_aberto_com_contato(self):
        st, r, _ = self.cx.hotmart(apoio.abandono_atual())
        self.assertEqual((st, r['resultado']), (200, 'novo'))
        sem = self.b.abandonos('aberto')
        self.assertEqual(len(sem), 1)
        self.assertNotIn('email', sem[0])
        com = self.b.abandonos('aberto', com_contato=True)[0]
        self.assertEqual(com['email'], 'buyer@email.com.br')
        self.assertEqual(com['telefone'], '5531999999999')
        self.assertEqual(com['nome'], 'Buyer name')
        self.assertEqual((com['produto_id'], com['oferta']), ('3526906', 'n82b9jqz'))

    def test_abandono_reenviado_entra_uma_vez(self):
        for _ in range(3):
            self.cx.hotmart(apoio.abandono_atual())
        self.assertEqual(len(self.b.abandonos(None)), 1)

    def test_compra_depois_resolve_o_abandono(self):
        self.cx.hotmart(apoio.abandono_atual())
        compra = apoio.compra_atual(product__id=3526906, buyer__email='Buyer@Email.com.br ')
        self.cx.hotmart(compra)
        self.assertEqual(self.b.abandonos('aberto'), [])
        self.assertEqual(len(self.b.abandonos('comprou')), 1)

    def test_compra_pelo_telefone_tambem_resolve(self):
        self.cx.hotmart(apoio.abandono_atual())
        compra = apoio.compra_atual(product__id=3526906, buyer__email='outro@exemplo.com',
                                    buyer__checkout_phone='999999999', buyer__checkout_phone_code='31')
        self.cx.hotmart(compra)
        self.assertEqual(len(self.b.abandonos('comprou')), 1)

    def test_compra_antes_do_aviso_de_abandono(self):
        """A Hotmart confere o carrinho a cada 30 min: a compra pode chegar antes do abandono."""
        self.cx.hotmart(apoio.compra_atual(product__id=3526906, buyer__email='buyer@email.com.br'))
        self.cx.hotmart(apoio.abandono_atual())
        self.assertEqual(self.b.abandonos('aberto'), [])
        self.assertEqual(len(self.b.abandonos('comprou')), 1)

    def test_compra_de_outro_produto_nao_resolve(self):
        self.cx.hotmart(apoio.abandono_atual())
        self.cx.hotmart(apoio.compra_atual(buyer__email='buyer@email.com.br'))   # produto 213344
        self.assertEqual(len(self.b.abandonos('aberto')), 1)

    def test_boleto_impresso_nao_resolve(self):
        self.cx.hotmart(apoio.abandono_atual())
        self.cx.hotmart(apoio.compra_atual(evento='PURCHASE_BILLET_PRINTED', product__id=3526906,
                                           buyer__email='buyer@email.com.br'))
        self.assertEqual(len(self.b.abandonos('aberto')), 1)

    def test_retencao_apaga_contato_e_expira(self):
        self.cx.hotmart(apoio.abandono_atual())
        r = self.b.purgar(time.time() + 31 * 86400)
        self.assertEqual(r['abandonos_sem_contato'], 1)
        linha = self.b.abandonos(None, com_contato=True)[0]
        self.assertEqual((linha['email'], linha['telefone'], linha['nome'], linha['estado']),
                         (None, None, None, 'expirado'))

    def test_abandono_nao_vai_para_a_meta_por_padrao(self):
        self.cx.hotmart(apoio.abandono_atual())
        self.assertEqual(self.b.status()['fila_capi'], {})

    def test_abandono_personalizado_quando_ligado(self):
        cx = apoio.Caixa(CAPI_ABANDONO='personalizado')
        try:
            cx.subir()
            cx.hotmart(apoio.abandono_atual())
            meta = apoio.MetaFalsa()
            p = cx.perfil()
            p['modo'] = 'real'
            with redirect_stderr(io.StringIO()):
                capi_worker.ciclo(p, None, meta, {'HM_CAPI_ARMADO': '1'})
            ev = meta.chamadas[0]['data'][0]
            self.assertEqual(ev['event_name'], capi.EVENTO_ABANDONO_PERSONALIZADO)
            self.assertEqual(ev['event_id'], 'hm-abandono.0d7aa966-b887-4617-8c56-9e865bfc8ce4')
            self.assertNotIn('buyer@email.com', json.dumps(ev))
        finally:
            cx.fechar()

    def test_cli_abandonos(self):
        self.cx.hotmart(apoio.abandono_atual())
        env = dict(os.environ, HM_PERFIL=str(self.cx.perfil_env), PYTHONDONTWRITEBYTECODE='1')
        r = subprocess.run([sys.executable, '-I', '-B', str(apoio.MOTOR / 'eventos.py'), 'abandonos'],
                           env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn('buyer@email.com', r.stdout)
        r = subprocess.run([sys.executable, '-I', '-B', str(apoio.MOTOR / 'eventos.py'), 'abandonos', '--com-contato'],
                           env=env, capture_output=True, text=True, timeout=30)
        self.assertIn('buyer@email.com', r.stdout)
        self.assertEqual(json.loads(r.stdout.splitlines()[0])['estado'], 'aberto')


if __name__ == '__main__':
    unittest.main()
