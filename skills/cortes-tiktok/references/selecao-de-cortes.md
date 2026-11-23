# Escolher o trecho e montar o gancho

A edição não salva um corte mal escolhido. Esta é a etapa que decide.

## O gancho tem que ser o segundo zero

O erro que mais custa: identificar a frase forte, escolher a janela em volta dela,
e a frase acabar aos 14 segundos porque o contexto veio antes. Numa leva de 18
cortes, **11 abriram assim** — e eu só descobri assistindo, depois de já ter
chamado um deles de "o mais forte de todos".

Por isso o produtor aceita **trechos fora de ordem**:

```
"08:11-08:16,07:56-08:11,08:16-08:24"
```

O primeiro trecho é a frase de impacto. O segundo é o contexto que a explica. O
terceiro é o desfecho. O espectador ouve o número duro antes de saber de onde ele
veio, e fica para descobrir.

Clipper automático corta linear. Esta é a diferença que justifica fazer à mão.

## Buscar na transcrição de palavra, nunca na compactada

A transcrição compactada agrupa a fala em blocos de 20s. Toda janela tirada dela
começa no meio de uma frase. Use o `.json` com timestamp por palavra e escolha o
tempo exato da primeira palavra da frase.

Depois de montar, **leia os 7 primeiros segundos de cada `.txt`**. Se abrir com
"a ter 17 negócios", "individual." ou "pelo celular." está errado. Um corte abriu
com "quebrou aqui" — era a cadeira quebrando.

## O que faz um gancho valer

Em ordem de força, pelo que retém:

1. **Número concreto contra expectativa.** "Faturei 48 milhões e minha vida virou
   um inferno." O número dá credibilidade, a virada dá motivo pra ficar.
2. **Pergunta que o espectador já se fez.** "Por que a maioria dos meus mentorados
   tem resultado?"
3. **Contradição com o senso comum do nicho.** "Eu não faço pitch."
4. **Antes e depois com número nos dois lados.** "Vendia a 5 mil, hoje vende o
   mesmo produto a 23 mil."

Fraco: começar por definição, por contexto, ou por "então", "aí", "e".

## Fechar em frase inteira

Corte que termina em vírgula soa quebrado. Ache a fronteira de frase antes do
limite que você queria e corte ali, mesmo perdendo alguns segundos.

Exceção proposital: num corte remontado, terminar no contexto cria um loop — o
final emenda com o começo quando o app repete. Aí a vírgula funciona.

## Fundir dois trechos distantes

Quando a mesma ideia aparece em dois momentos separados da gravação, junte. Duas
metades fracas viram um corte forte:

- Uma parte cita "minha margem era desse tamanho" sem o número que veio um minuto
  antes. Sozinha, não fecha.
- A outra tem o número mas não tem a conclusão.

Juntas: 17 negócios → burnout → reduzi → hoje tenho margem e paz.

Isso vale inclusive **entre arquivos-fonte diferentes**, com o prefixo `FONTE@` no
trecho. Se o enquadramento for o mesmo, a emenda não aparece.

## Duração

Alvo 30s a 360s. Mas **não estique com material fraco para bater o mínimo**. Um
corte de 24s que fecha o raciocínio vale mais que um de 32s com dez segundos de
enrolação no fim. Quando um tema não tem 30s de material bom, ou você funde com
outro do mesmo assunto, ou entrega curto e avisa.

## Material sensível

Gravação de call de consultoria tem nome de cliente, número de faturamento de
terceiro, crítica a concorrente e palavrão. Antes de escolher a janela, decida a
regra com o expert.

A regra que funciona melhor na prática: **prefira a janela sem nome nenhum a
bipar**. Bipe é ruído. De 16 cortes de um material cheio de nomes, 12 saíram sem
nenhum bipe só pela escolha da janela.
