# Estrutura da pasta do projeto HT e formato do handoff

Vale para todo agente do Squad High Ticket.

## 1. Onde fica

A raiz vem do perfil do estrategista (`~/.config/squad-ht/perfil.md`, campo `raiz_projetos`; padrão `~/squad-ht/`). O perfil é
opcional: sem ele, a raiz é `~/squad-ht/` e o agente trabalha direto (o nome do expert só é perguntado se for preciso criar a pasta).

| Situação | Raiz do projeto | Exemplo |
|---|---|---|
| Expert com pasta | `<raiz_projetos>/<expert>/ht/` | `~/squad-ht/expert-exemplo/ht/` |
| Expert sem pasta | o Diretor cria `<raiz_projetos>/<expert>/ht/` | `~/squad-ht/expert-exemplo/ht/` |

- Nas skills, `experts/<slug>/ht/` e `<raiz_projetos>/<expert>/ht/` são a **notação** da raiz resolvida pelo perfil; não são
  caminho literal.
- `<slug>` (nomes de arquivo): minúsculas, sem acento, com hífen (ex.: `expert-exemplo`). Se a pasta do expert já existe com
  espaço e acento, vale o nome que existe; sempre passar o caminho entre aspas.
- Antes de criar, o Diretor procura a pasta que já existe em `<raiz_projetos>` (`ls`), inclusive com nome parecido. Achou: usa
  ela e cria só `ht/` dentro. Não achou: cria a nova. Nos dois casos registra o caminho absoluto em `00-plano/README.md` na
  primeira linha.
- O que está na pasta do expert **fora** de `ht/` (materiais, planilhas e relatórios) é leitura para o squad; o squad escreve
  só dentro de `ht/`. Nenhum agente cria a pasta em outro lugar por conta própria.

## 2. Árvore e dono de cada subpasta

Convenção única dos 32 agentes. Vale acima do que um agente ou skill disser em contrário;
quem achar divergência corrige o próprio arquivo ou avisa o Diretor.

Regras de escrita:
- **Todo agente lê qualquer subpasta; escreve só nas que estão no nome dele na árvore abaixo.** Mudança em pasta alheia =
  pedido ao dono via Diretor (ou proposta escrita na própria subpasta, que o dono lê).
- **Dono da pasta** (primeira linha de cada número) responde pela pasta inteira e escreve em tudo que a árvore não atribui a
  outro agente. **Exceção** é a subpasta com outro nome ao lado: ali só esse agente escreve, nem o dono da pasta.
- **Quem cria**: o Diretor cria a raiz `ht/`, as 14 pastas numeradas e os arquivos de `00-plano/`. Cada agente cria as próprias
  subpastas na primeira gravação (o núcleo cria as de `08-copy/` e `09-visual/`; os estrategistas criam o seu `estrategia/`).
- **`estrategia/`**: cada estrategista escreve só no `estrategia/` da pasta do time que lidera (plano, sub-pedidos em
  `estrategia/pedidos/<nn>-a-<agente>.md`, consolidação e a entrega dele). Nada fora disso.
- **`privado/`** (dado de lead e aluno: gravação, Raio-X preenchido, conversa, contato, CPF): o `privado/` da raiz de uma pasta
  numerada é do agente indicado na árvore; qualquer outro agente que precise guardar dado sensível usa `<sua-subpasta>/privado/`.
  Nada de `privado/` vai para material público.
- **`12-revisoes/pedidos/`**: qualquer agente grava ali o **pedido** de revisão da própria entrega. Os **pareceres** são só dos
  dois revisores.
- **`historico/`**: arquivo substituído vai para o `historico/` da subpasta de quem o escreveu, com data no nome.
- **`13-aprendizados/`**: quando uma skill diz "debrief em `13-aprendizados/`", isso é o destino. O agente escreve o
  rascunho na própria subpasta e o manda pelo handoff; quem grava em `13-aprendizados/` é o Diretor.

