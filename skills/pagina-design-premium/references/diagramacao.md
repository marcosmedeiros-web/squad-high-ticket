# Diagramação

Vocabulário de **posicionamento**. `dispositivos.md` diz *o que* construir; este arquivo diz *onde* e *como* encaixar. Todos renderizados em `assets/catalogo-composicoes.html` — abra antes de escolher.

A observação que gerou este arquivo: as referências quase nunca colocam dois blocos lado a lado sem relação. Eles **se tocam, se sobrepõem, se conectam ou se emolduram**. É isso que faz a página parecer composta em vez de empilhada.

---

## 1 · Balão com cauda

A cauda é um quadrado de 20px rotacionado 45° herdando `background:inherit` — não um triângulo em `border`.

```css
.balao{position:relative;border-radius:18px;background:var(--paper-2);padding:.95rem 1.1rem;
  box-shadow:rgba(40,20,90,.18) 0 18px 42px -16px}
.balao::after{content:"";position:absolute;width:20px;height:20px;background:inherit;
  bottom:-8px;left:26px;transform:rotate(45deg);border-radius:0 0 5px 0}
.balao.up::after{bottom:auto;top:-8px;border-radius:5px 0 0 0}
.balao.dir::after{bottom:24px;left:auto;right:-8px;border-radius:0 5px 0 0}
```

**Durações e atrasos irregulares, medidos das referências:** `4.4s` · `5.6s +0.3` · `5s +0.6` · `5.8s +1.1`. Se você repetir a mesma duração, tudo pulsa junto e o efeito morre.

Use a cauda apontando para a pessoa ou o objeto que o balão credencia. Sem cauda, é card flutuante e perde a relação.

---

## 2 · Glow do botão

Medido, e diferente do que eu fazia. Não é `box-shadow` colorido: é um **duplicado desfocado do próprio botão** atrás dele.

```css
.btn{position:relative;z-index:0;transition:transform .25s}
.btn::after{content:"";position:absolute;inset:0;border-radius:inherit;
  background:rgb(var(--ok-rgb));z-index:-1;filter:blur(18px);opacity:.4;
  transition:opacity .25s;pointer-events:none}
.btn:hover{transform:scale(1.045)}
.btn:hover::after{opacity:.62}
```

`border-radius:inherit` é a peça-chave — o halo acompanha qualquer curvatura. Um `box-shadow` grande fica duro e não segue o contorno do mesmo jeito.

**Par primário + fantasma:** ao lado do botão com glow, um segundo botão de fundo claro sem halo. Uma ação principal e uma de menor compromisso ("ver como funciona") — as duas referências usam.

---

## 3 · Número marca-d'água

```css
.wm{position:relative;isolation:isolate}
.wm .n{position:absolute;right:4px;top:-18px;z-index:-1;
  font-size:5.4rem;font-weight:800;letter-spacing:-.04em;line-height:1;
  color:transparent;-webkit-text-stroke:1.6px var(--line-2);user-select:none}
.wm.on .n{-webkit-text-stroke-color:#F2C9C0}   /* item ativo */
```

`isolation:isolate` é obrigatório: sem ele o `z-index:-1` escapa e o número vai parar atrás do fundo da seção.

Numera sem ocupar espaço de leitura. O item ativo troca a cor do contorno — o olho encontra sozinho qual dos três importa.

---

## 4 · Trilha curva com nós

Substitui a timeline reta. Uma curva SVG sobe da esquerda para a direita, nós em posições percentuais com **alturas diferentes**, e linhas tracejadas descendo de cada nó até o card correspondente.

```html
<svg viewBox="0 0 900 120" preserveAspectRatio="none" style="height:120px;overflow:visible">
  <path d="M0,84 C170,84 200,52 330,52 C470,52 500,26 690,26 C800,26 850,20 900,18"
        fill="none" stroke="var(--line-2)" stroke-width="1.6"/>
  <!-- segundo path, só o trecho final, na cor de destaque -->
</svg>
<span class="no" style="left:18%">…</span>
<span class="queda" style="left:18%"></span>
```

