---
name: ht-webinario-de-vendas
description: 'Webinário de vendas do Squad High Ticket (método FHT). Monta o webinário recorrente (semanal ou quinzenal) que vende o HT por aplicação ou call, não por checkout, em duas variantes da FHT: o webinário com apresentador (abertura, aula e pitch de ~90 min, dúvidas) e o ciclo de 2 aulas com Score de Risco (aula 1 diagnóstico, aula 2 mapa e oferta). Entrega plano do ciclo, roteiro bloco a bloco, pitch para aplicação/call, captação qualificadora, confirmação, operação comercial pós-live, painel de métricas e plano anti-saturação. Use quando o estrategista disser "quero um webinário pra vender a mentoria", "monta o webinário semanal", "aula 1 e aula 2 com score de risco", "meu webinário saturou". NÃO usar para aula semanal sem oferta (ht-aula-semanal), live direto ao ponto (ht-live-direto-ao-ponto), imersão, nem lançamento pago semanal/5+1 (Turbo).'
---

# Webinário de vendas HT (método FHT)

## 1. Para que serve e o que entrega

Webinário HT é uma **live de vendas recorrente** cujo objetivo não é vender no checkout, e sim gerar **aplicações ou calls**
que o time comercial fecha. É replicável e simples (de casa ou do hotel; depois pode rodar gravado com apresentador ao vivo).
É um canal entre vários (sessão 1a1, imersões), útil quando a oferta já foi validada em 1a1 e o expert quer escala sem evento.

Duas variantes do método:
- **A. Webinário com apresentador** (palestra de webinários semanais, fev/2026): apresentador (2 min) + vídeo de abertura
  (2 min) + aula e pitch do expert (~90 min) + apresentador tirando dúvidas de inscrição (~10 min).
- **B. Ciclo de 2 aulas com Score de Risco** (palestra "R$ 500 mil a cada 15 dias", fev/2026): duas aulas longas no Zoom em
  dias seguidos, a cada 15 dias, sem parar o tráfego; aula 1 é o diagnóstico (laudo de risco), aula 2 é o mapa, a oferta e a
  decisão; quem dá entrada faz entrevista de qualificação. **Atenção à fonte:** os slides chamam o ciclo de "lançamento pago a
  cada 15 dias" e a tese é comprar atenção aceitando prejuízo planejado no front-end (entrada paga) para vender o HT depois.
  Não é o lançamento pago semanal da Turbo (não tem 5+1, a oferta é a do AR com o pitch do FHT), mas a entrada das 2 aulas
  (paga ou gratuita) é decisão do estrategista (seção 5); se for paga, a captação é de Vendas/Purchase, não de Leads.

**Entrega** (em `experts/<slug>/ht/05-eventos/AAAA-MM-webinario-<nome>/`, dono: ht-produtor-eventos):
1. **Plano do ciclo**: variante, cadência, datas, promessa e nome, meta de leads/presentes/aplicações/calls/vendas (conta de trás
   para frente), equipe (apresentador, closers), ferramentas.
2. **Roteiro bloco a bloco** com tempos, objetivo de cada bloco, objeções que quebra, provas usadas e CTA de aplicação/call
   (molde em `references/roteiro-e-operacao.md` ou `references/ciclo-2-aulas-score-de-risco.md`).
3. **Pedidos às skills vizinhas**: página e confirmação (`ht-captacao-e-presenca`), criativos (`ht-criativos-high-ticket`),
   campanha (`ht-trafego-high-ticket`), pitch (`ht-palestras-e-pitch`), call (`ht-roteiro-sessao-1a1`), agendamento
   (`ht-agendamento-e-follow-up`).
4. **Painel de métricas e plano anti-saturação** (`references/metricas-e-saturacao.md`).

## 2. Antes de começar

1. Carregar `ht-protocolo`. Portão: Aprovação 1 e **oferta validada em 1a1** (mínimo de 20 sessões, padrão do squad, com
   conversão de referência). Webinário com oferta não validada amplifica o erro.
