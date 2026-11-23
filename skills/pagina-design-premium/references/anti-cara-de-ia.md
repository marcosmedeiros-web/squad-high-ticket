# Anti "cara de IA"

Ler **antes** de gerar e **depois** de gerar.

## A calibração que importa

Design gerado por IA hoje se agrupa em três aparências. Elas são legítimas para alguns briefings, mas aparecem **independentemente do assunto** — por isso denunciam.

| # | Default | Como reconhecer |
|---|---|---|
| 1 | **Creme + serif + terracota** | fundo próximo de `#F4F1EA`, display serif de alto contraste, accent barro perto de `#D97757` |
| 2 | **Preto + neon** | fundo quase-preto com um único accent verde-ácido ou vermelhão |
| 3 | **Broadsheet** | filetes hairline, `border-radius:0`, colunas densas de jornal, tudo alinhado à esquerda |

Onde o briefing fixa a direção, siga o briefing — a palavra dele sempre ganha, inclusive quando ele pede um desses três. Onde o briefing deixa o eixo livre, **não gaste essa liberdade num default.**

Esta skill já entregou o default 1 e o default 3 achando que estava fazendo design bom. Não estava. Estava fazendo o que faria para qualquer briefing.

---

## Reprovação imediata

| # | Padrão | Por quê |
|---|---|---|
| 1 | **Gradiente entre dois matizes saturados** (roxo→azul, rosa→laranja) num botão ou título | Clichê de gerador. Gradiente de **uma** família tonal, desfocado, como brilho de fundo, é outra coisa e é legítimo |
| 2 | **Emoji como ícone** (🚀 ✅ 💡 🎯) | Nenhum estúdio entrega. Use SVG do sprite |
| 3 | **Ícones de bibliotecas diferentes** misturados | Um sprite só: mesma grade, mesmo traço, mesmas pontas |
| 4 | **Todas as seções com a mesma forma** | Grid de 3 cards repetido 6 vezes é o sinal mais visível |
| 5 | **Mesmo padding vertical em tudo** | Sem ritmo nada se destaca |
| 6 | **Números redondos inflados soltos** (10x, 500+, 99%) | Sem contexto é enfeite. Vira mock ou some |
| 7 | **Um peso tipográfico só** do h1 ao rodapé | Sem contraste a página achata |
| 8 | **Foto de banco genérica** (executivo apertando a mão, mulher rindo com salada) | Melhor placeholder marcado do que foto errada |
| 9 | **Página com 8 seções magras** | Página cara é densa |
| 10 | **Zero mock de prova** | Sem objeto visual a página é Word estilizado |
| 11 | **Nenhum elemento-assinatura** | Ver `linguagem-visual.md`. Página sem assinatura é intercambiável |
| 12 | **O mesmo sistema visual para todo nicho** | A direção de arte se deriva do público. Ver `direcao-de-arte.md` |

---

## O que NÃO está proibido

Esta seção existe porque a versão anterior desta skill proibiu coisas que as melhores páginas do mercado usam bem.

| Recurso | Quando é certo |
|---|---|
| **Sombra** | Para criar camada e sobreposição. Três níveis, usados com intenção — não uma sombra difusa em todo card |
| **`border-radius` grande** (14–20px em card, 100px em pill) | Registro acolhedor, produto, SaaS, público amplo. Radius 0–4px é **um** registro, não o certo |
| **Gradiente** | Wash tonal de fundo, brilho radial atrás de seção escura, foto sobre fundo colorido |
| **Centralizar** | Título e subtítulo de seção. O corpo de texto longo continua à esquerda |
| **Ícone colorido em card** | Se o conjunto tem pastéis derivados e o ícone usa o `-ink` do próprio pastel |
| **Cor viva e saturada** | O accent precisa aparecer. O que não pode é ele estar em tudo |
| **Animação** | Até 3 técnicas de scroll + 1 loop decorativo. Ver `movimento.md` |

---

## Sinais de acabamento

Seis ou mais destes = está de pé.

1. **Papel tingido alternando com branco puro**, seção a seção — não dois cinzas quase iguais
2. **Tinta com a temperatura do papel** — preto quente em papel quente, azulado em papel frio
3. **CTA numa cor que não é o accent**, e que não aparece em mais nada
4. **Profundidade por sobreposição** — algo saindo por cima de outra coisa
5. **Fotografia como âncora**, com cards flutuando sobre ela no desktop
6. **Marca-texto** em 2–4 trechos da página inteira
7. **Headline com uma parte no accent**, escolhida pelo conteúdo
8. **Mock dentro de moldura** — notebook, celular, bilhete, relatório
9. **Ritmo variado**: seção densa depois de seção arejada
10. **Uma seção escura** com brilho quente, não preto chapado
11. **Um elemento-assinatura** que vem do assunto
12. **Densidade real**: 12–18 seções, 7+ formas diferentes

---

## Regra da assimetria

A causa raiz de "cara de IA" é uniformidade. Antes de fechar, liste as seções e a forma de cada uma:

`grid-tiles` · `lista-densa` · `split-7-5` · `split-foto-sobreposta` · `tabela` · `mock-dispositivo` · `orbital` · `timeline` · `acordeao` · `faixa-escura` · `pilha-notificacao` · `full-bleed`

Duas seções consecutivas nunca compartilham a forma. Uma página de 14 seções usa 8+ formas.

## Regra da cor

O accent é **destaque**, não tema. Onde pode: botão secundário, palavra da headline, marca-texto, número-chave, borda do card em foco, brilho da seção escura.

Onde não pode: fundo de seção inteira, todos os títulos, todos os ícones, borda de todo card.

Se ele aparece em mais de 4 elementos por dobra, deixou de ser destaque.