A curva **subir** carrega significado: o terceiro item é o ponto de chegada. Um segundo `path` cobrindo só o trecho final, no accent, reforça isso sem texto.

---

## 5 · Painel sobreposto

O jeito mais econômico de dizer "este importa mais", sem seta e sem legenda.

```css
@media(min-width:860px){
  .sobre{display:grid;grid-template-columns:1fr 1fr}
  .sobre > :last-child{margin-left:-42px;margin-top:26px;z-index:2}
}
```

O painel da direita invade o da esquerda, desce um pouco e sobe no `z-index`. Complementos que valem: três pontinhos de janela no cabeçalho (situam que é uma tela), contador no canto direito, e um **selo pendurado** em `top:-13px`.

**Armadilha:** selo pendurado exige `overflow:visible` no painel. Se o card tiver `overflow:hidden` para arredondar cantos, o selo some — mova o `border-radius` para o cabeçalho e o último item.

---

## 6 · Nota com fita sobre malha

Para "o que você leva pra casa", entregáveis, peças de um método.

```css
.malha{background:
  linear-gradient(rgba(21,22,26,.045) 1px,transparent 1px) 0 0/26px 26px,
  linear-gradient(90deg,rgba(21,22,26,.045) 1px,transparent 1px) 0 0/26px 26px,
  var(--paper-2)}
.nota{transform:rotate(var(--r,-1.2deg));box-shadow:var(--sh2)}
.nota::before{content:"";position:absolute;top:-11px;left:50%;
  transform:translateX(-50%) rotate(var(--tr,-2deg));
  width:74px;height:22px;background:rgb(246 243 236/.92);border-radius:2px}
.canto{position:absolute;width:20px;height:20px;border:2px solid var(--accent)}
.canto.tl{top:12px;left:12px;border-right:0;border-bottom:0}   /* + tr/bl/br */
```

**Rotações diferentes por nota** (−1,4° · +1,1° · −0,6°) e a fita com rotação própria. Se todas girarem igual vira padrão e perde a naturalidade. Cantos em L emolduram a área e reforçam a leitura de "planta".

Complementos: carimbo rotacionado `-11deg` com borda vermelha, e cabeçalho com `3 peças · rev. 01 · folha 1/1`.

---

## 7 · Anéis concêntricos

```css
.anel{position:absolute;border-radius:50%;border:1px dashed var(--line-2);animation:gira 34s linear infinite}
.anel.b{animation-direction:reverse;animation-duration:26s}
.anel i{position:absolute;width:8px;height:8px;border-radius:50%;background:var(--accent);
  box-shadow:0 0 0 4px rgb(var(--accent-rgb)/.14)}
.halo{position:absolute;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,rgba(124,58,237,.2) 0%,rgba(99,45,220,.1) 34%,rgba(124,58,237,0) 66%)}
```

Dois anéis em **direções opostas** e velocidades diferentes. O halo em três paradas (0 / 34% / 66%) é medido — duas paradas dá um círculo duro, quatro fica sujo.

---

## 8 · Área com gradiente

A linha do sparkline com um `path` fechado atrás, preenchido por gradiente vertical que morre em `opacity:0`. Revela pelo mesmo `clip-path` da §A12.

---

## 9 · Selo numerado sobre divisor

Junta o corte de bilhete com a numeração de etapa. Círculo em `top:-17px` à direita do divisor tracejado. Card de dia de evento: foto em cima, data, corte com selo, conteúdo embaixo.

---

## 10 · Pilha de avatares

```css
.pilha i{width:34px;height:34px;border-radius:50%;margin-left:-11px;
  box-shadow:0 0 0 2.5px var(--paper)}
.pilha i:first-child{margin-left:0}
```

O anel na cor do papel é o que separa os círculos. Último círculo carrega o total (`+2K`). Ao lado, nota e frase curta. Prova social barata e que não quebra em nenhuma largura.

