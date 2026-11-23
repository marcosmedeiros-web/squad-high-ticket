# Dispositivos visuais

Biblioteca dos objetos construídos das duas referências, com o CSS real extraído do navegador. Existe porque a skill vinha usando o vocabulário de **uma** página (a de evento) e ignorando a outra, que é a mais inventiva das duas.

Inventário medido na página de SaaS/IA: **46 contadores animados**, **22 barras de gráfico**, 16 chips pastel, 9 CTAs com brilho, 6 pílulas em órbita, 1 notebook completo, 1 toast deslizante. Densidade de dispositivo é o que ela tem e a de evento não.

**Regra: toda página gerada usa no mínimo 3 dispositivos desta lista, e pelo menos 1 vindo de cada família.**

---

## Família A — construídos (página de SaaS/IA)

### A1 · Notebook em perspectiva

O melhor objeto das duas páginas. Cinco camadas, e cada uma tem um motivo.

```css
.lap{position:relative;margin:0 auto;width:100%;max-width:600px;
  transform:perspective(2200px) rotateX(6deg);transform-origin:center 78%}
.lap-bezel{position:relative;padding:5px;border-radius:20px 20px 9px 9px;
  background:linear-gradient(158deg,#EEF0F4 0%,#C9CED7 52%,#AAB0BB 100%);
  box-shadow:0 46px 88px -34px rgba(20,10,60,.62),      /* sombra TINGIDA com a tinta da página */
             inset 0 1px 0 rgba(255,255,255,.8),        /* luz pegando a borda de cima */
             inset 0 0 0 1px rgba(120,126,140,.32)}
.lap-screen{position:relative;background:#0A0B12;border-radius:15px;padding:22px;overflow:hidden}
.lap-hinge{position:relative;width:103%;left:-1.5%;height:9px;margin-top:-3px;
  background:linear-gradient(180deg,#8A909C,#BEC3CC 55%,#A6ACB8);
  border-radius:0 0 4px 4px;box-shadow:inset 0 2px 3px rgba(0,0,0,.28)}
.lap-base{position:relative;width:117%;left:-8.5%;height:22px;
  background:linear-gradient(180deg,#E7EAEF,#B9BFC9);border-radius:0 0 10px 10px}
```

Os quatro detalhes que fazem funcionar e que ninguém adivinha:
1. `rotateX(6deg)` com `transform-origin:center 78%` — inclinação sutil, eixo abaixo do centro
2. `inset 0 1px 0 rgba(255,255,255,.8)` no bezel — a luz na aresta superior
3. base **117% de largura** contra tela de 100% → ilusão de trapézio sem 3D real
4. sombra tingida `rgba(20,10,60,…)` com a tinta da página, nunca preto neutro

### A2 · Órbita

Seis pílulas em volta de um centro, cada uma flutuando fora de fase.

```css
.orbita{position:relative;min-height:520px}
.orbit-pill{position:absolute;transform:translate(-50%,-50%);animation:flut 5.2s ease-in-out infinite}
@keyframes flut{0%,100%{translate:0 0}50%{translate:0 -9px}}
```
```html
<span class="orbit-pill" style="left:27%;top:19%;animation-delay:-0.4s">…</span>
<span class="orbit-pill" style="left:73%;top:17%;animation-delay:-1.6s">…</span>
<span class="orbit-pill" style="left:10%;top:49%;animation-delay:-2.8s">…</span>
<span class="orbit-pill" style="left:90%;top:49%;animation-delay:-0.9s">…</span>
<span class="orbit-pill" style="left:29%;top:82%;animation-delay:-3.5s">…</span>
<span class="orbit-pill" style="left:71%;top:82%;animation-delay:-2.1s">…</span>
```

As posições acima são as medidas, e valem copiar: formam uma elipse legível sem sobrepor o centro. O `animation-delay` **negativo e irregular** é o truque — inicia cada uma num ponto diferente do ciclo, então nada pulsa junto.

No mobile a órbita não responde. Escreva a versão em grid de 2 colunas e troque por media query.

### A3 · Chips pastel

```css
.chip{border-radius:18px;padding:.8rem .9rem;font-weight:600;font-size:.82rem;
  color:var(--ink)}     /* ← a TINTA DA PÁGINA, não um tom escuro do pastel */
```
Pastéis medidos: `#EEEBFC` lavanda · `#E6EEFC` azul · `#E4F6EC` verde · e variações amarelo e rosa no mesmo nível.

Correção ao que esta skill dizia antes: o texto do chip é o **ink global**, não um `-ink` derivado de cada pastel. Fica mais coeso e é menos trabalho.

### A4 · Contador animado

