# Perfil do Squad High Ticket

O perfil é **opcional**. Sem ele, o squad trabalha com exatamente estes valores. Só existe se a pessoa pedir "personaliza o
squad": aí a skill `ht-configurar` grava em `~/.config/squad-ht/perfil.md` (fora do plugin, um por pessoa) só os campos que ela
quis mudar; o que não estiver lá vale como abaixo. Pode editar à mão também; o bloco precisa continuar sendo YAML válido.
Os nomes dos agentes são fixos (tabela no `ht-protocolo`, seção 2.1) e não ficam no perfil.

```yaml
versao_perfil: 1
estrategista: ""            # seu nome; vazio = o squad chama você de "você" (é quem aprova tudo)
agencia: ""                 # nome da sua empresa (opcional)
raiz_projetos: "~/squad-ht" # cada expert fica em <raiz_projetos>/<expert>/ht/

trafego:
  ferramenta: ""      # vazio = o gestor entrega a campanha campo a campo para subir à mão no Gerenciador; ou "Meta Ads CLI", outra CLI
  prefixo_campanha: "" # bloco obrigatório no nome da campanha; vazio = sem prefixo

fontes_metodo: ""           # opcional: pasta onde você tem o acervo de aulas do método FHT; vazio = sem acervo

revisao_cruzada: ""         # opcional: quem faz a verificação final além de você; vazio = você mesmo


# Padrões recomendados do método. Todo agente segue estes valores; mude qualquer um quando quiser.
padroes:
  preco_ht: "preço do HT de 5x a 10x a média do nicho, validado no teste de 20 sessões."
  garantia: "condicional e mensurável, ligada à execução do aluno, prazo igual ao do programa."
  ordem_preco_sessao: "na sessão, o preço sai na ordem entrada, parcelado, à vista."
  sinal_sessao: "sinal de R$ 500 a R$ 1.000 (até 10% do valor), pago com a call aberta."
  parcelamento: "definido por expert."
  duracao_programa: "12 meses, ajustável de 11 a 13 para cair no ciclo de renovação."
  preco_renovacao: "sem regra fixa; o agente recomenda uma opção (menor, igual ou reajuste) pelo dado do projeto, segue com ela e lista em \"Assumi\"; vale com o OK da aprovação do plano."
  eht_nao_renova: "a Experiência HT não renova; é escada para o próximo produto."
  dupla: "+50% sobre o individual."
  entregavel_ate_n: "entregável individual sempre \"até N\"; frequência fixa só em encontro de grupo."
  duracao_entregaveis_1a1: "entregável 1a1 com o alvo do manual, teto na duração real e parte 2 prevista (diagnóstico: alvo 1h20, teto 2h)."
  capacidade_entrega: "expert sozinho até 20 alunos; mentor 1:70; navegador 1:100."
  faixas: "4 níveis de resultado como padrão."
  comunidade: "WhatsApp até ~10 alunos, Telegram até ~150, Circle a partir daí."
  regras_gic: "em aberto no método; no primeiro GIC, o agente propõe a versão mais simples, marca como suposição e lista em \"Assumi\"."
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
  entrada_imersao: "entrada da imersão (gratuita, credencial, paga) escolhida por evento: o agente recomenda uma, segue com ela e lista em \"Assumi\" com o motivo em meia frase."
  comparecimento: "para planejar, gratuito 25%, credencial ou pago 70%; entrada no grupo, 50%."
  comissao_afiliado: "por projeto com piso, paga 45 dias após o recebimento, filiação de 30 dias."
  aprovacoes: "4 aprovações do estrategista: (1) pesquisa e oferta, (2) plano da ação, (3) peças revisadas, (4) ir ao ar."
```
