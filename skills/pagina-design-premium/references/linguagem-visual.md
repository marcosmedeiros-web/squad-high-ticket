# Linguagem visual

Este arquivo foi escrito medindo páginas reais de alto padrão do mercado brasileiro de infoproduto, não por opinião. Os hexes abaixo saíram de amostragem de pixel.

O erro mais caro que esta skill já cometeu foi tratar "design bom" como sinônimo de *editorial suíço* — filete de 1px, radius zero, tudo alinhado à esquerda, zero sombra, zero gradiente. Isso é **uma** linguagem, e não é a que o mercado de lançamento usa. Páginas caras desse mercado são **quentes, com profundidade, fotográficas e coloridas**.

---

## O que foi medido

Tokens extraídos do CSS computado das páginas ao vivo, não estimados de screenshot.

### Sistema A — evento pago, registro de urgência

```css
/* tipografia */
--font-display:'Archivo';        /* weight 800 SEMPRE no display */
--font-body:'Albert Sans';
/* h1: 59px · w800 · ls -.038em · lh 1.03                        */
/* h2: 39–44px · w800 · ls -.034em · lh 1.06 · muitos CENTRALIZADOS */
/* p : 19.5px · w400 · lh 1.55 · cor #574E48  ← corpo GRANDE      */

--ink:#14100E; --ink-soft:#221B17; --body:#574E48;
--line:#E8E1D9; --line-soft:#F0EAE2;
--paper:#FFFFFF; --cream:#FAF7F3; --cream-deep:#F4EEE6;
--flame:#FF754F; --flame-light:#FF9C7E; --ember:#C82B00;
--blush:#FDEDE7; --blush-line:#F7D6C9;

--radius-xs:6px; --radius-sm:8px; --radius-md:10px; --radius-lg:14px; --radius-xl:18px;

--shadow-soft:0 1px 2px rgba(20,16,14,.04), 0 10px 30px -18px rgba(20,16,14,.18);
--shadow-lift:0 2px 4px rgba(20,16,14,.04), 0 30px 70px -34px rgba(20,16,14,.32);
--shadow-ember:0 18px 44px -20px rgba(200,43,0,.5);
--shadow-inset-line:inset 0 0 0 1px rgba(20,16,14,.06);
```

CTA: `linear-gradient(128.9deg,#1CE565,#1FAE2B)` · radius 8px · **weight 800** · font-size 12.5–15.5px · caixa alta · padding 16px 24px · sombra `--shadow-ember`.

### Sistema B — SaaS/IA, registro de controle

```css
--font-display:'Plus Jakarta Sans';   /* uma família só, 400 e 800 */
/* h1: 64px · w800 · ls -.025em · lh 1.08                */
/* h2: 54px · w800 · CENTRALIZADO                        */
/* p : 20px · w400 · lh 1.65 · cor #50506A               */

--ink:#0D0D22;        /* preto AZULADO */
--body:#50506A;
--shadow-near:0 2px 10px rgba(20,10,60,.04);
--shadow-far:0 18px 42px -16px rgba(40,20,90,.18);
```

CTA: `linear-gradient(135deg,#1FAE55,#0E783A)` · radius 12px · w800 · 16px · padding 19px 38px · sombra `rgba(17,122,59,.4) 0 12px 32px`.

---

## Os sete padrões que as duas compartilham

Estes não são opinião. Aparecem nas duas, medidos.

1. **Display em weight 800**, com tracking negativo forte (−.025 a −.038em) e `line-height` entre 1.03 e 1.08. Nada de 600 "elegante".
2. **Corpo em 19.5–20px**, com `line-height` 1.55–1.65. Isto é o achado mais fácil de aplicar e o mais ignorado: corpo em 16px faz a página parecer amadora ao lado dessas.
3. **Texto de corpo em cinza tingido**, nunca no preto do título — `#574E48` no sistema quente, `#50506A` no frio.
4. **CTA verde em gradiente da mesma família** nas duas páginas, apesar de accents completamente diferentes. No mercado brasileiro de infoproduto, verde é a cor de comprar. O botão não usa a cor do tema.
5. **Sombra colorida no CTA, na cor do tema e não na do botão.** O botão verde do sistema A tem halo laranja `rgba(200,43,0,.5)`. É o detalhe mais sofisticado dos dois sistemas.
6. **Sombras compostas**, sempre duas: uma rente de 1–2px com 4% de opacidade, e uma difusa de 30–70px com offset negativo grande. Sombra única é o que denuncia template.
7. **Borda por `inset 0 0 0 1px`** em vez de `border`. Não entra no box model, não desloca layout, e some quando não deve aparecer.

### Escala de radius, medida

`6 · 8 · 10 · 14 · 18` e `999` para pill. Card fica em 14. Botão em 8–12. O radius 20+ que eu costumava proibir não aparece; o radius 0 que eu costumava exigir também não.

---


## Profundidade

O recurso mais ausente em página gerada. Cada camada tem uma função.

