"""Rubrica calibrada v1: critérios com teto 10 que reproduzem as notas exibidas nas avaliações reais.

Uso: python3 ferramentas/rubrica_calibrada.py

Para cada avaliação, aplica os três critérios e compara com o que a plataforma mostrou; depois imprime as previsões
para os textos da série 005. Os critérios estão descritos em `modelo/rubrica-calibrada.md`.

- Gramática: calculada do texto e das contagens de erros.
- Tangenciamento: calculado só do texto (palavras e pares da frase do tema).
- Abrangência: sai das ANOTACOES abaixo, que são a correção feita à mão, parágrafo a parágrafo, com o motivo de cada
  desconto. A plataforma exibe 0,4 × a nota bruta (hipótese H-A-esc).
"""
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sobreposicao_lexical as lex  # noqa: E402

RAIZ = lex.RAIZ


def arred1(x):
    return float(Decimal(repr(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


# Cada parágrafo de resposta (sem contar o título) tem a evidência concreta e pertinente que encontrei, ou None.
# Evidência concreta: dado com número e fonte, fato identificado (lugar ou data), lei ou política nomeada, ou, no
# parágrafo de propostas, órgão específico nomeado como agente. Repertório de bolso e dado que não prova a afirmação
# não contam. "E" é o apontamento exibido pela plataforma; "S", os erros de ortografia que encontrei.
ANOTACOES = {
    "001": {
        "E": 4, "S": 0,
        "evidencia": ["Política Nacional de Resíduos Sólidos (2010)", None, None, None],
        "recorte_intro": False,
        "nao_pertinente": [], "vago": [], "bolso": [],
        "notas": "§2 cita a dengue só como exemplo genérico; §4 tem agentes genéricos (escolas, prefeituras, cidadão); "
                 "a introdução não fala de educação nem de conscientização",
    },
    "002": {
        "E": 7, "S": 0,
        "evidencia": [None, None, None, None],
        "recorte_intro": True,
        "nao_pertinente": [], "vago": [], "bolso": [],
        "notas": "nenhum dado, fato, lei ou órgão nomeado; agentes genéricos (população, escolas, poder público)",
    },
    "003": {
        "E": 0, "S": 6,
        "evidencia": [None, None, None, None],
        "recorte_intro": True,
        "nao_pertinente": ["endividamento apresentado como consequência do consumismo (\"Além do endividamento\")"],
        "vago": [], "bolso": [],
        "notas": "ortografia: inpulso, quicições, estração, obsjetos, empregradaos, compar",
    },
    "004": {
        "E": 1, "S": 0,
        "evidencia": [None, None, "ONU: mais de 60 milhões de toneladas de lixo eletrônico em 2022",
                      "Ministério da Educação"],
        "recorte_intro": True,
        "nao_pertinente": ["CNC: 75% das famílias endividadas, como prova de compra por impulso"],
        "vago": [], "bolso": ["Zygmunt Bauman, Vida para consumo"],
        "notas": "§1 só tem Bauman (bolso); §2 só tem o dado da CNC, que não prova consumismo",
    },
    "005": {
        "E": 2, "S": 0,
        "evidencia": [None, "Lei 12.305/2010 (Política Nacional de Resíduos Sólidos)", None,
                      "Ministério do Meio Ambiente e Mudança do Clima"],
        "recorte_intro": True,
        "nao_pertinente": [], "vago": ["Panorama dos Resíduos Sólidos: \"milhões de toneladas\", sem número"],
        "bolso": ["Paulo Freire"],
        "notas": "§3 só tem Paulo Freire (bolso)",
    },
}

# Textos ainda não avaliados: as previsões ficam registradas antes do resultado.
PREVISOES = {
    "D2": ("lixo", "experimentos/textos/D2-lixo-metodo.txt", {
        "E": 0, "S": 0,
        "evidencia": ["Ibope 2018: 97% e 39%", "Goiânia, 1987: césio-137",
                      "Constituição, artigo 225 (educação ambiental)", "Ministério da Educação"],
        "recorte_intro": True, "nao_pertinente": [], "vago": [], "bolso": []}),
    "C2": ("consumo", "experimentos/textos/C2-consumo-metodo.txt", {
        "E": 0, "S": 0,
        "evidencia": [None, "Código de Defesa do Consumidor, artigo 49",
                      "Fundação Ellen MacArthur (36%); ONU (62 milhões de toneladas, 2022)", "Ministério da Educação"],
        "recorte_intro": True, "nao_pertinente": [], "vago": [], "bolso": []}),
    "M6": ("clima", "experimentos/textos/M6-clima-metodo.txt", {
        "E": 0, "S": 0,
        "evidencia": ["Organização Meteorológica Mundial: 2024, ano mais quente",
                      "enchentes no Rio Grande do Sul (2024) e Petrópolis (2022)",
                      "Science (2021); IPCC; SEEG", None],
        "recorte_intro": True, "nao_pertinente": [], "vago": [], "bolso": []}),
}

DESCONTOS = {"sem_evidencia": 0.5, "recorte_fora": 1.0, "nao_pertinente": 2.0, "vago": 1.0, "bolso": 1.0}
ESCALA_A = 0.4  # hipótese H-A-esc: Abrangência exibida = 0,4 × nota bruta


def paragrafos(texto):
    pars = [p.strip() for p in texto.split("\n") if p.strip()]
    if len(pars) >= 2 and len(pars[0]) < 90 and not re.search(r"[.!?:;]$", pars[0]):
        return pars[0], pars[1:]
    return None, pars


def gramatica(texto, E, S):
    """G = arred(10(1 − n/W)), n = E + 1,5·S, W = palavras nos primeiros 2.000 caracteres."""
    corrido = "\n\n".join(p.strip() for p in texto.split("\n") if p.strip())[:2000]
    W = len(corrido.split())
    return arred1(10 * (1 - (E + 1.5 * S) / W)), W


def abrangencia_bruta(a):
    d = DESCONTOS
    total = (d["sem_evidencia"] * sum(1 for e in a["evidencia"] if not e)
             + (0 if a["recorte_intro"] else d["recorte_fora"])
             + d["nao_pertinente"] * len(a["nao_pertinente"])
             + d["vago"] * len(a["vago"])
             + d["bolso"] * len(a["bolso"]))
    return max(0.0, 10 - total)


def tangenciamento(texto, tema):
    """T = 10 − 3·(palavras do tema ausentes) − 0,8·(pares ausentes) − 0,25·(palavras do tema ausentes da introdução)
    − 1,05 se o último parágrafo não traz a frase do tema completa (componente não observado: hipótese H-T-conc)."""
    frase = lex.PROPOSTAS[tema]["tema"]
    _, pars = paragrafos(texto)
    pt = set(lex.palavras(texto))
    ptema = set(lex.palavras(frase))
    t = len(ptema & pt) / len(ptema)
    tokens = re.findall(r"[a-z]+", lex.normalizar(frase))
    bigramas = [" ".join(tokens[i:i + 2]) for i in range(len(tokens) - 1)]
    fluxo = " " + " ".join(re.findall(r"[a-z]+", lex.normalizar(texto))) + " "
    p = sum(1 for b in bigramas if f" {b} " in fluxo) / len(bigramas)
    i = len(ptema & set(lex.palavras(pars[0]))) / len(ptema)
    ultimo = " " + " ".join(re.findall(r"[a-z]+", lex.normalizar(pars[-1]))) + " "
    c = 1 if " " + " ".join(tokens) + " " in ultimo else 0
    valor = 10 - 3 * (1 - t) - 0.8 * (1 - p) - 0.25 * (1 - i) - 1.05 * (1 - c)
    return arred1(valor), dict(tema=t, pares=p, intro=i, conclusao=c)


def avaliar(texto, tema, a):
    G, W = gramatica(texto, a["E"], a["S"])
    Ab = abrangencia_bruta(a)
    T, feat = tangenciamento(texto, tema)
    A = arred1(ESCALA_A * Ab)
    return dict(G=G, W=W, Ab=Ab, A=A, T=T, feat=feat,
                online=arred1(0.4 * G + 0.4 * A + 0.2 * T), criterio=arred1(0.4 * G + 0.4 * Ab + 0.2 * T))


def main():
    import csv
    obs = {r["id"]: r for r in csv.DictReader(open(RAIZ / "dados" / "avaliacoes.csv", encoding="utf-8"))}
    print("Avaliações reais: previsto pela rubrica / exibido pela plataforma\n")
    print(f"{'aval.':<6}{'G':>11}{'A bruta':>9}{'A':>11}{'T':>11}{'online':>12}{'critério':>10}")
    acertos = {"G": 0, "A": 0, "T": 0, "online": 0}
    for id_, a in ANOTACOES.items():
        tema, caminho = lex.AVALIACOES[id_]
        r = avaliar((RAIZ / caminho).read_text(encoding="utf-8"), tema, a)
        o = {k: float(obs[id_][c]) for k, c in
             [("G", "gramatica"), ("A", "abrangencia"), ("T", "tangenciamento"), ("online", "nota_online")]}
        cel = []
        for k in ("G", "A", "T", "online"):
            ok = abs(r[k] - o[k]) < 1e-9
            acertos[k] += ok
            cel.append(f"{r[k]:.1f}/{o[k]:.1f}{'' if ok else ' ✗'}")
        print(f"{id_:<6}{cel[0]:>11}{r['Ab']:>9.1f}{cel[1]:>11}{cel[2]:>11}{cel[3]:>12}{r['criterio']:>10.1f}")
    print("\nacertos exatos: " + ", ".join(f"{k} {v}/5" for k, v in acertos.items()))

    print("\nPrevisões para a série 005 (registradas antes do envio)\n")
    print(f"{'texto':<6}{'G':>6}{'A bruta':>9}{'A':>6}{'T':>6}{'online':>8}{'critério':>10}  T: tema/pares/intro/conclusão")
    for nome, (tema, caminho, a) in PREVISOES.items():
        r = avaliar((RAIZ / caminho).read_text(encoding="utf-8"), tema, a)
        f = r["feat"]
        print(f"{nome:<6}{r['G']:>6.1f}{r['Ab']:>9.1f}{r['A']:>6.1f}{r['T']:>6.1f}{r['online']:>8.1f}{r['criterio']:>10.1f}"
              f"  {f['tema']:.2f}/{f['pares']:.2f}/{f['intro']:.2f}/{f['conclusao']}")


if __name__ == "__main__":
    main()
