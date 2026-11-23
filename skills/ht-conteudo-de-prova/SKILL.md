---
name: ht-conteudo-de-prova
description: 'Monta as linhas de prova que vendem HT: podcast com quem teve resultado, cortes com CTA para a origem e consultoria ao vivo com um escolhido da audiência. Use para "monta o podcast do expert", "plano de cortes da live", "quero fazer consultoria ao vivo". NÃO use para Reels (ht-reels-com-cta), aula semanal nem depoimento (ht-provas-e-cases).'
---

# Conteúdo de prova: podcast HT, cortes e consultoria ao vivo

## 1. Para que serve e o que entrega

Serve para o expert demonstrar, em conteúdo denso, que sabe gerar resultado: entrevistando quem já teve resultado com o método dele (podcast HT), resolvendo ao vivo o problema de uma pessoa da audiência (consultoria ao vivo) e espalhando os melhores trechos disso tudo em cortes que mandam de volta para a origem. No método esses formatos fazem parte do cardápio de cinco linhas editoriais (aula semanal, consultoria ao vivo, Reels raiz, podcast HT e cortes), e todas terminam ligadas a um funil de venda HT.

**Entrega** (uma pasta em `experts/<slug>/ht/04-demanda/conteudo-de-prova/`):
- `plano-linhas-de-prova.md`: quais dos três formatos rodar, em que ordem, frequência, funil de destino de cada um (direto ou indireto) e métrica semanal.
- `podcast/pauta-<convidado>.md`: ficha do convidado, pauta de entrevista, pontos de seeding e CTA final (modelo em `references/roteiro-podcast-ht.md`).
- `consultoria-ao-vivo/`: tema, formulário de aplicação com a pergunta de repescagem, critério de escolha, roteiro da sessão ao vivo e fluxo dos não escolhidos (modelo em `references/consultoria-ao-vivo.md`).
- `cortes/plano-de-cortes-<origem>.md`: lista de cortes com arquivo de origem, tempos, primeiras e últimas palavras, ideia central e CTA para a origem (modelo em `references/plano-de-cortes.md`).
- Nomes de arquivo no padrão do `ht-protocolo` (`AAAA-MM-DD-<assunto>.md`, sem acento). Gravação bruta, transcrição de entrevista, respostas do formulário e autorizações ficam em `04-demanda/conteudo-de-prova/privado/`, nunca em material público.
- Copy final (convites, legendas, texto do formulário, CTA falado) vai para `08-copy/`; capas e vinhetas para `09-visual/`.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, preço só de `02-oferta`, nada inventado) e conferir o pedido do Diretor em `00-plano/` e a Aprovação 1; sem os dois, não começa.
2. Ler da pasta `experts/<slug>/ht/`:
   - `02-oferta/` (promessa, definição do AR, jornada: o que a consultoria ao vivo resolve e o que o seeding cita);
   - `01-pesquisa/` (onde o avatar mais trava, objeções, âncoras: escolhe o tema da consultoria e o ângulo dos cortes);
   - `04-demanda/` (a aula semanal já existe? qual dia e hora? o plano de Reels: os cortes entram no rodízio de lá);
   - `06-entrega/` e o catálogo de resultados da ht-provas-e-cases (quem teve resultado e pode ser entrevistado);
   - `03-sessao/` (como a sessão 1a1 é chamada e agendada: destino dos não escolhidos).
3. Entradas obrigatórias: oferta aprovada (Aprovação 1 do estrategista), pelo menos um funil HT ativo para receber o CTA (sessão 1a1, aula semanal ou imersão) e as gravações que existem (aula semanal, lives, consultorias, plantões).
4. Se faltar, pergunte só isto (no máximo 3):
   - "Quem já teve resultado com o método do expert e toparia uma entrevista? (aluno, paciente/cliente ou alguém da aula semanal)"
   - "Quanto de energia e agenda o expert tem por semana para conteúdo ao vivo?"
   - "Qual funil recebe o CTA agora: sessão 1a1, aula semanal ou imersão?"

## 3. Passo a passo

