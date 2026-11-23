# Otimização em 3 níveis, escala e diagnóstico pelo funil



## 1. Quando olhar

- Primeira leitura de estrutura: depois de **3 a 7 dias** rodando (depende da verba; a Meta precisa gastar para devolver dado).
- Depois disso: **todo dia**, com a planilha D-1. Captação curta e grande: olhar 2x/dia, mexer 1x/dia ou em dias alternados.
- Subir anúncios novos a cada ~3 dias; todo dia se o CPL estiver acima da meta.
- Lead cai de dia e sobe à noite: normal, não reagir ao horário.
- Nos primeiros dias, conferir se o lead que entra no grupo veio do anúncio e se o gerenciador marca conversão (o funil
  funciona?).

## 2. As métricas e a régua

| Etapa | Métrica | Referência do método | Se abaixo, mexer em |
|---|---|---|---|
| Leilão | CPM (custo por mil impressões) | R$ 20 a 30 em período normal; Black Friday R$ 60 a 104 (conferir) | público (muito pequeno encarece), época |
| Anúncio | CTR do link | ≥ 1% (6% muito bom) | gancho e segmentação do criativo |
| Clique → página | taxa de carregamento (connect rate) = visualizações da página de destino ÷ cliques no link | ≥ 80% (perda normal ~20%) | velocidade da página (tirar imagem, texto, mobile) |
| Página | conversão = cadastros ÷ visualizações da página | 40% a 50% em captação gratuita (50% já é muito bom; turmas citam 30% a 40%); 70% na calculadora do método | alinhamento criativo-página, promessa, tarja falando com o público |
| Resultado | CPL | ≈ 3x o CPC; meta = CPL máximo do plano | conforme a etapa que falhou |
| Saturação | frequência | ~3,5 no quente = esgotado | abrir público frio, criativo novo |

Leituras combinadas: CPM alto + CTR bom + página baixa = problema na página (mexer na página antes de criativo e público).
Dobrar a conversão da página corta o CPL pela metade. Criar coluna personalizada de taxa de carregamento.
Delay e iOS fazem Hotmart e gerenciador divergirem; custo real = valor do cartão, com imposto.

Colunas mínimas (ordem recomendada): **Resultado · Custo por resultado · Valor usado**; somar CPM, CTR do link,
cliques, visualizações da página de destino, taxa de carregamento e, para vídeo, hook rate e hold rate (fórmulas em
`ht-criativos-high-ticket`).

## 3. Otimização em 3 níveis (ordem)

**Nível 1, anúncio** (o que o método ensina):
- Dentro de cada conjunto, comparar: quem trouxe mais cadastro por menos x quem trouxe pouco e caro.
- Manter o barato; desativar o que gastou bem acima do CPL meta sem trazer (critério: gastou o dobro do CPL desejado
  sem nenhum lead; exemplos de anúncios desligados com R$ 126 sem lead e R$ 500 com 5 leads quando a média era ~R$ 100).
- Anúncio que gastou pouco: deixar rodar, não há dado.
- Aceitar um anúncio um pouco mais caro que a média se ele é o que traz volume.
- Desligar mídia relacionada (mistura métricas). Um anúncio dominando o gasto é a IA da Meta: isolar para forçar teste.
- **Regra do squad (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`)**: não pausar anúncio dentro de campanha; usar a alavanca de campanha
  (abaixo). Os critérios de corte acima são do método e ficam como contexto e leitura de desempenho, não como ação.

**Nível 2, conjunto**:
- Conjunto caro sem anúncio salvando: desativar. Conjunto barato: aumentar verba.
- Com orçamento na campanha: usar o **limite mínimo de gasto por conjunto** para forçar verba no conjunto bom (ex.: campanha
  de R$ 2.000/dia com 6 conjuntos → piso de R$ 300 no melhor).
- Truque de controle do gestor: deixar os últimos dígitos do orçamento indicando o valor anterior (ex.: 218 → 202) para saber
  no dia seguinte o que mudou. Alternativa mais limpa: anotar na planilha D-1.

**Nível 3, campanha**:
- Trazendo abaixo do CPL meta: subir verba (ex.: R$ 2.000 → R$ 2.400).
- Estratégia campeão: uma campanha de **teste de criativo** (1 conjunto = 1 criativo) ao lado da principal; o vencedor é
  copiado para todos os conjuntos da principal (seleção múltipla, copiar e colar, tirar o "cópia" do nome, publicar) e fica
  também na de teste.
- Teste de página: duplicar a campanha ou dividir o tráfego por uma ferramenta de split de URL (a aula usa uma paga, com
  porcentagens por página); migrar verba aos poucos.
- Volume de anúncios: 6 a 10 por campanha, no máximo 6 por conjunto.

## 4. Escala

- Aumento de **20%** por vez e no máximo **30%**. Acima disso: **duplicar a campanha** (escala horizontal; um
  gestor da casa chega a 10 campanhas).
- Subir verba rápido demais disparou o CPL de ~R$ 20 para R$ 45 a 53 (caso de referência).
- O pixel aprende: mais conversões baixam o CPL com o tempo; por isso a campanha de sessão não é recriada à toa.
- CPL na meta: não mexer na estrutura; escalar com calma.
- Campanhas Advantage+ abertas não competem entre si no leilão (regra do squad): não usar "canibalização" como diagnóstico;
  procurar a causa em criativo, oferta, página ou rastreio.

## 5. Formato do relatório de otimização (para o Diretor e o estrategista)

```
Projeto / campanha / janela analisada (datas) / verba gasta / leads / CPL x meta
Funil: CPM | CTR | carregamento | conversão de página | CPL  → gargalo: <etapa>
Até a venda (Central 1x1): agendamentos | comparecimentos | vendas | custo por agendamento | custo por venda
Ações propostas (cada uma): o quê · por quê (número) · risco · critério de reverter · precisa de OK? (sim/não)
Amostra: suficiente / pequena (se pequena, dizer e não decidir)
Nível de evidência: verificado (lido no gerenciador hoje) / inferido
```
