---
name: ht-onboarding-e-primeira-entrega
description: 'Squad High Ticket / método FHT. Monta tudo o que acontece entre a venda do HT e a primeira entrega do aluno: diagnóstico de prontidão (vender antes de entregar), linha do tempo pós-venda, aprovação ou reprovação da aplicação, áudio e mensagem de aprovação, onboarding individual (até 5 alunos) ou aula inaugural (acima de 5), salas de suporte ao vivo, ligação de ativação e os momentos que tornam a entrada do aluno inesquecível. Use quando o estrategista disser "vendeu, e agora?", "monta o onboarding do aluno", "roteiro da aula inaugural", "mensagem de aprovação", "aprovo ou reprovo essa aplicação?", "o aluno entrou e está perdido", "quero uma entrada de aluno marcante". NÃO usar para roteiro dos entregáveis 1a1 (ht-entregaveis-1a1), desafio de 30 dias (ht-desafio-30-dias), NPS e catálogo (ht-provas-e-cases), nem para pós-venda de LPSG/5+1 da Turbo (cs-lpsg-turbo).'
---

# Onboarding e primeira entrega do HT

## 1. Para que serve e o que entrega

Os primeiros dias depois do sim decidem se o aluno confirma que fez a melhor compra da vida ou começa a pensar em cancelar.
No FHT, o cancelamento de quem entra caiu de 34% para 15% (trilha 19, aula 02; número de aula, conferir antes de usar em venda)
com um conjunto de mudanças de entrega: aprovação e aula inaugural mais rápidas (de cerca de 10 dias para 1 a 2), próximo passo
em toda mensagem, salas de suporte ao vivo e o desafio de ativação. A aula não isola o efeito de cada uma. Esta skill
desenha essa passagem inteira para o HT do expert, já pensando em escala: o que o suporte faz sozinho, o que o mentor faz e o
que só o expert faz.

**Entrega**, em `experts/<slug>/ht/06-entrega/onboarding/`:
1. `prontidao.md`: em que parte da entrega o projeto está (sem venda, parte 1, 2 ou 3) e o que fazer agora.
2. `linha-do-tempo-pos-venda.md`: do pagamento da entrada até o primeiro entregável, com dia, responsável, canal e mensagem.
3. `aprovacao.md`: decisão de selecionar ou não, ficha de aplicação, critérios de sim óbvio, dúvida e reprovação, fluxo e textos.
4. `mensagens/`: roteiro do áudio de aprovação, mensagem de aprovação, boas-vindas do suporte, convite da aula inaugural,
   lembretes, ligação de ativação, salas de suporte (todas em estado **rascunho**).
5. `aula-inaugural.md` (acima de 5 alunos entrando juntos) ou `onboarding-individual.md` (até 5): roteiro com tempos, slides
   necessários, quem fala o quê e o fechamento com o próximo passo.
6. `momentos-marcantes.md`: o mapa de experiência da entrada (o que o aluno vê, ouve e recebe em cada momento).

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir o pedido do Diretor em `00-plano/pedidos/`.
- Ler: `02-oferta/oferta-vigente.md` (entregáveis, duração, bônus, garantia, entrada, regras: o onboarding repete a oferta, não
  inventa), `03-sessao/` (como a venda foi feita e o que foi prometido na call), `05-eventos/` (se a venda veio de evento),
  `06-entrega/` (o que já existe), `07-numeros/` (parcelas e datas de cobrança), `00-plano/cronograma.md` (ciclos de renovação).
- Entradas obrigatórias: canal da venda (1a1 ou evento), número de alunos entrando e data, ferramentas (área de membros,
  comunidade, agenda, canal de suporte), quem é o suporte e quem é o mentor. Se faltar, no máximo 3 perguntas:
  1. Quantos alunos entram agora e por qual canal foram vendidos?
  2. Onde ficam área de membros, comunidade e suporte (ferramenta e quem responde)?
  3. Quem faz a primeira entrega (expert, mentor) e qual é o primeiro entregável da oferta?

## 3. Passo a passo