```css
--sh-1:0 1px 2px rgba(21,17,14,.05);                          /* repouso */
--sh-2:0 4px 16px -4px rgba(21,17,14,.10);                    /* card em destaque */
--sh-3:0 18px 44px -12px rgba(21,17,14,.20);                  /* elemento flutuante */
--sh-glow:0 20px 60px -18px color-mix(in srgb,var(--accent) 45%,transparent);
```

**Sobreposição sobre foto** — cards de credencial saindo por cima da imagem:

```html
<div style="position:relative">
  <img src="foto.webp" alt="" style="border-radius:20px;width:100%">
  <div class="card" style="position:absolute;right:-8px;bottom:14%;max-width:250px;box-shadow:var(--sh-3)">
    <span class="lab">Professor</span>
    <strong>Nome</strong>
    <ul class="mini"><li>Credencial verificável</li><li>Segunda credencial</li></ul>
  </div>
</div>
```

No mobile, os cards saem do absoluto e viram lista abaixo da foto — `position:static` dentro do media query. Card sobreposto em 390px é ilegível.

**Pilha de notificações** — mock forte para prova social de venda. Empilhe 3–4 com opacidade decrescente e leve deslocamento:

```html
<div class="notifs">
  <div class="notif">…</div>
  <div class="notif" style="opacity:.55;transform:translateX(6px) scale(.985)">…</div>
  <div class="notif" style="opacity:.25;transform:translateX(12px) scale(.97)">…</div>
</div>
```

**Brilho no escuro** — a seção escura não é preta chapada. Um radial quente atrás do conteúdo:

```css
.dark{background:var(--ink);position:relative;overflow:hidden}
.dark::before{content:"";position:absolute;inset:auto -20% -45% 20%;height:70%;
  background:radial-gradient(ellipse at center,color-mix(in srgb,var(--accent) 55%,transparent),transparent 68%);
  filter:blur(60px);pointer-events:none}
```

---

## Sistema de pastéis

Como uma página fica **colorida sem ficar feia**. Derive 5 pastéis e o texto/ícone escuro de cada um. Todos com a mesma saturação baixa e a mesma luminância — é a uniformidade que faz parecer sistema.

```css
--p-1:#FDE8DC; --p-1-ink:#9A4A22;   /* pêssego  */
--p-2:#FBF0D2; --p-2-ink:#8A6512;   /* manteiga */
--p-3:#DFEDDF; --p-3-ink:#2F6340;   /* sálvia   */
--p-4:#DEE9F7; --p-4-ink:#264D80;   /* céu      */
--p-5:#E9E2F5; --p-5-ink:#4C3A78;   /* lilás    */
```

Uso: cada tile/card de um conjunto pega um pastel **diferente**. O texto do tile usa a **tinta global da página**, não um tom escuro derivado do pastel — foi assim na referência medida, e fica mais coeso. O `-ink` derivado serve só para o ícone, quando você quiser que ele destaque. Isso é o oposto da regra antiga desta skill, e está certo — a referência B faz exatamente assim com ~18 tiles e funciona.

```html
<span class="tile" style="background:var(--p-3);color:var(--p-3-ink)">
  <svg class="ic"><use href="#ic-alta"/></svg>
  <span>Escala vencedores</span>
</span>
```

Limite: pastéis só em **fundo de tile**, nunca em fundo de seção inteira, nunca em botão, nunca em texto de corpo.

---

## Marca-texto

Destaque de trecho dentro do parágrafo. Custa nada e é um dos recursos mais visíveis das duas referências.

```css
.mk{background:var(--accent-soft);padding:.06em .3em;border-radius:.28em;
    box-decoration-break:clone;-webkit-box-decoration-break:clone;font-weight:600}
```

O `box-decoration-break:clone` é obrigatório — sem ele o destaque quebra torto quando a frase pula de linha.

Regra: no máximo **duas** marcações por parágrafo, e nenhuma com mais de 6 palavras. Marcar tudo é marcar nada.

---

## Headline com palavra colorida

As duas referências fazem: headline em preto, **uma linha ou duas palavras** no accent.

```html
<h1>O maior faturamento<br><span class="ac">da sua vida</span></h1>
```
```css
h1{font-weight:800;letter-spacing:-.035em;line-height:1.03}
.ac{color:var(--accent)}
```

Escolha a parte colorida pelo **conteúdo**: colore o benefício, não o verbo. "O maior faturamento **da sua vida**" — o que a pessoa quer é a segunda parte.

---

## Molduras de dispositivo

Mock dentro de moldura de notebook ou celular. É o que faz um painel parecer produto em vez de tabela HTML.

```html
<div class="laptop">
  <div class="screen"><!-- mock da UI, fundo escuro --></div>
  <div class="base"></div>
</div>
```
```css
.laptop .screen{background:#15131A;border-radius:12px 12px 3px 3px;padding:1rem;border:8px solid #2A2730;border-bottom:0}
.laptop .base{height:11px;background:linear-gradient(#C9C7D0,#9B99A4);border-radius:0 0 9px 9px;
  margin-inline:-5%;box-shadow:var(--sh-2)}
```

