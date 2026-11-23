# Lições medidas que viraram trava

Cada item é um defeito que aconteceu numa operação real de infoproduto, o que ele custou e onde o código deste
pacote impede que volte. Nenhum deu erro na hora: todos pareciam funcionando.

## 1. Fiação certa não é trânsito
Uma coleta de e-mail foi publicada com os ramos, o cabeçalho e o campo nativo conferidos um a um na estrutura do
fluxo. Dois dias depois: zero e-mails capturados, zero erros. O contador por etapa mostrava 19 de 19 pessoas caindo
no ramo padrão; a pergunta nunca era entregue.
**No pacote:** ligar exige prova de TRÂNSITO (um evento de teste que atravessou o fluxo inteiro com cada passo
conferido na ponta) do desenho atual. `fluxos.py transito` é o contador por ramo e por passo. A reconferência do dia
seguinte é parte do roteiro, porque no dia da publicação o contador está zerado por falta de tráfego.

## 2. O ramo padrão esconde o que o roteador não entende
Num checkpoint "conseguiu instalar?", o padrão apontava para o mesmo destino do "não consegui". De 17 respostas, 14
foram roteadas errado: "ainda não comecei" virava "travei". E o casamento era por pedaço de palavra: "não consegui"
contém "consegui", e caía no ramo de sucesso.
**No pacote:** todo modelo tem ramo próprio para o que não entende (`sem_regra`, `invalido`,
`palavra_fora_da_lista`), contado e alarmado. Aceite e palavra-chave casam pelo valor inteiro normalizado: "não
aceito" não é "aceito". Há teste que planta exatamente essas frases.

## 3. Maiúscula que ninguém desligou
Uma regra mandada sem a chave `case_sensitive` voltou gravada como `true`: "Sim" não casava com "sim". O conserto só
parecia funcionar porque alguém tinha escrito as variantes à mão, e elas escondiam o defeito.
**No roteiro:** na ManyChat, `case_sensitive: false` explícito, conferido no painel depois de publicar.

## 4. Chamada a API que diz sucesso e não fez
"200" e "201" não provam nada. O gateway de WhatsApp devolve 201 até para número que não está no WhatsApp; o Mautic
pode aceitar e o contato não estar no segmento; um editor de e-mail já deixou de salvar sem mostrar erro.
**No pacote:** cada passo relê na ponta antes de virar `feito` (segmento do contato, linha da estatística do
e-mail, mensagem nova na conversa com o mesmo texto). Sem confirmação = `incerto`, e incerto nunca é reenviado.

## 5. Deploy de n8n com "webhook 200" falso
Depois de importar e publicar uma versão nova de um workflow, o webhook ainda respondia 200 por um tempo com a
versão em memória e caía no primeiro lead real: 76 minutos fora do ar. O n8n roda a versão PUBLICADA, não o
rascunho; publicar sem reiniciar não troca o que roda.
**No roteiro:** `references/n8n-sob-medida.md`. A prova é uma execução real gravada, com os nós rodados, depois do
reinício. A batida no fim do fluxo faz o vigia enxergar quando ele parou.

## 6. CTA e gatilho que não se falavam
Os vídeos pediam "comenta X" e o fluxo só tinha gatilho de palavra-chave na DM. Todo comentário foi perdido em
silêncio.
**No roteiro:** `references/manychat-comentario-dm.md`, item 1. O vigia de silêncio (e o de palavra muda, por
palavra) avisa quando uma CTA no ar não gera DM.

## 7. DM proativa pela API da ManyChat
O envio direto por API (`sendContent`) recusou mensagem para contato que tinha escrito havia duas horas, por
dessincronia da própria ManyChat. Já o envio disparado por um gatilho da ManyChat (comentário, palavra na DM)
atravessa normalmente. Antes de culpar a janela de 24 h, pergunte QUEM envia: nós por API, ou a ManyChat pelo
gatilho dela.
**No pacote:** o comentário vira DM pelo gatilho da ManyChat, nunca por API.

## 8. A própria automação confundida com humano
Um detector de "humano assumiu a conversa" lia mensagem saindo pela conta do dono como sinal de humano. A mensagem
era da automação: 38 conversas ficaram mudas, sem erro em lugar nenhum.
**No roteiro:** se o dono tem atendente automático no mesmo número, a mensagem deste pacote sai pela conta dele;
combine com quem cuida do atendente antes de ligar. E silêncio se mede: o vigia conta passo parado e evento que
não sai.

## 9. Agendamento que parou e tudo continuava verde
Um cron de container ficou 27 horas travado com web, worker, fila e healthcheck verdes. Só a contraprova por
RESULTADO ("quantos enviados hoje?") mostrou.
**No pacote:** o vigia olha resultado (evento entrando, passo saindo, lembrete que passou da hora), não processo.
Lembrete que passou da tolerância não sai atrasado: vira `perdido` e alarma. Agenda sem a próxima aula também alarma.

## 10. Marcação externa sem reconciliação
Um estado espelhado num sistema externo só era gravado na transição e falhava em silêncio para nomes com emoji.
**No pacote:** o estado do fluxo mora no banco local; o que se espelha fora (segmento, mensagem) é relido.
