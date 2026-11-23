"""Deduplicação contra o pixel: o servidor manda o MESMO event_name e o MESMO event_id que o navegador usou.

A Meta junta navegador e servidor por (event_name, event_id) no mesmo pixel, em até 48 h. O teste prova os dois
lados com a mesma régua: o snippet do site (rodado de verdade no node, com fbq e sendBeacon falsos) e o
receptor + worker (com a Meta falsa)."""
import io
import json
import shutil
import subprocess
import sys
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apoio  # noqa: E402
import capi_worker  # noqa: E402

ORIGEM = 'https://site.exemplo.com.br'
UA = 'Mozilla/5.0 (teste) Navegador/1.0'
JS_CAMINHO = apoio.RAIZ / 'site' / 'conversao-site.js'

RODAR_SNIPPET = r"""
const vm = require('vm'), fs = require('fs');
const codigo = fs.readFileSync(process.argv[1], 'utf8');
const chamadasFbq = [], beacons = [], ouvintes = [];
const link = { href: 'https://pay.hotmart.com/X123?off=abc', addEventListener: (t, f) => ouvintes.push(f) };
const armazenamento = {};
const janela = {
  HM_CONVERSAO: { endpoint: 'https://conversao.exemplo.com.br/v1/visita', evento: process.argv[2],
                  exigeConsentimento: process.argv[3] === 'sim' },
  location: { href: 'https://site.exemplo.com.br/vendas?fbclid=ABC123', search: '?fbclid=ABC123' },
  crypto: require('crypto').webcrypto,
  sessionStorage: { getItem: k => armazenamento[k] || null, setItem: (k, v) => { armazenamento[k] = v; } },
  navigator: { sendBeacon: (url, blob) => { beacons.push({ url, blob }); return true; } },
  fbq: function () { chamadasFbq.push(Array.from(arguments)); },
};
const documento = { cookie: '_fbp=fb.1.1596403881668.1116446470', querySelectorAll: () => [link] };
const ctx = { window: janela, document: documento, URL, URLSearchParams, Blob, Uint8Array, Date, JSON, RegExp,
              decodeURIComponent };
vm.createContext(ctx);
vm.runInContext(codigo, ctx);
const antes = ouvintes.length;
if (process.argv[3] === 'sim') { janela.HMConversao.ligar(); }
ouvintes.forEach(f => f({ currentTarget: link }));
Promise.all(beacons.map(b => b.blob.text())).then(textos => {
  const compra = janela.HMConversao.eventoCompraObrigado('HP02316330308193', 150.6, 'BRL');
  console.log(JSON.stringify({ antes, fbq: chamadasFbq, beacons: textos.map(t => JSON.parse(t)),
                               url_beacon: beacons.map(b => b.url), href: link.href, compra }));
});
"""