```
experts/<slug>/ht/
├── 00-plano/                         Dono: ht-diretor
│   ├── README.md                       caminho absoluto da raiz (1ª linha), expert, nicho, etapa atual da rota, links
│   ├── estado.md                       ciclo (criar/vender/entregar/renovar), etapa, próximo passo, bloqueios
│   ├── aprovacoes.md                   as 4 aprovações do estrategista (1 pesquisa e oferta, 2 plano da ação, 3 peças revisadas, 4 ir ao ar; padrão `aprovacoes` do perfil), com data e versão dos arquivos
│   ├── decisoes.md                     registro único: D1, D2… do que foi assumido, com os códigos de origem (DA-1, DC-4) e as mudanças da pessoa por extenso (§3.5)
│   ├── variaveis.md                    variáveis compartilhadas do projeto (§3.6): nome do programa, promessa, Big Idea, datas
│   ├── pedidos/                        um arquivo por pedido do Diretor (formato na seção 3.1)
│   ├── historico/                      versões antigas de README, estado (ht-diretor)
│   ├── cronograma.md                   EXCEÇÃO ht-gestor-projetos: calendário de ações, eventos e ciclos de renovação
│   └── cronograma/                     EXCEÇÃO ht-gestor-projetos: entregas do gestor e historico/ do cronograma
├── 01-pesquisa/                      Dono: ht-pesquisador
│   ├── (raiz)                          potencial HT, papéis e acordo, 4 âncoras, Market Fit, Roma/promessa, objeções do
│   │                                   expert, voz do avatar, proposta de portfólio para o Arquiteto, entregas
│   ├── bruto/  privado/                fontes brutas; dado identificável de pessoa
│   └── casos/                          EXCEÇÃO ht-consultor-casos: benchmark "nada nasce do zero" e a entrega dele
├── 02-oferta/                        Dono: ht-arquiteto-oferta (ÚNICA fonte de preço e oferta; só muda com OK do estrategista)
│   ├── oferta-vigente.md               a oferta em vigor (promoção: ver "Promoção da oferta" abaixo)
│   ├── oferta-proposta-vN.md           oferta completa candidata (ht-oferta-matadora)
│   ├── portfolio.md                    ordem dos HTs (vigente); versão anterior em historico/
│   ├── niveis-e-faixas.md  renovacao-<ciclo>.md
│   ├── rascunhos/                      um rascunho datado por passo (definição, entregáveis, preço…); rascunhos/upgrade/
│   ├── complementares/                 fichas de CI, peixe assado, experiência HT
│   ├── historico/                      versões anteriores datadas
│   └── estrategia/                     EXCEÇÃO ht-estrategista-produto (lidera pesquisa e oferta)
├── 03-sessao/                        Dono: ht-closer
│   ├── nome-da-sessao.md               FONTE ÚNICA do nome e da promessa da sessão 1a1 (ht-closer); página, vitrine, SLG,
│   │                                   aula e anúncio só citam este arquivo
│   ├── roteiro/  raio-x/  objecoes/    roteiro 6 etapas, herói relutante, acordo sim/não, deck; Raio-X; árvore de objeções
│   ├── agendamento/  follow-up/  aplicacao/   cadência, lembretes, no-show, follow-up, repescagem (rascunhos)
│   ├── privado/                        Raio-X preenchido, gravações e transcrições de sessão, conversas (ht-closer)
│   ├── estrategia/                     EXCEÇÃO ht-estrategista-comercial
│   └── treino/                         EXCEÇÃO ht-treinador-comercial: roleplay, check-up, auditorias de sessão, diagnóstico;
│                                       transcrição que ele gerar em treino/privado/ (lê as gravações de 03-sessao/privado/)
├── 04-demanda/                       Dono: ht-estrategista-demanda
│   ├── estrategia/                     plano de demanda, sub-pedidos, entrega (ht-estrategista-demanda)
│   ├── funil-de-entrada/               desenho, especificação e painel do funil de entrada (ht-estrategista-demanda)
│   ├── vitrine/  reels/  aula-semanal/  conteudo-de-prova/  lives-45-dias/
│   │                                   EXCEÇÃO ht-estrategista-conteudo (dado sensível em <subpasta>/privado/)
│   └── slg/  fila/  privado/           EXCEÇÃO ht-sdr: lista de 100, mensagens (rascunho), central-1x1-slg.csv, FILA de
│                                       leads que passa ao comercial (o estrategista pede e confere; o SDR grava),
│                                       contatos e conversas de lead
├── 05-eventos/                       Dono: ht-produtor-eventos
│   ├── AAAA-MM-<tipo>-<nome>/          uma pasta por evento (ldp, ima, imi, imr, presencial, webinario, turne…)
│   │   ├── (raiz)                      cronograma.md, grade, pacote do formato, debriefing.md, entregas (ht-produtor-eventos)
│   │   ├── captacao-e-presenca/  recuperacao/  privado/     (ht-produtor-eventos)
│   │   ├── estrategia/                 EXCEÇÃO ht-estrategista-eventos: ficha-do-evento.md, mapa-do-funil.md, pedidos/
│   │   ├── palco/                      EXCEÇÃO ht-roteirista-palco: palestras, pré-pitch, pitch, falas, roteiro de slides
│   │   └── ingressos/  afiliados/  patrocinio/   EXCEÇÃO ht-ingressos-e-patrocinio (dado em <subpasta>/privado/)
│   ├── AAAA-MM-desafio-<nome>/         EXCEÇÃO ht-diretor-desafio: a pasta inteira (privado/ incluído), menos
│   │                                   estrategia/ se o estrategista de eventos abrir uma
│   └── _programas/consultores/         EXCEÇÃO ht-ingressos-e-patrocinio: programa de consultores HT comissionados
├── 06-entrega/                       Dono: ht-arquiteto-entrega
│   ├── onboarding/  entregaveis-1a1/  grupo/  escala/  manual/   (ht-arquiteto-entrega; dado em <subpasta>/privado/)
│   ├── estrategia/                     EXCEÇÃO ht-estrategista-sucesso: plano de sucesso, sub-pedidos, entrega
│   ├── acompanhamento/  provas/        EXCEÇÃO ht-cs: painel de alunos, NPS, catálogo de resultados, Toque de Midas,
│   │                                   provas/autorizacoes.md
│   ├── privado/                        EXCEÇÃO ht-cs: base de alunos (dados pessoais); os outros leem
│   └── renovacao/  upgrade/            EXCEÇÃO ht-gestor-renovacao: ciclos, controle, pitch, upgrade e GIC
│                                       (dado em <subpasta>/privado/; oferta de renovação vai a 02-oferta pelo Arquiteto)
├── 07-numeros/                       Dono: ht-controller
│   Master Plan, número mágico, Central 1x1, funil comercial, KPIs pelas 4 alavancas, caixa contrato x recebido, orçamento,
│   LTV, historico/
├── 08-copy/                          Dono: ht-diretor-copy (subpastas criadas pelo núcleo)
│   ├── (raiz)                          entregas do Diretor de copy
│   ├── big-idea-e-voz/                 voz-<slug>.md, voz do avatar, Big Idea de cada ação e de cada evento (ht-diretor-copy)
│   ├── briefs/                         brief de copy por pedido (ht-diretor-copy)
│   ├── paginas-e-emails/               EXCEÇÃO ht-copy-paginas-e-emails (inclui pagina-sessao/)
│   └── anuncios-e-mensagens/           EXCEÇÃO ht-copy-anuncios-e-mensagens (inclui criativos/, convites, mensagens)
│   Todo arquivo com estado: rascunho / em revisão / aprovado pelo revisor / aprovado pelo estrategista
├── 09-visual/                        Dono: ht-diretor-arte (subpastas criadas pelo núcleo)
│   ├── (raiz)                          entregas do Diretor de arte
│   ├── direcao/                        direcao-<slug>.md com tokens, tipografia, foto, proibições (ht-diretor-arte)
│   ├── briefs/                         brief visual por pedido, inclusive o da página de inscrição (ht-diretor-arte)
│   ├── decks-e-slides/  criativos/<AAAA-MM-DD>-<acao>/  carrosseis/  video/   EXCEÇÃO ht-designer
│   └── paginas/<nome>/                 EXCEÇÃO ht-web-designer: código, prévia, teste/ (inclui paginas/pagina-sessao/)
├── 10-trafego/                       Dono: ht-gestor-trafego
│   plano, públicos, nomenclatura com o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver, planilha D-1, relatórios; campanha nasce PAUSADA
├── 11-automacoes/                    Dono: ht-gestor-automacoes
│   um fluxo por subpasta (desenho.md, teste/): lembretes-sessao/, pagina-sessao/, avaliacao-reunioes/…; nada liga sem OK
├── 12-revisoes/                      Pareceres: ht-revisor-metodo-copy e ht-revisor-visual
│   ├── pedidos/                        QUALQUER agente: <AAAA-MM-DD>-<nn>-pedido-revisao.md (pedido da própria entrega)
│   ├── <AAAA-MM-DD>-<nn>-parecer.md            ht-revisor-metodo-copy
│   ├── <AAAA-MM-DD>-<nn>-parecer-visual.md     ht-revisor-visual
│   └── prints/<nn>/                    ht-revisor-visual
└── 13-aprendizados/                  Dono: ht-diretor
    debrief de cada ação; cada agente manda o seu rascunho pelo handoff (escrito na própria subpasta) e o Diretor grava
```

