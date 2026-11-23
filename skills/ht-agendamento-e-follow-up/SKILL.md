---
name: ht-agendamento-e-follow-up
description: 'Cuida do caminho entre o "sim" do lead e a decisão: aplicação e seleção, agendamento com 2 horários, lembretes com confirmação afirmativa, no-show, follow-up e repescagem em 1 mês. Use para "muito no-show", "como confirmo a sessão", "o lead sumiu depois da call", "reativa os leads antigos". Gera RASCUNHO. NÃO usar para abordagem até o sim (ht-slg) nem condução da call (ht-roteiro-sessao-1a1).'
---

# Agendamento, lembretes, no-show e follow-up da sessão 1a1

## 1. Para que serve e o que entrega

No canal 1a1 há quatro etapas: geração de leads, **agendamento**, conversão (a sessão) e **follow-up**. Esta skill cobre a 2ª e
a 4ª, mais a aplicação quando o projeto a usa. É aqui que se perde lead qualificado sem perceber: notificação que ninguém abre,
sessão marcada longe demais, confirmação que convida a cancelar, falta sem nova tentativa, "depois eu te respondo" sem data.

**Entrega** (rascunhos para o estrategista):
1. `03-sessao/agendamento/AAAA-MM-DD-cadencia.md`: fluxo do sim à sessão (quem faz o quê, em quanto tempo), mensagens de cada
   toque em [campos], roteiro de ligação, regras de reagendamento e de no-show.
2. `03-sessao/follow-up/AAAA-MM-DD-follow-up.md`: roteiro do fechamento do retorno na própria sessão, cadência de follow-up,
   mensagens, encerramento e repescagem.
3. `03-sessao/aplicacao/AAAA-MM-DD-aplicacao.md` (se houver aplicação): ficha, critérios de aprovação e reprovação, mensagens
   de aprovado e reprovado, regra de devolução.
4. `11-automacoes/lembretes-sessao/AAAA-MM-DD-spec.md`: especificação da automação de lembretes (gatilho, horário, canal,
   texto), marcada **desligada** até o OK do estrategista.
5. Colunas e métricas de controle (para a Central 1x1) e o diagnóstico do gargalo, quando houver dados.
6. Bloco de entrega do protocolo e decisões para o estrategista.

