---
name: ht-slg
description: 'Squad High Ticket / método FHT. Social Lead Generation para encher a agenda da sessão 1a1 sem tráfego: lista de 50 a 100 potenciais (do mais quente ao mais frio), qualificação por característica visível, as 3 mensagens (desarmadora, condução, arremate) personalizadas por lead e por fonte, rotina diária com a conta 100-20-1, fontes de lista (enquete, stories, isca qualificada, live, Kinder Ovo, arpão), nome do convite, delegação e auditoria de prints. Use quando o estrategista disser "monta a lista do expert", "escreve a desarmadora para esse perfil", "quantas abordagens para 20 sessões?", "audita as mensagens", "de onde tiro lead orgânico?". Produz RASCUNHO para o estrategista aprovar; não envia nada nem fala com lead. NÃO usar para LPSG/5+1/Funil 8 (Turbo), agendamento e lembretes (ht-agendamento-e-follow-up) ou anúncio pago (ht-trafego-high-ticket).'
---

# SLG: Social Lead Generation para a sessão 1a1

## 1. Para que serve e o que entrega

O SLG é a prospecção social do FHT: abrir conversa, com contexto e sem cara de venda, com quem já tem o perfil do cliente, e
levá-lo até o "sim" para a sessão 1a1. Troca dinheiro de tráfego por tempo; custo quase zero, conversão alta porque a pessoa é
filtrada antes. Objetivo único da conversa: **vender o agendamento, nunca o HT no direct.** A venda acontece na sessão.

**Entrega** (em `experts/<slug>/ht/04-demanda/slg/`), sempre como rascunho para o estrategista:
1. `lista.md` (ou `.xlsx`): lista de 50 a 100 potenciais por categoria e prioridade, com qualificação marcada.
2. `qualificacao.md`: resumo do avatar ("Meu avatar é...") e características mínimas visíveis, em duas camadas.
3. `rascunhos/AAAA-MM-DD-lote-NN.md`: mensagens personalizadas por lead (desarmadora em 2 partes; condução e arremate prontos
   para quando a pessoa responder), com a fonte e o ponto de conexão anotados.
