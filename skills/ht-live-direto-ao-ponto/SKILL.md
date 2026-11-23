---
name: ht-live-direto-ao-ponto
description: 'Monta a Semente High Ticket (SHT) no formato LDP, a live direto ao ponto do método FHT do Squad High Ticket, com o funil inteiro pronto. Checa prontidão (oferta validada em 1a1 e demanda reprimida), calcula meta de vagas, inscritos e presentes, escolhe narrativa (herói relutante ou oferta indecente) e CTA (aplicação grátis, aplicação paga ou entrada direta), escreve convites, criativo, página, pesquisa, lembretes, roteiro bloco a bloco com as 4 objeções, formulário de aplicação, recuperação pós-live e auditoria. Use quando o estrategista disser "vamos fazer uma live direto ao ponto", "semente HT do expert", "SHT", "LDP", "live de venda para a lista", "colher a lista depois do lançamento". NÃO usar para LCO (live de conteúdo e oferta, fora do material), aula semanal, webinário recorrente, renovação, nem lançamento pago semanal/5+1 (método LPSG da Turbo).'
---

# Live Direto ao Ponto (Semente High Ticket, formato LDP)

## 1. Para que serve e o que entrega

A LDP é uma live de 1 a 4 horas em que o expert convida a própria lista para uma **oferta declarada**: não tem aula, o conteúdo
é a apresentação do programa, do preço e do caminho para entrar. A aula a coloca entre as campanhas de maior retorno sobre investimento do
FHT (simples, pouco ou nenhum investimento), e o pós-live alimenta a sessão 1a1 com lista qualificada.

**Entrega**: a pasta do evento `05-eventos/AAAA-MM-ldp-<nome>/` com o **Pacote LDP**, em markdown:
1. `plano.md`: prontidão, ativos, data, metas (vagas, presentes, inscritos), narrativa, CTA, orçamento, decisões do estrategista.
2. `cronograma.md`: cronograma reverso de D-18 a D+7 com responsável e status por item.
3. `pecas/`: promessa, e-mail e WhatsApp de convite, roteiro do criativo, página de captura, pesquisa de cadastro, lembretes,
   formulário de aplicação, roteiro da live, roteiro de recuperação (rascunhos, estado "em revisão").
4. `checklist-dia.md` e `auditoria.md` (check-up preenchido).
5. `recuperacao/` com a planilha de controle e o modelo de debrief para `13-aprendizados/`.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões vigentes, portão da Aprovação 1).
2. Ler `experts/<slug>/ht/`: `00-plano/` (estado, pedido, aprovações, decisões), `02-oferta/oferta-vigente.md` (programa,
   entregáveis, preço, entrada, parcelado, à vista, garantia, bônus), `03-sessao/` (história do herói relutante, deck da
   sessão, árvore de objeções, conversão das sessões), `04-demanda/` (listas, grupos, aula semanal), `07-numeros/` (Central 1x1).
3. Entradas obrigatórias: oferta vigente aprovada; número de sessões feitas e vendas; tamanho e tipo de cada lista (alunos,
   ex-clientes, grupos, e-mail, seguidores); capacidade real de alunos novos (vagas); verba disponível.
4. Se faltar, perguntar no máximo 3 coisas, nesta prioridade: (a) quantas vendas já saíram da oferta atual em 1a1;
   (b) quais listas existem e de que tamanho; (c) quantas vagas o expert consegue absorver agora. O resto vira `[FALTA: …]`.

## 3. Passo a passo

### Fase 1: planejamento (sai com `plano.md`)

1. **Portão de prontidão**, conferido num dia só: **D-15 da data da live** (`ht-protocolo` §3.6; com a live no dia 40 de um
   plano, o portão é o dia 25). O mesmo dia vale no Diretor, no `ht-gestor-projetos` e no `ht-estrategista-eventos`; mudou a data
   da live, o portão anda junto. Resultado registrado em `plano.md`: go, go condicional (com OK escrito do estrategista) ou no-go.
   Os dois critérios são obrigatórios; falhou um, parar e devolver ao Diretor:
   - Oferta **validada**: a exigência da aula é já ter vendido esta oferta (sem venda, a oferta tende a sair confusa no pitch
     e a lista se queima). O protocolo considera validada a oferta testada em 20 sessões com 10% a 20% de conversão; com
     vendas mas menos de 20 sessões, registrar o número e levar ao estrategista antes de seguir.
   - **Demanda reprimida**: lista de clientes, alunos, ex-clientes, e-mail, WhatsApp, newsletter ou audiência que já conhece o
     expert. Referência da aula: 300 pessoas já serviram. Sem demanda reprimida o formato certo é a LCO, que não está no
     material: registrar a lacuna e propor outro canal (`ht-decisao-de-evento`).
   - Sinais de formato errado: pedir LDP para renovação (renovação é consultiva, 1a1); misturar com a aula semanal (fazer a
     LDP no lugar da aula, usar o grupo ou a página da aula como os da LDP, ou ofertar dentro da aula). **Convidar** para a LDP a
     partir da aula semanal não é misturar: segue as regras da `ht-aula-semanal`, Passo 10.
