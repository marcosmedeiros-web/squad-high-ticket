---
name: ht-venda-de-ingressos
description: 'Squad High Ticket, método FHT. Monta e opera a venda de ingressos de um evento de venda do HT: meta e relatório diário ("SOS Ingresso"), tipos, lotes e preços, gratuitos como bônus e o menu de estratégias da trilha 17 (divulgação para a base, perpétuo, lote zero, relâmpago por e-mail, semente de ingresso, time comercial, downsell no evento, upsell em outros produtos, lives de aquecimento react e oficina), mais a página de vendas do ingresso. Use quando o estrategista disser "plano de ingressos", "lote zero", "relâmpago", "o ingresso não vende", "página de ingresso", "upsell do ingresso", "react de aquecimento". Entrada gratuita, credencial ou paga é decisão do estrategista, por evento. NÃO usar para afiliados, patrocínio, captação gratuita e presença (ht-captacao-e-presenca) nem lançamento LPSG/5+1/Funil 8/Turbo Express da Turbo.'
---

# Venda de ingressos do evento high ticket

## 1. Para que serve e o que entrega

No FHT o evento é o lugar onde o expert vende o HT a quem está na cadeira; com a pessoa presente, a conversão é parecida seja
aluno ou não, por isso o método aceita até prejuízo no ingresso desde que haja público. "Gente no evento vale mais que o
conteúdo do evento." Esta skill entrega o plano para encher o evento vendendo ingresso, medido dia a dia, com 2 ou 3
estratégias do menu rodando junto com o perpétuo.

**Entrega** (em `05-eventos/<AAAA-MM-tipo-nome>/ingressos/`):
1. `plano-de-ingressos.md`: meta, velocidade diária, responsável, Big Idea do evento, mix pago x gratuito, tipos e lotes,
   estratégias escolhidas com calendário, orçamento de tráfego pedido ao gestor.
2. `relatorio-diario.md` (modelo) e o grupo "SOS Ingresso" definido (quem manda, quem lê, a que horas).
3. Os roteiros e textos de cada estratégia escolhida (rascunhos para o núcleo de copy): lote zero, relâmpago, semente,
   lives de aquecimento, scripts por lista, mensagens do time comercial, upsell.
