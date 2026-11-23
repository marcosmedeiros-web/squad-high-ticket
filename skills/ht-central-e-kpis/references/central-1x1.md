# Central 1x1: estrutura, fórmulas e correções

Modelo do SLG e modelo do Funil de Reels, unificados pelo squad.

## 1. Versão unificada do squad (aba "Central 1A1", cabeçalho na linha 12, dados a partir da 13)

| Col | Campo | Tipo / lista |
|---|---|---|
| C | Nome (+ @ do perfil) | texto |
| D | Origem do Lead | lista: Tráfego, Bônus, Social, Orgânico, Outbound (validação do modelo) |
| E | Desarmadora | Sim/Não (1ª mensagem do SLG; só versão SLG) |
| F | Condução | Sim/Não |
| G | Arremate | Sim/Não |
| H | Sessão Agendada? | Sim/Não |
| I | Sessão Realizada? | Sim/Não |
| J | Data da Sessão | data |
| K | Oferta à Vista | R$ (de 02-oferta) |
| L | Oferta Parcelada | R$ (de 02-oferta) |
| M | Fazer Follow Up | data |
| N | Status Conversão | lista: Converteu, Não converteu (vazio = em aberto) |
| O | Valor do Contrato | R$ |
| P | Anotações da Negociação | texto |
| Q | Objeções Identificadas | texto curto padronizado (alimenta ht-objecoes) |
| R | Link Raio X | URL |

Definições de origem: Social = abordado pelo SLG; Orgânico = veio sozinho; Outbound = prospecção totalmente fria; Bônus =
sessão dada como bônus; Tráfego = anúncio. No desafio, a orientação para iniciantes foi "coloca tudo SLG".

## 2. Indicadores (bloco "Acompanhamento Geral", linhas 5 a 10) com fórmula corrigida

| Indicador | Fórmula recomendada (intervalo 13:1008) | O que o modelo faz |
|---|---|---|
| Leads gerados | `=COUNTIF(C13:C1008,"<>")` | igual |
| Sessões agendadas | `=COUNTIF(H13:H1008,"Sim")` | igual |
| Comparecimento | `=IFERROR(COUNTIFS(I13:I1008,"Sim",H13:H1008,"Sim")/COUNTIF(H13:H1008,"Sim"),0)` | igual na v14; v10 sem IFERROR |
| Conversão da sessão (geral) | `=IFERROR(COUNTIFS(N13:N1008,"Converteu",I13:I1008,"Sim")/COUNTIF(I13:I1008,"Sim"),0)` | v10: realizadas ÷ convertidas (invertida, dá >100%); v14: convertidas ÷ leads (é lead→venda, não sessão) |
| Conversão lead → venda | `=IFERROR(COUNTIF(N13:N1008,"Converteu")/COUNTIF(C13:C1008,"<>"),0)` | é o que a v14 chama de "geral" |
| Conversão por origem (sessão) | `=IFERROR(COUNTIFS(N13:N1008,"Converteu",D13:D1008,"Social",I13:I1008,"Sim")/COUNTIFS(D13:D1008,"Social",I13:I1008,"Sim"),0)` (uma por origem) | v14 igual; v10 divide por leads da origem |
| Faturamento total (K4) | `=SUMIFS(O13:O1008,N13:N1008,"Converteu")` | v14 igual (SUMIFS só de "Converteu"); v10 usa `SUM(O:O)`, que soma valor digitado em linha não convertida (no próprio exemplo do modelo dá 79.005, com 20.005 de linhas "Não converteu") |
| Faturamento médio por sessão realizada | `=IFERROR(K4/COUNTIF(I13:I1008,"Sim"),0)` (K4 = faturamento total) | as duas dividem por agendadas |
| Custo médio por agendamento | `=IFERROR(('Tráfego Funil de Sessão 1A1'!D3+'Tráfego Funil de Reels com CTA'!D3)/COUNTIF(H13:H1008,"Sim"),0)` | v10 divide por leads de tráfego; v14 correta |
| Custo médio por venda | `=IFERROR(('Tráfego Funil de Sessão 1A1'!D3+'Tráfego Funil de Reels com CTA'!D3)/COUNTIF(N13:N1008,"Converteu"),0)` | v14 correta; v10 divide só pelas vendas de origem Tráfego |

