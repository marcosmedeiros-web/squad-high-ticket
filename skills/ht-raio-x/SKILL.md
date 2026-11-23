---
name: ht-raio-x
description: 'Squad High Ticket / método FHT. Cria, aplica e audita o Questionário Raio-X da sessão 1a1 (5 a 7 áreas, 5 perguntas de 0 a 10 por área, planilha com radar atual x desejado), escreve a fala de aplicação na call, o tratamento de notas extremas e o mapa de consequências para a leitura do gráfico. Use quando o estrategista disser "cria o Raio-X do expert", "perguntas do diagnóstico da sessão", "monta a planilha do Raio-X", "como aplico o Raio-X na call", "como leio o gráfico", "revisa esse Raio-X", "o gráfico saiu torto". Entrega rascunho para o estrategista aprovar. NÃO usar para o diagnóstico de entrega do aluno (ht-entregaveis-1a1), para o roteiro inteiro da sessão (ht-roteiro-sessao-1a1) nem para lançamento pago semanal, 5+1 ou Funil 8 (método LPSG, fora do escopo deste squad).'
---

# Raio-X da sessão 1a1

## 1. Para que serve e o que entrega

O Raio-X é o questionário de notas que o vendedor aplica na sessão 1a1 para aflorar a necessidade do HT: a pessoa se avalia
de 0 a 10 em perguntas curtas, a planilha gera dois radares (o desejado, 100% em tudo, e o atual) e a leitura do gráfico
implica a consequência de cada área fraca. Funciona como consulta médica: quem investiga com método ganha o direito de
recomendar. Raio-X é ferramenta de **venda**; o diagnóstico que o aluno recebe depois de comprar é **entregável** e mora em
outra skill.

**Entrega** (pasta `03-sessao/raio-x/`):
1. `AAAA-MM-DD-raio-x-<nome-da-sessao>.md`: as áreas (nome de uma palavra ou duas), as 5 perguntas de cada área, a marca de
   pergunta invertida (se houver), a fonte de cada área na oferta (qual entregável resolve) e a versão curta de 5 áreas.
2. `AAAA-MM-DD-raio-x-<nome-da-sessao>.xlsx`: planilha no modelo FHT (especificação em `references/planilha-raio-x.md`),
   notas de exemplo zeradas, testada com notas baixas e altas.
3. `AAAA-MM-DD-aplicacao-e-leitura.md`: fala de abertura do questionário, regras de notas extremas, mapa de consequências
   por área (lado fraco e lado forte), roteiro da leitura do gráfico e a pergunta de transição para o herói relutante.
4. Auditoria preenchida (`references/auditoria-raio-x.md`) e bloco de entrega do protocolo.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões, pasta com dono, proibição de misturar LPSG).
2. Ler em `<raiz_projetos>/<expert>/ht/`:
   - `02-oferta/oferta-vigente.md` (pela regra de leitura da oferta do protocolo: antes da Aprovação 1, a proposta vN mais
     recente, e o Raio-X fica em rascunho): definição do AR, ponto A e B, jornada, pilares e entregáveis. **Sem oferta (vigente ou
     proposta) não há Raio-X**: cada área tem de apontar para algo que o HT resolve.
   - `01-pesquisa/`: avatar, 4 âncoras (dores e desejos na voz dele), Market Fit, indicadores duros do nicho.
   - `03-sessao/` (nome em `nome-da-sessao.md`, dono ht-closer; ausente = `[A CONFIRMAR COM ht-closer]`): nome da sessão (o convite), roteiro e Raio-X anteriores, objeções registradas.
   - `13-aprendizados/` e `07-numeros/` (Central 1x1): notas reais de sessões já feitas, se existirem.
3. Entradas obrigatórias: definição do AR, pilares e entregáveis, nome da sessão. Se faltar, no máximo 3 perguntas, por
   exemplo: "Qual o nome do convite da sessão?"; "Existe um indicador objetivo do nicho que o lead consegue trazer (medidas,
   faturamento, taxa de conversão)?"; "Quem vai aplicar: o expert ou um vendedor?". O resto vira `[FALTA: …]`.