### Passo 1. Prontidão: o projeto deve estar aqui?
Detalhe em `references/linha-do-tempo-e-aprovacao.md` (seção 1).
- **Sem venda, sem entrega.** Se não houve venda, o próximo passo é vender (ht-roteiro-sessao-1a1). Não construir plataforma,
  área de membros completa, manual nem equipe antes do primeiro sim. O MVP de entrega se constrói enquanto o aluno avança.
- **Parte 1** (tem aluno): receber e entregar no individual. **Parte 2** (cerca de 10 alunos, referência): entrega em grupo
  (ht-entrega-em-grupo). **Parte 3** (entregáveis já executados várias vezes, 10+ alunos): delegar (ht-escala-da-entrega).
- O canal manda no caminho: venda 1a1 vira entrada individual; venda em evento vira entrada em grupo.
- Capacidade (padrão do squad): expert sozinho até ~20 alunos; acima disso, já planejar mentor ou navegador.

### Passo 2. Linha do tempo pós-venda
Modelo dia a dia em `references/linha-do-tempo-e-aprovacao.md` (seção 2).
- Sequência: aplicação paga (sinal pago com a call aberta) → análise → aprovação → áudio + mensagem → acessos e comunidade liberados →
  ligação confirmando que entrou → aula inaugural ou onboarding individual → primeiro entregável solicitado (no padrão FHT:
  Raio-X do aluno e pedido do diagnóstico) → salas de suporte (se entrada em grupo) → abordagem individual do suporte uns dias
  depois → primeira vitória antes do vencimento da 1ª parcela.
- **Alvo: aula inaugural ou onboarding em até 1 a 2 dias** depois da venda (FHT atual: vendeu no domingo, inaugural na terça;
  venda na 1a1, onboarding no dia seguinte). A linha do tempo de primeira turma das lives cita 7 a 15 dias: aceitar só na turma
  piloto e avisando a data na venda. Quanto mais longe, maior o cancelamento.
- Programa de 12 meses, ajustável de 11 a 13 para cair no ciclo de renovação: a data de término sai já no onboarding.
- Nada de prometer prazo que a operação não cumpre ("diagnóstico amanhã").

### Passo 3. Aprovação ou reprovação
Fluxo, ficha e critérios em `references/linha-do-tempo-e-aprovacao.md` (seção 3).
- Primeira pergunta: faz sentido selecionar neste HT? (Sim quando há garantia, oferta exclusiva ou evento 1:N, onde a
  reprovação gera escassez real.) Não é obrigatório.
- O canal muda o como: na venda 1a1, a aptidão costuma ser decidida na própria sessão (o expert já viu o Raio-X e a história);
  na venda 1:N (imersão, live, palco), quem paga a aplicação preenche a ficha e entra na análise depois (trilha 19, aula 03).
- Ficha de aplicação: dados de contato, Instagram, nicho e subnicho, faturamento, se já tem clientes, mais o que filtra o
  avatar do expert. Resposta curta e vazia na ficha é sinal de alerta.
- **Sim óbvio** aprova direto. **Dúvida**: ligar ou validar em dupla (mentor + expert). **Reprovado**: explicar o motivo e
  devolver o valor da aplicação. Existe repescagem.
- Quem dá garantia (condicional, ligada à execução) aprova com mais cuidado: o aluno errado vira pedido de garantia.
- O critério de seleção é comprometimento, não dinheiro (live 057).

### Passo 4. Notificação de aprovação (2 mensagens, nesta ordem)
Roteiros em `references/mensagens-de-entrada.md`.
1. **Áudio personalizado de até 2 min** (referência real do FHT: 1 min 15 s), gravado por quem analisou: contexto do aluno,
   por que foi aprovado, pontos fortes, expectativa ("agora são 12 meses juntos"), tom acolhedor. Cita caso parecido se houver.
2. **Mensagem escrita** logo em seguida, com o próximo passo concreto: data, hora e link da aula inaugural (ou do onboarding
   individual) e o canal de suporte exclusivo. Nesta fase o aluno ainda não tem acesso a nada: a mensagem é o único mapa dele.
- Regra: **nunca só "bem-vindo"**. Toda mensagem termina com o próximo passo.

