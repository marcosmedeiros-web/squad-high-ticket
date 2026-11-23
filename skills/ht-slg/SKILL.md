---
name: ht-slg
description: 'Social Lead Generation para encher a agenda da sessão 1a1 sem tráfego: lista de potenciais, qualificação, as 3 mensagens (desarmadora, condução, arremate), rotina com a conta 100-20-1 e fontes de lista. Use para "monta a lista do expert", "escreve a desarmadora", "quantas abordagens para 20 sessões?". Só rascunho. NÃO use para agendamento nem anúncio.'
---

# SLG: Social Lead Generation para a sessão 1a1

## 1. Para que serve e o que entrega

O SLG é a prospecção social do método: abrir conversa, com contexto e sem cara de venda, com quem já tem o perfil do cliente, e
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
   WhatsApp, ex-alunos, grupos, lives). Se faltar, até 2 perguntas simples por vez (o resto o agente assume e lista em "Assumi"), por exemplo:
   - "Quantas sessões queremos em quantos dias?"
   - "Quem vai operar o direct: o expert ou alguém da equipe dele?"
   - "Quais listas o expert já tem (ex-alunos, WhatsApp, lista de evento)?"

## 3. Passo a passo

**Passo 1. Meta e conta reversa.** Da meta de vendas ou de sessões, calcular abordagens por dia com a conta 100-20-1 e as
taxas de referência (cenários em `references/rotina-e-funil.md`, seção 2). O 100-20-1 é o pior cenário com
lista 100% fria (20% de agendamento sobre abordagens); outras turmas citam 10%: mostrar os cenários, nunca prometer. Meta padrão do método: 20 sessões com oferta
apresentada (25 em versão de desafio), mesmo imperfeitas, antes de concluir qualquer coisa (padrão do squad).

**Passo 2. Lista de 50 a 100 potenciais** (`references/lista-e-qualificacao.md`, seção 1). Do mais quente ao mais frio:
alunos e ex-alunos, ambiente profissional, social, grupos, network de eventos, quem segue e interage, depois desconhecidos
(Google Meu Negócio, LinkedIn, perfis de players). "Fruta baixa" primeiro. Só potenciais do HT. Lista fria de telefone não
recebe WhatsApp: vira público de tráfego (passar ao `ht-trafego-high-ticket`).

**Passo 3. Qualificação** (`references/lista-e-qualificacao.md`, seção 2). Três frentes: tem o problema, tem perfil para
investir, tem contexto para aplicar. Só características visíveis no perfil e que sejam ponto de corte; o resto se valida na
condução. "Não óbvio, passa." Mas no começo o filtro não pode ser estreito demais: as primeiras sessões também treinam o
expert, e o funil afunila depois. Cara de Pix vai para a sessão; sem perfil para o HT vai para a aula semanal ou outro funil.

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

**Passo 7. Entrega do lote ao estrategista, com o "Assumi" e o "posso seguir?" simples.** Lote com até o volume diário da rotina; cada mensagem com lead, fonte, conexão e o
porquê da pergunta. **A skill não envia.** Quem envia, depois do OK, é o expert (ou quem o estrategista autorizar), do perfil do
expert, à mão.

**Passo 8. Próxima mensagem a partir da resposta.** Quando o estrategista trouxer o print da resposta, rascunhar a condução ou o
arremate. Quando houver o "sim" e o WhatsApp, passar o lead ao `ht-agendamento-e-follow-up`.

**Passo 9. Fontes de lista** (`references/fontes-de-lead.md`). Uma ou duas fontes por vez, esgotando uma antes de abrir outra
;  enquete de qualificação nos stories toda semana (rende mais que caixinha); isca e tráfego ficam para depois. Lembrar: votos e visualizações de story somem em 48 h,
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
  bloqueio vem de texto igual em sequência (copia e cola), não do volume personalizado.
- Nunca convidar dentro de grupo; cada pessoa no privado.
- Resiliência: perda em todas as etapas é normal; mais "não" que "sim". Só se para de falar com alguém quando a pessoa diz não.
- O SDR (`ht-sdr`) produz rascunho; não envia, não fala com lead (protocolo, regra 2).

## 5. O que o agente decide e o que pede OK

Sem lote de perguntas nem a/b/c: o agente decide pela recomendação e lista em "Assumi".
- **Quem opera o SLG**: assume o expert (mais resposta) e lista em "Assumi". Equipe do expert depois da 2ª mensagem ou no WhatsApp é a alternativa; pessoa contratada só para SLG (referência R$ 1.000 a 1.500 por mês, conferir) é gasto e pede "posso seguir?".
- **Ligar automação de isca** (palavra-chave no ManyChat) e qual pergunta de filtro: o agente propõe a pergunta; ligar a automação pede "posso seguir?".
- **Sessão paga ou Kinder Ovo** como fonte: mexem na oferta (valor da sessão, bônus num produto barato), então dependem de
  `02-oferta`. O agente não inclui sem estar na oferta e lista em "Assumi". Referência: sessão de avaliação de R$ 97 a 3 mil, R$ 500 vendeu mais que R$ 197 (conferir).
- **Nome e rotação do convite** (ex.: "diagnóstico", "análise", "auditoria"; "liberei mais 10 análises"): o agente propõe pelo padrão e lista em "Assumi".
- **Abordar lista do expert que é sensível** (pacientes, clientes de serviço regulado) ou base antiga com áudio: o agente deixa de fora no primeiro lote, lista em "Assumi" e só inclui com "posso seguir?".
- **Volume diário** muito acima das ~30 mensagens por dia citadas (risco de bloqueio da conta do expert): o agente mantém até ~30 e lista em "Assumi".

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

**Auditoria** (`references/auditoria-slg.md`): 12 critérios por mensagem e a tabela de erros comuns. Erros que
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
- Pesquisa de perfis e do nicho: `instagram-analise-estrategica`, `leitura-web`, `niche-research`.
- Peças de stories e carrossel com palavra-chave: `gerador-instagram`, `carrossel-instagram-publicacao`.
- Planilha da lista e da Central: `anthropic-skills:xlsx`.
- Automação de isca (só com OK): `automacao-fluxos`.

## 9. Limites

**Não inventar:** o método não dá cadência em dias entre mensagens do SLG (só "esperar um dia e mandar oi" num caso); o prompt de `references/agente-ia-e-delegacao.md` é do squad; o 100-20-1 é o pior cenário com lista fria, mas outras turmas citam taxas menores; as ~30 mensagens por dia são fala de diagnóstico, não limite da Meta; o custo de pessoa de SLG é referência falada.
