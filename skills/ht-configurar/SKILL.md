---
name: ht-configurar
description: 'Configura o Squad High Ticket para quem vai usar: conversa com você uma pergunta por vez (seu nome, agência, pasta raiz dos experts, ferramenta de tráfego, prefixo de campanha, nomes dos 32 agentes e os padrões recomendados do método) e grava o perfil em ~/.config/squad-ht/perfil.md, que todo agente ht-* lê antes de trabalhar. Também edita o perfil depois: "muda o nome do closer", "troca o prefixo de campanha", "muda o sinal da sessão", "mostra meu perfil". Use na primeira vez que instalar o squad, quando um agente avisar que o perfil não existe, ou para mudar qualquer campo. NÃO usar para montar o HT de um expert (isso é o ht-diretor).'
---

# Configurar o Squad High Ticket

## 1. Para que serve

Todo agente do squad começa lendo `~/.config/squad-ht/perfil.md`. É ali que mora quem aprova (você), onde ficam as pastas dos
experts, como você sobe campanha, o nome que cada agente usa e os padrões de método que o squad segue. Sem esse arquivo nenhum
agente começa. Esta skill cria o perfil numa conversa curta e depois edita qualquer campo a pedido.

Modelo com todos os campos e valores sugeridos: `references/perfil-modelo.md`.

## 2. Modo: criar ou editar

1. Conferir se `~/.config/squad-ht/perfil.md` existe.
2. **Não existe** → modo criar (seção 3).
3. **Existe** e o pedido é uma mudança ("muda o nome do closer para Rafa", "prefixo vazio", "sinal de R$ 300") → modo editar
   (seção 4). Existe e o pedido é genérico ("configura o squad") → mostrar o resumo do perfil atual e perguntar o que mudar.
   Nunca recriar do zero por cima de um perfil existente sem você pedir com essas palavras; antes de recriar, copiar o atual
   para `~/.config/squad-ht/historico/perfil-AAAA-MM-DD-HHMM.md`.

## 3. Modo criar (uma pergunta por vez)

Regras da conversa: **uma pergunta por mensagem**, esperar a resposta, nunca juntar duas. Toda pergunta mostra o valor
sugerido; "ok", "mantém" ou "pula" aceita a sugestão. "Para" interrompe: grava o que já foi respondido e completa o resto com
os valores do modelo, avisando quais ficaram no padrão.

1. **Seu nome.** "Como você quer ser chamado pelo squad? É você quem aprova tudo." → `estrategista`.
2. **Agência.** "Qual o nome da sua empresa ou agência? (opcional, pode pular)" → `agencia`.
3. **Pasta raiz.** "Onde ficam as pastas dos seus experts? Sugestão: `~/squad-ht`. Cada expert vira `<raiz>/<expert>/ht/`."
   → `raiz_projetos`. Se a pasta não existe, perguntar se pode criar; criar só com o sim.
4. **Ferramenta de tráfego.** "Como você sobe campanha na Meta? (a) Gerenciador de Anúncios manual: o agente entrega a
   especificação campo a campo e você sobe; (b) Meta Ads CLI oficial; (c) outra ferramenta ou CLI (qual?)." → `trafego.ferramenta`.
   Em qualquer opção, campanha nova nasce PAUSADA e só ativa com o seu OK.
5. **Prefixo de campanha.** "Quer um bloco obrigatório no nome de toda campanha, para saber o que o squad criou? Ex.: `[SQUAD HT]`.
   Vazio = sem prefixo." → `trafego.prefixo_campanha`.
6. **Acervo do método (opcional).** "Você tem acesso ao acervo de aulas do FHT numa pasta? Se sim, qual o caminho? Se não, pula:
   as skills já trazem o método em paráfrase." → `fontes_metodo`.
7. **Nomes dos agentes.** Mostrar a tabela abaixo (id, papel, nome sugerido) e perguntar: "Mantém esses nomes, quer trocar
   algum, ou prefere que os agentes se apresentem só pelo papel?". Troca vem como "closer = Rafa"; aceitar várias numa resposta.
   O agente se apresenta no formato "Nome, Função HT" (ex.: "Fernanda, Closer HT").
8. **Padrões.** Mostrar os padrões do modelo **um bloco por vez** (Oferta e preço, Sessão 1a1, Demanda e tráfego, Eventos,
   Aprovações), cada padrão numa linha com a chave e o valor, e perguntar por bloco: "Mantém esses padrões ou quer mudar algum?".
   Mudança vem como "sinal_sessao = R$ 300 a R$ 800". Não discutir método aqui: se a mudança contraria o FHT, registrar como você
   pediu e acrescentar um comentário `# diverge do padrão recomendado: <valor recomendado>` na linha.
9. **Revisão cruzada (opcional).** "Alguém além de você faz a verificação final do que o squad entrega? Se não, pula." → `revisao_cruzada`.
10. **Confirmar e gravar.** Mostrar o resumo (campos preenchidos e o que ficou no padrão), pedir o OK e gravar
    `~/.config/squad-ht/perfil.md` a partir do modelo, com permissão 600 (`chmod 600`). Criar a pasta `~/.config/squad-ht/` se
    não existir.

### Agentes e papéis (para a pergunta 7)

