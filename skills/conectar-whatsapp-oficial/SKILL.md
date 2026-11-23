---
name: conectar-whatsapp-oficial
description: 'Liga o WhatsApp oficial (Cloud API da Meta) do próprio expert ao CRM ou caixa de conversas dele, com resposta dentro das 24 h e o SAIR respeitado. Use para "conectar WhatsApp oficial", "WhatsApp Business API", "Cloud API", "webhook do WhatsApp", "conectar a WABA". NÃO usar para disparo em massa nem para WhatsApp comum (não oficial).'
---

# Conectar o WhatsApp oficial ao CRM

Esta skill liga o número oficial do expert à caixa de conversas do CRM que ele usa (qualquer CRM ou inbox que aceite o
webhook da Cloud API da Meta). O que vai ligado: receber, responder dentro da janela de 24 h (que é texto livre e não é
disparo) e o SAIR, que tira a pessoa de qualquer envio. **Disparo em massa não sai desta skill:** envio para lista só com
modelo UTILITY aprovado na Meta, custo mostrado antes e OK do expert para aquele envio.

## Regras (não negociáveis)

1. **Tudo é do expert.** O app da Meta, o portfólio, a WABA, o número, o meio de pagamento e o token.
2. **Eu nunca vejo o token nem o App Secret.** Eles vão do painel da Meta direto para onde o expert guarda credencial: um
   gerenciador de credenciais, ou um arquivo `.env` fora do projeto com `chmod 600` que ele mesmo escreve no terminal
   (`umask 077; cat > ~/.config/whatsapp-oficial/credenciais.env`, uma linha `NOME=valor` por credencial, Ctrl+D). Nunca no
   chat. Valor colado no chat, em arquivo versionado ou em comando já não serve: o expert gera outro no painel e guarda de novo.
3. **Faço no máximo os passos 1 a 5.** Do 6 em diante (termos, pagamento, verificação do negócio, nome de exibição, aprovar
   qualquer envio) é do expert. Eu digo onde clicar e paro no botão.
4. **Só utility.** Mensagem para lista fria ou com oferta é marketing, pela regra da própria Meta. Eu não envio isso e explico
   o porquê.

## Os passos

1. **Conferir o que já existe:** pergunto qual CRM ou inbox vai receber as conversas e se ele já tem a tela de "conectar
   WhatsApp Cloud API" (a maioria pede: ID do número, ID da WABA, token e App Secret, e devolve a URL de callback e o token de
   verificação do webhook). Se o CRM não tiver essa tela, digo isso e paro: sem um receptor de webhook não há onde ligar.
2. **O app da Meta** (o expert, comigo guiando): em developers.facebook.com → Meus apps → Criar app → caso de uso "WhatsApp" →
   o portfólio dele.
3. **A WABA e o número:** no app, WhatsApp → Configuração da API. Para testar, serve o número de teste grátis; para valer, o número
   real dele, que ele adiciona e confirma por SMS ou ligação.
4. **Os ids, que não são segredo:** o "Identificação da conta do WhatsApp Business" (`WABA_ID`) e o "Identificação do número de
   telefone" (`WABA_PHONE_NUMBER_ID`) da mesma tela, e o "ID do app" (`META_APP_ID`) em Configurações → Básico.
5. **O token e o App Secret, direto para o lugar seguro.**
   - O token: Configurações do negócio → Usuários do sistema → gerar token com as permissões `whatsapp_business_messaging` e
     `whatsapp_business_management` → copiar → colar no gerenciador de credenciais ou no `.env` 600 como `WABA_ACCESS_TOKEN`.
   - O App Secret: Configurações → Básico → Chave secreta do app → Mostrar → copiar → `META_APP_SECRET`.
   - Daqui em diante é do expert. Com os valores guardados, eu só rodo comandos que leem a variável, sem ver o valor.

Com os cinco guardados:

- **No CRM:** o expert cola os ids, o token e o App Secret na tela de integração do CRM (ou o CRM lê do `.env` dele). O CRM
  devolve a URL de callback e o token de verificação.
- **No painel da Meta:** WhatsApp → Configuração → Webhook → URL de callback e token de verificação do CRM → Verificar e salvar →
  assinar o campo `messages`.
- **Assinar o app na WABA** (eu rodo, lendo o token da variável de ambiente, sem imprimir):
  ```bash
  set -a; . ~/.config/whatsapp-oficial/credenciais.env; set +a
  curl -s -X POST "https://graph.facebook.com/v21.0/$WABA_ID/subscribed_apps" \
    -H @<(printf 'Authorization: Bearer %s\n' "$WABA_ACCESS_TOKEN")
  ```
  Tem de voltar `{"success":true}`.
- **Conferir de fora:** a verificação do webhook (`GET` na URL de callback com `hub.mode=subscribe`, o token de verificação e um
  `hub.challenge`) tem de dar 200 com o desafio de volta, e um `POST` sem assinatura tem de dar 401 ou 403.

Esse OK confere o endereço, não uma mensagem real. Eu mostro o resultado ao expert e peço uma mensagem de teste de outro celular
para o número. Só digo que está ligado quando ela aparecer na caixa do CRM. Se não aparecer, confiro se o app está publicado
(modo Live) e se é da mesma empresa dona da WABA.

Desligar: desassinar o campo `messages` no painel (ou `DELETE /$WABA_ID/subscribed_apps`). O app na Meta continua do expert.

## Custo

Sem disparo não há gasto de envio. Responder quem escreveu, dentro das 24 h, não é cobrado pela tabela da Meta. O expert confere
a tabela dele em WhatsApp → Preços, porque ela muda por país e por categoria.
