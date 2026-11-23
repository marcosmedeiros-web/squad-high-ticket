# Cobrança, inadimplência e estrutura fiscal inicial

Fontes: parte E `definir-cobranca-e-estrutura-fiscal-inicial` (dez/25 aula 143, abr/26, jan/26); resumos dos desafios dez/25
(perguntas sobre CNPJ e inadimplência), mai/25 (estratégia de pagamento), abr/26 (aplicação na plataforma e restante por outro
meio); parte H `desenhar-pagamento-p2p-dois-passos` (previsão de recebimento); live 065 (o mínimo para começar).
**Não é orientação contábil nem jurídica.** Cada item vira pergunta ao contador ou ao advogado do expert.

## 1. O mínimo para as primeiras vendas (live 065)

Precisa: oferta clara, apresentação formalizada e o processo de pagamento (Pix de entrada e cobrança do restante serve para as
primeiras 2 a 5 vendas). Não precisa: estrutura jurídica completa, equipe, plataforma própria. Regularizar com o contador logo depois.

## 2. Checklist para o contador (levar pronto)

- [ ] Abrir CNPJ? A fonte orienta CNPJ do Simples ou microempresa, não MEI, por causa do faturamento de HT.
- [ ] Conta na plataforma de pagamento: com CPF há limite de saque (a fonte cita que uma venda de R$ 10 mil pode não sacar).
- [ ] Quem fatura quando há expert e estrategista sócios: uma empresa recebe, emite a nota e repassa a parte do outro com nota
      (referência de um contador citado em aula; confirmar caso a caso).
- [ ] Nota fiscal de cada venda e de cada repasse.
- [ ] Quando abrir a empresa (ex.: virada do ano) e regime tributário.

## 3. Arquitetura de cobrança (referências das turmas)

| Parte | Onde | Prós | Contras |
|---|---|---|---|
| Aplicação/entrada | plataforma (ex.: Hotmart) | acesso automático, integração, simples para quem começa | taxa maior (valor exato não dado em aula) |
| Parcelas | gateway com boleto e cartão recorrente, ou direto na conta da empresa | taxa menor | cobrança manual ou integração |
| À vista de valor alto | Pix ou link | sem limite de cartão | não se aplica |

## 4. Política de cobrança e inadimplência

- Cobrar a parcela antes do vencimento (a fonte cita 2 dias antes).
- Termo ou contrato de compra assinado: o compromisso reduz inadimplência e dá base para negociar.
- Número de parcelas: definir com o expert no projeto (lote de decisões em `00-plano/decisoes.md`; padrão recomendado: parcelamento definido por expert, editável em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Na conversa, a referência das
  fontes: 8 parcelas em 12 meses deixam meses de margem para renegociar atraso; se preciso, abrir negociação em 12.
- Inadimplência e cancelamento vão existir: entender o motivo, renegociar, ajustar público e produto (dez/25).
- Quem cancela perde o acesso (fonte H).
- Previsão de caixa: a fonte cita receber cerca de R$ 70 a 80 mil a cada R$ 100 mil vendidos; medir a taxa real de recebimento e
  ajustar. O Master Plan usa a premissa conservadora do squad sobre o recebido (`ht-controller`).
- Envio de cobrança automática a aluno só liga com OK do estrategista (`ht-gestor-automacoes`).

## 5. Lacunas

Sem modelo de contrato, termo, política de cancelamento ou régua de cobrança nas fontes; sem taxa da plataforma para HT; sem
orientação sobre nota de aplicação reembolsável. Esses itens ficam marcados `[FALTA: validar com contador/advogado]`.
