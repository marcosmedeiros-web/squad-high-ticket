# Metas, orçamento e ROAS do evento

Toda taxa abaixo é referência do método; o expert com histórico usa o dele.

## 1. Fórmula de trás para frente

```
ENTRADAS
  V   = vendas desejadas do HT (e, se houver, do downsell, à parte)
  c   = conversão sobre presentes ELEGÍVEIS (quem pode comprar)
  e   = fração de presentes que é elegível (tira equipe, aluno ativo do HT, convidado de outro programa; sem dado: 0,95)
  a   = comparecimento sobre quem preencheu a confirmação tipo 1 (T1)
  f   = fração de inscritos que preenche o T1 (perda de ~20% entre inscrição e formulário: f ≈ 0,80)
  CPL = custo por lead (sobre T1, como o método mede)
  O   = leads orgânicos esperados (listas, base, parceiros), estimativa

CONTAS
  presentes elegíveis  Pe = V / c
  presentes            P  = Pe / e
  T1 necessários       T  = P / a
  inscritos            I  = T / f
  leads pagos          Ip = max(0, T - O)
  verba de captação    Vc = Ip x CPL
  verba total          Vt = Vc / 0,80     (reserva de ~20% para lembrete, remarketing e API)
  dias de captação     d  (online: 19 a 32 dias nos exemplos)
  verba diária         Vc / d
```

Checagem de capacidade: P no pico cabe na sala? Zoom até ~100 sem atrito; acima de ~500 muda plano e operação. Presencial: sala
para P, e confirmação mirando 110% a 120% do desejado (técnica do método para evento gratuito).

## 2. Taxas de referência (montar 3 cenários)

| Taxa | Conservador | Base | Otimista | De onde vem |
|---|---|---|---|---|
| Comparecimento, gratuito (sobre T1/inscritos) | 20% | 25% a 30% | 33% | referência do método; padrão do squad = 25% |
| Comparecimento, credencial ou pago | 60% | 70% | ~100% | padrão do squad = 70%; IMA de referência: pagantes ~100% |
| Conversão IMI online 1 dia, venda no evento | 1,5% | 5% | 10% | caso de referência 1,5% a 2% (ticket ~R$ 80 a 100 mil); média de casos 5% a 10%; caso isolado >10% |
| Conversão IMA online | 2% | 3% | 5% | IMA online de referência: ~2,8% sobre ~1.100 presentes (conferir) |
| Conversão presencial 3 dias | 14% | 18% a 20% | 25% | IMA presencial de referência 18,58% sobre elegíveis; faixa de referência 14% a 25% |
| LDP | 2% | 3% | 5% | referência |
| Agendamento de sessão após pitch sem preço (IMI) | 20% | 34% | 45% | edição 2: 97 de ~280 no pitch (34%), 79 realizadas, 13 vendas; edição 3: 81 de 178 (~45%), 64 realizadas, 14 vendas |

Leitura do conflito: conversão do online é cerca de metade da do presencial; ticket mais alto, conversão mais baixa. Nunca
usar como meta a taxa de uma live anterior com demanda reprimida (caso de referência: 14% na live; planejar bem abaixo).

Série de imersões online de 1 dia de um caso de referência (conferir):

| Edição | Inscritos | Presentes | No pitch | Fechamento | Resultado |
|---|---|---|---|---|---|
| edição 1 | ~1.000 | 432 | ~300 | venda no evento | 6 vendas, ~R$ 480 mil, ~R$ 5 mil investidos (maior parte API) |
| edição 2 | 1.345 | 335 | ~280 | pitch sem preço → sessão de avaliação | 97 agendaram (34%), 79 sessões, 13 vendas, ~R$ 1,04 mi |
| edição 3 | n/d | n/d | 178 | sessão de avaliação | 81 agendaram (~45%), 64 sessões, 14 vendas, ~R$ 1,12 mi |
| edição 4 | ~1.300 | n/d | ~280 | sessão de avaliação | projeção de ~10 vendas (fechamento em curso) |

