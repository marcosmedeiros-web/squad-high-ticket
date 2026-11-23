#!/usr/bin/env bash
# Instalador do pacote email-marketing (Mautic com HTTPS publico, gestor de disparo, troca de servico de envio).
#
#   bash instalar-email-marketing.sh --perfil <arquivo.env> --destino <pasta-do-kit> --so-conferir
#   bash instalar-email-marketing.sh --perfil <arquivo.env> --destino <pasta-do-kit> [--com-vigias]
#
# --so-conferir   confere python, perfil, cofre e acesso ao Mautic; NAO escreve nada.
# --com-vigias    alem de instalar, liga os vigias do cron e do disco (systemd --user).
# Instala SECO: o modo de disparo e o do perfil (padrao seco) e este instalador nunca o muda.
# Recusa com MOTIVO=<o que foi> na PRIMEIRA linha. Sucesso termina com MOTIVO=instalado rc=0.
set -u
AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PERFIL=""; DESTINO=""; SO_CONFERIR=0; VIGIAS=0
UNIT_DIR="${EMK_UNIT_DIR:-$HOME/.config/systemd/user}"

RELATO=""
nota() { RELATO="$RELATO$1"$'\n'; }
recusa() { local m="$1" rc="$2"; shift 2; echo "MOTIVO=$m rc=$rc"; [ $# -gt 0 ] && printf '%s\n' "$@"; [ -n "$RELATO" ] && printf '%s' "$RELATO"; exit "$rc"; }

while [ $# -gt 0 ]; do
  case "$1" in
    --perfil) PERFIL="${2:-}"; shift 2 ;;
    --destino) DESTINO="${2:-}"; shift 2 ;;
    --so-conferir) SO_CONFERIR=1; shift ;;
    --com-vigias) VIGIAS=1; shift ;;
    *) recusa opcao_desconhecida 3 "opcao: $1" ;;
  esac