Regras da pasta:
- Preço, entrada, parcela, bônus e garantia só existem em `02-oferta/` (a vigente; antes da Aprovação 1, a proposta vN, pela regra
  de leitura da oferta do protocolo, seção 4, regra 4). Qualquer outro arquivo **cita** esse arquivo; nunca copia o número sem dizer
  a versão.
- **Versão de rascunho**: rascunho corrigido depois de parecer é arquivo novo com a data do dia (o anterior vai para `historico/`);
  a versão citada por quem usa é a data do rascunho (ex.: "definição 2026-11-24"). Nota de correção no mesmo arquivo só para erro
  de digitação que não muda conteúdo. A oferta completa é a única com número de versão (`oferta-proposta-vN.md`).
- **Pasta ainda vazia**: quem depende dela segue com `[A CONFIRMAR COM <dono>]` (protocolo, seção 2, passo 6). O Diretor pede ao
  dono na mesma onda; não espera a pasta encher para despachar o resto.
- Dado de aluno e lead fica no `privado/` correto (regra acima), sem ir para material público.
- Arquivo substituído não é apagado: vai para `historico/` da mesma subpasta, com data no nome.
- Nome de arquivo: `AAAA-MM-DD-<assunto>.md` (ou a extensão do formato), sem espaço e sem acento.

