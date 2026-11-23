"""Descobre os containers do Mautic na VPS e sugere as linhas do perfil. So le.

O ambiente do container traz a senha do banco: ele e lido em memoria e so a linha DOCKER_MAUTIC_ROLE e usada.
Nunca `docker exec ... env` nem `docker inspect` impresso inteiro (na origem isso expos a senha do banco).
"""
from .docker_cfg import Docker
from .perfil import ler_cofre
from .envio import ESP_INFO
from .saida import Recusa, info, motivo

FMT_LABELS = '{{index .Config.Labels "com.docker.compose.service"}}|' \
             '{{index .Config.Labels "com.docker.compose.project.working_dir"}}'
FMT_ENV = '{{range .Config.Env}}{{println .}}{{end}}'


def descobrir(perfil_cmd):
    dk = Docker(perfil_cmd)
    rc, out, _ = dk.run(['ps', '--format', '{{.Names}}\t{{.Image}}'])
    if rc != 0:
        raise Recusa('docker_inalcancavel', rc=2, dica='EMK_DOCKER="sudo -n docker" se o usuario nao esta no grupo')
    papeis, db, servicos, cdir = {}, None, {}, None
    for linha in out.decode().splitlines():
        if '\t' not in linha:
            continue
        nome, img = linha.split('\t', 1)
        rc2, lab, _ = dk.run(['inspect', '-f', FMT_LABELS, nome])
        svc, wd = (lab.decode().strip().split('|', 1) + [''])[:2] if rc2 == 0 else ('', '')
        if 'mautic/mautic' in img:
            rc3, env, _ = dk.run(['inspect', '-f', FMT_ENV, nome])
            papel = 'mautic_web'
            for e in env.decode(errors='replace').splitlines() if rc3 == 0 else []:
                if e.startswith('DOCKER_MAUTIC_ROLE='):
                    papel = e.split('=', 1)[1].strip() or papel
            del env
            papeis[papel] = nome
            servicos[papel] = svc
            cdir = cdir or wd
            info(f'{nome}\t{img}\tpapel={papel}\tservico={svc}')
        elif img.split(':')[0].split('/')[-1] in ('mysql', 'mariadb') and (not cdir or wd == cdir):
            db = (nome, svc, wd)
            info(f'{nome}\t{img}\tbanco\tservico={svc}')
    if not papeis:
        return motivo('mautic_nao_encontrado', 1)
    info('# linhas sugeridas para o perfil:')
    for chave, papel in (('EMK_CT_WEB', 'mautic_web'), ('EMK_CT_CRON', 'mautic_cron'),
                         ('EMK_CT_WORKER', 'mautic_worker')):
        info(f"{chave}={papeis.get(papel, '')}")
    if db:
        info(f'EMK_CT_DB={db[0]}')
        info(f'EMK_SERVICO_DB={db[1]}')
    info(f"EMK_SERVICOS_MAUTIC={','.join(s for s in servicos.values() if s)}")
    if cdir:
        info(f'EMK_COMPOSE_DIR={cdir}')
    falta = [p for p in ('mautic_web', 'mautic_cron', 'mautic_worker') if p not in papeis]
    if falta or not db:
        return motivo('descoberta_incompleta', 1, falta=','.join(falta + ([] if db else ['banco'])))
    return motivo('ok', 0, containers=len(papeis) + 1)


def conferir_perfil(perfil):
    perfil.exigir()
    grupos = ('https', 'api', 'docker', 'envio', 'disparo', 'compose')
    falhas = []
    for g in grupos:
        try:
            perfil.exigir(g)
            info(f'[ok] {g}')
        except Recusa as r:
            falhas.append(g)
            info(f"[falta] {g}: {r.codigo} {' '.join(f'{k}={v}' for k, v in r.kv.items())}")
    esp = perfil['EMK_ESP']
    for arq, nomes in (('EMK_CHAVE_ARQUIVO', ESP_INFO[esp]['vars']),
                       ('EMK_API_ARQUIVO', ('MAUTIC_API_USUARIO', 'MAUTIC_API_SENHA'))):
        if perfil.get(arq):
            try:
                ler_cofre(perfil[arq], nomes)
                info(f'[ok] cofre {arq}: 600, variaveis presentes (valores nao exibidos)')
            except Recusa as r:
                falhas.append(arq)
                info(f"[falta] cofre {arq}: {r.codigo} {' '.join(f'{k}={v}' for k, v in r.kv.items())}")
    info(f'servico de envio: {esp}; modo: {perfil.modo()}')
    if esp == 'resend':
        info('ATENCAO: o Resend proibe por nome "get rich quick" e decide "high risk" a criterio dele; '
             'a regua de copy BLOQUEIA promessa de ganho. Ver references/esp-politicas.md.')
    if falhas:
        return motivo('perfil_incompleto', 3, grupos=','.join(falhas))
    return motivo('perfil_ok', 0, esp=esp, modo=perfil.modo())