2. Ler em `experts/<slug>/ht/`: `02-oferta/` (oferta, preço, entrada, garantia vigentes), `03-sessao/` (roteiro da call, Raio-X,
   objeções, conversão real), `01-pesquisa/` (as 5 objeções principais, avatar comprador), `04-demanda/` (lista, aula semanal),
   `05-eventos/` (calendário, para não colidir com imersão ou SHT), `07-numeros/` (metas e verba), `10-trafego/` (CPL histórico),
   `13-aprendizados/`.
3. Entradas obrigatórias e perguntas (máximo 3):
   - "Quem fecha as calls e quantas por semana o time aguenta?" (capacidade define o teto do webinário)
   - "Variante A (aula + pitch numa live) ou B (2 aulas com Score de Risco)? Semanal ou quinzenal?"
   - "O preço aparece no webinário ou só na call?" (decisão do estrategista, seção 5)

## 3. Passo a passo

### Passo 1. Decidir variante, cadência e capacidade
- Começar **quinzenal**, não semanal; fazer **ao vivo muitas vezes antes de automatizar** (pulos do gato da palestra).
- Variante A para nichos em que uma aula + pitch basta para levar à call; variante B quando a decisão é pesada e o avatar precisa
  enxergar o risco de errar sozinho antes de ouvir a oferta.
- Capacidade comercial: calls esperadas = presentes × 10% (agendam) × 80% (comparecem). Se o time não absorve, reduzir captação
  ou ampliar o time antes de subir verba.

### Passo 2. Conta de trás para frente
`references/metricas-e-saturacao.md` §1. Vendas desejadas → calls (÷ 40% de conversão) → agendamentos (÷ 80%) → presentes
(÷ 10%) → inscritos (÷ 15% a 25% de comparecimento) → leads qualificados (≥ 40% dos inscritos) → verba (× CPL histórico).
Todos esses percentuais são de uma palestra (mercado LATAM, tickets de ~R$ 10 a 20 mil): **referência**, trocar pelo dado
próprio depois de 2 ou 3 webinários.

### Passo 3. Promessa, nome e captação qualificadora
- Promessa no destino do avatar (Roma), com nome de aula atrativo; mudar nome e copy a cada 3 a 6 meses quando a performance cair.
- **Comunicação qualificadora**: criativo e página falam com o perfil de quem compra (ICP), não com o curioso; formulário de
  inscrição com 1 a 2 perguntas de qualificação (faturamento, momento, especialidade). Meta de lead qualificado > 40%.
- Páginas, formulário e tags: pedido para `ht-captacao-e-presenca`; criativos para `ht-criativos-high-ticket`; campanha para
  `ht-trafego-high-ticket` (Leads, sobe PAUSADA).
- **Confirmação como numa imersão online** (pulo do gato): página de obrigado com próximo passo, grupo ou canal de avisos,
  lembretes D-1, dia e 1 h antes. Envio a lead só liga com OK do estrategista.

### Passo 4. Roteiro
- **Variante A** (`references/roteiro-e-operacao.md` §1): abertura do apresentador (quem é o expert, o que a pessoa vai sair
  sabendo, regras da sala) → vídeo de abertura (autoridade: trajetória, provas, cases) → aula com 3 a 5 blocos de conteúdo que
  quebram as objeções principais sem entregar o "como" → transição → pitch para a aplicação/call → dúvidas de inscrição com o
  apresentador, repetindo o link.
- **Variante B** (`references/ciclo-2-aulas-score-de-risco.md`): aula 1 diagnóstico (5 pilares do Score de Risco = 5 objeções,
  vazio intencional, filtro do avatar de maior potencial) e aula 2 mapa (revisão, "o que eu vendo de verdade", planos A/B/C,
  pré-pitch, pitch, decisão, silêncio).
- O pitch segue o pitch do FHT (`ht-palestras-e-pitch`), adaptado: o CTA é **aplicar ou agendar**, não comprar. Variante de
  pitch para call em 3 tempos (antecipação com escassez real, história, oferta da reunião com o especialista) em
  `references/roteiro-e-operacao.md` §2.