2. **Ativos**: listar cada lista com origem, tamanho e canal (grupos de lançamentos antigos, alunos, ex-clientes, e-mail,
   seguidores, live semanal, quem disse "agora não" na sessão). Pode convidar mais de uma vez, sem spam.
3. **Data**: quinta às 19h ou 20h como padrão, ajustando ao nicho (o dia em que o avatar não trabalha ou não viaja), fora de
   feriado, Carnaval e recesso de fim de ano (`ht-protocolo` §3.6; data deslocada é decisão do estrategista). Não no mesmo dia e
   horário da aula semanal. Captação
   de 10 a 11 dias (segunda de uma semana até quinta da seguinte); a equipe da aula já fez com 3 e com 15 dias, e 10 a 11 é o
   ponto ótimo. Live de 1 a 4 horas. Ação própria: lista, grupo e página separados da aula semanal.
4. **Metas** (de trás para frente; calculadora em `references/metas-cronograma-ldp.md`):
   meta de vendas = **número de vagas reais**; presentes = vendas ÷ conversão (planejar 2% a 3%; faixa da aula 2% a 5%);
   inscritos = presentes ÷ comparecimento (20% a 30%). Exemplo da aula: 1 venda ≈ 37 presentes ≈ 150 inscritos.
5. **Promessa**: framework da aula (oferta, não conteúdo), 7 elementos: data e hora, "live direto ao ponto para apresentar" + nome do programa, acompanhamento individual, definição de
   resultado do AR, vagas limitadas, chance de aplicar ou condição especial, sem gravação e sem replay.
6. **Narrativa** (uma só para convite, criativo, página e live): herói relutante é o padrão e vale na dúvida; oferta indecente só
   se a audiência já conhece o programa e existe uma janela real (turma nova, vagas remanescentes, condição que de fato nunca
   existiu). A história do herói é a mesma da sessão 1a1 (copiar de `03-sessao/`).
7. **CTA** (escolher e não trocar no meio): caminho A, aplicação com avaliação (só se o expert vai aprovar e reprovar de
   verdade); caminho B, entrada direta. Aplicação grátis com poucos inscritos, paga com muitos; na dúvida, grátis. Inscrição na
   live é sempre grátis. Valor da aplicação ou entrada sai de `02-oferta/`; se não existir, vira decisão do estrategista (seção 5).
8. **Orçamento**: de zero (grupos, e-mail, convite orgânico) a ~R$ 20 mil de tráfego para ~1.000 cadastros no maior caso citado.
   API oficial do WhatsApp raramente passa de R$ 2 mil. Um criativo basta. Pode começar sem tráfego e ligar o tráfego depois,
   se a meta de inscritos não vier pelas listas.

### Fase 2: implementação (sai com `pecas/` e `cronograma.md`)

9. Sala: Zoom ou Meet (recomendados; Teams também funciona; YouTube só se quiser alcance aberto, e aí o cadastro perde
   sentido). Separar listas de e-mail e WhatsApp.
10. Escrever as peças com os modelos de `references/modelos-copy-ldp.md`: promessa; e-mail e WhatsApp de convite na narrativa
    escolhida; roteiro do criativo; página de captura (título, subtítulo, 3 condições, bio curta, botão, aviso "se está só
    curioso, não se cadastre"); pesquisa de cadastro de 4 perguntas; lembretes (grupo: boas-vindas fixada + 5 toques;
    2 e-mails; individual opcional); formulário de aplicação de 5 perguntas abertas.
