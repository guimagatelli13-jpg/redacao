"""Verifica se cada elo de um texto aparece em todos os parágrafos em que deveria aparecer.

Uso: python3 ferramentas/verificar_amarracao.py TEXTO.txt ELOS.json

ELOS.json é uma lista de objetos {"elo": descrição, "termo": regex, "paragrafos": [números a partir de 1]}.
Um elo falha quando o termo não aparece em algum dos parágrafos esperados, ou seja, quando há uma ponta solta:
algo anunciado e não desenvolvido, uma causa sem resposta na proposta, um repertório sem retomada. A checagem é
lexical; ela não substitui a leitura, só garante que nenhum elo previsto ficou sem a palavra que o sustenta.
"""
import json
import re
import sys


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    paragrafos = open(sys.argv[1], encoding="utf-8").read().rstrip("\n").split("\n")
    elos = json.load(open(sys.argv[2], encoding="utf-8"))
    falhas = 0
    for e in elos:
        onde = [i for i, p in enumerate(paragrafos, 1) if re.search(e["termo"], p, re.I)]
        faltando = [n for n in e["paragrafos"] if n not in onde]
        falhas += bool(faltando)
        situacao = "OK    " if not faltando else f"FALTA em P{','.join(map(str, faltando))} "
        print(f"{situacao}{e['elo']} (aparece em P{','.join(map(str, onde)) or '-'})")
    print(f"\n{len(elos) - falhas} de {len(elos)} elos completos")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
