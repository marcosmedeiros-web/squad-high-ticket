"""Instalador e perfil: --so-conferir não escreve nada, MOTIVO= na primeira linha, recusa de venda em dobro."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apoio  # noqa: E402
import config  # noqa: E402

INSTALADOR = apoio.RAIZ / 'instalar.sh'


def foto(raiz):
    return sorted((str(p.relative_to(raiz)), p.stat().st_mode, p.stat().st_size)
                  for p in Path(raiz).rglob('*'))


class TestPerfil(unittest.TestCase):
    def _motivo(self, **k):
        cx = apoio.Caixa(**k)
        try:
            cx.perfil()
            return None
        except config.PerfilRecusado as e:
            return e.motivo
        finally:
            cx.fechar()

    def test_purchase_em_dobro_recusado(self):
        self.assertEqual(self._motivo(HOTMART_PIXEL_NATIVO_COMPRA='ligado', CAPI_PURCHASE='kit'), 'purchase_em_dobro')

    def test_purchase_desligado_com_pixel_nativo_passa(self):
        self.assertIsNone(self._motivo(HOTMART_PIXEL_NATIVO_COMPRA='ligado', CAPI_PURCHASE='desligado'))

    def test_checkout_em_dobro_recusado(self):
        self.assertEqual(self._motivo(HOTMART_PIXEL_NATIVO_CHECKOUT='ligado', SITE_EVENTO_CLIQUE='InitiateCheckout'),
                         'checkout_em_dobro')

    def test_checkout_nativo_ligado_vira_evento_personalizado(self):
        cx = apoio.Caixa(HOTMART_PIXEL_NATIVO_CHECKOUT='ligado')
        try:
            self.assertEqual(cx.perfil()['evento_clique'], 'CliqueCheckout')
        finally:
            cx.fechar()

    def test_declaracao_do_pixel_nativo_e_obrigatoria(self):
        self.assertEqual(self._motivo(HOTMART_PIXEL_NATIVO_COMPRA=None), 'campo_obrigatorio')

    def test_preencher_recusa(self):
        self.assertEqual(self._motivo(HM_HOTTOK_ARQUIVO='PREENCHER'), 'campo_nao_preenchido')

    def test_chave_com_nome_errado_recusa(self):
        self.assertEqual(self._motivo(CAPI_MODOO='seco'), 'chave_desconhecida')

    def test_escuta_publica_recusa(self):
        self.assertEqual(self._motivo(HM_ESCUTA='0.0.0.0'), 'escuta_nao_local')

    def test_real_com_test_event_code_recusa(self):
        self.assertEqual(self._motivo(CAPI_MODO='real', CAPI_TEST_EVENT_CODE='TEST1'), 'valor_invalido')

    def test_exemplo_do_pacote_recusa_ate_ser_preenchido(self):
        with self.assertRaises(config.PerfilRecusado) as e:
            config.carregar(str(apoio.RAIZ / 'perfil' / 'perfil.exemplo.env'))
        self.assertEqual(e.exception.motivo, 'campo_nao_preenchido')

    def test_comentario_no_fim_da_linha(self):
        cx = apoio.Caixa()
        try:
            cx.perfil_env.write_text(cx.perfil_env.read_text().replace('CAPI_MODO=seco', 'CAPI_MODO=seco   # nada sai'))
            self.assertEqual(cx.perfil()['modo'], 'seco')
        finally:
            cx.fechar()


class TestInstalador(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa()
        self.destino = Path(tempfile.mkdtemp(prefix='hm-destino-'))
        self.cfg = Path(tempfile.mkdtemp(prefix='hm-cfg-'))
        self.env = dict(os.environ, XDG_CONFIG_HOME=str(self.cfg), PYTHONDONTWRITEBYTECODE='1')

    def tearDown(self):
        self.cx.fechar()
        shutil.rmtree(self.destino, ignore_errors=True)
        shutil.rmtree(self.cfg, ignore_errors=True)

    def _rodar(self, *args):
        return subprocess.run(['bash', str(INSTALADOR), '--perfil', str(self.cx.perfil_env), '--destino',
                               str(self.destino / 'hm'), '--python', sys.executable, *args],
                              env=self.env, capture_output=True, text=True, timeout=600)

    def test_so_conferir_nao_escreve_nada(self):
        antes = (foto(self.destino), foto(self.cfg), foto(self.cx.dir))
        r = self._rodar('--so-conferir')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('Nada foi escrito', r.stdout)
        self.assertEqual((foto(self.destino), foto(self.cfg), foto(self.cx.dir)), antes)

    def test_recusa_de_perfil_sobe_motivo_na_primeira_linha(self):
        self.cx.perfil_env.write_text(self.cx.perfil_env.read_text()
                                      .replace('HOTMART_PIXEL_NATIVO_COMPRA=desligado', 'HOTMART_PIXEL_NATIVO_COMPRA=ligado'))
        r = self._rodar('--so-conferir')
        self.assertEqual(r.returncode, 78)
        self.assertEqual(r.stderr.splitlines()[0], 'MOTIVO=purchase_em_dobro')

    def test_hottok_aberto_recusa(self):
        self.cx.hottok.chmod(0o644)
        r = self._rodar('--so-conferir')
        self.assertEqual(r.returncode, 3)
        self.assertEqual(r.stderr.splitlines()[0], 'MOTIVO=permissao_segredo')

    def test_saida_nunca_mostra_o_hottok(self):
        r = self._rodar('--so-conferir')
        self.assertNotIn(apoio.HOTTOK, r.stdout + r.stderr)

    def test_instala_parado_e_idempotente(self):
        r = self._rodar('--sem-systemd', '--sem-autoteste')
        self.assertEqual(r.returncode, 0, r.stderr)
        unidades = self.cfg / 'systemd' / 'user'
        self.assertTrue((unidades / 'hotmart-meta-receptor.service').is_file())
        self.assertFalse((unidades / 'hotmart-meta-capi.service.d').exists())     # sem --com-capi = seco
        self.assertIn('systemctl --user enable --now', r.stdout)
        texto = (unidades / 'hotmart-meta-receptor.service').read_text()
        self.assertNotIn('@', texto.replace('default.target', ''))
        antes = foto(self.destino), foto(self.cfg)
        r2 = self._rodar('--sem-systemd', '--sem-autoteste')
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertEqual((foto(self.destino), foto(self.cfg)), antes)

    def test_com_capi_escreve_drop_in_e_sem_capi_tira(self):
        self._rodar('--sem-systemd', '--sem-autoteste', '--com-capi')
        dropin = self.cfg / 'systemd' / 'user' / 'hotmart-meta-capi.service.d' / '60-capi-armado.conf'
        self.assertIn('HM_CAPI_ARMADO=1', dropin.read_text())
        self._rodar('--sem-systemd', '--sem-autoteste', '--sem-capi')
        self.assertFalse(dropin.exists())

    def test_perfil_dentro_do_destino_recusa(self):
        r = subprocess.run(['bash', str(INSTALADOR), '--perfil', str(self.cx.perfil_env), '--destino',
                            str(self.cx.dir), '--python', sys.executable, '--so-conferir'],
                           env=self.env, capture_output=True, text=True, timeout=60)
        self.assertEqual(r.returncode, 2)
        self.assertEqual(r.stderr.splitlines()[0], 'MOTIVO=perfil_dentro_do_pacote')


if __name__ == '__main__':
    unittest.main()