done
[ -n "$PERFIL" ] && [ -n "$DESTINO" ] || recusa uso 3 "uso: --perfil <arquivo> --destino <pasta> [--so-conferir] [--com-vigias]"
[ -f "$PERFIL" ] || recusa perfil_ausente 3 "arquivo: $PERFIL"
PERFIL="$(cd "$(dirname "$PERFIL")" && pwd)/$(basename "$PERFIL")"
case "$PERFIL" in "$AQUI"/*) recusa perfil_dentro_do_pacote 3 "copie o exemplo para fora do pacote" ;; esac

# 1.0.2: o destino NAO pode ser a arvore de skills ou de agentes do Claude (nem ficar dentro dela), nem a pasta onde esta
# a skill deste pacote, nem a propria skill. O instalador cria <destino>/email-marketing e, numa atualizacao, move o que
# havia para <destino>/.email-marketing-anterior-*: dentro de ~/.claude/skills isso e uma segunda skill (com SKILL.md) e,
# se a pasta da skill do kit tiver o mesmo nome, o instalador moveria a si mesmo. O destino documentado e a pasta do kit, fora de ~/.claude/skills.
# kit 5.3.8: caminho fisico mesmo quando o destino ainda nao existe (sobe ate o ancestral que existe e resolve ali). Antes, destino novo
# voltava cru e nao casava com a arvore resolvida quando havia link no caminho (macOS: /var -> /private/var), e passava sem recusa.
fisico() { local p="$1" r=""; while [ -n "$p" ] && [ "$p" != / ] && [ ! -d "$p" ]; do r="/$(basename "$p")$r"; p="$(dirname "$p")"; done
  [ -d "$p" ] && printf '%s%s' "$(cd "$p" && pwd -P)" "$r" || printf '%s' "$1"; }
DEST_F="$(fisico "$DESTINO")"; AQUI_F="$(fisico "$AQUI")"; PAI_F="$(fisico "$(dirname "$AQUI")")"
[ "$DEST_F" != "$PAI_F" ] || recusa destino_e_a_pasta_das_skills 3 "--destino $DESTINO e a pasta que contem esta skill; use --destino <pasta do kit>, fora de ~/.claude/skills e ~/.claude/agents"
case "$DEST_F/" in "$AQUI_F"/*) recusa destino_dentro_do_pacote 3 "--destino $DESTINO esta dentro desta skill; use --destino <pasta do kit>, fora de ~/.claude/skills e ~/.claude/agents" ;; esac
for ARV in "$HOME/.claude/skills" "$HOME/.claude/agents" "${CLAUDE_CONFIG_DIR:+$CLAUDE_CONFIG_DIR/skills}" "${CLAUDE_CONFIG_DIR:+$CLAUDE_CONFIG_DIR/agents}"; do
  [ -n "$ARV" ] || continue
  ARV_F="$(fisico "$ARV")"
  case "$DEST_F/" in "$ARV_F"/*) recusa destino_dentro_de_skills 3 "--destino $DESTINO esta na arvore de skills ou agentes do Claude (backup ali vira segunda skill); use --destino <pasta do kit>, fora de ~/.claude/skills e ~/.claude/agents" ;; esac
done

PY="$(command -v python3 || true)"
[ -n "$PY" ] || recusa python_ausente 10
"$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' || recusa python_antigo 10 "precisa de 3.8 ou mais"

MOTOR="$AQUI/motor/email_mkt.py"
saida="$("$PY" -I -B "$MOTOR" --perfil "$PERFIL" perfil conferir 2>&1)"; rc=$?
[ "$rc" -eq 0 ] || recusa perfil_incompleto 3 "$saida"
nota "$(echo "$saida" | sed 's/^/  perfil: /')"

saida="$("$PY" -I -B "$MOTOR" --perfil "$PERFIL" envio mostrar 2>&1)"; rc=$?
[ "$rc" -eq 0 ] || recusa mautic_inalcancavel 2 "$saida" "confira EMK_DOCKER e os containers (email-mkt descobrir)"
nota "$(echo "$saida" | sed 's/^/  mautic: /')"

if [ "$SO_CONFERIR" -eq 1 ]; then
  printf '%s' "$RELATO"
  echo "nada foi escrito (--so-conferir)"
  echo "MOTIVO=conferido rc=0"
  exit 0
fi

mkdir -p "$DESTINO" || recusa destino_sem_permissao 3
DESTINO="$(cd "$DESTINO" && pwd)"
ALVO="$DESTINO/email-marketing"
TMP="$(mktemp -d "$DESTINO/.email-marketing-novo.XXXXXX")" || recusa destino_sem_permissao 3
for item in motor modelos references perfil SKILL.md LEIA.md MUDANCAS.md instalar-email-marketing.sh; do
  cp -R "$AQUI/$item" "$TMP/" || recusa copia_falhou 2 "$item"
done
find "$TMP" -name '*.pyc' -type f -delete 2>/dev/null; find "$TMP" -name '__pycache__' -type d -empty -delete 2>/dev/null
if [ -d "$ALVO" ]; then
  mv "$ALVO" "$DESTINO/.email-marketing-anterior-$(date -u +%Y%m%dT%H%M%SZ)" || recusa troca_falhou 2
fi
mv "$TMP" "$ALVO" || recusa troca_falhou 2

mkdir -p "$DESTINO/bin"
cat > "$DESTINO/bin/email-mkt" <<EOF
#!/usr/bin/env bash
export EMK_PERFIL="\${EMK_PERFIL:-$PERFIL}"
exec python3 -I -B "$ALVO/motor/email_mkt.py" "\$@"
EOF
chmod 755 "$DESTINO/bin/email-mkt"

mkdir -p "$UNIT_DIR"
for u in email-vigia-cron email-vigia-disco; do
  sed -e "s#__PERFIL__#$PERFIL#" -e "s#__DESTINO__#$ALVO#" "$ALVO/modelos/$u.service" > "$UNIT_DIR/$u.service"
  cp "$ALVO/modelos/$u.timer" "$UNIT_DIR/$u.timer"
done
if [ "$VIGIAS" -eq 1 ]; then
  systemctl --user daemon-reload && systemctl --user enable --now email-vigia-cron.timer email-vigia-disco.timer \
    || recusa vigias_nao_ligaram 2 "as units estao em $UNIT_DIR; confira loginctl enable-linger"
  echo "vigias ligados: email-vigia-cron.timer (10 min) e email-vigia-disco.timer (2 min)"
else
  echo "vigias instalados DESLIGADOS (ligar: rode de novo com --com-vigias)"
fi
printf '%s' "$RELATO"
modo="$(grep -E '^EMK_MODO=' "$PERFIL" | tail -1 | cut -d= -f2)"
echo "instalado em $ALVO; atalho $DESTINO/bin/email-mkt; modo de disparo do perfil: ${modo:-seco}"
echo "proximos passos: email-mkt binlog conferir ; email-mkt https caddy ... ; email-mkt dns conferir"
echo "MOTIVO=instalado rc=0"
