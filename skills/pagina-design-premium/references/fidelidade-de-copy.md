# Fidelidade de copy

## A regra

> Quando o usuário fornece a copy, **100% do texto entregue vem dela**. A skill diagrama, não escreve.

O motivo é prático, não filosófico: texto inventado por IA numa página de cliente **não pode ser validado**. O cliente lê, não reconhece, e agora precisa auditar a página inteira procurando o que é dele e o que não é. Isso destrói a confiança na entrega e custa mais tempo do que teria custado escrever.

## O que conta como invenção

Inclusive quando parece inofensivo:

| Categoria | Exemplo do erro |
|---|---|
| **Seção nova** | criar um FAQ que não existia na copy |
| **Microcopy** | "Acesso imediato", "Garantia de 7 dias", "Vagas limitadas" — se não está na copy, não entra |
| **Conteúdo de mock** | inventar os passos de uma ficha, as métricas de um painel, as falas de um depoimento |
| **Rótulo de diagrama** | nomear as camadas de um esquema com termos que a copy não usou |
| **Depoimento** | qualquer um, sempre |
| **Número** | preço, prazo, quantidade, percentual |
| **Garantia** | a mais perigosa: promete algo que ninguém autorizou e vira problema jurídico |

## O que é permitido sem pedir

- **Cortar.** Se a headline tem 17 palavras e quebra em 5 linhas, encurtar é diagramação. Avise o que cortou.
- **Reordenar** dentro da estrutura que a copy já define.
- **Repetir** um CTA que já existe na copy, em outro ponto da página.
- **Traduzir**, quando a copy vem misturada de idioma — e avisar.
- **Rótulo estrutural** que não afirma nada: numeração de seção, "01 · ", eyebrow que repete uma palavra da própria copy.

## Mocks sem inventar conteúdo

O conflito real: `prova-visual.md` pede objeto visual, e objeto visual precisa de conteúdo.

Três saídas, nesta ordem de preferência:

1. **Construa o mock a partir de strings que já estão na copy.** Uma lista de seis itens da copy vira seis tiles, um cronograma da copy vira um diagrama. Zero texto novo.
2. **Mock com marcador de preenchimento.** Estrutura pronta, conteúdo em `{{ }}`, visualmente marcado como pendente:
   ```html
   <div class="stp"><span class="n">1</span><span class="fill">{{ PASSO 1 — preencher }}</span></div>
   ```
   ```css
   .fill{background:repeating-linear-gradient(45deg,var(--accent-soft),var(--accent-soft) 6px,transparent 6px,transparent 12px);
         color:var(--ink-3);border-radius:4px;padding:.1em .4em;font-style:italic}
   ```
   O cliente vê exatamente o que falta e onde.
3. **Pergunte.** Se o mock é central para a página, vale uma pergunta em vez de um chute.

## Blocos disponíveis sob pedido

Estes existem prontos em `blocos.md` e **não entram sozinhos**. Ofereça no fim da entrega, em uma linha:

`FAQ` · `garantia` · `depoimentos` · `stack de valor com preços` · `escassez / contador` · `comparativo com concorrentes` · `bônus` · `sobre o autor estendido`

Formato da oferta, no fim da resposta:

> A copy não trazia FAQ nem garantia. Os dois blocos estão prontos na skill — me manda o texto e eu encaixo, ou eu escrevo um rascunho pra você levar ao cliente, se preferir.

Deixa a decisão com quem responde pelo cliente.

## Relatório de fidelidade

Toda entrega termina com isto, curto:

```
CORTADO      headline reduzida de 17 para 9 palavras
TRADUZIDO    dobra 6 estava em PT, convertida para ES
PENDENTE     FAQ, garantia — não estavam na copy
PLACEHOLDER  ficha de protocolo (4 passos), fotos (2)
```

Sem isso, o cliente não sabe onde olhar.
