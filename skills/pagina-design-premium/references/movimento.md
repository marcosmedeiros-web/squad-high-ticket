# Movimento

Animação em página de venda tem uma função só: **dirigir a atenção**. Movimento decorativo atrapalha a leitura, atrasa o LCP e é outro sinal de template.

Regras que valem para tudo neste arquivo:

- Anime só `transform` e `opacity`. Qualquer outra propriedade força layout e trava no celular.
- Nada acima da dobra anima na entrada. O hero aparece pronto — animar o hero atrasa a leitura da promessa.
- Duração entre 300 e 600ms. Acima disso a pessoa espera; abaixo, ela nem percebe.
- Todo bloco de movimento respeita `prefers-reduced-motion`.
- Máximo **três** técnicas acionadas por scroll por página (reveal, contador, preenchimento…).
- Loops decorativos contínuos (selo girando, marquee) contam à parte: no máximo **um** deles.

Base obrigatória em todo arquivo gerado:

```css
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}
}
```

---

## 1. Reveal com escalonamento

O básico bem-feito. A diferença do template é o **stagger**: itens irmãos entram em cascata, não todos juntos.

```css
.rv{opacity:0;transform:translateY(18px);transition:opacity .55s cubic-bezier(.2,.7,.3,1),transform .55s cubic-bezier(.2,.7,.3,1)}
.rv.in{opacity:1;transform:none}
.rv-group > *{opacity:0;transform:translateY(14px);transition:opacity .5s ease,transform .5s ease}
.rv-group.in > *{opacity:1;transform:none}
.rv-group.in > *:nth-child(1){transition-delay:0ms}
.rv-group.in > *:nth-child(2){transition-delay:70ms}
.rv-group.in > *:nth-child(3){transition-delay:140ms}
.rv-group.in > *:nth-child(4){transition-delay:210ms}
.rv-group.in > *:nth-child(5){transition-delay:280ms}
.rv-group.in > *:nth-child(6){transition-delay:350ms}
```

```js
const io=new IntersectionObserver(es=>es.forEach(e=>{
  if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}
}),{threshold:.12,rootMargin:'0px 0px -60px'});
document.querySelectorAll('.rv,.rv-group').forEach(el=>io.observe(el));
```

---

## 2. Contador de número

Só para números que são a prova. Um ou dois por página, nunca uma fileira inteira.

```html
<span class="num count" data-to="12480" data-prefix="R$ " data-dec="0">0</span>
```

```js
const fmt=(v,d)=>v.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
const cio=new IntersectionObserver(es=>es.forEach(e=>{
  if(!e.isIntersecting)return; cio.unobserve(e.target);
  const el=e.target, to=+el.dataset.to, d=+(el.dataset.dec||0), pre=el.dataset.prefix||'', suf=el.dataset.suffix||'';
  const t0=performance.now(), dur=1100;
  const tick=t=>{const p=Math.min((t-t0)/dur,1); const e2=1-Math.pow(1-p,3);
    el.textContent=pre+fmt(to*e2,d)+suf; if(p<1)requestAnimationFrame(tick);};
  requestAnimationFrame(tick);
},{threshold:.5});
document.querySelectorAll('.count').forEach(el=>cio.observe(el));
```

O `toLocaleString('pt-BR')` é o que garante ponto de milhar e vírgula decimal. Contador em formato americano numa página brasileira é erro visível.

---

## 3. Marquee

Faixa horizontal em movimento contínuo. Ótima para logos, pontos-chave, depoimentos curtos. Duplique o conteúdo no HTML para o loop fechar sem salto.

```css
.marquee{overflow:hidden;--gap:2.5rem;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.marquee-track{display:flex;gap:var(--gap);width:max-content;animation:mq 38s linear infinite}
.marquee:hover .marquee-track{animation-play-state:paused}
@keyframes mq{to{transform:translateX(calc(-50% - var(--gap)/2))}}
```

```html
<div class="marquee"><div class="marquee-track">
  <span>item</span><span>item</span><!-- … -->
  <span aria-hidden="true">item</span><span aria-hidden="true">item</span><!-- cópia idêntica -->
</div></div>
```