## 3. Passo a passo

**Passo 1. Escolher as áreas (7, versão curta com 5).**
- Partir dos pilares e da jornada do AR. Cada área é um gargalo do avatar **que o HT resolve depois**: evidenciar gargalo que
  a oferta não arremata é erro (a oferta tem de contemplar todas as áreas medidas).
- Incluir ao menos uma área em que o avatar costuma ir bem (desejo, importância do tema, crença na própria capacidade): ela
  dá equilíbrio ao gráfico e é o ponto de partida da leitura.
- Nome de cada área com 1 ou 2 palavras (nome longo quebra o rótulo do radar).
- Ordem lógica, na ordem da jornada do AR: se o diferencial do expert começa por uma base (ex.: autoconhecimento antes da
  técnica), essa área vem primeiro; área solta no meio confunde o lead (laboratório abr/2026).
- Sem áreas que o lead não pode ter (se tudo daria zero, talvez nem seja o avatar).
- Montar desde já a versão de 5 áreas: ela substitui a de 7 quando a sessão passa de 30 minutos antes da leitura.

**Passo 2. Escrever 5 perguntas por área** (regras completas e reescritas certas/erradas em
`references/regras-de-pergunta.md`).
- Formato fixo: "De 0 a 10, o quanto você…", 0 = ruim e 10 = bom, com os extremos definidos quando houver ambiguidade
  (ex.: 0 = nunca, 10 = todos os dias).
- Sempre 5 por área: a planilha soma as 5 notas e multiplica por 0,02; com menos de 5, nem nota 10 chega a 100% e o gráfico
  mente.
- **Padrão do squad:** pergunta de fato ou de resultado com período ("nas últimas 5 negociações", "nos últimos 3 meses");
  no máximo **1 pergunta de percepção por área** ("o quanto você se sente seguro…").
- Situação específica, nunca genérica (a pessoa revive a cena); curta; um verbo só; sem jargão; sem sim/não; sem pergunta
  aberta; sem induzir à mentoria ("o quanto um acompanhamento te ajudaria" é proibido).
- Pergunta "negativa" (10 = ruim) é reescrita para o positivo. Se ficar invertida, marcar em vermelho na planilha e lançar
  10 menos a nota.
- Escrever para outra pessoa aplicar: o vendedor sem o conhecimento do expert tem de conseguir fazer a pergunta.
- Opcional por nicho: um campo de **indicador duro** (medidas, faturamento, taxa de fechamento) que vira dado de risco no
  gráfico. Só com fonte do expert sobre o cálculo.
- O GPT da FHT "Criador de Questionário Raio-X" existe para gerar a primeira versão a partir da definição do AR; a skill pode
  fazer o mesmo papel. Em qualquer caso, curadoria humana: conferir redundância, viés e se o lead consegue responder.

**Passo 3. Montar a planilha.** Seguir `references/planilha-raio-x.md`: aba "Diagnóstico de Negócio", blocos por área, nota
na coluna de resposta, total = soma × 0,02, tabela final Atual x Meta (1,0), dois radares com a mesma escala (0 a 100%).
Gerar com `anthropic-skills:xlsx`. Testar três vezes: tudo 0, tudo 10, notas mistas. Conferir rótulos, escala e a pergunta
invertida. Zerar antes de entregar.

**Passo 4. Escrever a fala de aplicação** (modelo em `references/aplicacao-e-leitura.md`).
- Dizer o objetivo (diagnóstico para ver pontos fortes e pontos a melhorar), a escala (0 muito ruim, 10 muito bom), que não
  é prova e que **não precisa justificar a nota, a não ser que o vendedor peça**.
