---
name: ht-escala-da-entrega
description: 'Squad High Ticket / método FHT. Tira o expert da entrega sem perder qualidade: nível (expert, mentores em partes, time inteiro), capacidade pelo consumo real, navegador, manual de entregáveis, recrutar, contratar e treinar mentores, diário do mentor, transferência de autoridade, qualidade por NPS e IA, gestão no Notion, planilha de Problemas e Oportunidades e auditorias do processo e de gravação. Use quando o estrategista disser "o expert não dá conta", "tira o expert da entrega", "manual do mentor", "preciso contratar mentor", "treina o novo mentor", "quantos alunos cabem", "audita a entrega", "essa sessão ficou no padrão?". NÃO usar para o cardápio (ht-entregaveis), roteiro de um entregável (ht-entregaveis-1a1), avaliação automática por IA (ht-avaliacao-de-reunioes-por-ia) nem CS de LPSG da Turbo.'
---

# Escala da entrega do HT

## 1. Para que serve e o que entrega

O cliente compra o resultado, não o expert. Quando o método está escrito, treinado e auditado, outra pessoa entrega com o mesmo
padrão, o expert volta a vender e a criar, e a experiência do aluno melhora em vez de piorar (resposta mais rápida, mentor com
contexto, menos improviso). O FHT chegou a mais de 15 mentores para 500+ alunos com NPS acima de 95% (trilha 19, números de
aula). Esta skill leva o projeto do expert pelos 3 níveis de delegação, na ordem certa e sem pular etapa.

**Entrega**, em `experts/<slug>/ht/06-entrega/escala/`:
1. `nivel-e-capacidade.md`: nível atual, conta de horas pelo consumo real, gargalo, quando e quem contratar.
2. `manual/<entregavel>.md`: manual de cada entregável (o que é, como solicitar, documentos, aprendizados, processo de ponta
   a ponta, roteiro da sessão com tempos, checklist) e `banco-de-entregaveis.md`.
3. `mentores/`: perfil e critérios, lista de espera, proposta de contratação (por entrega → full time), cadastro, mentor
   training, plano de transferência de autoridade, métricas e rotina de qualidade.
4. `navegador.md`: função, rotina, prazo de resposta, capacidade.
5. `gestao/`: estrutura da base (Notion ou equivalente) com os 5 bancos e os boards.
6. `problemas-e-oportunidades.xlsx`: planilha viva de 9 colunas.
7. `auditorias/<AAAA-MM-DD>-processo.md` e `auditorias/<AAAA-MM-DD>-gravacao-<entregavel>-<mentor>.md`.

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir o pedido do Diretor.
- Ler: `02-oferta/oferta-vigente.md` (entregáveis, quantidades, o que foi prometido na venda sobre quem entrega),
  `06-entrega/` (roteiros de ht-entregaveis-1a1, grupo, NPS, gravações, consumo), `07-numeros/` (caixa, margem e Master Plan: a
  contratação depende de fluxo de caixa), `06-entrega/entregaveis-1a1/` e a conta de horas de ht-entregaveis.
- Entradas obrigatórias: número de alunos ativos e em entrada, consumo real por entregável, quantas vezes o expert já executou
  cada entregável (e se há gravação). Se faltar, no máximo 3 perguntas:
  1. Quantos alunos ativos e quantas horas por semana o expert gasta em entrega hoje?
  2. Quais entregáveis o expert já fez muitas vezes e tem gravados?
  3. Há candidatos a mentor (aluno com resultado, alguém do time, parceiro) e qual o orçamento mensal para entrega?

## 3. Passo a passo

### Passo 1. Diagnóstico do nível e da capacidade
Conta e tabela em `references/capacidade-navegador-e-niveis.md`.
- **Nível 1**: o expert entrega e cria o processo (turma piloto). **Nível 2**: mentores entregam partes (um entregável por vez).
  **Nível 3**: o time entrega tudo e o expert vira estrategista e rosto (palco, inaugural, encontros, entregas gravadas).
- Pré-requisito da parte 3 (trilha 19): método ou primeiras entregas estruturadas, ~10+ alunos. Sem venda: vender primeiro.
- Capacidade (padrão do squad): expert sozinho até ~20 alunos; mentor 1:70; navegador 1:100. As fontes divergem (expert de
  10 a 60; navegador de 25 a 100; mentor de 70 a 100): dimensionar pelo **consumo real**, não pelo total teórico (ex. de aula:
  consumo médio de 1,8 de 12 análises).
