# Rubrica de auditoria de sessão 1a1 gravada

Arquitetura (status por etapa, observação com timestamp, nota 0-100 com peso por etapa, alerta de nota baixa, calibração com uma
sessão que deve reprovar e outra que deve passar): padrão do método. Etapas e critérios: roteiro de 6
etapas e erros comuns de laboratório. **Os pesos abaixo são proposta da skill** (o método só diz que as
etapas de maior peso eram as de conteúdo e oferta e que a apresentação perde no máximo 10 pontos, para a sessão de entrega);
calibrar com o estrategista depois das primeiras 5 auditorias.

## 1. Formato do relatório
```
Sessão: [data] · [iniciais do lead] · conduzida por [quem] · duração [hh:mm] · resultado [vendeu / não / follow-up em …]
Amostra: sessão N de M já auditadas
| Etapa | Status | Observação (com mm:ss) | Correção e fundamento |
Tempos reais x referência
Objeção final: [frase] · nasceu em [etapa] · poderia ter sido quebrada em [etapa]
Nota geral: [0-100] · Alerta: [sim se < 70]
3 ajustes de maior impacto
Próximo treino
```

## 2. Etapas, critérios e pesos propostos

| Etapa (peso) | Cumprida quando |
|---|---|
| 1 Boas-vindas (10) | quebra-gelo sem venda; uma pergunta inicial aberta + escuta; apresentação e objetivo sem método nem oferta |
| 2a Raio-X (15) | escala e "não precisa justificar" explicados; perguntas no formato; notas ≤3 aprofundadas; contradições tratadas; palavras anotadas; urgência; ~20 min |
| 2b Leitura do gráfico (15) | área boa → 3 piores com consequência e palavras do lead → 12 meses → "faz sentido?" → permissão; sem solução |
| 3 Herói relutante (10) | 6 passos, verdadeiro, escassez, ponte com o gráfico, até 5 min |
| 4 Acordo (5) | combinado de decisão (acordo do sim ou não, sem "em cima do muro"), sim e não explicados, sem ultimato |
| 5a Oferta e coleta (20) | definição, provas de resultado, 4 imagines, plausibilidade, entregáveis ligados às dores, coleta com silêncio, limpeza da mesa |
| 5b Ancoragem, preço, bônus, garantia (10) | 1 âncora + emocional; entrada → parcelado → à vista; silêncio; bônus depois; garantia clara (condicional e mensurável) |
| 6 Fechamento e objeções (15) | três sins com as palavras do lead; CTA; sinal na call (R$ 500 a R$ 1.000, até 10% do valor) ou objeção isolada, 3 camadas, acordo retomado; saída com dia e hora |

Status: cumprida = todos os critérios; parcial = algum faltou; não cumprida = etapa ausente ou contrária ao método. Pontuação
proposta: cumprida 100% do peso, parcial 50%, não cumprida 0. Nota < 70 = alerta e prioridade de análise humana.

## 3. Medições obrigatórias
- Duração total (alvo 1h15, teto 1h30) e de cada etapa.
- Minuto em que o preço apareceu e minuto em que o lead falou a primeira objeção.
- Quem falou mais no Raio-X e na coleta (o lead deve falar mais).

## 4. Calibração
- Antes de usar em série, aplicar a rubrica a uma sessão que deve reprovar (ex.: conversa solta sem Raio-X) e a uma que deve
  passar (call que vendeu e segue o roteiro). Se a ruim passar ou a boa reprovar, ajustar critérios.
- Revisar se uma nota alta foi merecida ou se a avaliação está "boazinha".
- Para automatizar (Fireflies + n8n + planilha, alerta no WhatsApp interno), usar `ht-avaliacao-de-reunioes-por-ia`.

## 5. Erros típicos para procurar na gravação
Sessão solta; método nas boas-vindas; várias perguntas iniciais; escala não explicada; nota baixa sem aprofundar; leitura que
dá solução ou é sucinta; herói pulado; acordo com ultimato ou sem o que acontece no sim e no não; coleta pulada; duas
ancoragens; ancoragem no que o expert gastou; preço confuso; continuar falando depois do preço; bônus antes do preço; garantia
não mensurável; não isolar objeção; sair sem data; tela inteira compartilhada; pressa.
