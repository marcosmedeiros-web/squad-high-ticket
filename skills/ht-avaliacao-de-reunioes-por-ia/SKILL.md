---
name: ht-avaliacao-de-reunioes-por-ia
description: 'Squad High Ticket / método FHT (trilha 15, IA no HT). Decide se a operação está pronta e desenha, monta e calibra a avaliação automática de 100% das reuniões de entrega e de venda: Fireflies grava e transcreve, n8n busca a transcrição, IA 1 avalia etapa por etapa (cumprida, parcial, não cumprida, com timestamp, em JSON), IA 2 dá nota 0-100 ponderada e resumo, Google Sheets registra, Error Trigger e alerta de nota baixa (< 70) avisam o gestor. Inclui prompts de sessão de diagnóstico e de sessão 1a1 de venda, avaliação de mentor e closer por bloco, custos e infra. Use quando o estrategista disser "avaliar as reuniões com IA", "montar o fluxo Fireflies n8n", "prompt de avaliação da sessão", "nota baixa do mentor", "auditar calls do closer". Nada envia mensagem nem liga sem OK do estrategista. NÃO usar para automação de lead da Turbo.'
---

# Avaliação de reuniões por IA

## 1. Para que serve e o que entrega

Garante a qualidade quando o expert delega a entrega a mentores ou a venda a closers: toda reunião é avaliada contra o roteiro
oficial assim que termina, e o gestor só assiste às poucas que tiram nota baixa (no FHT, corta 80% a 90% das avaliações manuais;
número de aula). Não gera venda: só faz sentido em operação que já vende e já tem método escrito.

**Entrega** (conforme o pedido), em `experts/<slug>/ht/11-automacoes/avaliacao-reunioes/`:
1. `prontidao.md`: diagnóstico dos pré-requisitos (sim/não com evidência) e recomendação "montar agora / ainda não".
2. `arquitetura.md`: desenho do fluxo para este expert (tipos de reunião, planilhas, quem recebe alerta), custos e decisões para o estrategista.
3. `prompts/<tipo>-avaliacao.md` e `prompts/<tipo>-nota-e-resumo.md`: os dois prompts por tipo de reunião (diagnóstico, reunião
   estratégica, sessão 1a1 de venda...), em Markdown, derivados do manual de entregáveis e do roteiro do expert.
4. `planilha-avaliacao.xlsx` (modelo de colunas) e `roteiro-de-montagem.md` (passo a passo do n8n para quem vai montar).
5. `calibracao.md`: registro das rodadas de teste (reunião, nota da IA, nota humana, ajuste feito no prompt ou no modelo).
6. `mineracao.md` (quando pedido): como usar as transcrições para Toque de Midas, objeções e evolução do método.

## 2. Antes de começar

- Carregar `ht-protocolo`. Pedido do Diretor conferido.
- Ler: `06-entrega/` (manual de entregáveis, roteiro de cada entregável, mentores), `03-sessao/` (roteiro oficial da sessão 1a1,
  Raio-X, deck), `02-oferta/` (o que o mentor e o closer podem prometer), `11-automacoes/` (o que já existe), `13-aprendizados/`.
- **Pré-requisitos do método** (aula 1 e 2): oferta encaixada, já vende bem, metodologia clara, **manual de entregáveis escrito**
  (do bootcamp de entrega) e intenção de delegar. Se faltar o manual ou o roteiro, a skill para e devolve ao Diretor: "automação sem
  clareza não funciona" (paráfrase do professor). Próximo passo vira ht-escala-da-entrega ou ht-roteiro-sessao-1a1.
- Entradas obrigatórias: tipo(s) de reunião a avaliar, roteiro/manual de cada um, plataforma de reunião (Meet, Zoom, Teams), quem
  recebe o alerta. Se faltar, no máximo 3 perguntas:
  1. Quais reuniões vamos avaliar primeiro (o entregável gargalo ou a sessão de venda)?
  2. O roteiro oficial dessas reuniões está escrito (manual ou roteiro de 6 etapas)?
  3. Quem deve ser avisado quando a nota for baixa (só o gestor, ou também o líder do mentor/closer)?

## 3. Passo a passo

### Passo 1. Prontidão e decisões para o estrategista
Checklist em `references/arquitetura-e-custos.md`. Montar a lista de decisões (seção 5) antes de qualquer conta ser criada:
contratação de ferramentas (gasto), canal de alerta, consentimento de gravação e envio de dados de reunião a terceiros.

### Passo 2. Arquitetura (versão simples do FHT, do simples para o complexo)
1. Reunião no Meet, Zoom ou Teams (Google Calendar facilita: o gravador entra sozinho).
2. **Fireflies** entra como participante, grava e transcreve (conta gratuita basta; idioma português; reunião com menos de 5 min não
   grava).
