# Sistema de ícones

Sprite SVG inline. Cole o bloco inteiro logo depois de `<body>` e use com `<svg class="ic"><use href="#ic-NOME"/></svg>`.

Por que sprite e não ícone solto: garante que todos tenham a mesma grade (24), o mesmo traço (1.6), as mesmas pontas (round) e herdem `currentColor`. Ícone puxado de biblioteca diferente por card é um dos sinais mais visíveis de página montada às pressas.

## CSS

```css
.ic{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;flex:none}
.ic.lg{width:28px;height:28px;stroke-width:1.5}
.ic.sm{width:18px;height:18px;stroke-width:1.8}
/* selo: ícone dentro de um quadrado da cor de apoio */
.icbox{width:44px;height:44px;border-radius:calc(var(--radius) * .9);display:grid;place-items:center;flex:none}
```

## Uso

```html
<span class="icbox" style="background:var(--sup-2);color:var(--sup-2-ink)">
  <svg class="ic"><use href="#ic-folha"/></svg>
</span>
```

Regra: dentro de uma seção, todos os `icbox` usam a **mesma** cor de apoio. A cor muda de seção para seção, não de card para card — é isso que faz o conjunto parecer sistema em vez de arco-íris.

---

## O sprite

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>

<!-- ação e navegação -->
<symbol id="ic-check" viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5"/></symbol>
<symbol id="ic-seta" viewBox="0 0 24 24"><path d="M4 12h15m-6-6l6 6-6 6"/></symbol>
<symbol id="ic-mais" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="ic-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></symbol>
<symbol id="ic-play" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/></symbol>
<symbol id="ic-download" viewBox="0 0 24 24"><path d="M12 4v11m-4-4l4 4 4-4M5 19h14"/></symbol>

<!-- tempo e jornada -->
<symbol id="ic-relogio" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>
<symbol id="ic-calendario" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3.5v4M16 3.5v4"/></symbol>
<symbol id="ic-etapas" viewBox="0 0 24 24"><circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M6 8.5v7M11 6h9M11 18h9"/></symbol>
<symbol id="ic-repetir" viewBox="0 0 24 24"><path d="M4 9a8 8 0 0113.7-5.2M20 15a8 8 0 01-13.7 5.2"/><path d="M4 4.5V9h4.5M20 19.5V15h-4.5"/></symbol>

<!-- dado e resultado -->
<symbol id="ic-grafico" viewBox="0 0 24 24"><path d="M4 20h16M7 20v-6M12 20V7M17 20v-9"/></symbol>
<symbol id="ic-alta" viewBox="0 0 24 24"><path d="M4 16.5l5.5-5.5 3.5 3.5L20 7.5"/><path d="M14.5 7.5H20V13"/></symbol>
<symbol id="ic-alvo" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.6" fill="currentColor" stroke="none"/></symbol>
<symbol id="ic-filtro" viewBox="0 0 24 24"><path d="M4 6h16l-6.2 7.3V19l-3.6-2v-3.7z"/></symbol>
<symbol id="ic-lupa" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/></symbol>
<symbol id="ic-moeda" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5v9M14.6 9.8c-.5-.9-1.5-1.3-2.6-1.3-1.5 0-2.6.8-2.6 2s1 1.7 2.6 2 2.6.8 2.6 2-1.1 2-2.6 2c-1.1 0-2.1-.4-2.6-1.3"/></symbol>

<!-- pessoa e corpo -->
<symbol id="ic-pessoa" viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M5 20c0-3.6 3.1-6 7-6s7 2.4 7 6"/></symbol>
<symbol id="ic-pessoas" viewBox="0 0 24 24"><circle cx="9" cy="8.5" r="3"/><path d="M3 19c0-3.1 2.7-5 6-5s6 1.9 6 5"/><path d="M16 6.2a3 3 0 010 5.6M17.5 14.4c2 .7 3.5 2.2 3.5 4.6"/></symbol>
<symbol id="ic-coracao" viewBox="0 0 24 24"><path d="M12 19.5s-7.3-4.4-7.3-9.2A4.3 4.3 0 0112 8.2a4.3 4.3 0 017.3 2.1c0 4.8-7.3 9.2-7.3 9.2z"/></symbol>
<symbol id="ic-halter" viewBox="0 0 24 24"><rect x="2.5" y="8.8" width="3.6" height="6.4" rx="1.3"/><rect x="17.9" y="8.8" width="3.6" height="6.4" rx="1.3"/><rect x="6.6" y="10.4" width="10.8" height="3.2" rx="1.2"/></symbol>
<symbol id="ic-prato" viewBox="0 0 24 24"><path d="M3.5 11.5h17a8.5 8.5 0 01-17 0z"/><path d="M9.5 8c0-1.8 1.2-2.4 1.2-4M14 8c0-1.8 1.2-2.4 1.2-4"/></symbol>
<symbol id="ic-folha" viewBox="0 0 24 24"><path d="M20 4C11 4 5.5 7.5 5.5 14c0 3.3 2.2 5.5 5.5 5.5C17 19.5 20 13 20 4z"/><path d="M4.5 20c3-6.5 7-9.5 11-11"/></symbol>
<symbol id="ic-sono" viewBox="0 0 24 24"><path d="M20 14.2A8 8 0 019.8 4 8.2 8.2 0 1020 14.2z"/></symbol>

