---
name: ht-master-plan
description: 'Squad High Ticket / método FHT. Monta o Master Plan do expert: aba PRODUTOS HT, projeção conservadora de 7 anos por HT (novos, ticket, renovação, margem), contrato x recebido x líquido, número mágico (vendas por mês e por semana), plano anual por canal (frequência x volume x conversão) com funil reverso da sessão 1a1, calendário de eventos e ciclos de renovação, LTV e escada, capacidade de entrega e auditoria da planilha. Gera a planilha corrigida (xlsx) com script próprio. Use quando o estrategista disser "monta o master plan", "projeta 7 anos", "quanto esse HT fatura?", "qual o número mágico?", "quantas sessões por semana ele precisa?", "o plano fecha?", "confere a planilha do master plan". NÃO usar para definir preço ou oferta (ht-preco-pagamento-e-garantia, 02-oferta), para o financeiro da agência ou do dono (fora do escopo deste squad) nem para metas de lançamento LPSG (Turbo).'
---

# Master Plan (7 anos, número mágico e plano por canal)

## 1. Para que serve e o que entrega

Dá ao expert e ao estrategista a visão de longo prazo do negócio HT: o que cada produto pode faturar em 7 anos com premissas
conservadoras, quantas vendas por mês isso exige agora, de quais canais elas vêm e se a entrega aguenta. No método, o Master Plan
é obrigatório antes do plano de ação e é revisado linha a linha nele; dá resiliência quando uma sessão ou um evento vai mal.

**Entrega** (em `experts/<slug>/ht/07-numeros/`):
1. `AAAA-MM-DD-master-plan-<slug>.xlsx`, gerado por `references/gerar_master_plan.py` (abas PREMISSAS, PRODUTOS HT, PLANEJAMENTO
   7 ANOS, NÚMERO MÁGICO, CAPACIDADE; amarelo = entrada, o resto é fórmula).
2. `AAAA-MM-DD-master-plan-leitura.md`: premissas com fonte, três cenários (conservador, base, otimista) em tabela, leitura do
   resultado (acumulado, líquido, ano a ano), número mágico, plano por canal do ano 1 e se ele fecha, funil reverso, calendário
   anual proposto, capacidade, riscos, linha "Assumi" e o que precisa de dado próprio.
3. `AAAA-MM-DD-master-plan-entrada.json` (os números usados, para regenerar a planilha a cada revisão).

## 2. Antes de começar

- Carregar `ht-protocolo`. Conferir pedido em `00-plano/pedidos/`.
- Ler: `02-oferta/portfolio.md` (HTs, ordem, gatilhos, aba PRODUTOS HT) e `02-oferta/oferta-vigente.md` (ticket, condições,
  duração, versão); `01-pesquisa/` (avatar, base existente, média de preço do nicho); `07-numeros/` (Central 1x1, conversão real,
  comparecimento real, recebimento real, versões anteriores do plano); `06-entrega/` (capacidade, mentores); `00-plano/decisoes.md`.
- Entradas obrigatórias (não abrir questionário: o que faltar é assumido pelo padrão e listado em "Assumi"; só perguntar o impossível de adivinhar, no máximo 2 coisas por vez, em linguagem simples):
  1. **Ticket de cada HT** de `02-oferta`. Se não existir ainda, usar R$ 10 mil (referência do método) marcado **provisório** e
     dizer que o plano será refeito quando a oferta for aprovada. O preço oficial só nasce na Aprovação 1.
  2. **Meta do expert para o ano 1** ou a pergunta-guia "com que faturamento no fim do ano ele fica tranquilo?" e quantas
     sessões por semana ele (ou o time) consegue fazer.
  3. **Base existente**: alunos ativos que podem renovar no ano 1 e dados reais de conversão, comparecimento e recebimento.
  Sem essas respostas, gerar com as referências e listar como lacuna.

## 3. Passo a passo

### Passo 1. Premissas (aba PREMISSAS)
Preencher com fonte em cada número (`references/planilha-e-auditoria.md`, seção 4):
- Ano inicial; horizonte de 7 anos.
- **% de recebimento** sobre o contrato: dado real da Central 1x1/financeiro; sem dado, 80% (referência da live 054; cancelamento
  de 20% a 30% citado nas lives 040 e 052).
- **Margem (lucro) sobre o recebido**: 40% (padrão do squad), ou seja, **custo de 60% do recebido**. Conta: líquido =
  recebido x 0,40; custos = recebido x 0,60. Atenção ao rótulo do modelo da FHT: lá a linha se chama "margem de custo" e o
  número digitado é o % de custo (a aula usa 40% de custo); o squad decidiu ser mais conservador e o script recusa a chave antiga.
