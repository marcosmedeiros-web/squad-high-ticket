# automacao-fluxos 1.0.0

Automação de marketing montada com o dono, com teste de trânsito antes de ligar e alarme quando o fluxo para.

- **Fluxos-modelo prontos** (`modelos/`): formulário para Mautic e WhatsApp, venda aprovada na Hotmart com
  boas-vindas, lembrete de aula ao vivo no grupo, comentário vira DM pela ManyChat com batida de controle.
- **Roteiro do fluxo sob medida** (`SKILL.md`, passo 8): n8n, ManyChat ou código, com a batida para o vigia.
- **Motor** (`motor/`, só biblioteca padrão do Python 3.9+): receptor em 127.0.0.1 atrás do Caddy, ciclo de um minuto,
  banco SQLite local, releitura na ponta de cada passo, vigia de falha silenciosa.
- **Instalador** (`instalar-automacao.sh`): `--so-conferir` não escreve nada; tudo nasce desligado.

Comece pelo `SKILL.md`. As lições que viraram trava estão em `references/licoes.md`.

## Arquivos
| Caminho | O que é |
|---|---|
| `motor/fluxos.py` | a linha de comando (conferir, status, transito, modo, ligar, rota, simular, esperar, ciclo, receptor) |
| `motor/executor.py` | modos, passos, travas, prova de trânsito |
| `motor/modelos.py` | os quatro tipos: conferência do desenho, ramos e passos |
| `motor/canais.py` | Mautic e OpenWA com lista fechada de rotas, e o canal de aviso |
| `motor/vigia.py` | o alarme: o que acende e quando |
| `motor/receptor.py` | a porta HTTP |
| `unidades/` | systemd (receptor, ciclo e timer) e o bloco do Caddy |
| `perfil/perfil.exemplo.env` | o perfil do dono |
