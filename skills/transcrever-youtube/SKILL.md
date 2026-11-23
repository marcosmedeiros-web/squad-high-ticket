---
name: transcrever-youtube
description: 'Transcreve vídeo do YouTube em texto corrido PT-BR: tenta a legenda do próprio vídeo e, sem ela, baixa o áudio com yt-dlp e roda Whisper local, sem chave de API. Gatilhos: "transcrever vídeo", "transcrever youtube", "pegar transcrição", "transcrever live", "converter vídeo em texto". NÃO usar quando o que importa é o que aparece na tela (watch).'
---

# Transcrever YouTube — yt-dlp + Whisper local

## O que esta skill faz

Baixa o áudio de um vídeo do YouTube com `yt-dlp`, transcreve localmente com `openai-whisper` em português-BR e entrega um `.txt` com texto corrido (sem timestamps).

Tudo offline depois da instalação. Sem API key, sem custo por minuto.

## Fluxo de execução

### 1. Peça a URL
Se o usuário não passou URL, peça. Aceite qualquer formato do YouTube (watch, youtu.be, shorts, live).

### 2. Verifique dependências
Confira `command -v yt-dlp whisper ffmpeg`. Se faltar algo, diga o que vai instalar (`yt-dlp`, `openai-whisper` e um ffmpeg estático, todos por `pip install --user`, sem Homebrew nem sudo) e, com o OK, rode uma vez por máquina:
```bash
bash <pasta-desta-skill>/setup.sh
```
Se a pessoa não quiser instalar nada, ofereça o caminho manual: abrir o vídeo no YouTube → "Mais" → "Mostrar transcrição" → copiar e colar o texto aqui.

### 3. Escolha o modelo Whisper
Default: `medium` (bom equilíbrio PT-BR). Opções:
- `tiny` / `base` — rápido, qualidade baixa
- `small` — aceitável, rápido
- `medium` — **recomendado** (padrão)
- `large` — melhor qualidade, lento

Só mude o default se o usuário pedir.

### 4. Execute a transcrição
```bash
bash <pasta-desta-skill>/transcrever.sh "<URL>" [modelo] [pasta_saida]
```

- `<URL>` obrigatória
- `modelo` opcional (default `medium`)
- `pasta_saida` opcional (default: diretório atual)

O script:
1. Baixa o áudio (m4a) com `yt-dlp` para `/tmp`
2. Roda `whisper --language Portuguese --output_format txt`
3. Move o `.txt` final pra pasta de saída com nome slugificado do vídeo
4. Limpa temporários

### 5. Entregue o resultado
- Informe caminho do arquivo salvo
- Se o usuário pediu, leia o conteúdo com `Read` e devolva no chat
- Se o vídeo for longo (>1h), avise que a transcrição pode levar vários minutos

## Quando NÃO usar esta skill
- Usuário quer legendas prontas do YouTube (use `youtube-transcript-api` em vez disso)
- Usuário quer timestamps (esta skill entrega texto corrido — se precisar de timestamps, mude `--output_format` para `srt` ou `vtt` no `transcrever.sh`)
- Vídeo não é do YouTube (yt-dlp suporta outras plataformas, mas esta skill é otimizada pra YouTube)

## Observações
- Primeira execução de cada modelo Whisper baixa ~1-2 GB (cache em `~/.cache/whisper/`)
- GPU Apple Silicon é usada automaticamente se disponível
- Áudio baixado vai pro `/tmp` e é deletado após transcrição