### 2.1 Quem despacha quem (limite de 3 níveis)

O Claude Code aceita até 3 níveis de subagente: estrategista → `ht-diretor` (1) → estrategista ou T0 (2) → especialista ou núcleo (3).
Só têm a ferramenta Agent o `ht-diretor` e os 5 estrategistas (produto, comercial, demanda, eventos, sucesso). O núcleo e os
especialistas não despacham ninguém.

- **Diretor de copy e Diretor de arte não têm a ferramenta Agent.** Escrevem o brief (`08-copy/briefs/`, `09-visual/briefs/`)
  e devolvem ao estrategista que pediu a lista "peça → executor"; **o estrategista despacha** os copywriters, o designer e o web
  designer, e devolve a peça ao diretor do núcleo para a aprovação interna antes do revisor.
- Pedido pequeno de uma pasta só: o Diretor pode despachar direto o especialista (nível 2).

### 2.2 Promoção da oferta a vigente

A proposta (`02-oferta/oferta-proposta-vN.md`) só vira `02-oferta/oferta-vigente.md` com a **Aprovação 1 registrada** em
`00-plano/aprovacoes.md`. Quem grava é o **`ht-arquiteto-oferta`, sob ordem do Diretor** (pedido em `00-plano/pedidos/`); a
versão anterior vai para `02-oferta/historico/` com data. O Diretor não escreve em `02-oferta/`. Mudou a oferta depois: nova
proposta, nova Aprovação 1, nova promoção.

