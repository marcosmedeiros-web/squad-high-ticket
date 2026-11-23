# Leitura de referência visual

Quando a entrada é imagem (JPG/PNG), PDF ou print de Figma. O objetivo **não** é copiar a página: é extrair o **sistema** e aplicá-lo ao conteúdo do cliente.

## Limite ético e prático

Extraia: paleta, escala tipográfica, densidade, ritmo, tipos de bloco, tratamento de borda, radius, conceito visual.

Não extraia: texto/copy, fotos, logo, ilustrações, ícones proprietários, nomes de marca. Se o usuário pedir cópia literal de uma página de terceiro, diga que dá pra reconstruir o sistema visual mas não o conteúdo — e que copiar copy alheia é risco de tomar takedown e de anunciar algo que não é dele.

## Fase 1 — Extração

Olhe a referência e escreva um **relatório de tokens** antes de gerar qualquer HTML. Preencha isto:

```
PALETA
  fundo principal:       #______  (é branco puro, off-white quente, off-white frio, ou escuro?)
  fundo secundário:      #______
  texto principal:       #______  (preto puro raramente; costuma ser #14–#24)
  texto secundário:      #______
  linha/borda:           #______
  destaque:              #______  (quantos elementos usam? se >4 por dobra, não é destaque)
  destaque secundário:   #______ ou ausente

TIPOGRAFIA
  display:    serif / grotesk / geométrica / condensada — peso ____
  corpo:      ____ — peso ____
  mono:       presente? onde (labels, números, ambos)?
  contraste:  tamanho do h2 ÷ tamanho do corpo = ____×   (< 2,2 achata)
  tracking:   display tem letter-spacing negativo? labels têm positivo?

ESTRUTURA
  radius:            ____px   (0–8 = técnico · 10–14 = caloroso · 16+ = template)
  separação:         borda hairline / sombra / só espaço
  alinhamento:       esquerda predominante? centralizado?
  grid:              simétrico ou assimétrico? qual proporção (7/5, 8/4, 6/6)?
  ritmo vertical:    todas as seções iguais, ou alterna denso/arejado?
  seções escuras:    quantas? onde?

CONCEITO
  qual é a metáfora?  ____________________
  onde ela aparece?   (numeração, códigos, molduras, separadores, nomenclatura)

BLOCOS IDENTIFICADOS
  1. ____  2. ____  3. ____  ...
```

Para cor: se não conseguir precisar o hex de olho, aproxime e **diga que aproximou**. Se o usuário puder passar o hex exato, peça — vale mais que qualquer chute.

## Fase 2 — Mapeamento para o sistema

Compare o relatório com `temas.md`. Um dos quatro temas costuma ficar a menos de 15% de distância da referência. Escolha o mais próximo e ajuste só os tokens divergentes, em vez de inventar um tema do zero — o tema já tem as relações internas resolvidas (contraste, hierarquia, escala), e mexer nelas por conta quebra o acabamento.

Se a referência não se aproximar de nenhum, derive um `:root` novo seguindo exatamente a mesma estrutura de tokens.

## Fase 3 — Confirmação antes de gerar

Mostre ao usuário, em uma mensagem:

1. O relatório de tokens preenchido
2. Qual tema você vai usar como base e o que vai ajustar
3. O mapa de blocos: seção da referência → bloco da biblioteca → conteúdo dele que entra ali

Ele aprova ou corrige. Só depois gere. Isso evita gerar uma página inteira em cima de uma leitura de cor errada.

## Fase 4 — Loop de aproximação

Fidelidade realista no primeiro passe: 85–90%. O gap se fecha comparando renderizações lado a lado, não relendo a referência.

```bash
npx playwright screenshot --viewport-size=390,844 --full-page saida.html mobile.png
npx playwright screenshot --viewport-size=1440,900 --full-page saida.html desktop.png
```

Abra o screenshot e compare com a referência. Procure nesta ordem — os erros mais visíveis primeiro:

1. **Escala do h1** — quase sempre o primeiro erro. Se parece pequeno, é pequeno.
2. **Densidade vertical** — padding de seção muito frouxo ou muito apertado é o que mais entrega diferença
3. **Peso da cor de destaque** — usei mais do que a referência usa?
4. **Largura de linha do corpo** — mais de 75 caracteres parece amador
5. **Alinhamento** — centralizei coisa que a referência alinha à esquerda?

Ajuste um item por rodada. Mudar cinco coisas de uma vez torna impossível saber o que melhorou.

## PDF e Figma

**PDF:** se for vetorial, `pdftotext -layout` dá a hierarquia de texto e a ordem dos blocos; a renderização da página dá o visual. Use os dois.

**Figma:** o caminho confiável hoje é o usuário exportar os frames em PNG (2x) e mandar como imagem — trate igual a JPG. Se ele mandar link de Figma, peça o export: link exige autenticação e a leitura via MCP é irregular.

**Vários frames:** peça na ordem de scroll e trate cada frame como uma seção. Não tente inferir a ordem por conta.