- Não mostrar a tela enquanto pergunta; tom de bate-papo de consultório, não de formulário.
- Notas extremas: nota até 3 → "me fala um pouco mais sobre isso" e anotar as palavras literais; nota alta que contradiz o
  que a pessoa disse na pergunta inicial → devolver com o que ela disse e perguntar se mantém; nota alta de ego → pedir o dado
  ("quantos clientes novos no último mês?").
- Anotar palavras literais do lead: viram consequência na leitura, personalização da oferta e os três sins.
- Pergunta de urgência no fim (isso é prioridade hoje?).
- Tempo: Raio-X aplicado em cerca de 20 minutos; leitura começando até os 30 minutos de call (padrão do squad: sessão com
  alvo de 1h15 e teto de 1h30).

**Passo 5. Mapa de consequências e leitura do gráfico.**
- Para cada área, escrever antes da sessão: a consequência na vida do lead se ela continuar fraca (concreta, no mundo dele) e,
  para a área forte, o elogio e o "de nada adianta X forte se Y continuar fraco".
- **Padrão do squad (leitura):** a leitura começa por uma área boa, aprofunda as 3 piores (uma consequência para cada, usando as
  palavras do lead) e fecha com a consequência geral em 12 meses se nada mudar.
- Nunca dar solução na leitura (solução barata esfria a necessidade e desvaloriza a oferta). Nunca dizer que ninguém chega a
  100%: o azul é o normal de quem está bem.