11. Fluxo: anúncio ou convite → página → botão → pesquisa → grupo de avisos. **Sem página de obrigado.** Evento Lead marcado no
    envio do formulário (não no clique do botão).
12. Roteiro da live bloco a bloco com `references/roteiro-da-live-ldp.md`: combinado, história, por que é oportunidade
    (metralhadora de travas com a voz da pesquisa), o que é e o que não é, para quem é (5 a 8) e para quem não é (3),
    entregáveis em 3 partes (o que é, benefício, como funciona), oferta com ancoragem e escassez real, CTA, 4 objeções
    eleitas respondidas pelo chat, encerramento. Reaproveitar 1 ou 2 slides do deck da sessão 1a1; o resto é fala.
13. Montar `cronograma.md` (modelo na referência de metas): cada peça com dono, prazo e revisão.

### Fase 3: execução e pós (sai com `checklist-dia.md`, `recuperacao/`)

14. Dia da live: checklist em `references/roteiro-da-live-ldp.md`. Link da aplicação repetido no chat; dúvidas só pelo chat,
    nunca microfone aberto; segurar a live depois do CTA; avisar que a equipe entra em contato no dia seguinte.
15. Pós-LDP (`references/pos-live-e-auditoria-ldp.md`): falar com **todos** os cadastrados, na ordem da pergunta de intenção da
    pesquisa. Aplicou: aprovar e integrar. Assistiu e não entrou: anotar a objeção, oferecer sessão 1a1 se fizer sentido. Não
    assistiu: levar para a sessão 1a1 completa. "Não tenho interesse": agradecer e deixar a porta aberta.
16. Debrief em `13-aprendizados/`: inscritos, presentes, aplicações, vendas na live, vendas da recuperação, objeções eleitas x
    objeções reais, custo.

## 4. Regras inegociáveis do método

- Só com oferta validada em 1a1 e demanda reprimida. Formato errado (LDP sem demanda) é o erro que mais derruba.
- A promessa é a **oferta**, dita com clareza ("vou apresentar e abrir vagas"), nunca conteúdo. Sem gravação, sem replay.
- A LDP sempre apresenta a oferta completa, com preço e condição de pagamento (é a mesma apresentação da sessão 1a1).
- Escassez **real**: número de vagas coerente com a capacidade (protocolo: expert sozinho até ~20 alunos). Nada de número
  inventado. "Depende de aprovação" só se houver aprovação de verdade.
- Uma narrativa para tudo. Não trocar o modo da aplicação (grátis/paga) no meio da campanha.
- Cadastro curto (perde gente entre botão e grupo); a aplicação pode ser longa. Não pedir dado que não será usado.
- Dúvidas só no chat. Link repetido. Live segurada depois do CTA. Não misturar com a aula semanal: lista, grupo, página, data e
  oferta da LDP são próprios; a aula pode **convidar** para a LDP nas regras da `ht-aula-semanal` (Passo 10), sem virar oferta.
- LDP não serve para renovação. Não repetir a toda hora; o uso citado mais frequente é a cada ~45 dias, logo depois de um
  lançamento clássico do produto principal.
- Padrões que se aplicam (o estrategista pode mudar em `padroes` do perfil): preço do HT vem de 02-oferta (5x a 10x a média do
  nicho); dupla +50% se a oferta tiver dupla; se o CTA levar a sessão de avaliação, a sessão usa o acordo do sim ou não, sem a
  metáfora "em cima do muro"; planejar 25% de comparecimento para evento gratuito, dentro da faixa da aula de 20% a 30%.

## 5. Quando a decisão é do estrategista

Levar em lote, opções fechadas, recomendação na a):
- **Caminho do CTA**: a) aplicação com avaliação, gratuita (recomendo quando a lista é pequena: mais aplicações, menos
  qualificadas); b) aplicação paga (filtra, menos gente para atender; precisa de lista grande); c) entrada direta (fecha mais
  rápido, sem filtro; exige oferta já muito clara).
- **Valor da aplicação ou entrada**, se `02-oferta/` não definir (faixa citada na aula: R$ 500 a R$ 2.000).
- **Número de vagas** (escassez real versus capacidade de entrega).
- **Narrativa**, quando o expert já vendeu o programa (herói relutante ou oferta indecente).
- **Verba de tráfego** e **condição especial** (bônus, preço) da live: preço e bônus só com nova versão de `02-oferta/`.
- Ativar campanha, disparar convite, ligar automação ou API: sempre OK explícito.

