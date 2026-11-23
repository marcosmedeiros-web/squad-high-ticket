# Especificação da planilha do Raio-X (modelo FHT)

Fonte: planilhas `rota3/materiais/planilhas/sessao1a1-questionario-raio-x.xlsx` (5 áreas) e `sessao1a1-roteiro.xlsx` (7 áreas,
apesar do nome), lidas célula a célula; trilha 09 RESUMO §6.1-6.2. Reproduzir a estrutura, não os textos de exemplo.

## 1. Estrutura

- Uma aba: "Diagnóstico de Negócio" (pode renomear para o tema do expert). Título no topo: "Sessão 1a1 | Questionário Raio-X
  | <nome da sessão>".
- Instruções curtas no topo: (1) nota de 0 a 10 em cada pergunta; (2) cada área sai em % de 0 a 100; (3) no fim, o panorama
  geral.
- Um bloco por área: linha de título ("ÁREA 01 · <nome>"), 5 linhas de pergunta (texto em coluna larga, nota numa coluna à
  direita, ex.: K), linha de total.
- **Total da área = soma das 5 notas × 0,02** (5 × 10 × 0,02 = 1,0 = 100%). Formatar em %.
- Pergunta invertida (se sobrou alguma): célula da pergunta em vermelho e a fórmula do total usa (10 − nota) naquela linha.
- Tabela final: coluna "Área" (nome curto), "Atual" (referência ao total da área) e "Meta" (1,0 em todas).
- **Dois radares** (ou um radar com duas séries): série Meta (azul, desejado) e série Atual (vermelho). Mesma escala, de 0 a
  100%, fixada manualmente (mínimo 0, máximo 1). Categorias = nomes curtos das áreas.
- Validação de dados nas células de nota: inteiro de 0 a 10.
- Opcional: bloco do indicador duro do nicho (entradas, fórmula, célula de alerta com formatação condicional).

## 2. Cuidados encontrados no modelo original

- O modelo vem com notas de exemplo: zerar antes de usar.
- As faixas das séries dos radares no modelo cobrem uma linha a mais que a tabela; ao replicar, ajustar a faixa exatamente às
  linhas das áreas (senão aparece um eixo vazio).
- No modelo de 5 áreas, a área 5 tem só 2 perguntas escritas: nunca entregar área com menos de 5.

## 3. Testes obrigatórios antes de entregar

1. Tudo 0 → todas as áreas 0% e o radar Atual colapsado no centro.
2. Tudo 10 → todas 100% e o radar Atual sobre o Meta.
3. Notas mistas (ex.: uma área com 2, 3, 2, 4, 3 → 28%) → conferir a conta à mão.
4. Pergunta invertida com nota 9 → contribui 1 ponto.
5. Rótulos legíveis em tela de celular (o lead muitas vezes vê pelo telefone).

## 4. Uso na call

- A planilha fica aberta só para o vendedor durante as perguntas (não compartilhar a tela).
- Compartilha só na leitura do gráfico, em tela cheia, de preferência só a aba ou o gráfico.
- Uma cópia por lead, nomeada `AAAA-MM-DD-<iniciais>-raio-x.xlsx`, em `03-sessao/privado/`; o link vai para a coluna "Link
  Raio-X" da Central 1x1 (`07-numeros/`).
