# IMI: parte do método, metas, orçamento e cronograma do projeto

Fontes: trilha 17 aulas 01 a 04 (planejamento, transcritas em 22/11/2026), aula 12 (planilha de tráfego); trilha 22, desafio
out/2025 (onboarding, planejamento, plantões) e fev/2026 (onboard, planejamento, início da captação, plantões); catálogo
fht-planejar-imi-online-1-dia, fht-imersao-implementacao-paga. Números de aula são referência, a conferir.

## 1. Escolher a parte do método (o que fica pronto)

Pergunta-guia da aula: dentro do HT, o que faz sentido implementar **junto** com o potencial cliente em um dia online?

1. Listar as etapas da jornada do avatar (`02-oferta/`).
2. Marcar a **primeira objeção** que trava o avatar (FHT: "preciso ter um HT" e logo depois "como vendo"; daí "criar o HT e
   estruturar o primeiro canal de vendas").
3. Escolher a etapa que resolve essa objeção e que pode ser executada online ao vivo. Se a habilidade final não cabe online
   (ex. cirurgia), usar uma etapa anterior (planejamento, avaliação, diagnóstico, preparação).
4. Definir o artefato que o participante leva: um plano, um primeiro conteúdo publicado, uma avaliação feita, uma oferta escrita,
   um trecho executado. Uma coisa só, sucinta.
5. Pré-requisito (instrumento, exame, caso real, conta numa ferramenta): avisar desde a página e mandar, no cadastro, a orientação
   para chegar pronto (exemplo da aula: mini guia para escolher o instrumento, cupom de loja).
6. Testar o efeito desejado: no fim do dia a pessoa fez, mas não sabe se fez certo nem como seguir; o feedback ao vivo em 1 ou 2
   pessoas mostra o valor de ser acompanhado.

Exemplos corrigidos ao vivo (nichos, sem nomes): plano de conteúdo de 30 dias e o primeiro conteúdo publicado (Instagram);
avaliar pacientes de coluna na prática (fisioterapia, sem apelo financeiro porque o HT não tem); plano para eliminar até X kg até
o fim do ano (emagrecimento; promessa de peso em template de API pode bloquear o número, cuidado com compliance); primeiro funil
de entrada configurado (IA); suplementação montada para um caso (nutrição).

## 2. IMI paga (variante)

O evento é o produto: entrega todo o conteúdo para o participante fazer sozinho; quem quer feedback compra o AR. Caso citado:
primeira versão a R$ 10 mil, teste a R$ 5 mil; credencial de R$ 97 em outras edições (conferir). Venda do ingresso com
`ht-venda-de-ingressos`. Decisão de entrada (gratuita, credencial ou paga) é do estrategista, por evento, com prós e contras.

## 3. Metas e orçamento

```
Meta mínima do método: 300 inscritos → 100 ao vivo (planos comuns de Zoom e Meet aguentam ~100 sem atrito; acima de ~500
muda a estrutura). Lista ou audiência grande: subir (ex. 1.000 inscritos → 300 ao vivo).

Modelo Venda (venda no evento):  vendas = presentes no pitch x c   c de planejamento das duas turmas: 5% (FHT 1,5% a 2% com
                                 ticket de R$ 80 a 100 mil; média vista nos alunos 5% a 10%; caso de aluno ~13%; conferir).
                                 Cenário conservador para ticket muito alto: 1,5% a 2%.
Modelo Sessão (sessão de avaliação): agendamentos = presentes no pitch x 34% a 45% (out e dez/2025) ; sessões realizadas ≈ 80% das agendadas
                                vendas = sessões x conversão da sessão do expert (03-sessao; referência 10% a 20%)
Recuperação: projetar à parte (casos: 8 → 16, 0 → 3, 3 → 13 vendas depois da recuperação, conferir)

Verba: leads pagos x CPL + ~20% de reserva (lembrete, remarketing, API)
  out/2025: R$ 3.000 = 300 leads x CPL médio de R$ 10 (aula 04); 19 dias, R$ 126/dia (planilha, conferir)
  fev/2026: R$ 4.500 = 300 leads x CPL de planejamento R$ 15 (FHT ~R$ 12,50); a planilha separa R$ 3.600 captação +
            R$ 900 distribuição dos Reels; 32 dias, R$ 113/dia (conferir)
  Faixa de verba (fev/2026): mínimo ~R$ 4.500; normal R$ 4.500 a R$ 10 mil; teto ~R$ 20 mil (acima o pico passa do plano
  da sala: ~300 no Zoom do FHT, acima de ~500 duas contas). Investir só o que aceita não ver voltar.
  Sem verba: compensar no orgânico (listas, Reels com CTA, e-mail, LinkedIn). Parte da verba pode ir para disparo pela API
  oficial a listas existentes (custo por lead da API no lugar do CPL). Plataforma: Meta; Google não para verba deste tamanho.
  CPL visto nas turmas: R$ 3 a R$ 50; FHT ~R$ 12,50 a 25; presencial do FHT até R$ 120
Comparecimento para planejar: 25% a 30% de quem preencheu o T1 (premissa do squad: 25%); perda de ~20% entre inscrição e T1
```

Investimento como construção de audiência: os ~70% que se inscrevem e não aparecem viram base para sessão 1a1, aula semanal e a
próxima imersão (o FHT passou a usar a imersão como principal estratégia de audiência). Lead frio converte zero enquanto frio;
depois de horas com o expert, já não é frio no momento da oferta.

Entrega da etapa 1 (formulário do desafio, usar como checklist): data · formato (implementação) · definição do HT · Big Idea ·
meta de inscritos · investimento em captação.

## 4. Cronograma do projeto (E = sábado do evento)

| Semana | Entregas | Dono |
|---|---|---|
| E-6 | Ficha do evento aprovada; parte do método; Big Idea; metas; verba; decisões do estrategista (entrada do evento, fechamento) | estrategista de eventos, ht-controller, estrategista |
| E-6 a E-5 | Copy de captação: página de inscrição, inscrição confirmada (curta e longas), convite para cada lista com gancho próprio, criativos (≥5 vídeo + 5 estático) | ht-diretor-copy, ht-copy-* |
| E-5 | Ferramentas: página (Hotmart Pages, WordPress ou Figma), formulário T1 com redirecionamento direto, grupo de avisos, e-mail automático; conta de anúncio, pixel, evento Lead no envio, públicos | ht-web-designer, ht-gestor-automacoes, ht-gestor-trafego |
| E-5 a E-1 | Captação (campanha PAUSADA até o OK; depois relatório D-1 e otimização a cada 2 a 3 dias); teoria das setas: bio, fixado, stories semanais, Reels com CTA, listas, tudo aponta para a página | ht-gestor-trafego, ht-estrategista-conteudo |
| E-4 a E-3 | Grade do dia; árvore de objeções da imersão; talk de entrada; palestra de oportunidade | ht-roteirista-palco |
| E-3 a E-2 | Pré-pitch e pitch (mapa mental → slide); laboratório interno de revisão | `ht-palestras-e-pitch`, revisores |
| E-2 (≈15 dias antes) | Aquecimento e confirmação de presença: lembretes para todos; confirmação com resposta; API oficial verificada | `ht-captacao-e-presenca`, automações |
| E-1 | Preparação técnica: central, sala, agenda ou checkout, ficha, plano B, ensaio | ht-produtor-eventos |
| E | Imersão | expert e equipe |
| E+2 dias a E+11 | Recuperação (ligações, encontro de fechamento, fluxo de sessão) | ht-closer (rascunhos), equipe |
| E+7 | Debriefing e análise individual da imersão | ht-produtor-eventos |

Regras de calendário (onboarding fev/2026): captação aberta até o início da imersão; Reels com CTA a partir da semana de
captação, 5 por semana, gravados e editados na semana anterior; com lançamento do produto principal em curso, abrir a captação
só depois do carrinho fechar ou dar a imersão como bônus do lançamento; as sessões 1a1 continuam durante o projeto. O FHT
montou edições em 7 dias como teste rápido; não é o recomendado para a primeira.

Versão comprimida de 4 semanas (out/2025): S1 planejamento e preparação da captação; S2 captação e ajustes; S3 conteúdo; S4
confirmação e ajustes finais. Captação mais longa dá mais segurança (fev/2026 usou ~32 dias).
