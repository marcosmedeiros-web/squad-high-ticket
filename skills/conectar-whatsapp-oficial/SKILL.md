---
name: conectar-whatsapp-oficial
description: >-
  Liga o WhatsApp OFICIAL (Cloud API da Meta) do PRÓPRIO dono ao CRM da VPS dele (kit 5.6.0): o número dele entra na caixa de
  conversas do CRM, com resposta dentro das 24 h e o SAIR respeitado. Use quando pedirem "conectar WhatsApp oficial", "ligar a API
  oficial no CRM", "WhatsApp Business API", "Cloud API", "número oficial no CRM", "webhook do WhatsApp", "conectar a WABA". O app, a
  WABA, o número e o token são do DONO, nunca da Turbo. O token e o App Secret entram no cofre pela área de transferência, e eu nunca
  vejo, peço nem mostro esses valores. Disparo em massa é outro comando, o disparo-whatsapp.sh.
---

# Conectar o WhatsApp oficial ao CRM

O CRM do kit fica atrás da central de login do dono, em `https://crm.<base>`. Esta skill liga o número oficial DELE à caixa do
CRM. O que vai ligado: receber, responder dentro da janela de 24 h (que é texto livre e não é disparo) e o SAIR, que tira a pessoa
de qualquer envio. O **disparo em massa não sai desta skill**: é o `disparo-whatsapp.sh`, que só envia com modelo UTILITY conferido,
custo em R$ mostrado antes e ensaio aprovado pelo dono.

## Regras (não negociáveis)

1. **Tudo é do dono.** O app da Meta, o portfólio, a WABA, o número, o meio de pagamento e o token. Nada da Turbo.
2. **Eu nunca vejo o token nem o App Secret.** Eles vão do painel da Meta para a área de transferência do dono e dali para o cofre:
   `bash ~/.claude/head-turbo/bin/guardar-chave.sh WABA_ACCESS_TOKEN --da-area` (e `META_APP_SECRET --da-area`). Valor colado
   no chat, em arquivo ou em comando já não serve: o dono gera outro no painel e guarda de novo.
3. **Faço no máximo os passos 1 a 5.** Do 6 em diante (termos, pagamento, verificação do negócio, nome de exibição, aprovar
   qualquer envio) é do dono. Eu digo onde clicar e paro no botão.
4. **Só utility.** Mensagem para lista fria ou com oferta é marketing, pela regra da própria Meta. O kit não envia, e eu explico
   o porquê.

## Os passos

1. **Conferir o que já existe** (não mostra valor nenhum, só ✅/❌):
   `bash ~/.claude/head-turbo/bin/com-cofre.sh bash ~/.claude/head-turbo/bin/conectar-whatsapp-oficial.sh conferir`
   Sem o CRM na VPS, a primeira coisa é `bash instalar-vps.sh --so-crm` (ou o Sim na grade da central).
2. **O app da Meta** (o dono, comigo guiando): em developers.facebook.com → Meus apps → Criar app → caso de uso "WhatsApp" →
   o portfólio dele.
3. **A WABA e o número:** no app, WhatsApp → Configuração da API. Para testar, serve o número de teste grátis; para valer, o número
   real dele, que ele adiciona e confirma por SMS ou ligação.
4. **Os ids, que não são segredo:** o "Identificação da conta do WhatsApp Business" e o "Identificação do número de telefone" da
   mesma tela, e o "ID do app" em Configurações → Básico. Cada um vai para o cofre:
   `guardar-chave.sh WABA_ID`, `guardar-chave.sh WABA_PHONE_NUMBER_ID`, `guardar-chave.sh META_APP_ID`.
5. **O token e o App Secret, pela área de transferência.**
   - O token: Configurações do negócio → Usuários do sistema → gerar token com as permissões `whatsapp_business_messaging` e
     `whatsapp_business_management` → copiar → `guardar-chave.sh WABA_ACCESS_TOKEN --da-area`.
   - O App Secret: Configurações → Básico → Chave secreta do app → Mostrar → copiar → `guardar-chave.sh META_APP_SECRET --da-area`.
   - Daqui em diante é do dono. Com os valores no cofre, eu só rodo o próximo comando, sem ver nada.

Com os cinco no cofre:

`bash ~/.claude/head-turbo/bin/com-cofre.sh bash ~/.claude/head-turbo/bin/conectar-whatsapp-oficial.sh conectar`

O comando faz o seguinte:
- grava a credencial no CRM da VPS (pela entrada do ssh, nunca em comando);
- assina o app na WABA;
- registra o webhook `https://crm.<base>/api/webhook/whatsapp`, que vai direto ao CRM e nunca pela central;
- confere de fora: a verificação tem de dar 200 com o desafio de volta, e uma mensagem sem assinatura tem de dar 401.

A última linha é `WHATSAPP OK rc=0` ou um `MOTIVO=` em português. Esse OK confere o endereço, não uma mensagem real. Eu mostro o
resultado ao dono, com os avisos que vierem antes dele, e peço uma mensagem de teste de outro celular para o número. Só digo que
está ligado quando ela aparecer na caixa do CRM. Se não aparecer, confiro se o app está publicado (modo Live) e se é da mesma
empresa dona da WABA.

Desligar: o mesmo comando com `desligar`. O app na Meta continua do dono.

## Custo

Sem disparo não há gasto de envio. Responder quem escreveu, dentro das 24 h, não é cobrado pela tabela da Meta. O dono confere a
tabela dele em WhatsApp → Preços, porque ela muda por país e por categoria.