- **Renovação**: 50% (padrão do squad) até haver dado próprio.
- **Capacidade**: expert sozinho até 20 alunos ativos; mentor 1:70; navegador 1:100 (padrão do squad).
Dado próprio do expert, quando existe, substitui a referência e isso é dito na leitura.

### Passo 2. Aba PRODUTOS HT
Copiar do portfólio (`02-oferta/portfolio.md`): até 3 HTs, cada um com o que é, para quem é, Roma, ticket (com versão de
`02-oferta` ou "provisório") e **canais de venda** (onde se faz a oferta: 1a1, SHT, imersão com pitch, lançamento; captação não é
canal de venda). Sem portfólio, devolver ao Diretor pedindo `ht-portfolio-e-escolha-do-ht`.

### Passo 3. Projeção de 7 anos por HT (aba PLANEJAMENTO 7 ANOS)
Regras de preenchimento (método FHT, detalhe na referência):
1. Ano 1 de pé no chão, conferido semana a semana ("consigo 1 por mês? 2? 1 por semana?").
2. Crescimento realizável de 20% a 25% ao ano nos novos (ou outra curva declarada); conferir se o ano 2 não é menor que o 1.
3. Ticket por ano: o de `02-oferta`; subir ticket nos anos seguintes só como cenário, marcado "hipótese de reajuste" (o preço oficial só nasce na Aprovação 1).
4. Renovação: ano 1 só sobre a base existente; dos anos seguintes, sobre o total de clientes do ano anterior.
5. Ticket de renovação: sem regra fixa, definido por projeto (menor, igual ou reajuste). Montar o cenário base com o mesmo ticket da venda (`preco_renovacao` do padrão) e listar em "Assumi"; as outras
   alternativas (menor, reajuste) entram só como cenário, com o efeito no acumulado.
6. HT 2 (GIC, upgrade) e HT 3 (EHT, pós, imersão de implementação cobrada) começam no ano do gatilho do portfólio; GIC com regras
   em aberto (a skill usa `regras_gic` do padrão e lista em "Assumi") entra como cenário. EHT e produtos sem acompanhamento com `conta_capacidade: false`. HT com margem diferente
   (ex.: EHT com custo de viagem) leva `margem_sobre_recebido` próprio no JSON, sempre como margem de lucro, com a fonte na leitura.
7. Gerar: `python3 references/gerar_master_plan.py entrada.json saida.xlsx` (exemplo com `--exemplo`). Recalcular antes de ler
   (abrir no Sheets/Excel ou `soffice --headless --convert-to xlsx`) e conferir uma coluna à mão.
8. Três cenários: conservador (conversão e renovação no piso), base (premissas do squad), otimista (teto das referências).
   Apresentar o conservador como o plano; os outros como sensibilidade. "Se o conservador agrada, o resto é lucro."

### Passo 4. Número mágico
Aba NÚMERO MÁGICO: novos do ano ÷ 12 (por mês) e ÷ 52 (por semana). Escrever a frase do expert: "para bater o ano 1 preciso de N
vendas por mês, isto é, uma a cada X dias". Fixar a data da primeira venda.

### Passo 5. Plano do ano 1 por canal
Para cada canal de venda do portfólio: frequência no ano x volume por vez x conversão = vendas previstas
(`references/plano-anual-canais-e-caixa.md`, seção 3). Referências do squad: sessão 1a1 com conversão de 10% a 20% (padrão
do squad); presença em evento gratuito 25%, credencial ou pago 70% (padrão do squad); imersão online cerca de 5% dos
presentes. Somar e comparar com a meta de novos. **Plano que não fecha não é plano**: ou aumenta frequência/volume, ou entra outro
canal (só com oferta validada em 1a1), ou a meta do ano 1 é revista. Primeiro canal é o 1a1; um-para-muitos depois de validar.

### Passo 6. Funil reverso da sessão 1a1
Preencher `funil_1a1.vendas_mes_1a1` no JSON com as vendas por mês que o plano por canal atribui ao 1a1. Vendas por mês do 1a1 ÷ conversão = sessões realizadas; ÷ comparecimento (75% de referência real da live 051) = agendamentos;
÷ 4,3 = sessões por semana. Conferir com a disponibilidade dada pelo expert (2 a 3 sessões por dia útil é a referência da
Central 1x1). Se não cabe na agenda, isso vai para as decisões (time comercial, mais canais, meta menor). Lembrar o mínimo de 20
sessões antes de mexer em preço ou filtro (padrão do squad).

