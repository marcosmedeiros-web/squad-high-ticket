# Prontidão, arquitetura e custos

## 1. Prontidão (sim/não com evidência)
| Pré-requisito | Evidência | Sim/Não |
|---|---|---|
| Oferta encaixada (vende com regularidade) | Central 1x1, conversão com N ≥ 20 | |
| Metodologia clara | jornada e entregáveis em 02-oferta | |
| Manual de entregáveis escrito (por entregável a avaliar) | 06-entrega/manual | |
| Roteiro oficial da sessão de venda escrito | 03-sessao/roteiro | |
| Vai delegar entrega ou venda (ou já delegou) | mentores/closers ativos | |
| Reuniões em Meet, Zoom ou Teams, com calendário | | |
Qualquer "não" nos três primeiros = não montar agora.

## 2. Contas necessárias (criadas pelo dono, nunca pelo agente)
Google (Calendar, Drive, Sheets) · Fireflies (gratuita basta; fechar a tela do trial Pro no X) · n8n (nuvem com 14 dias grátis ou servidor próprio)
· OpenRouter (pré-pago, 2FA, chave com limite diário) · canal de alerta (decisão assumida no padrão, listada em "Assumi"). Cartão virtual com limite recomendado
na aula.

## 3. Custos de referência (referência, conferir no ato)
| Item | Valor citado | Observação |
|---|---|---|
| n8n nuvem | R$ 125/mês (anual) ou R$ 150/mês | 2.500 execuções/mês; 1 reunião = 1 execução |
| n8n em servidor próprio | ~R$ 35/mês | instalação simples, manutenção e atualização por sua conta |
| OpenRouter | créditos de teste US$ 5-10 | cobrança por token; sem acréscimo sobre o preço do modelo |
| Por reunião real (duas IAs, Gemini 2.5 Flash) | ≈ US$ 0,03-0,04 (≈ R$ 0,20; até R$ 0,30 se longa) | valor de referência, conferir |
| Z-API (alerta WhatsApp) | ~R$ 100/mês por número | API não oficial, só alerta interno |
| Fireflies | gratuito | Pro não é necessário |
Tempo de montagem citado: ~3 h na primeira vez, 30 min na segunda, 15 min na terceira.

## 4. Escolha do modelo
Critérios: contexto longo (reunião de 1h a 2h), preço de entrada baixo, saída estável em JSON. A referência usa Gemini 2.5 Flash para
reunião longa (contexto ~1 milhão de tokens; preço citado ~US$ 0,30 por milhão de entrada e US$ 2,50 de saída) e citou GPT-4o mini
como mais barato porém com contexto de 128 mil. Na montagem: abrir o comparador de modelos do OpenRouter, escolher o equivalente
atual, registrar nome, preço e data em `arquitetura.md`. Regra: tarefa mecânica com modelo barato, tarefa de alto valor
com modelo melhor.

## 5. Desenho para o expert (preencher)
- Tipos de reunião e prioridade: [diagnóstico, reunião estratégica, sessão 1a1 de venda...]
- Uma planilha por tipo (ou abas), um par de prompts por tipo, separação por Switch (título da reunião com padrão de nome).
- Padrão de nome da reunião no calendário (necessário para o Switch e para o Append or Update): ex. "[tipo] - [aluno] - [mentor]".
- Destinatários do alerta: [padrão assumido; listar em "Assumi"]. Limiar: 70 (padrão de referência) ou [decisão].
