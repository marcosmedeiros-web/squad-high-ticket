# Armadilhas — falhas silenciosas que já custaram um lote inteiro

Todas estas passaram por inspeção de quadro estático sem serem notadas. O que
elas têm em comum: **falham sem erro**.

## 1. `colorlevels` devolve quadro preto em fonte HLG 10-bit

O filtro só aceita RGB. A conversão automática a partir de HLG/BT.2020 10-bit
(padrão em DJI, GoPro, celular em HDR) **falha em silêncio e devolve quadro
totalmente preto**. Quadro preto → o segmentador não acha ninguém → a máscara
zera → o corte sai só com o fundo, sem a pessoa.

Pior: ficava escondido porque o `eq=gamma` anterior já forçava a conversão. Só
apareceu no trecho em que o gamma medido caiu em 1.01 e o passo foi pulado —
**1 trecho em 33**.

**Correção:** `format=gbrp` explícito antes do `colorlevels`. Não remover.

## 2. `tonemap` sem `zscale` escurece em vez de corrigir

Material HLG parece "errado" e a reação é aplicar `tonemap`. Sem `zscale` para
linearizar antes, o resultado é **mais escuro** que não fazer nada. Medido quadro
a quadro. Se a build não tem `zimg`, decodifique direto e aplique grade leve.

## 3. `./lote.sh | tail` engole a falha

O código de saída do pipeline é o do `tail`. Um lote inteiro pode "terminar com
sucesso" sem renderizar um arquivo. Aconteceu: rodou com o Python errado, falhou
em todos os 18, e saiu 0.

**Correção:** `set -eo pipefail` no script e **conferir que os `.mp4` existem**,
não confiar no código de saída.

## 4. Python do sistema não tem as dependências

`cv2` e `mediapipe` ficam no venv do projeto. Chamar `python3` em vez de
`.venv/bin/python` falha só na hora do render, depois de já ter gasto o corte.

## 5. Mediana temporal para extrair fundo não funciona

Se a pessoa fica parada, a mediana de cada pixel **é o rosto dela**. Ver
`fundo.py` para o método que funciona.

## 6. Caminho relativo com `cwd` trocado

Rodar ffmpeg com `cwd=` uma pasta e passar caminhos relativos à pasta original
falha. Use `.resolve()` em tudo que vai para subprocesso.

## 7. Desfoque de profundidade de campo quase nunca melhora

Três tentativas, todas com aparência embaçada em vez de cinematográfica. Fundo
desfocado simples (chapa já desfocada) ganha. Não gaste tempo aqui.

---

# Como conferir de verdade

Inspeção de quadro estático **não pega** nenhuma das falhas acima. O que pega:

## Assistir um corte de cada leva

Obrigatório antes de entregar. A skill `watch` faz isso
(`--detail efficient --no-whisper`, a transcrição já existe). Uma sessão de vídeo
achou o gancho enterrado e o véu de exposição; dez conferências de quadro não
acharam.

## Auditar a presença do sujeito

Amostre o `.mp4` a cada 0,8s e compare a região central com a chapa de fundo.
Diferença média menor que 8 significa que a máscara zerou e a pessoa sumiu.

```python
np.abs(quadro[500:1300, 300:800] - chapa[500:1300, 300:800]).mean() < 8
```

## Auditar as aberturas

Os 7 primeiros segundos de cada `.txt`, lado a lado. Abertura no meio de frase
salta na hora quando você vê as 16 juntas.

## Auditar a equalização

Mediana de luma de cada saída, três amostras por corte. Desvio acima de 10 pontos
entre cortes quer dizer que vão parecer vídeos diferentes na timeline.

## Contato visual dos quadros

Um quadro do meio de cada corte, lado a lado numa imagem só. Pega discrepância de
cor e de enquadramento em segundos.

---

# A regra geral

Todo defeito desta lista foi encontrado **depois** de eu ter dito que o trabalho
estava pronto. A ordem que evita isso:

1. gerar só as legendas (`--so-legenda`) e ler
2. renderizar
3. auditar por medição (presença, luma, aberturas)
4. **assistir um**
5. só então entregar