- Responder dúvidas no chat até o fim (a variante B fecha muito dentro da própria live).
- Revisão: roteiro passa pelo `ht-revisor-metodo-copy` antes de ir ao expert.

### Passo 5. Operação comercial pós-live
- Link de aplicação/agendamento no chat, na tela, no e-mail e no grupo; **contato em minutos** com quem aplicou (ligação ou
  mensagem em até ~30 min; agendar para o mesmo dia ou o seguinte; padrão do squad: 2 horários, sessão em até 2 dias).
- Agendamento com regras de corte (não agenda quem não tem perfil ou não pode decidir agora; os dados ficam para contato
  posterior). Quem não agendou entra na repescagem de `ht-agendamento-e-follow-up`.
- Call: roteiro da sessão (`ht-roteiro-sessao-1a1`; versão de 6 etapas, padrão do squad; VSD como variante) com o Raio-X;
  sinal com a call aberta; ordem do preço entrada, parcelado, à vista.
- Variante B: quem dá entrada faz **entrevista de qualificação** (aprovação do candidato) antes de entrar.
- Tudo registrado na Central 1x1 com origem "webinário <data>".

### Passo 6. Medir, renovar e só então automatizar
- Painel por edição (`references/metricas-e-saturacao.md` §2) e debrief em `13-aprendizados/`.
- Anti-saturação: anúncios novos a cada 2 webinários (no mínimo), visualmente diferentes (ambiente, formato: ponto de vista,
  podcast, tela dividida), teste constante de páginas, nome e copy novos a cada 3 a 6 meses.
- Automatizar (gravado) só depois de várias edições ao vivo estáveis, com **apresentador ao vivo** abrindo e tirando dúvidas.

## 4. Regras inegociáveis do método

- Um-para-muitos só com oferta validada em 1a1; webinário não é lugar de testar oferta.
- Venda por aplicação ou call, com time comercial treinado; webinário não substitui a sessão.
- Conteúdo quebra objeção e mostra o "o quê" e o "porquê", nunca o "como" completo (quem sai saciado não aplica).
- Preço, entrada, parcelas, bônus e garantia saem de `02-oferta/`; nada é improvisado no ao vivo.
- Escassez real (vagas = capacidade de entrega e de agenda); nada de urgência fabricada.
- Integridade na decisão: a palestra da variante B usa uma moldura de responsabilidade moral e família no fechamento; o
  catálogo alerta que isso exige cuidado. Nesta skill: falar do custo real de continuar no mesmo lugar, sem culpa nem medo
  manipulado, e nunca em tema de saúde ou dívida de forma que constranja.
- Replay: a fonte não traz regra para webinário; não liberar replay por padrão e levar a decisão ao estrategista (seção 5).
- Não misturar com a aula semanal (que não tem oferta) nem com o SHT (venda direta para lista com demanda reprimida).

## 5. Quando a decisão é do estrategista

- **Preço no webinário ou só na call**: a) preço só na call, com inscrição para a call aberta a quem quer saber (recomendo no
  começo; uma palestra de jun/2026 relata que abrir a call para quem queria saber o preço lotou a agenda) · b) preço dito no
  pitch com planos (variante B mostra investimento e planos no Dia D) · c) faixa de investimento sem o número.
- **Variante e cadência** (A x B; semanal x quinzenal) e dias da semana.
- **Entrada das aulas da variante B** (mesma lógica da entrada de evento, decisão do estrategista): a) gratuita com cadastro qualificado (Leads; mais volume, menos
  compromisso; é a forma da variante A) · b) paga, como no case dos slides (Vendas/Purchase; o ingresso paga parte do tráfego e
  filtra, mas exige página de venda, checkout e aceitar prejuízo no front) · c) credencial de baixo valor. Sem a escolha
  escrita do estrategista, a skill não monta a captação da variante B.