| id | papel | nome sugerido |
|---|---|---|
| ht-diretor | orquestrador, porta de entrada de todo pedido | Heitor, Diretor HT |
| ht-gestor-projetos | cronograma, prazos, rotina do expert | Priscila, Gestora de projetos HT |
| ht-controller | números, Master Plan, KPIs | Ricardo, Controller HT |
| ht-revisor-metodo-copy | portão de todo texto | Helena, Revisora de método e copy HT |
| ht-revisor-visual | portão de toda peça visual | Vera, Revisora visual HT |
| ht-estrategista-produto | lidera a oferta até a Aprovação 1 | Olívia, Estrategista de produto HT |
| ht-pesquisador | avatar, market fit, potencial | Pedro, Pesquisador HT |
| ht-arquiteto-oferta | dono da oferta e do preço | Otávio, Arquiteto de oferta HT |
| ht-consultor-casos | precedentes do nicho | Cecília, Consultora de casos HT |
| ht-estrategista-demanda | lidera a geração de leads | Diana, Estrategista de demanda HT |
| ht-estrategista-conteudo | Reels, aula semanal, vitrine | Clara, Estrategista de conteúdo HT |
| ht-sdr | lista, SLG, rascunhos de contato | Samuel, SDR HT |
| ht-estrategista-comercial | lidera a sessão 1a1 | Vitor, Estrategista comercial HT |
| ht-closer | roteiro da sessão, objeções, follow-up | Fernanda, Closer HT |
| ht-treinador-comercial | roleplay e auditoria de call | Tiago, Treinador comercial HT |
| ht-estrategista-eventos | escolhe e monta o evento um-para-muitos | Eduardo, Estrategista de eventos HT |
| ht-produtor-eventos | operação do evento | Gustavo, Produtor de eventos HT |
| ht-roteirista-palco | palestra, pitch, live | Rebeca, Roteirista de palco HT |
| ht-ingressos-e-patrocinio | ingressos, afiliados, patrocínio | Igor, Ingressos e patrocínio HT |
| ht-diretor-desafio | desafio de 30 dias | Daniel, Diretor de desafio HT |
| ht-estrategista-sucesso | experiência do aluno até a renovação | Sofia, Estrategista de sucesso HT |
| ht-arquiteto-entrega | desenho da entrega e da escala | Elisa, Arquiteta de entrega HT |
| ht-cs | dia a dia do aluno, NPS, provas | Marina, CS HT |
| ht-gestor-renovacao | renovação e upgrade | Renata, Gestora de renovação HT |
| ht-diretor-copy | Big Idea, voz, brief de copy | Bruno, Diretor de copy HT |
| ht-copy-paginas-e-emails | páginas e e-mails | Luana, Copy de páginas e e-mails HT |
| ht-copy-anuncios-e-mensagens | anúncios, Reels, mensagens | André, Copy de anúncios e mensagens HT |
| ht-diretor-arte | direção visual | Arthur, Diretor de arte HT |
| ht-designer | decks, slides, criativos, vídeos | Laís, Designer HT |
| ht-web-designer | páginas no ar | Wagner, Web designer HT |
| ht-gestor-trafego | campanhas Meta | Caio, Gestor de tráfego HT |
| ht-gestor-automacoes | fluxos, lembretes, CRM | Alice, Gestora de automações HT |

## 4. Modo editar

1. Ler o perfil atual e localizar o campo pelo pedido: "nome do closer" → `nomes_agentes.ht-closer`; "prefixo" →
   `trafego.prefixo_campanha`; "sinal" → `padroes.sinal_sessao`; "minha pasta" → `raiz_projetos`. Ambíguo: perguntar qual, numa
   linha, mostrando as opções.
2. Mostrar antes e depois ("`ht-closer`: Fernanda, Closer HT → Rafa, Closer HT") e pedir o OK.
3. Com o OK: copiar o perfil atual para `~/.config/squad-ht/historico/perfil-AAAA-MM-DD-HHMM.md` e gravar só o campo mudado,
   mantendo o resto e os comentários.
4. Conferir que o bloco YAML continua carregando (ex.: `python3 -c "import yaml,re,sys; t=open(sys.argv[1]).read();
   yaml.safe_load(re.search(r'```yaml\n(.*?)```', t, re.S).group(1))" ~/.config/squad-ht/perfil.md`). Falhou: voltar a cópia
   do histórico e avisar.
5. "Mostra meu perfil": exibir o resumo, sem editar.

Mudança de padrão vale para os projetos a partir de agora. Para mudar só num projeto, a decisão vai em `00-plano/decisoes.md`
daquele projeto (pelo ht-diretor), que vence o perfil ali.

## 5. Regras

- Nunca gravar senha, token, chave de API ou dado de cliente no perfil. Se você colar um token numa resposta, não gravar e avisar
  que ele deve ser trocado.
- O perfil é seu: a skill não muda nada sem o seu OK e não inventa valor. Campo sem resposta fica com o valor do modelo e é
  listado no resumo como "no padrão".
- O `name` técnico dos agentes (`ht-closer` etc.) nunca muda; só o nome de apresentação.

## 6. Critério de pronto

- [ ] `~/.config/squad-ht/perfil.md` existe, com permissão 600, e o bloco YAML carrega.
- [ ] `estrategista` e `raiz_projetos` preenchidos; `trafego.ferramenta` definido.
- [ ] Você viu o resumo e deu o OK antes da gravação.
- [ ] Em edição: cópia do perfil anterior em `~/.config/squad-ht/historico/`.

## 7. Saída

Mensagem curta: onde o perfil foi gravado, o que ficou no padrão e o próximo passo ("chame o ht-diretor com o nome do expert para
começar").
