---
name: ht-treino-comercial
description: 'Squad High Ticket / método FHT. Treina e mede quem vende o HT por sessão 1a1: organiza e conduz roleplay (cliente simulado com objeções reais e feedback por etapa), faz check-up do material antes das sessões, audita gravação ou transcrição de sessão contra o roteiro FHT (status por etapa, timestamp, nota), diagnostica conversão baixa na ordem avatar, oferta, execução, desmonta a call que vendeu (engenharia reversa) e monta o time comercial (quando delegar, kit do vendedor, remuneração sobre recebimento, fluxo SDR-closer). Use quando o estrategista disser "faz um roleplay da sessão", "analisa essa gravação", "por que não está vendendo", "fiz 15 sessões e vendi uma", "engenharia reversa dessa call", "posso contratar closer?", "quanto pago o vendedor". NÃO usar para escrever o roteiro (ht-roteiro-sessao-1a1) nem para LPSG, 5+1 ou Funil 8 (Turbo).'
---

# Treino comercial da sessão 1a1

## 1. Para que serve e o que entrega

A sessão 1a1 melhora a cada call, mas só se alguém olha de fora com o método na mão. Esta skill é o "olho de fora": ensaia antes
(roleplay e check-up), mede depois (auditoria da gravação), acha a causa quando os números não vêm (diagnóstico de conversão),
aprende com o que deu certo (engenharia reversa) e prepara a passagem da sessão do expert para um vendedor (time comercial).

**Entregas** (pasta `03-sessao/treino/`, uma por pedido):
- **Roleplay**: roteiro do cliente simulado (perfil, dores, notas que vai dar, objeções plantadas), condução e relatório de
  feedback por etapa (`references/roleplay.md`).
- **Check-up** (antes): parecer sobre Raio-X, roteiro, herói e deck, com os ajustes numerados.
- **Auditoria de sessão** (depois): tabela por etapa com status (cumprida, parcial, não cumprida), observação com timestamp e
  correção; nota geral; objeção final e onde nasceu; 3 ajustes de maior impacto (`references/rubrica-auditoria-sessao.md`).
- **Diagnóstico de conversão**: funil com números, hipóteses na ordem avatar → oferta → execução, plano de ajuste
  (`references/diagnostico-de-conversao.md`).
- **Engenharia reversa**: trecho a trecho da call que vendeu, com o porquê e o impacto no fechamento
  (`references/engenharia-reversa.md`).
