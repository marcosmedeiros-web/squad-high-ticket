# Mobile

Extraído do CSS das referências. **O breakpoint delas é `760px`**, não 768, com um segundo corte em `360px` só para o botão flutuante.

O ponto central: elas não escrevem uma media query por componente. Escrevem uma **camada defensiva** que protege a página inteira, e depois abrem exceções nomeadas.

---

## A camada defensiva

Cole inteira. Ela sozinha resolve a maior parte dos defeitos de mobile.

```css
@media (max-width:760px){
  /* 1 · tipografia re-escalada em vw, com piso e teto */
  h1{font-size:clamp(30px,8.4vw,50px)!important;line-height:1.1!important}
  h2{font-size:clamp(25px,6.6vw,40px)!important;line-height:1.2!important}
  h3{font-size:clamp(20px,5vw,27px)!important}

  /* 2 · quebras de linha trocam de lado */
  h1 br,h2 br{display:none!important}
  h1 br.m-br,h2 br.m-br{display:inline!important}

  /* 3 · todo grid vira 1 coluna, com lista de exceções */
  [style*="grid-template-columns"]{grid-template-columns:1fr!important;max-width:100%!important}
  [style*="grid-template-columns"] > *{min-width:0!important}

  /* 4 · todo flex horizontal ganha quebra */
  [style*="display:flex"]:not([style*="flex-direction:column"]){flex-wrap:wrap!important}

  /* 5 · a página inteira centraliza */
  section{text-align:center}
}
```

### Por que cada uma existe

**1 · Tipografia em `vw` com `clamp`.** No desktop a escala é fluida por container; no mobile ela precisa responder à largura da tela. `8.4vw` num iPhone SE (375px) dá 31,5px; num 430px dá 36px. O piso de 30px impede headline ilegível e o teto de 50px impede estouro em tablet pequeno.

**2 · Troca de `<br>`.** Esta é a que eu mais errei. Um `<br>` colocado para quebrar bem no desktop vira quebra errada no mobile — some com ele e ofereça uma quebra própria:

```html
<h1>Seu imóvel pode valer<br class="d-br"> muito mais<br class="m-br"> que o aluguel</h1>
```
```css
.m-br{display:none}
@media(max-width:760px){.d-br{display:none}.m-br{display:inline}}
```

**3 · O colapso geral de grid.** Qualquer elemento com `grid-template-columns` inline vira uma coluna. É o que permite montar dezenas de grids ad-hoc sem escrever media query para cada um. O `min-width:0` nos filhos é obrigatório — é a causa número um de scroll horizontal em grid e flex, porque o padrão `min-width:auto` impede o filho de encolher abaixo do próprio conteúdo.

**4 · `flex-wrap` universal.** Mesma lógica: linha horizontal que não quebra é a segunda causa de overflow.

**5 · `section{text-align:center}`.** No desktop as referências misturam esquerda e centro; no mobile **centralizam tudo**. Em coluna estreita o alinhamento à esquerda perde a função de criar ritmo e só deixa a página torta.

---

## Exceções nomeadas

Grids que **não** podem colapsar são re-proporcionados, nunca empilhados:

```css
@media (max-width:760px){
  [style*="grid-template-columns"]:not([style*="210px 1fr 52px"]):not([style*="110px 1fr 148px"]){
    grid-template-columns:1fr!important
  }
  /* a exceção vira uma proporção menor, não uma pilha */
  [style*="210px 1fr 52px"]{grid-template-columns:84px 1fr 38px!important;gap:10px!important}
  [style*="210px 1fr 52px"] > div:first-child{font-size:10.5px!important;line-height:1.25!important}
}
```

Use quando a leitura depende de as colunas continuarem lado a lado: linha de métrica com rótulo + barra + valor, item de tabela, linha de cronograma.

---

## Reordenar, não só empilhar

Empilhar na ordem do HTML costuma colocar a foto no lugar errado. As referências reordenam explicitamente:

```css
@media (max-width:760px){
  .hist-img{order:0!important;margin:22px 0 6px!important}
  .hist-body{order:1!important}
}
```

