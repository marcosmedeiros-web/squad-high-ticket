"""Prevencao do incidente de disco cheio por binlog do MySQL do Mautic.

O que aconteceu na operacao de origem (08/10/2026): o Mautic 7.1.2 tem um laco no `campaigns:trigger`
(ScheduledExecutioner, linha 322, reagenda para a data errada quando um evento vence perto da meia-noite UTC fora da
janela de horario). Cada volta reescreve a mesma linha, o MySQL grava tudo no binlog, e foram 177 GB em cerca de 2 h
ate o disco chegar a 100%. Caiu junto tudo que dividia o disco. A correcao saiu no Mautic 7.1.3, mas a 7.1.3 quebrou
o login na mesma operacao, entao a casa ficou na 7.1.2 com a linha corrigida por cima.

Duas camadas, as duas aplicadas por um `docker-compose.override.yml` (o compose do instalador nao e tocado):
  1. MySQL com `--disable-log-bin`: o Mautic numa VPS so nao usa replicacao; sem binlog, laco nenhum enche o disco;
  2. na 7.1.2, o arquivo do ScheduledExecutioner com a linha corrigida montado por cima, gerado AQUI a partir do
     proprio container (o pacote nao carrega codigo do Mautic) e so se a linha defeituosa aparecer exatamente 1 vez.
O vigia do cron (processo unico com mais de 30 min) e o vigia de disco fecham o resto.
"""
import json
import os
import shutil
import subprocess
import time

from .docker_cfg import Docker, EXECUTIONER
from .saida import Recusa, info, motivo

DEFEITO = b'addForReschedule($toReschedule, $log, $latestExecutionDate);'
CORRECAO = b'addForReschedule($toReschedule, $log, $executionDate);'
MARCA = '# email-marketing: gerado por "email-mkt binlog aplicar"; pode apagar para desfazer'
OVERRIDES = ('docker-compose.override.yml', 'docker-compose.override.yaml', 'compose.override.yml',
             'compose.override.yaml')
SQL_LOGBIN = 'MYSQL_PWD="$MYSQL_ROOT_PASSWORD" mysql -uroot -N -B -e "SELECT @@log_bin"'
SQL_PURGE = 'MYSQL_PWD="$MYSQL_ROOT_PASSWORD" mysql -uroot -N -B -e "PURGE BINARY LOGS BEFORE NOW()"'
ESPERA_S = 3
SH_TAMANHO ='for f in /var/lib/mysql/binlog.[0-9]*; do [ -f "$f" ] && wc -c < "$f"; done; true'


def medir_logbin(dk, db):
    rc, out, _ = dk.exec(db, ['sh', '-c', SQL_LOGBIN], user=None)
    v = out.decode().strip()
    if rc != 0 or v not in ('0', '1'):
        return None
    return v == '1'


def medir_executioner(dk, web):
    """-> 'vulneravel' | 'corrigido' | None (nao mediu)."""
    rc, out, _ = dk.exec(web, ['cat', EXECUTIONER])
    if rc != 0 or b'<?php' not in out[:64]:
        return None, None
    n = out.count(DEFEITO)
    if n == 1:
        return 'vulneravel', out
    if n == 0:
        return 'corrigido', out
    return None, None


def medir_binlog_bytes(dk, db):
    rc, out, _ = dk.exec(db, ['sh', '-c', SH_TAMANHO], user=None)
    if rc != 0:
        return None
    return sum(int(x) for x in out.decode().split() if x.isdigit())


def conferir(perfil, dk=None):
    perfil.exigir('docker')
    dk = dk or Docker(perfil.docker_cmd())
    itens = []
    lb = medir_logbin(dk, perfil['EMK_CT_DB'])
    itens.append(('mysql_log_bin', 'nao_medido' if lb is None else ('falhou' if lb else 'ok'),
                  'binlog LIGADO: um laco do cron enche o disco' if lb else 'desligado' if lb is False else ''))
    ex, _ = medir_executioner(dk, perfil['EMK_CT_WEB'])
    itens.append(('mautic_laco_campaigns_trigger', 'nao_medido' if ex is None else (
        'falhou' if ex == 'vulneravel' else 'ok'), ex or ''))
    tam = medir_binlog_bytes(dk, perfil['EMK_CT_DB'])
    if tam is None:
        itens.append(('binlog_antigo', 'nao_medido', ''))
    else:
        itens.append(('binlog_antigo', 'aviso' if tam > 1 << 30 else 'ok', f'{tam / (1 << 30):.2f} GB em binlog.*'))
    for n, e, d in itens:
        info(f'[{e}] {n} {d}')
    if any(e == 'falhou' for _, e, _ in itens):
        return motivo('binlog_exposto', 1, fazer='email-mkt binlog aplicar')
    if any(e == 'nao_medido' for _, e, _ in itens):
        return motivo('binlog_nao_medido', 2)
    return motivo('binlog_protegido', 0)


