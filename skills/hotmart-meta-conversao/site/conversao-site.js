/* conversao-site.js: o lado do navegador da conversão (pacote hotmart-meta-conversao 1.0.0).
 *
 * No clique em um link de checkout da Hotmart ele faz três coisas com o MESMO identificador:
 *   1. dispara o evento no pixel da Meta com eventID sorteado aqui;
 *   2. avisa o receptor (POST /v1/visita, por sendBeacon) com esse eventID, o _fbp, o _fbc e o id da visita,
 *      e o receptor manda o mesmo evento pela API de Conversões com o mesmo event_id (a Meta junta os dois);
 *   3. põe xcod=<id da visita> no link do checkout. A Hotmart devolve o xcod no webhook da compra
 *      (data.purchase.origin.xcod), e o receptor usa isso para dar ao Purchase o fbp, o fbc e o navegador
 *      de quem clicou. Os parâmetros UTM não chegam no webhook; o xcod chega (Central de Ajuda da Hotmart).
 *
 * Configuração, ANTES deste arquivo:
 *   <script>window.HM_CONVERSAO = {
 *     endpoint: 'https://conversao.SEU-DOMINIO/v1/visita',
 *     evento: 'InitiateCheckout',          // ou 'CliqueCheckout' se o pixel da Hotmart já manda InitiateCheckout
 *     seletor: 'a[href*="pay.hotmart.com"]',
 *     exigeConsentimento: true             // true: só liga quando o site chamar HMConversao.ligar() após o aceite
 *   };</script>
 *
 * Página de obrigado PRÓPRIA (opcional): HMConversao.eventoCompraObrigado(transacao, valor, moeda) dispara o
 * Purchase do navegador com eventID "hm." + transacao, a mesma regra do servidor. Só use se o kit manda
 * Purchase (CAPI_PURCHASE=kit) e o pixel da Hotmart NÃO manda.
 */
(function (w, d) {
  'use strict';
  var C = w.HM_CONVERSAO || {};
  var ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  function aleatorio(n) {
    var a = new Uint8Array(n), s = '', i;
    (w.crypto || w.msCrypto).getRandomValues(a);
    for (i = 0; i < n; i++) { s += ALF.charAt(a[i] % 62); }
    return s;
  }
  function cookie(nome) {
    var m = d.cookie.match(new RegExp('(?:^|; )' + nome + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : '';
  }
  function fbc() {
    var c = cookie('_fbc'), p;
    if (c) { return c; }
    try { p = new URLSearchParams(w.location.search).get('fbclid'); } catch (e) { p = null; }
    return p ? 'fb.1.' + Date.now() + '.' + p : '';
  }
  function visitaId() {
    var v;
    try {
      v = w.sessionStorage.getItem('hm_visita');
      if (v) { return v; }
      v = aleatorio(22);
      w.sessionStorage.setItem('hm_visita', v);
      return v;
    } catch (e) { return aleatorio(22); }
  }
  function comXcod(href, id) {
    try {
      var u = new URL(href, w.location.href);
      u.searchParams.set('xcod', id);
      return u.toString();
    } catch (e) { return href; }
  }
  function aoClicar(ev) {
    var a = ev.currentTarget, id = visitaId(), eventId = 'ck.' + aleatorio(20);
    var nome = C.evento === 'CliqueCheckout' ? 'CliqueCheckout' : 'InitiateCheckout';
    if (typeof w.fbq === 'function') {
      if (nome === 'InitiateCheckout') { w.fbq('track', 'InitiateCheckout', {}, { eventID: eventId }); }
      else { w.fbq('trackCustom', nome, {}, { eventID: eventId }); }
    }
    if (C.endpoint && w.navigator && typeof w.navigator.sendBeacon === 'function') {
      var corpo = JSON.stringify({ visita_id: id, event_id: eventId, event_name: nome, fbp: cookie('_fbp'),
                                   fbc: fbc(), url: w.location.href });
      try { w.navigator.sendBeacon(C.endpoint, new Blob([corpo], { type: 'text/plain' })); } catch (e) { /* segue */ }
    }
    a.href = comXcod(a.href, id);
  }
  var ligado = false;
  function ligar() {
    if (ligado) { return; }
    ligado = true;
    var links = d.querySelectorAll(C.seletor || 'a[href*="pay.hotmart.com"]'), i;
    for (i = 0; i < links.length; i++) { links[i].addEventListener('click', aoClicar); }
  }
  w.HMConversao = {
    ligar: ligar,
    eventoCompraObrigado: function (transacao, valor, moeda) {
      if (typeof w.fbq !== 'function' || !transacao) { return null; }
      var eid = 'hm.' + transacao;
      w.fbq('track', 'Purchase', { value: valor, currency: moeda }, { eventID: eid });
      return eid;
    }
  };
  if (C.exigeConsentimento === false) { ligar(); }
})(window, document);
