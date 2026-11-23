---
name: ht-funil-de-entrada-para-ht
description: 'Desenha o funil de entrada que alimenta o HT: produto barato como PENEIRA para a sessão 1a1 (três peneiras: minicurso, aplicação paga reembolsável, sessão), curso como máquina de vendas do HT, funil com lucro na captura (CAC, ACV) e fontes de lead qualificado. Use para "só lead quente na sessão", "funil das três peneiras", "qual o CAC e o ACV". NÃO usar para low ticket como negócio.'
---

# Funil de entrada para o HT

## 1. Para que serve e o que entrega

Resolve o problema do expert com pouca audiência que leva lead frio do criativo direto para a sessão e ouve "vou pensar".
Um produto barato (ou um bônus, ou uma sessão paga) faz o lead **se filtrar**: quem compra, consome e aplica chega à sessão
quente. O objetivo é **venda do AR**, não lucro no produto de entrada ("não temos low ticket, é um funil", na fala dos alunos
do case). Só a variante C (lucro na captura) trata o produto de entrada como fonte de caixa, e mesmo assim para pagar o tráfego.

Variantes do método:
- **A. Três peneiras**: minicurso pago ~R$ 49,70 → conteúdo que eleva dor e desejo, pitch na 3ª aula e repeat na
  4ª aula → aplicação paga ~R$ 500, reembolsável → sessão 1a1. É a variante padrão desta skill.
- **B. Curso como máquina de vendas do HT**: curso de preço baixo com módulo 0 "comece por aqui" que convida para
  imersão, live semanal e avaliação de negócio; resumo de módulo que captura contato.
- **C. Funil com lucro na captura**: produto principal + 2 a 3 complementos + upsell; aumenta investimento só
  quando sobe o ACV; aulas que qualificam e levam à sessão estratégica.
- **D. Fontes de lead qualificado**: bônus Kinder Ovo num produto barato já existente; sessão de avaliação vendida
  como produto (R$ 97 a ~R$ 3 mil, abatida no HT); consultoria gratuita filtrada por formulário.

**Entrega** (em `experts/<slug>/ht/04-demanda/funil-de-entrada/`):
1. **Desenho do funil**: fluxograma em texto (tráfego → página → checkout → aulas → pitch → aplicação → sessão), cada etapa com
   métrica, meta e dono.
2. **Especificação do produto de entrada**: promessa (derivada da Roma do AR), índice de aulas com o tipo de conteúdo de cada uma,
   pitch e repeat, frase de aterrissagem, duração do acesso.
3. **Pedidos às skills vizinhas**: página e checkout (`ht-web-designer`/`ht-copy-paginas-e-emails`), criativos
   (`ht-criativos-high-ticket`), campanha (`ht-trafego-high-ticket`), automações e tags (`ht-gestor-automacoes`), aplicação e
   agendamento (`ht-agendamento-e-follow-up`), sessão (`ht-roteiro-sessao-1a1`).
4. **Painel de peneiras e conta de CAC/ACV** (`references/metricas-cac-acv.md`) e plano de ciclo (minicurso → IMA → novo minicurso).

## 2. Antes de começar

1. Carregar `ht-protocolo`. Portão: Aprovação 1 (oferta do AR aprovada); o funil vende o AR que está em `02-oferta/`.
2. Ler em `experts/<slug>/ht/`: `02-oferta/` (definição do AR, Roma, pilares, preço, garantia), `01-pesquisa/` (dores, desejos,
   objeções, quem decide a compra), `03-sessao/` (roteiro, Raio-X, conversão atual: o funil existe para subir esta conversão),
   `04-demanda/` (audiência atual, produtos que já existem), `07-numeros/` (verba e metas), `13-aprendizados/`.
3. Escolher a variante pelo que o expert já tem:
   - já vende curso ou produto barato → **D (Kinder Ovo)** ou **B (curso como máquina)** primeiro, custo de aquisição zero;
   - não tem produto e tem pouca audiência → **A (três peneiras)**;
   - quer que a captação se pague e tem operação para vários produtos → **C**.
4. Perguntas (máximo 3, só o que não está nos arquivos):
   - "O expert já tem algum produto barato ou base de compradores?" (muda a variante)
   - "Qual verba fixa podemos pôr no tráfego do minicurso e o faturamento dele volta para o tráfego?"
   - "Quem decide a compra no nicho e quem precisa ser excluído (ex.: secretária, estudante)?"

## 3. Passo a passo (variante A, três peneiras; B, C e D em `references/curso-lucro-na-captura-e-fontes.md`)

Fluxograma e checklist de montagem da variante A: `references/tres-peneiras-passo-a-passo.md`.

### Passo 1. Promessa do minicurso (peneira 1: exclui o frio)
- Derivar da Roma do AR trocando poucas palavras, no vocabulário do avatar. O minicurso promete um passo do caminho, não o destino.
- Nome simples; preço baixo (referência do caso R$ 49,70; o agente assume o preço e lista em "Assumi").
- Filtro de quem compra: exigir um dado que qualifica (no case, número do registro profissional) e excluir quem não decide.

