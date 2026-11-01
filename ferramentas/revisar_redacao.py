"""Revisão automática de uma redação pelos critérios do método da professora e do que se sabe da plataforma.

Uso: python3 ferramentas/revisar_redacao.py TEXTO.txt TEMA     (TEMA = lixo, consumo ou clima)

Cobre o que dá para medir: tamanho, uma pergunta por parágrafo, frase e palavras do tema, evidência por parágrafo,
repertório de bolso, dado vago, endividamento (no consumo), gerúndio, frases longas, palavras repetidas e conectivos
repetidos na abertura dos parágrafos. Pertinência dos dados, pontas soltas e coesão de sentido continuam exigindo
leitura humana; a lista de falhas desta ferramenta é o ponto de partida da correção, não o fim.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rubrica_calibrada as rc  # noqa: E402
import sobreposicao_lexical as lex  # noqa: E402

PERGUNTAS = {}
for tema, info in lex.PROPOSTAS.items():
    PERGUNTAS[tema] = [l[2:] for l in Path(info["arquivo"]).read_text(encoding="utf-8").split("\n") if l.startswith("- ")]

PARADAS = {lex.normalizar(p) for p in lex.PARADAS}
# Gerúndios que fazem parte das próprias perguntas da proposta não contam.
GERUNDIOS_DA_PROPOSTA = {"contribuindo"}
NAO_GERUNDIO = {"quando", "segundo", "mundo", "fundo", "profundo", "rotundo", "oriundo", "nefando", "tremendo", "estupendo",
                "horrendo", "comando", "bando", "brando", "mando", "nando", "fecundo", "imundo", "vagabundo", "redondo"}


def palavras_limpas(texto):
    return [p for p in re.findall(r"[a-z]+", lex.normalizar(texto)) if p not in PARADAS and len(p) > 2]


def frases(p):
    return [f for f in re.split(r"(?<=[.!?])\s+", p) if f]


def revisar(caminho, tema):
    texto = Path(caminho).read_text(encoding="utf-8")
    titulo, pars = rc.paragrafos(texto)
    falhas, ok = [], []

    chars = len("\n\n".join(pars if not titulo else [titulo] + pars))
    (ok if 1200 <= chars <= 2000 else falhas).append(f"tamanho: {chars} caracteres (com linha em branco entre parágrafos)")

    qs = PERGUNTAS[tema]
    n_esperado = len(qs) if tema != "clima" else (4, 5)
    if (len(pars) in n_esperado) if isinstance(n_esperado, tuple) else len(pars) == n_esperado:
        ok.append(f"{len(pars)} parágrafos")
    else:
        falhas.append(f"{len(pars)} parágrafos; o esperado é um por pergunta")
    # Cada parágrafo responde à sua pergunta: as palavras da pergunta precisam estar no parágrafo, mas não
    # necessariamente na primeira frase (a abertura repetindo a pergunta soa solta).
    mapa = list(range(len(qs))) if len(pars) == len(qs) else ([0, 1, 2, 2, 3] if tema == "clima" and len(pars) == 4 else None)
    if mapa:
        for i, q in enumerate(qs):
            j = mapa[i]
            qp = set(palavras_limpas(q))
            cob = len(qp & set(palavras_limpas(pars[j]))) / len(qp)
            faltam = sorted(qp - set(palavras_limpas(pars[j])))
            (ok if cob >= 0.8 else falhas).append(
                f"P{i + 1} no §{j + 1}: o parágrafo retoma {cob:.0%} das palavras da pergunta" + (f" (faltam {', '.join(faltam)})" if faltam else ""))

    # O texto começa por um repertório (dado, fato, lei, obra), não pela pergunta da proposta.
    primeira = frases(pars[0])[0]
    n1 = lex.normalizar(primeira)
    repert = re.search(r"\d", primeira) or re.search(rc.LEI, n1) or re.search(r"\b(segundo|conforme|de acordo com)\b", n1)
    (ok if repert else falhas).append("a primeira frase traz um repertório" if repert else f"a primeira frase não traz repertório: “{primeira}”")

    # Frases soltas: cada frase (e cada parágrafo, a partir do 2º) deve se prender ao que veio antes por um conectivo
    # ou por uma retomada (pronome demonstrativo, "tal", "assim"...) logo no começo.
    ELO = re.compile(r"\b(esse|essa|esses|essas|isso|este|esta|estes|estas|isto|tal|tais|dessa|desse|desses|dessas|disso|nesse|nessa|"
                     r"nesses|nessas|neste|nesta|ambos|ambas|assim|logo|portanto|porem|contudo|entretanto|todavia|alem disso|ademais|"
                     r"por isso|desse modo|dessa forma|diante|ou seja|com isso|consequentemente|por conseguinte|nao por acaso|"
                     r"paralelamente|so assim|embora|ainda que|apesar|mesmo|tambem|afinal|quando|como|dai|enfim|por sua vez|"
                     r"o mesmo|a mesma|seu|sua|seus|suas|dele|dela|deles|delas|o primeiro|o segundo|no primeiro|no segundo|"
                     r"em ambos|antes|depois|mais de|trinta|decadas|aquele|aquela|aqueles|aquelas|na pratica|prova disso|em primeiro lugar|"
                     r"primeiramente|por fim|nesse sentido|isso porque|ainda|para tanto|entre as|entre os|ele|ela|eles|elas|o restante|os demais|nisso|no extremo|no limite)\b")
    soltas = []
    for j, p in enumerate(pars):
        for k, f in enumerate(frases(p)):
            if j == 0 and k == 0:
                continue
            inicio = " ".join(lex.normalizar(f).split()[:8])
            if not ELO.search(inicio):
                soltas.append(f"§{j + 1}, frase {k + 1}: “{' '.join(f.split()[:8])}…”")
    (falhas if soltas else ok).append(f"frases sem elo com a anterior no começo: {soltas or 'nenhuma'}")

    m = lex.medir(caminho, tema)
    T, feat = rc.tangenciamento(texto, tema)
    (ok if m["tema"] == 1 else falhas).append(f"palavras da frase do tema no texto: {m['tema']:.0%}")
    (ok if feat["intro"] == 1 else falhas).append(f"palavras da frase do tema na introdução: {feat['intro']:.0%}")
    (ok if m["nucleo"] == 1 else falhas).append(f"núcleo (tema + perguntas): {m['nucleo']:.2f}" + (f"; faltam {m['ausentes']}" if m["ausentes"] else ""))

    a = rc.abrangencia_automatica(texto, tema)
    for i, e in enumerate(a["evidencia"]):
        (ok if e else falhas).append(f"§{i + 1}: {'tem' if e else 'sem'} evidência concreta (dado com número e fonte, fato com data, lei ou órgão)")
    (ok if a["recorte_intro"] else falhas).append("recorte do tema na introdução")
    if a["bolso"]: falhas.append(f"repertório de bolso: {a['bolso']}")
    if a["vago"]: falhas.append(f"dado vago: {a['vago']}")
    if a["nao_pertinente"]: falhas.append("endividamento usado no tema consumo (não prova consumismo)")

    gerundios = [g for g in re.findall(r"\b\w+ndo\b", texto.lower())
                 if lex.normalizar(g) not in NAO_GERUNDIO and g not in GERUNDIOS_DA_PROPOSTA]
    (falhas if gerundios else ok).append(f"gerúndios: {gerundios or 'nenhum'}")
    longas = [f for p in pars for f in frases(p) if len(f.split()) > 40]
    (falhas if longas else ok).append(f"frases com mais de 40 palavras: {len(longas)}")

    tema_pal = set(palavras_limpas(lex.PROPOSTAS[tema]["tema"] + " " + " ".join(qs)))
    cont = Counter(p for p in palavras_limpas(texto) if p not in tema_pal)
    repetidas = [(p, n) for p, n in cont.most_common() if n >= 3]
    (falhas if repetidas else ok).append(f"palavras repetidas 3 vezes ou mais (fora as da proposta): {repetidas or 'nenhuma'}")
    # Primeira palavra de cada parágrafo, sem contar artigos: um conectivo repetido na abertura é falha de coesão.
    aberturas = [re.split(r"[ ,]", lex.normalizar(p), maxsplit=1)[0] for p in pars]
    rep_ab = [x for x, n in Counter(aberturas).items() if n > 1 and x not in {"a", "o", "as", "os", "um", "uma"}]
    conectivos = Counter(c for c in re.findall(r"\b(portanto|assim|logo|alem disso|por isso|dessa forma|desse modo|nesse contexto|ademais|"
                                               r"contudo|entretanto|no entanto|ou seja|consequentemente|por fim)\b", lex.normalizar(texto)))
    rep_con = [(c, n) for c, n in conectivos.items() if n > 1]
    (falhas if rep_con else ok).append(f"conectivos repetidos no texto: {rep_con or 'nenhum'}")

    # Clichês que um corretor exigente desconta, e presença de contraponto (concessão seguida de refutação).
    CLICHES = [r"primeiro passo", r"so assim", r"nos dias de hoje", r"hoje em dia", r"nos dias atuais", r"desde os primordios",
               r"de suma importancia", r"cada vez mais", r"mais do que nunca", r"faz-se necessario", r"e notorio", r"e inegavel",
               r"e fundamental", r"e imprescindivel", r"nos ultimos anos", r"questao central", r"recaem sobre todos", r"via de regra"]
    norm_txt = lex.normalizar(texto)
    cliches = [c for c in CLICHES if re.search(r"\b" + c + r"\b", norm_txt)]
    (falhas if cliches else ok).append(f"clichês: {cliches or 'nenhum'}")
    contraponto = re.search(r"pode-se (alegar|objetar|argumentar|dizer)|argumenta-se|alguem (dira|diria|poderia)|e verdade que|"
                            r"poder-se-ia|ha quem (diga|defenda|argumente)|objeta-se", norm_txt)
    (ok if contraponto else falhas).append("contraponto presente" if contraponto else "sem contraponto (objeção reconhecida e refutada)")
    (falhas if rep_ab else ok).append(f"primeira palavra dos parágrafos: {aberturas}")

    return falhas, ok


if __name__ == "__main__":
    falhas, ok = revisar(sys.argv[1], sys.argv[2])
    print(f"== {sys.argv[1]}")
    print(f"FALHAS ({len(falhas)}):")
    for f in falhas: print("  ✕", f)
    print(f"OK ({len(ok)}):")
    for f in ok: print("  ✓", f)