def _args_db(dk, db):
    rc, out, _ = dk.run(['inspect', '-f', '{{json .Args}}', db])
    if rc != 0:
        raise Recusa('inspect_db_falhou', rc=2, container=db)
    try:
        args = json.loads(out.decode() or '[]') or []
    except ValueError:
        raise Recusa('inspect_db_ilegivel', rc=2)
    if args and args[0] == 'mysqld':
        args = args[1:]
    args = [a for a in args if a not in ('--disable-log-bin', '--skip-log-bin')]
    return args + ['--disable-log-bin']


def _yaml_lista(xs):
    return '[' + ', '.join(json.dumps(x) for x in xs) + ']'


def gerar_override(perfil, dk):
    cdir = perfil.caminho_de('EMK_COMPOSE_DIR')
    if not os.path.isdir(cdir):
        raise Recusa('compose_dir_inexistente', rc=3, dir=cdir)
    for nome in OVERRIDES:
        p = os.path.join(cdir, nome)
        if os.path.exists(p):
            with open(p, encoding='utf-8', errors='replace') as f:
                if MARCA not in f.read():
                    raise Recusa('override_do_dono_ja_existe', rc=1, arquivo=p,
                                 fazer='juntar_a_mao_os_blocos_de_modelos/compose-override.yml.modelo')
    ex, conteudo = medir_executioner(dk, perfil['EMK_CT_WEB'])
    if ex is None:
        raise Recusa('executioner_nao_medido', rc=2)
    linhas = [MARCA, 'services:', f"  {perfil['EMK_SERVICO_DB']}:",
              f"    command: {_yaml_lista(_args_db(dk, perfil['EMK_CT_DB']))}"]
    if ex == 'vulneravel':
        odir = os.path.join(cdir, 'overrides-email-marketing')
        os.makedirs(odir, exist_ok=True)
        corr = conteudo.replace(DEFEITO, CORRECAO)
        if corr.count(CORRECAO) < 1 or corr.count(DEFEITO) != 0:
            raise Recusa('correcao_nao_aplicavel', rc=1)
        alvo = os.path.join(odir, 'ScheduledExecutioner.php')
        with open(alvo + '.tmp', 'wb') as f:
            f.write(corr)
        os.chmod(alvo + '.tmp', 0o644)
        os.replace(alvo + '.tmp', alvo)
        for svc in [s.strip() for s in perfil['EMK_SERVICOS_MAUTIC'].split(',') if s.strip()]:
            linhas += [f'  {svc}:', '    volumes:',
                       f'      - ./overrides-email-marketing/ScheduledExecutioner.php:{EXECUTIONER}:ro']
        info(f'linha 322 corrigida gerada a partir do container: {alvo}')
    p = os.path.join(cdir, 'docker-compose.override.yml')
    with open(p + '.tmp', 'w', encoding='utf-8') as f:
        f.write('\n'.join(linhas) + '\n')
    os.replace(p + '.tmp', p)
    info(f'override gravado: {p}')
    return p, ex


def aplicar(perfil, executar=False, dk=None):
    perfil.exigir('docker', 'compose')
    dk = dk or Docker(perfil.docker_cmd())
    p, ex = gerar_override(perfil, dk)
    cdir = perfil.caminho_de('EMK_COMPOSE_DIR')
    cmd = perfil['EMK_COMPOSE_CMD'].split() + ['up', '-d']
    if not executar:
        info(f'para valer: cd {cdir} && {" ".join(cmd)}   (recria os containers; o Mautic fica fora uns segundos)')
        return motivo('override_gerado_nao_aplicado', 0, arquivo=p, fazer='email-mkt binlog aplicar --executar')
    if medir_logbin(dk, perfil['EMK_CT_DB']):
        rc, _, _ = dk.exec(perfil['EMK_CT_DB'], ['sh', '-c', SQL_PURGE], user=None)
        info(f'PURGE BINARY LOGS antes de desligar: rc {rc}')
    if not shutil.which(cmd[0]):
        raise Recusa('compose_indisponivel', rc=2, comando=cmd[0])
    r = subprocess.run(cmd, cwd=cdir, capture_output=True, timeout=600)
    if r.returncode != 0:
        raise Recusa('compose_up_falhou', rc=1, rc_compose=r.returncode)
    for _ in range(40):
        if medir_logbin(dk, perfil['EMK_CT_DB']) is not None:
            break
        time.sleep(ESPERA_S)
    return conferir(perfil, dk)
