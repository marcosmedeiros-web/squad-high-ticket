# Contrato da batida

Qualquer fluxo que roda fora deste pacote (ManyChat, n8n, código do dono) manda uma batida a cada evento que
atravessou. O vigia usa as batidas para avisar quando o fluxo para.

## Requisição
- `POST https://<subdomínio>/f/<fluxo>/<rota secreta>` (a URL inteira sai de `fluxos.py rota <fluxo>`, num arquivo 600).
- Corpo JSON, todos os campos opcionais:
  - `palavra`: o ramo (a palavra-chave, o nome do ramo do n8n). Comparada sem acento e sem maiúscula, pelo valor
    inteiro. Com `palavras` no desenho, o que estiver fora vira `palavra_fora_da_lista` (alarma).
  - `contato`: um identificador da pessoa; só a digital (sha256) é guardada.
  - `id`: identificador único do evento; batida repetida com o mesmo id conta uma vez.
- Também aceita `application/x-www-form-urlencoded`.

## Respostas
- `200 {"ok": true}`: gravada (inclusive repetida e fora da lista).
- `404`: rota errada, fluxo desligado ou inexistente (a tentativa errada é contada; 3 por hora alarma).
- `413`/`411`: corpo grande demais (256 KB) ou sem tamanho.
- `500`: não gravou; a origem pode tentar de novo.

## Desenho do fluxo `batida`
```json
{"nome": "<fluxo>", "tipo": "batida", "origem": "n8n", "palavras": ["ok"],
 "vigia": {"silencio_max_h": 24, "palavra_silencio_max_h": 0}}
```
Sem `palavras`, toda batida entra no ramo `batida` (ou `palavra:<x>` quando vem palavra).
