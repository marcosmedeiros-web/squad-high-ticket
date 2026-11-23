---
name: ht-central-e-kpis
description: 'Squad High Ticket / método FHT. Monta e opera a gestão de números do HT: Central 1x1 (planilha white label do FHT, uma linha por lead, com as fórmulas corrigidas), funil comercial em microetapas, produtividade de SDR e closer, funil reverso (meta de vendas → leads, sessões e pessoas), painel de KPIs do programa (conversão por canal e origem, recebimento, consumo, NPS, renovação, Toques de Midas, custo por agendamento e por venda), diagnóstico pelas 4 alavancas (aquisição, retenção, upgrade, renovação + gestão) e a rotina do expert para executar o plano (mapa de atividades, time block, ciclos de compromisso). Use quando o estrategista disser "monta a Central 1x1", "como estão os números", "onde o funil trava", "quantos leads preciso", "painel do programa", "qual alavanca atacar", "o expert não tem tempo". NÃO usar para dashboard de lançamento LPSG da Turbo.'
---

# Central 1x1 e KPIs do HT

## 1. Para que serve e o que entrega

Dá ao estrategista e ao expert uma leitura única dos números do HT e a próxima ação que mais gera crescimento. Começa simples (a
Central 1x1 do ciclo de sessões) e cresce para o painel do programa e o diagnóstico por alavanca.

**Entrega** (conforme o pedido), em `experts/<slug>/ht/07-numeros/`:
1. `central-1x1-<expert>.xlsx`: Central no modelo FHT, já com as fórmulas corrigidas e a aba de tráfego (inclui Reels).
2. `leitura-da-central-<data>.md`: taxas por etapa e por origem, gargalo, próxima ação, alerta de amostra pequena.
3. `funil-reverso.md` (ou aba): meta de vendas → sessões → agendamentos → leads → abordagens → pessoas/horas.
4. `produtividade-time.xlsx`: relatório de SDR e closer por dia, semana e mês contra meta.
5. `painel-kpis.md` (+ planilha ou página): indicadores do programa com fonte, referência e semáforo.
6. `diagnostico-4-alavancas-<data>.md`: métricas por alavanca, gargalo e UMA ação recomendada.
7. `rotina-do-expert.md`: mapa de atividades, time block semanal, rituais e ciclo de compromisso.

## 2. Antes de começar

- Carregar `ht-protocolo`. Pedido do Diretor conferido.
- Ler: `02-oferta/` (ticket, entrada, parcelas: para faturamento e projeções), `03-sessao/` (registros de sessões, objeções),
  `04-demanda/` e `10-trafego/` (gasto de mídia de sessão e de Reels), `06-entrega/` (NPS, consumo, catálogo, controle de
  renovação), `07-numeros/` (Master Plan, número mágico, metas), `13-aprendizados/`.
- Entradas obrigatórias: para a Central, a lista de leads/sessões (ou começar vazia); para funil reverso, a meta de vendas do
  período e o ticket; para o painel, as fontes disponíveis. Se faltar, não abrir questionário: assumir o padrão (meta do
  Master Plan e ticket da oferta vigente; Central começando vazia numa planilha; o expert operando sozinho) e listar em
  "Assumi" (regra 16 do `ht-protocolo`). Perguntar só o que for impossível de adivinhar (por exemplo, onde estão hoje os
  registros de leads e sessões), no máximo 2 coisas por vez e em linguagem simples.

## 3. Passo a passo

### Passo 1. Central 1x1 (base de tudo no canal de sessão)
Estrutura do white label FHT e correções em `references/central-1x1.md`. Resumo:
- **Uma linha por lead**: Nome (com o @ do perfil) · Origem (Tráfego, Bônus, Social, Orgânico, Outbound) · Desarmadora · Condução ·
  Arremate (as 3 mensagens do SLG, sim/não) · Sessão agendada? · Sessão realizada? · Data da sessão · Oferta à vista · Oferta
  parcelada · Fazer follow-up (data) · Status conversão (Converteu / Não converteu) · Valor do contrato · Anotações da negociação ·
  Objeções identificadas · Link do Raio-X.