A máscara nas bordas é o detalhe que faz parecer intencional em vez de gambiarra.

---

## 4. Barra de progresso de leitura

Custa 6 linhas e dá sensação de página construída.

```css
.progress{position:fixed;top:0;left:0;height:2px;background:var(--accent);width:0;z-index:80;transition:width .1s linear}
```

```js
const pb=document.querySelector('.progress');
addEventListener('scroll',()=>{const h=document.body.scrollHeight-innerHeight;
  pb.style.width=(scrollY/h*100)+'%'},{passive:true});
```

---

## 5. Título grudado

O título da seção fica fixo enquanto os itens passam ao lado. Excelente para cronograma, módulos e lista longa. Só desktop.

```css
@media (min-width:900px){
  .stick-col{position:sticky;top:5rem;align-self:start}
}
```

Combina com `.split` — coluna esquerda grudada, coluna direita rolando.

---

## 6. Preenchimento por scroll (grade de progresso)

O motivo visual mais forte para produto de jornada (12 semanas, 30 dias, 8 módulos). Os quadradinhos preenchem conforme a pessoa desce.

```css
.gridfill{display:grid;grid-template-columns:repeat(12,1fr);gap:5px}
.gridfill i{aspect-ratio:1;border-radius:3px;background:var(--line);transition:background .4s ease,transform .4s ease}
.gridfill i.on{background:var(--accent);transform:scale(1.06)}
```

```js
document.querySelectorAll('.gridfill').forEach(g=>{
  const cells=[...g.querySelectorAll('i')];
  new IntersectionObserver(es=>es.forEach(e=>{ if(!e.isIntersecting)return;
    cells.forEach((c,i)=>setTimeout(()=>c.classList.add('on'), i*55));
  }),{threshold:.4}).observe(g);
});
```

---

## 7. Hover com intenção

Card não deve "flutuar". Deve responder de forma discreta e coerente com o registro.

```css
.card{transition:border-color .25s ease,transform .25s ease}
@media (hover:hover){
  .card.tap:hover{border-color:var(--accent);transform:translateY(-3px)}
}
```

No mobile, `hover` não existe — por isso o `@media (hover:hover)`. Sem isso o estado fica preso após o toque.

Link com sublinhado que cresce:

```css
.ul{background-image:linear-gradient(var(--accent),var(--accent));background-size:0 1.5px;background-position:0 100%;background-repeat:no-repeat;transition:background-size .3s ease}
.ul:hover{background-size:100% 1.5px}
```

---

## 8. Selo circular girando

Motivo de assinatura. Usa `textPath` em SVG.

```html
<svg viewBox="0 0 120 120" class="seal" width="104" height="104" aria-hidden="true">
  <defs><path id="c" d="M60,60 m-42,0 a42,42 0 1,1 84,0 a42,42 0 1,1 -84,0"/></defs>
  <text font-size="10.5" letter-spacing="3.4" fill="currentColor">
    <textPath href="#c">ACOMPANHAMENTO · 12 SEMANAS · AO VIVO · </textPath>
  </text>
</svg>
```
```css
.seal{animation:spin 22s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
```

---

## 9. Divisor orgânico

Separa seções sem linha reta. Só nos registros acolhedor e festival — no técnico fica errado.

```html
<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true">
  <path d="M0,32 C240,4 480,52 720,32 C960,12 1200,50 1440,26 L1440,60 L0,60 Z" fill="var(--bg-2)"/>
</svg>
```
```css
.wave{display:block;width:100%;height:clamp(30px,5vw,60px)}
```

---

## 10. Blob de fundo

Mancha de cor desfocada atrás do hero. Aqui está a **exceção legítima ao gradiente**: um gradiente radial de **uma família tonal** é sofisticado; o gradiente linear entre dois matizes saturados é o clichê.

```css
.blob{position:absolute;inset:auto;z-index:-1;filter:blur(70px);opacity:.55;pointer-events:none;
  border-radius:40% 60% 55% 45%/50% 45% 55% 50%}
.blob.a{width:min(56vw,520px);aspect-ratio:1;background:var(--sup-3);top:-8%;right:-12%}
.blob.b{width:min(44vw,400px);aspect-ratio:1;background:var(--sup-2);top:38%;left:-16%}
```

