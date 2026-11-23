---
name: ht-entregaveis-1a1
description: 'Squad High Ticket / método FHT. Estrutura e roteiriza os entregáveis individuais do HT do expert a partir dos 5 modelos reais do FHT (3.354 gravações): diagnóstico, plano de ação, reunião estratégica, checkup de vendas e análise de vendas. Para cada um: estruturador de 5 perguntas, formulário com perguntas coringa, agenda, roteiro com blocos e tempos, perguntas do mentor, fechamento com próximo passo e documento de ações (núcleo). Use quando o estrategista disser "roteiro do diagnóstico do aluno", "como o mentor conduz o plano de ação", "estrutura a reunião estratégica", "checkup antes do evento do aluno", "analisa a sessão gravada", "documento de feedbacks". NÃO usar para o cardápio da oferta (ht-entregaveis), entregas em grupo (ht-entrega-em-grupo), sessão de venda do expert (ht-roteiro-sessao-1a1) nem LPSG/5+1 da Turbo.'
---

# Entregáveis individuais (1a1) do HT

## 1. Para que serve e o que entrega

O entregável individual é onde o aluno sente o acompanhamento: alguém olha o caso dele, decide junto, devolve o que fazer e
cobra a evidência. O FHT entregou milhares deles (1.003 diagnósticos, 1.168 reuniões estratégicas, 602 planos de ação, 312
checkups e 269 análises gravados na trilha 21), e a estrutura que se repete nessas gravações é o modelo desta skill. Ela pega o
cardápio já aprovado em `02-oferta/` e transforma cada entregável individual em processo que qualquer mentor treinado repete
com a mesma qualidade.

Os 5 do FHT servem de **molde por função**, adaptado ao nicho do expert (o diagnóstico de uma nutricionista não monta oferta
HT; monta o plano personalizado da paciente pela jornada dela). Quando o HT do expert ensina negócio a outros experts, os
roteiros valem quase literais.

**Entrega**, em `experts/<slug>/ht/06-entrega/entregaveis-1a1/<entregavel>/`:
1. `estruturador.md`: as 5 perguntas respondidas (objetivo, output, preparo, condução, ferramenta) + função no ciclo.
2. `formulario-solicitacao.md`: campos de preparo + perguntas coringa (a partir do 2º entregável) + regra de condição.
3. `roteiro.md`: blocos com tempos, falas-guia, perguntas do mentor, fechamento e checklist do mentor (pré, durante, pós).
4. `agenda.md`: calendário por mentor, oferta de 2 horários, padrão do nome do evento, gravação e IA de resumo.
5. Para o projeto: `documento-de-acoes-modelo.md` (núcleo do aluno) e `sequencia-dos-entregaveis.md` (ordem e gatilhos).

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir o pedido do Diretor.
- Ler: `02-oferta/oferta-vigente.md` (nome, "o que é", benefício e "até N" de cada entregável; jornada e faixas),
  `01-pesquisa/` (avatar, objeções, Market Fit), `03-sessao/` (Raio-X e roteiro de venda: o checkup e a análise usam isso),
  `06-entrega/` (manual e roteiros que já existem, NPS), `07-numeros/` (Master Plan, usado no plano de ação).
- Entradas obrigatórias: qual entregável, a jornada do aluno (ponto de partida, etapas, chegada) e quem vai conduzir. Se faltar,
  no máximo 3 perguntas:
  1. Qual entregável estruturar primeiro e quantos o aluno tem direito ("até N")?
  2. O expert já entregou esse entregável? Quantas vezes, e há gravação?
  3. Quem conduz (expert ou mentor) e qual ferramenta de chamada e de registro o time usa?
- Gravações próprias do expert, se existirem, valem mais que o molde do FHT: ler 2 a 3 antes de escrever o roteiro.

## 3. Passo a passo

### Passo 1. Posicionar o entregável no ciclo do acompanhamento
Todo entregável serve a um dos 4 passos do ciclo (live 060): **direcionar** de forma personalizada (diagnóstico, plano de ação),
**fornecer recurso pronto** (drive, bootcamp, GPS: ht-entrega-em-grupo), **destravar** obstáculo (reunião estratégica, suporte em
tempo real) e **analisar** o que foi executado (checkup antes, análise depois). Ordem natural no FHT: diagnóstico → plano de ação
→ execução → checkup → suporte real time → análise → nova reunião ou revisão do plano. Registrar em `sequencia-dos-entregaveis.md`
qual entregável dispara qual (o fechamento de um indica o próximo).