- Conta de horas: se todos consumissem tudo (ht-entregaveis) x o que consomem de fato; o gargalo é o entregável que mais toma
  hora do expert.
- Ordem de delegação do expert: administrativo → entrega → marketing → vendas → liderança. Contratar quando houver fluxo de
  caixa: foco em vender primeiro.

### Passo 2. Manual de entregáveis (antes de qualquer mentor)
Estrutura completa em `references/manual-de-entregaveis.md`.
- Só se escreve manual do que já foi executado. Referências: micro turma piloto de 3 a 5 (ou ~20) entregue pelo expert; executar
  cada entregável ~20 vezes antes de revisar; os fundadores do FHT entregaram sozinhos para cerca de 200 alunos antes de criar o
  guia de mentores, e o time já passou de 500 diagnósticos (trilha 19, aulas 13 e 14; números de aula, conferir).
- Começar pelo entregável gargalo, o mais repetitivo (no FHT, o diagnóstico).
- **Aprendizados** sem filtro (o que deu certo e errado, objeções, dificuldades), que não são instruções: o aprendizado decide
  o que entra no processo (ex.: "precisa quebrar objeção" virou o bloco de visão estratégica).
- **Processo de ponta a ponta**: solicitação → agenda → preparo (núcleo) → sessão → resumo no diário → NPS → gravação na área
  de membros. Depois detalhar a sessão: blocos, tempos, perguntas, falas-guia, fechamento.
- Ações autoexplicativas (por que e como, não só "cumprimente pelo nome").
- Banco de entregáveis: 10 a 12 bem descritos de onde o mentor escolhe o que indicar (o FHT tem 22 na oferta e cerca de 50 no
  banco). Habilidades complementares (design, tráfego, psicólogo) entram como consultorias pontuais com especialista.
- Processo versionado: muda a cada dúvida e entrega; aceitar até ~10% de falha em volume e corrigir rápido.

### Passo 3. Recrutar e contratar mentores
Detalhe em `references/mentores.md`.
- Quatro origens, em mix: aluno com resultado ("mão suja de terra"), pessoa do time, parceria (especialista que entrega por
  visibilidade, clientes ou comissão), mercado (profissional formado para área complementar).
- Duas formas: **por entrega** (1 a 2 horários na agenda, sem custo fixo) para começar; **full time** só depois que flui.
- Lista de espera de interessados, acionada quando há vaga e o candidato já tem resultado. Exercício: listar 5 candidatos.
- Fluxo: abordagem → cadastro → termos e contrato formal (o que pode e não pode) → onboarding → treinamento.
- Não pôr estagiário respondendo cliente de HT. Mentor dá direção clara; quem não confia no que fala não mentora.

### Passo 4. Treinar (mentor training) e transferir autoridade
Template em `references/mentores.md` (seção 3).
- Ciclo por entregável: aprender o manual → assistir 3 a 5 gravações daquele entregável → abrir horário → briefing com mentor
  veterano → 1ª entrega gravada, **sem o veterano na call** (testado e descartado no FHT) → veterano assiste e dá feedback + NPS
  do aluno → apto segue para o próximo entregável; senão revisita → amostragem contínua de calls pelo expert.
- Acessos: e-mail de mentor no domínio da empresa, ferramenta de chamada, logins, link de links, comunidade de mentores.
- O manual é a base; os treinos gravados (videoaula explicando o manual) vão sendo somados à área do mentor, assíncronos. Não é
  preciso ter tudo gravado para contratar o primeiro mentor: o FHT tem 15 mentores e não tem 100% dos treinos gravados; entregável
  ainda em mudança fica no individual (aula 16).
- O link de links do mentor inclui chamadas de exemplo marcadas no minuto exato (ex.: uma call em que o fundador desmonta a
  palestra de pré-pitch, usada em todo checkup de imersão).
- **Transferência de autoridade**: o expert apresenta o mentor na aula inaugural com história e resultados, coloca no palco
  (palestra em imersão), faz entregas juntos, fala bem dele e mostra os resultados que ele gerou. A venda já disse quem entrega.
  O mentor treinado pode começar a entregar antes de a transferência acontecer (aula 17).
- Com mentor dedicado, a escrita dos processos também é delegada: no FHT, só o processo do diagnóstico foi escrito pelos
  fundadores; os outros foram escritos pelos mentores full time (aula 18).

