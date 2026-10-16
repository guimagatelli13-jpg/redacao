"""Testa fórmulas candidatas para a nota da redação contra todas as avaliações em dados/avaliacoes.csv.

Uso: python3 ferramentas/testar_modelos.py [caminho_csv]

Para cada modelo, mostra a nota prevista, o erro em cada avaliação e quantas avaliações ele reproduz
exatamente (com duas casas, como o sistema exibe). Depois faz uma busca em grade de pesos (passo 0,05)
para mostrar quantas combinações de pesos continuam compatíveis com os dados — o tamanho desse conjunto
é a medida direta do problema de identificabilidade.
"""
import csv
import itertools
import math
import sys
from decimal import Decimal, ROUND_FLOOR, ROUND_HALF_UP
from pathlib import Path

CSV_PADRAO = Path(__file__).resolve().parent.parent / "dados" / "avaliacoes.csv"


def trunc1(x):
    # O épsilon neutraliza o erro de representação binária (9,7 + 3 + 7,1 = 19,7999… em ponto flutuante), de modo que
    # o truncamento siga a aritmética exata. Um sistema real que trunque em ponto flutuante pode dar 0,1 a menos.
    return float(Decimal(repr(x + 1e-9)).quantize(Decimal("0.1"), rounding=ROUND_FLOOR))


