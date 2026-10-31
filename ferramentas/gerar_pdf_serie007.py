"""Gera entregas/redacoes-serie-007.pdf com os textos D3, C3 e M7. Uso: python3 ferramentas/gerar_pdf_serie007.py (na raiz)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape

F = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Serif", F + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", F + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", F + "LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Sans", F + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", F + "LiberationSans-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-Bold")

TINTA = colors.HexColor("#1d1b18"); CINZA = colors.HexColor("#6b655c"); AZUL = colors.HexColor("#1f5c86")
rotulo = ParagraphStyle("rotulo", fontName="Sans-Bold", fontSize=8.5, leading=11, textColor=CINZA)
titulo = ParagraphStyle("titulo", fontName="Serif-Bold", fontSize=17, leading=21, textColor=TINTA, spaceBefore=2, spaceAfter=4)
tema = ParagraphStyle("tema", fontName="Serif-Italic", fontSize=10.5, leading=14, textColor=CINZA, spaceAfter=14)
corpo = ParagraphStyle("corpo", fontName="Serif", fontSize=12, leading=18.5, alignment=TA_JUSTIFY, firstLineIndent=1.25 * cm, spaceAfter=9, textColor=TINTA)
nota = ParagraphStyle("nota", fontName="Sans", fontSize=8.8, leading=12, textColor=CINZA)
nota_b = ParagraphStyle("notab", parent=nota, fontName="Sans-Bold", textColor=TINTA)

TEXTOS = [
    ("DESCARTE CORRETO DO LIXO", "a importância da educação e da conscientização sobre o descarte correto do lixo", "experimentos/textos/D3-lixo-nota10.txt"),
    ("CONSUMO E CONSUMISMO", "consumo e consumismo: como estabelecer limite entre o necessário e o exagero", "experimentos/textos/C3-consumo-nota10.txt"),
    ("MUDANÇAS CLIMÁTICAS", "efeitos negativos das mudanças climáticas", "experimentos/textos/M7-clima-nota10.txt"),
]

def rodape(c, doc):
    c.saveState()
    c.setFont("Sans", 8); c.setFillColor(CINZA)
    c.drawString(2.2 * cm, 1.3 * cm, "Simulador de redação · série 007 · textos de teste para o simulador de treino")
    c.drawRightString(A4[0] - 2.2 * cm, 1.3 * cm, f"{doc.page} / 3")
    c.restoreState()

story = []
for i, (tit, frase, caminho) in enumerate(TEXTOS):
    pars = [p.strip() for p in open(caminho, encoding="utf-8").read().split("\n") if p.strip()]
    chars = len("\n\n".join(pars))
    story.append(Paragraph(f"TEXTO PARA TESTE · TEMA {i + 1} DE 3", rotulo))
    story.append(Paragraph(escape(tit), titulo))
    story.append(Paragraph(f"Tema: “{escape(frase)}”", tema))
    for p in pars:
        story.append(Paragraph(escape(p), corpo))
    story.append(Spacer(1, 10))
    info = Table([
        [Paragraph("Como enviar", nota_b), Paragraph("Copie só o texto, sem título, com uma linha em branco entre os parágrafos: " + f"{chars:,}".replace(",", ".") + " caracteres como a plataforma conta.", nota)],
        [Paragraph("Previsão registrada", nota_b), Paragraph("Gramática 10,0 · Abrangência 4,0 · Tangenciamento 10,0 · nota online 7,6 (se a plataforma exibe 0,4 × a Abrangência). Nota pelo critério: 10,0.", nota)],
        [Paragraph("Depois do envio", nota_b), Paragraph("Registre os seis campos no histórico do simulador (“Registrar notas oficiais”).", nota)],
    ], colWidths=[3.4 * cm, None])
    info.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, AZUL),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(info)
    if i < len(TEXTOS) - 1:
        story.append(PageBreak())

doc = SimpleDocTemplate("entregas/redacoes-serie-007.pdf", pagesize=A4, leftMargin=2.2 * cm, rightMargin=2.2 * cm,
                        topMargin=2 * cm, bottomMargin=2.2 * cm, title="Redações para teste — série 007",
                        author="Simulador de redação", subject="Textos de teste para o simulador de treino")
doc.build(story, onFirstPage=rodape, onLaterPages=rodape)
print("ok")