### Passo 5. Qualidade e acompanhamento dos mentores
- **Diário do mentor** (canal com histórico, ex.: Telegram): áudio de 1 a 1,5 min por entregável com aluno, programa,
  entregável, nicho, ferramenta e resumo. O próximo mentor chega com 100% do contexto. Pagamento por entrega condicionado ao áudio.
- Métricas do mentor: entregáveis executados, NPS médio por mentor, Toques de Midas gerados (ht-provas-e-cases), nota da
  avaliação por IA de cada call (ht-avaliacao-de-reunioes-por-ia).
- Recomendação de mentor que o expert não faria: ligar logo para corrigir. Treino recorrente quando o método muda.
- Matchmaking: mentor adequado por afinidade de nicho ou tema; o Raio-X do aluno cruza com o perfil do mentor.

### Passo 6. Navegador
- Contato proativo, indica o entregável certo, responde dúvida pontual (resolve ~80% das dúvidas), prazo de resposta em dias
  úteis declarado. No início o próprio expert é o navegador.
- Custo de referência R$ 1.500 a 3.000 ou permuta (aula, conferir); checkpoint mensal com cada aluno (quinzenal não funcionou);
  IA pode lembrar, não substitui o contato.

### Passo 7. Gestão (Notion ou equivalente)
Estrutura em `references/gestao-problemas-e-auditorias.md` (seção 1).
- 5 bancos duplicados **na ordem e no mesmo workspace**: Base de Alunos, Gestão de Entregáveis, NPS Entregáveis, Indicadores,
  Catálogo de Resultados. Linha = conta (individual, dupla, trio). Alternativas: Trello, ClickUp, Sheets.

### Passo 8. Problemas e Oportunidades (melhoria contínua)
Planilha de 9 colunas em `references/gestao-problemas-e-auditorias.md` (seção 2). Todos os mentores alimentam o tempo todo; a
coluna "framework" diz por que o problema existe (método não fornecido · fornecido e ineficiente · eficiente e não seguido ·
bom e melhorável). É a fonte de bootcamps (ht-entrega-em-grupo), entregáveis novos, ajustes no manual e da oferta de renovação.
Processo de evolução do método (live 057): ideia → implementar → engenharia reversa → passo a passo replicável → acompanhar →
analisar erros e acertos → evoluir.

### Passo 9. Auditorias
Checklists em `references/gestao-problemas-e-auditorias.md` (seções 3 e 4).
- **Do processo** (mensal ou a cada turma): aprovação, onboarding, ativação, formulários, gravação, NPS, manual, treino,
  delegação, renovação.
- **De gravação** (amostragem aleatória contínua): a call contra o manual do entregável, com feedback numerado ao mentor.

## 4. Regras inegociáveis do método

1. Não delegar o que não foi executado; manual antes de mentor.
2. Um entregável por vez, começando pelo gargalo.
3. Mentor sem processo faz do jeito dele: a metodologia é do dono.
4. Começar por entrega; full time depois.
5. 1ª entrega do mentor gravada, sem veterano na call; feedback depois.
6. Diário do mentor e documento de ações em toda entrega.
7. Prometer na venda quem entrega; nunca vender "com o expert" e entregar com outro sem dizer.
8. Dimensionar pelo consumo real; contratar com fluxo de caixa.
9. Gravar 100% das entregas (sem gravação não há treino, auditoria nem Toque de Midas).
10. Qualidade medida por NPS por mentor e por amostragem do expert.
- Padrões que se aplicam: capacidade de referência do squad, entregável individual "até N", protocolo regra 14 (dados de aluno em `privado/`).

## 5. Quando a decisão é do estrategista

- **Contratar** (quem, forma, valor por entrega ou fixo): é gasto. Opções: a) por entrega com 1 a 2 horários (recomendo:
  sem custo fixo, testa o encaixe); b) full time (agenda dedicada, custo fixo, pode assumir retenção e upgrade); c) parceria
  sem custo (visibilidade ou comissão; menos controle).
- **Proporção de capacidade** diferente do padrão do squad para este projeto.
- **Ferramenta paga** (Notion pago, IA de reunião, Circle).
- **Mudança no que a oferta promete** sobre quem entrega (texto público e risco ético).
- Contrato com mentor: termos e valores são do estrategista e do expert; o material não dá modelo.

