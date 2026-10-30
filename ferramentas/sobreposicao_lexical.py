"""Mede a sobreposição de vocabulário entre cada redação avaliada e o enunciado da sua proposta.

Uso: python3 ferramentas/sobreposicao_lexical.py            (todas as avaliações registradas)
     python3 ferramentas/sobreposicao_lexical.py TEXTO TEMA  (um texto; TEMA = lixo, consumo ou clima)

Testa a hipótese de que Abrangência e Tangenciamento acompanham a semelhança lexical com a proposta (H-A9, H-T-lex).
As métricas são simples e transparentes (palavras de conteúdo, sem dicionário de sinônimos):
- cobertura: fração das palavras de conteúdo do enunciado inteiro que aparecem no texto;
- núcleo: o mesmo, mas só com a frase do tema e as perguntas, sem as palavras de instrução ("redija", "texto"…);
- cosseno: semelhança entre os vetores de frequência de palavras de conteúdo do texto e do enunciado;
- tema literal: fração das palavras de conteúdo da frase do tema que aparecem no texto;
- n-gramas do tema: quantos bigramas da frase do tema aparecem literalmente no texto.
"""
import csv
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

PARADAS = set("""a o as os um uma uns umas de da do das dos em na no nas nos por pela pelo pelas pelos para pra com sem
sobre entre e ou que se seu sua seus suas ao aos à às é ser são foi era como mais menos muito muita muitos muitas já
não sim também isso esse essa esses essas este esta estes estas aquele aquela ele ela eles elas lhe lhes quando onde
qual quais quem cujo cuja há ter tem têm pode podem deve devem mas porém pois porque assim então portanto ainda
seja sejam você voce num numa nesse nessa neste nesta desse dessa deste desta""".split())

# Enunciado de cada tema (texto da proposta, sem o título) e frase do tema entre aspas.
PROPOSTAS = {
    "lixo": {
        "arquivo": RAIZ / "avaliacoes" / "001-descarte-lixo" / "proposta.md",
        "tema": "a importância da educação e da conscientização sobre o descarte correto do lixo",
    },
    "consumo": {
        "arquivo": RAIZ / "propostas" / "002-consumo-consumismo.md",
        "tema": "consumo e consumismo: como estabelecer limite entre o necessário e o exagero",
    },
    "clima": {
        "arquivo": RAIZ / "propostas" / "003-mudancas-climaticas.md",
        "tema": "efeitos negativos das mudanças climáticas",
    },
}

AVALIACOES = {
    "001": ("lixo", "avaliacoes/001-descarte-lixo/redacao.txt"),
    "002": ("lixo", "avaliacoes/002-descarte-lixo-b/redacao.txt"),
    "003": ("consumo", "avaliacoes/003-consumo-a/redacao.txt"),
    "004": ("consumo", "avaliacoes/004-consumo-b/redacao.txt"),
    "005": ("lixo", "avaliacoes/005-descarte-lixo-c/redacao.txt"),
}


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")


def palavras(texto):
    return [p for p in re.findall(r"[a-z]+", normalizar(texto)) if p not in PARADAS and len(p) > 2]


def nucleo(arquivo, tema):
    """Frase do tema mais as perguntas (linhas com marcador de lista) do enunciado."""
    perguntas = [l[2:] for l in Path(arquivo).read_text(encoding="utf-8").split("\n") if l.startswith("- ")]
    return tema + "\n" + "\n".join(perguntas)


def enunciado(arquivo):
    linhas = Path(arquivo).read_text(encoding="utf-8").split("\n")
    corpo = [l for l in linhas if l.strip() and not l.startswith("#") and not l.startswith("Transcrição")
             and not l.startswith("**Título") and not l.startswith("Limite máximo")]
    return "\n".join(corpo)


def cosseno(a, b):
    ca, cb = Counter(a), Counter(b)
    num = sum(ca[k] * cb[k] for k in ca)
    den = math.sqrt(sum(v * v for v in ca.values())) * math.sqrt(sum(v * v for v in cb.values()))
    return num / den if den else 0.0


def medir(caminho_texto, tema):
    """Cobertura do núcleo, palavras do tema e pares de palavras do tema para um texto qualquer."""
    texto = Path(caminho_texto).read_text(encoding="utf-8")
    pt = set(palavras(texto))
    pn = set(palavras(nucleo(PROPOSTAS[tema]["arquivo"], PROPOSTAS[tema]["tema"])))
    ptema = set(palavras(PROPOSTAS[tema]["tema"]))
    tn = " " + " ".join(re.findall(r"[a-z]+", normalizar(texto))) + " "
    tokens = re.findall(r"[a-z]+", normalizar(PROPOSTAS[tema]["tema"]))
    bigramas = [" ".join(tokens[i:i + 2]) for i in range(len(tokens) - 1)]
    return {"nucleo": len(pn & pt) / len(pn), "tema": len(ptema & pt) / len(ptema),
            "bigramas": (sum(1 for b in bigramas if f" {b} " in tn), len(bigramas)), "ausentes": sorted(pn - pt)}


def main():
    notas = {}
    with open(RAIZ / "dados" / "avaliacoes.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            notas[r["id"]] = (float(r["abrangencia"]), float(r["tangenciamento"]))
    print(f"{'aval.':<6}{'tema':<9}{'A':>5}{'T':>5}{'cobertura':>11}{'núcleo':>8}{'cosseno':>9}{'tema lit.':>11}{'bigramas':>10}")
    for id_, (tema, caminho) in AVALIACOES.items():
        if id_ not in notas:
            continue
        texto = (RAIZ / caminho).read_text(encoding="utf-8")
        pt = palavras(texto)
        pe = palavras(enunciado(PROPOSTAS[tema]["arquivo"]))
        ptema = palavras(PROPOSTAS[tema]["tema"])
        cobertura = len(set(pe) & set(pt)) / len(set(pe))
        pn = palavras(nucleo(PROPOSTAS[tema]["arquivo"], PROPOSTAS[tema]["tema"]))
        cob_nucleo = len(set(pn) & set(pt)) / len(set(pn))
        tema_lit = len(set(ptema) & set(pt)) / len(set(ptema))
        tn = " ".join(re.findall(r"[a-z]+", normalizar(texto)))
        tema_tokens = re.findall(r"[a-z]+", normalizar(PROPOSTAS[tema]["tema"]))
        bigramas = [" ".join(tema_tokens[i:i + 2]) for i in range(len(tema_tokens) - 1)]
        achados = sum(1 for b in bigramas if f" {b} " in f" {tn} ")
        A, T = notas[id_]
        print(f"{id_:<6}{tema:<9}{A:>5.1f}{T:>5.1f}{cobertura:>11.2f}{cob_nucleo:>8.2f}{cosseno(pt, pe):>9.2f}{tema_lit:>11.2f}"
              f"{f'{achados}/{len(bigramas)}':>10}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        m = medir(sys.argv[1], sys.argv[2])
        print(f"núcleo {m['nucleo']:.2f} | tema {m['tema']:.2f} | pares de palavras do tema "
              f"{m['bigramas'][0]}/{m['bigramas'][1]} | ausentes do núcleo: {m['ausentes']}")
    else:
        main()