### Passo 2. Estruturador de 5 perguntas
Modelo em `references/estruturador-formulario-e-agenda.md`.
1. Qual o objetivo? 2. O que o aluno leva no final (output concreto)? 3. Que informação o mentor precisa para se preparar
(vira o formulário)? 4. O que o mentor precisa para conduzir organizado (vira o roteiro e o documento de condução)? 5. Qual
ferramenta (mapa mental, documento, planilha, agenda, slide)?
- Começa na "revisão zero"; executar ~20 vezes antes de revisar a estrutura. Preciosismo não: melhora a cada entrega.
- Regra do entregável: tem **condição de execução** (o aluno pede depois de uma ação dele) e quantidade "até N" (padrão
  do squad), nunca frequência fixa.

### Passo 3. Formulário de solicitação e agenda
- Um formulário por entregável (ou um com seleção do entregável). Campos de preparo + perguntas coringa a partir do 2º:
  progresso no objetivo, resultado já alcançado (com o número do nicho), investimento feito (ex.: tráfego), maior desafio.
  Elas alimentam o catálogo de resultados (ht-provas-e-cases) sem esforço extra.
- Pré-requisito declarado no formulário (ex.: sem Raio-X, sem diagnóstico; sem gravação, a análise muda de formato).
- Agenda: um calendário por mentor; oferecer **2 horários** e marcar em até 2 dias (padrão do squad); evento com nome
  `[Entregável] | [Mentor] - [Aluno]`, videochamada e convite ao aluno e ao mentor. Gravar 100% com IA de resumo.

