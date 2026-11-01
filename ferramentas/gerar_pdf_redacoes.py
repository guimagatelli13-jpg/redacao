"""Gera o PDF de uma série de redações, um tema por página.

Uso (na raiz do repositório): python3 ferramentas/gerar_pdf_redacoes.py SERIE      (SERIE = 007 a 011)
"""
import sys
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

TEMAS = {
    "lixo": ("DESCARTE CORRETO DO LIXO", "a importância da educação e da conscientização sobre o descarte correto do lixo"),
    "consumo": ("CONSUMO E CONSUMISMO", "consumo e consumismo: como estabelecer limite entre o necessário e o exagero"),
    "clima": ("MUDANÇAS CLIMÁTICAS", "efeitos negativos das mudanças climáticas"),
}
SERIES = {
    "007": {
        "titulo": "série 007 · textos de teste para o simulador de treino",
        "textos": [("lixo", "D3-lixo-nota10"), ("consumo", "C3-consumo-nota10"), ("clima", "M7-clima-nota10")],
        "previsao": {t: "Gramática 10,0 · Abrangência 4,0 · Tangenciamento 10,0 · nota online 7,6 (se a plataforma exibe "
                        "0,4 × a Abrangência). Nota pelo critério: 10,0." for t in TEMAS},
    },
    "008": {
        "titulo": "série 008 · método da professora, corrigido em cinco rodadas",
        "textos": [("lixo", "D4-lixo-professora"), ("consumo", "C4-consumo-professora"), ("clima", "M8-clima-professora")],
        "previsao": {
            "lixo": "Gramática 10,0 · Abrangência 3,0 (2,8 a 3,2) · Tangenciamento 8,7 · nota online 6,9 (6,7 a 7,1). Pela rubrica: 10,0.",
            "consumo": "Gramática 10,0 · Abrangência 2,5 (2,4 a 2,7) · Tangenciamento 8,7 · nota online 6,7 (6,6 a 6,9). Pela rubrica: 10,0.",
            "clima": "Gramática 10,0 · Abrangência 2,8 (2,4 a 3,2) · Tangenciamento 8,7 · nota online 6,9 (6,6 a 7,1). Pela rubrica: 10,0.",
        },
    },
    "009": {
        "titulo": "série 009 · padrão ENEM, aberta por repertório",
        "textos": [("lixo", "D5-lixo-enem"), ("consumo", "C5-consumo-enem"), ("clima", "M9-clima-enem")],
        "previsao": {
            "lixo": "Plataforma: Gramática 10,0 · Abrangência 3,0 (2,8 a 3,2) · Tangenciamento 8,7 · nota online 6,9 (6,7 a 7,1). Autoavaliação ENEM: 1000.",
            "consumo": "Plataforma: Gramática 10,0 · Abrangência 2,5 (2,4 a 2,7) · Tangenciamento 8,6 · nota online 6,7 (6,6 a 6,9). Autoavaliação ENEM: 1000.",
            "clima": "Plataforma: Gramática 10,0 · Abrangência 2,8 (2,4 a 3,2) · Tangenciamento 8,7 · nota online 6,9 (6,6 a 7,1). Autoavaliação ENEM: 1000.",
        },
    },
    "010": {
        "titulo": "série 010 · escrita do zero pelos princípios de uma redação excelente",
        "textos": [("lixo", "D6-lixo-excelente"), ("consumo", "C6-consumo-excelente"), ("clima", "M10-clima-excelente")],
        "previsao": {
            "lixo": "Tese: o brasileiro não ignora o problema, ignora o gesto. Plataforma (previsão): nota online 6,9 (6,7 a 7,1).",
            "consumo": "Tese: o limite entre o necessário e o exagero é o uso, não a renúncia. Plataforma (previsão): nota online 6,7 (6,6 a 6,9).",
            "clima": "Tese: os efeitos atingem primeiro quem menos os causou. Plataforma (previsão): nota online 6,9 (6,6 a 7,1).",
        },
    },
    "011": {
        "titulo": "série 011 · voz de autor",
        "textos": [("lixo", "D7-lixo-autor"), ("consumo", "C7-consumo-autor"), ("clima", "M11-clima-autor")],
        "previsao": {
            "lixo": "Abre com \u201cLixo Extraordinário\u201d e fecha com Gramacho. Plataforma (previsão): nota online 6,9 (6,7 a 7,1).",
            "consumo": "Abre com o cartel Phoebus (1924) e fecha com ele. Plataforma (previsão): nota online 6,7 (6,6 a 6,9).",
            "clima": "Abre com o cavalo Caramelo e fecha com ele. Plataforma (previsão): nota online 6,9 (6,6 a 7,1).",
        },
    },
}

