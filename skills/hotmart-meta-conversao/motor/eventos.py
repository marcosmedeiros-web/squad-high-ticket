#!/usr/bin/env python3
"""eventos.py: a porta de leitura do banco do receptor (para o dono, para o agente e para a ficha 2).

  eventos.py status                         contagens, idade do último evento, fila da Meta, quarentena, recusas
  eventos.py abandonos [--estado aberto|comprou|expirado|todos] [--desde-min N] [--ate-min N] [--com-contato]
                                            lista os carrinhos abandonados em JSON (uma linha por lead).
                                            Sem --com-contato sai só id, produto, oferta, horário e as digitais;
                                            o contato só sai quando a recuperação vai de fato usar.
  eventos.py purgar                         aplica a retenção agora (o worker já faz isso a cada minuto)

CONTRATO COM A RECUPERAÇÃO DE CARRINHO (ficha 2): references/contrato-abandono.md. Em Python:
    import banco; banco.Banco(dados_dir).abandonos(estado='aberto', desde=<epoch>, com_contato=True)
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import banco as bco      # noqa: E402
import config            # noqa: E402


def main(argv):
    os.umask(0o077)
    try:
        perfil = config.carregar()
    except config.PerfilRecusado as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        return 78
    b = bco.Banco(perfil['dados_dir'])
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd, args = argv[1], argv[2:]
    if cmd == 'status':
        print(json.dumps(b.status(), ensure_ascii=False, indent=1))
        return 0
    if cmd == 'purgar':
        print(json.dumps(b.purgar()))
        return 0
    if cmd == 'abandonos':
        estado, desde, ate, contato = 'aberto', None, None, False
        i = 0
        agora = int(time.time())
        while i < len(args):
            a = args[i]
            if a == '--com-contato':
                contato = True
                i += 1
                continue
            if i + 1 >= len(args):
                print(f'MOTIVO=argumento_sem_valor {a}', file=sys.stderr)
                return 2
            v = args[i + 1]
            if a == '--estado' and v in ('aberto', 'comprou', 'expirado', 'todos'):
                estado = None if v == 'todos' else v
            elif a == '--desde-min' and v.isdigit():
                desde = agora - int(v) * 60
            elif a == '--ate-min' and v.isdigit():
                ate = agora - int(v) * 60
            else:
                print(f'MOTIVO=argumento_invalido {a}', file=sys.stderr)
                return 2
            i += 2
        for linha in b.abandonos(estado, desde, ate, contato):
            print(json.dumps(linha, ensure_ascii=False))
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