### Passo 5. Onboarding individual (até 5 alunos) ou aula inaugural (acima de 5)
- **Até 5 alunos novos juntos: call individual de cerca de 1 h**, conduzida pelo suporte (ou pelo expert no começo) seguindo
  o roteiro de `references/mensagens-de-entrada.md` (seção 4): parabéns, apresentação da equipe, acessos (área de membros,
  comunidade, agenda, suporte) conferidos na tela, regras e como pedir entregável, próximo passo (preencher o formulário do
  primeiro entregável e pedir a sessão), confirmação dos canais.
- O onboarding individual explica como o programa funciona e confere acessos; não é o momento de tirar dúvidas de conteúdo
  (essas vão para o primeiro entregável). No FHT quem conduz é o suporte, com um mapa mental de roteiro e um slide do time.
- **Acima de 5: aula inaugural** em grupo. Roteiro com tempos em `references/aula-inaugural.md`. Ela vende o programa de novo:
  o expert abre com história, parabéns e resultados, o sócio ou o expert apresenta a equipe (inclusive suporte e financeiro, para
  a cobrança da parcela não parecer golpe vinda de outro número) e passa a condução ao mentor (primeira transferência de autoridade);
  obstáculos e objeções quebrados de novo; o que esperar e o que não esperar; regras; todos os entregáveis e como solicitar;
  liberação e sincronização dos acessos ao vivo; menção ao desafio de ativação; **só o próximo passo** no fechamento.
- Comunidade liberada **antes** da aula inaugural, para o aluno chegar já dentro.
- Over delivery anunciado na inaugural ("tem mais isso"), nunca prometido na venda sem existir.

### Passo 6. Ativação: a primeira vitória antes da 1ª parcela
- Ativação é a fase em que o aluno precisa de vitórias rápidas e engajamento, principalmente antes de pagar a primeira parcela.
- No FHT, o desafio de ativação é casado com cada turma que entra, entra na oferta como bônus contra a objeção "não tenho
  dinheiro para as primeiras parcelas" e mede sucesso por avanço do aluno nos 30 dias, não por chegar à Roma. A cada edição,
  os alunos de turmas anteriores que travaram são convidados de novo (trilha 19, aulas 04 e 05). Desenho do desafio:
  ht-desafio-30-dias. Usar o desafio como bônus é oferta: só se estiver em `02-oferta/`.
- Venda 1a1 com datas de entrada diferentes: o mesmo roteiro do desafio vira um SNA por aluno, com uma aba por semana liberada
  só depois que a anterior foi cumprida (trilha 19, aula 04).
- Ferramentas, por tamanho de turma: aula inaugural + salas de suporte + desafio de 30 dias (ht-desafio-30-dias) quando há base
  (~10 a 15 alunos); abaixo disso, SNA de 5 semanas no individual (ht-entregaveis) e acompanhamento por WhatsApp.
- **Ligação de ativação**: confirmar que entrou, que acessou e que pediu o primeiro entregável. Quem não pediu em poucos dias
  recebe contato ativo (acompanhamento de duas vias: o aluno pede, e o time vai atrás antes do pedido).
- O primeiro entregável é marcado na própria onboarding, com 2 horários oferecidos (padrão do squad).

### Passo 7. Salas de suporte ao vivo (entrada grande)
- Só quando entra muita gente de uma vez (pós-imersão, pós-evento). Quem entra pouco não precisa.
- Plantões em **3 janelas** de horário com o time de suporte, divulgados no fim da aula inaugural e por mensagem a todos os
  novos (inclusive os do individual). Servem para acesso e ansiedade; **não entregam conteúdo**. Entrar junto na tela do aluno
  se preciso.
- Cronologia de referência do FHT: evento termina domingo, inaugural quarta de manhã, sala quarta à tarde, duas salas na
  quinta, na segunda seguinte o suporte aborda cada aluno individualmente (acessos, dúvidas, se está tudo certo).