### 2.3 Big Idea de evento

A Ficha do Evento (`05-eventos/<evento>/estrategia/ficha-do-evento.md`, do `ht-estrategista-eventos` pela `ht-decisao-de-evento`)
traz formato, definição de resultado, metas e orçamento. A **Big Idea** do evento é proposta pelo **`ht-diretor-copy`** em cima
da Ficha (3 candidatas, a recomendada na a)), gravada em `08-copy/big-idea-e-voz/`. Se ela diverge da Ficha (promessa, data, CTA),
não se escolhe por conta própria: vira decisão numerada ao estrategista, pelo Diretor. A escolhida é citada na Ficha pelo estrategista.

## 3. Formato do handoff

Todo trabalho começa com um **pedido do Diretor** e termina com uma **entrega do agente**. Sem pedido, o agente não começa;
sem entrega no formato, o Diretor não aceita.

### 3.1 Pedido do Diretor
Arquivo `00-plano/pedidos/<AAAA-MM-DD>-<nn>-<skill>.md`:

```markdown
# Pedido <AAAA-MM-DD>-<nn>
- Expert: <slug>
- Pedido do estrategista (origem): <o que ele pediu, nas palavras dele, resumido>
- Ciclo / etapa da rota: <criar|vender|entregar|renovar> / <0-6 ou gestão>
- Agente: <ht-...>        Skill: <ht-...>
- Objetivo: <o que fica pronto, em 1 frase>
- Entradas (ler antes): <arquivos com caminho; versão de 02-oferta usada>
- Saída esperada: <artefato, formato, onde gravar>
- Restrições: <decisões que se aplicam, o que não pode; nunca "ler material de lançamento pago" como régua de método>
- Variáveis compartilhadas (copiadas de `00-plano/variaveis.md`, com a data da versão; obrigatório quando há pedido paralelo):
  - Nome do programa: <…>            Promessa / Roma: <…>
  - Big Idea da ação: <… ou "não se aplica">
  - Nome da sessão 1a1: <de 03-sessao/nome-da-sessao.md ou [A CONFIRMAR COM ht-closer]>
  - Dia e horário da aula semanal / da live: <…>   Destino de cada CTA (URL ou "página X"): <…>
  - Datas-chave: <Aprovação 2, abertura de captação, portão D-15, data do evento>   Oferta usada: <arquivo e versão>
  - Pedidos irmãos (correm em paralelo e usam as mesmas variáveis): <nn, nn>
- Critério de pronto: <checklist objetivo, copiado da skill e ajustado>
- Revisor: <ht-revisor-metodo-copy | ht-revisor-visual | ambos>
- Prazo: <data>
- Aprovação 1 existe? <sim (data) | não: só pesquisa/oferta>
```

### 3.2 Entrega do agente
Arquivo na subpasta do agente, `<AAAA-MM-DD>-<nn>-entrega.md`, ao lado do artefato:

```markdown
# Entrega do pedido <AAAA-MM-DD>-<nn>
- Agente / skill: <ht-...> / <ht-...>
- Artefatos: <caminhos>
- O que foi feito: <3 a 6 linhas>
- Fontes usadas: <02-oferta vX, arquivos de 01-pesquisa, skills do método; sem nomear curso, trilha, live ou mentor de origem>
- Evidência: verificado <o quê e como> | feito sem teste <o quê> | inferido <o quê>
- Números: <cada número usado e a fonte; "referência/conferir" quando vier de referência do método ou de caso parecido do nicho>
- Critério de pronto: <cada item marcado [x] ou [ ] com o motivo>
- Auditoria final: <erros típicos conferidos e o que foi corrigido>
- Assumi: <PREFIXO-n: o que foi decidido pelo padrão ou pela recomendação, em linguagem simples; citar a suposição de outro agente pelo código dele> (ou "nada"); pedido de OK: <só aprovação, envio, verba, ativação ou data pública, numa frase "posso seguir?"> (ou "nenhum")
- Variáveis compartilhadas usadas: <versão de 00-plano/variaveis.md>; divergência encontrada: <qual, ou "nenhuma">
- Lacunas: <o que faltou e não foi inventado>
- Próximo: <revisor> → depois <agente seguinte>
- Debrief (se fechou uma ação): <link para 13-aprendizados/>
```

