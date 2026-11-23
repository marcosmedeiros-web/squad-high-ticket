#!/usr/bin/env bash
# =============================================================================================================
# instalar-automacao.sh - instala a skill automacao-fluxos (fluxos-modelo + roteiro do fluxo sob medida + vigia).
#                         NÃO INTERATIVO, SEM SUDO, IDEMPOTENTE. Não liga fluxo nenhum e não manda mensagem nenhuma:
#                         todo fluxo nasce `desligado`; quem liga é `fluxos.py ligar <fluxo> --ok`, com prova de trânsito.
#
#   bash instalar-automacao.sh --perfil <perfil.env> --so-conferir   # pré-voo inteiro, NÃO escreve nada
#   bash instalar-automacao.sh --perfil <perfil.env>                 # instala a skill e o perfil (sem serviço)
#        [--com-servico]        # escreve as unidades systemd (receptor + ciclo a cada minuto), SEM ligar
#        [--ligar]              # com --com-servico: liga o receptor e o timer
#        [--skill-dir <dir>]    # padrão: ~/.claude/skills/automacao-fluxos
#        [--udir <dir>]         # padrão: ~/.config/systemd/user
#        [--sem-systemctl]      # não chama systemctl (laboratório, ou Mac: o receptor roda na VPS)
#        [--substituir-perfil]  # o perfil instalado é diferente: guarda cópia e troca
#   bash instalar-automacao.sh --parar   [--perfil <perfil.env>]   # nada sai na hora (arquivo PARAR); a entrada segue gravando
#   bash instalar-automacao.sh --retomar [--perfil <perfil.env>]
#
# CÓDIGOS: 0 ok · 10 pré-voo · 11 perfil · 12 fonte do pacote · 16 unidades/systemd · 18 destino
# Toda recusa imprime `MOTIVO=<slug>: <o que fazer>` na primeira linha do stderr.
# Portável (Linux e macOS): soma e permissão conferidas em Python, nunca `sha256sum` nem `stat -c`.
# =============================================================================================================
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
PACOTE="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PERFIL='' SKILL_DIR="$HOME/.claude/skills/automacao-fluxos" UDIR="$HOME/.config/systemd/user"
COM_SERVICO=0 LIGAR=0 SEM_SYSTEMCTL=0 SUBST=0 SO_CONFERIR=0 ACAO=instalar
CFG_DIR="$HOME/.config/automacao-fluxos"

recusar() { echo "MOTIVO=$1: $2" >&2; exit "$3"; }
passo()   { echo "== $* =="; }
carimbo() { date -u +%Y%m%dT%H%M%SZ; }
py()      { python3 -B "$@"; }

while [ $# -gt 0 ]; do
  case "$1" in
    --perfil)            PERFIL="${2:-}"; shift 2;;
    --skill-dir)         SKILL_DIR="${2:-}"; shift 2;;
    --udir)              UDIR="${2:-}"; shift 2;;
    --com-servico)       COM_SERVICO=1; shift;;
    --ligar)             LIGAR=1; shift;;
    --sem-systemctl)     SEM_SYSTEMCTL=1; shift;;
    --substituir-perfil) SUBST=1; shift;;
    --so-conferir)       SO_CONFERIR=1; shift;;
    --parar)             ACAO=parar; shift;;
    --retomar)           ACAO=retomar; shift;;
    *) recusar argumento_desconhecido "$1 (veja o cabeçalho deste arquivo)" 11;;
  esac
done
SEGURO='^[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._/:@+,~-]*$'
for D in "$SKILL_DIR" "$UDIR" "$PERFIL"; do
  [[ $D =~ $SEGURO ]] || recusar caminho_malformado "$D: só letras ASCII, dígitos e . _ / : @ + , ~ -" 18
done
[ "$LIGAR" = 1 ] && [ "$COM_SERVICO" = 0 ] && recusar ligar_sem_servico "--ligar só junto com --com-servico" 11
command -v python3 >/dev/null 2>&1 || recusar sem_python "instale python3 (3.9 ou mais novo)" 10
py -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' || recusar python_velho "precisa de python3 3.9+" 10

# valor de uma chave do perfil, já validado pela própria skill (uma fonte só da verdade)
valor() {
  py - "$PACOTE/motor" "$PERFIL" "$1" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
import base
print(base.ler_perfil(sys.argv[2])[sys.argv[3]])
PY
}
# caminho físico mesmo quando ainda não existe (no Mac /var é /private/var): resolve o pai que existe
fisico() {
  py - "$PACOTE/motor" "$1" <<'PY'
import sys
sys.path.insert(0, sys.argv[1])
import base
print(base.fisico(sys.argv[2]))
PY
}

