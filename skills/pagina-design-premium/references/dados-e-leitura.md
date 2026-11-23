# Dados e leitura

Vocabulário de visualização de dados. Renderizado em `assets/catalogo-dados.html`.

Este arquivo saiu de **prints**, não de extração de CSS — e isso é o ponto. O navegador entrega tokens, regras e estilos computados; ele não mostra que a legenda tem três linhas estruturadas, que a pílula está montada sobre a divisa entre duas seções, ou que a desordem do lado esquerdo foi desenhada de propósito. As duas fontes são complementares: **código para o sistema, imagem para a composição.**

---

## A regra que atravessa este arquivo

> Gráfico que só mostra número é decoração. Gráfico que **ensina a ler** é argumento.

Toda visualização daqui carrega uma referência (linha de empate, faixa semântica, anel de escala) e uma legenda que diz o que fazer com o dado. Sem isso, `0,7x` e `1,3x` são apenas "menor" e "maior".

---

## 1 · Legenda de três linhas

O achado mais reaproveitável. Cabe embaixo de qualquer gráfico.

```
O QUE É        Quantos param o scroll nos 3 primeiros segundos.
COMO LER       ● ótimo (≥20%)   ● na média (12–20%)   ● fraco (abaixo)
O QUE FAZER    Gancho alto sozinho não é vitória. Cruze com a conversão.
```

```css
.leg-l{display:grid;grid-template-columns:88px 1fr;gap:.9rem;align-items:start}
.leg-l > span:first-child{font-family:var(--fm);font-size:.62rem;letter-spacing:.11em;
  text-transform:uppercase;color:var(--accent);padding-top:.18rem}
@media(max-width:600px){.leg-l{grid-template-columns:1fr;gap:.15rem}}
```

A terceira linha é a que quase ninguém escreve e a que mais vale: sem "o que fazer", o leitor entende o gráfico e não faz nada.

---

## 2 · Barra divergente com linha de empate

Barras crescem da esquerda; uma **linha vertical de referência** marca o ponto de virada. Verde passa, vermelho não passa.

```css
.dv-tr{position:relative;height:26px;background:var(--paper-3);border-radius:7px;overflow:hidden}
.dv-linha{position:absolute;left:var(--x,42%);top:-6px;bottom:-6px;width:1.5px;background:var(--line-2);z-index:2}
```

A linha extrapola a barra em 6px em cima e embaixo — é o que a faz ler como régua e não como divisória.

---

## 3 · Colunas com faixa semântica

Cor por **faixa de valor**, não por item: verde ≥ meta, amarelo na média, vermelho abaixo. O rótulo fica logo acima da barra, no fluxo — não em `position:absolute`, que gruda no topo do contêiner e perde a relação com a altura.

```css
.col{display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:100%}
.col b{margin-bottom:.3rem}      /* no fluxo, acima da barra */
.col i{height:0;transition:height .9s cubic-bezier(.22,.61,.36,1)}
```

---

## 4 · Hub com raios

Três cards de cada lado, núcleo no meio, raios SVG ligando cada card ao centro.

```html
<svg class="raios" viewBox="0 0 1000 300" preserveAspectRatio="none">
  <g stroke="var(--line-2)" stroke-width="1" fill="none">
    <path d="M330,60 C420,60 440,150 470,150"/>
    <path d="M330,150 L470,150"/>
    <path d="M330,240 C420,240 440,150 470,150"/>
  </g>
</svg>
```

Prefira o hub à **órbita** quando os itens têm texto longo: a órbita só comporta rótulo de duas palavras. No mobile os conectores somem e vira lista.

### A armadilha do círculo que vira elipse

```css
/* errado — caixa 260×240, inset em % dá recuos diferentes nos dois eixos */
.hub-c{min-height:240px}
.hub-ring{position:absolute;inset:8%;border-radius:50%}   /* → elipse 238×223 */

/* certo — caixa quadrada, inset zero */
.hub-c{width:min(100%,300px);aspect-ratio:1;margin-inline:auto}
.hub-ring{position:absolute;inset:0;border-radius:50%}    /* → círculo real */
```

`border-radius:50%` numa caixa retangular **sempre** produz elipse, e `inset` em porcentagem calcula a partir de eixos diferentes. Confirme medindo: `Math.abs(w-h) < 2`.

### Conectores: por card, não por SVG global

Um SVG de raios com `preserveAspectRatio="none"` esticado sobre o grid inteiro **desloca os pontos de chegada** — no meu caso, 29px para fora do centro. E qualquer mudança na largura do container move tudo de novo.