### Passo 2. Conteúdo que eleva a dor sem saciar (peneira 2: exclui o morno)
- Usar pelo menos um dos **3 tipos**: conteúdo de **erro** (desfaz uma crença falsa), **quick win que cria nova dor** (resolve
  um pedaço e revela o próximo problema) e **custo de oportunidade** (o que a pessoa deixa de ganhar).
- Ensinar o **o quê e o porquê, não o como**. Frase de aterrissagem entre aulas lembrando que aquilo não basta para chegar à Roma.
- Estrutura de referência do case (5 aulas): história e erro · pilares do AR · quick win + **pitch** · custo de oportunidade +
  **repeat** · "aula zero" de quebra de objeções já liberada na entrada. Duração: no case a 1ª aula teve ~25 min e as outras
  ~1 h (pitch incluído); para aquele avatar (cirurgião) aula curta parecia fraca e 1 h não atrapalhou, mas houve queixa de
  aulas longas e a rodada seguinte, em teste, foi para 7 aulas de 30 a 40 min. Duração é decisão por avatar, não regra.
  Detalhe e roteiro por aula em `references/conteudo-do-minicurso-e-pitch.md`.
- **Pitch na 3ª aula** igual ao pitch da IMA do método (o que é, o que não é, para quem é e não é, resultados, pilares, preço,
  garantia), com o preço dito; **repeat na 4ª aula** (prova antes, prova emocional, repeat, parabéns a quem decidiu).
- A pessoa precisa chegar ao pitch depois das aulas de dor e desejo (ver o pitch antes queima a construção). No case isso foi
  feito pela ordem de liberação e pelas mensagens de "assista na sequência", não por trava técnica; travar a aula do pitch
  por pré-requisito na plataforma é opção, se ela permitir (conferir). Nada de vender outro produto barato no momento do pitch.
- Preço do AR dito no pitch, e só depois do preço a explicação da aplicação paga (no case, apresentada como garantia).

### Passo 3. Página, checkout e acesso
- Página simples: primeira dobra com a promessa do minicurso, o benefício, o preço e **um** botão para o checkout; avisos de
  exclusão ("somente para <perfil>"); para quem é e não é; programação das aulas; o que vai aprender; perguntas frequentes.
- Checkout com acesso imediato, aula inaugural e **pesquisa rápida** de quem comprou (orienta os próximos criativos).
- Acesso por tempo limitado e declarado (no case, 3 semanas fixas na rodada nova).

### Passo 4. Tráfego para o minicurso
- Público frio; criativos que falam **só da promessa do minicurso** (simples funcionam: no case, estáticos do expert trabalhando e
  um vídeo dele falando da dor). Objetivo Vendas, evento Purchase do checkout; sobe PAUSADA pela `ht-trafego-high-ticket`.
- Verba fixa definida pelo estrategista e reinvestimento do faturamento do minicurso no tráfego (no case: R$ 11 mil de base, R$ 22,2 mil
  no total investido).
- Ajuste por peneira seguinte: o criativo se ajusta pela pesquisa de quem **comprou**; o conteúdo se ajusta pelo questionário de
  quem **aplicou**.

### Passo 5. Automação de consumo (fazer assistir em ordem)
- Tag na compra; grupo VIP e mensagens individuais por e-mail e WhatsApp; toda mensagem reforça assistir todas as aulas na
  sequência e o acesso com prazo; contagem regressiva no fim (3, 2, 1 dia e último dia).
- Monitorar na plataforma: progresso, tempo médio e curva de retenção por aula; corrigir aula com queda abrupta (no case, um
  trecho do pitch derrubou ~20% da retenção e foi cortado).
- Tag "viu o pitch" dispara a mensagem de aplicação. Envio a lead/aluno só liga com OK do estrategista.

### Passo 6. Aplicação paga (peneira 3: seleciona o muito quente)
- Link de aplicação em **todos** os pontos: abaixo da aula do pitch e do repeat, numa aula só com o link e o passo a passo, no
  e-mail, no grupo e no WhatsApp individual logo depois de a pessoa ver o pitch.
- Formulário de aplicação do método terminando em pagamento (referência R$ 500), apresentado como **garantia**: se o caso não tiver
  como dar resultado, o valor volta. Recusa antes ou depois da sessão com devolução (no case: 6 de 24 recusados e reembolsados).
- Pagou → mensagem **na hora** para agendar a sessão o mais rápido possível (2 a 3 dias esfria); 2 horários, sessão em até 2 dias
  (padrão do squad).

### Passo 7. Sessão 1a1 e ciclo
- Sessão normal (`ht-roteiro-sessao-1a1`): Raio-X, deixar a pessoa falar, mostrar a oportunidade, entregáveis em versão curta,
  forma de pagamento. O valor da aplicação abate no AR se `02-oferta/` assim definir.
- Fim do ciclo: o lead morno não recebe outro produto barato; volta a ouvir o pitch no próximo canal (minicurso → IMA → novo
  minicurso; também aula semanal, SHT, SLG).