def rodar_snippet(evento='InitiateCheckout', consentimento='nao'):
    r = subprocess.run(['node', '-e', RODAR_SNIPPET, str(JS_CAMINHO), evento, consentimento],
                       capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        raise AssertionError(r.stderr)
    s = json.loads(r.stdout)
    s['compra_fbq'] = [c for c in s['fbq'] if c[1] == 'Purchase']
    s['fbq'] = [c for c in s['fbq'] if c[1] != 'Purchase']      # só o clique de checkout
    return s


@unittest.skipUnless(shutil.which('node'), 'node ausente: o lado do navegador não foi testado')
class TestSnippet(unittest.TestCase):
    def test_fbq_e_aviso_levam_o_mesmo_event_id(self):
        s = rodar_snippet()
        self.assertEqual(len(s['fbq']), 1)
        chamada = s['fbq'][0]
        self.assertEqual(chamada[:2], ['track', 'InitiateCheckout'])
        self.assertEqual(chamada[3]['eventID'], s['beacons'][0]['event_id'])
        self.assertEqual(s['beacons'][0]['event_name'], 'InitiateCheckout')
        self.assertEqual(s['beacons'][0]['fbp'], 'fb.1.1596403881668.1116446470')
        self.assertTrue(s['beacons'][0]['fbc'].startswith('fb.1.'))
        self.assertTrue(s['beacons'][0]['fbc'].endswith('.ABC123'))
        self.assertIn('xcod=' + s['beacons'][0]['visita_id'], s['href'])

    def test_evento_personalizado_usa_trackcustom(self):
        s = rodar_snippet('CliqueCheckout')
        self.assertEqual(s['fbq'][0][:2], ['trackCustom', 'CliqueCheckout'])
        self.assertEqual(s['beacons'][0]['event_name'], 'CliqueCheckout')

    def test_compra_do_navegador_usa_a_regra_do_servidor(self):
        s = rodar_snippet()
        self.assertEqual(s['compra'], 'hm.HP02316330308193')
        self.assertEqual(s['compra_fbq'][0][3]['eventID'], 'hm.HP02316330308193')
        self.assertEqual(s['compra_fbq'][0][2], {'value': 150.6, 'currency': 'BRL'})

    def test_com_consentimento_so_liga_depois_do_aceite(self):
        s = rodar_snippet(consentimento='sim')
        self.assertEqual(s['antes'], 0)
        self.assertEqual(len(s['fbq']), 1)


class TestServidorRepeteOEventId(unittest.TestCase):
    def setUp(self):
        self.cx = apoio.Caixa(CAPI_MODO='real')
        self.cx.subir()
        self.p = self.cx.perfil()

    def tearDown(self):
        self.cx.fechar()

    def _visita(self, event_id='ck.AbCdEfGhIjKlMnOpQrSt', visita_id='VisitaTeste0123456789A', origem=ORIGEM,
                nome='InitiateCheckout'):
        corpo = {'visita_id': visita_id, 'event_id': event_id, 'event_name': nome,
                 'fbp': 'fb.1.1596403881668.1116446470', 'fbc': 'fb.1.1554763741205.AbCdEfGh',
                 'url': ORIGEM + '/vendas'}
        return self.cx.post('/v1/visita', json.dumps(corpo),
                            {'Origin': origem, 'Content-Type': 'text/plain', 'User-Agent': UA,
                             'X-Forwarded-For': '203.0.113.7'})

    def _enviar(self):
        meta = apoio.MetaFalsa()
        with redirect_stderr(io.StringIO()):
            capi_worker.ciclo(self.p, None, meta, {'HM_CAPI_ARMADO': '1'})
        return [ev for ch in meta.chamadas for ev in ch['data']]

    def test_checkout_do_servidor_igual_ao_do_navegador(self):
        st, _, h = self._visita()
        self.assertEqual(st, 200)
        self.assertEqual(h.get('Access-Control-Allow-Origin'), ORIGEM)
        evs = self._enviar()
        self.assertEqual(len(evs), 1)
        ev = evs[0]
        self.assertEqual((ev['event_name'], ev['event_id']), ('InitiateCheckout', 'ck.AbCdEfGhIjKlMnOpQrSt'))
        self.assertEqual(ev['action_source'], 'website')
        ud = ev['user_data']
        self.assertEqual(ud['client_user_agent'], UA)
        self.assertEqual(ud['client_ip_address'], '203.0.113.7')
        self.assertEqual(ud['fbp'], 'fb.1.1596403881668.1116446470')
        self.assertEqual(ev['event_source_url'], ORIGEM + '/vendas')

    def test_aviso_repetido_nao_duplica(self):
        self._visita()
        self._visita()
        self.assertEqual(len(self._enviar()), 1)

    def test_origem_fora_da_lista_403(self):
        st, _, _ = self._visita(origem='https://outro.exemplo.net')
        self.assertEqual(st, 403)
        self.assertEqual(self._enviar(), [])

    def test_evento_diferente_do_perfil_nao_vai_para_meta(self):
        st, _, _ = self._visita(nome='CliqueCheckout')
        self.assertEqual(st, 200)
        self.assertEqual(self._enviar(), [])

    def test_compra_com_xcod_herda_o_navegador_do_clique(self):
        self._visita()
        compra = apoio.compra_atual(purchase__origin={'xcod': 'VisitaTeste0123456789A'})
        self.cx.hotmart(compra)
        evs = {e['event_name']: e for e in self._enviar()}
        p = evs['Purchase']
        self.assertEqual(p['event_id'], 'hm.HP02316330308193')
        self.assertEqual(p['action_source'], 'website')
        self.assertEqual(p['user_data']['fbc'], 'fb.1.1554763741205.AbCdEfGh')
        self.assertEqual(p['user_data']['client_user_agent'], UA)

    @unittest.skipUnless(shutil.which('node'), 'node ausente')
    def test_ponta_a_ponta_snippet_receptor_meta(self):
        """O aviso que o snippet monta, entregue ao receptor, sai na Meta com o eventID que foi para o fbq."""
        s = rodar_snippet()
        b = s['beacons'][0]
        st, _, _ = self.cx.post('/v1/visita', json.dumps(b), {'Origin': ORIGEM, 'Content-Type': 'text/plain',
                                                              'User-Agent': UA})
        self.assertEqual(st, 200)
        ev = self._enviar()[0]
        self.assertEqual(ev['event_id'], s['fbq'][0][3]['eventID'])
        self.assertEqual(ev['event_name'], s['fbq'][0][1])


if __name__ == '__main__':
    unittest.main()
