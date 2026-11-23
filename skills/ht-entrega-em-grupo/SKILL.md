---
name: ht-entrega-em-grupo
description: 'Squad High Ticket / método FHT. Desenha e roteiriza as entregas um-para-muitos do HT do expert: bootcamp ou dia de implementação (introdução em 5 partes + ciclo dos 4 Es, grade de 9 h, exame ao vivo), plantão de dúvidas, laboratório de feedback em grupo, hot seat, sprint de resultado, dia de mentalidade, debriefing e sala colab, rotina semanal de divulgação com as 4 mensagens, comunidade (ferramenta, regras e animação) e encontros exclusivos. Use quando o estrategista disser "monta um bootcamp para os alunos", "dia de implementação", "como divulgo as entregas da semana", "hot seat", "desafio para reativar alunos", "a comunidade morreu", "encontro presencial dos alunos", "entregar em grupo sem perder qualidade". NÃO usar para desafio de 30 dias de venda ou ativação (ht-desafio-30-dias), entregáveis individuais (ht-entregaveis-1a1), imersão de venda (ht-imersao-*) nem para aulas de LPSG/5+1 da Turbo (estrutura-aulas-lpsg-turbo).'
---

# Entrega em grupo do HT

## 1. Para que serve e o que entrega

Entregar em grupo dá velocidade (mais gente avança ao mesmo tempo), escala sem perder qualidade, formaliza o método em
gravações reaproveitáveis, deixa o aluno autodidata seguir sem esperar o individual e cria o ambiente que nenhum concorrente
copia. Mas só funciona quando resolve um ponto comum a muitos alunos; ideia boa que ajuda poucos continua no individual. Esta
skill escolhe o formato certo para cada necessidade, roteiriza a entrega e monta a rotina que faz o aluno aparecer.

**Entrega**, em `experts/<slug>/ht/06-entrega/grupo/`:
1. `<AAAA-MM-DD>-bootcamp-<tema>.md`: estruturador do evento de implementação (introdução, conteúdos em 4 Es com tempos,
   exercícios, exame, output, NPS) e a grade do dia.
2. `rotina-semanal.md` + `mensagens/`: calendário da semana seguinte e as 4 mensagens (divulgação, falta 1 h, começou, gravação).
3. `formatos/`: roteiro de plantão, laboratório, hot seat, sprint de resultado, dia de mentalidade, debriefing/sala colab.
4. `comunidade.md`: ferramenta, regras do ambiente, calendário de animação e responsáveis.
5. `encontros.md`: formato, datas, programação e ligação com a renovação.
6. `grade-do-trimestre.md`: o que acontece em grupo em cada semana, divulgado com no máximo 1 semana de antecedência no início.

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir o pedido do Diretor.
- Ler: `02-oferta/oferta-vigente.md` (quais entregas em grupo foram vendidas, com que quantidade e condição; a jornada),
  `06-entrega/escala/problemas-e-oportunidades` (planilha que decide os temas, ht-escala-da-entrega), `06-entrega/` (NPS,
  consumo, gravações), `00-plano/cronograma.md` (ciclos de renovação e eventos), `05-eventos/` (para não colidir datas).
- Entradas obrigatórias: número de alunos ativos, a dificuldade comum (com evidência: quantos pediram, onde apareceu) e quem
  conduz. Se faltar, no máximo 3 perguntas:
  1. Quantos alunos ativos e quantos travam no mesmo ponto?
  2. Qual entrega em grupo foi prometida na oferta e com que frequência ou quantidade?
  3. Quem conduz (expert, mentor) e qual o canal fixo de avisos?

## 3. Passo a passo

### Passo 1. Decidir se é caso de grupo
- Referência: a partir de ~10 alunos (não é regra dura). Abaixo disso, resolver no individual.
- A entrega em grupo resolve **ponto comum a muitos**: sai da planilha de Problemas e Oportunidades (todos os mentores
  alimentam). Dois pontos de partida: a necessidade que os alunos trazem ou o tema que o expert sabe que é essencial.
- Escolher o formato pela necessidade:

| Necessidade | Formato | Referência |
|---|---|---|
| Muitos travam na mesma etapa da jornada e precisam sair com algo pronto | Bootcamp / dia de implementação | Passo 2 |
| Dúvidas pontuais e variadas | Plantão de dúvidas | `references/formatos-de-grupo.md` §1 |
| Precisam de correção no que fizeram | Laboratório (feedback ao vivo em grupo) | §2 |
| Alunos em nível parecido trocando soluções | Hot seat | §3 |
| Procrastinação, base parada, falta de prova | Sprint de resultado | §4 |
| O método já existe e é bom, mas o aluno não aplica (framework 3 da planilha) | Dia de implementação associado a um desafio de 14 ou 30 dias, com cronograma e tarefa comprovada | Passo 2 + ht-desafio-30-dias |
| Travas internas (medo, comparação) | Dia de mentalidade | §5 |
| Aluno com resultado replicável ou especialidade | Debriefing / sala colab | §6 |
| Pertencimento e troca contínua | Comunidade + encontros | Passos 5 e 6 |
| Ativação de turma nova ou desafio de vendas de 30 dias | ht-desafio-30-dias | - |

### Passo 2. Bootcamp ou dia de implementação
Estruturador completo e grade em `references/bootcamp-de-implementacao.md`. O roteiro tem sempre 4 momentos: introdução,
conteúdo (4 Es), próximos passos e encerramento com NPS (trilha 19, aula 11).
- Bootcamp sozinho às vezes não basta: no FHT, o mesmo conteúdo gravado é muito menos assistido e aplicado do que o ao vivo, e
  dentro de um desafio quase a turma inteira participa (aula 10). Por isso a maioria das entregas em grupo é ao vivo; gravado
  só como teste ou para tema já dado em outro lugar. Desafio só a partir de 10 a 15 alunos (abaixo disso, acompanhar no
  individual e por WhatsApp).