## 6. Critério de pronto e auditoria final

Pronto quando: [ ] portão de prontidão registrado com evidência, no dia D-15 da live, com o resultado (go, go condicional, no-go);
[ ] data conferida contra feriado e recesso; [ ] meta de vagas, presentes e inscritos calculada com as
taxas usadas; [ ] promessa com todos os elementos do passo 5; [ ] uma narrativa nas peças; [ ] CTA escolhido e o valor citado de 02-oferta
(versão); [ ] todas as peças da lista do item 1 escritas e em revisão; [ ] 4 objeções eleitas com resposta; [ ] cronograma
com dono e prazo; [ ] plano de recuperação com planilha; [ ] decisões do estrategista listadas.

**Auditoria** (rodar `references/pos-live-e-auditoria-ldp.md`, seção 3; os erros típicos da aula): formato certo; oferta
validada; promessa de oferta (não de conteúdo); escassez real; aprovação real; modo de aplicação fixo; cadastro curto e sem
obrigado; link repetido; live segurada; sem microfone aberto; sem replay; não misturada com a aula semanal; copy do expert
adaptada (não copiar modelo nem copy de outro expert ao pé da letra); números de aula marcados como referência.

## 7. Saída e handoff

- Grava em `05-eventos/AAAA-MM-ldp-<nome>/` (dono: ht-produtor-eventos; roteiro da live com ht-roteirista-palco).
- Copy das peças: pedido ao ht-diretor-copy (ht-copy-paginas-e-emails para e-mail e página; ht-copy-anuncios-e-mensagens para
  criativo e WhatsApp); a versão final mora em `08-copy/`.
- Página: ht-web-designer em `09-visual/`. Criativo e tráfego: ht-gestor-trafego (campanha nasce PAUSADA; no nome, o prefixo de campanha do perfil, `trafego.prefixo_campanha`, se houver).
- Grupo, lembretes e disparos: ht-gestor-automacoes (nada envia sem OK do estrategista).
- Números e verba: ht-controller (`07-numeros/`). Recuperação: rascunhos para o ht-closer (`03-sessao/`), que não fala com lead.
- Revisão obrigatória: textos → ht-revisor-metodo-copy; página e slides → ht-revisor-visual.

## 8. Ferramentas de apoio

`ht-palestras-e-pitch` (se quiser aprofundar oferta e objeções do roteiro), `ht-objecoes` (árvore), `ht-captacao-e-presenca`
(grupo, lembretes, WhatsApp), `ht-criativos-high-ticket` e `ht-trafego-high-ticket`; `hook-generator` e `avoid-ai-writing` ou
`humanizer` na copy; `pagina-design-premium` ou `designer-senior-turbo` e `publicar-pagina-cloudflare` para a página;
`conectar-whatsapp-oficial` e `automacao-fluxos` para grupo e lembretes; `email-marketing-mautic` para os 2 e-mails;
`meta-ads-cli-turbo` ou a ferramenta de tráfego do perfil (`trafego.ferramenta`) para a campanha; `ad-creative-video` ou `capcut-edit` para o vídeo do convite;
`anthropic-skills:xlsx` para a planilha de recuperação.

## 9. Fontes e lacunas

**Fontes**: trilha 16 (Bootcamp de SHT formato LDP, 3h09, transcrição lida por inteiro na revisão R6 de 23/11/2026) e seu
RESUMO; catálogo, entradas
fht-sht-planejar, fht-sht-promessa-narrativa-e-cta, fht-sht-convites-e-captacao, fht-sht-roteiro-da-live, fht-sht-auditoria,
fht-recuperacao-pos-evento, fht-semente-de-ingresso (partes C, H, I); trilha 17, aula 53 (recuperação de vendas pós-imersão,
usada como adaptação na recuperação, marcado na referência).

**Lacunas**: textos dos lembretes e a versão de WhatsApp das narrativas não foram ditados (ficaram no documento de apoio da
aula, sem link); os modelos de lembrete nesta skill são rascunhos do squad seguindo a cadência da aula. A LCO (variante sem
demanda reprimida) não está no material. Duração de cada bloco do roteiro não foi dada. Conta de datas do cronograma da aula
tem ruído de legenda. Valores dos casos (inclusive o de ~R$ 232 mil) são referência a conferir.
