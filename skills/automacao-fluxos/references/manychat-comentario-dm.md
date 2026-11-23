# Comentário vira DM com link (ManyChat) e a batida para o vigia

A ManyChat só deixa montar a estrutura do fluxo pela tela. A API dela mexe em campo, etiqueta e dispara fluxo, mas
não cria nem edita etapa. Então este modelo é montado na tela, com o dono logado, e o que o pacote acrescenta é a
batida no fim e o vigia.

## Montagem, item por item (com o dono, na tela)

1. **Gatilho de COMENTÁRIO, não de DM.** Automação > Instagram > "comentário no post ou reel". Se o post pede
   "comenta QUERO", o gatilho tem que ser de comentário naquele post (ou em todos). Gatilho só de palavra na DM
   deixa todo comentário sem resposta, em silêncio.
2. **Regra da palavra.** Prefira "é igual a" com a lista de variantes ("quero", "eu quero"); "contém" casa pedaço
   de palavra ("querosene" contém "quero"). Diferenciar maiúscula: DESLIGADO, conferido na caixa depois de
   publicar.
3. **Resposta pública** (opcional): duas ou três variantes curtas, para não parecer robô.
4. **A DM.** Uma mensagem, com o link no BOTÃO. É a resposta privada ao comentário: só sai uma até a pessoa
   responder, e o comentário precisa ter no máximo 7 dias.
5. **A batida.** Logo depois da DM, uma ação "Solicitação externa" (recurso do plano pago da ManyChat):
   - método POST, URL = a que `fluxos.py rota comentario-dm` gravou no arquivo 600 (o dono abre no terminal dele);
   - cabeçalho `Content-Type: application/json`;
   - corpo: `{"palavra": "quero", "contato": "<id do contato, pelo seletor de campos da ManyChat>"}`.
   A resposta pode ser ignorada; a DM não depende dela. Um fluxo por palavra = uma batida com a palavra dele.
6. **Publicar.** Salvo não é publicado: a bolinha de rascunho só some depois de publicar.

## Teste de trânsito

1. `fluxos.py modo comentario-dm teste`.
2. O dono comenta a palavra com uma conta de teste num post do perfil.
3. A DM chega na conta de teste, com o link funcionando, e a batida chega aqui:
   `fluxos.py esperar comentario-dm --minutos 5` devolve `ramo: palavra:quero`.
4. Contraprova: comentar uma palavra que não está no gatilho não gera DM nem batida.
5. Com o OK do dono: `fluxos.py ligar comentario-dm --ok`.
6. No dia seguinte: compare o contador da ManyChat (quantos dispararam o gatilho) com as batidas
   (`fluxos.py transito comentario-dm --horas 24`). Diferença grande = a DM não está chegando ao fim do fluxo.

## O que o vigia avisa

- `silencio`: nenhuma batida no prazo (`vigia.silencio_max_h`). O post saiu do ar? O gatilho foi despublicado? A
  sessão da ManyChat caiu? A janela de 7 dias do comentário passou?
- `palavra_muda`: uma palavra da lista sem batida no prazo (`vigia.palavra_silencio_max_h`, 0 desliga). Útil
  quando há uma CTA por post.
- `sem_regra`: chegou batida com palavra fora da lista. A regra está casando o que não devia (o "contém").

## Login e verificação humana

A sessão da ManyChat é do dono. Quando ela pede verificação humana, quem digita a senha é ele. O agente nunca
digita senha por ferramenta de navegador (a ferramenta guarda o que foi digitado).