4. `rotina.md`: meta de sessões → conta reversa de abordagens por dia, janelas de trabalho, fontes a ativar na semana.
5. `fontes.md`: peças de geração de lista (enquete, sequência de stories, isca, live) em rascunho.
6. `auditoria/AAAA-MM-DD.md`: correção de prints de abordagem (erro → ajuste) e diagnóstico da etapa que falha.
7. Registro de cada lead abordado no formato da Central 1x1 (`central-1x1-slg.csv`), para o consolidado do `ht-central-e-kpis`.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`:
   - `02-oferta/oferta-vigente.md`: **definição do AR** (insumo obrigatório das mensagens) e a parcela (o corte de renda da
     qualificação conversa com ela).
   - `03-sessao/` (nome em `nome-da-sessao.md`, dono ht-closer; ausente = `[A CONFIRMAR COM ht-closer]`): **nome da sessão 1a1** (o arremate usa esse nome) e o roteiro (para saber o que se promete).
   - `01-pesquisa/`: avatar, subnicho, 4 âncoras (dores e desejos na voz do avatar), listas do Market Fit.
   - `04-demanda/vitrine/`: o perfil precisa estar minimamente pronto (a abordagem leva a pessoa ao perfil). Vitrine ausente:
     avisar o Diretor e sugerir `ht-vitrine` antes ou em paralelo.
3. Entradas obrigatórias: definição do AR, nome da sessão, avatar, meta de sessões e prazo, ativos do expert (seguidores,
   WhatsApp, ex-alunos, grupos, lives). Se faltar, até 3 perguntas ao estrategista, por exemplo:
   - "Quantas sessões queremos em quantos dias?"
   - "Quem vai operar o direct: o expert ou alguém da equipe dele?"
   - "Quais listas o expert já tem (ex-alunos, WhatsApp, lista de evento)?"

## 3. Passo a passo

**Passo 1. Meta e conta reversa.** Da meta de vendas ou de sessões, calcular abordagens por dia com a conta 100-20-1 e as
taxas de referência (cenários em `references/rotina-e-funil.md`, seção 2). O 100-20-1 da trilha 10 é o pior cenário com
lista 100% fria (20% de agendamento sobre abordagens); outras turmas citam 10%: mostrar os cenários, nunca prometer. Meta padrão do método: 20 sessões com oferta
apresentada (25 no desafio), mesmo imperfeitas, antes de concluir qualquer coisa (padrão do squad).

**Passo 2. Lista de 50 a 100 potenciais** (`references/lista-e-qualificacao.md`, seção 1). Do mais quente ao mais frio:
alunos e ex-alunos, ambiente profissional, social, grupos, network de eventos, quem segue e interage, depois desconhecidos
(Google Meu Negócio, LinkedIn, perfis de players). "Fruta baixa" primeiro. Só potenciais do HT. Lista fria de telefone não
recebe WhatsApp: vira público de tráfego (passar ao `ht-trafego-high-ticket`).

**Passo 3. Qualificação** (`references/lista-e-qualificacao.md`, seção 2). Três frentes: tem o problema, tem perfil para
investir, tem contexto para aplicar. Só características visíveis no perfil e que sejam ponto de corte; o resto se valida na
condução. "Não óbvio, passa." Mas no começo o filtro não pode ser estreito demais: as primeiras sessões também treinam o
expert, e o funil afunila depois (bootcamp abr/2026). Cara de Pix vai para a sessão; sem perfil para o HT vai para a aula semanal ou outro funil.

**Passo 4. Análise do perfil e ponto de conexão.** Para cada lead: conferir a qualificação, achar a **fonte/contexto** (de
onde veio: seguiu, curtiu, respondeu story, ex-aluno) e um **ponto de conexão** específico e verdadeiro (um post, um evento,
um tema). Anotar os dois na linha do lead. Perfil fechado: usar só a procedência.

**Passo 5. Rascunhar as 3 mensagens** (`references/mensagens.md`):
1. **Desarmadora**: nome, contexto, ponto de conexão, uma pergunta sem cara de venda; curta, em 2 partes.
2. **Condução**: valida o que a pessoa disse e busca, uma pergunta por vez, a característica mínima e a dor ou o desejo.
3. **Arremate**: no timing (dor ou desejo apareceu), liga o que ela disse ao diagnóstico, convida com o nome da sessão e pede
   o WhatsApp (ou já oferece 2 horários, se quem agenda é o próprio expert no direct).
Modelos por fonte e por canal (Instagram, WhatsApp, LinkedIn, Facebook, presencial, B2B) na mesma referência. A primeira
pergunta faz a pessoa falar dela; a condução pode usar 2 ou 3 opções fechadas tiradas do perfil; o arremate diz o benefício
para a pessoa. Se o rascunho veio do agente de IA, conferir se a desarmadora não já puxa para o negócio (erro típico do agente).

**Passo 6. Filtro de humanização.** Passar cada rascunho por `avoid-ai-writing` e `humanizer`, e pela lista de marcas de IA
da `references/mensagens.md` (seção 5): sem travessão, sem cadeia de adjetivos, sem aspas, sem "dei uma olhada rápida", sem
textão, na voz do expert.

**Passo 7. Entrega do lote ao estrategista.** Lote com até o volume diário da rotina; cada mensagem com lead, fonte, conexão e o
porquê da pergunta. **A skill não envia.** Quem envia, depois do OK, é o expert (ou quem o estrategista autorizar), do perfil do
expert, à mão.

**Passo 8. Próxima mensagem a partir da resposta.** Quando o estrategista trouxer o print da resposta, rascunhar a condução ou o
arremate. Quando houver o "sim" e o WhatsApp, passar o lead ao `ht-agendamento-e-follow-up`.

**Passo 9. Fontes de lista** (`references/fontes-de-lead.md`). Uma ou duas fontes por vez, esgotando uma antes de abrir outra
(bootcamp abr/2026); enquete de qualificação nos stories toda semana (rende mais que caixinha); isca e tráfego ficam para depois. Lembrar: votos e visualizações de story somem em 48 h,
lista de curtidas da live só aparece ao encerrar; print na hora.

**Passo 10. Registro e leitura do funil.** Cada lead entra na Central 1x1 (origem "Social"; desarmadora, condução e arremate
sim/não). A cada lote ou semana, ler o funil por etapa e apontar onde falha (`references/rotina-e-funil.md`, seção 4).

**Passo 11. Auditoria** de prints e do lote antes de entregar (`references/auditoria-slg.md`).

## 4. Regras inegociáveis do método

- SLG é relacionamento, não spam: poucas mensagens, uma por pessoa, personalizadas. Nunca disparo em massa, nunca copia e cola,
  nunca robô de DM. (Trava do kit: WhatsApp nunca em massa.)
- "Interessado antes de interesseiro": a 1ª mensagem não tem nada a ver com o que o expert vende.
- Vender o agendamento, não o produto; preço e oferta só na sessão. Preço antes da sessão, só para afastar lead claramente
  desqualificado, e com o número de `02-oferta`.
- Uma pergunta por mensagem, um assunto por vez; mensagens curtas e separadas; esperar a resposta antes de mandar outra.
- Validar o que a pessoa disse antes de seguir; não virar interrogatório; não perder o timing do arremate.
- Não ser invasivo: nada de faturamento, margem ou "quanto quer investir" na abertura; isso aparece na condução, se precisar.
- Pessoas se conectam com pessoas: a desarmadora sai do perfil pessoal do expert. Perfil de membro do time quase não responde.
- Nunca mentir sobre quem escreve: se perguntarem, o membro da equipe se apresenta como equipe.
- B2B: venda é para pessoa; achar o dono ou o decisor, não o perfil da empresa. O decisor precisa estar na sessão.
- Ética de fonte: pode abordar quem interagiu publicamente com conteúdo do nicho; não prospectar dentro de curso, grupo ou
  comunidade fechada de terceiros. Lista fria de telefone: sem WhatsApp. Google Meu Negócio: só números públicos de empresa (LGPD).
- Automação (ManyChat) só quando o lead pediu algo (palavra-chave para receber material) e só com OK do estrategista; a abordagem
  seguinte é humana.
- Volume: alunos citam mandar cerca de 30 mensagens por dia sem bloqueio (fala de diagnóstico, não limite oficial; conferir). O
  bloqueio citado nas aulas vem de texto igual em sequência (copia e cola), não do volume personalizado.
- Nunca convidar dentro de grupo; cada pessoa no privado.
- Resiliência: perda em todas as etapas é normal; mais "não" que "sim". Só se para de falar com alguém quando a pessoa diz não.
- O SDR (`ht-sdr`) produz rascunho; não envia, não fala com lead (protocolo, regra 2).

## 5. Quando a decisão é do estrategista

Formato: decisão numerada, opções a/b/c com prós, contras e custo; recomendação na a).
- **Quem opera o SLG**: a) o expert (mais resposta); b) equipe do expert depois da 2ª mensagem ou no WhatsApp; c) pessoa
  contratada só para SLG (referência de aula R$ 1.000 a 1.500 por mês, conferir; decisão de gasto).
- **Ligar automação de isca** (palavra-chave no ManyChat) e qual pergunta de filtro.
- **Sessão paga ou Kinder Ovo** como fonte: mexem na oferta (valor da sessão, bônus num produto barato), então dependem de
  `02-oferta` e do estrategista. Referência de aula: sessão de avaliação de R$ 97 a 3 mil, R$ 500 vendeu mais que R$ 197 (conferir).
- **Nome e rotação do convite** (ex.: "diagnóstico", "análise", "auditoria"; "liberei mais 10 análises").
- **Abordar lista do expert que é sensível** (pacientes, clientes de serviço regulado) ou base antiga com áudio.
- **Volume diário** muito acima das ~30 mensagens por dia citadas (risco de bloqueio da conta do expert).

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Meta de sessões e conta reversa por dia calculadas, com as taxas e a fonte de cada uma marcadas "referência".
- [ ] Lista com pelo menos 50 nomes por categoria, prioridade e qualificação marcada (ou o que faltou e por quê).
- [ ] Características mínimas visíveis e de corte (sem dor, desejo ou objeção misturados), em duas camadas.
- [ ] Cada rascunho tem lead, fonte, ponto de conexão verdadeiro e a pergunta final sem cara de venda.
- [ ] Condução e arremate preparados para as respostas prováveis; arremate usa o nome exato da sessão de `03-sessao`.
- [ ] Nenhuma mensagem com preço, oferta, link cru, travessão, textão ou mais de uma pergunta.
- [ ] Pelo menos uma fonte de lista nova da semana em rascunho, com o lembrete de print em 48 h.
- [ ] Registro no formato da Central 1x1 pronto.
- [ ] Nada enviado; tudo marcado "rascunho para aprovação".

**Auditoria** (`references/auditoria-slg.md`): 12 critérios por mensagem e a tabela de erros dos laboratórios. Erros que
derrubam a entrega: copia e cola (nome errado, texto igual para todos); textão; tom de ChatGPT; "matar todas as etapas numa
mensagem"; várias perguntas; abrir falando de faturamento; mensagem para o perfil da empresa; pular a condução; arremate sem
ponte com o que a pessoa disse; característica de qualificação vaga ("disposto a fazer o que precisa"); abordar quem não decide.

## 7. Saída e handoff

- Gravar em `experts/<slug>/ht/04-demanda/slg/` com o bloco de entrega do protocolo.
- Revisão: rascunhos e peças de stories → `ht-revisor-metodo-copy`. Sem parecer, entrega incompleta.
- Depois do OK do estrategista: o envio é manual, pelo expert ou por quem o estrategista indicar.
- Lead que disse sim e passou contato → `ht-agendamento-e-follow-up` (scripts de agendamento, lembretes, no-show).
- Lista fria de telefone e públicos de engajamento → `ht-trafego-high-ticket`. Destino de link → `ht-pagina-inscricao-sessao`.
- Números do funil → `ht-central-e-kpis` (07-numeros). Debrief do ciclo de 20 sessões → `13-aprendizados/`.

## 8. Ferramentas de apoio (por nome)

- Texto: `avoid-ai-writing`, `humanizer` (filtro obrigatório), `voice-builder` (voz do expert), `hook-generator` (gancho de
  stories e enquetes).
- Pesquisa de perfis e do nicho: `instagram-analise-estrategica-turbo`, `leitura-web-turbo`, `niche-research`.
- Peças de stories e carrossel com palavra-chave: `gerador-instagram-turbo`, `carrossel-instagram-publicacao`.
- Planilha da lista e da Central: `anthropic-skills:xlsx`.
- Automação de isca (só com OK): `automacao-fluxos`.

## 9. Fontes e lacunas

**Fontes:** trilha 10 (aulas 02 a 10 lidas por inteiro na revisão R3; White Label de Mensagens, planilhas Lista de potenciais e
Central 1A1); desafio abr/2026, bootcamp 97 e laboratório 98 de SLG (lidos por inteiro na revisão R3); rota 3, resumo e
transcrição 06; demais laboratórios e bootcamps de SLG dos desafios (jul/2026 RJ itens 10-11, jun/2026 SP aulas 22-23, jan/2026
aulas 129-130, dez/2025 aulas 146-147, mai/2025 159, mar/2025 178, via RESUMOs da
trilha 22 e partes E, F, G); lives FHT 001-003, 020, 025, 027, 038, 043 (partes H e I: arpão, convite por oportunidade,
Kinder Ovo, sessão paga, notificação de curiosidade); catálogo (fht-lista-de-potenciais-clientes, fht-slg-qualificacao,
fht-slg-mensagens, fht-slg-agente-ia, fht-slg-auditoria-mensagens, fht-slg-rotina-e-funil, fht-slg-fontes-de-lead,
fht-slg-delegar-para-equipe, fht-prospeccao-arpao, fht-nome-e-rotacao-do-convite-1a1, fht-fontes-de-lead-qualificado-1a1);
GPT "FHT Social Lead Generation" (citado; prompt não disponível).

**Lacunas (não inventar):** o material não dá cadência em dias entre mensagens do SLG (só "esperar um dia e mandar oi" num
caso); o prompt interno do GPT da FHT não existe nos arquivos (o prompt da `references/agente-ia-e-delegacao.md` é nosso, não o
deles); o 100-20-1 foi conferido na trilha 10, aula 08 (agendamentos, lista fria, pior cenário), mas outras turmas citam taxas
menores; as ~30 mensagens por dia são fala de diagnóstico, não limite da Meta; o custo de pessoa de SLG é fala de aula;
o mapa mental e a Central do Desafio não foram lidos; o detalhe da ferramenta interna de IA de SLG citada na Live 025 não existe.