Usado 46 vezes na página medida. Ver `movimento.md §2`. O que a medição acrescenta: eles contam **quase todo número da página**, não só um ou dois. Se o número é prova, ele conta.

### A5 · Ponto pulsante

Status "ao vivo", "conta ativa", "operando". Custa 8 linhas.

```css
.pulse{position:relative;animation:pd 1.8s ease-in-out infinite}
.pulse::after{content:"";position:absolute;inset:0;border-radius:50%;background:inherit;
  animation:pr 1.8s ease-out infinite;pointer-events:none}
@keyframes pd{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
@keyframes pr{0%{transform:scale(1);opacity:.6}70%,100%{transform:scale(2.6);opacity:0}}
```

### A6 · Três pontos digitando

Para mock de conversa. Dá vida sem custo.

```css
.typing{display:inline-flex;align-items:center;gap:3px}
.typing i{width:5px;height:5px;border-radius:50%;background:currentColor;
  animation:tp 1.3s ease-in-out infinite}
.typing i:nth-child(2){animation-delay:.18s}
.typing i:nth-child(3){animation-delay:.36s}
@keyframes tp{0%,100%{opacity:.35;transform:translateY(0)}50%{opacity:1;transform:translateY(-3px)}}
```

### A7 · Card comparativo com selo pendurado

Dois cards lado a lado, cada um com um selo saindo pela borda de cima e **sombra na cor do estado**.

```css
.comp{position:relative}
.comp-badge{position:absolute;top:-15px;left:50%;transform:translateX(-50%);
  width:max-content;max-width:92%;border-radius:999px;padding:.4rem 1rem}
.comp.ruim .comp-badge{box-shadow:0 8px 20px rgba(168,14,24,.28)}
.comp.bom  .comp-badge{box-shadow:0 8px 20px rgba(17,122,59,.28)}
```

O `top:-15px` com `translateX(-50%)` é o que dá a sensação de etiqueta pendurada. A sombra colorida por estado é o detalhe caro.

### A8 · Barras de gráfico

22 na página medida. Ver `prova-visual.md §3`. Detalhe da medição: as barras usam `width` inline em `%` e altura fixa baixa, e a cor é **gradiente**, não sólida.

---

## Família B — tangíveis (página de evento)

### B1 · Bilhete com entalhe

O elemento-assinatura daquela página. CSS em `linguagem-visual.md`.

### B2 · Barra de progresso de lote no topo

Cabeçalho fixo com logo, progresso de venda e CTA. Só com escassez verificável.

### B3 · Cards flutuando sobre foto

Credencial saindo por cima do retrato no desktop, virando lista no mobile.

### B4 · Pilha de notificações

Três a quatro notificações empilhadas com opacidade decrescente e deslocamento em X.

### B5 · Marca-texto

`box-decoration-break:clone` obrigatório.

---

## Como escolher

| O argumento é | Dispositivos |
|---|---|
| "a ferramenta faz X" | A1 notebook + A6 digitando + A5 pulso |
| "são muitas peças servindo uma coisa" | A2 órbita + A3 chips |
| "o número prova" | A4 contador + A8 barras |
| "compare o antes com o depois" | A7 card com selo |
| "isto é um evento com data" | B1 bilhete + B2 progresso de lote |
| "esta pessoa é a autoridade" | B3 cards sobre foto |
| "outras pessoas já compraram" | B4 pilha de notificações |

Nunca use A2 e A7 na mesma página — as duas disputam o papel de composição central.

## O que a página de evento tem e a de SaaS não

Fotografia. Ela carrega 7 a 13 imagens por seção; a de SaaS quase nenhuma e compensa com densidade de dispositivo construído.

**Esse é o mix a perseguir:** a fotografia e a temperatura de uma, a densidade de objeto construído e a inventividade de composição da outra. Página que só tem foto fica bonita e vazia; página que só tem dispositivo fica fria.

---

## Elementos fixos: escolha, não default

Medido: **as duas páginas resolvem isto de formas opostas.** Não existe padrão único, e colocar cabeçalho fixo com logo + botão em tudo é vício, não decisão.

| Página | O que fica fixo |
|---|---|
| Evento (FLP) | **Cabeçalho fixo de 93px** com logo, barra de lote e CTA. Wrapper com `pointer-events:none`, botão com `pointer-events:auto`. Mais uma **coluna sticky** em `top:104px` no desktop |
| SaaS/IA | **Nenhum cabeçalho.** Só um CTA flutuante no rodapé e um toast |

Três opções, escolha uma e justifique:

**A · Cabeçalho fixo** — só quando há escassez verificável para exibir (lote, vagas, contagem). Sem número para mostrar, o cabeçalho vira barra vazia ocupando 90px.

