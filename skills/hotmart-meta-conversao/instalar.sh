#!/bin/bash
# instalar.sh - instala o receptor Hotmart + API de Conversões DESLIGADO e SECO. Não liga nada.
#
# Contrato (o mesmo dos outros componentes do kit):
#   · não interativo, sem sudo, idempotente (rodar de novo com o mesmo pacote não muda nada);
#   · toda recusa imprime `MOTIVO=<slug>` na primeira linha do stderr e sai com um código próprio;
#   · instala units `--user`, faz daemon-reload e NÃO roda enable/start: imprime o comando exato;
#   · a chamada de verdade à Meta só existe com --com-capi (escreve o drop-in 60-capi-armado.conf) E com
#     CAPI_MODO=teste ou real no perfil. Sem os dois, o worker é seco.
#
# Uso:
#   bash instalar.sh --perfil <perfil.env> --destino <dir> [opções]
#     --perfil ARQ      o SEU perfil.env (modelo em perfil/perfil.exemplo.env), fora do pacote
#     --destino DIR     onde o componente mora (caminho absoluto; ex.: ~/kit/hotmart-meta)
#     --python ARQ      python3 >= 3.10 (padrão: o python3 do PATH)
#     --so-conferir     só confere (perfil, segredos, porta) e não escreve nada
#     --com-capi        escreve o drop-in que ARMA a chamada à Meta (ainda depende do CAPI_MODO)
#     --sem-capi        remove o drop-in se existir (volta ao seco)
#     --com-vigia       instala o timer do vigia (a cada 30 min)
#     --sem-autoteste   não roda a suíte depois de instalar
#     --sem-systemd     não roda daemon-reload (máquina sem systemd de usuário, ou teste)
#
# Códigos de saída: 0 ok · 2 uso errado · 3 pré-voo falhou (python, segredo) · 4 instalação falhou ·
#                   78 perfil recusado
set -uo pipefail
export PYTHONDONTWRITEBYTECODE=1

AQUI=$(cd "$(dirname "$0")" && pwd)
PERFIL="" DESTINO="" PY="" SO_CONFERIR=0 CAPI="" VIGIA=0 AUTOTESTE=1 SYSTEMD=1

recusa() { local rc=$1 slug=$2; shift 2; echo "MOTIVO=$slug" >&2; [ $# -gt 0 ] && echo "instalar: $*" >&2; exit "$rc"; }

while [ $# -gt 0 ]; do
  case "$1" in
    --perfil) PERFIL=${2:-}; shift 2 ;;
    --destino) DESTINO=${2:-}; shift 2 ;;
    --python) PY=${2:-}; shift 2 ;;
    --so-conferir) SO_CONFERIR=1; shift ;;
    --com-capi) [ -n "$CAPI" ] && recusa 2 capi_duplo "use --com-capi OU --sem-capi"; CAPI=com; shift ;;
    --sem-capi) [ -n "$CAPI" ] && recusa 2 capi_duplo "use --com-capi OU --sem-capi"; CAPI=sem; shift ;;
    --com-vigia) VIGIA=1; shift ;;
    --sem-autoteste) AUTOTESTE=0; shift ;;
    --sem-systemd) SYSTEMD=0; shift ;;
    -h|--help) sed -n '2,26p' "$0"; exit 0 ;;
    *) recusa 2 argumento_desconhecido "$1" ;;
  esac
done

