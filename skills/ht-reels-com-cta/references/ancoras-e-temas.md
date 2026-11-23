# Âncoras e temas de Reels

A base do método vem marcada como padrão; o que é proposta da skill deve ser testado em campo. Nenhum prompt aqui é "o GPT do método": são modelos próprios.

## 1. As 4 âncoras

Âncoras são os quatro pilares que direcionam o conteúdo para atrair o avatar certo, gerar conexão e conduzir ao HT.
Regra de ouro: todo Reels puxa pelo menos uma; pode puxar mais de uma; o banco deve cobrir as quatro.

| Âncora | O que é | Por que funciona | Teste rápido |
|---|---|---|---|
| Dor | problema, frustração, incômodo real que o avatar vive hoje | prende, gera identificação ("ele sabe o que eu sinto"), cria urgência | o avatar diria isso numa conversa? o HT resolve? |
| Desejo | o que ele já quer conquistar ou viver | vende o futuro, motiva a agir; costuma casar com a promessa | ele já pede isso nos comentários e caixinhas? |
| Objeção | bloqueio para acreditar ou dar o próximo passo (declarado ou não) | respondida no conteúdo, aumenta a crença no expert | é um "mas" que trava a decisão? |
| Oportunidade | algo novo, pouco explorado, que ele ainda não sabe que existe ou que o expert entrega | ativa curiosidade, mostra caminho novo | ele se surpreenderia ao ouvir? |

**Truque central**: a âncora é o que sai da boca do avatar. Escrever em 1ª pessoa, como ele falaria.
Exemplo de correção de referência: trocar a etiqueta técnica ("falta de autoridade percebida") pela frase do avatar
("talvez eu não seja bom o suficiente para vender no Sebrae").

## 2. Zonas cinzentas e como corrigir

- **Dor x ação**: "fico procurando saber dele" é ação. Reescrever para o incômodo por trás da ação.
- **Dor x objeção**: "preciso de um alto investimento para abrir consultório" soa objeção. Mover de aba ou reescrever.
- **Desejo x oportunidade**: desejo ele já quer; oportunidade ele não sabe que quer. O mesmo tema muda de aba conforme o nível
  de consciência do avatar. O método admite que as duas se confundem às vezes: o critério final é conversar com o avatar.
- **Dor genérica**: "síndrome do impostor" atrai qualquer pessoa. Ligar ao nicho ("empreender na enfermagem").
- **Dor de consciência avançada**: dor que o avatar ainda nem sente (ex.: "meu produto não vai ter a minha cara") não conecta
  agora; trocar pela dor que ele sente hoje.
- **Objeção não é só dinheiro e tempo**: incluir as não declaradas ("não sei se consigo", "fora da minha zona de conforto").
  "Não tenho dinheiro" quase nunca vira Reels, porque o Reels não é contexto direto de venda.
- **Atração x nutrição**: o método não separa âncoras assim; toda âncora cumpre o papel se identificar o avatar nos primeiros segundos.

## 3. Fontes para levantar as âncoras

Dúvidas que o expert mais recebe; onde os alunos mais travam; comentários e caixinhas de perguntas; DMs; respostas do Raio-X,
da pesquisa da página de obrigado da aula semanal e do NPS (ler em `01-pesquisa/` e `03-sessao/`, sem copiar dado pessoal
para material público). Tempo do exercício: 10 min para 5 dores, 5 min para as outras (ponto de partida, não teto).

## 4. Âncora x tema x conteúdo

- **Tema** é sobre o que se fala. **Âncora** é o tempero, o ângulo dado ao tema.
- Ordem fixa: escolher a âncora → escolher qual dor/desejo/objeção/oportunidade → definir o tema → definir o conteúdo que
  resolve a dor, realiza o desejo, quebra a objeção ou mostra a oportunidade.
- Exemplo desconstruído (supermercado): âncora = dor do lucro pequeno; tema = por que o lucro é pequeno; conteúdo =
  promoção sem estratégia corrói a margem. (Exemplo de aluno, só como molde.)

## 5. Banco de temas: 40 no mínimo

o método pede 50 e o método corrige ao vivo para 40 ("vou tirar 10 aí pra ficar mais fácil", paráfrase). A skill entrega
no mínimo 40, com no mínimo 8 por âncora; o agente gera mais quando o banco
acabar ("me traga mais N"). Entradas do agente: promessa, nicho e subnicho.

Tabela do arquivo `AAAA-MM-DD-ancoras-e-temas.md`:

| # | Âncora | Item da âncora (fala do avatar) | Tema | Promessa provável | Framework sugerido | Usado em |
|---|---|---|---|---|---|---|
| 1 | Dor | "…" | … | … | jeito errado/certo | AAAA-Www |

A coluna "Usado em" evita repetir tema sem querer e alimenta a replicação (o tema vencedor ganha variação com um ajuste).

## 6. Prompt de rascunho

Usar como acelerador; a saída sempre passa pela curadoria da seção 7. Preencher a partir de `01-pesquisa/` e `02-oferta/`.

```
Você vai me ajudar a levantar as 4 âncoras de conteúdo de um avatar e depois temas de Reels.
Promessa do produto do expert: [promessa de 02-oferta].
Nicho: [nicho]. Subnicho: [subnicho]. Avatar: [quem é, momento de vida/negócio].
Frases reais do avatar (comentários, caixinhas, DMs, Raio-X): [colar 10 a 30, sem nome].

Passo 1. Liste no mínimo 5 itens de cada âncora: dores, desejos, objeções, oportunidades.
Regras: escreva em primeira pessoa, como o avatar falaria; dor é incômodo, não ação; dor ligada ao nicho, nunca genérica;
desejo é o que ele já quer; oportunidade é o que ele ainda não sabe que existe; inclua objeções não declaradas.
Marque cada item com a frase real que o inspirou, ou "sem frase real" se for dedução.

Passo 2. Para cada âncora, sugira 12 temas de Reels (assunto específico do vídeo), cada um com a âncora de origem.
Não repita tema. Não use jargão técnico que o avatar não usa.
```
Depois: "traga mais 10 temas de [âncora]" quantas vezes precisar.

## 7. Curadoria e auditoria das âncoras

Para cada linha, marcar ok ou corrigir:
1. Está em 1ª pessoa, na fala do avatar? (não na ótica do expert)
2. É da aba certa? (dor x ação x objeção; desejo x oportunidade)
3. É específica do nicho e do subnicho?
4. O avatar sente isso hoje? (não é consciência avançada)
5. O HT do expert resolve isso? (dor que o produto não resolve sai)
6. Tem frase real por trás, ou é dedução? (dedução fica marcada para validar nos comentários)
7. Está na voz do expert, sem cara de IA? (passar `avoid-ai-writing`/`humanizer` só no texto que vai ao ar)
Saída: a lista corrigida com nota curta por linha alterada. Nunca copiar e colar a saída da IA sem curadoria.

## 8. Exemplos de âncora (molde, não prova)

- Dor (corporativo feminino): ser deixada de fora das decisões apesar de entregar bem.
- Desejo (psicólogas): lotar a agenda e depois trabalhar menos ganhando mais.
- Objeção (escoliose): medo de piorar a coluna do paciente.
- Objeção (emagrecimento): "já tentei de tudo".
- Oportunidade (terapeutas): ganhar sem lotar a agenda.
- Oportunidade quente: mudança de legislação do nicho (o material cita reforma tributária e NR1 como assunto quente).
São de alunos de outros nichos; servem só para mostrar o formato.
