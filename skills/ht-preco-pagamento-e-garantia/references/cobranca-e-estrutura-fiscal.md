# Cobrança, inadimplência e estrutura fiscal inicial

**Não é orientação contábil nem jurídica.** Cada item vira pergunta ao contador ou ao advogado do expert.

## 1. O mínimo para as primeiras vendas

Precisa: oferta clara, apresentação formalizada e o processo de pagamento (Pix de entrada e cobrança do restante serve para as
primeiras 2 a 5 vendas). Não precisa: estrutura jurídica completa, equipe, plataforma própria. Regularizar com o contador logo depois.

## 2. Checklist para o contador (levar pronto)

- [ ] Abrir CNPJ? O método orienta CNPJ do Simples ou microempresa, não MEI, por causa do faturamento de HT.
- [ ] Conta na plataforma de pagamento: com CPF há limite de saque (uma venda de R$ 10 mil pode não sacar).
- [ ] Quem fatura quando há expert e estrategista sócios: uma empresa recebe, emite a nota e repassa a parte do outro com nota
      (referência de um contador; confirmar caso a caso).
- [ ] Nota fiscal de cada venda e de cada repasse.
- [ ] Quando abrir a empresa (ex.: virada do ano) e regime tributário.

## 3. Arquitetura de cobrança (referências das turmas)

| Parte | Onde | Prós | Contras |
|---|---|---|---|
| Aplicação/entrada | plataforma (ex.: Hotmart) | acesso automático, integração, simples para quem começa | taxa maior (valor exato não dado em aula) |
| Parcelas | gateway com boleto e cartão recorrente, ou direto na conta da empresa | taxa menor | cobrança manual ou integração |
| À vista de valor alto | Pix ou link | sem limite de cartão | não se aplica |

## 4. Política de cobrança e inadimplência

- Cobrar a parcela antes do vencimento (referência: 2 dias antes).
- Termo ou contrato de compra assinado: o compromisso reduz inadimplência e dá base para negociar.
- Número de parcelas: definir com o expert no projeto (registrar em `00-plano/decisoes.md`; padrão recomendado: parcelamento definido por expert, editável em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Na conversa, a referência:
  8 parcelas em 12 meses deixam meses de margem para renegociar atraso; se preciso, abrir negociação em 12.
- Inadimplência e cancelamento vão existir: entender o motivo, renegociar, ajustar público e produto.
- Quem cancela perde o acesso.
- Previsão de caixa: a referência é receber cerca de R$ 70 a 80 mil a cada R$ 100 mil vendidos; medir a taxa real de recebimento e
  ajustar. O Master Plan usa a premissa conservadora do squad sobre o recebido (`ht-controller`).
- Envio de cobrança automática a aluno só liga com OK da pessoa (`ht-gestor-automacoes`).

## 5. Lacunas

Sem modelo de contrato, termo, política de cancelamento ou régua de cobrança no método; sem taxa da plataforma para HT; sem
orientação sobre nota de aplicação reembolsável. Esses itens ficam marcados `[FALTA: validar com contador/advogado]`.
