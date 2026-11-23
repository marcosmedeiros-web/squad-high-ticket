# Fontes consultadas em 18/10/2026

Documentação oficial apenas. Citação direta curta e uma por fonte; o resto é paráfrase.

## Hotmart Developers (webhook 2.0.0)

O site `developers.hotmart.com` respondeu 403 ao servidor onde este pacote foi montado. O conteúdo foi lido nas
cópias do próprio site guardadas pelo Web Archive (os arquivos `page-data.json` que o site publica), com a data de
cada cópia abaixo.

- **D1. Evento de abandono de carrinho.**
  https://developers.hotmart.com/docs/en/2.0.0/webhook/cart-abandonment-webhook/ (cópias de 08/06/2022 em inglês e
  18/11/2024 em espanhol). Nome do evento `PURCHASE_OUT_OF_SHOPPING_CART`, versão 2.0.0, hottok no cabeçalho
  `X-HOTMART-HOTTOK`, campos `data.product`, `data.buyer` (name, email, phone), `data.offer.code`,
  `data.checkout_country`, `data.buyer_ip` (na versão em espanhol). Conferência periódica: "This check is done
  every 30 minutes."
- **D2. Eventos de compra.**
  https://developers.hotmart.com/docs/en/2.0.0/webhook/purchase-webhook/ (cópia de 29/04/2024). Lista dos nove
  eventos de compra, campos de `purchase` (transaction, status, approved_date, price, full_price, offer,
  recurrence_number, order_bump) e `buyer`.
- **D3. Exemplos de código** (consulta estática `4285555676` do site, cópia de 09/05/2026): os exemplos
  `cart-abandonment-webhook-v2` e `purchase-webhook-v2`, copiados para `testes/fixtures/` como estão
  (`*.literal.txt`) e consertados só na vírgula sobrando (`*.json`). O exemplo de compra traz `purchase.origin.xcod`.
- **D4. Códigos de resposta do webhook** (pt-BR 1.0.0, cópia de 09/05/2026): 401 indica que o serviço exige chave e
  que o hottok deve ser validado.

## Central de Ajuda da Hotmart (lida pela API pública de artigos do Zendesk dela)

- **H1. Como configurar a API do meu produto usando o Webhook (Postback)?** artigo 360001491352, atualizado em
  13/03/2026. Passo a passo do cadastro, eventos disponíveis (inclui "abandono de carrinho" em Outros), teste de
  envio pela aba Minhas configurações, histórico de 60 dias, reenvio automático até cinco vezes e reenvio manual.
  Desativação: "a Hotmart desativa automaticamente a configuração".
- **H2. Parâmetros UTM** artigo 360002403031, atualizado em 10/07/2026: UTM não é repassado no webhook; o xcod é
  a alternativa.
- **H3. Pixel de Rastreamento no produto** artigo 360015341051, atualizado em 22/05/2026: envio Web, API de
  Conversões ou ambos; eventos de vendas, de página de pagamento e de página de produto.
- **H4. Opções avançadas do pixel** artigo 6565866201741, atualizado em 15/09/2026: "Vendas realizadas" dispara
  Purchase; "Visitas na Página de pagamento" dispara Initiate Checkout e não caracteriza abandono; envio via API
  sai do servidor da Hotmart com token.
- **H5. Pixel da Meta na Hotmart** artigo 115004826368, atualizado em 23/06/2026: onde fica a integração no
  painel. Não diz qual event_id a Hotmart usa.

## Meta for Developers (API de Conversões)

- **M1. Deduplicate Pixel and Server Events.**
  https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events
  `eventID` no quarto argumento do fbq, igual ao `event_id` do servidor, com o mesmo nome de evento; janela de 48 h.
- **M2. Using the API.** https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api
  Endpoint `/{PIXEL_ID}/events`, até 1.000 eventos por requisição, lote inteiro rejeitado se um evento for
  inválido, `event_time` até 7 dias, `test_event_code` só para teste, exemplos em v25.0.
- **M3. Server Event Parameters.**
  https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event
  Campos obrigatórios (`event_name`, `event_time`, `user_data`, `action_source`), valores de `action_source`,
  `event_source_url` exigido para website, regra do `event_id`.
- **M4. Customer Information Parameters.**
  https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters
  Normalização e hash de cada campo; o que nunca vai em hash; `client_user_agent` exigido para website.
- **M5. Custom Data.** https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/custom-data
  `currency` e `value` exigidos em Purchase.

## O que NÃO foi confirmado em fonte

- O event_id que o pixel e a API de Conversões nativos da Hotmart usam. Por isso a regra do `purchase_em_dobro`.
- O formato exato do evento de TESTE que o painel da Hotmart manda (data, ids). O receptor aceita qualquer evento
  2.0.0 válido; o teste de ponta a ponta com o painel é o passo 4 do procedimento.
- Os nomes dos eventos de assinatura e de área de membros: ficam na quarentena, contados, até alguém pedir.
- O tamanho máximo do `xcod` aceito pelo checkout. O snippet usa 22 caracteres.
