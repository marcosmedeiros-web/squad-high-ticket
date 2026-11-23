# Mudanças

## 1.0.0 (18/10/2026)

Primeira versão.
- Receptor do webhook 2.0.0 da Hotmart com hottok no cabeçalho, dedupe por id e por chave de negócio, quarentena
  com 200 e banco SQLite local (600) com lista branca de campos.
- API de Conversões: Purchase (event_id `hm.` + transação) e clique de checkout (event_id do navegador), degraus
  seco, teste e real, drop-in de armar, freio `PARAR-CAPI`, retentativa e limite de 7 dias.
- Abandono de carrinho (`PURCHASE_OUT_OF_SHOPPING_CART`) guardado com contato e retenção, resolvido pela compra.
- Vigia que compara com a API de vendas e aponta webhook provavelmente desativado.
- Recusa de Purchase e checkout em dobro quando o pixel nativo da Hotmart já manda.