### Passo 8. Experiência inesquecível da entrada
Mapa completo em `references/momentos-marcantes.md`. O princípio vem das fontes: a entrega começa no sim, o aluno precisa sentir
que foi escolhido, visto e conduzido. Momentos com base no método: áudio personalizado de aprovação, ligação de boas-vindas,
inaugural que vende de novo e mostra a equipe, kit de boas-vindas quando a oferta prevê, primeira vitória rápida, aluno nunca
sem próximo passo, contato ativo antes do pedido. Cada momento tem dono, prazo e roteiro. Nada de mimo que a operação não
sustenta para todos os alunos.

### Passo 9. Registro e passagem para a entrega
- Card do aluno na base (Base de Alunos, ht-escala-da-entrega): status aplicou → validação dupla → notificar aprovação →
  aprovado/onboarding → aguardando pagamento → concluído (ou reprovado). Cada linha é uma **conta** (individual, dupla, trio).
- Abrir o documento de ações do aluno (núcleo) com as informações gerais e as respostas da ficha (ht-entregaveis-1a1).
- Mensagens automáticas (lembretes da inaugural, boas-vindas) só ligam com OK do estrategista (ht-gestor-automacoes).

## 4. Regras inegociáveis do método

1. Sem venda, sem entrega: quem não vendeu volta para vendas.
2. Próximo passo em toda mensagem e em toda etapa; aluno nunca fica perdido nem sem acesso.
3. Onboarding o quanto antes: alvo 1 a 2 dias após a venda.
4. Até 5 alunos: individual. Acima de 5: aula inaugural. Comunidade liberada antes da inaugural.
5. Na inaugural, o expert abre e passa a condução ao mentor; todos os entregáveis explicados; só o próximo passo no fim.
6. Sala de suporte não entrega conteúdo.
7. Onboarding repete a oferta vigente de `02-oferta/`: nada de entregável, prazo ou bônus que não esteja lá.
8. Prometer na venda o que se entrega; se a entrega será com mentor, isso foi dito na venda (risco ético de vender "com o
   expert" e entregar com outro).
9. Reprovado recebe motivo e devolução; nunca silêncio.
10. Envio a aluno só com OK do estrategista (protocolo, regra 2). Rascunho até lá.
- Padrões que se aplicam: garantia condicional e mensurável, ligada à execução (o onboarding explica as condições); sinal pago com
  a call aberta; programa de 12 meses, ajustável de 11 a 13; capacidade de referência do squad; comunidade pelo tamanho (WhatsApp
  até ~10, Telegram até ~150, Circle depois); 2 horários e sessão em até 2 dias.

## 5. Quando a decisão é do estrategista

- **Selecionar ou não** neste HT (com prós: exclusividade, escassez, proteção da garantia; contras: devolução, atrito).
- **Reprovar um aplicante** em caso de dúvida: o agente monta o resumo (ficha, sinais, recomendação) e o estrategista decide com o expert.
- **Kit de boas-vindas físico** (custo, frete, para quem): opções com custo por aluno.
- **Ferramenta de comunidade** fora do padrão do squad (ex.: já ter Circle pago) e **canal de suporte** (número próprio, WhatsApp
  oficial, horário de atendimento e prazo de resposta declarado).
- Qualquer texto que fale em nome do expert. Formato: decisão numerada, a) recomendada, prós, contras e custo em uma linha.

## 6. Critério de pronto e auditoria final

**Pronto quando**:
- [ ] Prontidão diz a parte da entrega e o motivo (com número de alunos e canal).
- [ ] Linha do tempo tem dia, responsável, canal e texto de cada toque, da entrada paga ao primeiro entregável agendado.
- [ ] Inaugural ou onboarding marcado em até 2 dias da venda (ou exceção justificada e aprovada).
- [ ] Toda mensagem termina com próximo passo concreto (data, link ou ação).
- [ ] Roteiro do áudio de aprovação tem os 5 elementos e cabe em 2 min.
- [ ] Aula inaugural com tempos, quem fala, transferência de autoridade, todos os entregáveis e o próximo passo único.
- [ ] Ativação definida (desafio, SNA ou WhatsApp) e ligação de ativação com responsável.
- [ ] Entregáveis, bônus, prazos e condições batem com `02-oferta/oferta-vigente.md` (versão citada).
- [ ] Tudo em estado rascunho, com handoff de revisão pedido.

