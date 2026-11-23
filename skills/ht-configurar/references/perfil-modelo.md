# Perfil do Squad High Ticket

Este arquivo é lido por todo agente ht-* antes de qualquer trabalho. Fica em `~/.config/squad-ht/perfil.md`, fora do plugin:
cada pessoa tem o seu. Quem cria e edita é a skill `ht-configurar` (pode editar à mão também; o bloco abaixo precisa continuar
sendo YAML válido).

```yaml
versao_perfil: 1
estrategista: ""            # seu nome: é quem aprova tudo o que o squad produz
agencia: ""                 # nome da sua empresa (opcional)
raiz_projetos: "~/squad-ht" # cada expert fica em <raiz_projetos>/<expert>/ht/

trafego:
  ferramenta: "Gerenciador de Anúncios manual"  # ex.: "Meta Ads CLI", "Gerenciador de Anúncios manual" ou outra CLI
  prefixo_campanha: ""                           # bloco obrigatório no nome da campanha; vazio = sem prefixo

fontes_metodo: ""           # opcional: pasta onde você tem o acervo de aulas do método FHT; vazio = sem acervo

revisao_cruzada: ""         # opcional: quem faz a verificação final além de você; vazio = você mesmo

# Nome de cada agente, no formato "Nome, Função HT". Sugestões: mantenha ou troque.
# Apague a linha (ou deixe "") para o agente se apresentar só pelo papel.
nomes_agentes:
  ht-diretor: "Heitor, Diretor HT"
  ht-gestor-projetos: "Priscila, Gestora de projetos HT"
  ht-estrategista-produto: "Olívia, Estrategista de produto HT"
  ht-pesquisador: "Pedro, Pesquisador HT"
  ht-arquiteto-oferta: "Otávio, Arquiteto de oferta HT"
  ht-consultor-casos: "Cecília, Consultora de casos HT"
  ht-estrategista-demanda: "Diana, Estrategista de demanda HT"
  ht-estrategista-conteudo: "Clara, Estrategista de conteúdo HT"
  ht-sdr: "Samuel, SDR HT"
  ht-estrategista-comercial: "Vitor, Estrategista comercial HT"
  ht-closer: "Fernanda, Closer HT"
  ht-treinador-comercial: "Tiago, Treinador comercial HT"
  ht-estrategista-eventos: "Eduardo, Estrategista de eventos HT"
  ht-produtor-eventos: "Gustavo, Produtor de eventos HT"
  ht-roteirista-palco: "Rebeca, Roteirista de palco HT"
  ht-ingressos-e-patrocinio: "Igor, Ingressos e patrocínio HT"
  ht-diretor-desafio: "Daniel, Diretor de desafio HT"
  ht-estrategista-sucesso: "Sofia, Estrategista de sucesso HT"
  ht-arquiteto-entrega: "Elisa, Arquiteta de entrega HT"
  ht-cs: "Marina, CS HT"
  ht-gestor-renovacao: "Renata, Gestora de renovação HT"
  ht-diretor-copy: "Bruno, Diretor de copy HT"
  ht-copy-paginas-e-emails: "Luana, Copy de páginas e e-mails HT"
  ht-copy-anuncios-e-mensagens: "André, Copy de anúncios e mensagens HT"
  ht-diretor-arte: "Arthur, Diretor de arte HT"
  ht-designer: "Laís, Designer HT"
  ht-web-designer: "Wagner, Web designer HT"
  ht-gestor-trafego: "Caio, Gestor de tráfego HT"
  ht-gestor-automacoes: "Alice, Gestora de automações HT"
  ht-controller: "Ricardo, Controller HT"
  ht-revisor-metodo-copy: "Helena, Revisora de método e copy HT"
  ht-revisor-visual: "Vera, Revisora visual HT"

# Padrões recomendados do método. Todo agente segue estes valores; mude qualquer um quando quiser.
padroes:
  preco_ht: "preço do HT de 5x a 10x a média do nicho, validado no teste de 20 sessões."
  garantia: "condicional e mensurável, ligada à execução do aluno, prazo igual ao do programa."
  ordem_preco_sessao: "na sessão, o preço sai na ordem entrada, parcelado, à vista."
  sinal_sessao: "sinal de R$ 500 a R$ 1.000 (até 10% do valor), pago com a call aberta."
  parcelamento: "definido por expert."
  duracao_programa: "12 meses, ajustável de 11 a 13 para cair no ciclo de renovação."
  preco_renovacao: "sem regra fixa; mostrar opções (menor, igual, reajuste) e o estrategista decide por projeto."
  eht_nao_renova: "a Experiência HT não renova; é escada para o próximo produto."
  dupla: "+50% sobre o individual."
  entregavel_ate_n: "entregável individual sempre \"até N\"; frequência fixa só em encontro de grupo."
  duracao_entregaveis_1a1: "entregável 1a1 com o alvo do manual, teto na duração real e parte 2 prevista (diagnóstico: alvo 1h20, teto 2h)."
  capacidade_entrega: "expert sozinho até 20 alunos; mentor 1:70; navegador 1:100."
  faixas: "4 níveis de resultado como padrão."
  comunidade: "WhatsApp até ~10 alunos, Telegram até ~150, Circle a partir daí."
  regras_gic: "em aberto; perguntar ao estrategista quando o primeiro GIC for montado (não decidir)."
  master_plan_conservador: "renovação 50% e margem (lucro) de 40% sobre o recebido, ou seja, custo de 60%, até haver dado próprio."
  roteiro_sessao: "versão de 6 etapas da trilha 09."
  duracao_sessao: "alvo de 1h15, teto de 1h30."
  agendamento: "2 horários oferecidos, sessão marcada em até 2 dias."
  acordo_sim_ou_nao: "usar o acordo do sim ou não, sem a metáfora \"em cima do muro\"."
  ancoragem: "duas âncoras seguidas (comparação em torno de 10x o preço, depois valor de mercado dos entregáveis em torno de 5x) e por fim a emocional; nunca ancorar no que o expert investiu."
  arrependimento_7_dias: "não usar os 7 dias de arrependimento para resolver o \"vou falar com o cônjuge\"."
  leitura_raio_x: "o gráfico começa por uma área boa, aprofunda as 3 piores e fecha com a consequência geral em 12 meses."
  perguntas_raio_x: "5 perguntas por área, de fato ou resultado com período; no máximo 1 de percepção por área."
  conversao_referencia: "10% a 20%; abaixo de 5% aciona o diagnóstico de conversão."
  minimo_sessoes: "20 sessões antes de concluir (25 no desafio, pelo pacto das 25)."
  bio_e_fixados: "bio fixa na promessa, CTA trocado pela ação do momento; link direto; 2º fixado = Evidência."
  cadencia_conteudo: "aula semanal de 1h; Reels até 90 s (raiz longo é variante); 5 Reels por semana."
  aula_semanal_no_lancamento: "a aula semanal não para durante lançamento."
  cortes_aula_semanal: "1 a 2 cortes por aula semanal."
  campanha_sessao: "exclusões em cascata (00/01/02); orçamento no conjunto na fase de teste."
  nao_pausar_anuncio: "não pausar anúncio dentro da campanha; mexer na campanha (nova, pausar, verba)."
  imagem_e_video: "campanha mistura imagem e vídeo."
  funil_novo_verba_menor: "funil novo começa com verba menor."
  abertura_pitch: "o pitch abre com emoção e indignação com a situação atual e segue racional."
  entrada_imersao: "entrada da imersão (gratuita, credencial, paga) decidida por evento; mostrar prós e contras e perguntar."
  comparecimento: "para planejar, gratuito 25%, credencial ou pago 70%; entrada no grupo, 50%."
  comissao_afiliado: "por projeto com piso, paga 45 dias após o recebimento, filiação de 30 dias."
  aprovacoes: "4 aprovações do estrategista: (1) pesquisa e oferta, (2) plano da ação, (3) peças revisadas, (4) ir ao ar."
```