if [ "$ACAO" != instalar ]; then
  [ -n "$PERFIL" ] || PERFIL="$CFG_DIR/perfil.env"
  [ -f "$PERFIL" ] || recusar sem_perfil "não achei $PERFIL (passe --perfil)" 11
  EST="$(valor af_dados_dir)" || recusar perfil_invalido "o perfil não passou na conferência" 11
  mkdir -p "$EST"; chmod 700 "$EST"
  if [ "$ACAO" = parar ]; then
    : > "$EST/PARAR"; echo "PARAR gravado em $EST: nenhum passo sai; a entrada continua gravando (nada se perde)"
  else
    rm -f "$EST/PARAR"; echo "PARAR removido de $EST: os passos devidos voltam a sair no próximo ciclo"
  fi
  exit 0
fi

passo "1. pré-voo (nada é escrito até o fim dele)"
for f in SKILL.md LEIA.md MUDANCAS.md instalar-automacao.sh SHA256SUMS.interno motor/fluxos.py motor/base.py \
         motor/banco.py motor/canais.py motor/modelos.py motor/executor.py motor/receptor.py motor/vigia.py \
         motor/versao.py perfil/perfil.exemplo.env unidades/automacao-fluxos-receptor.service \
         unidades/automacao-fluxos.service unidades/automacao-fluxos.timer; do
  [ -f "$PACOTE/$f" ] || recusar fonte_incompleta "falta $f no pacote: baixe o pacote de novo" 12
done
py - "$PACOTE" <<'PY' || recusar fonte_alterada "algum arquivo do pacote não bate com SHA256SUMS.interno: baixe de novo" 12
import hashlib, sys
from pathlib import Path
raiz = Path(sys.argv[1])
linhas = [l for l in (raiz / 'SHA256SUMS.interno').read_text().splitlines() if l.strip()]
ok = bool(linhas)
for l in linhas:
    h, nome = l.split(None, 1)
    nome = nome.lstrip('*')
    p = raiz / nome
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != h:
        print(f'soma diferente: {nome}', file=sys.stderr)
        ok = False
sys.exit(0 if ok else 1)
PY
[ -n "$PERFIL" ] || recusar sem_perfil "passe --perfil <perfil.env> (modelo em perfil/perfil.exemplo.env)" 11
[ -f "$PERFIL" ] || recusar sem_perfil "não achei $PERFIL" 11
SAIDA="$(py "$PACOTE/motor/fluxos.py" --perfil "$PERFIL" conferir 2>&1)" || {
  M="$(printf '%s\n' "$SAIDA" | grep -m1 '^MOTIVO=' | sed 's/^MOTIVO=//')"
  recusar "${M:-perfil_invalido}" "$(printf '%s' "$SAIDA" | grep -v '^MOTIVO=' | head -1)" 11; }
printf '%s\n' "$SAIDA"
EST="$(valor af_dados_dir)"; FLX="$(valor af_fluxos_dir)"
for D in "$EST" "$FLX"; do
  [[ $D =~ $SEGURO ]] || recusar caminho_malformado "$D (do perfil): só letras ASCII, dígitos e . _ / : @ + , ~ -" 18