[ -n "$PERFIL" ] && [ -n "$DESTINO" ] || recusa 2 faltou_argumento "--perfil e --destino são obrigatórios"
case "$DESTINO" in /*) ;; *) recusa 2 destino_relativo "use caminho absoluto em --destino" ;; esac
[ -f "$PERFIL" ] || recusa 78 perfil_ausente "$PERFIL"
PERFIL="$(cd "$(dirname "$PERFIL")" && pwd)/$(basename "$PERFIL")"
case "$PERFIL" in "$AQUI"/*|"$DESTINO"/*) recusa 2 perfil_dentro_do_pacote "o perfil mora FORA do código" ;; esac
[ -d "$AQUI/motor" ] || recusa 4 pacote_incompleto "não achei $AQUI/motor"

PY=${PY:-$(command -v python3 || true)}
[ -n "$PY" ] && [ -x "$PY" ] || recusa 3 python_ausente "python3 não encontrado"
"$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' || recusa 3 python_velho "precisa de python 3.10 ou mais novo"
"$PY" -c 'import sqlite3' 2>/dev/null || recusa 3 python_sem_sqlite "o python não tem o módulo sqlite3"

# ---- perfil (o próprio motor confere; o MOTIVO dele sobe igual) -------------------------------------------
SAIDA=$("$PY" -I -B "$AQUI/motor/config.py" --conferir "$PERFIL" 2>&1); RC=$?
if [ $RC -ne 0 ]; then echo "$SAIDA" >&2; exit 78; fi
echo "$SAIDA"
CAMPOS=$(HM_PERFIL="$PERFIL" "$PY" -I -B -c '
import sys; sys.path.insert(0, sys.argv[1]); import config
p = config.carregar()
print(p["hottok_arquivo"]); print(p["modo"]); print(p["token_arquivo"] or "-"); print(p["hotmart_cred_arquivo"] or "-")
print(p["escuta"]); print(p["porta"]); print(p["dados_dir"])' "$AQUI/motor") || recusa 78 perfil_ilegivel
{ read -r HOTTOK_ARQ; read -r MODO; read -r TOKEN_ARQ; read -r CRED_ARQ; read -r ESCUTA; read -r PORTA; read -r DADOS; } <<< "$CAMPOS"
case "$DADOS/" in "$AQUI"/*|"$DESTINO"/*) recusa 78 dados_dentro_do_pacote "HM_DADOS_DIR tem que ficar fora do código" ;; esac

# ---- segredos: só confere forma e permissão; nunca imprime valor -----------------------------------------
conf_segredo() {
  local saida; saida=$("$PY" -I -B "$AQUI/motor/segredo.py" --conferir "$@" 2>&1) || { echo "$saida" >&2; exit 3; }
  echo "$saida"
}
conf_segredo "$HOTTOK_ARQ" HOTMART_HOTTOK
if [ "$MODO" != "seco" ]; then conf_segredo "$TOKEN_ARQ" META_CAPI_TOKEN; fi
if [ "$CRED_ARQ" != "-" ]; then conf_segredo "$CRED_ARQ" HOTMART_CLIENT_ID HOTMART_CLIENT_SECRET HOTMART_BASIC; fi
if [ "$CAPI" = "com" ] && [ "$MODO" = "seco" ]; then
  echo "aviso: --com-capi com CAPI_MODO=seco arma o drop-in, mas o worker continua seco até o perfil mudar" >&2
fi

# ---- porta ---------------------------------------------------------------------------------------------
if ! "$PY" -I -B -c 'import socket,sys
s=socket.socket(socket.AF_INET6 if ":" in sys.argv[1] else socket.AF_INET)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try: s.bind((sys.argv[1], int(sys.argv[2])))
except OSError: sys.exit(1)
finally: s.close()' "$ESCUTA" "$PORTA"; then
  echo "aviso: porta $ESCUTA:$PORTA ocupada (se for o próprio receptor já instalado, está certo)" >&2
fi

if [ $SO_CONFERIR -eq 1 ]; then
  echo "conferido: perfil, segredos e porta. Nada foi escrito (--so-conferir)."
  exit 0
fi

# ---- instalação ----------------------------------------------------------------------------------------
UNIDADES="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
mkdir -p "$DESTINO" "$UNIDADES" || recusa 4 sem_escrita "não consegui criar $DESTINO ou $UNIDADES"
chmod 700 "$DESTINO"
"$PY" -I -B - "$AQUI" "$DESTINO" <<'PYEOF' || recusa 4 copia_falhou "cópia do motor"
import filecmp, shutil, sys
from pathlib import Path
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
mudou = 0
for parte in ('motor', 'site', 'testes', 'references', 'perfil', 'unidades', 'SKILL.md', 'LEIA.md', 'MUDANCAS.md',
              '_SOURCE.txt', 'instalar.sh'):
    s = src / parte
    itens = [s] if s.is_file() else sorted(p for p in s.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    for f in itens:
        alvo = dst / f.relative_to(src)
        if alvo.exists() and filecmp.cmp(f, alvo, shallow=False):
            continue
        alvo.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, alvo)
        mudou += 1
print(f'motor copiado para {dst} ({mudou} arquivo(s) novo(s) ou mudado(s))')
PYEOF

escrever_unidade() {   # <modelo> <destino>
  local tmp; tmp=$(mktemp "$UNIDADES/.hm.XXXXXX") || recusa 4 sem_escrita "$UNIDADES"
  sed -e "s#@PERFIL@#$PERFIL#g" -e "s#@PYTHON@#$PY#g" -e "s#@DESTINO@#$DESTINO#g" "$1" > "$tmp"
  if [ -f "$2" ] && cmp -s "$tmp" "$2"; then rm -f "$tmp"; else mv "$tmp" "$2"; chmod 644 "$2"; echo "unidade: $2"; fi
}
for u in hotmart-meta-receptor.service hotmart-meta-capi.service hotmart-meta-capi.timer; do
  escrever_unidade "$AQUI/unidades/$u" "$UNIDADES/$u"
done
if [ $VIGIA -eq 1 ]; then
  for u in hotmart-meta-vigia.service hotmart-meta-vigia.timer; do escrever_unidade "$AQUI/unidades/$u" "$UNIDADES/$u"; done
fi
DROPIN="$UNIDADES/hotmart-meta-capi.service.d/60-capi-armado.conf"
if [ "$CAPI" = "com" ]; then
  mkdir -p "$(dirname "$DROPIN")"
  escrever_unidade "$AQUI/unidades/60-capi-armado.conf" "$DROPIN"
elif [ "$CAPI" = "sem" ] && [ -f "$DROPIN" ]; then
  rm -f "$DROPIN"; echo "drop-in removido: a fila volta ao seco"
fi

if [ $SYSTEMD -eq 1 ]; then
  systemctl --user daemon-reload || recusa 4 daemon_reload_falhou "systemctl --user daemon-reload"
fi

if [ $AUTOTESTE -eq 1 ]; then
  if ! (cd "$DESTINO" && "$PY" -I -B -m unittest discover -s "$DESTINO/testes" -t "$DESTINO" -q 2>&1 | tail -4); then
    recusa 4 autoteste_falhou "a suíte do pacote falhou no destino"
  fi
fi

echo
echo "Instalado e PARADO. Para ligar:"
echo "  systemctl --user enable --now hotmart-meta-receptor.service hotmart-meta-capi.timer"
[ $VIGIA -eq 1 ] && echo "  systemctl --user enable --now hotmart-meta-vigia.timer"
echo "Conferir: HM_PERFIL=$PERFIL $PY -I $DESTINO/motor/eventos.py status"