## 6. Critério de pronto e auditoria final

**Pronto quando**:
- [ ] Nível e capacidade calculados com consumo real (ou marcado "estimado" quando não há dado).
- [ ] Manual do entregável gargalo com aprendizados separados do processo, processo de ponta a ponta e roteiro com tempos.
- [ ] Perfil de mentor, lista de candidatos e proposta de contratação com as opções para o estrategista.
- [ ] Mentor training com os passos a até i e responsáveis.
- [ ] Plano de transferência de autoridade com datas (inaugural, entrega conjunta, palco).
- [ ] Diário, métricas de mentor e rotina de amostragem definidos.
- [ ] Base de gestão desenhada (5 bancos, boards e vínculo por conta).
- [ ] Planilha de Problemas e Oportunidades criada com as primeiras linhas e o responsável.
- [ ] Auditoria feita com nota por item e plano de correção.

**Auditoria (erros típicos)**:
1. Contratar mentor antes de ter manual.
2. Manual escrito sem ter entregue (teórico).
3. Aprendizado confundido com instrução.
4. Delegar vários entregáveis de uma vez.
5. Veterano dentro da 1ª call do novo mentor.
6. Full time sem testar por entrega.
7. Sem diário: aluno repete a história a cada mentor; mentores se contradizem.
8. Notion com bancos em workspaces diferentes (vínculos quebram) ou linha por aluno em vez de por conta.
9. Mudar o método sem treinar o time.
10. Dimensionar pelo total teórico e contratar cedo demais (ou tarde, com o expert virando refém).
11. Expert que some da entrega sem transferir autoridade (o aluno sente abandono).
12. Mentor que dá opção solta em vez de direção.

## 7. Saída e handoff

- Grava em `06-entrega/escala/` (escreve o ht-arquiteto-entrega; o ht-estrategista-sucesso lê e confere). Dados de candidatos
  e alunos em `06-entrega/escala/privado/`.
- Manual, mentor training e textos → **ht-revisor-metodo-copy**. Estrutura visual (slides de treino) → **ht-revisor-visual**.
- Custos e caixa → ht-controller (`07-numeros/`). Avaliação de call por IA → ht-avaliacao-de-reunioes-por-ia. Indicadores →
  ht-central-e-kpis. Bootcamps saídos da planilha → ht-entrega-em-grupo. Oferta de renovação → ht-renovacao.

## 8. Ferramentas de apoio

`anthropic-skills:xlsx` (planilha de problemas, capacidade, base), `anthropic-skills:docx` (manual, contrato-rascunho para o
jurídico), `anthropic-skills:pptx` / `gerador-slides-turbo` (treino de mentores), `transcrever-youtube-turbo` e `watch`
(auditoria de gravação), `analytics-dashboard` (indicadores), `automacao-fluxos` (formulários e NPS, com OK).

## 9. Fontes e lacunas

**Fontes**: trilha 19, aulas 08, 09, 10 e 13 a 18 (Notion, problemas e oportunidades, delegação, manual, negociação e
treinamento de mentores, transferência de autoridade, encerramento), RESUMO §3 a §10; parte-A (navegador e capacidade), parte-D
blocos 6, 8 e 9 (manual, recrutador, treinador, auditor de gravação e de processo), parte-E (dimensionar time), parte-G
(dimensionador de navegador), parte-H (manual do mentor, 3 níveis, diário e qualidade por IA, matchmaking, NPS, engajamento,
auditoria de escalabilidade, direção sem neutralidade), parte-I (manual e banco, formar mentores, entrega sem o expert,
habilidades complementares); lives FHT 011, 021, 029, 057 (processo de validação do método) e 060 (etapa de entrega da jornada
do FHT), as duas últimas transcritas hoje. Revisão de 23/11/2026: trilha 19 aulas 08, 09, 13 a 18 lidas por inteiro.

**Lacunas**: (1) os templates (Notion Mentor Training, manual no MindMeister, bases do Notion) não foram abertos: estrutura vem
das aulas; (2) contrato com mentor não é tratado no material; (3) a estrutura completa de "entrega sem depender do expert"
(palestra de encontro) estava em imagem, só parte chegou ao texto; (4) proporções de capacidade divergem entre fontes (resolvido
pelo padrão do squad, a conferir com dado próprio); (5) critérios da avaliação de call por IA são citados (ex.: nota da
abertura), sem a lista completa.
