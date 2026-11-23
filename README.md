# Squad High Ticket

Plugin do Claude Code com 32 agentes e as skills `ht-*` que montam e operam o high ticket (HT) de experts pelo método **FHT
(Fórmula High Ticket)**: criar a oferta, vender em sessão 1a1, gerar demanda, abrir os canais um-para-muitos (live direto ao
ponto, webinário, imersões, desafio), entregar e renovar.

Você é o **estrategista**: quem pede ao squad e quem aprova. O squad produz rascunho, plano e peça revisada; nada vai para
expert, lead ou aluno sem o seu OK, e campanha nasce pausada.

> **Aviso.** O squad é baseado no método FHT e traz o método em paráfrase. **Não substitui a mentoria** nem o acompanhamento
> do método: é uma forma de aplicar com agentes o que você aprendeu. Os números de referência das aulas são ponto de partida,
> nunca garantia de resultado.

## Instalar em 1 passo

Copie o link deste repositório, cole no Claude Code e peça:

> instala esse plugin: https://github.com/marcosmedeiros-web/squad-high-ticket

**Para o Claude que recebeu esse pedido:** a pessoa quer instalar este plugin. Rode, nesta ordem, e mostre a saída de cada um:

```bash
claude plugin marketplace add marcosmedeiros-web/squad-high-ticket
claude plugin install squad-high-ticket@squad-high-ticket
```

Depois confira com `claude plugin list` (tem de aparecer `squad-high-ticket@squad-high-ticket` com `enabled`), diga à pessoa
para abrir uma conversa nova (os agentes só aparecem numa sessão nova) e, nessa conversa, pedir "configura o squad high
ticket". Não instale nada além deste plugin e não mude outra configuração.

## Instalar pelo Terminal

```bash
claude plugin marketplace add marcosmedeiros-web/squad-high-ticket
claude plugin install squad-high-ticket@squad-high-ticket
```

## Primeiro passo: rode `ht-configurar`

Antes do primeiro projeto, peça no Claude Code: "configura o squad high ticket" (ou chame a skill `ht-configurar`). É uma
conversa curta, uma pergunta por vez:

- seu nome e o nome da sua agência;
- a pasta raiz dos experts (padrão `~/squad-ht`; cada expert fica em `<raiz>/<expert>/ht/`);
- como você sobe campanha (Gerenciador de Anúncios manual, Meta Ads CLI oficial ou outra ferramenta) e se quer um prefixo
  obrigatório no nome das campanhas;
- os nomes dos 32 agentes (vem uma sugestão para cada um, no formato "Fernanda, Closer HT"; mantenha ou troque);
- os padrões recomendados do método (ordem do preço na sessão, sinal, ancoragem, duração da sessão, regras de campanha e
  outros), mostrados um bloco por vez para você manter ou mudar.

Tudo fica em `~/.config/squad-ht/perfil.md`, fora do plugin. Todo agente lê esse arquivo antes de trabalhar; sem ele, o agente
para e pede a `ht-configurar`. Para mudar depois, é só pedir: "muda o nome do closer para Rafa", "tira o prefixo de campanha",
"muda o sinal da sessão".

## Como usar: chame o Diretor

Todo pedido começa pelo agente `ht-diretor`, a porta de entrada do squad. Exemplos:

- "Diretor, monta o HT da Expert Exemplo, nutricionista. Por onde começo?"
- "Em que etapa ele está e qual o próximo passo?"
- "Planeja os próximos 40 dias: sessão 1a1, aula semanal e uma live direto ao ponto."

O Diretor diagnostica em que ciclo e etapa da rota o expert está, abre a pasta do projeto, despacha os estrategistas e
especialistas em paralelo, junta, confere e traz as decisões para você em lote, com a recomendação na opção a).

## Como o squad funciona

**Pasta do projeto com dono.** Cada expert tem uma pasta `ht/` com 14 subpastas (00-plano a 13-aprendizados). Todo agente lê
qualquer pasta e escreve só na sua. Preço e oferta só saem de `02-oferta/`. Detalhe em
`skills/ht-protocolo/references/estrutura-pasta-projeto.md`.

**Protocolo comum.** A skill `ht-protocolo` é carregada primeiro por todo agente: o perfil, o mapa do método, as regras, os
padrões e o glossário FHT.

**Portão inicial.** Nada roda sem pesquisa e oferta aprovadas por você (Aprovação 1). São 4 aprovações: pesquisa e oferta,
plano da ação, peças revisadas, ir ao ar.