3. Ao terminar, o Fireflies avisa o **n8n por webhook** (manda só o aviso e o `meetingId`, não a transcrição).
4. n8n pede a transcrição pela API (**Get a transcript**, com o `meetingId` em modo Expression).
5. **Code 1** limpa e junta a transcrição em um bloco com timestamps e o título.
6. **IA 1** (AI Agent + Chat Model): avalia cada etapa do roteiro como cumprida, parcial ou não cumprida, com observação e timestamp,
   em JSON.
7. **Code 2** quebra o JSON em campos.
8. **Google Sheets, Append Row**: grava a linha da reunião.
9. **IA 2**: recebe a transcrição completa + o JSON da IA 1 e devolve nota geral 0-100 (ponderada) e resumo.
10. **Code 3** trata a resposta.
11. **Google Sheets, Append or Update Row** casando pelo nome da reunião: grava nota e resumo.
12. Extra: **If** nota < 70 → alerta ao gestor com nota, reunião, link e participantes. Fluxo separado com **Error Trigger** avisa
    quando o fluxo quebra.
Duas IAs rendem mais que uma (o professor testou juntar e a qualidade caiu); pode-se testar juntar depois. Entrega e venda usam o
mesmo fluxo com prompt e planilha diferentes (separar por tipo com nó **Switch**; o material só cita, não ensina).
Passo a passo de cada nó, com as configurações ditas em aula: `references/montagem-n8n-fireflies.md`.

### Passo 3. Prompts (o coração)
Modelos em `references/prompts-de-avaliacao.md`.
- **IA 1 (avaliação por etapa)**: papel de avaliador técnico que verifica se o mentor/closer cumpriu os critérios obrigatórios de
  cada etapa; responde só em português; usa os timestamps (minutos:segundos) para justificar parcial e não cumprida; classifica cada
  etapa em cumprida / parcial / não cumprida; saída em JSON com status e observação por etapa.
- Cada etapa tem sub-itens obrigatórios tirados do manual de entregáveis (diagnóstico) ou do roteiro oficial (venda). No FHT, para o
  diagnóstico: Apresentação, Visão estratégica, Jornada de sucesso, Oferta, Recap final, Próximos passos, Segunda call (sub-itens de
  Apresentação e Visão estratégica foram ditados; os demais saem do manual do expert).
- **IA 2 (nota e resumo)**: nota 0 a 100 com peso por etapa. No diagnóstico do FHT, peso maior em Jornada de sucesso, Oferta e
  Recap; Apresentação perde no máximo 10 pontos. Para a sessão de venda, os pesos são proposta do squad a calibrar (referência).
- Avaliação de pessoa (mentor ou closer) de 1 a 5 por bloco, com recomendações e alertas: autopromoção, oferta de produto de
  terceiros, fechamento abrupto, desvalorização do aluno (palestra de encontro nov/2025).
