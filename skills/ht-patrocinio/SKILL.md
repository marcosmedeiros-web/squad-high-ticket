---
name: ht-patrocinio
description: 'Monta o patrocínio de um evento de venda do HT: decide se vale buscar, planilha de custos, cotas, mídia kit, prospecção, negociação, manual do expositor e pós-evento. Use com "patrocínio da imersão", "mídia kit", "cotas do evento". NÃO usar para vender ingresso (ht-venda-de-ingressos) nem afiliados.'
---

# Patrocínio de evento high ticket

## 1. Para que serve e o que entrega

Evento presencial custa caro e o ingresso muitas vezes não paga a conta. No método o evento existe para vender o HT a quem está
sentado na cadeira; patrocínio e expositores são a forma de abrir o evento com a estrutura coberta (meta: "zero a
zero") e sobrar margem. Esta skill leva o projeto da pergunta "vale buscar patrocinador?" até o pós-evento que vira prova
para a edição seguinte.

**Entrega** (em `05-eventos/<AAAA-MM-tipo-nome>/patrocinio/`):
1. `decisao.md`: parecer buscar / não buscar agora, com custo x receita de ingresso e espaço disponível.
2. `planilha-custos-e-cotas.xlsx` (ou `.md` enquanto rascunho): custos previsto x executado, tabela de cotas com preço,
   entregas e contrapartidas, soma das cotas x custo.
3. `midia-kit.md` (estrutura e texto, página a página) para o Diretor de arte transformar em PDF/slides.
4. `prospeccao.md`: lista priorizada de candidatos com fit e o porquê de cada um.
5. `roteiros-abordagem.md`: WhatsApp em blocos, call de 30 min, e-mail pós-call com pré-reserva, follow-up, convite ao kick-off.
6. `negociacao.md`: o que se negocia e o que não se negocia, condições de pagamento propostas, cláusulas para o jurídico.
7. `checklist-riscos.md` por patrocinador e `manual-do-expositor.md` (índice preenchido).
8. `pos-evento.md`: pesquisa de expositores e participantes, mensagem do expert no dia seguinte, o que vai para o próximo mídia kit.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões vigentes, pasta com dono).
2. Ler a pasta do projeto `<raiz_projetos>/<expert>/ht/`:
   - `00-plano/` (estado, cronograma, aprovações, decisões);
   - `05-eventos/<evento>/` (decisão de formato, Big Idea, metas e orçamento feitos pela `ht-decisao-de-evento`);
   - `07-numeros/` (orçamento do evento, receita esperada de ingresso e de HT);
   - `01-pesquisa/` (perfil do público, pesquisa de avatar: vira o "perfil do público" do mídia kit);
   - `06-entrega/` (provas e cases) e `13-aprendizados/` (debrief de edições anteriores, depoimentos de expositores).
3. Entradas obrigatórias: data e local (ou previsão), público estimado, formato (presencial/online), planta ou metragem do
   espaço, orçamento previsto, receita prevista de ingresso. Se faltar, não abrir questionário: assumir o padrão (janela e capacidade pelo
   formato do evento, orçamento estimado pela planilha, sem histórico) e listar em "Assumi". Perguntar só o impossível de
   adivinhar (por exemplo, "Tem data e local?"), no máximo 2 coisas por vez e em linguagem simples. O resto vira `[FALTA: …]`
   ou `[SUPOSIÇÃO: …]`.
4. Pré-condição do método: o programa é para quem **tem evento previsto nos próximos meses** (principalmente presencial).
   Sem evento mapeado, registrar "fora do momento" e devolver ao Diretor.

## 3. Passo a passo

### Passo 1. Decidir se é hora de buscar patrocínio
- Gatilho do método: **custo estimado do evento acima da receita de ingresso** e **espaço para expositor** (ou, no online,
  espaço para a marca aparecer: banner, vídeo, link, menção).
- Funciona pequeno: caso de referência com evento de 150 a 200 pessoas em que 2 patrocinadores cobriram 80% do custo na 1ª edição.
  Funciona online: o patrocinador recebe alcance e dados mensuráveis (quem assistiu, por quanto tempo, cliques).
- Pode começar antes do evento estar todo estruturado: esboçar quem se quer dentro, montar a planilha e, com o custo, dividir
  em cotas.
- Expectativa honesta para a pessoa: 1º ano sofre (às vezes o expert põe dinheiro do bolso), 2º ganha visibilidade, 3º
  consolida e os expositores procuram o evento.
- Saída: `decisao.md` com a conta (custo previsto, receita de ingresso prevista, diferença, espaço) e a recomendação.

