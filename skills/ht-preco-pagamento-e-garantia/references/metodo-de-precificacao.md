# Método de precificação do AR

Fontes: trilha 06 RESUMO (5.6, 7); rota3 01-02 (2.8); partes A, E, F, G, H, I; transcrições das lives 057, 058, 060 e do bootcamp
de AR mai/26 parte 2. Todo número de aula: referência, conferir. O padrão recomendado vigente é a faixa de 5x a 10x (abaixo).

## 1. Padrão recomendado e o que as fontes dizem

- **Padrão recomendado**: preço do HT = 5x a 10x a média do nicho, validado no teste de 20 sessões (o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`).
- Fontes: 3x a 20x (lives 053, 054), 4x a 20x (live 035), 5x a 20x (lives 041, 046, 055, 057 e 060, onde é chamada de "nossa
  definição de HT"), "4 a 20 vezes o produto mais barato" (desafio). O padrão do squad fixa o teto em 10x; acima disso é decisão do estrategista.
- Exemplo de conta da live 060: média de R$ 1.000 → 5x a 20x = R$ 5.000 a R$ 20.000; média de R$ 5.000 → R$ 25.000 a R$ 100.000.
  Com a faixa de 5x a 10x: R$ 5.000 a R$ 10.000 e R$ 25.000 a R$ 50.000.

## 2. Critérios (os quatro do desafio jan/26 + os complementares)

1. **Ganho do cliente**: quanto ele ganha ou economiza com o resultado (no desafio, a referência é um "chute" baseado no ganho
   do primeiro mês). Negócio e carreira sustentam mais.
2. **Mercado do nicho e comparáveis**: média dos produtos digitais e tetos do nicho (o que o avatar já paga em cirurgia,
   tratamento, faculdade, funcionário).
3. **Lastro e autoridade**: casos, prints, resultado do próprio expert. Não cobrar acima do que a prova sustenta.
4. **Teste em campo**: 20 sessões com a conversão de referência (régua do squad: 10% a 20%).
Complementares: tipo de AR (negócio > carreira > habilidade > conquista); custo da entrega e margem (especialistas comem a margem);
teste do "resultado garantido" (live 024); ancoragem na promessa.

## 3. Faixas citadas (referência, conferir)

| Contexto | Faixa citada | Fonte |
|---|---|---|
| Expert com curso de R$ 1 mil ou mais | cerca de 10x o curso | trilha 06 |
| HT de hobby | R$ 5 a 12 mil | trilha 06 |
| Piso percebido pelo professor | não vê HT abaixo de R$ 5 a 7 mil | trilha 06 |
| Começo comum | R$ 7 a 10 mil por ano; mais comum R$ 10 a 20 mil | lives 001 a 026 |
| Emagrecimento | teto de mercado de R$ 8 a 10 mil (RJ/26); um caso passou de R$ 4.997 para R$ 5.997 à vista depois de cerca de 120 alunas em um ano, e o parcelado fica cerca de R$ 2 mil acima (dez/25, conferir) | desafios RJ/26 e dez/25 |
| Programa de AR de negócio do próprio FHT | R$ 80 mil (trilha 06); outras aulas citam R$ 100 mil | trilha 06, lives |
| Direito, HT de captação de clientes | R$ 20 mil à vista, R$ 25 mil parcelado (jun/26 SP) | jun/26 SP |
| Direito | R$ 20 a 25 mil | desafios RJ e SP/26 |
| Medicina | R$ 30 mil em diante | desafio RJ/26 |
| AR de negócio | R$ 30 a 38 mil citados | desafio mai/26 |
| Treinamento de equipe de empresa | acima de R$ 80 mil | desafio RJ/26 |
| Viola para 60+ | poucos milhares/ano, ainda HT para o nicho | live 058 |
| "R$ 2 a 5 mil não é HT" | alerta, não regra contra o múltiplo | desafio RJ/26 |

## 4. Matemática de volume (live 006)

Meta de R$ 2 milhões = 2.000 vendas a R$ 1 mil, 200 a R$ 10 mil, 100 a R$ 20 mil, 25 a R$ 80 mil. Argumento da trilha 06: sem
audiência, é mais fácil vender R$ 10 mil para 1 pessoa do que R$ 1 mil para 10. Usar com o Master Plan (`ht-controller`) para
traduzir cada cenário em vendas por mês.

## 5. Template dos 3 cenários

```markdown
| Cenário | Preço à vista | Múltiplo da média | Vendas/mês para a meta | Conversão necessária (sessões/mês) | Prova que sustenta | Risco |
|---|---|---|---|---|---|---|
| a) alvo (recomendo) | R$ ... | ...x | ... | ...% (... sessões) | ... | ... |
| b) entrada no mercado | R$ ... | 5x | ... | ... | ... | deixa dinheiro na mesa; ancora baixo |
| c) alto | R$ ... | 10x | ... | ... | ... | exige prova forte; conversão menor |
```

## 6. Teste de 20 sessões (como ler)

| Conversão em 20 sessões | Leitura | Ação |
|---|---|---|
| abaixo de 5% | algo errado no avatar, na oferta ou na execução | diagnóstico de conversão (`ht-treino-comercial`) antes de mexer no preço |
| 5% a 10% | abaixo da referência | revisar sessão e objeções; preço só depois |
| 10% a 20% | dentro da referência | manter; subir conforme chegam cases |
| muito acima (a fonte cita 70%) | preço provavelmente baixo | decisão do estrategista sobre subir |
Primeira venda pode vir tarde (a fonte cita na 12ª sessão). Produto novo: as 10 primeiras podem ser vendidas mais baratas e o
preço sobe com o resultado (desafio jan/26, bootcamp mai/26); a facilidade de vender é o termômetro. Opção ao estrategista, nunca
automática.