F = "/usr/share/fonts/truetype/liberation/"
for nome, arq in [("Serif", "LiberationSerif-Regular"), ("Serif-Bold", "LiberationSerif-Bold"),
                  ("Serif-Italic", "LiberationSerif-Italic"), ("Sans", "LiberationSans-Regular"), ("Sans-Bold", "LiberationSans-Bold")]:
    pdfmetrics.registerFont(TTFont(nome, F + arq + ".ttf"))
registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-Bold")

TINTA, CINZA, AZUL = colors.HexColor("#1d1b18"), colors.HexColor("#6b655c"), colors.HexColor("#1f5c86")
ROTULO = ParagraphStyle("rotulo", fontName="Sans-Bold", fontSize=8.5, leading=11, textColor=CINZA)
TITULO = ParagraphStyle("titulo", fontName="Serif-Bold", fontSize=17, leading=21, textColor=TINTA, spaceBefore=2, spaceAfter=4)
TEMA = ParagraphStyle("tema", fontName="Serif-Italic", fontSize=10.5, leading=14, textColor=CINZA, spaceAfter=14)
CORPO = ParagraphStyle("corpo", fontName="Serif", fontSize=12, leading=18.5, alignment=TA_JUSTIFY,
                       firstLineIndent=1.25 * cm, spaceAfter=9, textColor=TINTA)
NOTA = ParagraphStyle("nota", fontName="Sans", fontSize=8.8, leading=12, textColor=CINZA)
NOTA_B = ParagraphStyle("notab", parent=NOTA, fontName="Sans-Bold", textColor=TINTA)


def gerar(serie):
    cfg = SERIES[serie]
    total = len(cfg["textos"])

    def rodape(c, doc):
        c.saveState()
        c.setFont("Sans", 8)
        c.setFillColor(CINZA)
        c.drawString(2.2 * cm, 1.3 * cm, "Simulador de redação · " + cfg["titulo"])
        c.drawRightString(A4[0] - 2.2 * cm, 1.3 * cm, f"{doc.page} / {total}")
        c.restoreState()

    story = []
    for i, (tema, arquivo) in enumerate(cfg["textos"]):
        tit, frase = TEMAS[tema]
        pars = [p.strip() for p in open(f"experimentos/textos/{arquivo}.txt", encoding="utf-8").read().split("\n") if p.strip()]
        chars = f"{len(chr(10).join(pars)) + len(pars) - 1:,}".replace(",", ".")
        story += [Paragraph(f"TEXTO PARA TESTE · TEMA {i + 1} DE {total}", ROTULO), Paragraph(escape(tit), TITULO),
                  Paragraph(f"Tema: “{escape(frase)}”", TEMA)]
        story += [Paragraph(escape(p), CORPO) for p in pars]
        info = Table([
            [Paragraph("Como enviar", NOTA_B), Paragraph("Copie só o texto, sem título, com uma linha em branco entre os "
                                                          f"parágrafos: {chars} caracteres como a plataforma conta.", NOTA)],
            [Paragraph("Previsão registrada", NOTA_B), Paragraph(cfg["previsao"][tema], NOTA)],
            [Paragraph("Depois do envio", NOTA_B), Paragraph("Registre os seis campos no histórico do simulador "
                                                             "(“Registrar notas oficiais”).", NOTA)],
        ], colWidths=[3.4 * cm, None])
        info.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 0), (-1, 0), 0.6, AZUL),
                                  ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
        story += [Spacer(1, 10), info]
        if i < total - 1:
            story.append(PageBreak())

    saida = f"entregas/redacoes-serie-{serie}.pdf"
    SimpleDocTemplate(saida, pagesize=A4, leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=2 * cm, bottomMargin=2.2 * cm,
                      title=f"Redações para teste — série {serie}", author="Simulador de redação",
                      subject="Textos de teste para o simulador de treino").build(story, onFirstPage=rodape, onLaterPages=rodape)
    print(saida)


if __name__ == "__main__":
    gerar(sys.argv[1] if len(sys.argv) > 1 else "011")