### Passo 2. Planilha de custos prevista x executada
Blocos de custo, colunas e regras em `references/planilha-e-cotas.md`. Pontos que o método cobra:
- Preencher a coluna **prevista** antes de abrir qualquer cota; a **executada** durante e depois.
- Incluir **impostos** e **taxa da plataforma de pagamento**: o caso de referência esqueceu os dois na previsão.
- Prever estouro: no caso de referência o realizado passou o previsto em cerca de R$ 150 mil (referência, conferir).
- Planilha é dado sensível do projeto: fica na pasta, não vai para material externo.

### Passo 3. Converter custo em cotas
- Dimensionar o espaço com a planta (quantos estandes de cada tamanho cabem; projetista/montadora ajuda).
- Definir a **cota máster** (maior estande, mais entregas, a única com tempo de palco), as **intermediárias** e a **menor**.
  O nome é do evento (o caso usou máster, diamante, platina, ouro). Pode nascer cota nova pela demanda (o caso criou uma
  intermediária com 3 estandes entre máster e diamante).
- **Fórmula de preço**: custo da feira ÷ m² da feira = custo por m²; × m² da cota; + ~50% pelas entregas extras
  (live, e-mail, palco, menções); + margem para negociar (exemplo: se a conta dá 50, anuncia 70).
- Conferir que **a soma das cotas paga as despesas** previstas.
- **Cota propriedade (permuta)** para evento pequeno sem caixa: o patrocinador paga direto ao hotel/fornecedor a sala ou o
  coffee break, em troca de 10 a 20 minutos para apresentar o produto.
- Preço de cada cota: a skill propõe pela fórmula e lista em "Assumi" (seção 5); vira oficial na aprovação do plano.

### Passo 4. Lista de candidatos com fit
- Três fontes do método: quem **já patrocina eventos do segmento**; quem **vende para o mesmo público**; **fornecedores**
  do próprio expert. Estudar cada candidato antes de abordar (site, redes, eventos em que aparece).
- Filtro de fit "ganha-ganha": o patrocinador **não concorre** com o produto do expert, **facilita** a oferta do HT e
  **interessa** ao público. Contraexemplo: rede de motéis num evento de infoproduto. O expert é quem precisa brilhar.
- Rodar o checklist de riscos (Passo 9) já na lista, não depois do contrato.
- Usar `leitura-web` ou `niche-research` para levantar quem patrocina eventos do nicho (pesquisa externa marcada como tal).

### Passo 5. Mídia kit
Estrutura de 11 blocos em `references/midia-kit.md`. Regras: **dados reais e atualizados** (seguidores,
ingressos já vendidos, público de edições anteriores); sem histórico, usar a base de clientes ou uma pesquisa com o público;
nunca prometer o que não entrega ("100 rosas" e põe 10); sem "historinha" sem dado. O texto sai daqui; a execução visual vai
para o Diretor de arte (`gerador-slides`, `slides-uipm` ou `anthropic-skills:pptx`/`pdf`).

### Passo 6. Kick-off de vendas das cotas
- Evento grande e recorrente: **webinário de kick-off ~365 dias antes**, no formato de um semente, com o **expert
  apresentando** a edição e as novidades; convidar expositores dos anos anteriores e empresas que passaram pela base.
- No fim, **formulário** de escolha de cota e posição, por ordem de chegada; reserva com sinal (Passo 8).
- Meta de referência: **60% dos estandes vendidos ou em negociação no 1º mês** de comercialização; depois a equipe aborda
  ativamente os que quer no evento. Caso: pico de 72 pessoas no webinário e 46 estandes (referência).
- Evento pequeno ou 1ª edição: o "kick-off" é uma conversa com 1 ou 2 patrocinadores-alvo.
- Roteiro em `references/prospeccao-abordagem-negociacao.md`.

### Passo 7. Abordagem
WhatsApp em blocos curtos (saudação, quem sou, cotas abertas, o expert pediu para priorizar vocês, convite para call),
esperando 5 a 10 min entre blocos; se pedirem "manda o material", propor **call de 30 min**; depois da call, **e-mail com a
pré-reserva** do estande de interesse, o book, **3 pontos fortes** do evento e as condições de pagamento; sem resposta, um
novo e-mail. Modelos em `references/prospeccao-abordagem-negociacao.md`. Toda mensagem sai como **rascunho**: quem envia é o
time do expert, com o OK simples da pessoa (é falar em nome do expert).

### Passo 8. Negociação
- A proposta é padrão; o que se negocia são **contrapartidas** (e-mail extra para a base com conteúdo validado, live
  pós-evento com o expert, sorteio no palco, desconto de ingresso para clientes do patrocinador).
- **Não se negocia**: tempo de palco fora da cota máster; **lista/mailing de participantes** fora da cota máster. O caso de referência
  é ambíguo: diz que o mailing "não se entrega para todo mundo" e também o lista entre as entregas da máster (conferir).
  Padrão do squad: não entregar mailing (dado pessoal de participante, LGPD) e oferecer a captura de lead por leitor oficial no
  estande; entregar à máster só com o OK simples da pessoa e base legal validada pelo jurídico.