Pasta com dono: a spec de automação em `11-automacoes/` é gravada pelo gestor de automações, a pedido via Diretor; quem roda
esta skill (Closer ou SDR) escreve só em `03-sessao/`.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`:
   - `03-sessao/` (nome em `nome-da-sessao.md`, dono ht-closer; ausente = `[A CONFIRMAR COM ht-closer]`): nome da sessão, duração (alvo 1h15, teto 1h30), roteiro, árvore de objeções, quem conduz.
   - `02-oferta/oferta-vigente.md`: entrada, sinal, parcelado, à vista, **piso de negociação** (se existir) e se há aplicação e
     seu valor. Nada de preço fora daqui.
   - `04-demanda/slg/` e `11-automacoes/pagina-sessao/`: de onde chegam os leads e com quais dados (período preferido, dor).
   - Central 1x1 (`07-numeros/` ou `04-demanda/slg/central-1x1-slg.csv`): agendados, comparecimentos, follow-ups abertos.
3. Entradas obrigatórias: quem agenda e quem conduz (expert, SDR, secretária), canal (WhatsApp, Instagram), ferramenta de
   agenda e de chamada (Meet, Zoom), dias e horários disponíveis do condutor. Se faltar, até 3 perguntas ao estrategista, por exemplo:
   - "Quem vai agendar e com que número de WhatsApp (tem foto de pessoa real)?"
   - "Quais dias e horários o expert tem para sessões nas próximas 2 semanas?"
   - "Vai haver aplicação antes da sessão? Gratuita ou paga?"

## 3. Passo a passo

**Passo 1. Desenhar o fluxo e os papéis.** Do "sim" (arremate do SLG, inscrição na página, aplicação paga, levantada de mão na
aula) até a decisão: quem contata, em quanto tempo, em que canal; quem conduz; quem faz o follow-up. Funil em micro-etapas
para medir: notificação (recebe, abre, lê, responde) → agendamento (convencimento, formalização) → comparecimento (lembrete,
realização) → venda → follow-up. Modelo em `references/planilha-de-controle.md`.

**Passo 2. Aplicação e seleção, se o projeto usar** (`references/aplicacao-e-selecao.md`). Ficha curta e com propósito;
aplicação paga como filtro reembolsável; ao pagar, agendamento imediato; critérios de sim, dúvida e não; devolução e motivo a
quem é reprovado. Só chamar de "aplicação" se a seleção for real. Valor: o agente assume o padrão (seção 5).

**Passo 3. Primeiro contato em minutos** (`references/agendamento-e-lembretes.md`, seção 1). Chamar o lead logo que ele disse
sim ou se inscreveu (referência de palestra: ligação em até 30 minutos). Número com foto de pessoa real, mensagem curta, sem
link cru nem texto de varejo. Primeira mensagem para gerar abertura e resposta, não para explicar tudo.

**Passo 4. Agendar** (padrão do squad). Perguntar o período (manhã, tarde, noite) se ainda não veio do formulário e
oferecer **2 horários**, com a sessão **em até 2 dias**. Agendar mais longe aumenta a falta. O agendamento também é uma venda:
vender o valor da sessão (o diagnóstico), não a pessoa que vai atender; se não souber quem conduz, falar "equipe"/"especialista".

**Passo 5. Formalizar.** Convite de calendário com data, hora e link; pedir compromisso honesto (o horário fica reservado);
alinhar as condições: lugar tranquilo, câmera aberta, tempo de 1h15, e o decisor junto quando há outro decisor (sócio,
cônjuge, quem paga). Dois canais (WhatsApp + calendário/e-mail).

**Passo 6. Lembretes** (`references/agendamento-e-lembretes.md`, seção 3). Cadência padrão de 5 toques: véspera, manhã do dia
com o link, 5 minutos antes, "já estou na sala" na hora, ligação se não entrou. Confirmação **afirmativa** ("está tudo certo
para hoje às [hora], o horário está reservado para você"), nunca "confirma?" ou "tudo certo?". Lembrar demais irrita: os toques
são esses, sem mais.

**Passo 7. No-show e reagendamento** (`references/no-show-e-reagendamento.md`). Durante: mensagem curta "estou te aguardando no
link" e ligação. Depois: mensagem leve sem culpa, com um novo horário próximo. 2 a 3 tentativas em 2 a 3 dias; faltou de novo:
avisar com leveza e passar à repescagem. Ao reagendar, a sessão precisa elevar a dor de novo. Limitar reagendamentos.

**Passo 8. Follow-up de quem não fechou** (`references/follow-up-e-repescagem.md`). O objetivo é fechar na sessão (sinal de R$ 500 a
R$ 1.000, até 10%, pago com a call aberta; condução é do `ht-roteiro-sessao-1a1`). Quem não fechou sai da sessão com **dia e hora de retorno** marcados
por ele. Retorno no dia seguinte, de preferência por ligação; usar a gravação ou o PDF do Raio-X; negociação com piso
(`02-oferta`); quebra de objeção em 3 passos (empatia, argumento racional, prova; detalhe em `ht-objecoes`). Insistir por cerca
de 1 semana; encerrar com mensagem gentil e porta aberta; repescar em 1 mês com motivo novo.

**Passo 9. Reativação de leads antigos** (seção 4 da mesma referência): aula semanal, contato consultivo, proposta de refazer o
diagnóstico, convite para evento. Oferta menor (produto de entrada) só depois do "não" definitivo ao HT e nunca junto com ele.

**Passo 10. Especificar a automação** dos lembretes que podem ser automáticos (véspera, manhã) para o `ht-gestor-automacoes`,
**desligada** até o OK do estrategista. No começo, o método recomenda fazer "no dedo" e automatizar só depois de validar o processo.

**Passo 11. Medir e diagnosticar** (`references/planilha-de-controle.md`). Comparecimento esperado 70% a 80% (no-show até 20%);
abaixo disso, olhar a cadência antes de culpar o lead. Processo novo de agendamento só é avaliado com pelo menos ~12
agendamentos (conferir).

**Passo 12. Auditoria final** (seção 6) e handoff.

## 4. Regras inegociáveis do método

- Velocidade: lead quente esfria em horas; contato em minutos, sessão em até 2 dias (padrão do método).
- 2 horários oferecidos, não "qual horário fica bom pra você?" aberto (padrão do método).
- Confirmação afirmativa, nunca pergunta que abre espaço para cancelar.
- Vender a sessão, não o atendente; nunca prometer o expert e entregar outra pessoa.
- Mensagem curta, humana, de número com foto de pessoa; nada de texto de varejo, emoji em excesso ou link cru na abertura.
- Sem chantagem emocional e sem culpa no no-show e no follow-up (nada de "você não quer mudar sua vida?").
- Follow-up com data marcada pelo cliente na sessão; nunca "depois a gente se fala" solto.
- Proposta não vai por PDF ou mensagem no lugar da conversa: convidar para mostrar ao vivo.
- Negociação só dentro do piso definido em `02-oferta`; o agente nunca cria condição, desconto ou parcela.
- Uma oferta por vez: produto de entrada só depois do não definitivo ao HT.
- Lead frio sem resposta depois das tentativas: parar e levar a outra ação (aula semanal, evento), não insistir.
- Só se para de falar com quem disse não; mesmo assim, ex-lead e ex-aluno voltam à lista no futuro.
- Aplicação só com seleção real; reprovado recebe motivo e a devolução prometida.
- WhatsApp nunca em massa; nenhuma mensagem automática a lead liga sem OK do estrategista (protocolo, regra 2).
- SDR e Closer produzem rascunho: a skill não envia, não liga e não marca na agenda de ninguém.

## 5. Padrões assumidos (o agente decide e lista em "Assumi: … (é só pedir para mudar)")

- **Aplicação antes da sessão:** padrão = sessão gratuita sem aplicação (canal 1a1 no começo; mais volume, mais falta). Alternativas:
  aplicação gratuita com ficha (filtra sem barreira de pagamento) ou aplicação paga reembolsável (referência do método R$ 500
  a R$ 2.000; o método usa R$ 2.000; filtra e compromete, reduz volume). O valor, se houver, entra em `02-oferta`.
- **Quem agenda e faz o follow-up:** expert, SDR do expert ou secretária (custo e qualidade do primeiro contato).
- **Ligar automação de lembretes** e por qual canal (WhatsApp oficial, e-mail), com quais textos.
- **Ferramenta de agenda:** agendamento manual com 2 horários (padrão do método) x link de calendário com lógica condicional.
- **Técnicas de abertura de caso** (ex.: a sequência "só o nome, áudio mudo, depois me fala" citada em conteúdo do método): usar ou não.
- **Condição da repescagem e piso de negociação:** mexem em preço, logo saem de `02-oferta` com OK do estrategista.
- **Política de reagendamento** (quantas vezes) e quando encerrar um lead.

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Fluxo do sim à decisão com responsável e prazo de cada etapa.
- [ ] Mensagem do primeiro contato, do agendamento (2 horários, até 2 dias) e da formalização em rascunho.
- [ ] Os 5 lembretes escritos, todos com confirmação afirmativa e o link no lugar certo.
- [ ] Roteiro de no-show (durante, depois, 2ª tentativa, encerramento) e regra de reagendamento.
- [ ] Roteiro de fechamento do retorno na sessão e cadência de follow-up com encerramento e repescagem.
- [ ] Toda condição de preço ou negociação citando `02-oferta` (versão), sem valor inventado.
- [ ] Aplicação (se houver): ficha, critérios, mensagens de aprovado e reprovado, devolução.
- [ ] Spec da automação marcada desligada; nada enviado.
- [ ] Colunas de controle e metas de comparecimento definidas.

**Auditoria (erros típicos dos plantões e laboratórios):** contato horas ou dias depois do sim; "qual horário é bom pra você?"
aberto; sessão marcada para a semana seguinte; "estou passando para confirmar, tudo certo?"; texto gigante com emojis e link
cru; número sem foto; prometer o expert e mandar outro; deixar o lead sair "pensando" sem data; follow-up marcado para semanas
depois; mandar PDF de proposta no lugar da conversa; "vamos aproveitar a oferta" com cara de feira; culpa ou chantagem no
no-show; insistir para sempre em lead frio; oferecer o produto barato junto com o HT; aplicação sem seleção de verdade;
reprovado sem motivo ou sem devolução; automação de lembrete ligada sem OK.

## 7. Saída e handoff

- Cadência, roteiros, follow-up e aplicação → `03-sessao/` (Closer), com o bloco de entrega do protocolo.
- Spec de automação → `11-automacoes/lembretes-sessao/` (`ht-gestor-automacoes`), desligada.
- Revisão: todas as mensagens → `ht-revisor-metodo-copy`. Sem parecer, entrega incompleta.
- Depois do OK do estrategista: o envio é feito por quem ele indicar; a skill não envia.
- Objeção que apareceu no follow-up → `ht-objecoes` (árvore). Sessão que não converte → `ht-treino-comercial`.
- Números de agendamento, comparecimento e follow-up → `ht-central-e-kpis` (07-numeros). Debrief a cada 20 sessões →
  `13-aprendizados/`.

## 8. Ferramentas de apoio (por nome)

- Texto: `avoid-ai-writing`, `humanizer`, `voice-builder`.
- Automação (só com OK do estrategista): `automacao-fluxos`, `conectar-whatsapp-oficial`, `email-marketing-mautic`.
- Planilha de controle: `anthropic-skills:xlsx`.
- Análise de gravação para follow-up: `watch`, `transcrever-youtube` (só arquivos do projeto; dado de lead fica na pasta).

## 9. Limites (não inventar)

Não há regra oficial de quantas vezes reagendar nem de intervalo exato entre toques de follow-up além de
"~1 semana" e "1 mês"; números de referência com ruído (cerca de 14 follow-ups até marcar; 3 ligações ≈ +60% de chance de atender;
~20% atendem; 90% somem sem aplicação paga) ficam como "conferir"; sessão em até 2 dias e 2 horários oferecidos valem como padrão do
método; a mensagem antes da sessão segue a forma afirmativa ("só passando pra dizer que já está tudo certo").