def round1(x):
    return float(Decimal(repr(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def round2(x):
    return float(Decimal(repr(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


ARREDONDAMENTOS = {"trunc 0,1": trunc1, "arred 0,1": round1, "arred 0,01": round2}


def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    for r in linhas:
        for k in ("gramatica", "abrangencia", "tangenciamento", "apont_erro", "nota_online", "nota_final", "palavras"):
            r[k] = float(r[k])
    return linhas


# Cada modelo recebe G, A, T, E (apontamentos) e W (palavras) e devolve a nota bruta, antes do arredondamento.
MODELOS = {
    "media(G,A,T)": lambda G, A, T, E, W: (G + A + T) / 3,
    "media(G,A,T,E)": lambda G, A, T, E, W: (G + A + T + E) / 4,
    "(G+A+T-0,05E)/3": lambda G, A, T, E, W: (G + A + T - 0.05 * E) / 3,
    "0,4G+0,4A+0,2T": lambda G, A, T, E, W: 0.4 * G + 0.4 * A + 0.2 * T,
    "0,35G+0,35A+0,3T": lambda G, A, T, E, W: 0.35 * G + 0.35 * A + 0.3 * T,
    "(G+A+2T)/4": lambda G, A, T, E, W: (G + A + 2 * T) / 4,
    "(2G+A+T)/4": lambda G, A, T, E, W: (2 * G + A + T) / 4,
    "(G+2A+T)/4": lambda G, A, T, E, W: (G + 2 * A + T) / 4,
    "media(G,A,10-T)": lambda G, A, T, E, W: (G + A + (10 - T)) / 3,
    "media geometrica": lambda G, A, T, E, W: (G * A * T) ** (1 / 3),
    "media harmonica": lambda G, A, T, E, W: 3 / (1 / G + 1 / A + 1 / T),
    "mediana": lambda G, A, T, E, W: sorted([G, A, T])[1],
    "minimo": lambda G, A, T, E, W: min(G, A, T),
}

# Regras candidatas para a "Nota Final": cada uma diz quando a Nota Final vira 0; fora disso, Nota Final = nota online.
# "Não explica" quer dizer que a regra, sozinha, não reproduz os dados; ela ainda pode coexistir com outra causa.
# Causas externas às notas (status do processo, integridade, etapa pendente) são compatíveis com qualquer
# observação e por isso não aparecem aqui: não podem ser refutadas só com as notas.
REGRAS_NOTA_FINAL = {
    "sempre igual à nota online": lambda r: False,
    "0 se algum critério = 0": lambda r: min(r["gramatica"], r["abrangencia"], r["tangenciamento"]) == 0,
    "0 se Tangenciamento = 0 (fuga total)": lambda r: r["tangenciamento"] == 0,
    "0 se nota online < 5": lambda r: r["nota_online"] < 5,
    "0 se nota online < 6": lambda r: r["nota_online"] < 6,
    "0 se nota online < 7": lambda r: r["nota_online"] < 7,
    "0 se Abrangência < 4": lambda r: r["abrangencia"] < 4,
    "0 se Abrangência < 5": lambda r: r["abrangencia"] < 5,
    "0 se algum critério < 5": lambda r: min(r["gramatica"], r["abrangencia"], r["tangenciamento"]) < 5,
    "0 se Tangenciamento < 7,5": lambda r: r["tangenciamento"] < 7.5,
    "0 se apontamentos >= 4": lambda r: r["apont_erro"] >= 4,
}

# Hipóteses sobre a relação entre Gramática e Apontamentos.
MODELOS_G = {
    "G = 10 - 0,025E": lambda E, W: 10 - 0.025 * E,
    "G = 10(1 - E/palavras)": lambda E, W: 10 * (1 - E / W),
    "G = 10 - E/(palavras/100)": lambda E, W: 10 - E / (W / 100),
    "G = 10 - 0,1E": lambda E, W: 10 - 0.1 * E,
}


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else CSV_PADRAO
    dados = carregar(caminho)
    n = len(dados)
    print(f"{n} avaliação(ões) carregada(s) de {caminho}\n")

    print("== Modelos da 'Nota Final da Redação Online' ==")
    for nome, f in MODELOS.items():
        for nome_arr, arr in ARREDONDAMENTOS.items():
            acertos, erros = 0, []
            for r in dados:
                bruto = f(r["gramatica"], r["abrangencia"], r["tangenciamento"], r["apont_erro"], r["palavras"])
                prev = arr(bruto)
                erros.append(prev - r["nota_online"])
                acertos += math.isclose(prev, r["nota_online"], abs_tol=1e-9)
            bruto0 = f(dados[0]["gramatica"], dados[0]["abrangencia"], dados[0]["tangenciamento"],
                       dados[0]["apont_erro"], dados[0]["palavras"])
            marca = "OK " if acertos == n else "   "
            print(f"{marca}{nome:<22} {nome_arr:<11} bruto[0]={bruto0:7.4f}  acertos={acertos}/{n}  "
                  f"erro máx={max(abs(e) for e in erros):.2f}")
    print()

    print("== Modelos da nota de Gramática a partir dos apontamentos ==")
    for nome, f in MODELOS_G.items():
        for nome_arr, arr in ARREDONDAMENTOS.items():
            acertos = sum(math.isclose(arr(f(r["apont_erro"], r["palavras"])), r["gramatica"], abs_tol=1e-9)
                          for r in dados)
            bruto0 = f(dados[0]["apont_erro"], dados[0]["palavras"])
            marca = "OK " if acertos == n else "   "
            print(f"{marca}{nome:<26} {nome_arr:<11} bruto[0]={bruto0:7.4f}  acertos={acertos}/{n}")
    print()

    print("== Precisão oculta: as notas exibidas podem ser arredondadas ou truncadas de valores mais precisos ==")
    for r in dados:
        soma = r["gramatica"] + r["abrangencia"] + r["tangenciamento"]
        for exib, (lo, hi) in {"exibidas arredondadas": (soma - 0.15, soma + 0.15),
                               "exibidas truncadas": (soma, soma + 0.3)}.items():
            for nome_arr, arr in (("trunc 0,1", trunc1), ("arred 0,1", round1)):
                somas_ok = [x / 1000 for x in range(round(lo * 1000), round(hi * 1000))
                            if math.isclose(arr(x / 3000), r["nota_online"], abs_tol=1e-9)]
                faixa = f"soma interna em [{min(somas_ok):.2f}; {max(somas_ok):.2f}]" if somas_ok else "incompatível"
                print(f"  aval. {r['id']}: {exib:<22} + média com {nome_arr}: {faixa}")
    print()

    print("== Regras candidatas para a 'Nota Final' ==")
    for nome, zera in REGRAS_NOTA_FINAL.items():
        ok = all(math.isclose(0.0 if zera(r) else r["nota_online"], r["nota_final"], abs_tol=1e-9) for r in dados)
        print(f"  {'compatível ' if ok else 'não explica'}  {nome}")
    print()

    print("== Busca em grade: pesos (wG, wA, wT), passo 0,05, soma 1 ==")
    passos = [i / 20 for i in range(21)]
    for nome_arr, arr in ARREDONDAMENTOS.items():
        compativeis = []
        for wG, wA in itertools.product(passos, passos):
            wT = round(1 - wG - wA, 10)
            if wT < 0:
                continue
            if all(math.isclose(arr(wG * r["gramatica"] + wA * r["abrangencia"] + wT * r["tangenciamento"]),
                                r["nota_online"], abs_tol=1e-9) for r in dados):
                compativeis.append((wG, wA, wT))
        total = sum(1 for wG, wA in itertools.product(passos, passos) if wG + wA <= 1 + 1e-9)
        print(f"{nome_arr:<11}: {len(compativeis)} de {total} vetores de pesos compatíveis")
        for c in compativeis:
            print(f"    wG={c[0]:.2f} wA={c[1]:.2f} wT={c[2]:.2f}")
    print()

    print("== Pesos inteiros em % que reproduzem a nota exatamente, sem arredondamento ==")
    for g in range(101):
        for a in range(101 - g):
            t = 100 - g - a
            if all(abs((g * r["gramatica"] + a * r["abrangencia"] + t * r["tangenciamento"]) / 100
                       - r["nota_online"]) < 1e-9 for r in dados):
                print(f"    wG={g}% wA={a}% wT={t}%")


if __name__ == "__main__":
    main()