---

## 11 · Card com borda lateral

Filete de 3px à esquerda trocando de cor por estado. Mais discreto que borda inteira colorida, mais legível que só o ícone. Bom para "é pra você / não é pra você" quando você não quer usar claro-contra-escuro.

---

## 12 · Colagem de fotos

Três fotos sobrepostas com rotações pequenas e **diferentes** (−3° · +2,4° · −1,4°), mais uma malha pontilhada preenchendo o canto vazio:

```css
.malhapt{background-image:radial-gradient(var(--line-2) 1.4px,transparent 1.4px);background-size:13px 13px}
```

Para bloco de história e bastidores, onde uma foto só ficaria pobre e um grid de três ficaria burocrático.

---

## Regra que atravessa tudo

Antes de fechar a página, olhe as seções e pergunte: **quantas delas têm algum elemento que atravessa a borda de outro?** Selo pendurado, painel sobreposto, cauda de balão apontando, número vazando, foto rotacionada, nó ligado por linha.

Se a resposta for zero, a página está empilhada, não composta. Duas ou três já mudam a leitura inteira.
---

## 13 · Agenda em linha do tempo lateral

Vista numa terceira referência. Resolve "o que acontece no dia do evento" sem virar lista burocrática.

```
        ● Manhã            ┃ DIAGNÓSTICO
        ⏱ 9h às 12h        ┃ texto do bloco
                           ┃
                           ┃ PROSPECÇÃO
                           ┃ texto do bloco

        ● Tarde            ┃ RETENÇÃO
        ⏱ 13h30 às 17h30   ┃ texto do bloco
```

Coluna esquerda estreita com **turno + horário**; coluna direita com os cards. Cada card tem **filete vertical de 3px na cor de destaque** à esquerda, e o ponto do turno se alinha ao primeiro card do grupo.

O que faz funcionar: o horário aparece **uma vez por turno**, não por item. Repetir "9h às 12h" em cada card transformaria informação em ruído.

Fundo com **malha quadriculada sutil** por trás de tudo — mesma técnica da §6, mas em escuro: `rgba(255,255,255,.03)` em vez de `rgba(0,0,0,.045)`.

---

## 14 · Par de cards com peso invertido

Para "é / não é para você", com uma diferença em relação ao filete lateral da §11:

| | Fundo | Efeito |
|---|---|---|
| Não é para você | escuro, igual ao papel da seção | **recua** |
| É para você | **azul chapado**, cor de marca | **avança** |

O card que interessa recebe cor sólida; o outro se dissolve no fundo. Mais forte que dois cards iguais com ícones diferentes — o olho encontra o lado certo antes de ler.

Ícones de estado seguem: vermelho de "proibido" contra verde de "check", ambos em círculo cheio.

---

## 15 · Comparação de lotes lado a lado

Dois cards de preço, e o inativo é o argumento:

```
┃ LOTE 50% OFF          │  LOTE SEM DESCONTO
┃ R$49                  │  R̶$̶9̶7̶
┃ Oferta por tempo…     │  Em breve
```

O ativo tem filete de destaque à esquerda e preço em cor viva. O inativo fica **cinza e translúcido**, com "Em breve" — não riscado, porque não é preço antigo: é o preço que vem. Isso ancora sem mentir sobre o histórico.

Abaixo dos dois, uma linha em mono: `PREÇO EXCLUSIVO ENQUANTO DURAR O LOTE`.

---

## 16 · A barra de progresso repetida em três lugares

Na mesma página, `67% dos ingressos vendidos por R$49` aparece no hero, na barra fixa inferior e no card de preço — sempre com a **mesma barra e o mesmo número**.

A repetição funciona porque o número é **um só e verificável**. Três barras com percentuais diferentes destruiriam a credibilidade das três.

Regra: escassez numérica se repete à vontade, desde que venha da mesma fonte. Nunca invente uma variação por seção.
