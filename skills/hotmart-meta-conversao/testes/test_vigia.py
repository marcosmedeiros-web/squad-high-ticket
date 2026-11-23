"""Vigia: venda aprovada na API que o webhook não trouxe. Hotmart falsa, nenhuma chamada sai."""
import io
import json
import sys
import time
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apoio  # noqa: E402
import banco  # noqa: E402
import hotmart_api as ha  # noqa: E402
import vigia  # noqa: E402


class HotmartFalsa:
    """Responde o token e as páginas de sales/history que o teste mandar. Grava as rotas pedidas."""
    def __init__(self, paginas, status_token=200):
        self.paginas = list(paginas)
        self.status_token = status_token
        self.pedidos = []

    def __call__(self, req, timeout):
        self.pedidos.append((req.get_method(), req.full_url.split('?')[0]))
        if 'oauth/token' in req.full_url:
            return self.status_token, json.dumps({'access_token': 'tok-falso'}).encode()
        p = self.paginas.pop(0)
        if isinstance(p, int):
            return p, b''
        return 200, json.dumps(p).encode()


def venda(tx, aprovado_ha_min=60, produto=213344):
    return {'product': {'id': produto}, 'purchase': {'transaction': tx, 'status': 'APPROVED',
                                                      'approved_date': int((time.time() - aprovado_ha_min * 60) * 1000)}}


def pagina(itens, total=None, prox=None):
    info = {'total_results': len(itens) if total is None else total, 'results_per_page': 500}
    if prox:
        info['next_page_token'] = prox
    return {'items': itens, 'page_info': info}


class TestVigia(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        cred = self.cx.dir / 'hotmart.env'
        apoio.Caixa._segredo(cred, 'HOTMART_CLIENT_ID=id-teste\nHOTMART_CLIENT_SECRET=seg-teste\nHOTMART_BASIC=YmFzaWM=\n')
        avisos = self.cx.dir / 'avisos.jsonl'
        self.cx.perfil_env.write_text(self.cx.perfil_env.read_text() +
                                      f'HM_HOTMART_CRED_ARQUIVO={cred}\nHM_AVISO_CANAL=arquivo:{avisos}\n')
        self.avisos = avisos
        self.cx.subir()
        self.p = self.cx.perfil()
        self.b = banco.Banco(self.p['dados_dir'])

    def tearDown(self):
        self.cx.fechar()

    def _rodar(self, paginas):
        falsa = HotmartFalsa(paginas)
        err = io.StringIO()
        with redirect_stderr(err):
            rc, res = vigia.rodar(self.p, self.b, ha.Cliente(self.p['hotmart_cred_arquivo'], abrir=falsa))
        return rc, res, err.getvalue(), falsa

    def test_venda_que_o_webhook_trouxe_esta_coberta(self):
        self.cx.hotmart(apoio.compra_atual(transacao='HP11112222333344'))
        rc, res, _, falsa = self._rodar([pagina([venda('HP11112222333344')])])
        self.assertEqual((rc, res['estado']), (0, 'COBERTO'))
        self.assertTrue(all(m in ('POST', 'GET') for m, _ in falsa.pedidos))
        self.assertEqual([u for m, u in falsa.pedidos if m == 'GET'],
                         ['https://developers.hotmart.com/payments/api/v1/sales/history'])

    def test_venda_sem_webhook_e_buraco_com_hash8_e_sem_codigo_cru(self):
        self.cx.hotmart(apoio.compra_atual(transacao='HP11112222333344'))
        rc, res, log, _ = self._rodar([pagina([venda('HP11112222333344'), venda('HP99998888777766')])])
        self.assertEqual((rc, res['estado'], len(res['faltam'])), (1, 'BURACO', 1))
        self.assertFalse(res['webhook_desativado_provavel'])
        aviso = self.avisos.read_text()
        self.assertIn(res['faltam'][0]['hash8'], aviso)
        for texto in (aviso, log, json.dumps(res)):
            self.assertNotIn('HP99998888777766', texto)

    def test_sem_nenhum_evento_aponta_webhook_desativado(self):
        rc, res, _, _ = self._rodar([pagina([venda('HP99998888777766')])])
        self.assertEqual(rc, 1)
        self.assertTrue(res['webhook_desativado_provavel'])

    def test_venda_recente_dentro_da_tolerancia_nao_e_buraco(self):
        rc, res, _, _ = self._rodar([pagina([venda('HP99998888777766', aprovado_ha_min=5)])])
        self.assertEqual(rc, 0)

    def test_aviso_uma_vez_por_venda(self):
        self._rodar([pagina([venda('HP99998888777766')])])
        self._rodar([pagina([venda('HP99998888777766')])])
        self.assertEqual(len(self.avisos.read_text().splitlines()), 1)

    def test_api_fora_nao_vira_coberto(self):
        rc, res, _, _ = self._rodar([503])
        self.assertEqual((rc, res['estado']), (2, 'NAO_CONSEGUI_MEDIR'))
        self.assertEqual(res['motivo'], 'vendas:http503')

    def test_paginacao_com_transacao_repetida_nao_mede(self):
        rc, res, _, _ = self._rodar([pagina([venda('HP11112222333344')], total=2, prox='p2'),
                                     pagina([venda('HP11112222333344')], total=2)])
        self.assertEqual((rc, res['motivo']), (2, 'vendas:transacao_repetida'))

    def test_contagem_que_nao_fecha_nao_mede(self):
        rc, res, _, _ = self._rodar([pagina([venda('HP11112222333344')], total=3)])
        self.assertEqual((rc, res['motivo']), (2, 'vendas:contagem_nao_fecha'))

    def test_nao_mede_avisa_so_na_terceira(self):
        for _ in range(4):
            self._rodar([503])
        linhas = self.avisos.read_text().splitlines()
        self.assertEqual(len(linhas), 1)
        self.assertEqual(json.loads(linhas[0])['tipo'], 'vigia_nao_mede')

    def test_rota_fora_da_lista_recusa_antes_da_rede(self):
        c = ha.Cliente(self.p['hotmart_cred_arquivo'], abrir=HotmartFalsa([]))
        with self.assertRaises(ha.HotmartErro):
            c._get('/payments/api/v1/sales/refund', {})

    def test_sem_credencial_comparacao_desligada(self):
        p = dict(self.p, hotmart_cred_arquivo='')
        with redirect_stderr(io.StringIO()):
            rc, res = vigia.rodar(p, self.b)
        self.assertEqual((rc, res['comparacao']), (0, 'desligada'))


if __name__ == '__main__':
    unittest.main()