### Passo 7. Calendário anual de eventos e ciclos
Propor o calendário do ano: meses de 1a1 (cerca de 6 meses antes do primeiro evento online, se o expert está sozinho), imersões
(o ciclo se repete 5 a 7 vezes por ano quando maduro), SHT na cauda de cada imersão, ciclos de renovação casados com os
presenciais (programa de 12 meses, ajustável de 11 a 13, ciclo casado a um encontro presencial), datas de revisão do Master Plan. **Calendário e feriados**:
conferir cada mês e cada data proposta contra feriados nacionais, Carnaval, Semana Santa, recesso de fim de ano (24/12 a 01/01) e
datas do nicho; evento ou live que cai num deles é deslocado para a data livre mais próxima, listado em "Assumi" (data pública pede o OK simples). Portão de cada evento um-para-muitos
em D-15 da data dele (`ht-protocolo` §3.6). Entregar como proposta ao
`ht-gestor-projetos` (dono de `00-plano/cronograma.md`); formato e entrada de cada evento ficam com `ht-decisao-de-evento` (a entrada segue `entrada_imersao`, listada em "Assumi").

### Passo 8. Caixa, LTV e capacidade
- Mostrar contrato, recebido e líquido por ano e acumulados; explicar "efeito farmácia" e propor a reserva (Open Doors) como
  sugestão listada em "Assumi", sem número de divisão inventado.
- LTV por cliente (novos + renovação + upgrade previsto) e CAC máximo aceitável como conta, não como meta de tráfego.
- Aba CAPACIDADE: se os ativos passam de 20, o plano precisa de mentor e navegador no ano em que isso acontece; levar para
  `ht-escala-da-entrega`.

### Passo 9. Auditoria e leitura
Rodar a auditoria (seção 6) e escrever a leitura: o que o plano diz, o que depende de quê, o que é provisório, quando revisar.

## 4. Regras inegociáveis do método

- Projeção conservadora; faturamento não é dinheiro no bolso (margem de lucro sempre preenchida: 40% sobre o recebido, custo 60%); contrato não é recebido.
- Ticket só de `02-oferta` (ou referência de R$ 10 mil marcada provisória). O plano nunca define preço nem reajuste.
- Só células de entrada são editadas; fórmula não é sobrescrita. Planilha da FHT copiada tem os defeitos da referência corrigidos.
- Imersão é canal de venda, não HT (salvo ingresso de implementação de valor alto, declarado no portfólio). Captação não é canal
  de venda. GIC só depois de resultado. Um público por plano.
- Primeiro canal: sessão 1a1. Um-para-muitos só com oferta validada.
- O plano é vivo: revisado no plano de ação, depois de cada 20 sessões, de cada evento e de cada ciclo de renovação, com número
  real; versão anterior vai para `historico/`.
- Números de aula são referência: na leitura, cada um com fonte e "conferir" quando houver ruído.
- Padrões aplicáveis (editáveis em `padroes` do perfil): preço vem da oferta (5x a 10x a média do nicho); programa de 12 meses,
  ajustável de 11 a 13; preço da renovação definido por projeto (proposto pelo padrão e listado em "Assumi"); entrada de evento pelo padrão; regras
  do GIC em aberto; conversão de referência da sessão de 10% a 20%; mínimo de 20 sessões antes de concluir; renovação de 50% e
  margem de 40% sobre o recebido no plano conservador; capacidade de 20 alunos com o expert sozinho, mentor 1:70, navegador
  1:100; comparecimento de 25% no gratuito e 70% no credencial ou pago.

## 5. O que a skill decide e lista em "Assumi"

