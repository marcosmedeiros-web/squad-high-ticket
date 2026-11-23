# Fluxo sob medida no n8n do dono

Use o n8n quando o motor deste pacote não fala com a ferramenta que o pedido precisa. O n8n é do dono: a conta, o
servidor e as credenciais de cada nó são dele. O roteiro abaixo é o que evita os defeitos medidos.

## Instalação (se o dono ainda não tem)
- Imagem com versão FIXA (nunca `latest`), banco Postgres, atrás do Caddy com HTTPS, só o caminho `/webhook/` e a
  tela de edição expostos. A versão fica anotada no compose; atualizar é decisão do dono, com teste.
- Credenciais dos nós no cofre do próprio n8n, nunca em nó de código nem em campo de texto.

## Montagem
1. Desenho no papel antes (SKILL.md, passo 8): gatilho, ramos com o "não entendi", saídas, onde se confere cada
   saída.
2. Nó IF/Switch: comparação pelo valor inteiro, sem diferenciar maiúscula, e a saída "senão" ligada a um ramo
   próprio, nunca ao destino de um ramo real.
3. Nó HTTP de saída com "nunca repetir" quando a ação não é idempotente (mensagem, e-mail): repetição automática
   pode mandar duas vezes.
4. **A batida:** último nó de cada ramo bom, um HTTP Request POST para a URL de `fluxos.py rota <fluxo>`, corpo
   `{"palavra": "<nome do ramo>", "id": "{{$execution.id}}"}`. O ramo "não entendi" manda a batida com
   `"palavra": "nao-entendi"` fora da lista de `palavras` do desenho: vira `palavra_fora_da_lista`, que alarma.
5. Um workflow de erro (Error Trigger) que manda a batida `"palavra": "erro"` (também fora da lista).

## Teste
1. Serviço falso primeiro: dados fixados no nó de entrada (pin data) e os nós de saída apontando para um endereço de
   teste; rode "Test workflow" e confira cada nó.
2. Depois, o trânsito real com o contato do dono (SKILL.md, passo 6) e `fluxos.py esperar <fluxo>`.

## Publicar sem cair (a regra que custou 76 minutos fora do ar)
- O n8n roda a versão PUBLICADA. Importar cria um rascunho e pode desativar o workflow; publicar marca a versão; em
  alguns modos de instalação é preciso reiniciar o n8n para a versão nova valer.
- "Webhook respondeu 200" logo depois de publicar NÃO é prova: a versão velha em memória responde por um tempo.
- Prova = uma execução REAL gravada depois do reinício, com status de sucesso e todos os nós esperados rodados, e a
  batida dela chegando aqui.
- Prefira editar pela API REST do n8n (reversível, sem reinício) a importar arquivo.
- Antes de qualquer mudança: exporte o workflow (cópia fora do servidor), para voltar atrás.