- Relatório pré-sessão (o que olhar no Raio-X antes da call) e avaliação pós-sessão contra o roteiro: mesmos insumos, outro prompt.
- Escrever o prompt em Markdown (títulos com #, ##, ###). Base: o prompt do FHT + o manual do expert + uma transcrição real; pedir
  a uma IA boa que adapte.

### Passo 4. Modelo de IA e custo
- Conta de plataforma por API (pré-paga, por token), não assinatura de chat. Agregador citado: **OpenRouter** (uma chave, vários
  modelos, preço sem acréscimo). Créditos iniciais de teste citados: US$ 5 a 10; chave com limite de gasto diário (exemplo de aula:
  US$ 1/dia; em produção um pouco maior para não travar); 2FA ligado; sem recarga automática.
- IA certa para a função: reunião longa pede modelo barato com contexto longo. A aula usou Gemini 2.5 Flash (contexto ~1 milhão de
  tokens). Na hora de montar, conferir no comparador do OpenRouter o modelo atual equivalente (contexto, preço de entrada e saída,
  latência) e registrar a escolha em `arquitetura.md`.
- Custo medido na aula 5 com o Gemini 2.5 Flash: reunião real completa com as duas IAs ficou em torno de US$ 0,03 a 0,04
  (cerca de R$ 0,20; reunião mais longa ou prompt maior, R$ 0,30). A conta foi feita ao vivo com ruído de legenda: conferir na
  conta real depois das primeiras execuções. O prompt de avaliação do FHT tinha ~1.300 tokens.
- Se a qualidade não chegar lá depois de ajustar o prompt, a aula sugere trocar o Flash por um modelo mais forte da mesma
  família (ex. citado: Gemini 2.5 Pro); o refinamento vem primeiro do prompt, depois do modelo.
- Infra: n8n nuvem (citado R$ 125/mês anual ou R$ 150/mês, 2.500 execuções; cada reunião = 1 execução) ou n8n num servidor próprio
  (~R$ 35/mês, com manutenção própria). Para não-desenvolvedor, a aula recomenda nuvem. Se você já tem servidor próprio, é opção a
  avaliar com o estrategista.

### Passo 5. Planilha de avaliação
Colunas (aula 5): nome da reunião, data, duração, participantes, link da transcrição, nota geral, resumo, e para cada etapa
"status" e "observação". Uma aba por tipo (entrega, venda). A planilha precisa estar no Drive da conta Google conectada.
Modelo em `references/planilha-e-alertas.md`.

### Passo 6. Teste e calibração
1. Reunião de teste com pelo menos 5 minutos; ver a execução verde no n8n (Executions).
2. Rodar com transcrições reais (uma boa, uma média, uma ruim, de preferência já avaliadas por humano).
3. Conferir: a nota bate com a avaliação humana? A IA está "boazinha" (dando 10 a tudo)? Ajustar o prompt como se fosse feedback a um
   funcionário; trocar de modelo se o prompt não resolver. A primeira versão costuma ficar mediana.
4. Conferir o próprio prompt: palavra estranha no prompt contamina a resposta (caso citado de IA que passou a falar palavrão).
5. JSON quebrado em reunião longa: rodar de novo ou tratar no Code.
6. Registrar cada rodada em `calibracao.md`. Só pedir ao estrategista para ligar em produção depois de ≥ 5 reuniões reais com nota da IA
   a até 10 pontos da nota humana (critério do squad).

### Passo 7. Alertas e erros
- **Error Trigger** em fluxo separado, ligado em Settings → Error Workflow do fluxo principal: mensagem com o erro e o nome do
  workflow.
- **Nota baixa** (nó If, nota < 70, tipo número): mensagem com nota, reunião, link, participantes.
- Canal citado em aula: WhatsApp por API não oficial (Z-API, ~R$ 100/mês por número; ou Evolution API em servidor próprio) só para alerta
  interno de baixo volume; disparo em massa a cliente só pela API oficial. No squad, o canal do alerta é decisão do estrategista e o
  destino é só a equipe interna.
- Acompanhar as Executions (verdes e vermelhas) toda semana: é mais importante que ter criado o fluxo.

### Passo 8. Gravar, transcrever e minerar
- Toda interação com aluno é gravada e transcrita (cabeçalho: tipo, nicho, mentor, aluno, duração) e indexada na pasta do projeto.
- Minerar: trecho do feedback do mentor para o Toque de Midas (ht-provas-e-cases), objeções reais (ht-objecoes), padrões de quem teve
  resultado (engenharia reversa), problemas recorrentes (planilha de Problemas e Oportunidades).
- Corpus de referência do FHT (3.354 gravações da trilha 21, por tipo e nicho) é consultado pelo ht-consultor-casos, nunca copiado
  com nome de aluno para fora.

## 4. Regras inegociáveis do método e do squad

1. Sem manual de entregáveis ou roteiro escrito, não se automatiza.
2. A IA avalia contra o roteiro oficial do expert, não contra o gosto do avaliador.
3. Duas etapas de IA (avaliação por etapa e nota/resumo), com timestamp na justificativa.
4. Calibrar com reunião real antes de confiar na nota.
5. Nota da IA é triagem, não sentença: nota baixa leva um humano a assistir antes de qualquer feedback ao mentor ou closer.
6. **Nenhum envio liga sem OK do estrategista**: alerta de nota baixa, aviso de erro, resumo para mentor, feedback ao closer, mensagem ao
   aluno. O fluxo é entregue com os nós de envio desligados (ou fora do fluxo) até o OK registrado em `00-plano/aprovacoes.md`.
7. Fluxo publicado e ativo em produção também só com OK do estrategista (ativar = começar a processar dados reais).
8. Chave de API (Fireflies, OpenRouter, Google, WhatsApp) nunca no chat, no prompt, no brief, em print ou em arquivo do projeto:
   vai direto no gerenciador de credenciais da ferramenta (ex.: Credentials do n8n), digitada pelo dono; o agente não lê nem mostra
   a chave.
9. Conta e contratação de ferramenta (n8n pago, créditos de IA, Z-API) é gasto: decisão do estrategista; conta é criada pelo dono, nunca
   pelo agente.
10. Dado de reunião é dado pessoal de aluno ou lead: fica na conta do projeto; nada de transcrição em material público.

## 5. Quando a decisão é do estrategista

1. **Ferramentas e gasto**: a) n8n nuvem (simples, ~R$ 125-150/mês citado); b) n8n em servidor próprio (mais barato, manutenção
   própria); c) adiar. Créditos de IA e limite diário da chave.