O contêiner precisa de `position:relative;overflow:hidden`. Use no máximo dois blobs, sempre em cores de apoio dessaturadas, nunca no accent.

---

## Duas armadilhas de CSS que só aparecem renderizadas

Ambas encontradas em produção, ambas invisíveis no código.

### 1 · `.rv` mata o `transform` de quem já tem um

`.rv{transform:translateY(18px)}` e `.rv.in{transform:none}` sobrescrevem o `transform` próprio de qualquer elemento. Um notebook com `perspective(2200px) rotateX(6deg)` que também carrega `.rv` **perde a perspectiva inteira** — vira um retângulo chapado, e nada no código denuncia.

Nunca aplique a classe de reveal no mesmo elemento que tem transform próprio. Envolva:

```html
<!-- errado --><div class="lap rv">…</div>
<!-- certo  --><div class="rv"><div class="lap">…</div></div>
```

Vale para qualquer par: `rotate`, `scale`, `perspective`, `skew`.

### 2 · `<i>` e `<span>` como barra não aceitam `width`

Elemento inline ignora `width` e `height`. Uma barra de gráfico escrita como `<i class="bar-fl">` com `width:83%` renderiza com **0px** e o gráfico aparece vazio — sem erro nenhum no console.

```css
/* errado */ .bar-fl{height:100%;width:0;transition:width 1s}
/* certo  */ .bar-fl{display:block;height:100%;width:0;transition:width 1s}
```

Vale para qualquer `<i>`, `<span>` ou `<em>` usado como elemento gráfico. Se você escolheu a tag pela brevidade, declare o `display`.

### 3 · Observar o elemento que você mesmo escondeu

`IntersectionObserver` calcula a razão pela **área visível**. Se o elemento se esconde com `clip-path:inset(0 100% 0 0)`, `transform:scale(0)` ou `visibility:hidden`, a razão é sempre 0 e o observer **nunca dispara**. Ele se esconde e por isso nunca é revelado.

```js
/* errado — o alvo é o próprio elemento clipado */
document.querySelectorAll('.spark').forEach(s=>
  new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)s.classList.add('in')}),
    {threshold:.4}).observe(s));

/* certo — observa o contêiner, aplica a classe no filho */
document.querySelectorAll('.spark').forEach(function(s){
  var alvo=s.closest('.dev')||s.parentElement;
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){s.classList.add('in');io.disconnect()}})},{threshold:.15});
  io.observe(alvo);
});
```

`opacity:0` e `translateY` **não** têm esse problema — a área continua a mesma. Só clip, scale e visibility.

**Threshold alto também engana.** `.5` num elemento alto exige metade dele na tela; num scroll rápido isso pode não acontecer. Use `.15`–`.3` para revelar e reserve `.5` para contador.

### 4 · Contador que nasce em zero

`<span class="count" data-to="2800">0</span>` mostra **"Mais de 0 pessoas"** se o JS falhar, se o observer não disparar, ou no instante antes da animação. É o pior estado possível justamente no número que serve de prova.

```html
<!-- errado --><span class="count" data-to="2800">0</span>
<!-- certo  --><span class="count" data-to="2800">2.800</span>
```

O conteúdo inicial é o **valor final formatado**; o JS sobrescreve com a contagem a partir do zero. Sem JS, sem observer ou com erro de sintaxe, a página continua correta — só não anima. Vale para qualquer número que a página usa como argumento.

### 5 · `margin:0 auto` num item de grid desliga o `stretch`

Item de grid com `width:auto` estica por padrão. Basta uma margem automática para o `justify-self:stretch` ser cancelado e o elemento virar shrink-to-fit. Um notebook com `max-width:530px` numa coluna de 554px renderizou com **173px** por causa disso.

```css
/* errado */ .lap{margin:0 auto;max-width:530px}
/* certo  */ .lap{width:100%;margin-inline:auto;max-width:530px}
```

Como pegar: meça no navegador em vez de olhar o código.