4. `pagina-de-vendas.md`: estrutura e copy da página do ingresso (para o `ht-web-designer`).
5. `auditoria.md` ao fim do ciclo de vendas.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`: `05-eventos/<evento>/` (decisão de formato, Big Idea, metas e orçamento da
   `ht-decisao-de-evento`; grade); `02-oferta/` (o HT que o evento vende; preço do ingresso só se já aprovado);
   `07-numeros/` (orçamento, custo do evento, CPL e conversão anteriores); `04-demanda/` (base, listas, aula semanal, Reels);
   `13-aprendizados/` (eventos anteriores).
3. Entradas obrigatórias: data e local, capacidade, decisão de entrada (gratuita, credencial ou paga), Big Idea, tamanho e temperatura das listas,
   verba. Perguntar no máximo 3 coisas se faltar:
   (a) "A entrada deste evento é gratuita, credencial ou paga?" (decisão do estrategista; se não decidido, apresentar o quadro da seção 5);
   (b) "Quantos lugares e qual o custo do evento?"; (c) "Quais listas temos e de que tamanho (alunos ativos, inativos,
   lançamentos, quem já foi a evento, 'agora não' da sessão 1a1)?".
4. Evento gratuito sem venda de ingresso: esta skill não se aplica; ir para `ht-captacao-e-presenca`. Evento com credencial:
   a cobrança da credencial é tratada aqui (tipos e preço) e a captação lá.

## 3. Passo a passo

### Passo 1. Meta, velocidade e responsável (aulas 21 e 22)
- **Meta de ingressos** = lotação, um pouco acima (nem todos comparecem; parte dos ingressos é gratuita).
- **Início**: 1 a 2 meses antes da data (evento novo com pouca audiência: 2 meses). Lote zero começa 4 a 6 meses antes.
- **Velocidade** = ingressos que faltam ÷ dias restantes. É o número que o time olha todo dia.
- **Responsável** com nome (no início pode ser o expert; o ideal é um squad pequeno: uma pessoa de criativo e Big Idea, outra
  de tráfego).
- O segredo, nas palavras da aula, não é um funil: é medir dia após dia e propor uma ação nova para amanhã.

### Passo 2. Relatório diário "SOS Ingresso"
Grupo só para isso; o responsável manda todo dia: vendas de ontem, acumulado, quanto falta, velocidade necessária x real,
custo por venda, criativos e campanhas que mais venderam, sugestão para amanhã. Modelo em `references/plano-e-relatorio-diario.md`.

### Passo 3. Big Idea e nome do evento
Destino simples e atrativo, em uma frase que a pessoa explica em casa. Caso da aula: nome confuso não vendia; baixar o preço
sozinho também não; o que destravou foi a Big Idea nova junto com o preço novo. Regra: **testar preço e Big Idea juntos** e
testar o nome em criativo. A Big Idea vem da `ht-decisao-de-evento`; aqui ela é testada.

### Passo 4. Tipos, lotes, preços e gratuitos
- Diferença principal entre gratuito e pago é **comparecimento** (referência da aula 22: gratuito ~40%, com muito esforço
  50% a 55%; pago pode passar de 100% porque leva acompanhante; para planejar, usar o padrão do squad: gratuito 25%,
  credencial ou pago 70%).
- Valor simbólico (R$ 97 a R$ 197 nas aulas) já faz a pessoa pôr na agenda.
- Categorias e lotes, oferta 2 por 1 e 3º com desconto, upgrade: modelos em `references/tipos-precos-e-gratuitos.md`.
- **Gratuito com critério** (aula 30): só para avatar de HT (bônus de tsunami de um low ticket, primeiros compradores,
  mentorados); nunca banalizar.
- Mudar de lote gera reclamação de quem pagou mais: resolver no 1 a 1, não deixar de testar por isso.
- Preço de cada tipo e lote é decisão do estrategista (seção 5).

### Passo 5. Escolher 2 ou 3 estratégias do menu + perpétuo
O menu (11 estratégias da trilha 17) e quando cada uma cabe:

| # | Estratégia | Cabe quando | Referência |
|---|---|---|---|
| 1 | Divulgação para a base | sempre, primeiro (orgânico converte mais que pago) | `divulgacao-base-e-time-comercial.md` |
| 2 | Perpétuo | sempre, é o ritmo diário | `perpetuo-e-pagina.md` |
| 3 | Lote zero | evento presencial com 4 a 6 meses de antecedência e lista ativa | `lote-zero.md` |
| 4 | Relâmpago por e-mail | base de e-mail; para picos e para upgrade | `relampago-e-semente.md` |
| 5 | Semente de ingresso | precisa de uma live que explique o evento; ticket alto | `relampago-e-semente.md` |
| 6 | Time comercial | sempre que houver listas geradas pelas ações | `divulgacao-base-e-time-comercial.md` |
| 7 | Downsell no evento ao vivo | vender o próximo evento no último dia do atual | `upsell-e-downsell.md` (pitch é da `ht-palestras-e-pitch`) |
| 8 | Ingressos gratuitos | avatar de HT a premiar | `tipos-precos-e-gratuitos.md` |
| 9 | Afiliados | produto estável | **`ht-afiliados-e-consultores`** |
| 10 | Upsell/downsell em outros produtos | expert tem low ticket ou outro produto rodando | `upsell-e-downsell.md` |
| 11 | Lives de aquecimento (react, oficina, conhecimento) | 40 a 60 dias antes, com material de edições anteriores ou oficina | `lives-de-aquecimento.md` |

Regra da aula: o que bateu recorde num evento pode não funcionar no seguinte; nunca depender de uma estratégia só.

**Complementares vistas no Bootcamp Lote Zero (aula 19)**, que entram como variações do menu: abordagem do comercial filtrada
pelo DDD da cidade do evento; social selling e lives no perfil próprio do evento (react de palestra da edição anterior, live com
aluna que teve resultado contando que o primeiro passo foi o evento, temas do nicho, a formatura da edição anterior); pitch curto
do evento em toda aula ao vivo do produto; semente com uma promessa de "método" que só se aprende no evento; e **downsell para
ingresso online** do evento presencial nas duas últimas semanas (seção 12). Números do caso em `references/lote-zero.md` §9.

### Passo 6. Divulgação para a base (estratégia 1)
Tudo o que o expert tem aponta para o evento nas semanas antes ("teoria das setas"): bio, post e vídeo fixados, stories
documentando a jornada, YouTube com o evento, comunidade de alunos, banner/pop-up na área de membros, criativo curto entre
aulas, QR code, aula inaugural e aulas semanais (seeding do evento), suporte (todo atendimento pergunta "já tem o ingresso?"),
direct, e-mail e API oficial do WhatsApp. **Listas da mais quente para a mais fria, um script por lista.** O expert precisa
"vibrar" o evento: incoerência (evento fora da bio, do calendário do local) faz a pessoa não comprar. Detalhe e scripts em
`references/divulgacao-base-e-time-comercial.md`. Público fora do Brasil, sem Instagram nem WhatsApp: a aula 23 aponta afiliados
como o que funcionou melhor (`ht-afiliados-e-consultores`).

### Passo 7. Perpétuo (estratégia 2)
Campanha contínua levando à página de vendas; meta mínima: o **custo de aquisição empatar o custo do evento** (muitas vezes é
melhor ingresso barato e vender o HT com menos pressão). **Criativo raiz** simples com benefício, data, horário, onde e o que
aprende; dele derivam variações de dor, desejo, objeção, história e encenação. Vídeo simples sem produção converte. Página com
botão de WhatsApp para dúvidas e **proteção de checkout** (captura nome, e-mail e telefone antes do checkout, para o comercial
recuperar). A campanha é montada pelo `ht-gestor-trafego` (objetivo Vendas; nasce PAUSADA, prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver); os
criativos pelo `ht-criativos-high-ticket`. Briefing em `references/perpetuo-e-pagina.md`.

### Passo 8. Lote zero (estratégia 3)
Pré-venda do lote mais acessível em um dia, num grupo de WhatsApp: mistura de webinário (como no semente) com abertura de
carrinho dentro do grupo. **8 passos**: estratégia, Big Idea, oferta, tema do webinário, aquecimento, convite e pontos de
contato, pré-lançamento (webinário + vídeos), lançamento. Calendário: 2 semanas de aquecimento, 2 de convite, vídeo 1 na
segunda (ancoragem e preço do último lote), webinário na quarta 20h + vídeo 2, carrinho na quinta das 9h às 19h só nos grupos,
reabertura na sexta com áudio do expert. Webinário dos **5 segredos** do evento anterior, cada um entregando valor e plantando o
próximo. Nos criativos fala-se só da oferta ("mais acessível", nunca "barato"). Não sobrepor com outro lançamento nem com pré-venda para a
mesma base (o caso viu o CAC quase triplicar). Oferta com **bônus de ação rápida**; o caso testaria começar com ticket menor e
abrir também para não alunos; sold out 1 a 2 meses antes libera o time para as palestras. Roteiro completo em `references/lote-zero.md`.

### Passo 9. Relâmpago (estratégia 4) e semente (estratégia 5)
- **Relâmpago**: 4 dias de e-mail. Dia 1 revela a oferta com a Big Idea e avisa que acaba rápido; dias seguintes trazem um
  motivo novo (oportunidade, bônus), "acaba amanhã", e no último dia "acaba hoje" e "última chamada", prazo 23h59; cada e-mail
  com dois assuntos e pré-header para teste A/B. Serve também para upgrade de categoria.
- **Semente de ingresso**: criativos, página de inscrição, grupo, lembretes e uma live (webinário ou "live direto ao ponto",
  sem replay, condição só ao vivo) que conta tudo sobre o evento e faz a oferta do ingresso. Ticket alto: rodar sem falar o
  preço e passar a mão levantada para o comercial vender no 1 a 1. Cuidado com criativo que confunde quem está comprando outro
  produto do expert ao mesmo tempo.
- Estruturas em `references/relampago-e-semente.md`.

### Passo 10. Time comercial (estratégia 6)
Abordar 1 a 1 as listas que as ações geram, da mais quente para a mais fria: carrinho abandonado, proteção de checkout,
inscritos das ações que não compraram, quem respondeu formulário/pesquisa, melhores notas de NPS. **Evento presencial: priorizar
pelo DDD da região.** A quem já comprou, perguntar se quer levar alguém e vender o 2º ou 3º ingresso. Sequência de 3 mensagens do
SDR (apresentação, vídeo do expert, CTA) salva no CRM. Rascunhos pela `ht-copy-anuncios-e-mensagens`; quem envia é o time do
expert, com OK do estrategista.

### Passo 11. Lives de aquecimento (estratégia 11)
Série de lives gratuitas antes do evento (2 por semana): **react** de palestras de edições anteriores comentadas por quem tem
resultado, **oficina** revisando material dos inscritos (uma oficina vendeu 46 ingressos, referência), ou **live de
conhecimento** do nicho. Grupo de inscritos que acumula de live em live; **pelo menos 3 pitches por live** (início, meio,
fim); no chat, "quem já tem o ingresso?" e depois a oferta aos que não têm; bônus exclusivo para inscritos (gravação dos reacts,
um guia). Roteiro em `references/lives-de-aquecimento.md`.

### Passo 12. Upsell e downsell (estratégias 7 e 10)
- **Upsell em outro produto**: página pós-compra do low ticket com contador e vídeo; o texto valida a compra anterior; o **botão
  só aparece no momento da oferta no vídeo** (antes gera compra sem entender e reembolso); "não, obrigado" leva ao próximo passo;
  depois, **upsell do upsell** (upgrade VIP). Uma decisão por vez.
- **Downsell no evento**: no último dia, antes da última palestra, oferecer o ingresso do próximo evento com condição especial
  (muitas vezes a gravação como bônus). O pitch no palco é da `ht-palestras-e-pitch`; aqui entram a oferta, o lote e o checkout.
- **Downsell do presencial para o online** (aula 19): nas duas últimas semanas, depois da "última chance" do presencial com o
  preço ancorado, uma live revela o ingresso online mais barato para quem não vai viajar. A transmissão não pode competir com o
  presencial: deixar claro que não haverá interação garantida. A aula não recomenda evento híbrido desde o início; só esse
  movimento final. Caso: ingresso online de R$ 297, 305 vendas e 14% desses compradores levaram o HT (referência, conferir).
- Estruturas em `references/upsell-e-downsell.md`.

### Passo 13. Página de vendas do ingresso
Estrutura observada nos eventos da aula: nome + promessa + Big Idea; escassez e botão; bastidor; data e local; networking;
o que aborda; prova social; tipos de ingresso; FAQ das objeções que o comercial devolve (a página cresce com elas); WhatsApp de
dúvida; vídeo do evento anterior; depoimentos; para quem é; palestrantes; lote e valor; hospedagem e transporte (parceria com
agência quando presencial). Detalhe em `references/perpetuo-e-pagina.md`. Execução: `ht-web-designer`.

### Passo 14. Rodar, medir e corrigir
Todo dia: relatório, velocidade, ação nova para amanhã. Semana a semana: qual estratégia vendeu, qual cortar, qual entrar.
Ao fim: auditoria (seção 6) e debrief em `13-aprendizados/` (vendas por estratégia, CAC por estratégia, comparecimento real).

## 4. Regras inegociáveis do método

1. Meta de ingressos e relatório diário desde o 1º dia; sem meta não se enxerga o ritmo.
2. Big Idea clara e testada; baixar preço não substitui Big Idea.
3. O evento aparece em todos os pontos de contato do expert; o expert vibra o evento.
4. Mais de uma estratégia; perpétuo sempre rodando; orgânico antes do pago.
5. Gratuito só com critério de avatar de HT.
6. Botão de upsell sincronizado com o vídeo; uma oferta por vez.
7. Lote zero não compete com outro lançamento para a mesma base.
8. O ingresso serve à venda do HT: custo de aquisição empatando o custo do evento já é vitória.
9. **Entrada do evento**: gratuita, credencial ou paga é decisão do estrategista por evento (quadro na seção 5).
10. Padrão do squad para planejar comparecimento (gratuito 25%, credencial/pago 70%, entrada no grupo 50%).
11. Campanha nasce PAUSADA com o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver; e-mail, disparo e mensagem a lead só com OK do estrategista; disparo em massa no
    WhatsApp só pela API oficial.

## 5. Quando a decisão é do estrategista

**Entrada do evento** (apresentar assim, com os números do projeto quando houver):

| Opção | Prós | Contras | Referência das aulas |
|---|---|---|---|
| Gratuita | custo por presente menor no histórico da FHT (catálogo, conflito 23); lista maior vira audiência | comparecimento baixo e imprevisível; precisa de confirmação dupla forte | aula 22: ~40% dos gratuitos comparecem (50% a 55% com muito esforço); para planejar, 25% (padrão do squad) |
| Credencial simbólica (ex.: R$ 97 com kit) | voto de comprometimento; sobe presença; cobre o kit | atrito na inscrição; exige checkout e comunicação clara | aula 24: ~90% de presença em imersões online de R$ 97/197 (relato, referência) |
| Paga (lotes) | receita que pode pagar o evento; presença alta | exige as estratégias desta skill e verba; vende menos cadeiras | pago pode passar de 100% com acompanhante |

Também são do estrategista: preço de cada tipo e lote; quantos gratuitos e para quem; oferta 2 por 1 ou desconto do 3º; datas de
virada de lote; verba de tráfego; quais estratégias do menu entram; enviar qualquer disparo para a base.

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Meta, data de início, velocidade e responsável escritos.
- [ ] Relatório diário modelado e grupo definido.
- [ ] Big Idea e nome com plano de teste.
- [ ] Decisão de entrada registrada; tipos, lotes e gratuitos com critério.
- [ ] 2 ou 3 estratégias + perpétuo com calendário, materiais e dono de cada peça.
- [ ] Mapa dos pontos de contato da base e um script por lista.
- [ ] Página de vendas com a estrutura completa e FAQ.
- [ ] Proteção de checkout e lista do comercial previstas.
- [ ] Nada enviado nem ativado sem OK.

**Auditoria final (erros típicos)**
1. Sem meta ou sem relatório diário (o alarme toca tarde demais)?
2. Big Idea fraca ou nome que confunde; preço baixado sem mexer na Big Idea?
3. Evento invisível na bio, nos fixados, na área de membros, no suporte?
4. Uma estratégia só?
5. Gratuito distribuído sem critério?
6. Lote zero sobreposto a outro lançamento ou começando tarde?
7. Criativo de lote zero dizendo "barato"?
8. Botão de upsell aparecendo antes da oferta; duas ofertas ao mesmo tempo?
9. Criativo do evento confundindo quem está comprando outro produto do expert?
10. Vendendo ingresso até a última semana a ponto de prejudicar a preparação das palestras?

## 7. Saída e handoff

- Grava em `05-eventos/<evento>/ingressos/` (agente `ht-ingressos-e-patrocinio`).
- Copy (página, e-mails, scripts, criativos) → `ht-diretor-copy` → `ht-copy-paginas-e-emails` / `ht-copy-anuncios-e-mensagens`
  → `ht-revisor-metodo-copy` (com compliance Meta nos anúncios).
- Página → `ht-web-designer` → `ht-revisor-visual`. Criativos → `ht-criativos-high-ticket` / `ht-designer`.
- Campanhas → `ht-gestor-trafego` (`10-trafego/`). Grupos, e-mails, disparos → `ht-gestor-automacoes` (`11-automacoes/`).
- Números → `ht-controller` (`07-numeros/`). Afiliados → `ht-afiliados-e-consultores`. Presença → `ht-captacao-e-presenca`.

## 8. Ferramentas de apoio

`email-marketing-mautic` (relâmpago e base), `conectar-whatsapp-oficial` (disparo por lista pela API oficial), `designer-senior-turbo`,
`pagina-design-premium`, `publicar-pagina-cloudflare` (página), `countdown-video` (contador do upsell e da virada de lote),
`ad-creative-video` e `hook-generator` (variações do criativo raiz), `hotmart-meta-conversao` (venda no pixel),
`analytics-dashboard` e `anthropic-skills:xlsx` (relatório diário), `avoid-ai-writing` e `humanizer`.

## 9. Fontes e lacunas

**Fontes**: trilha 17, Bootcamp Venda de Ingressos (aulas 21 a 34) e Bootcamp Lote Zero (aulas 13 a 20), relidas por inteiro
na revisão R8 (23/11/2026), transcrições em
`FORMULA HIGH TICKET/trilhas/17-execute-uma-imersao-online/`; `RESUMO-parte-A-planejamento-a-lote-zero.md` §3.2, §3.6 a 3.10,
§5.4 a 5.7, §7, §8; `RESUMO-parte-B-ingressos-e-patrocinio.md` §3.1 a 3.3, §4, §5.1 a 5.10, §7, §8; pasta
`_materiais/17-bonus-imersao-online/` (scripts de venda direta, e-mails do relâmpago, convites de react e oficina);
`_skills-mapa/parte-D` bloco 4; `CATALOGO-SKILLS-FHT.md` 5.4; Conflitos 22 e 23.

**Lacunas**: (1) o mapa mental das 11 estratégias, a planilha de cronograma de lotes e o pacote de materiais do lote zero não
foram capturados: os modelos daqui são reconstruídos; (2) o e-mail 2 do relâmpago não está na pasta; (3) o valor do ingresso do
caso de lote zero tem ruído (provável R$ 697, conferir); (4) os 6 vídeos de criativo da pasta de bônus não foram vistos;
(5) o "bootcamp de comparecimento" prometido na aula 22 não existe nas fontes; (6) não há regra de reembolso nem de termo de
ingresso.
