# Composição

Medido do CSS computado das duas referências. Existe porque a skill caiu no vício de usar **uma** composição (hero split 7/5 com foto à direita) para tudo, o que é o mesmo defeito que ela tenta evitar.

## O que foi medido derrubou três regras que eu pregava

| Regra que eu pregava | O que as páginas fazem |
|---|---|
| "Alterne seção densa com seção arejada" | Padding vertical **uniforme**: `112px/112px` em quase todas as seções. O ritmo vem do **conteúdo e da troca de fundo**, não do padding |
| "Grid de 2 colunas sempre assimétrico, 7/5" | `576/576` e `636/636` — **simétrico**. A assimetria aparece no hero (`669/582`) e em grids de 5, não no padrão |
| "Alinhe tudo à esquerda" | Títulos de seção **centralizados** em quase todas. Alinhamento à esquerda só no hero e em uma seção editorial |

Correção: **a variedade não vem de quebrar simetria. Vem de trocar a contagem de colunas.**

---

## A grade

Referência A roda sobre **12 colunas de 52px**. Referência B usa larguras derivadas da mesma ideia.

```css
.wrap{max-width:1176px;margin-inline:auto;padding-inline:clamp(1.15rem,5vw,2rem)}
.grid12{display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(1rem,2vw,1.5rem)}
```

Composições que aparecem, medidas:

| Colunas | Onde é usada |
|---|---|
| `1fr 1fr` simétrico | argumento com mock ao lado, comparativo, antes/depois |
| `repeat(3,1fr)` | aulas, dias, pilares, módulos — a mais frequente |
| `repeat(4,1fr)` | métricas, logos, entregáveis curtos |
| `141/100/100/80/80` (5 col decrescente) | listas de peças com hierarquia de importância |
| `repeat(12,1fr)` com filhos de 1–3 col | grade fina para a seção-assinatura |
| `669/582` (leve assimetria) | **só o hero** |

Regra prática: dentro de uma página, use **pelo menos quatro** contagens diferentes. Repetir `repeat(3,1fr)` em seis seções é o que dá cara de template — não a simetria.

---

## Ritmo vertical

```css
section{padding-block:clamp(4rem,8vw,7rem)}   /* uniforme */
section.hero{padding-block:clamp(5rem,9vw,8rem) clamp(3.5rem,6vw,6rem)}
```

O ritmo vem de três coisas, nesta ordem:

1. **Troca de fundo** — branco puro ↔ papel tingido, seção a seção
2. **Densidade de conteúdo** — uma seção com 9 itens ao lado de uma com um parágrafo
3. **Uma seção escura**, uma só, perto do fecho

Não de mexer no padding.

---

## Biblioteca de heróis

O hero é onde a skill mais precisa parar de repetir. Escolha pelo **assunto**, não por costume, e justifique a escolha em uma linha antes de gerar.

| Hero | Composição | Quando |
|---|---|---|
| **Retrato lateral** | texto 57% / foto recortada 43%, cards de credencial sobrepostos | pessoa é a autoridade e existe foto boa |
| **Objeto central** | texto centralizado, o artefato do produto grande e centralizado abaixo | o produto tem forma própria (bilhete, ficha, dispositivo, peça) |
| **Demonstração** | texto à esquerda, mock funcional/animado à direita ocupando mais espaço que o texto | ferramenta, software, painel |
| **Declaração** | headline enorme centralizada, sem imagem, prova em faixa logo abaixo | promessa forte e nenhum ativo visual bom |
| **Antes/depois** | duas colunas simétricas com o contraste já na primeira dobra | o produto resolve um estado ruim visível |
| **Diagrama** | headline curta em cima, esquema do método ocupando a dobra inteira | o método é visualmente explicável |
| **Faixa de dados** | headline + tira horizontal de números reais em mono | prova numérica é o argumento mais forte |

Se o hero anterior que você gerou nesta conversa foi *retrato lateral*, o próximo não pode ser. Anote qual usou.

---

## Densidade de imagem

O número que mais separa as referências de uma página gerada: **7 a 13 imagens por seção** nas seções fortes da referência A.

Quando não há foto, isso precisa ser compensado com objeto visual construído em HTML/CSS — mock, diagrama, esquema, ficha. Uma seção com só texto e cards de borda é uma seção fraca, e três delas seguidas afundam a página.

Contagem mínima por página: **3 objetos visuais construídos** + a lista de fotos pendentes entregue ao usuário com proporção e uso.

---

## Antes de gerar, preencha

```
GRADE          12 col · container 1176
HERO           [qual dos 7] — porque ______
CONTAGENS      2 · 3 · 4 · 12   (mínimo 4 diferentes)
FUNDOS         branco ↔ tingido, escura na seção __
CENTRALIZADO   títulos de seção sim / não
OBJETOS        [3+ mocks construídos]
FOTOS          [lista com proporção e uso]
```