- Origem: "Social" = abordado pelo SLG; "Orgânico" = veio sozinho (mandou mensagem, conteúdo); "Outbound" = prospecção totalmente
  fria; "Bônus" = sessão dada como bônus (Kinder Ovo); "Tráfego" = anúncio.
- **Acompanhamento geral**: leads gerados, sessões agendadas, comparecimento, conversão geral, conversão por origem, faturamento
  total, faturamento médio por sessão, custo médio por agendamento e por venda.
- Há **duas versões** do white label: a do SLG (trilha 10, com as colunas das 3 mensagens) e a do Funil de Reels (trilha 14, sem
  elas, com aba de tráfego de sessão e aba de Reels). As duas têm fórmulas com erro (a do SLG dá conversão de 125% no exemplo, o
  sinal de "conferir fórmula se passar de 100%" das aulas). Usar a versão unificada com as fórmulas corrigidas da referência e
  dizer ao estrategista o que mudou.
- Custo por agendamento e por venda soma o tráfego da sessão **e** o dos Reels turbinados (versão da trilha 14 já faz isso).
- Preenchimento: no mesmo dia da abordagem e da sessão; objeções em texto curto padronizado (alimenta ht-objecoes).

### Passo 2. Ler a Central (ciclo da sessão)
- Referências do protocolo: conversão de sessão 10% a 20% (padrão do squad); abaixo de 5% aciona diagnóstico de conversão
  (ht-treino-comercial). Comparecimento: medir; referência de live 75% a 80% (conferir).
- **Amostra mínima**: não concluir sobre produto, preço ou filtro antes de 20 sessões (25 no desafio). Análise de vendas pelo mentor
  depois de 5 sessões. Sempre dizer "N sessões" ao lado de cada taxa.
- Volume de referência: 10 sessões por semana fora do desafio, 2 a 3 por dia útil; SLG de lista fria 100 abordagens → 20 reuniões
  → 1 venda (pessimista; lista quente precisa de menos).
- Gargalo por etapa (funil de 6 métricas do 1a1): leads → contactadas → retornos → agendadas → compareceram → converteram. A etapa
  com a maior queda contra a referência é o gargalo; a ação vai para a skill dona (mensagem → ht-slg; agendamento e no-show →
  ht-agendamento-e-follow-up; conversão → ht-roteiro-sessao-1a1 / ht-treino-comercial; pouco lead → ht-reels-com-cta,
  ht-trafego-high-ticket).
- Comparar conversão **por origem** antes de decidir onde pôr energia e verba.

### Passo 3. Funil comercial em microetapas e produtividade do time
Detalhe em `references/funil-reverso-e-produtividade.md`.
- Microetapas: lead → notificação (recebe, abre, lê, responde) → agendamento (convencimento, confirmação) → comparecimento
  (lembrete, sessão) → venda (pitch, script, fechamento) → pós-venda (recebimento, retenção) → entrega.
- Relatório de produtividade: cada SDR/closer registra leads, abordagens, respostas, agendamentos, comparecimentos, sessões e vendas;
  cálculo por dia, semana e mês e taxa contra meta; link de compra rastreado por vendedor (comissão).
- Erro real citado: 500 a 600 leads por semana e só 7 a 10 agendamentos (o gargalo era o contato, não o lead).

### Passo 4. Funil reverso (meta → esforço)
- Partir da meta de vendas do período (número mágico) e das taxas **próprias** do expert; sem dado próprio, usar as do protocolo e
  marcar "premissa".
- Exemplo ilustrativo de live (não é meta): 10 vendas/mês a 10% = 100 sessões; 50% de comparecimento = 200 agendamentos; 50%
  qualificam = 400; 50% geram = 800 leads. A própria live diz que a real ficou em 22% a 25% de conversão e 75% a 80% de
  comparecimento (conferir).
- Converter sessões em horas e pessoas: sessão 1a1 com alvo de 1h15 e teto de 1h30 (padrão do squad) + preparo; o expert solo
  vende até ~5 por semana (referência); acima disso, time comercial (ht-treino-comercial), só depois de processo validado.

### Passo 5. Painel de KPIs do programa
Lista completa, fonte e referência em `references/painel-kpis-e-alavancas.md`. Grupos:
- **Aquisição**: leads por origem e canal, custo por lead, agendamento, comparecimento, conversão por canal (1a1, aula semanal, SHT,
  imersão), faturamento por sessão, CAC por canal, ROAS de evento, origem de quem compra.