```css
.top{position:fixed;inset-inline:0;top:0;z-index:50;pointer-events:none}
.top > *{pointer-events:auto}   /* deixa o clique passar fora dos filhos */
```

**B · CTA flutuante** — a solução da página de SaaS. Canto inferior direito no desktop, faixa centralizada no mobile.

```css
.cta-float{position:fixed;right:20px;bottom:18px;z-index:99999;max-width:calc(100% - 32px)}
@media(max-width:767px){
  .cta-float{left:0;right:0;bottom:14px;display:flex;justify-content:center;
             max-width:none;padding:0 12px;pointer-events:none}
  .cta-float__btn{pointer-events:auto;font-size:13px;letter-spacing:.03em;padding:14px 20px}
}
```

**C · Nada fixo** — página curta, uma dobra de decisão. Legítimo.

**D · As duas ao mesmo tempo, com papéis separados.** Medido numa terceira referência (Framer, nicho B2B):

| | Altura | Fundo | z-index | Conteúdo |
|---|---|---|---|---|
| Topo | 43px | `rgba(0,0,0,.8)` + `backdrop-filter:blur(10px)` | 9 | escassez: `67% DAS VAGAS PREENCHIDAS · LOTE 50% OFF POR R$49` |
| Rodapé | 91px | transparente | 5 | ação: `GARANTIR VAGA` + repetição da escassez |

Funciona porque **os papéis não competem**: a de cima informa o estado, a de baixo pede a ação. A de cima é fina e escura para não roubar a dobra; a de baixo é transparente e o botão flutua sobre o conteúdo.

Isso corrige a regra anterior. A ou B eram apresentadas como excludentes — não são, desde que uma **informe** e a outra **peça**. Duas barras pedindo a mesma coisa é que é spam.


Regra: se a página anterior desta conversa usou A, a próxima não usa A por inércia. Decida pelo conteúdo.

---

## B1 · Bilhete com entalhe — implementação real

A minha versão anterior pendurava os entalhes no próprio cartão e exigia calibrar um `--notch` na mão. A implementação medida é melhor: um elemento de **altura zero** que você solta onde a linha de corte deve passar, e ele se posiciona sozinho.

```css
.ticket-rip{position:relative;height:0;border-top:2px dashed var(--line)}
.ticket-rip::before,.ticket-rip::after{content:"";position:absolute;top:-15px;
  width:28px;height:28px;border-radius:50%;background:var(--rip-color,var(--paper))}
.ticket-rip::before{left:-20px}
.ticket-rip::after{right:-20px}
```

```html
<div class="ticket">
  <div class="head">…</div>
  <div class="ticket-rip"></div>   <!-- solta aqui, acabou -->
  <div class="body">…</div>
</div>
```

O `--rip-color` resolve o caso da seção escura: basta `style="--rip-color:var(--ink)"` no bilhete. Sem seletor `.dark .ticket::before`.

---

## Canal RGB para alfa

As duas páginas guardam o accent também em **canais separados**, o que permite opacidade sem `color-mix`:

```css
:root{--accent:#FF754F; --accent-rgb:255 117 79}
/* uso */ box-shadow:0 0 0 7px rgb(var(--accent-rgb)/0);
```

Adote nos tokens. É o que torna o `pulse-live` abaixo possível sem hardcode.

---

## Detalhe de acabamento: a barra de rolagem

Custa 4 regras e quase ninguém faz.

```css
::-webkit-scrollbar{width:11px}
::-webkit-scrollbar-track{background:var(--paper)}
::-webkit-scrollbar-thumb{background:#DDD3C8;border-radius:99px;border:3px solid var(--paper)}
::-webkit-scrollbar-thumb:hover{background:#8C8279}
```

---

## Os cinco últimos (medidos e construídos)

Todos renderizados em `assets/catalogo-dispositivos.html`. Abra o catálogo antes de escolher.

### A9 · Funil de conversão
Largura proporcional ao volume, piso de 18% para o último continuar legível, e **um item em âmbar marcando onde vaza**. Funil todo verde não ensina nada.

### A10 · Tabela de gerenciador
Grid `210px 1fr 52px` que no mobile vira `84px 1fr 38px` — re-proporcionado, nunca empilhado (ver `mobile.md`). Cada linha: nome, barra com custo e retorno, bolinha de status. Sempre inclua **uma linha ruim**.

### A11 · Medidor
Arco semicircular com `stroke-dasharray`. Meça o caminho no JS em vez de chutar:
```js
gauge.style.setProperty('--len', Math.ceil(path.getTotalLength()));
```
```css
.arc-fg{stroke-dasharray:var(--len);stroke-dashoffset:var(--len);transition:stroke-dashoffset 1.2s cubic-bezier(.22,.61,.36,1)}
.gauge.on .arc-fg{stroke-dashoffset:calc(var(--len) - var(--len) * var(--pct))}
```