- **Time comercial**: decisão de delegar, kit do vendedor, remuneração, fluxo e rotina de treino (`references/time-comercial.md`).

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`: `03-sessao/` (Raio-X, roteiro, deck, objeções, gravações e transcrições em `privado/`),
   `02-oferta/oferta-vigente.md`, `07-numeros/` (Central 1x1: leads, agendadas, realizadas, vendas, objeções por lead, origem),
   `13-aprendizados/`.
3. Entradas obrigatórias por entrega: roleplay e check-up → os 3 materiais (Raio-X, roteiro, deck); auditoria → gravação ou
   transcrição com tempo (e o resultado da call); diagnóstico → número de sessões, vendas e origem dos leads; time comercial →
   conversão atual do expert e capacidade de entrega. Se faltar, no máximo 2 perguntas simples por vez; o resto vira `[SUPOSIÇÃO: …]` e entra em "Assumi".
4. Gravação de lead é dado sensível: fica em `03-sessao/privado/`, sem nome em material de treino compartilhado.

## 3. Passo a passo

**Passo 1. Escolher o momento certo.**
- Antes da primeira sessão real: **check-up** dos materiais e **roleplay** completo.
- Primeiras sessões: só observar; a análise vale a partir de **5 sessões** (as primeiras quase sempre têm ajustes óbvios).
- Conclusão sobre conversão e preço: só depois de **20 sessões** (padrão do squad; 25 no desafio).
- Expectativa para alinhar com o expert (referências da trilha 09, aula 13, a conferir): a maioria das sessões termina em não;
  casos citados levaram 14 e 30 sessões até a primeira venda. Quem não tem urgência de caixa pode fazer as primeiras sessões com
  pessoas de baixo potencial de compra, só para aprender; quem precisa vender começa pelos potenciais.

**Passo 2. Roleplay** (`references/roleplay.md`). Pré-requisito: roteiro, Raio-X e deck prontos. O "cliente" é uma pessoa da
equipe (ou o agente, por texto ou voz) no papel do avatar real, sem facilitar, com objeções reais da planilha de `ht-objecoes`.
Simula do quebra-gelo ao fechamento, sem pausas, cerca de 35 a 50 minutos, e depois feedback por etapa. Formato do feedback: o
que foi bom, o que estava errado em cada etapa com o **fundamento** (o porquê no método), o que fazer na próxima sessão real.
Um ponto por observador; prioridade aos de maior impacto.

**Passo 3. Check-up** (antes). Rodar as auditorias de `ht-raio-x` e de `ht-roteiro-sessao-1a1` sobre os materiais e devolver os
ajustes numerados. Conferir links abertos e o gráfico carregando.

**Passo 4. Auditoria de sessão gravada** (`references/rubrica-auditoria-sessao.md`).
- Transcrever com tempo (`transcrever-youtube-turbo` ou `watch` para ver tela e gráfico).
- Para cada etapa do roteiro de 6 etapas, marcar cumprida, parcial ou não cumprida, com observação e timestamp.
- Medir os tempos reais contra o padrão do squad (alvo 1h15, teto 1h30) e a proporção fala do vendedor x fala do lead.
- Registrar a objeção final e em que etapa ela poderia ter sido quebrada.
- Nota geral 0 a 100 com pesos (proposta da skill em `references/rubrica-auditoria-sessao.md`, a calibrar).
- Fechar com os 3 ajustes de maior impacto e o que treinar no próximo roleplay.

**Passo 5. Diagnóstico de conversão** (`references/diagnostico-de-conversao.md`). Montar o funil pela Central 1x1 (leads →
agendadas → realizadas → ofertadas → vendas, por origem). Referência (padrão do squad): **10% a 20%** de conversão da sessão;
**abaixo de 5%** aciona este diagnóstico. Investigar na ordem: **avatar** (quem chega é cliente? tem dinheiro e dor?), **oferta**
(o benefício é incomparavelmente maior que o preço? garantia e forma de pagamento?), **execução** (auditoria de 3 a 5 gravações).
Sinais rápidos de execução: notas 10 em tudo, herói pulado, leitura sucinta, preço antes do valor, coleta pulada, saída sem data.
Preço à vista travando: o agente assume a recomendação (manter o preço à vista e sugerir P2P como reforço; Fake HT só como referência) e lista em "Assumi".

**Passo 6. Engenharia reversa da call que vendeu** (`references/engenharia-reversa.md`). Play, pausa, motivo da fala, impacto
agora e no fechamento, o que ainda melhoraria. Extrair o padrão replicável (pergunta que aprofundou a dor, oferta aterrissada no
Raio-X, preço com silêncio, sinal na call) para o roteiro e para o kit do vendedor. Fazer o mesmo com uma call que não vendeu,
para achar onde a venda se perdeu.

**Passo 7. Time comercial** (`references/time-comercial.md`). Delegar só depois que o expert fez pelo menos 10 a 20 sessões e a
conversão está validada (fontes citam 20% a 30% antes de delegar; referência a conferir). Kit do vendedor: roteiro em tópicos e
completo, Raio-X, deck, planilha de objeções, gravações-modelo, acesso à Central 1x1. Remuneração: fixo + variável sobre o
**recebido** (parcelas pagas), não sobre o contrato; link de pagamento por vendedor. Fluxo: SDR alimenta até a reunião, closer
conduz a sessão, suporte agenda o diagnóstico de entrega. Rotina: gravar tudo, roleplay semanal, auditoria por amostragem.

**Passo 8. Registrar e fechar.** Toda entrega termina com o que muda no roteiro (proposta ao Closer via Diretor, porque
`03-sessao/` tem dono), o próximo treino e o debrief em `13-aprendizados/`.

## 4. Regras inegociáveis do método

- O padrão de avaliação é o roteiro de 6 etapas da trilha 09 (padrão do squad) e os padrões recomendados de garantia condicional e mensurável, ordem do preço (entrada,
  parcelado, à vista), sinal com a call aberta e acordo do sim ou não sem "em cima do muro".
- Feedback cirúrgico e numerado, sempre com o fundamento; sem elogio vazio e sem humilhação (reconhecer a coragem de quem
  apresentou e ser específico).
- Analisar com amostra suficiente: 5 sessões para análise, 20 para concluir sobre conversão ou preço. Dizer "N de M analisadas".
- Nada de inventar fala, nota ou resultado de sessão; o que a gravação não mostra é "não observável".
- Roleplay com IA no papel de cliente é desenho do squad (a FHT faz roleplay humano); deixar isso claro no relatório.
- Gravação de lead só com aviso ao lead e guardada em `privado/`.
- O treino não fala com lead: produz material para o expert e o vendedor já definido no projeto (sem definição, assume o expert e lista em "Assumi").

## 5. O que o agente decide e o que pede OK

Sem lote de perguntas nem a/b/c: o agente decide pela recomendação e lista em "Assumi" ("Assumi: …; é só pedir para mudar").
- Delegar a sessão e a quem; modelo de remuneração (fixo, variável, percentual) e metas: propõe pela recomendação (remuneração sobre recebimento). Contratar alguém é gasto e pede "posso seguir?".
- Ajuste de oferta ou preço vindo do diagnóstico (só depois de 20 sessões): o agente propõe um ajuste, com o impacto no caixa em uma linha, e ele só vira oficial na Aprovação 1 ou na aprovação do plano.
- Testar variante de roteiro (VSD, ordem do acordo, bônus antes do preço): assume o roteiro padrão e lista em "Assumi".
- Montar a avaliação automática de reuniões por IA (`ht-avaliacao-de-reunioes-por-ia`): ativar pede "posso seguir?".

## 6. Critério de pronto e auditoria final

- [ ] Entrega certa para o momento (check-up antes, análise com ≥ 5 sessões, conclusão com ≥ 20).
- [ ] Toda etapa avaliada com status, observação, timestamp (quando há gravação) e correção com fundamento.
- [ ] Tempos medidos; objeção final e etapa de origem registradas.
- [ ] Diagnóstico de conversão com números da Central 1x1 e hipóteses na ordem avatar → oferta → execução.
- [ ] 3 ajustes de maior impacto e o próximo treino definidos.
- [ ] Amostra declarada ("N de M"); nada inventado.

**Auditoria final** (erros típicos que os mentores mais apontam nos laboratórios e roleplays): sessão solta; boas-vindas que
falam do método; várias perguntas iniciais; Raio-X sem explicar a escala; nota baixa não aprofundada; não anotar as palavras do
lead; leitura sucinta ou que dá solução; herói pulado ou longo; acordo com ultimato; entregáveis demais e sem ligação com a dor;
coleta pulada; ancoragem fora da ordem 10x, 5x, emocional; continuar falando depois do preço; bônus antes do preço; garantia vaga; não isolar a objeção;
insistir em parcela com quem quer pagar à vista; sair sem dia e hora; tela inteira compartilhada; pressa e falta de escuta.
Conferir se o relatório cobre cada um quando aplicável.

## 7. Saída e handoff

- Gravar em `experts/<slug>/ht/03-sessao/treino/` (relatórios sem nome de lead; transcrições em `03-sessao/privado/`).
- Mudanças no roteiro, Raio-X ou deck: proposta ao `ht-closer` (dono de `03-sessao/`) via Diretor; preço ou oferta: ao
  `ht-arquiteto-oferta`; números: ao `ht-controller` (`07-numeros/`).
- Revisão: `ht-revisor-metodo-copy`.
- Debrief de cada ciclo de 5 e de 20 sessões em `13-aprendizados/`.

## 8. Ferramentas de apoio (por nome, sem copiar)

`watch` (ver a gravação, gráfico e slides) · `transcrever-youtube-turbo` (transcrição com tempo) · `anthropic-skills:xlsx`
(funil e rubrica) · `analytics-dashboard` (painel de conversão) · `anthropic-skills:docx` (kit do vendedor) · `avoid-ai-writing`
(feedback em texto limpo).

## 9. Fontes e lacunas

**Fontes:** trilha 22, roleplays (mar/2025 179, mai/2025 160, jul/2026 RJ 12, jun/2026 SP 25 via resumo), laboratórios (fev/2025
197, mar/2025 180, dez/2025 144, jan/2026 128, abr/2026 95 transcrita em 22/11, mai/2026 80, jul/2026 RJ 09) e engenharia reversa
(jan/2025 192-195); trilha 15, Bootcamp de IA (RESUMO: fluxo de avaliação de reunião, status por etapa, nota 0-100 com peso,
alerta abaixo de 70, calibração); trilha 09 (benchmarks e erros, RESUMO-vendas §7-8, RESUMO-apresentacao §7-8); rota 3 resumos
01-02 e 03-10 (check-up, análise após 5 sessões, documento de ações recomendadas); planilha Central 1A1
(`trilhas/_materiais/planilhas/10-social-lead-generation__16k_wVG3.xlsx`); catálogo fht-roleplay-sessao-1a1,
fht-auditoria-sessao-1a1, fht-diagnostico-de-conversao-1a1, fht-engenharia-reversa-de-sessao-que-vendeu, fht-time-comercial
(partes B, E, F, G, H, I); padrões do squad.

**Lacunas (não inventar):** a rubrica da trilha 15 é a da sessão de diagnóstico de entrega, não a de vendas; os prompts, os pesos
completos e a planilha "Avaliação da reunião" não estão nos arquivos; não há GPT de roleplay na FHT (citado, sem link); o
formulário "Análise de Vendas" é só citado; não há treinamento formal de vendedor, metas por vendedor nem tabela de comissão nos
arquivos (só princípios de lives e palestras); números de conversão variam entre turmas (de 1 em 20 a 10%-20%; vale o padrão do squad).