done
SK_F="$(fisico "$(dirname "$SKILL_DIR")")"; PAC_F="$(fisico "$PACOTE")"
for D in "$EST" "$FLX"; do
  DF="$(fisico "$D")"
  case "$DF/" in "$SK_F"/*) recusar destino_dentro_de_skills "$D fica dentro de $(dirname "$SKILL_DIR"): dado do dono fora da árvore de skills" 18;; esac
  case "$DF/" in "$PAC_F"/*) recusar destino_dentro_do_pacote "$D fica dentro do pacote" 18;; esac
done
if [ "$COM_SERVICO" = 1 ] && [ "$SEM_SYSTEMCTL" = 0 ]; then
  systemctl --user show-environment >/dev/null 2>&1 \
    || recusar sem_systemd_usuario "systemctl --user não responde (sem sessão de usuário, ou é um Mac): na VPS rode loginctl enable-linger \$USER; no Mac use --sem-systemctl" 16
fi
if [ "$SO_CONFERIR" = 1 ]; then
  echo "SO_CONFERIR: pré-voo completo, nada foi escrito"
  exit 0
fi

passo "2. skill em $SKILL_DIR"
mkdir -p "$(dirname "$SKILL_DIR")"
SKF="$(fisico "$SKILL_DIR")"
if [ "$SKF" = "$PAC_F" ]; then
  echo "rodando de dentro da skill instalada: nada a copiar"
else
  if [ -e "$SKILL_DIR" ]; then
    if diff -rq -x testes -x __pycache__ "$PACOTE" "$SKILL_DIR" >/dev/null 2>&1; then
      echo "já instalada, igual ao pacote"
    else
      # a versão anterior vai para FORA de ~/.claude/skills: pasta com SKILL.md ao lado vira uma segunda skill
      BK="$(dirname "$(dirname "$SKILL_DIR")")/backups-automacao-fluxos/$(carimbo)"; mkdir -p "$BK"
      ANTES="$BK/$(basename "$SKILL_DIR")"; mv "$SKILL_DIR" "$ANTES"; echo "versão anterior guardada em $ANTES (fora de skills)"
    fi
  fi
  if [ ! -e "$SKILL_DIR" ]; then
    T="$(mktemp -d "$(dirname "$SKILL_DIR")/.automacao-novo.XXXXXX")"
    # leva o pacote INTEIRO (instalador, SHA256SUMS.interno, MUDANCAS.md junto), menos a suíte e o lixo de execução
    ( cd "$PACOTE" && tar --exclude=./testes --exclude='__pycache__' --exclude='*.pyc' -cf - . ) | ( cd "$T" && tar -xf - )
    chmod 755 "$T"; mv "$T" "$SKILL_DIR"; echo "instalada"
  fi
fi

passo "3. estado e perfil"
mkdir -p "$EST" "$FLX" "$CFG_DIR"; chmod 700 "$EST" "$CFG_DIR"
DEST_PERFIL="$CFG_DIR/perfil.env"
if [ "$(fisico "$PERFIL")" != "$(fisico "$DEST_PERFIL")" ]; then
  if [ -f "$DEST_PERFIL" ] && ! cmp -s "$PERFIL" "$DEST_PERFIL"; then
    [ "$SUBST" = 1 ] || recusar perfil_instalado_diferente "$DEST_PERFIL já existe e é diferente; use --substituir-perfil (guarda cópia)" 11
    cp -p "$DEST_PERFIL" "$CFG_DIR/perfil.env.antes-$(carimbo)"
  fi
  if ! cmp -s "$PERFIL" "$DEST_PERFIL" 2>/dev/null; then
    cp "$PERFIL" "$DEST_PERFIL.novo"; chmod 600 "$DEST_PERFIL.novo"; mv "$DEST_PERFIL.novo" "$DEST_PERFIL"
    echo "perfil instalado em $DEST_PERFIL (600)"
  else
    echo "perfil já instalado, igual"
  fi
fi

if [ "$COM_SERVICO" = 1 ]; then
  passo "4. unidades systemd em $UDIR"
  mkdir -p "$UDIR"
  for u in automacao-fluxos-receptor.service automacao-fluxos.service automacao-fluxos.timer; do
    sed -e "s#@PERFIL@#$DEST_PERFIL#g" -e "s#@SKILL@#$SKILL_DIR#g" "$SKILL_DIR/unidades/$u" > "$UDIR/.$u.novo"
    mv "$UDIR/.$u.novo" "$UDIR/$u"; chmod 644 "$UDIR/$u"
  done
  grep -q "motor/fluxos.py" "$UDIR/automacao-fluxos.service" || recusar unidade_torta "a unidade não aponta pro fluxos.py" 16
  echo "unidades escritas"
  if [ "$SEM_SYSTEMCTL" = 0 ]; then
    systemctl --user daemon-reload || recusar systemctl_falhou "daemon-reload falhou" 16
    if [ "$LIGAR" = 1 ]; then
      systemctl --user enable --now automacao-fluxos-receptor.service automacao-fluxos.timer \
        || recusar systemctl_falhou "não consegui ligar o receptor e o timer" 16
      echo "receptor e timer LIGADOS. Os fluxos continuam como estavam (desligado até \`modo\` e \`ligar --ok\`)"
    else
      echo "unidades escritas e DESLIGADAS. Para ligar: bash $SKILL_DIR/instalar-automacao.sh --perfil $DEST_PERFIL --com-servico --ligar"
    fi
  else
    echo "--sem-systemctl: nada ligado"
  fi
fi
echo "OK instalado. Próximo passo: o roteiro em $SKILL_DIR/SKILL.md"
