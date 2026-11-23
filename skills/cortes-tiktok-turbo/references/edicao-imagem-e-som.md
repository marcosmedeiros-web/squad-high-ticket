# Grade, máscara, legenda e áudio

## A grade tem três etapas, e a ordem é o que importa

Gravação longa muda de luz no meio. Num material de 1h42 a mediana de luma foi de
**0,19 a 0,66** entre os trechos — postados em sequência parecem vídeos
diferentes, de pessoas diferentes, em dias diferentes.

A correção, nesta ordem exata:

1. **`eq=gamma`** leva o meio-tom até a mediana-alvo (use 0,48).
2. **`colorlevels=rimin=…`** devolve o ponto preto para baixo.
3. **contraste, saturação e nitidez**, só depois, sobre a faixa já correta.

### Nunca somar gamma com brightness

Este foi o pior defeito da primeira leva. A grade tinha `gamma=1.22` e
`brightness=0.045` fixos, e a exposição por corte entrava como **um segundo
gamma** por cima. Gamma efetivo ~1,96, com o preto levantado de verdade.

O resultado é um **véu leitoso sobre a imagem inteira**: pele acinzentada, camisa
branca virando cinza-esverdeado, contraste morto. Passa despercebido em quadro
estático e salta na hora de assistir.

Gamma sozinho já levanta a sombra junto com o meio-tom. O `colorlevels` depois
não é opcional, é o que devolve o pretume.

### Medir por trecho, não por corte

Num corte remontado que junta momentos separados por um minuto — ou por arquivo
diferente — a luz muda no meio dele. Meça e corrija **cada trecho**, não o corte
inteiro com um número só.

Fórmulas que funcionaram:

```
gamma  = log(mediana_medida / 255) / log(0.48)     limitado a [0.72, 2.15]
preto  = (p1 / 255) ** (1/gamma) * 0.85
satur  = 1.10 + 0.16 * max(0, gamma - 1)
```

Medir a mediana só no **miolo do quadro** (onde a pessoa está), não no quadro
inteiro — a borda vira fundo trocado e não interessa. O `p1` é o preto real da
fonte e vem do quadro inteiro.

O limite `[0.72, 2.15]` existe porque material muito escuro não vira material
claro: forçar além disso só amplifica ruído. Aceite que os extremos ficam um
pouco fora e diga isso ao expert.

Resultado esperado depois de equalizar: mediana em torno de 122 com desvio de 4
pontos entre os cortes.

## Troca de fundo

MediaPipe Tasks ImageSegmenter, modelo `selfie_multiclass_256x256`, em
`RunningMode.VIDEO`. `rembg` não instala em Python 3.12 (numba antigo).

Três ajustes que separam um recorte bom de um ruim:

**Endurecer o alfa.** A confiança crua deixa ~10% de fundo passar por cima da
pessoa e a camisa branca fica acinzentada.
```python
a = np.clip((a - 0.30) / 0.16, 0, 1)
```

**Unir com a máscara de categoria.** A de confiança perde a mão quando ela passa
na frente do corpo — a mão derrete no peito. A de categoria pega.
```python
a = np.maximum(a, (cat > 0).astype(np.float32))
```

**Suavizar no tempo.** Sem isso a borda treme entre quadros.
```python
alpha_ant = 0.65 * a + 0.35 * alpha_ant
```

Erosão 3×3 e desfoque de borda 2,2 fecham o acabamento. Erosão maior come o
contorno do cabelo.

Cuidado com `RunningMode.VIDEO`: exige timestamp crescente. Se você precisar
segmentar um quadro avulso antes do laço (para calcular o fundo, por exemplo),
crie um segmentador separado em `RunningMode.IMAGE`.

## Legenda

Padrão que funciona em vertical: **Montserrat ExtraBold 74, branca com contorno
preto, a 70% da altura**, quatro palavras por bloco.

70% e não mais baixo porque o terço inferior é onde o app põe usuário, descrição
e botões — legenda ali fica coberta.

Se o ffmpeg da máquina não tiver `libass` nem `libfreetype` (a build do brew não
tem), renderize a legenda em **PIL dentro do laço de quadros**. Fica melhor até:
dá contorno de verdade, quebra por largura medida e pastilha escura atrás do
texto quando o fundo é claro. Pré-renderize cada bloco uma vez em cache RGBA — se
desenhar por quadro, o render fica lento.

### Corrigir a transcrição antes de queimar

Whisper erra sistematicamente em marca, jargão e número. Número errado vira
legenda queimada com número errado. Rode sempre `--so-legenda` primeiro e **leia
o `.txt`**.

Uma regra por erro. Duas regras que casam o mesmo trecho se aplicam em sequência
e produzem lixo: `"eu turei 48" → "eu faturei 48"` mais `"turei 48" → "faturei 48"`
gera **"fafaturei"**.

Remontar trecho fora de ordem deixa minúscula depois de ponto na costura
("eles. quando eu faturei"). Recapitalize depois de juntar.

## Bipe

Nome vira **seno de 1 kHz no áudio e `———` na legenda**, casados pelo timestamp da
palavra, com uma margem de ~60 ms de cada lado.

No áudio: mutar a fala na janela e somar o seno só dentro dela.
```
[0:a]volume=0:enable='between(t,A,B)'[fala]
sine=frequency=1000[s];[s]volume=0.16,volume=0:enable='not(between(t,A,B))'[bip]
[fala][bip]amix=inputs=2:duration=first
```

Na legenda, censure **antes** de rodar as correções de transcrição — senão uma
correção desfaz o `———`.

## Áudio

`loudnorm=I=-14:TP=-1.5:LRA=11`. É o alvo de plataforma; sem isso um corte sai
mais baixo que o outro e o espectador some no que exigir aumentar volume.