- Debrief com o painel de peneiras em `13-aprendizados/`.

## 4. Regras inegociáveis do método

- O produto de entrada é **filtro do AR**: promessa derivada da Roma, pitch do AR dentro dele, métrica final = AR vendido.
- Não saciar a dor; ensinar o o quê e o porquê. Quem acha que resolveu não aplica.
- Não liberar a aula do pitch a quem não viu as anteriores; não vender outro produto menor no pitch.
- Não deixar o aplicante esfriar sem agendar.
- Preço do minicurso, valor da aplicação, regra de reembolso e abatimento saem de `02-oferta/` (aprovados pelo estrategista).
- A aplicação "reembolsável se não houver fit" é diferente da garantia do AR (padrão recomendado: condicional, mensurável, ligada à execução):
  não confundir nem misturar as duas na copy.
- Número de case é **amostra pequena** (um ciclo, 18 vendas): nunca vira promessa ao expert nem material de venda.
- Diferença com low ticket como negócio: lá o produto barato é motor de lucro e base; aqui é peneira do AR. Não misturar os dois métodos.

## 5. Padrões assumidos (o agente decide e lista em "Assumi: … (é só pedir para mudar)")

- **Variante** (A, B, C, D) para o expert.
- **Preço do minicurso** e **valor da aplicação** (referências: R$ 49,70 e R$ 500; a sessão paga vendeu mais a R$ 500 que a
  R$ 197 num teste do método; faixa citada R$ 97 a ~R$ 3 mil). Contras a avisar: aplicação mais cara filtra mais e reduz
  volume.
- **Reembolso e abatimento** da aplicação no AR.
- **Complementos e upsell** (variante C): mais ACV x risco de dividir a atenção e baixar a aplicação.
- **Verba fixa e reinvestimento** do faturamento do minicurso.
- **Duração do acesso** ao minicurso e número de aulas.

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Variante escolhida com o motivo; promessa do minicurso derivada da Roma do AR (frase lado a lado).
- [ ] Índice de aulas com o tipo de conteúdo de cada uma, pitch na 3ª aula, repeat na 4, frase de aterrissagem.
- [ ] Página, checkout com pesquisa, filtro de qualificação e prazo de acesso especificados.
- [ ] Automação de consumo e tag "viu o pitch" desenhadas (sem ligar envio).
- [ ] Aplicação paga com garantia de devolução, links em todos os pontos e disparo imediato de agendamento.
- [ ] Painel de peneiras com metas e conta de CAC/ACV; decisões do estrategista listadas.

**Auditoria (erros típicos):**
1. Lead frio do criativo direto para a sessão (o erro que o funil corrige)?
2. Promessa do minicurso que não leva ao AR, ou que já entrega a Roma?
3. Conteúdo que ensina o como e sacia a dor?
4. Pitch liberado para quem não viu as aulas? Preço escondido no pitch?
5. Produto menor vendido no pitch, dividindo a atenção?
6. Aplicante esperando dias para agendar?
7. Sem filtro de quem decide (secretária, estudante comprando)?
8. Criativo do minicurso falando do HT em vez da promessa do minicurso?
9. Métrica final só de vendas do minicurso, sem aplicação e AR vendido?
10. Número do case usado como meta ou promessa?
11. Reembolso da aplicação confundido com a garantia do AR?

## 7. Saída e handoff

- Gravar em `04-demanda/funil-de-entrada/` (desenho, especificação, painel). Debrief em `13-aprendizados/`.
- Handoff: `ht-revisor-metodo-copy` (aulas, pitch, página, mensagens) · `ht-copy-paginas-e-emails` e `ht-web-designer` (página e
  checkout) · `ht-criativos-high-ticket` + `ht-gestor-trafego` (captação) · `ht-gestor-automacoes` (tags e envios, só com OK) ·
  `ht-closer` (sessões) · `ht-controller` (CAC, ACV, reinvestimento) · `ht-arquiteto-oferta` (se o preço do minicurso ou da
  aplicação precisar entrar em `02-oferta/`).

## 8. Ferramentas de apoio

`gerador-slides` ou `slides-uipm` (aulas), `criacao-guia-gravacao` (pauta de gravação das aulas), `pagina-design-premium`
e `publicar-pagina-cloudflare` (landing), `hotmart-meta-conversao` (Purchase do checkout), `email-marketing-mautic`,
`automacao-fluxos` e `conectar-whatsapp-oficial` (sequência de consumo, só com OK), `anthropic-skills:xlsx` (painel e CAC/ACV),
`watch` (rever aula e achar trecho que derruba retenção).## 9. Limites (não inventar)

A pasta "três peneiras" (fluxograma, 12 mensagens de grupo, e-mails, WhatsApp individual, tabela de quando enviar e quem excluir) não
vem no pacote: há só a estrutura, não os textos das mensagens. Não há CPA do minicurso nem custo por aplicação de referência. A
variante C é só estrutura de slide. O caso de referência tem um ciclo e amostra pequena (100% de conversão em 18 sessões). Preço ideal
do minicurso por nicho não é definido.
