"""Gera as variantes experimentais a partir do texto-base, aplicando substituições exatas.

Uso: python3 ferramentas/gerar_variantes.py

Cada substituição precisa ocorrer exatamente uma vez no texto; caso contrário o script para. Assim, cada
variante difere do texto-base apenas pelo que está declarado aqui, e o diff fica registrado no próprio código.
As variantes são gravadas em experimentos/variantes/, junto com MUDANCAS.md (cada substituição, antes e depois,
e a extensão resultante), e a tabela de extensão é impressa no fim.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = RAIZ / "avaliacoes" / "001-descarte-lixo" / "redacao.txt"
SAIDA = RAIZ / "experimentos" / "variantes"

P2 = ("As implicações do descarte indevido atingem o meio ambiente, a saúde e a economia. O lixo jogado nas ruas "
      "entope bueiros e agrava enchentes, enquanto os resíduos acumulados em lixões contaminam o solo e os lençóis "
      "freáticos. Além disso, o acúmulo de lixo favorece a proliferação de vetores de doenças, como o mosquito da "
      "dengue, o que sobrecarrega o sistema público de saúde. Há ainda um desperdício econômico, pois materiais que "
      "poderiam ser reaproveitados deixam de gerar renda, sobretudo para os catadores.\n")

ERROS_4 = [
    ("Cabe às prefeituras", "Cabe as prefeituras"),                      # crase
    ("contaminam o solo", "contamina o solo"),                            # concordância verbal
    ("As escolas devem incluir", "As escolas deve incluir"),              # concordância verbal
    ("lençóis freáticos", "lençois freáticos"),                           # acentuação
]
ERROS_8_EXTRAS = [
    ("materiais recicláveis misturados", "materiais recicláveis misturado"),  # concordância nominal
    ("proliferação", "proliferassão"),                                    # ortografia
    ("sobrecarrega", "sobrecarega"),                                      # ortografia
    ("desperdício", "desperdicio"),                                       # acentuação
    ("ferramentas fundamentais", "ferramentas fundamental"),              # concordância nominal
    ("Há ainda", "A ainda"),                                              # há/a
    ("futuras gerações", "futuras geraçoes"),                             # acentuação
    ("entrega voluntária", "entrega voluntaria"),                         # acentuação
]

VARIANTES = {
    "X0-reteste": [],
    "X1a-mais-4-erros": ERROS_4,
    "X1b-mais-12-erros": ERROS_4 + ERROS_8_EXTRAS,
    "X2-sem-falsos-positivos": [
        ("Apesar de a separação do lixo ser uma prática simples,",
         "Ainda que a separação do lixo seja uma prática simples,"),
        ("além de entulho e embalagens abandonados em ruas, terrenos e rios.",
         "além do abandono de entulho e embalagens em ruas, terrenos e rios."),
        ("isoladamente, não conseguem.", "isoladamente, não conseguem fazer."),
        ("compreende que o seu descarte", "compreende que seu descarte"),
        ("Ao cidadão, compete separar o lixo", "Compete ao cidadão separar o lixo"),
    ],
    "X3-fatos-em-P1-P2": [
        ("não garante mudança de comportamento.",
         "não garante mudança de comportamento. Prova disso é que o prazo legal para o fim dos lixões, 2014, foi "
         "descumprido e prorrogado pelo Marco Legal do Saneamento, em 2020."),
        ("como o mosquito da dengue,",
         "como o Aedes aegypti, que se reproduz na água parada de pneus e garrafas descartados,"),
        ("sobretudo para os catadores.",
         "sobretudo para os catadores. O acidente com o césio-137 em Goiânia, em 1987, causado pelo abandono de um "
         "aparelho de radioterapia, mostra que o descarte indevido pode ser trágico."),
    ],
    "X4-aprofunda-recorte": [
        ("por convicção, e não por imposição.",
         "por convicção, e não por imposição. Isso ocorre porque o descarte correto depende de pequenas decisões "
         "diárias, como separar os recicláveis e levar pilhas e eletrônicos a pontos adequados, que nenhuma "
         "fiscalização consegue acompanhar em cada casa. Além disso, a educação tem efeito multiplicador: crianças "
         "que aprendem a separar o lixo na escola levam esse hábito para a família e para a comunidade."),
    ],
    "X5-so-extensao": [
        ("por convicção, e não por imposição.",
         "por convicção, e não por imposição. Em outras palavras, a educação e a conscientização transformam a "
         "maneira como as pessoas se relacionam com os resíduos que produzem, e essa transformação tende a "
         "permanecer ao longo do tempo. Trata-se, portanto, de uma mudança que nasce do entendimento das próprias "
         "pessoas, e não apenas da obrigação imposta a elas por regras externas."),
    ],
    "X6-tese-explicita": [
        ("não garante mudança de comportamento.",
         "não garante mudança de comportamento, o que torna a educação e a conscientização indispensáveis para "
         "que o descarte correto se torne um hábito."),
    ],
    # Troca o parágrafo das implicações (pergunta 2) por outro de extensão semelhante sobre educação, sem fatos novos:
    # a cobertura das perguntas cai de 4 para 3 enquanto a extensão fica constante. Remover o P2 sem reposição
    # deixaria o texto com ~1.140 caracteres sem espaços, abaixo do mínimo, o que confundiria o teste.
    "X7-troca-P2": [(P2, "A educação ambiental também forma cidadãos capazes de compreender o ciclo dos resíduos, "
                         "desde a produção até o destino final. Quando esse conhecimento é construído desde a "
                         "infância, a separação do lixo deixa de ser vista como uma tarefa incômoda e passa a fazer "
                         "parte da rotina. Do mesmo modo, a conscientização dos adultos, por meio do diálogo e do "
                         "exemplo, fortalece o sentimento de pertencimento à comunidade e torna cada pessoa "
                         "corresponsável pelos espaços que compartilha.\n")],
}


def aplicar(texto, substituicoes, nome):
    for antigo, novo in substituicoes:
        n = texto.count(antigo)
        if n != 1:
            raise SystemExit(f"{nome}: '{antigo[:50]}' ocorre {n} vezes (esperado: 1)")
        texto = texto.replace(antigo, novo)
    return texto


def medidas(texto):
    corrido = texto.rstrip("\n").replace("\n", "")
    return (len(corrido), len(re.sub(r"\s", "", corrido)),
            len(re.findall(r"[\wÀ-ÿ]+(?:-[\wÀ-ÿ]+)*", corrido)), len(texto.rstrip("\n").split("\n")))


def main():
    base = BASE.read_text(encoding="utf-8")
    SAIDA.mkdir(parents=True, exist_ok=True)
    c0, s0, w0, p0 = medidas(base)
    doc = ["# Mudanças exatas de cada variante", "",
           "Gerado por `ferramentas/gerar_variantes.py`; não edite à mão. Caracteres contados sem as quebras de "
           "parágrafo.", "",
           f"Base: {c0} caracteres com espaços, {s0} sem espaços, {w0} palavras, {p0} parágrafos.", ""]
    print(f"{'variante':<26}{'chars c/esp':>12}{'Δ%':>7}{'chars s/esp':>12}{'palavras':>10}{'parágr.':>9}")
    print(f"{'base':<26}{c0:>12}{'':>7}{s0:>12}{w0:>10}{p0:>9}")
    for nome, subs in VARIANTES.items():
        texto = aplicar(base, subs, nome)
        (SAIDA / f"{nome}.txt").write_text(texto, encoding="utf-8")
        c, s, w, p = medidas(texto)
        print(f"{nome:<26}{c:>12}{(c - c0) / c0:>+7.1%}{s:>12}{w:>10}{p:>9}")
        doc += [f"## {nome}", "",
                f"{c} caracteres com espaços ({(c - c0) / c0:+.1%}), {s} sem espaços, {w} palavras, {p} parágrafos.",
                ""]
        if not subs:
            doc += ["Texto idêntico à base.", ""]
        for i, (antigo, novo) in enumerate(subs, 1):
            doc += [f"{i}. Antes: «{antigo.strip()}»", f"   Depois: «{novo.strip()}»" if novo.strip()
                    else "   Depois: (removido)", ""]
    (SAIDA / "MUDANCAS.md").write_text("\n".join(doc), encoding="utf-8")


if __name__ == "__main__":
    main()
