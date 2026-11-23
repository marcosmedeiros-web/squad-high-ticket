# Pegadinhas que o código já trata (e onde)

Cada item diz o fato, a fonte (detalhe em `fontes.md`) e o que o pacote faz com ele.

## Hotmart

1. **URL que dá erro desativa o webhook sozinha.** Central de Ajuda (H1). Ninguém é avisado. O receptor só responde
   401 para hottok errado e 500 quando o banco não gravou; todo o resto autenticado leva 200, mesmo o que vai para a
   quarentena. O vigia compara com a API e marca "webhook_desativado_provavel". (`receptor.py`, `vigia.py`)
2. **Reenvio automático até 5 vezes, e reenvio manual em Minhas Vendas.** (H1) O dedupe usa duas chaves: o id do
   evento e a chave de negócio (evento + transação). Reenvio manual com id novo cai na segunda. (`banco.py`)
3. **O hottok vem no cabeçalho `X-HOTMART-HOTTOK` na versão 2.0.0.** (D1, D2) Hottok no corpo não autentica.
   Comparação em tempo constante. Troca de hottok só pelo suporte da Hotmart.
4. **O nome do evento de abandono é `PURCHASE_OUT_OF_SHOPPING_CART`.** (D1) Guias antigos usavam
   `CHECKOUT_INITIATED` ou `PURCHASE_BILLET_PRINTED`; o primeiro não existe na lista oficial e o segundo é boleto
   impresso, outra coisa. Um mutante da suíte reintroduz o nome errado e a suíte fica vermelha.
5. **O abandono só nasce quando a pessoa preenche nome ou e-mail no checkout, e a conferência é a cada 30 min.**
   (D1) Por isso a compra pode chegar ANTES do aviso de abandono: o receptor confere a compra anterior e já grava o
   abandono como `comprou`.
6. **"Visitas na página de pagamento" do pixel da Hotmart não é abandono.** (H4) É o InitiateCheckout dela.
7. **O exemplo de compra da documentação não é JSON válido** (vírgula sobrando antes de `}`). A suíte usa o texto
   literal para provar a quarentena com 200, e uma cópia consertada para o resto. O mesmo exemplo traz
   `"status": "STARTED"` dentro de um `PURCHASE_APPROVED`: o kit decide pelo nome do evento, não pelo status.
8. **Telefone.** Na compra, `checkout_phone` vem sem DDD quando `checkout_phone_code` existe; no abandono, `phone`
   vem com DDD; fora do Brasil o DDI vem junto. O 55 só entra quando o país é BR. (D1, D2; `normaliza.py`)
9. **UTM não chega no webhook; `xcod` chega.** (H2) O snippet do site põe `xcod=<id da visita>` no link do
   checkout e a compra volta com `data.purchase.origin.xcod`.
10. **A Hotmart tem pixel e API de Conversões próprios** (Web, API ou ambos). (H3, H4) Ela não publica o event_id
    que usa. Se o pixel dela manda Purchase, o kit não manda (o perfil recusa `purchase_em_dobro`).
11. **Leitura da API (vigia):** o filtro de data do `sales/history` é pela data do PEDIDO, e sem
    `transaction_status` só voltam APPROVED e COMPLETE. O vigia lê uma janela 10 dias maior que a de comparação.
    Paginação que não fecha (total que muda, transação repetida, laço de token) é "não consegui medir", nunca
    "nenhuma venda". (medido na operação de origem; `hotmart_api.py`)
12. **Histórico de envios do painel guarda 60 dias.** (H1) O banco local é a memória longa.

## Meta

13. **Dedupe é por (event_name, event_id), no mesmo pixel, em até 48 h.** (M1) O event_id nunca é sorteado no
    servidor: Purchase = `hm.` + transação; o clique repete o ID que o navegador sorteou e já usou no fbq.
14. **Evento com mais de 7 dias derruba o lote inteiro.** (M2) Uma requisição por evento, e o velho vira
    `velho_demais` sem chamada. O evento de teste do painel da Hotmart pode chegar com data antiga; para testar a
    Meta use `capi_worker.py --evento-sintetico`.
15. **Purchase exige `currency` e `value`.** (M5) Sem os dois, o evento não entra na fila.
16. **`client_user_agent` é exigido para `action_source=website`.** (M4) Compra sem clique registrado vai com
    `CAPI_ORIGEM_SEM_NAVEGADOR` (padrão `other`).
17. **Hash:** e-mail, telefone, nome, cidade, estado, CEP e país em SHA-256 depois de normalizar; IP, navegador,
    fbp e fbc NUNCA em hash. (M4)
18. **Token fora da URL e do log.** Vai no corpo do POST, como no exemplo da Meta. (M2)
19. **Versão da Graph API:** v25.0 nos exemplos da Meta em 18/10/2026. Fica no perfil (`CAPI_VERSAO_GRAPH`).

## Servidor

20. **O Caddy grava os cabeçalhos da requisição no log de acesso.** O bloco de exemplo apaga o
    `X-Hotmart-Hottok` e mascara o IP.
21. **Serviço de usuário para quando a sessão fecha** sem `loginctl enable-linger`.