- **Ao vivo x gravado** e quando automatizar.
- **Replay**: sem replay (força presença) x replay curto para inscritos.
- **Verba de captação** por edição e ativação das campanhas.
- **Oferta em 3 planos** (A/B/C) só se `02-oferta/` tiver os três aprovados.

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Oferta validada em 1a1 registrada (número de sessões e conversão) e capacidade comercial calculada.
- [ ] Conta de trás para frente feita, com os percentuais marcados como referência.
- [ ] Roteiro completo com tempos, objeções, provas (com fonte) e CTA de aplicação/call repetido.
- [ ] Pedidos de página, confirmação, criativos e campanha emitidos às skills vizinhas.
- [ ] Fluxo pós-live (aplicação → contato em minutos → call → sinal) desenhado e testado.
- [ ] Painel e plano anti-saturação prontos; decisões do estrategista listadas.

**Auditoria (erros típicos):**
1. Webinário montado antes de 20 sessões e conversão conhecida?
2. Captação genérica que enche a sala de curioso (lead qualificado < 40%)?
3. Aula que ensina o "como" inteiro e mata a aplicação?
4. Pitch que manda para checkout quando a venda é por call?
5. Lead que aplicou esperando 2 a 3 dias para ser chamado?
6. Agenda aberta para quem não tem perfil, lotando o closer de call sem chance?
7. Mesmos anúncios, nome e página por meses (saturação)?
8. Fechamento com culpa, medo ou escassez falsa?
9. Preço ou condição diferente de `02-oferta/`?
10. Automatizou antes de estabilizar ao vivo?

## 7. Saída e handoff

- Gravar em `05-eventos/AAAA-MM-webinario-<nome>/` (plano, roteiro, painel por edição). Debrief de cada edição em `13-aprendizados/`.
- Handoff: `ht-revisor-metodo-copy` (roteiro, pitch, copy) · `ht-captacao-e-presenca` (página, confirmação, lembretes) ·
  `ht-criativos-high-ticket` e `ht-gestor-trafego` (captação) · `ht-closer` e `ht-agendamento-e-follow-up` (calls) ·
  `ht-gestor-automacoes` (tags, disparo de aplicação) · `ht-diretor-arte` (slides, vídeo de abertura) · `ht-controller` (painel).

## 8. Ferramentas de apoio

`gerador-slides-turbo` ou `slides-uipm-turbo` (slides da aula), `hyperframes` ou `remotion` (vídeo de abertura),
`lower-thirds` (nome do expert e apresentador), `countdown-video` (lembrete "é hoje"), `email-marketing-mautic` e
`automacao-fluxos` (confirmação e lembretes, só com OK), `anthropic-skills:xlsx` (painel), `transcrever-youtube-turbo` e `watch`
(rever gravação da edição para corte de trecho que derruba retenção).

## 9. Fontes e lacunas

**Fontes:** `RESUMO-palestras-encontros-fht.md`, seções de fev/2026 "Webinários semanais para venda de HT no mercado Latam"
(roteiro, 3 diferenças do lançamento, 5 pulos do gato, saturação, métricas, ferramentas) e "A arquitetura por trás de R$ 500 mil a
cada 15 dias" (ciclo de 2 aulas, Score de Risco); jun/2026 "Os 3 funis que geraram ~R$ 700 mil" (pitch para call em 3 etapas,
agendamento imediato, agenda condicional); catálogo `fht-webinario-semanal-ht` e `fht-webinar-2-aulas-score-de-risco`;
padrões do squad.

**Lacunas (não inventar):** as duas palestras só têm **slides** (o vídeo não tem transcrição): exemplos de comunicação
qualificadora, ecossistema típico, slides de engenharia reversa e de pré-pitch da variante B estão em imagem; não há roteiro
falado do pitch do webinário nem texto de lembretes; os números são de mercado LATAM e de cases do palestrante (tickets de
US$ 2 a 3 mil), não do Brasil; não há regra sobre replay; o "filtro do milhão" é descrito só no título do slide; o preço e a
forma de cobrança da entrada da variante B não estão nos slides (só "lançamento pago" e "prejuízo planejado no front").
Conferido na revisão de 23/11: os arquivos das palestras de fev/2026 e jun/2026 em `trilhas/23-materiais-extras/` estão
vazios (sem transcrição); esta skill continua apoiada só no resumo dos slides.
