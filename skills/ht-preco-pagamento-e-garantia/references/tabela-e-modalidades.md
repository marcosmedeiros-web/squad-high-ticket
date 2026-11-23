# Tabela de pagamento e modalidades (P2P, Fake HT)

Fontes: trilha 06 RESUMO (5.6, 7, 8); rota3 01-02 (2.8); partes A, E, F, G, H, I; bootcamp de AR mai/26 parte 2 (transcrição);
Padrões recomendados do squad (ordem do preço, sinal, dupla; editáveis em `padroes` do perfil). Exemplos numéricos abaixo são ilustração de conta, não preço recomendado.

## 1. Template da tabela

```markdown
## Preço e condições (versão N, AAAA-MM-DD)
Base: média do nicho R$ ... (fontes: ...) · faixa de 5x a 10x R$ ... a R$ ... · cenário aprovado: ...

| Plano | À vista | Parcelado | Entrada (sinal) |
|---|---|---|---|
| Individual | R$ A | entrada + nx de R$ p (total R$ T = ~1,2 x A) | R$ E |
| Dupla (+50%) | R$ 1,5 x A | entrada + nx de R$ p2 (total ~1,2 x 1,5A) | R$ E (igual) |

n = número de parcelas, sem padrão no squad: definir com o expert no projeto (lote de decisões em `00-plano/decisoes.md`; padrão recomendado: parcelamento definido por expert, editável em `padroes` do perfil `~/.config/squad-ht/perfil.md`).

Desconto à vista escrito: "à vista você economiza R$ (T - A)".
Ordem na sessão (padrão recomendado): entrada → parcelado → à vista.
Piso de negociação: parcelas até [n máximo, definir com o expert no projeto (lote de decisões em `00-plano/decisoes.md`)]; entrada mínima R$ ...; preço não muda.
Modalidade especial aprovada: <nenhuma | P2P | Fake HT>
```

## 2. Fórmulas de conferência

- Total parcelado T ≈ 1,2 x à vista A (referência "cerca de 20% acima", trilha 06 e desafios).
- Parcela p = (T - E) / nº de parcelas. Conferir: E + n x p = T.
- Dupla: A2 = 1,5 x A; T2 ≈ 1,2 x A2.
- Entrada E: R$ 500 a R$ 1.000 e no máximo 10% de A (padrão recomendado). Se 10% de A for menor que R$ 500, levar ao estrategista.
- Erros que apareceram nos exercícios de aluno: total à vista maior que o parcelado; parcelas que não fecham; células de exemplo
  da planilha (11.997, "1.0", 27.997, 4.440) copiadas sem conferir.

Exemplo de conta (ilustração; n = 8 só para mostrar a conta, não é padrão): A = R$ 10.000 → T = R$ 12.000; E = R$ 1.000; 8x de R$ 1.375 (1.000 + 8 x 1.375 = 12.000).
Dupla: A2 = R$ 15.000; T2 = R$ 18.000; 8x de R$ 2.125 com a mesma entrada. (O bootcamp de mai/26 deu a referência "individual 10,
dupla 15, trio 18 mil", que coincide com o +50% da dupla; o trio não tem decisão vigente.)

## 3. Como o preço é falado (para o closer, não é tarefa desta skill)

Slide ou fala com uma informação por vez; mostrar a parcela; à vista com o desconto escrito; em 1a1 chamar de "entrada" (o termo
"aplicação" fica para imersão e live de venda, fonte A); bônus depois do preço; garantia depois dos bônus; objeção de dinheiro
costuma ser medo ou prioridade. Sinal pago com a call aberta.

## 4. P2P (pagamento em dois passos)

- Passo 1: aplicação (o sinal) para garantir a vaga; filtra curiosos; se a pessoa não for aceita, devolve.
- Passo 2: em 10 a 15 dias, o restante à vista ou a primeira parcela recorrente; o prazo permite ao cliente se organizar.
- Exemplos das fontes (forma, não preço): aplicação de R$ 1 a 2 mil + 10 parcelas; R$ 500 + 10x.
- Quem cancela perde o acesso. Variante "paga depois de faturar" existe só como exceção (fonte H).
- Aviso do bootcamp de mai/26: P2P não funciona para todo público; alternativa é o Fake HT.

## 5. Fake HT (anual comunicado como mensalidade)

- Lógica de faculdade ou escola: ninguém paga o total, paga a mensalidade.
- Programa de 12 meses; comunica-se a mensalidade, com desconto para quem antecipa (à vista).
- Cobrança recorrente no gateway (assinatura, Pix, boleto), não parcelar tudo no cartão.
- Exemplos das fontes (referência): emagrecimento cerca de R$ 597/mês; viola cerca de R$ 397/mês; confeitaria cerca de R$ 900/mês.
- Cuidados: precisa ser acompanhamento real de longa duração; deixar claro que o programa é anual e só o pagamento é mensal;
  prever consumo baixo e puxar engajamento; oferecer também o limite do cartão (antecipa caixa, live 065).

## 6. Regras de condição

- Ticket alto: Pix ou link de aplicação, não cartão de valor cheio.
- Diferença grande demais entre à vista e parcelado afasta quem quer parcelar.
- Ter links de entrada prontos em valores menores dentro do padrão do sinal (R$ 500 a R$ 1.000, até 10%) e perguntar quanto a pessoa consegue agora.
- Toda proposta tem prazo; prorrogar 2 a 3 dias com data (fonte G).
- Contrato ou termo de compra ajuda o compromisso e reduz inadimplência.