<!-- objeto e entrega -->
<symbol id="ic-livro" viewBox="0 0 24 24"><path d="M4 5.5c2.7-1 5.3-1 8 0v14c-2.7-1-5.3-1-8 0z"/><path d="M12 5.5c2.7-1 5.3-1 8 0v14c-2.7-1-5.3-1-8 0z"/></symbol>
<symbol id="ic-pagina" viewBox="0 0 24 24"><path d="M6 3.5h7.5L19 9v11.5H6z"/><path d="M13.5 3.5V9H19M9 13h7M9 16.5h5"/></symbol>
<symbol id="ic-chat" viewBox="0 0 24 24"><path d="M20.5 12.5c0 4-3.8 7-8.5 7-1.2 0-2.4-.2-3.4-.6L3.5 20.5l1.7-4.3a6.6 6.6 0 01-1.7-4.4c0-3.9 3.8-7 8.5-7s8.5 3.1 8.5 7z"/></symbol>
<symbol id="ic-escudo" viewBox="0 0 24 24"><path d="M12 3.5l7 2.8v5.4c0 4.2-2.8 7.3-7 8.8-4.2-1.5-7-4.6-7-8.8V6.3z"/><path d="M9 12l2.2 2.2L15.5 10"/></symbol>
<symbol id="ic-cadeado" viewBox="0 0 24 24"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8.2 10.5V7.8a3.8 3.8 0 017.6 0v2.7"/></symbol>
<symbol id="ic-estrela" viewBox="0 0 24 24"><path d="M12 4l2.5 5.2 5.5.8-4 3.9 1 5.6-5-2.7-5 2.7 1-5.6-4-3.9 5.5-.8z"/></symbol>
<symbol id="ic-faisca" viewBox="0 0 24 24"><path d="M12 3.5l1.9 5.6 5.6 1.9-5.6 1.9L12 18.5l-1.9-5.6-5.6-1.9 5.6-1.9z"/></symbol>
<symbol id="ic-chama" viewBox="0 0 24 24"><path d="M12 20.5c3.3 0 5.5-2.2 5.5-5.2 0-4.3-4-5.6-3.2-11.3-2.8 1.4-4.6 4-4.6 6.4 0 1.4-.8 2.1-1.6 2.1-.9 0-1.6-.7-1.6-2C5.6 12 6.5 20.5 12 20.5z"/></symbol>

</defs></svg>
```

---

## Escolhendo ícones para o nicho

Não use os 30. Escolha **6 a 10** que formem um conjunto coerente com o assunto, e repita esses.

| Nicho | Conjunto |
|---|---|
| Tráfego / negócios | `grafico` `alta` `alvo` `filtro` `moeda` `lupa` `repetir` `chat` |
| Saúde / bem-estar | `folha` `coracao` `halter` `prato` `sono` `relogio` `pessoas` `faisca` |
| Educação / curso | `livro` `pagina` `play` `etapas` `calendario` `pessoas` `download` `escudo` |
| Evento / lançamento | `calendario` `relogio` `pessoas` `play` `faisca` `alvo` `chama` `escudo` |

Se faltar um ícone específico, desenhe seguindo a mesma regra: `viewBox="0 0 24 24"`, sem `fill`, traço 1.6, pontas arredondadas, formas construídas na grade de 24 com margem de 3px nas bordas.

## Ícone não é decoração

Um ícone só entra se ele **identifica** — ajuda a pessoa a achar de novo o item que ela quer reler. Se todos os itens de uma lista têm ícone diferente sem significado, tire todos e deixe um marcador simples. Lista com 8 ícones aleatórios é pior que lista sem ícone nenhum.