- Piso: não vender "a preço de banana", porque a cota paga a estrutura inteira, não só o estande. Preço de custo só para marca
  estratégica que traz autoridade, só se a pessoa pedir.
- Não prometer ganho quantitativo ao patrocinador (nem número de vendas). Faltou visibilidade para fechar: **bônus de
  fechamento** (e-mail pré ou pós-evento, live).
- Condições usadas no caso (referência; a skill propõe por projeto e lista em "Assumi"): reserva com sinal fixo abatido da cota e 30 dias para
  decidir (na fala, a gestora diz R$ 3 mil e se corrige para R$ 6 mil; conferir); 10% de desconto para pagamento em 30 dias após
  o contrato; até 12 parcelas sem virar o ano em débito; 5% nas últimas cotas; upgrade de categoria com diferença diluída.
- Contrato com **multa** e proibição de produto concorrente; cláusulas em `references/prospeccao-abordagem-negociacao.md`
  marcadas "validar com o jurídico do projeto".
- Vendedor terceirizado de patrocínio cobra percentual e ainda pesa imposto e taxa: o método prefere pessoa interna.

### Passo 9. Riscos e manual do expositor
- Checklist por patrocinador em `references/riscos-e-manual-do-expositor.md`: concorrência com o produto, pitch agressivo no
  palco, pedido de lista de contatos, apresentação do palestrante patrocinador vista antes, número de pitches externos
  reduzido, externos para o **fim do último dia** (depois das vendas do HT) quando não houver confiança.
- Evolução do caso de referência: de 6 cotas máster com palco para 4 e depois 2, só no 1º dia (a manhã do 2º dia prepara a primeira
  oferta do HT), porque alguns vendiam produto de alto valor no palco (referência). Tempo de palco do caso: 15 minutos por
  expositor, apresentação vista antes e uma pessoa do time conversando com cada um.
- **Manual do expositor**: índice completo na referência; enviado **até 90 dias antes** (prazo no contrato); uma pessoa do
  time circulando na feira para fiscalizar.

### Passo 10. Pós-evento
- Pesquisa ao fim do evento para **expositores e participantes**; para subir a taxa de resposta, dizer que a pesquisa melhora a
  próxima edição e aceitar tudo o que vier (elogio e crítica).
- **Mensagem do expert no dia seguinte** aos expositores: agradece, dá o número do evento e pergunta "como foi para você?".
  As respostas viram prova social do próximo mídia kit.
- Levar o patrocinador a uma live depois de fechado e provocar um lançamento dele perto do evento ajuda a renovar.
- Debrief em `13-aprendizados/` (previsto x executado, cotas vendidas, o que o expositor reclamou, o que muda).
- Modelo de pesquisa, mensagem e debrief em `references/pos-evento.md`.

## 4. Regras inegociáveis do método

1. Não vender cota sem conhecer o **custo do evento** e **quem se quer dentro**.
2. Fit antes de dinheiro: patrocinador que concorre ou tira o brilho do expert não entra, mesmo pagando.
3. Tudo o que está no mídia kit e no contrato tem de ser cumprido; dado sempre real e atualizado.
4. Palco só para máster; mailing de participantes não entra nas cotas (exceção só com OK simples e base legal, ver Passo 8).
5. Não prometer resultado quantitativo ao patrocinador.
6. Impostos e taxa de plataforma entram na planilha desde a coluna prevista.
7. Regras de conduta do expositor no contrato e no manual, com multa; o aceite combinado em contrato não volta atrás "porque
   foi pedido".
8. O evento serve à venda do HT: grade, palco e feira não podem competir com o pitch (alinhar com `ht-palestras-e-pitch`).
9. Padrões recomendados aplicáveis: nenhuma regra numérica fixa de patrocínio foi decidida; tudo que é preço, desconto e
   aceite de patrocinador a skill propõe pelo padrão e lista em "Assumi" (seção 5). Se o patrocínio for usado para trocar a entrada do evento
   (gratuita, credencial, paga), vale o padrão `entrada_imersao`: a skill propõe a entrada e lista em "Assumi".

## 5. O que a skill decide e lista em "Assumi"