Regra prática: no mobile, **a imagem vem antes do texto** em blocos de autoridade e de história — ela ancora a leitura. Em blocos de argumento com mock, o texto vem primeiro.

---

## Elementos absolutos no mobile

Cards flutuando sobre foto, balões e selos: no mobile eles **saem do absoluto** ou são reposicionados com `inset` + unidades de viewport.

```css
@media (max-width:760px){
  .balao{inset:auto auto 126px 0!important;width:min(62vw,226px)!important}
  .arte{padding-bottom:104px!important}   /* abre espaço pro elemento reposicionado */
}
```

O `padding-bottom` no contêiner é o detalhe: sem ele o elemento reposicionado sobrepõe o conteúdo seguinte.

Alternativa mais simples, e a que esta skill prefere: `position:static` no mobile e o card vira item de lista abaixo da foto.

---

## Classes auxiliares só de mobile

Prefixe com `m-` e declare que só existem abaixo do breakpoint. As referências usam `.m-center-row`, `.m-br`. Deixa explícito no HTML que aquele elemento tem comportamento próprio no celular.

---

## Checklist de validação

Renderize em **390px** e confira, nesta ordem:

- [ ] `document.documentElement.scrollWidth === 390` (zero scroll horizontal)
- [ ] Nenhum `<br>` de desktop quebrando errado
- [ ] Nenhum grid preso em 2+ colunas espremidas
- [ ] Nenhum card absoluto sobrepondo texto
- [ ] Headline entre 30 e 40px
- [ ] Botão com no mínimo 48px de altura e texto sem quebrar em 3 linhas
- [ ] Barra fixa inferior não cobre o último bloco (`body{padding-bottom}`)
- [ ] Tabela larga com `overflow-x:auto` no contêiner

## Rolagem rápida demais gera falso negativo

O `IntersectionObserver` **coalesce** callbacks quando o scroll acontece em passos muito rápidos. Um loop de 380px a cada 80ms fez um teste meu reportar que áreas e radar não animavam — quando na verdade animavam perfeitamente com rolagem real.

```python
# rápido demais: perde callbacks
for(let y=0;y<h;y+=380){scrollTo(0,y); await sleep(80)}
# certo: passo menor, pausa maior
for(let y=0;y<h;y+=300){scrollTo(0,y); await sleep(220)}
```

Se o teste acusar que algo não disparou, confirme com `scroll_into_view_if_needed` naquele elemento antes de sair "consertando" o que não está quebrado.

## Validar de verdade, não com estados forçados

O erro que me custou uma entrega: eu tirava screenshot depois de forçar as classes com `page.evaluate`, o que **contornava o JS quebrado** e escondia um erro de sintaxe. Além disso o listener de console era anexado depois do `goto`, então perdia o erro de parse.

O teste honesto tem quatro partes:

```python
pg = b.new_page(viewport={"width":390,"height":844})
errs = []
pg.on("console",   lambda m: errs.append(m.text) if m.type=="error" else None)
pg.on("pageerror", lambda e: errs.append("PAGEERROR: "+str(e)))   # ANTES do goto
pg.goto(url)
# rola a página inteira devagar para acionar os observers de verdade
pg.evaluate('''async()=>{const h=document.body.scrollHeight;
  for(let y=0;y<h;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,90))}}''')
# confirme que os estados foram acionados SOZINHOS
st = pg.evaluate('''()=>({barras:[...document.querySelectorAll('[data-w]')].filter(b=>b.style.width!=='').length,
                          spark:document.querySelectorAll('.spark.in').length})''')
```

E antes de tudo, valide a sintaxe fora do navegador:

```bash
# extraia cada <script> e rode
node --check trecho.js
```

Um `SyntaxError` derruba o bloco inteiro e nenhuma animação roda — mas a página continua *parecendo* certa numa captura estática.

### Falso positivo: carrossel horizontal

O diagnóstico ingênuo acusa todo filho de um carrossel `overflow-x:auto` como estouro, porque o retângulo deles passa dos 390px — mas eles são clipados pelo contêiner e não geram rolagem de página. Filtre quem tem ancestral com rolagem própria:

```js
const rolavel=e=>{for(let p=e.parentElement;p;p=p.parentElement){
  const o=getComputedStyle(p).overflowX;
  if(o==='auto'||o==='scroll'||o==='hidden'||o==='clip')return true} return false};
[...document.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().right>392&&!rolavel(e))
```

A verdade continua sendo `document.documentElement.scrollWidth === 390`. Se esse número está certo e o filtro acima devolve lista vazia, não há estouro.

```js
// diagnóstico rápido de overflow em 390px
[...document.querySelectorAll('*')].filter(e=>e.getBoundingClientRect().right>392)
  .map(e=>({cls:(e.className+'').slice(0,40),r:Math.round(e.getBoundingClientRect().right)}))
```
---

## As duas arquiteturas — e como escolher

Medi as duas referências e elas **não usam a mesma estratégia**:

| | `min-width` | `max-width` | Arquitetura |
|---|---|---|---|
| Evento (FLP) | **44 regras** | 12 | **mobile-first** |
| SaaS/IA | 5 regras | 12, concentradas em `760px` | camada defensiva |

**Mobile-first (FLP).** O estilo base **é** o mobile. Desktop é enriquecimento por `min-width`. Breakpoints medidos: `640 · 768 · 1024 · 1280 · 1536` — a escala do Tailwind, mais alguns sob medida (`801`, `1025`, `1565`).

**Camada defensiva (SaaS/IA).** O estilo base é o desktop, e um bloco `max-width:760px` conserta tudo de uma vez.

### Qual usar

**Página nova, escrita por você:** mobile-first. O layout mobile nasce certo em vez de ser consertado, e você não precisa da camada defensiva inteira.

**Página que já existe, feita em builder:** camada defensiva. É o único caminho aditivo — você não vai reescrever o CSS base de uma página do Elementor.

Isso reconcilia o que parecia contradição neste arquivo: a camada defensiva não é a forma certa de construir, é a forma certa de **consertar**. Ver a skill `melhoria-de-pagina`.

---

## `env(safe-area-inset-bottom)` — a barra fixa no iPhone

Achado que faltava e que quebra em aparelho real, não no emulador:

```css
/* o corpo abre espaço para a barra fixa E para a faixa do iPhone */
body:has([data-sticky-cta]){
  padding-bottom: calc(76px + env(safe-area-inset-bottom));
}
/* a própria barra respeita a faixa por dentro */
.barra-fixa{
  padding-bottom: calc(12px + env(safe-area-inset-bottom));
}
```

Sem isso, no iPhone com barra de gestos o botão fica **por baixo da faixa do sistema** — clicável na metade de cima e morto na de baixo. É o defeito que não aparece em nenhum teste de viewport, só no aparelho.

Exige `<meta name="viewport" content="... viewport-fit=cover">` para o `env()` retornar valor diferente de zero.

### A referência que erra isso

Comparando as duas no mesmo quesito:

| | `env(safe-area)` | viewport | CTA fixo no mobile |
|---|---|---|---|
| Evento (FLP) | **sim**, no corpo e na barra | com `viewport-fit` | protegido |
| SaaS/IA | **nenhuma ocorrência** | `width=device-width, initial-scale=1` | `bottom:14px` |

A segunda tem CTA flutuante em `bottom:14px` no mobile e **nenhum tratamento de safe-area**. Num iPhone com barra de gestos, esses 14px caem debaixo da faixa do sistema — o botão fica clicável só na parte de cima.

E como o `viewport` dela não tem `viewport-fit=cover`, mesmo que alguém adicionasse `env()` o valor voltaria zero.

**Não copie referência sem conferir este ponto.** Foram as mesmas duas páginas que me deram quase todo o sistema medido — e uma delas erra aqui.

### `:has()` para reservar o espaço

```css
body:has([data-sticky-cta]){ padding-bottom: … }
```

O corpo só ganha o respiro **se a barra existir na página**. Melhor que `body{padding-bottom:76px}` fixo, que deixa um vão morto quando não há barra. Um atributo no elemento e o `:has()` cuida do resto.