**Auditoria (erros típicos)**:
1. Montar plataforma, manual ou equipe antes da primeira venda.
2. Mensagem de boas-vindas sem próximo passo.
3. Mais de 2 dias entre venda e recepção sem motivo (o FHT já teve ~10 dias e cancelava mais).
4. Aula inaugural para 3 alunos (era call individual) ou call individual para 40 (era inaugural).
5. Aluno sem acesso a comunidade ou área de membros depois da inaugural (aluno sem acesso pensa em cancelar).
6. Inaugural que vira aula de conteúdo e esquece entregáveis, regras e próximo passo.
7. Expert conduz tudo e não apresenta o mentor (a transferência de autoridade não acontece).
8. Sala de suporte usada para entregar conteúdo.
9. Prometer prazo que a operação não cumpre.
10. Onboarding citando entregável, bônus ou número que não está na oferta vigente.
11. Aprovar quem a ficha já mostrava fora do avatar, em HT com garantia.
12. Reprovar sem explicar e sem devolver.

## 7. Saída e handoff

- Grava em `06-entrega/onboarding/` (escreve o ht-arquiteto-entrega; o ht-cs executa e grava em `acompanhamento/`). Dados de
  aplicante e aluno na base de `06-entrega/privado/` (do ht-cs) ou em `06-entrega/onboarding/privado/`.
- Mensagens, áudio e roteiro da inaugural → **ht-revisor-metodo-copy**. Slides da inaugural → ht-diretor-arte / ht-designer →
  **ht-revisor-visual**.
- Automações de lembrete e boas-vindas → ht-gestor-automacoes (só liga com OK do estrategista). Datas de término e ciclos →
  ht-controller e ht-gestor-renovacao. Primeiro entregável → ht-entregaveis-1a1. Desafio de ativação → ht-desafio-30-dias.

## 8. Ferramentas de apoio

`gerador-slides-turbo` ou `slides-uipm-turbo` (slides da inaugural), `anthropic-skills:pptx`, `humanizer` e `avoid-ai-writing`
(mensagens), `voice-builder` (voz do expert no áudio), `criacao-guia-gravacao` (guia para o expert gravar o áudio e a abertura),
`conectar-whatsapp-oficial` e `automacao-fluxos` (lembretes, só com OK), `email-marketing-mautic` (e-mails de acesso),
`anthropic-skills:xlsx` (linha do tempo e base de alunos).

## 9. Fontes e lacunas

**Fontes**: trilha 19, aulas 02 (introdução, 34% → 15%), 03 (aprovação x reprovação), 04 (onboarding e ativação, salas de
suporte), 17 (transferência de autoridade), RESUMO §3 a §8 e white labels §5.1 e §5.2; parte-D bloco 6
(diagnosticador-prontidao, decisor-aprovacao, redator-notificacao, planejador-onboarding, roteirista-aula-inaugural,
organizador-salas); parte-G (conduzidor-onboarding-aula-inaugural, 5 passos); parte-H (montar-onboarding-ht-e-aula-inaugural);
parte-I (plano-primeira-venda-e-entrega-inicial, onboarding-e-aula-inaugural-ht); lives FHT 057 e 061 (turma piloto, over
delivery, acompanhamento de duas vias, comprometimento como critério; transcritas hoje); gravação real de diagnóstico (kit de
boas-vindas como bônus de turma, exemplo de sessão).

**Lacunas**: (1) os mapas mentais "Onboard modelo FHT" e "Aula Inaugural modelo FHT" não foram abertos: o roteiro da inaugural
é reconstruído do que as aulas descrevem, e os tempos de cada bloco são proposta do squad (marcados como tal); (2) não há prazo
máximo oficial entre venda e inaugural além do caso FHT (1 a 2 dias) e da linha de primeira turma (7 a 15 dias); (3) o conteúdo
de um kit de boas-vindas não é detalhado no material; (4) contrato e termo de compra são citados ("ajudam"), sem modelo.