```js
[...document.querySelector('.devices').children].map(c=>({
  cls:c.className, w:Math.round(c.getBoundingClientRect().width),
  maxw:getComputedStyle(c).maxWidth, t:getComputedStyle(c).transform.slice(0,40)}))
```

---

## O que não fazer

| Efeito | Por que não |
|---|---|
| Parallax de fundo com `background-attachment:fixed` | quebra no iOS e trava o scroll |
| Entrada animada no hero | atrasa a leitura da promessa e piora o LCP |
| Typewriter na headline | a headline é a coisa mais importante da página; escondê-la letra por letra é sabotagem |
| Contador regressivo falso que reinicia | destrói confiança e é reprovado na revisão |
| Carrossel automático de depoimentos | ninguém consegue terminar de ler. Use marquee com pausa no hover, ou grade |
| Biblioteca de animação (AOS, GSAP, Framer) | 40–120kb para o que 20 linhas de CSS resolvem |
| Cursor customizado | não existe no mobile, atrapalha no desktop |
| Animação em `width`, `height`, `top`, `left` | força reflow, engasga em celular antigo |

---

## Keyframes medidos das referências

Extraídos do navegador. Use estes valores em vez de inventar tempos: eles já foram calibrados em produção. Entre as duas páginas há **22 keyframes**.

```css
/* pulso de status — melhor que pseudo-elemento escalando:
   usa spread de box-shadow, não cria camada nem custa paint */
@keyframes pulse-live{
  0%,100%{opacity:1;box-shadow:0 0 0 0 rgb(var(--accent-rgb)/.55)}
  60%    {opacity:.85;box-shadow:0 0 0 7px rgb(var(--accent-rgb)/0)}
}

/* entrada ao rolar — 14px, não 18 */
@keyframes rise{0%{opacity:0;transform:translateY(14px)}100%{opacity:1;transform:none}}

/* flutuação suave — translate3d liga aceleração de GPU */
@keyframes float-soft{0%,100%{transform:translateZ(0)}50%{transform:translate3d(0,-7px,0)}}

/* flutuação de item JÁ CENTRADO por transform — preserva o translate */
@keyframes orbitFloat{
  0%,100%{transform:translate(-50%,-50%)}
  50%    {transform:translate(-50%,calc(-50% - 9px))}
}

/* três pontinhos digitando — pico em 30%, mais vivo que em 50% */
@keyframes typing{
  0%,60%,100%{transform:translateY(0);opacity:.45}
  30%        {transform:translateY(-3px);opacity:1}
}

/* varredura de brilho sobre botão ou card */
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(320%)}}

/* marquee por distância absoluta, não por -50% */
@keyframes lr{0%{transform:translateX(0)}100%{transform:translateX(-89.25rem)}}

/* piscar discreto */
@keyframes blink{50%{opacity:.25}}
```

### Duas armadilhas que estes keyframes evitam

**`orbitFloat` preserva o `translate(-50%,-50%)`.** Item posicionado com `left:27%;top:19%;transform:translate(-50%,-50%)` que recebe uma animação de `transform` **perde a centralização** e salta. A animação precisa repetir o translate original — é o mesmo tipo de colisão do `.rv` acima.

**`pulse-live` não usa pseudo-elemento.** A minha versão anterior escalava um `::after` até 2.6×. Funciona, mas cria uma camada extra por elemento. `box-shadow` com spread crescente e alfa decrescente dá o mesmo anel sem camada nenhuma — e por isso as referências usam em dezenas de pontos sem custo.

### Borda cônica girando (`@property`)

A técnica mais avançada das duas páginas: registrar um ângulo como propriedade tipada para poder animá-lo.

```css
@property --angle{syntax:'<angle>';initial-value:0deg;inherits:false}
@keyframes spin-border{100%{--angle:360deg}}
.borda-viva{
  border:1px solid transparent;border-radius:14px;
  background:linear-gradient(var(--paper),var(--paper)) padding-box,
             conic-gradient(from var(--angle),transparent 0 70%,var(--accent) 85%,transparent 100%) border-box;
  animation:spin-border 4s linear infinite;
}
```

Sem `@property` o ângulo não interpola e a animação simplesmente não roda. Use com parcimônia — um elemento por página, no card em destaque.
