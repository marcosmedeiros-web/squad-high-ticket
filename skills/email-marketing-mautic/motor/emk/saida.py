"""Saida padrao: a ULTIMA linha de todo comando e `MOTIVO=<codigo> ... rc=<n>`.

rc 0 = ok / medido e verde
rc 1 = medido e reprovado, ou recusado por uma trava
rc 2 = nao consegui medir (nunca vira verde)
rc 3 = perfil ou uso invalido
"""
import sys


class Recusa(Exception):
    """Interrompe o comando com um MOTIVO e um rc. Nada depois dela roda."""

    def __init__(self, _codigo, rc=1, **kv):
        super().__init__(_codigo)
        self.codigo = _codigo
        self.rc = rc
        self.kv = kv


def linha_motivo(_codigo, _rc, **kv):
    extra = ''.join(f' {k}={_limpo(v)}' for k, v in kv.items())
    return f'MOTIVO={_codigo}{extra} rc={_rc}'


def motivo(_codigo, _rc=0, **kv):
    print(linha_motivo(_codigo, _rc, **kv))
    sys.stdout.flush()
    return _rc


def info(texto):
    print(texto)
    sys.stdout.flush()


def _limpo(v):
    s = str(v)
    return s.replace('\n', ' ').replace(' ', '_') if s else '-'
