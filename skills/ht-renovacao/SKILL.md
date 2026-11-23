---
name: ht-renovacao
description: 'Squad High Ticket / método FHT. Planeja e conduz a renovação dos alunos de um HT (acelerador de resultados) do começo ao fim: engenharia de renovação desde a criação do programa, ciclos e calendário (11 a 13 meses casados a um encontro), pesquisa 1 para muitos e 1 para 1, controle de renovações, oferta de renovação e de migração, evento presencial de renovação com pitch só para aptos, abordagem de quem faltou, retenção e cancelamento, áudio personalizado e auditoria do programa. Use quando o estrategista disser "planeja a renovação da turma", "monta a oferta de renovação", "pesquisa antes do encontro", "evento de renovação", "aluno quer cancelar", "a renovação caiu", "migrar alunos de 3 meses". Preço da renovação é decisão do estrategista, por projeto. NÃO usar para upgrade/GIC (ht-upgrade-e-gic) nem para lançamento pago LPSG (fora do escopo deste squad).'
---

# Renovação do HT (engenharia de renovação FHT)

## 1. Para que serve e o que entrega

Faz o aluno que está terminando o programa continuar com o expert. No FHT a renovação não é um pitch no fim do ano: começa na
entrega (fase 0), passa por coleta de informação (fase 1), análise e redesenho da oferta (fase 2) e termina na renovação em si,
num encontro presencial, com acompanhamento um a um (fase 3). A renovação não tem custo de aquisição e, somada ano a ano, chega a
igualar o faturamento de alunos novos (referência de live, conferir).

**Entrega** (um ou mais, conforme o pedido), em `<raiz_projetos>/<expert>/ht/06-entrega/renovacao/<ciclo-AAAA-MM>/`:
1. `plano-de-renovacao.md`: calendário do ciclo (D-90 a D+14), lista de aptos, metas, responsáveis.
2. `pesquisa-1-para-muitos.md`: formulário pronto para Typeform/Google Forms (19 perguntas adaptadas) + mensagem de envio (rascunho).
3. `roteiro-1-para-1.md`: abordagem "feedback sincerão" + divisão da lista entre expert e mentores.
4. `controle-de-renovacoes.xlsx` (ou .csv): planilha de controle no modelo do FHT.
5. `mapa-oferta-de-renovacao.md`: avatar que renova, pontos fortes e fracos, oferta atual → oferta de renovação (com as opções de
   preço para o estrategista decidir).
6. `evento-de-renovacao.md`: identificação no crachá, momento do pitch, salinha, papéis, pós-evento.
7. `retencao-e-cancelamento.md` (quando houver pedido de cancelamento).
8. `auditoria-renovacao.md`: checklist do programa pronto para renovar.

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir pedido do Diretor e a Aprovação 1.
- Ler: `02-oferta/` (oferta vigente, duração, garantia, entregáveis), `06-entrega/` (NPS por entregável, consumo, catálogo de
  resultados, planilha de problemas e oportunidades, lista de alunos com data de entrada), `05-eventos/` (data e local do encontro),
  `07-numeros/` (Master Plan: taxa e ticket de renovação planejados), `13-aprendizados/` (renovações anteriores).
- **Pré-requisito do método:** existe AR rodando com alunos passando de ~6 meses de programa. Sem aluno perto do fim do ciclo, a
  skill não roda: o próximo passo é vender (ht-slg, ht-roteiro-sessao-1a1). Quem está no começo da entrega vai para
  ht-onboarding-e-primeira-entrega e ht-entregaveis-1a1.
- Entradas obrigatórias: lista de alunos com data de entrada e de fim; data do encontro (ou necessidade de marcar); oferta atual.
  Se faltar, no máximo 3 perguntas ao Diretor:
  1. Quantos alunos vencem neste ciclo e em que data termina cada turma?
  2. Já existe encontro presencial marcado (data, cidade, capacidade)?
  3. Há NPS por entregável e registro de resultado por aluno? (se não houver, a fase 1 vai precisar compensar com o 1 a 1)