Decidir pelo padrão ou pela recomendação, sem lote de perguntas, mostrando o efeito no acumulado e listando em "Assumi: X, Y, Z (é só pedir para mudar)"; vira oficial na aprovação do plano:
- **Ticket de renovação**: igual ao da venda (padrão); menor ou reajuste só como cenário.
- **Meta do ano 1** quando a do expert não fecha com os canais ou com a agenda.
- **Entrada de novos canais** (imersão, SHT, lançamento) e o mês em que entram: propor pelo ciclo do calendário.
- **Quando abrir o GIC** e com qual ticket: pelo padrão `regras_gic`.
- **Contratação** (vendedor, mentor, navegador) quando o funil reverso ou a capacidade pedirem: só sugerir; contratar pede o OK simples ("posso seguir?").
- **Reserva de caixa** (Open Doors) e divisão do lucro: sugerir sem número inventado.
- Usar dado próprio do expert que contradiz a premissa do squad (ex.: renovação real de 30%): usar o dado próprio e dizer isso em "Assumi".

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Planilha gerada e recalculada; uma coluna conferida à mão e registrada na leitura.
- [ ] Margem conferida numa célula à mão: líquido = 40% do recebido e custos = 60% (padrão do squad), nunca o contrário.
- [ ] Toda premissa com fonte (dado próprio, decisão do squad ou aula marcada referência/conferir).
- [ ] Ticket igual ao de `02-oferta` (versão citada) ou marcado provisório.
- [ ] Três cenários, com o conservador como plano.
- [ ] Número mágico (mês e semana) e data da primeira venda.
- [ ] Plano por canal do ano 1 com a diferença para a meta e o que fazer se for negativa.
- [ ] Funil reverso do 1a1 comparado com a agenda real.
- [ ] Calendário anual proposto, conferido contra feriados e recesso, com o portão de cada evento em D-15, e enviado ao gestor
      de projetos.
- [ ] Capacidade conferida; contrato x recebido x líquido explicados.
- [ ] Linha "Assumi" em linguagem simples e "posso seguir?"; bloco de entrega preenchido.

**Auditoria final**: rodar os 14 itens de `references/planilha-e-auditoria.md`, seção 5 (imersão como HT, captação como canal,
dois públicos, GIC sem resultado, produto de entrada como AR, ticket baixo para público profissional, renovação sem motivo, metas
invertidas, margem vazia ou sobre contrato, fórmula quebrada, Roma vaga, ticket fora de 02-oferta, capacidade estourada, plano por
canal que não fecha). Na leitura, dizer quais foram conferidos e o que foi corrigido.

## 7. Saída e handoff

- Grava em `07-numeros/` (dono: `ht-controller`). Quando executada por outro agente (estrategista de produto, gestor de projetos),
  entrega a proposta ao `ht-controller`, que grava.
- Revisão: `ht-revisor-metodo-copy` (método e leitura). O Diretor leva à pessoa com o "Assumi" e o "posso seguir?".
- Próximos: `ht-gestor-projetos` (calendário em `00-plano/cronograma.md`), `ht-central-e-kpis` (metas da Central 1x1 e painel),
  `ht-escala-da-entrega` (mentores), `ht-decisao-de-evento` (eventos do calendário), plano de ação do expert.

## 8. Ferramentas de apoio (por nome)

`references/gerar_master_plan.py` (planilha corrigida; requer `openpyxl`), `anthropic-skills:xlsx` (ajustes e leitura de planilha
do expert), LibreOffice `soffice --headless` (recalcular para conferir), `analytics-dashboard` (painel, quando o estrategista pedir),
`hotmart-meta-conversao` e a ferramenta de tráfego do perfil, `trafego.ferramenta` (só leitura, para trazer vendas e custo real ao plano), `avoid-ai-writing` (leitura).

## 9. Fontes e lacunas

**Fontes**: trilha 07 (Bootcamp MasterPlan: RESUMO e aulas 01 a 12 lidas por inteiro na revisão de 23/11/2026; planilha
`07-descricao__1AEUAfPQ.xlsx` lida fórmula a fórmula); rota3 resumo 09 e transcrição `09-bootcamp-master-plan` (é a mesma
gravação do bootcamp da trilha 07, conferida por comparação de trechos); live 054 lida por inteiro (contrato x recebido x lucro); `rota3/materiais/planilhas/master-plan.xlsx`;
lives 001, 006, 025, 027, 031, 032, 040, 051, 052, 054, 055; parte A, E, G, H, I do catálogo (master plan, auditoria, plano anual,
calendário, caixa, LTV); padrões do squad.

**Lacunas**: a FHT não define regra de % de recebimento para planejar (80% é leitura de exemplos de live); o padrão do squad é margem (lucro) de 40% sobre o recebido, isto é,
custo de 60%; a aula usa 40% de custo (margem de 60%) e a live 054 cita cerca de 50% de lucro sobre o recebido, então o plano do
squad fica abaixo das duas referências de propósito; premissas de renovação divergem nas fontes (30% a 90%); o mapa mental do bootcamp não está nos arquivos;
números do ecossistema, do LTV e da escada têm ruído de legenda; não há modelo FHT de calendário anual nem de planilha de plano
por canal (as abas NÚMERO MÁGICO e CAPACIDADE são do squad); o script foi testado com dados de exemplo, não com um expert real.