- **Caixa**: contrato x recebido, taxa de recebimento por parcela, inadimplência, cancelamento (contrato ≠ recebido).
- **Retenção e entrega**: consumo de entregáveis, NPS por entregável e por mentor, cancelamento por mês de programa, alunos travados.
- **Resultado**: alunos por faixa de resultado, Toques de Midas disponíveis, resultados novos no catálogo.
- **Renovação e upgrade**: aptos, confirmados, presentes, renovados (presentes x ausentes), elegíveis a upgrade, upgrades.
- Semáforo: verde/amarelo/vermelho contra a meta do Master Plan ou a referência do protocolo; cada KPI mostra a fonte e o "N".
- O material do FHT não descreve um painel pronto: o painel é síntese do squad sobre as métricas citadas (dizer isso).
- Formato: planilha (`anthropic-skills:xlsx`) ou página interna (`analytics-dashboard`), nunca pública.

### Passo 6. Diagnóstico pelas 4 alavancas
1. Pergunta fixa: **"qual ação gera mais crescimento agora?"**
2. Para cada alavanca, as métricas: aquisição (leads, agendamento, comparecimento, conversão); retenção (cancelamento, consumo,
   resultado, NPS); upgrade (elegíveis por marco, ofertas, conversão); renovação (ciclos definidos, oferta, taxa); gestão (margem,
   recebimento, caixa) como 5ª.
3. Ordem típica de quem está começando: aquisição no 1a1 → entrega → retenção → upgrade e renovação.
4. Escolher **uma** ação, com dono, prazo e métrica de execução e de resultado. As demais ficam em fila.
5. Exemplo de raciocínio do FHT: se 100 alunos chegam ao marco, há 100 elegíveis a upgrade; resultado gera upgrade e evita
   cancelamento (live 052).

### Passo 7. Rotina do expert para executar o plano
Modelo em `references/rotina-do-expert.md` (sala colab dez/25 e mai/25):
- Fases: estabilizar, otimizar, crescer.
- Mapa de atividades (atividade, domínio, tipo recorrente/espontânea/pontual/contínua, etapas, duração, cadência, quando termina).
- Time block com 4 tipos de bloco: específicos, genéricos, reserva (~2 h/dia) e abertos; âncoras primeiro; tarefa cognitiva de manhã.
- Rituais: revisão diária de 5 min (só registrar) separada do planejamento semanal.
- 5 sistemas: captura, organização, acompanhamento, revisão, planejamento; notificações desligadas.
- Ciclos de compromisso de 1 semana a 90 dias: 1 estratégia, 1 métrica de execução (ex.: 10 sessões por semana) e 1 de resultado
  (ex.: 2 vendas por mês).
- Comprar tempo de volta: valor da hora do expert; delegar na ordem administrativo → entrega → marketing → vendas → liderança.
- Pergunta do 10x para achar a alavanca.
- Agenda e lembretes reais do expert não são criados por esta skill sem pedido e OK.

## 4. Regras inegociáveis do método

1. Toda sessão e todo lead entram na Central; sem registro não há diagnóstico.
2. Taxa sem "N" não vale; menos de 20 sessões é tendência, não conclusão.
3. Contrato ≠ recebido: faturamento do painel mostra os dois.
4. Custo por agendamento e por venda inclui todo o tráfego que trouxe o lead (sessão e Reels).
5. Uma ação por diagnóstico, ligada à alavanca de maior crescimento.
6. Número de aula é referência; a meta vem do Master Plan do expert.
7. Dado de lead e aluno fica na pasta do projeto; painel não é publicado.
8. Mudança de preço, de filtro ou de oferta a partir dos números: proposta ao estrategista, nunca alteração direta.

## 5. O que a skill decide e o que pede OK

A skill decide pelo padrão ou pela recomendação e lista em "Assumi: X, Y, Z (é só pedir para mudar)": metas do período (se divergirem
do Master Plan, segue o Master Plan), qual alavanca vira prioridade quando o diagnóstico empatar (a de maior efeito), mudança de preço
ou filtro depois das 20 sessões (vira proposta na aprovação do plano). Pede o OK simples ("posso seguir?"): contratação de
SDR/closer e remuneração, verba de tráfego para cobrir o funil reverso, compartilhar o painel com o expert ou o time.