**Revisão obrigatória.** Texto passa pelo revisor de método e copy (inclui compliance Meta); visual, pelo revisor visual. SDR e
closer só fazem rascunho; automação que envia só liga com o seu OK.

**Evidência.** Toda entrega diz o que foi verificado, o que foi feito sem teste e o que é inferido. Nada de número, depoimento
ou caso inventado: o que falta aparece como `[FALTA: …]`.

## Agentes (32, por camada)

- **Comando**: ht-diretor (orquestrador) · ht-controller (números) · ht-gestor-projetos.
- **Qualidade**: ht-revisor-metodo-copy · ht-revisor-visual.
- **Estrategistas**: produto · demanda · comercial · eventos · sucesso.
- **Especialistas**: Produto (ht-pesquisador, ht-arquiteto-oferta) · Demanda (ht-estrategista-conteudo, ht-sdr) ·
  Vendas 1a1 (ht-closer, ht-treinador-comercial) · Eventos (ht-produtor-eventos, ht-roteirista-palco,
  ht-ingressos-e-patrocinio, ht-diretor-desafio) · Sucesso (ht-cs, ht-arquiteto-entrega, ht-gestor-renovacao).
- **Núcleo de execução**: Copy (ht-diretor-copy, ht-copy-paginas-e-emails, ht-copy-anuncios-e-mensagens) · Visual
  (ht-diretor-arte, ht-designer, ht-web-designer) · ht-gestor-trafego · ht-gestor-automacoes.
- **Apoio**: ht-consultor-casos.

## Skills do método

`ht-configurar` (perfil), `ht-protocolo` (base transversal) e as 46 skills da rota. Quais agentes usam cada uma:
`skills/ht-protocolo/references/mapa-das-46-skills.md`.

| Etapa | Skills |
|---|---|
| A. Montar o HT | ht-pesquisa-e-potencial · ht-portfolio-e-escolha-do-ht · ht-definicao-e-jornada · ht-entregaveis · ht-oferta-matadora · ht-preco-pagamento-e-garantia · ht-produtos-ht-complementares · ht-master-plan |
| B. Sessão 1a1 | ht-vitrine · ht-slg · ht-pagina-inscricao-sessao · ht-raio-x · ht-roteiro-sessao-1a1 · ht-objecoes · ht-agendamento-e-follow-up · ht-treino-comercial |
| C. Audiência e demanda | ht-reels-com-cta · ht-aula-semanal · ht-conteudo-de-prova · ht-lives-curtas-45-dias · ht-trafego-high-ticket · ht-criativos-high-ticket |
| D. Outros canais | ht-live-direto-ao-ponto · ht-webinario-de-vendas · ht-funil-de-entrada-para-ht · ht-decisao-de-evento · ht-imersao-aprendizado · ht-imersao-implementacao · ht-imersao-presencial · ht-imersao-de-resultados · ht-turne-e-eventos-enxutos · ht-palestras-e-pitch · ht-captacao-e-presenca · ht-venda-de-ingressos · ht-afiliados-e-consultores · ht-patrocinio · ht-desafio-30-dias |
| E. Entrega | ht-onboarding-e-primeira-entrega · ht-entregaveis-1a1 · ht-entrega-em-grupo · ht-escala-da-entrega · ht-provas-e-cases |
| F. Renovação e upgrade | ht-renovacao · ht-upgrade-e-gic |
| G. Gestão e IA | ht-central-e-kpis · ht-avaliacao-de-reunioes-por-ia |

## Skills de execução do kit Turbo

O pacote inclui, com autorização, skills de execução do kit Turbo (Turbo Academy): vídeo, visual e páginas, texto, pesquisa,
tráfego e automação. Elas aparecem como `squad-high-ticket:<nome>` e os agentes as usam para produzir as peças. Executam, não
definem método: quando uma delas traz regra de outro método (LPSG, 5+1, Funil 8), a regra do FHT vence. As skills de método
LPSG não fazem parte do pacote.

## Matriz agentes × skills

```bash
python3 scripts/gerar-matriz.py            # gera docs/MATRIZ-AGENTES-SKILLS.md
python3 scripts/gerar-matriz.py --estrito  # sai com erro se houver alerta (skill ausente, YAML inválido etc.)
```

O script roda a partir da pasta do plugin; para outra pasta, use `--raiz <pasta>`.