### Passo 4. Roteiro de cada entregável
Um arquivo de referência por entregável, com estrutura real das gravações, perguntas, erros e checklist:
- **Diagnóstico** → `references/diagnostico.md`. Lê o ponto de partida (Raio-X do aluno), desenha a jornada personalizada e
  fecha o produto do momento (no FHT, a oferta HT do aluno). **Alvo de 1h20, teto de 2 h e parte 2 prevista** quando a jornada
  não fecha (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Contexto: a aula do manual (trilha 19, aula 14) diz que o
  FHT testou 1h20 numa turma, errou, e voltou para cerca de 2 h (10 de abertura, 10 de visão estratégica, 40 de jornada, oferta,
  10 de recap, 5 de próximos passos); daí o teto. Gravações reais lidas: 42 a 81 min (as curtas tratam só parte do caso ou são
  continuação).
- **Plano de ação** → `references/plano-de-acao.md`. Da meta e da agenda real ao plano mês a mês de 3 a 4 meses, com metas de
  trás para frente e tudo lançado na agenda; revisão marcada.
- **Reunião estratégica** → `references/reuniao-estrategica.md`. Destrava um tema que o aluno escreveu no formulário; o mentor
  troca a pergunta do aluno pela que importa, dá direção clara e sai com o artefato rascunhado.
- **Checkup de vendas** → `references/checkup-de-vendas.md`. Pente fino na ação de venda antes de ir ao ar (sessão 1a1,
  imersão, live fechada) + suporte em tempo real durante.
- **Análise de vendas** → `references/analise-de-vendas.md`. Assiste a gravação da ação (no FHT, a sessão 1a1 do aluno) etapa
  por etapa, aponta o que corrigir e fecha com lista priorizada.
- Para entregável que não é dos 5 (roleplay, consultoria complementar, análise de imagem): aplicar o estruturador e o esqueleto
  comum de `references/esqueleto-comum-e-padroes-reais.md`.

### Passo 5. Esqueleto comum (vale para todo entregável individual)
Detalhe e números reais em `references/esqueleto-comum-e-padroes-reais.md`.
1. **Antes**: mentor lê formulário, documento do aluno (núcleo) e diário dos mentores anteriores; prepara hipóteses; tira dúvida
   com outro mentor se precisar. Confere se o entregável pedido é o certo para o momento: se não há o que analisar (ex.: análise
   pedida por quem fez 2 sessões e vendeu as 2), o mentor converte na abertura para o entregável certo (ex.: reunião estratégica)
   e o registro conta só um consumo. Sem formulário preenchido, sem material ou com o aluno sem condição de se concentrar
   (deslocamento, ambiente sem controle), remarca em vez de improvisar (visto em gravações da trilha 21).
   Quem participa: só quem está no programa (todos da conta, se for dupla ou trio, são convidados). Exceção vista no FHT: o
   expert parceiro de um aluno lançador entra no diagnóstico para montar a jornada, e só nele.
2. **Abertura (até 5 min)**: chamar pelo nome, quebra-gelo curto, apresentação do mentor em 30 a 40 s com credencial, dizer que
   estudou o caso, **declarar o objetivo e o output da sessão**, confirmar a pauta ("vi que você quer…, é isso?").
3. **Contexto (até 10 min)**: o aluno conta o momento; o mentor puxa número (fato com período), não opinião.
4. **Trabalho**: o bloco específico do entregável, com tela compartilhada e o artefato sendo preenchido ao vivo.
5. **Direção**: recomendar uma opção com a razão; opção solta só quando for teste. Neutralidade não ajuda o aluno.
6. **Recap (5 a 10 min)**: ler em voz alta as ações recomendadas; perguntar o maior insight.
7. **Próximo passo**: tarefa com data, próximo entregável indicado (e como pedir), onde está o artefato.
8. **Depois**: áudio de 1 a 1,5 min no diário do mentor; atualizar o documento de ações; NPS enviado pelo suporte; gravação na
   área de membros. Exceção: trecho de desabafo, vida pessoal ou dado sensível do aluno não sobe para a área de membros; a
   gravação fica guardada em `06-entrega/entregaveis-1a1/privado/` (o FHT faz o mesmo com entregas de desabafo).

### Passo 6. Documento de ações recomendadas (núcleo do aluno)
Modelo em `references/estruturador-formulario-e-agenda.md` (seção 4). Um documento por conta de aluno, não um por reunião: cada
entregável com data, mentor e assunto; até 14 pontos de ajuste e 15 ações com "feita?" e evidência; categorias do método do
expert. Dá contexto ao próximo mentor, evita conflito entre mentores e permite cobrar evidência. Abre no onboarding
(ht-onboarding-e-primeira-entrega).

### Passo 7. Exemplos reais por nicho (corpus da trilha 21)
Antes de roteirizar para um nicho, consultar 2 a 3 gravações do mesmo tipo e grupo de nicho em
`FORMULA HIGH TICKET/trilhas/21-gravacoes-dos-entregaveis/<tipo>/<grupo-de-nicho>/` (índice em `INDICE.md`). Como minerar e o
que extrair: `references/esqueleto-comum-e-padroes-reais.md` (seção 3). Nunca levar nome, número ou caso de aluno do FHT para
material do expert; o corpus é referência de condução.

## 4. Regras inegociáveis do método

1. Entregável individual é "até N" com condição de solicitação; nunca frequência fixa (padrão do squad, live 057 erro 4).
2. Todo entregável tem objetivo e output declarados no início e entregues no fim.
3. Mentor chega preparado (formulário, núcleo, diário); sem pré-requisito, o entregável muda ou é remarcado, não improvisado.
4. Direção clara com recomendação; nunca opção solta sem posição.
5. Próximo passo com data e próximo entregável indicado em todo fechamento.
6. Gravar 100%; resumo por IA; áudio no diário; documento de ações atualizado; NPS por entregável (ht-provas-e-cases).
7. Doses certas: entregar o que o aluno precisa agora, não tudo de uma vez (live 057, erro 3).
8. Não executar no lugar do aluno; o mentor direciona, dá recurso, destrava e analisa.
9. Preço, condição e bônus que aparecem num diagnóstico de oferta seguem o padrão do método (preço de 5x a 10x a média do nicho, validado em 20 sessões;
   garantia condicional e mensurável; ordem entrada, parcelado, à vista; sinal de R$ 500 a R$ 1.000, até 10% do valor, com a call
   aberta; dupla +50%) para o produto do
   aluno; para o expert, só `02-oferta/`.
10. Dados do aluno ficam em `06-entrega/entregaveis-1a1/privado/` (a base de alunos de `06-entrega/privado/` é do ht-cs); nada de nome ou número de aluno em material público.

## 5. Quando a decisão é do estrategista

- **Quantidade "até N"** de cada entregável e mudança no cardápio: é oferta (ht-arquiteto-oferta + estrategista).
- Padrão recomendado (não volta como pergunta; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): **diagnóstico** com alvo de 1h20, teto de 2 h e parte 2
  prevista quando a jornada não fecha (o manual do FHT usava cerca de 2 h como alvo); **demais entregáveis** com o alvo do manual
  e o teto na mediana real das gravações (ex.: reunião estratégica, alvo ~50 min e teto ~76 min), com parte 2 quando não fecha.
- **Quem conduz** (expert, mentor interno, parceiro) e se a promessa de venda permite (risco ético).
- **Ferramenta paga** (Zoom, IA de resumo, Notion pago).

## 6. Critério de pronto e auditoria final

**Pronto quando**, para cada entregável estruturado:
- [ ] Estruturador com as 5 respostas e a função no ciclo do acompanhamento.
- [ ] Formulário com campos de preparo, pré-requisito e perguntas coringa (a partir do 2º entregável).
- [ ] Roteiro com blocos, tempos, perguntas, fechamento e checklist pré, durante e pós.
- [ ] Output concreto definido (o que o aluno tem na mão ao sair) e onde fica salvo.
- [ ] Nome e "até N" iguais aos da oferta vigente (versão citada).
- [ ] Indica o próximo entregável e o gatilho.
- [ ] Documento de ações modelo pronto para o projeto.
- [ ] Nenhum nome ou número de aluno do corpus FHT no material.

**Auditoria (erros vistos nas gravações e nas aulas)**:
1. Sessão sem objetivo declarado: vira conversa e acaba sem output.
2. Mentor sem ler o formulário ou sem acesso ao mapa do aluno (houve sessão desmarcada por isso).
3. 5 a 15 min perdidos com câmera, microfone e permissão de link: checklist técnico antes.
4. Conversa paralela longa (desabafo, ferramenta, iluminação) sem trazer de volta à pauta.
5. Diagnóstico sem a transformação clara do aluno: gira 30 min e termina sem oferta (fazer parte 2 com tarefa, não forçar).
6. Lista de entregáveis que assusta o aluno: mostrar a carga real e liberar por partes.
7. Confundir checkup (antes) e análise (depois).
8. Plano de ação irreal (vira cobrança) ou sem a agenda real do expert.
9. Mentor ensina na análise o que devia corrigir na prática; ou critica sem a frase corrigida.
10. Fechamento sem data; NPS esquecido; diário não enviado.
11. Entregável prometido por frequência ("1 reunião por semana").
12. Entregável errado consumido: análise sem nada a analisar, diagnóstico pedido por quem já tem oferta redonda (converter ou
    remarcar, não queimar a cota do aluno).
13. Gravação com desabafo ou dado sensível publicada na área de membros.

## 7. Saída e handoff

- Grava em `06-entrega/entregaveis-1a1/` (dono: ht-arquiteto-entrega; ht-estrategista-sucesso e ht-arquiteto-oferta leem).
- Roteiros, formulários e falas → **ht-revisor-metodo-copy**. Slides ou mapa de condução → ht-diretor-arte → **ht-revisor-visual**.
- Formulários e agenda automatizados → ht-gestor-automacoes (com OK do estrategista). Manual do mentor e treino →
  ht-escala-da-entrega. NPS, perguntas coringa no catálogo e Toque de Midas → ht-provas-e-cases. Gravação e avaliação por IA →
  ht-avaliacao-de-reunioes-por-ia.

## 8. Ferramentas de apoio

`anthropic-skills:docx` e `anthropic-skills:xlsx` (roteiros, documento de ações, formulários), `transcrever-youtube-turbo` e `watch`
(rever gravação do próprio expert), `anthropic-skills:pptx` / `gerador-slides-turbo` (apoio visual da sessão), `humanizer` e
`avoid-ai-writing` (falas-guia), `automacao-fluxos` (formulário → agenda, só com OK).

## 9. Fontes e lacunas

**Fontes**: trilha 19, aulas 05 a 08 e 14 (estruturador, perguntas coringa, formulário, agenda, Notion, processo do diagnóstico),
RESUMO §5.4 a §5.7; trilha 21 INDICE e 15 gravações lidas inteiras (3 por tipo, nichos e mentores diferentes) + contagens no
corpus inteiro (durações do cabeçalho, termos, temas) feitas em 22/11/2026; parte-A (documento de ações), parte-D bloco 6 e 8,
parte-F (documento de feedbacks), parte-H (raio-x, diagnóstico, plano, checkup e real time, direção sem neutralidade), parte-I
(roteiro do diagnóstico, NPS e formulário); lives FHT 057, 060 (ciclo do acompanhamento, entregáveis por passo) e 061
(gravações de análises de outros alunos como entregável valioso), transcritas hoje. Revisão de 23/11/2026: trilha 19 aulas 02
a 18 lidas por inteiro e mais 10 gravações da trilha 21 (2 por tipo, nichos e mentores diferentes das 15 do escritor).

**Lacunas**: (1) as notas das gravações são, na maioria, vazias (60 de 1.003 diagnósticos, 26 de 602 planos) e o resto é resumo
automático: não há ata do mentor como gabarito; (2) os tempos por bloco vêm da posição na transcrição (±3 min) em 3 gravações por
tipo, não do todo; (3) o mapa mental do núcleo FHT e o template do Notion não foram abertos; (4) NPS no fechamento não aparece
nas 15 gravações lidas (é enviado pelo suporte depois); (5) a cota "até N" de reuniões estratégicas varia entre mentores (5 ou 6),
não dá para cravar o número do FHT.