### A12 · Sparkline — a técnica medida
As referências **não usam `stroke-dasharray`** para revelar linha. Usam `clip-path`, que funciona para qualquer conteúdo SVG:
```css
.spark{clip-path:inset(0 100% 0 0);transition:clip-path 1.15s cubic-bezier(.22,.61,.36,1);will-change:clip-path}
.spark.in{clip-path:inset(0)}
.spark--up{clip-path:inset(100% 0 0)}   /* revela de baixo pra cima */
```
Cores por significado, medidas: azul `#2626D9` neutro · violeta `#4318E0` positivo · vermelho `#E02B2B` em queda · âmbar `#E8960C` atenção.

### A13 · Toast deslizante
**Só desktop** nas referências (`min-width:1024px`), fixo no canto inferior esquerdo, deslizando de `translateX(-32px)`.
```css
.toast{display:none}
@media(min-width:1024px){.toast{display:block;position:fixed;left:16px;bottom:16px;z-index:99998;
  max-width:calc(100vw - 32px);pointer-events:none}}
.toast__slide{transform:translateX(-32px);opacity:0;transition:transform .5s ease-out,opacity .5s ease-out}
.toast__slide.is-shown{transform:none;opacity:1}
.toast__card{pointer-events:auto}
```
Aparece após ~2s, some sozinho, e tem botão de fechar. Use no máximo um por página — dois viram spam.

### Correção no entalhe do bilhete
`--rip-color` é a cor **do que está atrás** do bilhete, não a do cartão. Em seção escura: `--rip-color:var(--ink)`. Se ficar invisível, é porque foi igualada à cor do próprio cartão.

---

## Fundamento cognitivo dos dispositivos

Quatro leis que **explicam por que** dispositivos que já usamos funcionam, e que dão o critério de quando parar. Fonte: Laws of UX.

### Efeito Goal-Gradient → a barra de progresso do lote

> Quanto mais perto do fim, mais rápido a pessoa trabalha para chegar lá. Indicar progresso motiva a conclusão.

É por isso que `67% dos ingressos vendidos` funciona melhor que `restam 33 vagas`: a barra mostra o **avanço**, não o que falta.

**O limite ético.** A mesma fonte diz que progresso artificial em direção à meta também motiva. Aí está a fronteira: barra que reflete venda real é persuasão; barra inventada é engano. Percentual sempre vem de número verificável — a mesma regra da §16 de `diagramacao.md`.

### Efeito Von Restorff → o CTA em cor única

> Torne informação importante ou ação-chave visualmente distinta. **Use contenção**, para que os destaques não compitam entre si e não sejam confundidos com anúncio.

O verde do CTA é o único verde da página. Se tudo se destaca, nada se destaca — e pior: elemento muito destacado vira cego de banner.

O aviso completa: **não dependa só de cor**. Por isso o botão tem também tamanho, peso e posição, não apenas matiz.

### Efeito de Posição Serial → a ordem das listas

> Itens no meio da lista são lembrados com menos frequência. Ações-chave nas pontas aumentam a memorização.

Aplicação direta em lista de entregáveis e de bônus: **o item mais forte primeiro, o segundo mais forte por último, os medianos no meio.** Nunca despeje na ordem em que o cliente mandou.

### Regra do Pico e Fim → onde investir o acabamento

> As pessoas julgam pela intensidade máxima e pelo momento final. E lembram do negativo com mais vivacidade que do positivo.

Traduzido para a página: o **hero** (pico) e o **último bloco antes do rodapé** (fim) definem a impressão inteira. É onde o acabamento rende mais.

E a parte incômoda: um defeito no fim pesa mais que três acertos no meio. Botão quebrado no CTA final estraga a página toda.

---

## O aviso que vale para o nosso próprio trabalho

### Efeito Estético-Usabilidade

> Design bonito faz as pessoas acreditarem que funciona melhor, e as torna mais tolerantes a falhas de usabilidade. **Design agradável pode mascarar problemas e impedir que sejam descobertos.**

Isto é um alerta contra a `pagina-design-premium` inteira. Acabamento de estúdio **esconde** defeito: a página fica bonita, o cliente aprova, e o botão continua morto sob a faixa do iPhone.

**Por isso o Passo 7 mede em vez de olhar.** `scrollWidth`, `node --check`, contraste — números não se deixam seduzir pelo acabamento. É a razão de a `melhoria-de-pagina` existir como skill separada e medir tudo.