### 3.1 Plano das linhas de prova
1. Listar os formatos densos que o expert já faz ou pode fazer: aula semanal (da ht-aula-semanal), consultoria ao vivo, Reels raiz (da ht-reels-com-cta), podcast HT. Cortes são o quinto formato e sempre nascem dos outros.
2. Escolher pelo que existe e pela energia do expert. O material permite combinar vários; a regra é ver a disposição de energia.
   - Sem nenhum caso de resultado ainda: não começar pelo podcast (quem aplicou o conteúdo da aula semanal já pode ser entrevistado). Recomendação desta skill: começar pela consultoria ao vivo, que gera o primeiro caso na frente da audiência.
   - Com aula semanal rodando: **1 a 2 cortes dirigidos por aula**, só dos trechos mais fortes, escolhidos pelo estrategista (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Contexto: o foco da aula é o cadastro; os cortes entram no cardápio com CTA para a origem; corte mal feito deixa o conteúdo raso, por isso o limite de 1 a 2.
3. Ligar cada formato a um funil HT: **direto** (sessão individual ou imersão) ou **indireto** (outra linha editorial, como aula semanal ou consultoria, que depois leva ao funil direto). Nenhum formato sai sem destino.
4. Definir a métrica semanal por formato: aplicações, sessões marcadas e vendas que vieram dele (o material destaca que essas linhas permitem medir o retorno semana a semana).
5. Registrar o ciclo que o plano alimenta: vende, gera resultado, entrevista, Toque de Midas, mais autoridade, mais vendas. A parte de Toque de Midas é da ht-provas-e-cases.

### 3.2 Podcast HT (entrevista com quem teve resultado)
1. **Quem entrevistar:** pessoas que tiveram resultado implementando a metodologia do expert. Não precisa ser só aluno pagante: pode ser alguém da aula semanal que aplicou o conteúdo. Puxar a lista do catálogo de resultados (ht-provas-e-cases).
2. **Formato:** entrevista fechada no Zoom (ou gravação equivalente), sem audiência assistindo, para a pessoa ficar à vontade. Só o expert, ou alguém da equipe, e o convidado. A entrevista pode ser linha editorial do expert ou um processo da equipe interna (às vezes é o editor de vídeo que entrevista, seguindo um roteiro).
3. **Pauta:** usar os tópicos do material (situação antes, o que fez para superar, obstáculos, como resolveu, resultado, o que mais ajudou, dica para quem está começando) e montar a pauta pelo modelo de `references/roteiro-podcast-ht.md`. O material só tem tópicos; o encadeamento do modelo é proposta da skill.
4. **Seeding:** durante a entrevista, buscar fazer seeding do programa (o entregável, o momento da jornada ou a sacada do mentor que destravou o convidado), sem pitch.
5. **CTA final:** para algum funil de venda HT (direto ou indireto), com a mesma promessa da oferta. Preço nunca no podcast.
6. **Autorização:** antes de gravar, o convidado autoriza uso público e uso em cortes; nicho de saúde exige conferir as regras do conselho profissional do expert para depoimento de resultado (o método não trata disso: ver Limites). Sem autorização escrita, a entrevista vira só material interno de prova.
7. **Depois de gravar:** entra no catálogo de resultados como prova por nicho (o caso no catálogo aponta para a entrevista completa) e vira matéria-prima de cortes (3.4) e de Toque de Midas (ht-provas-e-cases). Conferir onde a entrevista pode virar post fixado de Evidência com a ht-vitrine.

### 3.3 Consultoria ao vivo na audiência
1. **O que é:** consultoria individual, ao vivo, com o expert (ou mentor) e uma pessoa escolhida da audiência. Referência citada no material: a mesa em que dois especialistas atendiam uma pessoa ao vivo.
2. **Tema:** o ponto em que o avatar mais trava, resolvido de ponta a ponta na frente de todos (o exemplo é construir ao vivo a oferta do HT de uma pessoa). Sai de `01-pesquisa/`.
3. **Aplicação obrigatória:** a audiência preenche um formulário para concorrer. Ele serve a dois fins ao mesmo tempo: escolher quem recebe a consultoria e qualificar leads para o HT. Modelo do formulário em `references/consultoria-ao-vivo.md`.
4. **Pergunta de repescagem no formulário:** se não for escolhido desta vez, a pessoa quer um contato individual do time para conversar sobre um acompanhamento? É ela que transforma a consultoria em fila de sessão 1a1.
5. **Escolha:** um escolhido por consultoria, pelo critério do modelo (caso que ensina o máximo para a audiência e tem o perfil do avatar).
6. **Não escolhidos qualificados:** quem tem perfil para o HT e respondeu sim na repescagem recebe contato individual e é convidado para a sessão 1a1 (passa para ht-agendamento-e-follow-up e ht-roteiro-sessao-1a1). Quem não respondeu sim, mas é qualificado, entra na lista da ht-slg.
7. **Contexto que funciona:** a oferta precisa ser feita para a turma presente (ao vivo, na aula semanal ou numa live), com aplicação. Uma oferta de consultoria gratuita mandada por mensagem a 600 pessoas não teve nenhuma resposta. Não repetir esse formato.
8. **Frequência:** padrão de uma por semana. Ajustar à energia do expert (assumo o padrão e listo em "Assumi").
9. **Roteiro ao vivo:** abertura com o porquê, apresentação do escolhido, diagnóstico rápido, construção ao vivo, recapitulação do que a audiência aprendeu, CTA (modelo em `references/consultoria-ao-vivo.md`, marcado como proposta da skill onde o material não detalha).
10. **Variantes citadas, sem receita:** a linha em formato de episódio em que o expert monta ao vivo o plano completo de um empresário convidado ("O plano perfeito") e a ideia de uma linha de "desconstrução" em que o expert faz ao vivo a engenharia reversa do resultado de um aluno, para gerar entrevistas e material de Toque de Midas (dita como plano). Usar só como ideia de formato, nunca como método.

### 3.4 Cortes com CTA para a origem
1. **Lógica F1:** a corrida inteira, a corrida resumida e os melhores momentos. Aqui: o conteúdo denso inteiro (aula semanal, live, consultoria, podcast), uma versão compactada quando fizer sentido e os cortes (highlights, as melhores sacadas).
2. **De onde cortar:** só de conteúdo denso que já existe: aula semanal, lives, consultorias ao vivo, podcast. Usar `transcrever-youtube` ou `watch` para achar os trechos com tempo.
3. **Direção antes do editor:** quem conhece o método (expert ou estrategista) escolhe os trechos e escreve a instrução de cada corte: arquivo de origem, tempo de início com as primeiras palavras, tempo de fim com as últimas palavras, a ideia que o corte prova. O editor só corta depois. Essa regra vem do Toque de Midas e a skill a aplica a todo corte: sem direção, o corte vira loteria.
4. **Todo corte tem CTA para o formato de origem.** Molde do material: o vídeo foi um trecho da [origem], que acontece toda [dia] às [hora]; vai lá e se inscreve. Os CTAs finais seguem o rodízio da ht-reels-com-cta; o destino padrão é a origem (funil indireto), e a origem leva ao funil direto.
5. **Formato de publicação:** o corte publicado como Reels segue as regras da ht-reels-com-cta (duração até 90 s pelo padrão do squad, legenda, edição, horário, frequência, distribuição). Esta skill entrega o plano de cortes e o CTA; a edição e a postagem são de lá.
6. **Qualidade:** o material alerta que o método de picotar conteúdo raiz funciona, mas corte mal executado, sem sentido, deixa o conteúdo raso. Corte que não se sustenta sozinho (sem contexto, ideia pela metade) não entra.
7. Checklist completo e ficha de cada corte: `references/plano-de-cortes.md`.

## 4. Regras inegociáveis do método

- Só produzir conteúdo conectado a funil de venda HT; todo formato termina com CTA ou link para um funil, direto ou indireto.
- Conteúdo de prova é denso: tempo para mostrar conhecimento, resultado próprio e resultado de clientes (os três elementos de autoridade do material).
- Podcast entrevista quem teve resultado com a metodologia; resultado inventado, combinado ou "arredondado" é proibido. Número dito pelo convidado entra com a fonte (minuto da gravação) e, se a legenda for duvidosa, marcado "conferir".
- Entrevista não é paga nem roteirizada para o convidado: a pessoa conta a própria história.
- Consultoria ao vivo sempre com aplicação e com a pergunta de repescagem; não escolhido qualificado vai para sessão 1a1.
- Consultoria gratuita oferecida por mensagem, sem aplicação e sem a turma presente, não é usada.
- Todo corte tem CTA para a origem; corte só com instrução escrita (origem, tempos, primeiras e últimas palavras).
- Preço, condições e bônus nunca aparecem nesses formatos; preço e oferta só saem de `02-oferta` e só são falados na sessão 1a1 ou no evento.
- Padrão do squad: aula semanal de 1 h (a origem principal dos cortes) e Reels até 90 s, com o raiz longo como variante (vale para o corte publicado como Reels).

## 5. O que o agente decide e o que pede OK

Sem lote de perguntas nem a/b/c: o agente segue o padrão e lista em "Assumi: … (é só pedir para mudar)". Pede um "posso seguir?" simples só no que sai para fora, gasta ou mexe em preço.
- **Formato e frequência**: padrão cortes da aula semanal, 1 a 2 dirigidos por aula (dá para mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Consultoria ao vivo semanal entra quando há audiência presente e o expert topa se expor (gera caso e lead já na primeira semana).
- **Quem conduz a entrevista**: assume o expert (faz seeding melhor); a equipe entra quando ele não tiver agenda.
- **Publicar um caso** com autorização parcial, ou em nicho de saúde com regra do conselho incerta: o agente deixa de fora; publicar: "posso seguir?".
- **Destino do CTA** com mais de um funil ativo: assume a aula semanal (ou a sessão 1a1, se não houver aula).
- **Ligar qualquer envio** a lead ou aluno (convite da consultoria, contato com não escolhidos, aviso do episódio): "posso seguir?".

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Cada formato do plano tem funil de destino (direto ou indireto), frequência, dono e métrica semanal.
- [ ] Pauta de podcast com ficha do convidado, resultado com fonte, perguntas, pontos de seeding e CTA; autorização registrada.
- [ ] Consultoria ao vivo com tema vindo da pesquisa, formulário com pergunta de repescagem, critério de escolha, roteiro e fluxo dos não escolhidos até a sessão 1a1.
- [ ] Plano de cortes com origem, tempos, primeiras e últimas palavras, ideia, CTA para a origem e destino de publicação (ht-reels-com-cta).
- [ ] Nenhum preço, nenhum número sem fonte, nenhum caso sem autorização.

**Auditoria (erros típicos, rodar antes de entregar):**
1. Conteúdo "solto", sem CTA nem funil (o erro que o material mais combate).
2. Podcast com quem não teve resultado, ou com resultado vago ("melhorou muito") e sem número com período.
3. Entrevista virando pitch: o convidado elogia, o expert vende. Seeding é citar o que funcionou, não ofertar.
4. Consultoria ao vivo sem formulário, ou formulário sem a pergunta de repescagem (perde a fila de sessões).
5. Não escolhidos qualificados esquecidos depois da live (ninguém liga).
6. Corte sem contexto, cortado pelo editor sem direção, ou sem CTA para a origem.
7. Corte que promete o que a oferta não entrega (promessa do CTA diferente da promessa do produto).
8. Dado de cliente ou paciente exposto sem autorização; em saúde, depoimento publicado sem conferir a regra do conselho.
9. Linguagem de IA na pauta e nas legendas (passar `avoid-ai-writing` antes da revisão).

## 7. Saída e handoff

- Grava em `experts/<slug>/ht/04-demanda/conteudo-de-prova/` (plano, pautas, formulário, roteiro, planos de cortes).
- Copy final (convites, legenda, texto do formulário, CTA falado dos cortes) vai para `08-copy/` pelo Diretor de copy; capas, vinhetas e lettering para `09-visual/` pelo Diretor de arte.
- Revisão obrigatória, com pedido em `12-revisoes/pedidos/`: texto para o **Revisor de método e copy** (`ht-revisor-metodo-copy`, inclui compliance Meta quando o corte for impulsionado); peças visuais para o **Revisor visual** (`ht-revisor-visual`).
- Passa para: ht-reels-com-cta (edição e publicação dos cortes), ht-provas-e-cases (entrevista vira caso, Toque de Midas e catálogo), ht-agendamento-e-follow-up (não escolhidos e leads do podcast), ht-slg (qualificados sem sim na repescagem), Gestor de automações (formulário e avisos, só com OK do estrategista).
- Cada entrega fecha com o bloco de entrega do protocolo (nível de evidência, lacunas, decisões pendentes do estrategista).
- Corte impulsionado: a campanha é do `ht-trafego-high-ticket`, nasce PAUSADA com o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver, e só ativa com OK do estrategista.
- Debrief do ciclo em `13-aprendizados/` (aplicações e sessões por formato, cortes que mais levaram à origem).

## 8. Ferramentas de apoio (por nome, sem copiar)

- Achar trechos e transcrever: `transcrever-youtube`, `watch`.
- Cortar, legendar e montar: `cortes-tiktok`, `short-form-video`, `capcut-edit`, `caption-animation`, `lower-thirds` (nome e resultado do convidado), `testimonial-video` (só quando o corte for de depoimento, alinhado com ht-provas-e-cases).
- Gancho do corte: `hook-generator`. Texto: `avoid-ai-writing`, `humanizer`, `voice-builder`.
- Capa do episódio: `youtube-thumbnail`, `banner-design`.
- Formulário e avisos: `automacao-fluxos`, `conectar-whatsapp-oficial` (envio só com OK do estrategista).

## 9. Limites

**Não inventar:**
- Script de entrevista e roteiro do podcast: o método só traz tópicos de perguntas. O roteiro de `references/roteiro-podcast-ht.md` é proposta da skill.
- Roteiro da consultoria ao vivo e critério formal de escolha: o método não detalha; os modelos são proposta da skill.
- Duração, plataforma, periodicidade e formato de publicação do podcast (áudio, vídeo, YouTube): não definidos pelo método.
- Quantos cortes por conteúdo denso e duração ideal do corte: não definidos; vale o padrão do squad (Reels até 90 s) quando o corte vira Reels.
- Taxa de conversão de não escolhidos para sessão e de sessão para venda vinda da consultoria ao vivo: sem número de referência.
- Regras de conselho profissional (saúde, direito etc.) para depoimento de resultado: fora do método; conferir caso a caso antes de publicar.