O conector confiável sai do próprio card:

```css
@media(min-width:900px){
  .hub-card::after{content:"";position:absolute;top:50%;width:40px;height:1px;background:var(--line-2)}
  .hub-card::before{content:"";position:absolute;top:50%;width:7px;height:7px;border-radius:50%;
    transform:translateY(-50%);background:var(--paper);box-shadow:0 0 0 1.6px var(--line-2)}
  .hub-card.esq::after{right:-40px} .hub-card.esq::before{right:-43px}
  .hub-card.dir::after{left:-40px}  .hub-card.dir::before{left:-43px}
}
```

Ele acompanha o centro vertical do card sozinho, em qualquer altura de conteúdo. O **ponto na ponta** é o que faz a linha ler como terminada: sem ele, os conectores de cima e de baixo parecem parar no ar, porque a borda do círculo está mais afastada naquelas alturas.

Se você quiser a curva chegando exatamente na borda, é possível — mas exige travar a altura dos cards para que os centros caiam em ângulos conhecidos. Vale só quando o conteúdo é fixo.

---

## 5 · Linha de equação

`CUSTO + MARGEM + ROAS → ZONA DE DECISÃO`. Mostra **de onde sai** a recomendação. Torna a caixa-preta auditável e vale mais que um parágrafo explicando o critério.

O resultado à direita ganha fundo de destaque e o operador vira `→`, não `=`.

---

## 6 · Cards de zona

Vermelha / amarela / verde, cada uma com sparkline **na própria cor** e com inclinação coerente: a vermelha desce, a amarela oscila, a verde sobe. O conjunto lê antes de qualquer texto.

Fundo em `linear-gradient(180deg, tint, #FFF 60%)` — a cor mora no topo do card e some no corpo, então não briga com o texto.

---

## 7 · Radar

Cinco eixos, três anéis de referência. Leitura correta é **área e equilíbrio**, não pico — vale dizer isso na legenda, porque o instinto do leitor é procurar o eixo mais alto.

Anima com `opacity` + `scale(.82) → none` no polígono. Como é `transform`, observe o **contêiner**, nunca o polígono.

---

## 8 · Tag de estado

Sob o card, duas palavras nomeando a consequência: `Perda silenciosa` · `Lucro ilusório` · `Custo aumentando` · `Dinheiro queimado`.

```css
.estado{display:inline-flex;border-radius:8px;padding:.26rem .6rem;font-size:.72rem;font-weight:700;
  background:var(--bad-soft);color:var(--bad);margin-top:.6rem}
```

Faz o card virar diagnóstico. Sem ela, é só mais um item de lista.

---

## 9 · Dados borrados

```css
.borr{filter:blur(4px);user-select:none;pointer-events:none;opacity:.72}
```

Mostra dado real sem expor cliente. E o borrão **em si** comunica que aquilo é de verdade — mais convincente que um nome genérico inventado.

---

## 10 · Pílula na borda

A seção escura não simplesmente começa: ela é anunciada por um rótulo montado exatamente sobre a divisa.

```css
.pilula{position:absolute;top:0;left:50%;transform:translate(-50%,-50%);z-index:3;
  background:var(--paper);border-radius:999px;padding:.5rem 1.1rem;box-shadow:0 8px 20px rgba(0,0,0,.22)}
```

Detalhe pequeno, efeito grande: costura as duas seções em vez de empilhá-las.

---

## 11 · Caos × organizado

Esquerda: cards em **posições absolutas irregulares**, curvas tracejadas ligando alguns deles, bolinhas de interrogação nos vãos. Direita: grid perfeito com números.

A desordem precisa ser **desenhada**. Grid torto não passa a sensação — é preciso posição absoluta com valores que não seguem padrão nenhum.

---

## 12 · Abas

Trocam a **forma** de ver o mesmo dado, nunca o conteúdo. Se o número muda entre abas, o leitor perde a confiança nos dois.

```css
.aba[aria-selected="true"]{background:var(--paper-2);color:var(--accent);
  box-shadow:0 -1px 0 var(--line) inset,-1px 0 0 var(--line) inset,1px 0 0 var(--line) inset}
.painel{border-radius:0 14px 14px 14px;margin-top:-1px}
```

O `border-radius` com canto superior esquerdo em zero e o `margin-top:-1px` são o que fazem a aba ativa parecer colada no painel.

Use `role="tablist"` / `role="tab"` / `aria-selected` / `role="tabpanel"` — leitor de tela precisa, e custa três atributos.