- Fechar com "faz sentido para você?" (a pessoa conclui sozinha) e a pergunta de permissão ("você gostaria da minha ajuda para
  chegar aqui?"). O sim abre a história do herói relutante (`ht-roteiro-sessao-1a1`).
- Dosar: implicação demais faz a pessoa fugir ("não é para mim"); implicação de menos deixa a venda fria.

**Passo 6. Auditoria e ajuste em campo.** Rodar `references/auditoria-raio-x.md`. Depois das primeiras sessões, ajustar
pergunta que sempre gera 10, que o lead não entende ou que dá a mesma nota de outra; manter o histórico de versões.

## 4. Regras inegociáveis do método

- Toda pergunta é "de 0 a 10", quantitativa; nada de sim/não nem pergunta aberta.
- 5 perguntas por área, 5 a 7 áreas; a fórmula soma × 0,02 não muda.
- Área medida = área que a oferta resolve. Raio-X não fala da mentoria, do método nem do preço.
- Não ensinar nem resolver nada durante o Raio-X e a leitura.
- Gráfico com a mesma escala nos dois radares e nomes curtos; testado antes de ir para a call.
- Gravar a sessão desde o início (com aviso ao lead); notas e anotações vão para `03-sessao/privado/`.
- Padrões do squad que se aplicam: formato da leitura (área boa, 3 piores, consequência em 12 meses), tempo da sessão (alvo
  1h15, teto 1h30), tipo de pergunta (fato ou resultado com período) e conversão de referência de 10% a 20% (usada só para
  diagnóstico, não aqui).

**Divergências das fontes (mostrar, não esconder):** dizer ou não o número de perguntas ao lead (uma mentora manda não dizer;
outro diz "7 áreas, 35 perguntas" e relata sessão mais curta); "não precisa justificar" (ensinado em 2025-2026, criticado
numa turma de 2025). Padrão da skill: não anunciar o total e usar o aviso de não justificar; a alternativa vai como teste
para o estrategista aprovar.

## 5. Quando a decisão é do estrategista

- Usar o Raio-X de 7 ou de 5 áreas como padrão do expert (7 dá mais consciência; 5 cabe em agenda curta).
- Incluir indicador duro do nicho (mais impacto; exige cálculo correto e cuidado com dado de saúde ou financeiro).
- Testar o anúncio do total de perguntas (prós: expectativa gerenciada; contras: a pessoa pode cansar antes de começar).
Formato: opções a/b/c com prós e contras; o agente não decide.

## 6. Critério de pronto e auditoria final

- [ ] 5 a 7 áreas, cada uma com o entregável que a resolve; ao menos 1 área tende a ir bem.
- [ ] 5 perguntas por área, todas "de 0 a 10", extremos claros, no máximo 1 de percepção por área, sem sim/não, sem indução.
- [ ] Nenhuma pergunta repetida; invertidas reescritas ou marcadas.
- [ ] Planilha testada (tudo 0, tudo 10, misto), mesma escala, nomes legíveis, notas zeradas.
- [ ] Versão de 5 áreas pronta.
- [ ] Fala de aplicação, regras de nota extrema e mapa de consequências escritos; leitura no formato padrão (área boa, 3 piores, consequência em 12 meses).
- [ ] Nenhum número, caso ou indicador inventado.

**Auditoria** (`references/auditoria-raio-x.md`). Erros típicos dos laboratórios: pergunta sim/não; pergunta aberta; "você
entende/sabe" que todo mundo responde 10; pergunta sem período; pergunta invertida sem marca (gráfico torto); perguntas
duplicadas geradas por IA; área que o HT não resolve; menos de 5 perguntas; nome de área longo; escala diferente nos radares;
pergunta que depende de algo fora do controle do lead; pergunta tendenciosa para a mentoria; leitura que dá solução; leitura
sucinta, sem aprofundar a nota baixa; começar pelas áreas ruins; frase "a perfeição não existe"; não anotar as palavras do lead.

## 7. Saída e handoff

- Gravar em `<raiz_projetos>/<expert>/ht/03-sessao/raio-x/` com o bloco de entrega do protocolo. Notas de leads reais ficam em
  `03-sessao/privado/`.
- Revisão: texto → `ht-revisor-metodo-copy`; planilha e gráfico → `ht-revisor-visual`.
- Segue para `ht-roteiro-sessao-1a1` (o Raio-X entra na etapa 2 do roteiro) e para `ht-treino-comercial` (roleplay).
- Debrief depois de 5 sessões: perguntas trocadas e por quê em `13-aprendizados/`.

## 8. Ferramentas de apoio (por nome, sem copiar)

`anthropic-skills:xlsx` (planilha e radares) · `avoid-ai-writing` e `humanizer` (fala de aplicação e consequências) ·
`voice-builder` (tom do expert) · `niche-research` (indicador duro e linguagem do nicho, só com fonte).

## 9. Fontes e lacunas

**Fontes:** trilha 09, bootcamp Vendas através de Sessão 1:1, aulas 06 (Raio-X) e 07 (leitura do gráfico), e
RESUMO-vendas-por-sessao-1a1.md §3, §5.3, §5.4, §6; rota 3, resumo 05 (regras, planilha, exemplos); planilhas
`rota3/materiais/planilhas/sessao1a1-questionario-raio-x.xlsx` (5 áreas) e `sessao1a1-roteiro.xlsx` (é o Raio-X de 7 áreas);
trilha 22, bootcamps e laboratórios de sessão 1a1 (abr/2026 aulas 93-95, transcritas; mai/2026 79-80; jul/2026 RJ
07-09 e 12; dez/2025 143-144; jan/2026 128; engenharia reversa jan/2025 192-195); catálogo (fht-raio-x-questionario,
fht-auditoria-raio-x, fht-aplicar-raio-x-na-sessao, fht-leitura-do-grafico), partes B, E, F, G; GPTS-DA-FHT.md;
padrões do squad (formato da leitura, tempo da sessão, tipo de pergunta).

**Lacunas (não inventar):** o bootcamp dedicado só ao Raio-X foi anunciado e não existe nos arquivos; o prompt do GPT criador
de Raio-X não está disponível; a transcrição da aula 93 (abr/2026) acaba antes da aplicação do Raio-X; o arquivo do checklist
oficial de condução não existe (o bootcamp abr/2026, aula 94, só descreve a estrutura: Raio-X em ~20 min, explicar a escala,
pedir contexto só quando precisar, mudar de pergunta com delicadeza se o lead se alonga); não há benchmark numérico de nota média por nicho.
