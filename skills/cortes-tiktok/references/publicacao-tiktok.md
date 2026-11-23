# Publicar no TikTok

Pela **Zernio** (o plano grátis dá 2 conexões: Instagram + TikTok, ou Instagram + YouTube, à escolha do dono da conta), com a
chave da Zernio guardada num gerenciador de credenciais ou variável de ambiente, nunca no chat: sobe o vídeo, publica, confere de fora
que o post está no ar e registra. Sem a Zernio, o dono da conta publica pelo app do TikTok com o arquivo e a legenda revisada que eu
entrego. Só ferramenta grátis; conector pago de publicação não entra.

O que vale qualquer que seja o caminho: os limites de mídia, a cota e as escolhas do dono abaixo.

## Limites de mídia — conferir antes, não depois

Vídeo: MP4/WebM/MOV, até 1 GB, **3 a 600 segundos**, mínimo 360 px nos dois lados,
**23 a 60 FPS**. Foto: só JPEG ou WebP (PNG é recusado), até 20 MB.

Arquivo recusado custa uma volta inteira de conversão e reenvio, e o TikTok
recusa alguns só depois de aceitar a postagem.

## Cota

**5 posts por minuto e 13 por 24 horas**, ambos deslizantes (medido pela API de
publicação do TikTok). Recusa por cadência pede espera: espere, não repita antes.
Tentativa falha e rascunho não consomem cota.

Um post a cada 2 horas dá 12 ou 13 na janela: encostado no teto, e qualquer post
manual pelo celular passa a ser recusado. **A cada 5 horas dá ~5 por dia**, com
folga.

## Escolhas que são do dono da conta, não suas

O TikTok pede três escolhas na publicação que são decisão de quem responde pela
conta e não devem ser assumidas:

**Selo de IA (`is_aigc`).** Fundo trocado por segmentação é equivalente a chroma
key: fala, imagem e voz são reais. Não é mídia sintética. Mas quem declara é o
dono. Marcar sem precisar reduz alcance.

**Conteúdo comercial.** Opinião sobre o mercado não é anúncio. Vira selo
"Conteúdo promocional" e derruba alcance. Se tem oferta, preço ou chamada, aí
sim.

**Privacidade e interações.** Comentário liberado é sinal forte de alcance.

Ao publicar você aceita o
[Music Usage Confirmation](https://www.tiktok.com/legal/page/global/music-usage-confirmation/en)
do TikTok. Se declarar conteúdo de marca, também a
[Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en).

## Música

Vídeo de fala com legenda queimada e áudio normalizado **não leva trilha**. A
música disputa com a voz e derruba retenção. Pergunte ao dono uma vez; a resposta
padrão para talking head é não.

## Postagem em série

Guarde a fila num **arquivo em disco** com título e descrição já escritos, e um
campo `postado` por item. Três razões:

1. Texto que vai público não deve ser inventado por um agente sem revisão.
2. Se a sessão cair no meio, o estado sobrevive — retomar não repete nem pula.
3. O expert pode editar qualquer legenda que ainda não saiu.

**Não prometa agendamento por `CronCreate`.** Testado numa série real: em 19
horas ele **perdeu 5 de 5 disparos**. O job vive só na sessão do Claude Code, só
dispara com a sessão ociosa e a máquina acordada, e essa janela quase nunca
coincide com o horário marcado. Pior que não funcionar: o job aparece na lista e
passa impressão de que tem algo rodando.

O que funciona, em ordem:

1. **Agendador nativo do TikTok** — programa até 10 dias, não depende de sessão
   nenhuma. Com as legendas já escritas na fila, é copiar e colar.
2. **Rascunhos** (`mode: UPLOAD_TO_DRAFT`) — o agente faz o trabalho pesado, o
   dono da conta toca em publicar quando quiser.
3. **Manual sob demanda** — a fila em disco garante que não repete nem pula, e
   publicar um leva menos de um minuto.

## Ordem de publicação

Do gancho mais forte para o mais fraco. Os primeiros treinam o algoritmo sobre
quem é a audiência; se os primeiros são fracos, os fortes que vêm depois herdam
uma audiência mal calibrada.

Deixe o mais longo por último.