Para produto de evento/ingresso, a moldura equivalente é o **bilhete com entalhe**:

```css
.ticket{position:relative;background:var(--surface);border-radius:16px;overflow:hidden;box-shadow:var(--sh-3)}
.ticket .head{background:var(--accent);color:#fff;padding:.7rem 1.1rem;display:flex;justify-content:space-between}
.ticket::before,.ticket::after{content:"";position:absolute;top:var(--notch,150px);width:22px;height:22px;
  border-radius:50%;background:var(--bg)}
.ticket::before{left:-11px} .ticket::after{right:-11px}
```

Ajuste `--notch` para a altura onde a linha pontilhada de corte deve passar.

---

## Composição orbital

Alternativa ao grid, quando o argumento é "muitas peças servindo uma coisa central". A referência B usa para "70 habilidades".

Desktop: um elemento central (mock, círculo, avatar) e os tiles posicionados em volta com `position:absolute` em ângulos calculados. Mobile: vira grid de 2 colunas, simples.

```css
.orbit{position:relative;min-height:520px;display:none}
@media(min-width:900px){.orbit{display:block}.orbit-grid{display:none}}
@media(max-width:899px){.orbit-grid{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}}
```

Sempre escreva as duas versões. Tentar fazer o orbital responder no mobile sempre quebra.

---

## Barra fixa com escassez

Topo grudado com logo, progresso de lote e CTA. Só use se a escassez for real e verificável.

```html
<header class="top">
  <img src="logo.svg" alt="" height="24">
  <div class="lote">
    <span class="lab">Lote 01</span>
    <div class="pbar"><i style="width:47%"></i></div>
    <span class="num">47%</span>
  </div>
  <a href="#oferta" class="btn sm">Garantir lote 1 →</a>
</header>
```

No mobile some o bloco do meio e fica logo + botão.

---

## O elemento-assinatura

A coisa única pela qual a página é lembrada. Toda página gerada precisa ter **um**, e ele precisa vir do assunto.

- Evento pago → o **bilhete com entalhe e número de série**
- Ferramenta de IA → a **constelação de habilidades** em volta do produto
- Programa de jornada → o **mapa de constância** preenchendo
- Serviço de auditoria → o **relatório com carimbo** e nota
- Curso de ofício → a **bancada com as ferramentas** dispostas

Teste: se você trocasse esse elemento pelo de outra página, alguém notaria? Se não, ele não é assinatura — é decoração.

Gaste a ousadia **nele**. Todo o resto fica disciplinado em volta.

---

## Registro B2B: a escala tipográfica encolhe

Terceira referência medida, nicho profissional (gestor de tráfego), contra as duas de infoproduto de consumo:

| | Display máximo | Corpo | Altura da página |
|---|---|---|---|
| Evento (consumo) | **59px** | 19,5px | longa |
| SaaS/IA (consumo) | **54px** | 20px | longa |
| B2B profissional | **40px** | **16px** | 6.960px — metade |

O público que compra ferramenta de trabalho lê texto menor e página mais curta sem reclamar. O display de 88px que funciona para "Emagreça até 5 kg" soa exagerado para "chegar aos R$30 mil de faturamento médio como gestor de tráfego".

**Regra:** quando o comprador é profissional e o produto é meio de trabalho, desça o display para 36–42px e o corpo para 16–17px. Quando é consumidor e o produto é transformação pessoal, suba para 50–60px e 19–20px.

Isso contradiz o "corpo sempre 19,5–20px" que eu tinha medido nas duas primeiras. O número não era universal — era do registro delas.

---

## Numeração de seção: uma terceira via

Já tínhamos a **pílula** (`01 · O CICLO`) e o **número marca-d'água** (contorno gigante ao fundo). A terceira referência usa uma marcação mais seca:

```css
.marcador{font-family:'IBM Plex Mono',monospace;font-size:14px;font-weight:400;
  color:var(--accent)}   /* conteúdo: / 01 */
```

Só a barra, o número e a cor de destaque. Sem fundo, sem borda, sem peso.

**Quando usar cada uma:**

| | Peso visual | Serve para |
|---|---|---|
| Pílula | médio | seções que precisam se anunciar |
| Marca-d'água | leve, decorativo | numerar sem ocupar espaço de leitura |
| `/ 01` em mono | mínimo | registro técnico, lista densa, público profissional |

A `/ 01` é a única das três que cabe **dentro** de um card sem competir com o título dele.

---

## Trio tipográfico com papéis estritos

A terceira referência separa três famílias por função, sem sobreposição:

- **Space Grotesk** w700 — só display
- **Inter** w400/w500 — só corpo
- **IBM Plex Mono** w400/w600 — só rótulo, numeração e dado

O mono não aparece em nenhuma frase corrida. É exclusivamente marcador. Isso é o que faz o `/ 01` ler como código de referência em vez de enfeite: em toda a página, mono significa "isto é rótulo, não é leitura".