Nomes das abas: as fórmulas de custo usam os nomes do modelo do Funil de Reels entre aspas simples; se renomear a aba, trocar na
fórmula. Na conversão por origem, a origem pode vir de uma célula de rótulo (ex.: `$H6`), como faz a v14, em vez do texto fixo.

**Teste de aceitação (LibreOffice headless, fórmulas acima numa planilha de teste):**
6 linhas de teste: A Social agendou, realizou, Converteu, 30.000 · B Tráfego agendou, realizou, Converteu, 25.000 · C Social
agendou, realizou, Não converteu, valor 5 digitado por engano · D Tráfego agendou, realizou, status vazio · E Orgânico agendou,
não realizou · F Social não agendou. Aba de sessão: 30 leads, R$ 600 investidos; aba de Reels: 160 seguidores, R$ 400.
Resultado esperado e obtido: leads 6 · agendadas 5 · comparecimento 80% (4/5) · conversão da sessão 50% (2/4) · lead → venda 33%
(2/6) · conversão Tráfego 50% (1/2 realizadas) · Social 50% (1/2) · faturamento 55.000 (com `SUM` daria 55.005: por isso SUMIFS) ·
faturamento por sessão realizada 13.750 · custo por agendamento R$ 200 (1.000/5) · custo por venda R$ 500 (1.000/2) · custo global
por seguidor R$ 2,50 (400/160; a média das linhas do modelo daria R$ 6,00). Nenhuma taxa acima de 100%.
Na entrega ao estrategista, repetir este teste no arquivo gerado (ou um equivalente) e apagar as linhas de teste depois.

## 3. Abas de tráfego
- "Tráfego Funil de Sessão 1A1": Data · Quantidade de leads · Investimento do dia · Custo por lead (`=IFERROR(D/C,0)`); totais em
  C3 (leads), D3 (investido), E3 (CPL médio = D3/C3).
- "Tráfego Funil de Reels com CTA": Nome dos Reels · Link · Status (ATIVO/AGUARDANDO) · Estilo (CTA) · Data de início · Seguidores ·
  Investimento · Visitas ao perfil · Alcance · Custo por seguidor (`=H/G`). Total global: usar `=D3/C3` (investido ÷ seguidores);
  o modelo usa a média dos custos por linha, que distorce.
- Dados de gasto: só leitura pela ferramenta de tráfego do perfil (`trafego.ferramenta`; ex.: `meta ads insights get` na Meta Ads CLI oficial); nada é criado ou alterado em campanha.

## 4. Aba "Calc HT" (calculadora de tráfego)
Entradas: valor gasto, CPM, CTR, connect rate, taxa de conversão da página. Calcula impressões, cliques, acessos, CPC e CPA.
Métricas esperadas impressas no arquivo (sem explicação de origem, conferir): CTR acima de 1%; connect rate acima de 80%; conversão
da página "acima de 70%". Ações sugeridas no arquivo: alinhar expectativas; testar públicos maiores; melhorar gancho do criativo;
melhorar carregamento mobile; alinhar criativo e página. Leitura de tráfego é do ht-gestor-trafego (ht-trafego-high-ticket).

## 5. Regras de preenchimento
- Linha nasce na abordagem (ou no lead de tráfego), não na sessão.
- Atualizar no mesmo dia; follow-up com data.
- Valor do contrato = valor fechado, não a oferta.
- Uma linha por pessoa; dupla numa linha com observação.
- Dado de lead não sai da pasta do projeto.