Decidir pelo padrão ou pela recomendação, sem lote de perguntas, e listar em "Assumi: X, Y, Z (é só pedir para mudar)"; vira oficial na aprovação do plano. Continuam pedindo só o OK simples ("posso seguir?"): enviar qualquer mensagem a patrocinador, contratar ou gastar, entregar mailing de participantes (exige base legal) e usar foto, nome ou depoimento de aluno (exige autorização registrada).
- Buscar patrocínio nesta edição ou não (e se online, presencial ou ambos): seguir o parecer de `decisao.md`.
- Preço e quantidade de cotas, nomes, o que cada uma entrega; margem de negociação.
- Valor do sinal, desconto à vista, número de parcelas, desconto das últimas cotas.
- Aceitar ou recusar um patrocinador com risco de fit: padrão = recusar o de fit duvidoso; preço de custo a marca estratégica só se a pessoa pedir.
- Quantos pitches externos no palco, em que dia e por quanto tempo (caso: 15 min, só no 1º dia).
- Incluir ou não mailing de participantes na cota máster (padrão: não; exige base legal validada).
- Quem do time faz a venda: padrão = interno; terceirizar é contratar e pede o OK simples.
- Enviar qualquer mensagem a patrocinador (é falar em nome do expert): sempre o OK simples ("posso enviar?").

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] `decisao.md` com custo previsto, receita de ingresso, diferença e espaço, e recomendação clara.
- [ ] Planilha com todos os blocos, impostos e taxa de plataforma, colunas prevista e executada.
- [ ] Cotas com m², entregas, contrapartidas e preço calculado pela fórmula; soma das cotas ≥ custo previsto.
- [ ] Mídia kit com os 11 blocos, só dado real com fonte; `[FALTA: …]` onde não há dado.
- [ ] Lista de candidatos com o motivo de fit de cada um e o checklist de riscos rodado.
- [ ] Roteiros de abordagem, call e e-mail em rascunho; nenhum enviado sem OK.
- [ ] Negociação com o que se negocia e o que não se negocia; condições propostas pelo padrão e listadas em "Assumi".
- [ ] Manual do expositor com o índice completo e prazo de 90 dias previsto em contrato.
- [ ] Pós-evento planejado (pesquisa, mensagem do expert, uso no próximo mídia kit).

**Auditoria final (erros típicos do material; conferir um a um)**
1. Cota vendida sem custo conhecido ou sem planilha?
2. Impostos e taxa de plataforma fora da previsão?
3. Patrocinador sem fit ou que concorre com o HT do expert?
4. Mídia kit com número desatualizado (seguidores, ingressos) ou história sem dado?
5. Promessa ao patrocinador de número de vendas ou de público que o evento não garante?
6. Palco oferecido fora da máster, ou mailing de participantes oferecido sem OK e sem base legal?
7. Cota "a preço de banana" ou desconto a quem não compra nem vende ao público?
8. Contrato sem multa, sem proibição de produto concorrente, sem prazo do manual?
9. Pitch externo antes do pitch do HT, sem ver a apresentação antes?
10. Expectativa de 1ª edição vendida como se fosse 3ª?

## 7. Saída e handoff

- Grava em `05-eventos/<evento>/patrocinio/` (agente dono da tarefa: `ht-ingressos-e-patrocinio`, dentro da pasta do
  `ht-produtor-eventos`). Números consolidados vão para o `ht-controller` (`07-numeros/`) por handoff, não por escrita direta.
- Bloco de entrega no formato do `ht-protocolo`, com a linha "Assumi" e as lacunas.
- Texto (mídia kit, roteiros, e-mails, manual) → `ht-revisor-metodo-copy`.
- Mídia kit visual e planta → `ht-diretor-arte` → `ht-designer` → `ht-revisor-visual`.
- Contrato → jurídico do expert (fora do squad); a skill só lista cláusulas.

## 8. Ferramentas de apoio

`anthropic-skills:xlsx` (planilha de custos e cotas), `anthropic-skills:pptx` / `anthropic-skills:pdf` / `gerador-slides` /
`slides-uipm` (mídia kit), `anthropic-skills:docx` (manual do expositor e e-mails), `designer-senior` (mídia kit em
página), `leitura-web` e `niche-research` (quem patrocina eventos do nicho), `avoid-ai-writing` e `humanizer` (revisão
das mensagens antes do revisor).

## 9. Lacunas (não inventar)

(1) Os materiais de apoio (script de abordagem, planilha de custos, mídia kit, live de lançamento) são modelos reconstruídos desta skill, nunca apresentados como arquivo pronto de outro evento; (2) o valor do sinal de reserva varia entre casos (R$ 3 mil ou R$ 6 mil): conferir; (3) o exemplo numérico de custo por m² é ilustrativo; (4) não há modelo de contrato, só cláusulas citadas: o jurídico do expert redige; (5) os números do caso de referência (R$ 2,3 mi de despesa, 45 expositores, cotas de R$ 60 a 90 mil) são de evento de 2.500 a 3.500 pessoas: não servem de régua para evento pequeno; (6) não há método próprio para patrocínio de evento online além de "muda a forma como a marca aparece".