## 3. Passo a passo

### Passo 0. Engenharia de renovação (já na criação do programa)
Três fatores combinados (lives 012, 047, 050):
1. **Entrega = resultado + satisfação.** Quem tem resultado tende a renovar; quem teve resultado médio exige esforço; quem não teve
   procura objeções para justificar a saída. Gratidão tem prazo: o momento é perto do resultado.
2. **Ciclos de renovação** fixos (ver passo 1).
3. **Oferta de renovação diferente da de aquisição**: nasce do que os alunos disseram (passo 4).
Decidir na criação: duração de 12 meses (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`), encontro presencial como entregável (canal de renovação, não opcional), garantia
atrelada à execução e à presença nos encontros (garantia condicional e mensurável, padrão recomendado), NPS por entregável (ht-provas-e-cases). Evitar programa de 2, 3, 4 ou 6 meses.
Evitar entregável de "plano de continuidade" que concorra com a renovação (fonte: desafio SP aula 19).

### Passo 1. Ciclos e calendário
- Concentrar os vencimentos em ciclos fixos (FHT: 3 por ano; exemplo citado fevereiro, junho e novembro, conferir para o expert).
- Duração por data de entrada: 11 a 13 meses (padrão recomendado: ciclo casado a um encontro presencial) para terminar num encontro. 11 aceitável, 10 não.
- Quem ganha meses é avisado como vantagem; a quem perde, só se informa a data de término.
- Encontro presencial no fim de cada ciclo: entrega + renovação (+ upgrade, ver ht-upgrade-e-gic).
- Gerar a tabela "turma → data de entrada → data de fim → encontro de renovação" (modelo em `references/calendario-e-plano.md`).

### Passo 2. Fase 0, durante a entrega (contínua)
- Manter viva a planilha **Problemas e Oportunidades** (9 colunas; dono: ht-arquiteto-entrega em 06-entrega). Todo mentor alimenta.
- Cada item pode virar palestra, desafio, bootcamp novo ou entregável novo da renovação.
- Registrar resultado de aluno no catálogo (ht-provas-e-cases): é a matéria-prima do pitch.

### Passo 3. Fase 1, coleta de informação (D-90 a D-30)
**1 para muitos (formulário), 2 a 3 meses antes** (referência de mundo ideal):
- Usar as 19 perguntas do FHT adaptadas (`references/pesquisa-de-renovacao.md`): presença no encontro, dados, se já tem HT, o que
  quer aprender no encontro, crachá, acessibilidade, título e descrição de apresentação (para quem tem resultado), NPS 0 a 10 e
  motivo, sugestão, entregáveis usados, 3 de mais valor, 3 de menos valor, maior dificuldade.
- O mesmo formulário confirma presença. Presença é levada a sério: renova muito mais quem vai ao encontro.
- Só pedir os dados que forem usados (CPF/CNPJ, crachá e acessibilidade são logística).

**1 para 1 ("feedback sincerão")**:
- Listar 100% dos aptos (programa vencendo, opção renovar ou sair). Dividir a lista igualmente entre expert e mentores.
- Canal: WhatsApp, Telegram ou ligação. Pedido: feedback sincero e "o que você faria diferente". Aproveitar para perguntar como
  está o negócio e o faturamento, e confirmar presença de quem não respondeu o formulário.
- Base grande: "multiplicar os olhos" (mentores que mais atenderam nos últimos 3 meses, por faixa ou avatar, e os alunos que
  circulam nos grupinhos). Declarar que é amostra.
- O que se procura: movimento negativo, cancelamento iminente (ex.: aluno bravo com mentor que faltou), quem está propenso a
  renovar (temperatura), quebra de expectativa entre o vendido e o entregue.
- Registrar tudo na planilha de controle (passo 5). Roteiro em `references/pesquisa-de-renovacao.md`.
- **Rascunho**: a mensagem e o formulário saem como rascunho; o envio aos alunos só com OK do estrategista.

### Passo 4. Fase 2, análise e oferta de renovação (D-30 a D-7)
Monta-se o **mapa da oferta de renovação** (modelo do mapa mental do FHT em `references/oferta-de-renovacao.md`):
1. **Dados gerais**: alunos ativos, elegíveis à renovação, confirmados no evento, elegíveis entre os confirmados (base pequena:
   nome a nome, com a percepção de cada um).
2. **Pontos fortes e fracos** do programa, da pesquisa, do 1 a 1 e da planilha de problemas e oportunidades.
3. **Discussão com os mentores** (reunião de compilado: elogios, dificuldades recorrentes, sugestões dos alunos). No FHT foi uma
   reunião com quem fará o pitch.
4. **Oferta atual → oferta de renovação**: o que foi bom, o que tirar, o que pôr, o que mudar. Critério: o que gera mais resultado
   para o aluno, o que ele pede e o que dá para entregar.
5. Cada objeção ouvida vira resposta dentro da oferta (entregável novo, ajuste de formato, condição). Ex. do FHT: alunos sentiam
   falta do fundador → sessão mensal com ele entrou na oferta; avançados pediam conteúdo mais rápido → entregável novo no mastermind.
   Quando o entregável veio da sugestão de um aluno, o pitch diz isso (o aluno se sente ouvido).
6. Entregável sem valor na pesquisa sai da oferta (caso FHT: o encontro com o expert principal saiu porque não estava entre os de
   mais valor).
7. "Cartas na manga": entregáveis guardados para over delivery ou para reconstruir a oferta no evento.
8. **Condições**: validade só no evento (integridade: quem volta depois paga mais), forma de pagamento (preferir à vista,
   oferecer parcelas). **Preço: decisão do estrategista (seção 5).**
9. Tese do pitch: o aluno não renova o passado, renova o futuro. Vende-se um próximo ano diferente, com casos de colegas e o
   programa novo. Frases-guia citadas: "faltam só dois metros" e "o que te trouxe até aqui não te leva ao próximo nível".
- **Migração** (aluno de produto menor ou de 3 meses para o HT de 12): renegociar parcelas restantes, abrir novo ciclo com valor
  menor ou bônus, Raio-X 1a1, preço de fundador ou cashback; preferir à vista. Valores: decisão do estrategista.
- O texto do pitch de renovação é escrito por ht-diretor-copy / ht-roteirista-palco com esta oferta como entrada (ht-palestras-e-pitch).

### Passo 5. Planilha de controle de renovações
Modelo FHT (aba "ACOMPANHAMENTO RENOVAÇÃO"): Nome · E-mail · Turma · Confirmou presença? · Temperatura · Feedback · O que faria de
diferente? · Está presente? · Status Renovação · Comentários. Bloco 1 (D a G) = presença e feedback; bloco 2 (H a J) = renovação.
- Colocar **todos** os aptos (não só os confirmados) e filtrar por "confirmou".
- **Temperatura** (coluna E) tem lista fechada no próprio modelo: Satisfeito / Neutro / Insatisfeito (é o "estado" que a fase 3
  mostra). **Status Renovação** (coluna I), também lista do modelo: Em aberto / Renovado (pintado de verde) / Não vai renovar.
- Quem está "propenso a renovar" (o termômetro da fase 1) se lê na temperatura + feedback; não inventar outra escala.
- Planilha pronta: `references/controle-de-renovacoes.md` (colunas, validações e uso em tempo real). Gerar o arquivo com
  `anthropic-skills:xlsx` quando pedido.

### Passo 6. Fase 3, o evento de renovação
Roteiro detalhado em `references/evento-de-renovacao.md`. Essencial:
1. Lista "cara-crachá" de 100% dos aptos presentes, com o que cada um disse.
2. **Identificação visual no crachá** (adesivo ou bolinha de cor). Padrão do squad: verde = apto à renovação; amarelo = elegível a
   upgrade (live 047). Serve para qualquer pessoa da equipe puxar conversa no café.
3. **Pitch só para os aptos**, em sala própria; os demais seguem conteúdo ou vão ao coffee. Base pequena: evento só da turma (ex.
   da fase 3: 8 a 10 aptos entre 20 e poucos alunos) → antes do coffee, pedir que os identificados fiquem e fechar a sala; poucos
   aptos dentro de um evento grande (ex. do FHT: ~20 aptos entre ~300 presentes) → não tirar todo mundo da sala, chamar um a um e
   fazer a oferta individual.
4. **Hora do pitch**: evento de 1 dia → à tarde, antes do coffee (por volta de 15h a 16h, referência); evento de 2 dias → no
   primeiro dia, à tarde, antes do coffee. A manhã leva o melhor conteúdo e casos de alunos improváveis. Não deixar para tarde
   demais: precisa sobrar tempo para o 1 a 1.
5. **Salinha de renovação em tempo real**: equipe com a planilha aberta (de preferência numa tela maior), marcando quem já foi
   abordado, por quem, e o status. O pitch é o início; a conversão acontece no 1 a 1 até o fim do evento e depois.
6. **Abordagem individual de quem não decidiu**: navegador ou alguém da equipe chama ("o mentor quer conversar com você"). Ouvir,
   resolver o que for simples (ex.: consultoria com o financeiro), jogar limpo: se não faz sentido para o aluno renovar, dizer isso.
7. **Se a renovação despencar** no evento: assumir a fraqueza, perguntar aos aptos o que faltou, acrescentar entregáveis (cartas na
   manga) e fechar ali. Caso FHT: renovação muito baixa no primeiro pitch foi recuperada para ~70% (intro da trilha 20) / "10% para
   73%" (live 012). Números de legenda, conferir antes de usar em material.
8. Separar "toalha molhada" (reclamação de baixo peso, não faz cancelar) de necessidade real (faz).

### Passo 7. Pós-evento (D+1 a D+14)
- Cruzar a lista: confirmou e foi, não confirmou, confirmou e faltou, ficou pendente.
- Na semana seguinte, abordar um a um quem não esteve ou não decidiu, com pitch individual (call). Referência de live: presentes
  renovam 60% a 80% (até 90%), ausentes ~20% (conferir). Por isso o esforço de confirmação de presença.
- Áudio personalizado (renovação/reativação de afastado): roteiro com a história do aluno no programa, gravado pelo expert; caso
  citado com duas rodadas de 8 e 10 alunas e ~90% de renovação (conferir). Modelo em `references/retencao-e-cancelamento.md`.
  Envio só com OK do estrategista.
- Debriefing em `06-entrega/renovacao/<ciclo>/debriefing.md` (o Diretor leva a `13-aprendizados/renovacao-<ciclo>.md`): taxa por grupo (presentes, ausentes, por temperatura), objeções que
  apareceram, o que entra na próxima oferta.

### Passo 8. Retenção e cancelamento (a qualquer momento do ciclo)
Protocolo em `references/retencao-e-cancelamento.md`: call de entrevista antes de cancelar, entender o motivo, renegociar estratégia
ou financeiro (parcela atrasada: parte agora, resto diluído), reembolso com segunda chance e plano de pilotagem, e categoria abaixo
para cancelados só a partir do 1º ou 2º ano. Valores e condições de qualquer renegociação: decisão do estrategista.

## 4. Regras inegociáveis do método

1. A renovação começa na entrega. Sem NPS, sem registro de resultado e sem 1 a 1, não há oferta de renovação, há palpite.
2. 100% dos aptos são ouvidos (ou amostra declarada, com base grande). Formulário sozinho não basta: resposta fria.
3. A oferta de renovação é outra oferta: nasce do que os alunos disseram, não da oferta de aquisição repetida.
4. Pitch de renovação só para aptos e separado do pitch de upgrade.
5. Renovação presencial rende mais que a online (WhatsApp, financeiro). Toda turma termina num encontro.
6. Programa de 12 meses ajustável de 11 a 13 (padrão recomendado); nada de HT de 6 meses.
7. Condição da renovação vale no evento; depois, condição pior (integridade, sem exceção escondida).
8. Não ser vendedor a qualquer custo: se a renovação não faz sentido para o aluno, dizer.
9. Nada é enviado a aluno sem OK do estrategista: formulário, mensagem, áudio, oferta.
10. Dado do aluno (CPF, faturamento, feedback) fica na pasta do projeto; nunca em material público.

## 5. Quando a decisão é do estrategista

**Preço da renovação (definido por projeto: menor, igual ou reajuste; é do estrategista).** Apresentar sempre as três opções, com números do projeto (ticket atual, taxa de
renovação planejada no Master Plan, margem):
- a) **Menor que a entrada** (fontes: ~40% menor em exemplo da live 047/parte I; levemente menor, 20 mil → 17 mil, parte H; R$ 5 mil
  a menos num AR de 30 mil, live 047). Prós: facilita o sim de quem está em cima do muro, vende "vantagem de quem já é aluno".
  Contras: reduz receita por aluno; ancora o próximo ano mais baixo.
- b) **Igual à entrada**, com mais parcelas ou entregáveis novos. Prós: preserva o ticket; o valor percebido vem da oferta nova.
  Contras: exige oferta claramente melhor; risco maior com aluno de resultado médio.
- c) **Reajuste** (fonte: manter o preço por 2 anos e reajustar no 3º, desafio jan/26). Prós: acompanha o valor entregue e o
  posicionamento. Contras: só funciona com resultado forte e NPS alto; pede pesquisa muito favorável.
A ordem acima é só de exposição. Ao levar ao estrategista: se o dado do projeto sustentar uma recomendação, ela passa a ser a opção a)
marcada "(recomendo)" com o motivo em uma linha (regra do protocolo); se não sustentar, apresentar as três sem recomendação e
dizer qual dado falta.

Também são do estrategista: condições de migração, desconto à vista, valor da categoria abaixo, reembolso, mudança de duração do
programa, data e custo do encontro (gastar), envio de qualquer mensagem a aluno, texto público novo.

## 6. Critério de pronto e auditoria final

**Critério de pronto** (o que o pedido exigir):
- [ ] Lista de 100% dos aptos com data de fim e turma; aptos sem encontro têm plano de 1 a 1.
- [ ] Calendário com fase 1 começando 60 a 90 dias antes do encontro (ou o motivo de ser menos).
- [ ] Formulário com as perguntas de NPS, motivo, 3+/3- entregáveis, maior dificuldade e presença.
- [ ] Planilha de controle com as 10 colunas, as duas listas do modelo (temperatura e status) e todos os aptos.
- [ ] Mapa da oferta com pontos fortes/fracos rastreáveis a fonte (pesquisa, 1 a 1, mentores, planilha P&O).
- [ ] Cada objeção relevante tem resposta na oferta ou no pitch.
- [ ] Preço com as 3 opções e a pergunta ao estrategista registrada (nenhum preço decidido pela skill).
- [ ] Evento com identificação de aptos, horário do pitch, salinha, papéis e pós-evento.
- [ ] Números de aula marcados "referência/conferir"; nenhum resultado de aluno inventado.

**Auditoria final** (erros típicos; detalhe em `references/auditoria-renovacao.md`):
1. Achar que sabe o que o aluno valoriza sem pesquisa (caso do entregável que ninguém valorizava).
2. Confiar só no formulário; não fazer o 1 a 1.
3. Ignorar o sinal dos mentores e dos alunos ("toalha molhada" tratada como irrelevante quando era necessidade real).
4. Pitch para a sala inteira, incluindo quem não é apto.
5. Pitch tarde demais, sem tempo de 1 a 1.
6. Contar só com o pitch; sem salinha nem planilha em tempo real.
7. Esquecer quem não foi ao evento.
8. Oferta de renovação igual à de aquisição; vender o passado em vez do futuro.
9. Promessa de entrega que não se sustentou (ex.: "100% com os fundadores") repetida na renovação.
10. Área de membros e jornada desatualizadas em relação à entrega real.
11. Duração do programa que não cai em nenhum encontro.
12. Preço de renovação decidido pelo agente.

## 7. Saída e handoff

- Grava em `06-entrega/renovacao/<ciclo>/` (dono: ht-gestor-renovacao). Preço e condições aprovados pelo estrategista vão para
  `02-oferta/renovacao-<ciclo>.md` pelo ht-arquiteto-oferta (esta skill não escreve em 02-oferta).
- Textos (formulário, mensagens, roteiro do 1 a 1, pitch, áudio) → **ht-revisor-metodo-copy**. Slides do pitch → ht-designer e
  **ht-revisor-visual**.
- Logística do encontro → ht-produtor-eventos (05-eventos). Automação de lembretes e formulário → ht-gestor-automacoes (11-automacoes,
  só liga com OK do estrategista). Números da renovação no Master Plan e no painel → ht-controller (ht-central-e-kpis).
- Upgrade no mesmo evento → ht-upgrade-e-gic.
- Bloco de entrega no formato do protocolo, com nível de evidência e as decisões pendentes (D-numeradas pelo Diretor).

## 8. Ferramentas de apoio

`anthropic-skills:xlsx` (planilha de controle e calendário), `anthropic-skills:docx` (roteiro impresso da salinha),
`gerador-slides-turbo` / `slides-uipm-turbo` (deck do pitch, com direção do ht-diretor-arte), `email-marketing-mautic` e
`automacao-fluxos` (lembretes de presença, só com OK), `humanizer` e `avoid-ai-writing` (mensagens e áudio), `testimonial-video`
(cases de alunos para o pitch, com autorização).

## 9. Fontes e lacunas

**Fontes**: trilha 20 Bootcamp de Renovação (02-introducao, 03-fase-01, 04-fase-02, 05-fase-03, 06-encerramento, lidas por inteiro
na revisão; Notion da trilha 20 em `_materiais/notion-5a20.txt` com as 19 perguntas; RESUMO.md); planilha `_materiais/planilhas/20-renovacao__1UcuiCdP.xlsx`; lives FHT 012, 022, 040, 047, 050, 052 (via
parte-H bloco 7 e parte-I seção 6); desafios E (renovação e migração, preço 2 anos), F (encontro exclusivo, áudio personalizado);
CATALOGO-SKILLS-FHT.md seção 7 e conflito 16; padrões recomendados do squad (garantia, ciclo de 11 a 13 meses, preço
da renovação por projeto).

**Lacunas**: (1) o mapa mental "Criador de oferta de renovação" (MindMeister) não foi lido; a estrutura usada é a descrita em voz na
fase 2 e na fase 3 (avatar, problemas e oportunidades, pontos fortes e fracos, oferta atual, oferta de renovação); (2) a planilha de
controle não traz fórmulas nem regra de quando um aluno muda de temperatura (só a lista Satisfeito/Neutro/Insatisfeito); (3) não há roteiro literal do
pitch de renovação, só princípios; (4) taxas de renovação (80%, 90%, 70%, 20% dos ausentes) e o caso 10% → 73% vêm de legenda e de
relato oral: referência, conferir; (5) não há método escrito de cobrança/inadimplência além de "renegociar"; (6) custos de
encontro (~R$ 15 mil para 100 pessoas num hub) são de um relato, conferir com orçamento real.
