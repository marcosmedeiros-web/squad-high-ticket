# Planilha de avaliação e mensagens de alerta

## 1. Colunas (aula 5), uma aba por tipo de reunião
Nome da reunião · Data · Duração · Participantes · Link da transcrição · Nota geral · Resumo · [Etapa 1] status · [Etapa 1]
observação · [Etapa 2] status · [Etapa 2] observação · ... (todas as etapas do prompt) · Revisada por humano? · Nota humana ·
Ação (refazer, feedback, ok) · Responsável.
As quatro últimas são acréscimo do squad para calibração e acompanhamento.
Casamento do "Append or Update": coluna Nome da reunião (por isso o padrão de nome no calendário).

## 2. Mensagens (montadas na aula 6; texto final revisado; envio só com OK do estrategista)
Erro do fluxo:
```
ATENÇÃO: erro no fluxo de avaliação.
Erro: {{mensagem do erro}}
Fluxo: {{nome do workflow}}
```
Nota baixa:
```
ATENÇÃO: reunião com nota baixa.
Nota: {{nota geral}}
Reunião: {{nome da reunião}}
Link: {{URL da transcrição}}
Participantes: {{participantes}}
```
Destino: só equipe interna definida pelo estrategista. Nunca o aluno ou o lead.

## 3. Calibração (registro)
| Rodada | Reunião | Nota IA | Nota humana | Diferença | Problema visto | Ajuste (prompt/modelo) | Data |
Critério do squad para pedir o OK de produção: ≥ 5 reuniões reais com diferença ≤ 10 pontos e nenhuma etapa classificada ao contrário.