### 3.3 Revisão
O agente que entregou grava o pedido em `12-revisoes/pedidos/<AAAA-MM-DD>-<nn>-pedido-revisao.md` (número do pedido, revisor,
caminho da entrega e dos artefatos, o que conferir). O revisor grava o parecer em `12-revisoes/<AAAA-MM-DD>-<nn>-parecer.md`
(texto) ou `-parecer-visual.md` (peça, com prints em `12-revisoes/prints/<nn>/`): veredito (aprovado / aprovado com ajustes / reprovado),
achados numerados com trecho e correção, checagem de método do Squad HT, de copy (anti-IA, anti-bajulação) e de compliance Meta quando
for anúncio. Reprovado volta ao agente com o mesmo número de pedido. Aprovado segue ao Diretor, que leva ao estrategista.

### 3.4 Estados de um artefato
`rascunho` → `em revisão` → `aprovado pelo revisor` → `aprovado pelo estrategista` → `no ar / enviado`. Só o último estado pode
sair para expert, lead ou aluno, e só pela mão (ou pelo OK explícito) do estrategista.

### 3.5 Numeração das suposições (prefixo por agente)

Regra completa no `ht-protocolo` §6. Cada agente usa o prefixo abaixo, com número que só cresce no projeto; o Diretor consolida
em `00-plano/decisoes.md` como `D1, D2…` com os códigos de origem ao lado.

| Prefixo | Agente | Prefixo | Agente |
|---|---|---|---|
| DD | ht-diretor (as próprias) | DE | ht-estrategista-conteudo |
| DG | ht-gestor-projetos | DS | ht-sdr |
| DN | ht-controller (números) | DC | ht-closer |
| DR | ht-revisor-metodo-copy | DTC | ht-treinador-comercial |
| DRV | ht-revisor-visual | DPE | ht-produtor-eventos |
| DEP | ht-estrategista-produto | DRP | ht-roteirista-palco |
| DED | ht-estrategista-demanda | DI | ht-ingressos-e-patrocinio |
| DEC | ht-estrategista-comercial | DDS | ht-diretor-desafio |
| DEV | ht-estrategista-eventos | DCS | ht-cs |
| DES | ht-estrategista-sucesso | DAE | ht-arquiteto-entrega |
| DP | ht-pesquisador | DRN | ht-gestor-renovacao |
| DK | ht-consultor-casos | DDC | ht-diretor-copy |
| DA | ht-arquiteto-oferta | DCP | ht-copy-paginas-e-emails |
| DT | ht-gestor-trafego | DCA | ht-copy-anuncios-e-mensagens |
| DAU | ht-gestor-automacoes | DDA | ht-diretor-arte |
| DDE | ht-designer | DW | ht-web-designer |

### 3.6 Variáveis compartilhadas (`00-plano/variaveis.md`)

Arquivo do Diretor, uma linha por variável, com valor, estado (`proposta` / `decidida em D<n>`), dono que propõe e data. Antes de
despachar dois ou mais pedidos que se tocam (ex.: aula semanal e tráfego, página e anúncio, live e convite), o Diretor preenche as
variáveis que eles compartilham e copia o bloco em cada pedido. Variável ainda não aprovada vai como `proposta` (o padrão recomendado) e todos usam
o mesmo valor. Agente que precisa mudar uma variável não muda sozinho: devolve ao Diretor, que atualiza o arquivo e avisa os pedidos
irmãos. Alternativa quando não dá para fixar antes: sequenciar (conteúdo → tráfego; nome da sessão → página).