- **Introdução** (vale também para palestra e treino de mentor): boas-vindas e quebra-gelo; o que é; para quem é; para quem
  não é; por que este bootcamp, contado em 5 partes (contexto, obstáculo, ideia, resultado, razão); output ("você sai com ___
  pronto"). Não assumir que o aluno sabe o que o especialista sabe.
- **Conteúdo no ciclo dos 4 Es**, repetido por tema: Ensino (o que é, por que importa, como fazer) → Exemplo (de preferência
  caso de aluno com resultado) → Exercício (proposta, tempo, links) → Exame (feedback ao vivo em alguns alunos; os outros
  aprendem com a correção). Tempo estimado em cada parte, ajustado a cada edição.
- Grade de referência de um dia: 09:00 a ~18:00, 3 ciclos de 4 Es, almoço, fechamento com próximos passos e NPS.
- Cabeçalho: tema, o que será implementado, pré-requisitos, objeções que quebra, entregáveis do dia, responsável.
- Gravar bruto e subir rápido na área de membros; depois fragmentar em aulas. Um "link de links" por bootcamp com todos os
  materiais, em vez de vários links soltos. Câmera aberta como regra. Durante o dia: execução, nada de ajuste estético.

### Passo 3. Rotina semanal de entregas em grupo
Mensagens em `references/rotina-semanal-e-mensagens.md`.
- **Quarta** define a agenda da semana seguinte; **quinta** divulga no canal fixo (grupo de avisos da comunidade) e nos outros.
- No dia: "falta 1 hora" e "começou"; depois "gravação disponível".
- No início, divulgar com no máximo 1 semana de antecedência (o cronograma muda muito); cronograma de 3 meses só quando estável.
- Toda mensagem diz o que o aluno ganha participando e tem o link.

### Passo 4. Formatos curtos (plantão, laboratório, hot seat, sprint, mentalidade, debriefing)
Roteiros em `references/formatos-de-grupo.md`. Pontos-chave:
- **Plantão**: só com volume (comparecem 5% a 10% dos alunos); mão levantada, câmera aberta, uma dúvida por vez, "minha dúvida é
  X, sou do nicho Y"; separar salas por nível quando há volume (vendeu / não vendeu).
- **Hot seat**: mesas ou salas de 5 a 7; rodadas de 12 min (2 de contexto + 10 de ideias) com cronômetro; nº de rodadas = nº de
  pessoas na mesa; só com 10 a 20 alunos ou mais.
- **Sprint de resultado**: ação-alvo, período com começo, meio e fim, quem é e quem não é, regras, formulário com prazo,
  convite; nome promete "as primeiras X"; etapas de nível em vez de prêmio. Serve de over delivery e de reativação.
- **Dia de mentalidade**: Roda da Vida (11 áreas de 0 a 10, 3 piores, 1 ação em 7 e 30 dias, repetir todo mês), valores e
  declarações, raiz das travas (roteiro completo é lacuna).

### Passo 5. Comunidade (ambiente)
Detalhe em `references/comunidade-e-encontros.md`.
- Ferramenta pelo tamanho (padrão do squad): WhatsApp até ~10 alunos (até os 10 primeiros, grupo VIP com o mentor),
  Telegram até ~150, Circle a partir daí. Vender "comunidade", não o nome da ferramenta.
- Comunidade conecta; área de membros armazena. Comunidade vazia não se promete.
- Animação: lives dentro da comunidade, reconhecimento dos que mais contribuem, desafios mensais, mentores postando treinos e
  tropeços, área de parceria entre alunos com regras, símbolos de pertencimento. Regra contra "cego guiando cego": dúvida de
  método é respondida por mentor ou validada.
- A comunidade morre quando o aluno é largado, os líderes não postam e não há incentivo.

### Passo 6. Encontros exclusivos
- Datas fechadas com antecedência; melhor presencial; a partir de 10 a 15 alunos.
- Programação: palestra de aluno com resultado (prova e ego), hot seat, perguntas e respostas, network, exercícios.
- É o canal natural de renovação: o encontro de fim de ciclo combina entrega, upgrade e renovação (ht-renovacao,
  ht-upgrade-e-gic). Todo aluno recebe, mesmo quando foi bônus.

### Passo 7. Experiência e escala no grupo
- Cada encontro: alguém do time abre no horário, chama pelo nome no chat, reconhece resultado de aluno, fecha com o próximo
  passo e NPS (ht-provas-e-cases).
- Com autorização, as gravações das análises e dos exames de outros alunos viram biblioteca: para o aluno é dos materiais mais
  ricos (aprende com o erro do outro), para o expert é fonte de gargalos do método (live 061).
- Toda entrega em grupo segue o estruturador e fica gravada, para outro mentor repetir (ht-escala-da-entrega).

## 4. Regras inegociáveis do método

1. Grupo só para ponto comum a muitos; o resto no individual.
2. Introdução em 5 partes + 4 Es; output declarado no começo e entregue no fim.
3. Exercício com tempo e exame ao vivo; o aluno implementa, não só assiste.
4. Frequência fixa só em encontro de grupo (padrão do squad); entregável individual é sempre "até N".
5. Divulgar com no máximo 1 semana de antecedência no início; quarta define, quinta divulga; um canal fixo (grupo de avisos)
   como lugar oficial.
6. Gravar bruto, subir rápido, um link de links.
7. Não prometer comunidade ou encontro que ainda não existe; comunidade não é vendida como o item mais valioso.
8. Plantão e hot seat só com volume.
9. Mensagem a aluno só com OK do estrategista (protocolo, regra 2).
- Padrões que se aplicam: entregável individual "até N" e frequência fixa só em encontro de grupo; faixas de 4 níveis, para medir
  o avanço no bootcamp; ferramenta de comunidade pelo tamanho; ciclo de 11 a 13 meses casado a um encontro presencial.

## 5. Quando a decisão é do estrategista

- **Encontro presencial** (cidade, custo, quem paga, se é bônus ou entregável): opções com custo por aluno.
- **Ferramenta paga de comunidade** fora do padrão do squad.
- **Criar entrega em grupo nova não prevista na oferta** (é over delivery: custo de tempo do time).
- **Cronograma fixo de 3 meses** divulgado aos alunos (compromisso público).
- **Uso de gravação de aluno** como material para outros alunos (autorização).

## 6. Critério de pronto e auditoria final

**Pronto quando**:
- [ ] O tema veio da planilha de Problemas e Oportunidades (ou da jornada) com evidência de que é comum.
- [ ] Estruturador com introdução completa (5 partes da história e output) e cada conteúdo em 4 Es com tempo.
- [ ] Exercício com proposta, tempo e links; exame com critério de feedback.
- [ ] Grade do dia com horários, pausas e fechamento com NPS.
- [ ] As 4 mensagens prontas em rascunho, com datas e links.
- [ ] Link de links e plano de gravação e publicação.
- [ ] Formato coerente com o volume (plantão, hot seat e encontro com o mínimo de alunos).
- [ ] Nada prometido que não está na oferta vigente (versão citada).

**Auditoria (erros típicos)**:
1. Bootcamp para dificuldade de 2 alunos.
2. Introdução pulada (assumir que o aluno já sabe por que está ali).
3. Aula expositiva sem exercício nem exame.
4. Cronograma que estoura e corta o exercício (ajustar a cada edição).
5. Cronograma de 3 meses divulgado cedo e mudado depois.
6. Vários links soltos em vez de um central.
7. Gravação subida dias depois.
8. Plantão com 8 alunos na base (ninguém aparece).
9. Comunidade prometida e vazia; dúvida de método respondida por colega sem validação.
10. Encontro sem data fechada (no virtual, o aluno não aparece se não for avisado).
11. Entrega em grupo prometida com frequência que o time não sustenta.

## 7. Saída e handoff

- Grava em `06-entrega/grupo/` (escreve o ht-arquiteto-entrega; ht-cs e ht-estrategista-sucesso leem e propõem).
- Roteiros e mensagens → **ht-revisor-metodo-copy**. Slides e materiais visuais → ht-diretor-arte / ht-designer →
  **ht-revisor-visual**.
- Lembretes automáticos → ht-gestor-automacoes (com OK). Encontro de renovação → ht-gestor-renovacao (ht-renovacao). Tema novo
  e aprendizados → planilha de Problemas e Oportunidades e manual (ht-escala-da-entrega). NPS → ht-provas-e-cases.

## 8. Ferramentas de apoio

`gerador-slides-turbo`, `slides-uipm-turbo`, `anthropic-skills:pptx` (slides do bootcamp), `anthropic-skills:xlsx` (estruturador
e grade), `capcut-edit`, `short-form-video`, `caption-animation` (fragmentar a gravação em aulas), `banner-design` (capas na área
de membros), `humanizer` e `avoid-ai-writing` (mensagens), `automacao-fluxos` e `conectar-whatsapp-oficial` (lembretes, com OK).

## 9. Fontes e lacunas

**Fontes**: trilha 19, aulas 09 a 12 (por que grupo, Problemas e Oportunidades, evento de implementação, framework da
introdução, 4 Es, rotina e white labels de lembretes), RESUMO §3, §4 passos 14 a 20, §5.3, §5.8, §5.9, §5.12, §8; parte-A
(bootcamp implementation day, navegador e plantão, comunidade, desafio de resultado), parte-D bloco 6, parte-F (aula bootcamp
4 Es, comunidade VIP, encontro exclusivo, desafio como entregável, gestão de engajamento), parte-G (plantão de dúvidas),
parte-H (GIC e hot seat), parte-I (hot seat, comunidade engajada, dia de mentalidade, debriefing e sala colab); lives FHT 057,
060 (bootcamp + drive + GPS) e 061 (gravações de análises de outros alunos), transcritas hoje. Revisão de 23/11/2026: trilha 19
aulas 09 a 12 lidas por inteiro (ao vivo x gravado, desafio associado ao DIV, 4 momentos do bootcamp).

**Lacunas**: (1) o mapa mental do bootcamp parte 2 e o estruturador em grupo não foram abertos (campos vêm do RESUMO); (2) a aba
"Níveis de resultado" (nível 1 a 4, grau 1 a 3) existe em branco e nenhuma aula explica o uso; (3) o roteiro completo do dia de
mentalidade era brinde de palestra e não está no material; (4) plantão e laboratório não têm script oficial além das regras
citadas; (5) custo de encontro (100 pessoas por ~R$ 15 mil em espaço com projetor) é número de aula, conferir.