2. **Consentimento**: como avisar mentores, closers, alunos e leads que a reunião é gravada e analisada por IA, e se o contrato do
   programa já cobre (o material não trata disso; lacuna).
3. **Envio de dado a terceiros** (Fireflies, provedor de IA): aceitar ou escolher alternativa.
4. **Canal e destinatários do alerta**: WhatsApp interno, e-mail, Telegram; quem recebe.
5. **Limiar da nota** (padrão de aula: 70) e o que acontece com a reunião abaixo dele (refazer a entrega? quem decide?).
6. **Feedback ao mentor/closer**: automático ou só via gestor (recomendação do squad: só via gestor).
7. Ligar o fluxo em produção.

## 6. Critério de pronto e auditoria final

**Pronto para pedir o OK do estrategista quando**:
- [ ] Prontidão: manual/roteiro escritos e anexados.
- [ ] Prompts IA 1 e IA 2 por tipo de reunião, em Markdown, com sub-itens tirados do roteiro e pesos explicitados.
- [ ] Saída JSON definida (campos por etapa) e mapeada para as colunas da planilha.
- [ ] Calibração com ≥ 5 reuniões reais registrada (nota IA x nota humana).
- [ ] Error Trigger e If de nota baixa montados, com envio desligado.
- [ ] Custos mensais estimados e decisões da seção 5 listadas.
- [ ] Nenhuma chave em arquivo, chat ou print.

**Auditoria (erros típicos das aulas)**:
1. Esquecer de publicar o fluxo (o webhook de produção só responde publicado).
2. Colar a Test URL no Fireflies em vez da Production URL.
3. Não marcar "Transcription complete" nas configurações de desenvolvedor do Fireflies.
4. Reunião de teste com menos de 5 minutos.
5. AI Agent vermelho: faltou "Define below" ou faltou plugar o Chat Model.
6. Planilha fora do Drive da conta conectada.
7. IA "boazinha" (notas altas demais) sem calibração.
8. Prompt único fazendo tudo (qualidade pior).
9. Chave exposta em tela ou chat.
10. WhatsApp não oficial usado para disparo a cliente.
11. Cartão sem limite / trial do Fireflies aceito sem querer (fechar no X).

## 7. Saída e handoff

- Grava em `11-automacoes/avaliacao-reunioes/` (dono: ht-gestor-automacoes). O ht-controller lê a nota média como KPI de qualidade
  (ht-central-e-kpis); o ht-treinador-comercial usa as avaliações de venda (ht-treino-comercial); o ht-arquiteto-entrega usa as de
  entrega (ht-escala-da-entrega).
- Prompts e textos de alerta → **ht-revisor-metodo-copy** (confere se o prompt reflete o método e o roteiro).
- Montagem técnica pode ser feita pelo executor de automação do squad, seguindo o roteiro; ativação e envios só com OK do estrategista.

## 8. Ferramentas de apoio

`automacao-fluxos` (desenho e montagem do fluxo), `anthropic-skills:xlsx` (planilha de avaliação e calibração), `watch` e
`transcrever-youtube-turbo` (transcrever gravação antiga para calibrar), `conectar-whatsapp-oficial` (se o estrategista escolher a API
oficial para alertas), `analytics-dashboard` (painel da nota por mentor, interno).

## 9. Fontes e lacunas

**Fontes**: trilha 15 Bootcamp de Inteligência Artificial (01-introducao, 02-como-funciona, 03-cadastro-fireflies,
04-configurando-n8n, 05-chat-model, 06-error-triger; RESUMO.md); parte-C (arquitetura, fluxo, prompts, calibração); parte-I
(avaliador de gravações de sessão: nota 1-5 por bloco e alertas; relatório pré e pós-sessão; Kaizen); parte-D (auditor de gravação de
entregável); parte-H (gravar e transcrever); trilha 19 (manual de entregáveis, roteiro do diagnóstico em blocos e tempos); trilha 09
(roteiro de 6 etapas da sessão); CATALOGO seção 9.

**Lacunas**: (1) o prompt completo do FHT, os códigos dos nós Code, a planilha-modelo e o JSON do fluxo foram passados no chat/mapa
mental e não estão nos arquivos: os modelos desta skill são reconstrução marcada; (2) número de etapas do prompt do diagnóstico
diverge (6 x 7 na legenda); (3) regra de corte entre "parcial" e "não cumprida" só tem um exemplo dito em aula ("dois x" já dá parcial), sem regra fechada; (4) pesos exatos da nota não foram
ditos, só a regra geral; (5) consentimento e LGPD não são tratados no material; (6) custo por execução foi medido ao vivo com ruído (≈ US$ 0,03-0,04 ou R$ 0,20 por reunião real), conferir na conta;
(7) o nó Switch para separar tipos de reunião é citado, não ensinado.