## 6. Critério de pronto e auditoria final

**Pronto quando**:
- [ ] Central com as 16 colunas, listas de origem e status, fórmulas corrigidas e conferidas com um caso de teste (nenhuma taxa acima
  de 100%).
- [ ] Leitura com taxa por etapa e por origem, "N" de cada uma, gargalo e próxima ação com skill dona.
- [ ] Funil reverso com as taxas marcadas (próprias ou premissa).
- [ ] Painel com fonte e referência por KPI e semáforo.
- [ ] Diagnóstico com uma ação, dono, prazo e duas métricas.
- [ ] Rotina com time block, rituais e ciclo de compromisso.

**Auditoria (erros típicos)**:
1. Conversão acima de 100% (fórmula invertida do white label).
2. Faturamento médio por sessão dividido por agendadas em vez de realizadas; faturamento somando valor de linha não convertida
   (usar SUMIFS por "Converteu").
3. Custo por agendamento dividido por leads.
4. Origem preenchida errado ("social" para quem veio sozinho).
5. Concluir com 5 ou 7 sessões; mudar preço antes de 20.
6. Olhar só o total, sem origem e sem canal.
7. Muito lead e pouco agendamento atribuído ao anúncio, quando o gargalo é contato.
8. Contrato tratado como caixa.
9. Painel com 30 indicadores e nenhuma ação.
10. Rotina sem bloco de reserva (tudo vira urgência).

## 7. Saída e handoff

- Grava em `07-numeros/` (dono: ht-controller; ht-gestor-projetos usa a rotina e as metas em 00-plano).
- A Central é alimentada pelo ht-sdr e pelo ht-closer (rascunho de registro; eles não falam com lead) e lida pelo ht-treinador-comercial.
- Leitura e diagnóstico → Diretor (que junta o "Assumi" e pede o "posso seguir?") e skill dona do gargalo. Textos → **ht-revisor-metodo-copy**;
  painel visual → **ht-revisor-visual**.
- Automação de coleta (formulários → planilha) → ht-gestor-automacoes, só com OK do estrategista.

## 8. Ferramentas de apoio

`anthropic-skills:xlsx` (Central, funil reverso, produtividade), `analytics-dashboard` (painel interno), a ferramenta de tráfego do perfil (`trafego.ferramenta`) e
`meta-ads-cli-turbo` (gasto e leads de tráfego, só leitura), `hotmart-meta-conversao` (vendas e recebimento), `ht-avaliacao-de-reunioes-por-ia`
(nota das sessões como KPI de qualidade).

## 9. Fontes e lacunas

**Fontes**: white labels "Central 1A1" (`_materiais/planilhas/10-social-lead-generation__16k_wVG3.xlsx`, abas Central 1A1, Tráfego,
Calc FHT, Dados; e `14-funil-de-reels__1fc_XB-P.xlsx`, com Tráfego Funil de Sessão 1A1 e Tráfego Funil de Reels com CTA; lidas célula
a célula); Notion `notion-5a20.txt` (trilha 10 e 14); trilha 10 e desafios (RESUMO-desafio-30d-*:
origem, outbound, metas de 20/25 sessões); parte-A (central e ciclo 100-20-1), parte-B (operador da central), parte-C (painel e aba de
Reels), parte-E (registrar calls, sala colab de tempo), parte-G (calculadora de sessões, time block), parte-H (número mágico, painel de
KPIs), parte-I (funil em microetapas, produtividade, funil reverso, plano anual, alavancas); lives 038, 040, 043, 051, 052.

**Lacunas**: (1) não existe painel de KPIs pronto no material (síntese do squad); (2) referências da aba "Calc FHT" (CTR acima de 1%,
connect rate acima de 80%, conversão de página "acima de 70%") estão no arquivo sem explicação em aula: conferir antes de usar;
(3) números do funil reverso e de comparecimento são de live, conferir; (4) não há método de cobrança e inadimplência além de
"70% a 80% de recebimento" citado; (5) as duas versões da Central divergem em colunas e fórmulas; a versão unificada é do squad.
