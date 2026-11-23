# Controle e métricas do agendamento e do follow-up

Referência da `ht-agendamento-e-follow-up`. Complementa a Central 1x1 (colunas-base em `ht-slg`, `references/agente-ia-e-delegacao.md`).
O consolidado e o painel são do `ht-central-e-kpis` em `07-numeros/`.

## 1. Colunas extras para a Central 1x1

| Coluna | Valor |
|---|---|
| Origem do sim | SLG / página / aula semanal / aplicação / Kinder Ovo / outro |
| Data e hora do sim (ou da inscrição) | |
| Data e hora do 1º contato | (minutos até o contato = diferença) |
| Respondeu a notificação? | Sim / Não |
| Horários oferecidos | 2 horários |
| Agendada para | Data e hora (dias até a sessão = diferença) |
| Lembretes enviados | V (véspera) · M (manhã) · 5 (5 min) · S (sala) · L (ligação) |
| Compareceu? | Sim / Não |
| Nº de reagendamentos | |
| Aplicação | Não se aplica / enviada / paga / aprovada / reprovada / devolvida |
| Data de retorno combinada na sessão | |
| Toques de follow-up | Datas e canais |
| Objeção final | Texto curto (onde nasceu) |
| Status | Agendado · realizado · converteu · follow-up · encerrado · repescagem em [data] |

## 2. Métricas por micro-etapa

| Etapa | Métrica | Referência de aula (conferir) |
|---|---|---|
| Notificação | Tempo até o 1º contato; % que responde | Contato em minutos; ligação em até 30 min |
| Agendamento | % de quem respondeu que agenda; dias até a sessão | Sessão em até 2 dias (decisão 17) |
| Comparecimento | Compareceram / agendados | 70% a 80%; no-show até 20% |
| Venda | Converteram / realizadas | 10% a 20% (decisão 6); < 5% aciona diagnóstico de conversão |
| Follow-up | Vendas vindas do follow-up / follow-ups abertos | Sem referência nas fontes |

Relatório por pessoa que agenda (modelo de live): leads recebidos, abordagens, respostas, agendamentos, comparecimentos, por
dia, semana e mês, com a taxa de comparecimento contra a meta.

## 3. Diagnóstico do gargalo

| Sintoma | Onde olhar primeiro |
|---|---|
| Muita inscrição, pouca resposta | Notificação: tempo, número sem foto, texto longo, link cru |
| Responde, mas não agenda | Agendamento: horários abertos demais, data longe, valor da sessão mal vendido |
| Agenda e falta | Formalização e lembretes: confirmação em pergunta, sem lembrete da manhã, sem ligação na hora |
| Comparece e não compra | Sessão: `ht-roteiro-sessao-1a1`, `ht-objecoes`, `ht-treino-comercial` |
| Muitos "vou pensar" que somem | Retorno não marcado na sessão; follow-up tardio; sem aplicação ou sinal |

Amostra: avaliar processo novo de agendamento com pelo menos ~12 agendamentos (número de plantão, conferir); conversão só com
20 sessões (decisão 7). Até lá, registrar e corrigir o óbvio, sem conclusões estatísticas.
