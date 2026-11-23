---
name: ht-imersao-de-resultados
description: 'Monta a Imersão de Resultados (alunos palestram erros e acertos, formato Toque de Midas) e o encontro de alunos aberto a convidados, com venda do HT e renovação. Use com "evento com os alunos palestrando", "IMR do expert", "prepara o aluno para palestrar". NÃO usar para preço da renovação (ht-renovacao).'
---

# Imersão de Resultados (IMR) e encontro de alunos com convidados

## 1. Para que serve e o que entrega

Na IMR o conteúdo do evento são os próprios alunos contando como chegaram ao resultado e qual feedback do programa mudou o jogo.
Isso gera a prova social mais forte que existe, mostra o poder do feedback (que é o que o HT vende), atualiza o método e
intensifica a comunidade. A variante "encontro de alunos aberto a convidados" usa os alunos como captação de custo quase
zero e pode reunir, no mesmo evento, entrega, renovação e venda a público novo.

**Entrega** (em `experts/<slug>/ht/05-eventos/<evento>/`):
1. `imr-planejamento.md`: objetivo (venda nova, renovação, ou as duas), público (alunos, convidados, público frio), formato e
   duração, metas, entrada (gratuita, credencial ou paga), local e custo.
2. `imr-grade.md`: grade com palestras de alunos, palestras do expert, pré-pitch, pitch, break, hot seat, P&R, celebração.
3. `palestrantes/`: um briefing por aluno (template em references) com status (mapa mental, slides, ensaio, autorização).
4. `imr-apresentacoes.md`: a fala do expert antes e depois de cada caso (3 As) e a objeção que cada caso quebra.
5. `imr-convidados.md` (se houver): régua de convite, confirmação, página, kit, abordagem no break.
6. Debrief para `13-aprendizados/`.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`: `02-oferta/` (oferta do HT para convidados), `06-entrega/` e o catálogo de resultados
   (ht-provas-e-cases), gravações de feedback e NPS, `05-eventos/` (decisão do ht-decisao-de-evento), plano de renovação (se o
   evento tiver renovação; ht-renovacao), `13-aprendizados/`.
3. Entradas obrigatórias: lista de alunos com resultado e evidência; gravações das interações mentor-aluno; objetivo do evento;
   número de alunos ativos.
4. Perguntar no máximo 3 coisas, se faltar: (a) o evento é para venda nova, renovação ou ambos; (b) quais alunos já autorizaram
   expor nome e números; (c) haverá convidados e quantos por aluno.

## 3. Passo a passo

### Passo 1. Prontidão
- Existem pelo menos 3 a 5 casos com resultado do mesmo tipo que o programa promete, com evidência e, de preferência, a gravação
  do feedback? Sem isso há dois caminhos: fazer IMA ou IMI (ht-imersao-aprendizado / ht-imersao-implementacao), ou fazer a versão
  estilo "o expert conta os próprios erros", em que o próprio expert e o time palestram os erros e acertos da implementação do método (há casos de referência em que
  os erros e acertos eram do próprio expert e só o time ficava no palco). Nessa versão valem as mesmas regras de prova e de 3 As; o que muda é quem conta o caso.
- Encontro presencial de alunos só depois de 10 a 15 alunos (antes disso, não prometer).
- Gravar SEMPRE as interações mentor-aluno daqui em diante (não dá para gravar depois).

### Passo 2. Definir o desenho
Escolher entre:
- **IMR aberta** (venda nova): alunos palestram para público que ainda não comprou; pitch do HT no dia 2; downsell no fim.
- **Encontro de alunos com convidados**: alunos trazem convidados quentes; venda do HT ao convidado; aula exclusiva para
  aluno.
- **Renovação + venda emendada**: dia 1 só alunos (entrega e renovação), a partir do dia 2 imersão de venda com os renovados
  como prova viva (crachá diferente).
Duração, local e custo pelo porte: hub/auditório de cerca de 100 lugares, data show, sem LED, quando o evento é de alunos.
Detalhe: `references/encontro-de-alunos-com-convidados.md`.

### Passo 3. Selecionar os alunos palestrantes
1. Do catálogo de resultados: resultado com evidência, obtido **com o programa** (não com o curso), perfil parecido com quem
   estará na sala, variedade de pontos de partida (do zero, transição, já tinha audiência) e de objeções quebradas.
2. Mapear cada caso a uma objeção da árvore e a um entregável do HT (o que aquele caso prova).
3. Coletar autorização registrada de exposição.

### Passo 4. Briefing, entrevista e preparo de cada aluno
Entrevistar; levantar o trecho da gravação do feedback; aluno faz o mapa mental na estrutura Antes → Feedback → O que fiz →
Depois → Erros e acertos → Lição; feedback do mentor; slides; feedback; ensaio cronometrado com o time; palco. Ajustes finos:
vocabulário do público, obstáculos do começo da jornada, objeção escondida na história, nada de "o curso me salvou".
Detalhe e template: `references/briefing-palestrante-aluno.md`.

### Passo 5. Grade da IMR
Ordem de referência (adaptar à duração e usar a grade do ht-imersao-presencial para horários):
1. Talk de entrada do expert (procedência, combinados, repasse de autoridade aos mentores e aos alunos que vão palestrar).
2. Blocos de palestras de alunos agrupados por tema (ex.: oferta, aquisição, entrega), cada caso com os 3 As do expert e
   perguntas e respostas curtas.
3. Hot seat ou dinâmica entre blocos.
4. Pré-pitch (pode ser o Tipo 2, case de aluno, se houver um caso que atravessa todos os entregáveis) e pitch do HT no dia 2
   (ht-palestras-e-pitch).
5. Dia 3 (se houver): re-pitch, palestra de decisões com casos de alunos, celebração dos que entraram, downsell, reconhecimento.
6. Reconhecimento público dos resultados (ex.: placa ou certificado de marco atingido, foto oficial), que vira conteúdo e ego
   saudável para quem palestrou.
Na versão encontro de alunos: aula exclusiva para aluno, kit diferenciado, palestras na mesma sala com lugares separados.

### Passo 6. Convidados (quando houver)
Anúncio aos alunos com aviso de que haverá venda (75 dias antes no caso de referência), aquecimento com cara de evento HT,
formulário de confirmação com dados do convidado (30 dias antes), boas-vindas e página própria do convidado, confirmação ativa
(10 dias), almoço com convidados, abordagem no break pelos mentores e alunos. Convite no tom "venha, viva o evento e, se fizer
sentido, decide no final". Detalhe: `references/encontro-de-alunos-com-convidados.md`.

### Passo 7. Venda e renovação no evento
Pitch e break pelo ht-palestras-e-pitch; renovação pelo ht-renovacao (oferta e preço definidos por projeto). Quem não
renovou no dia 1 continua decidindo nos dias seguintes. Recuperação de convidados e indicações na semana seguinte.
Lições de um caso de referência de renovação, para o pitch de renovação emendado:
1. Ler o avatar dos renovantes antes e conversar com alguns alunos antes do evento; a renovação nunca vai no piloto automático.
2. Apresentar a renovação dizendo o que continua e o que é novo.
3. Pitch "desapegado" não serve a todo avatar: no caso, alunos de nível alto se sentiram ignorados e a renovação ficou entre 10% e
   15% até a tarde (referência, conferir), até o expert assumir o erro no palco e perguntar o que eles queriam para renovar.
4. Na manhã seguinte ao pitch de renovação, reunião interna de objeções (como a das 7h às 9h do dia 3 da imersão).
5. Se a oferta precisar mudar no evento, o agente assume a recomendada, leva as objeções e lista em "Assumi".
Fusão no mesmo evento: um caso de referência separou salas por nível, cada uma com o pitch do programa adequado; é
opção a propor quando a sala mistura alunos de níveis diferentes.

### Passo 8. Debrief
Conversão de convidados, de público novo e de renovação; quais casos geraram mais conversa no break; o que ajustar nos briefings.
Os casos apresentados entram atualizados no catálogo de resultados.

## 4. Regras inegociáveis do método

1. Cada palestra de aluno segue o Toque de Midas: antes, feedback do mentor (com evidência), depois. Não vale só "cheguei em X".
2. Resultado do programa, não do curso; resultado do mesmo tipo que o programa promete.
3. Mapa mental aprovado e ensaio antes de qualquer aluno subir ao palco.
4. Conteúdo inédito a cada edição; o expert apresenta cada caso com os 3 As.
5. Aluno avisado de que haverá venda; convidado tratado com integridade (sem "pegadinha").
6. Encontro presencial prometido só com 10 a 15 alunos; todos os alunos ativos recebem o encontro se ele é entregável.
7. Nunca expor aluno sem autorização registrada; nada de número sem evidência.
8. Preço do HT de 02-oferta; preço da renovação definido por projeto.
9. Proibido misturar a estrutura desta imersão com a de evento pago de ingresso.

## 5. O que a skill assume e o que pede OK simples

- **Objetivo do evento** (venda nova, renovação, ambos) e **entrada do convidado e do público novo** (gratuito, VIP, pago; a skill propõe pelo padrão do evento e lista em "Assumi").
- **Oferta e preço da renovação** (definida por projeto: menor, igual, reajuste; com prós e contras do ht-renovacao).
- **Quantos convidados por aluno** e critérios de convite.
- **Quem palestra** (exposição de alunos) e reconhecimentos públicos.
- **Emendar com imersão aberta** (mais caixa e prova viva x mais complexidade e custo).
- **IMR sem casos suficientes**: (a) IMA/IMI (recomendado no primeiro evento; menos risco de prova fraca); (b) estilo Mundo
  Paralelo com o expert e o time contando os próprios erros e acertos (mais diferente, exige casos próprios com evidência).
- **Salas separadas por nível** com pitches diferentes (mais conversão por nível x mais equipe e logística).

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Objetivo, desenho, metas e entrada definidos (decisões registradas em "Assumi").
- [ ] Pelo menos 3 a 5 casos selecionados, cada um ligado a uma objeção e a um entregável, com autorização.
- [ ] Briefing enviado e status de cada aluno (mapa mental, slides, ensaio) verde antes do evento.
- [ ] Grade com palestras de alunos, falas de 3 As do expert, pré-pitch, pitch, break e reconhecimentos.
- [ ] Régua de convidados (se houver) com prazos e página própria.
- [ ] Integração com ht-palestras-e-pitch (pitch), ht-renovacao (renovação) e ht-captacao-e-presenca (confirmação).

**Auditoria (erros típicos):**
1. Aluno contando história sem o feedback do mentor no meio. 2. Resultado vindo do curso. 3. Aluno sem ensaio, improvisando.
4. Jargão de outro programa ou obstáculos de quem já está no topo. 5. Casos todos iguais (mesmo ponto de partida), sem quebrar
objeções diferentes. 6. Aluno surpreendido com a venda. 7. Convidado sem confirmação e sem página própria. 8. Promessa de
encontro com poucos alunos. 9. Evento caro demais para o porte (LED e estrutura de evento grande num encontro de 100).
10. Exposição sem autorização. 11. Renovação com preço decidido por agente.
12. Renovação emendada sem conversa prévia com os alunos e sem "o que continua e o que é novo".

## 7. Saída e handoff

- Grava em `05-eventos/<evento>/` (dono: ht-produtor-eventos); briefings e falas com o ht-roteirista-palco.
- Casos e evidências → ht-cs / ht-provas-e-cases (catálogo). Renovação → ht-gestor-renovacao. Convidados e mensagens →
  ht-gestor-automacoes e ht-copy-anuncios-e-mensagens. Números → ht-controller.
- Revisão: textos → ht-revisor-metodo-copy; slides e vídeos → ht-revisor-visual.
- Debrief em `13-aprendizados/`.

## 8. Ferramentas de apoio (por nome)

- Vídeo de Toque de Midas e depoimentos: `testimonial-video`, `hyperframes`, `remotion`, `caption-animation`, `lower-thirds`.
- Encontrar o trecho do feedback na gravação: `watch`, `transcrever-youtube`.
- Slides dos alunos: `gerador-slides`, `slides-uipm`, `anthropic-skills:pptx`.
- Página do convidado: `designer-senior`, `publicar-pagina-cloudflare`.
- Mensagens aos alunos e convidados: `conectar-whatsapp-oficial`, `automacao-fluxos` (envio só com OK da pessoa).
- Texto: `avoid-ai-writing`, `humanizer`.

## 9. Lacunas (não inventar)

(1) A operação de uma IMR de grande porte (milhares de pessoas) é citada sem passo a passo. (2) A grade da IMR não existe como planilha: a ordem do passo 5 é composição da grade de 3 dias com as regras da IMR. (3) Os números dos casos (75%, ~100%, 50%) são de amostras pequenas e relatos ao vivo: referência a conferir. (4) Não há roteiro oficial de reconhecimento (placa, foto) além da menção no pitch. (5) Palestras sobre eventos de baixo custo não têm texto de apoio.