Leitura: o modelo com sessão de avaliação repetiu o resultado em três edições e foi conduzido por time de vendas, não pelos
experts (processo de venda um-para-muitos delegável). No online, medir a conversão sobre presentes e também sobre presentes
no momento do pitch (reportar os dois). Ticket do caso de referência: R$ 80 a 100 mil, avatar sem consciência da oportunidade, por
isso as taxas baixas; produto de consciência alta tende a converter mais.

## 3. Orçamento de referência

| Exemplo | Verba | CPL | Período | Leads | Presentes alvo |
|---|---|---|---|---|---|
| Mínimo sugerido (caso 1) | R$ 3.000 | R$ 8 | 19 dias, R$ 126/dia | 300 | ~100 |
| Mínimo recomendado (caso 2) | R$ 4.500 (= 300 x CPL de planejamento R$ 15; a planilha separa R$ 3.600 captação + R$ 900 distribuição dos Reels, conferir) | R$ 15 para planejar (caso de referência ~R$ 12,50) | 32 dias, R$ 113/dia | 300 | 100 |
| meta mínima do método para imersão online | n/a | R$ 10 de média para planejar | n/a | 300 inscritos | 100 ao vivo |
| Imersão online de referência | ~R$ 25 mil | R$ 19 geral (R$ 24 a 25 só Meta) | n/a | 1.324 | pico 334 |
| Imersão presencial de referência | > R$ 100 mil a R$ 500 mil | até R$ 120 | n/a | n/a | n/a |

Faixa de verba do online de 1 dia : mínimo ~R$ 4.500, de R$ 4.500 a R$ 10 mil o normal, teto de
~R$ 20 mil (é o máximo do caso de referência; acima disso o pico passa do plano da sala, ~300 no Zoom, e acima de ~500 exige
duas contas). Sem verba, compensar no orgânico (listas, Reels com CTA, e-mail, LinkedIn); com verba, os dois. Parte do
orçamento pode ir para disparo pela API oficial a listas que já existem (custo por lead da API no lugar do CPL do tráfego).
Plataforma: Meta Ads; Google Ads não é recomendado para verba desse tamanho (curva de aprendizado longa e cara).
Faixa de CPL vista em casos: R$ 3 a R$ 50. "Verba de guerra": primeira campanha com algo que não comprometa a empresa (R$ 5 a
10 mil citados); a primeira tende a sair pior. Conta nova no Meta libera gasto aos poucos. Campanha sempre nasce PAUSADA, com
o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver, e só ativa com OK do estrategista.

## 4. Projeção de ROAS e margem (reconstrução do squad)

O método calcula, antes de cada imersão, presentes esperados, no-show, ticket médio, faturamento bruto, quanto entra no caixa,
custo do evento e imposto, até a margem. A planilha não foi baixada; campos abaixo são a reconstrução do squad:

```
presentes esperados (P) · elegíveis (Pe) · conversão (c) · vendas = Pe x c
ticket médio (02-oferta: mix à vista / parcelado / dupla, citar versão)
faturamento em contrato = vendas x ticket médio
recebido no período = contrato x % que entra em caixa no horizonte (o GPS usou 50% como hipótese; Master Plan conservador também)
receita de ingresso / downsell (se houver)
custos: tráfego + API/mensagens + estrutura (local, som, LED, staff, viagem) + equipe + ferramentas
imposto sobre o recebido (alíquota do expert; sem dado: [FALTA])
margem = recebido + ingressos - custos - imposto
ROAS de contrato = contrato / custos ; ROAS de caixa = recebido / custos
```

Referências de resultado (conferir): IMA presencial de referência ~R$ 2,67 mi de faturamento total com ~R$ 500 mil de custo; IMA online de referência
~R$ 1,26 mi com ~R$ 60 mil; lote zero de ingresso ROAS 14; IMI online citada com ROAS ~28 (ruído). Regra prática: se sobram
20% a 30% depois de pagar tudo, o botão está funcionando; se a margem aperta, ajustar o parafuso que está pior.

## 5. Relatório diário de captação (campos)

dia · leads do dia · T1 do dia · gasto · CPL · desvio da meta diária · acumulado x meta · entrada no grupo (%) · criativo
vencedor · ação de amanhã. Planilhado D-1 (com um dia de atraso), mesmo com dashboard, para reaproveitar o criativo vencedor.
