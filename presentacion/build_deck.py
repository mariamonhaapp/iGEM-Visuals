"""Builds NEUMA_HP.pptx: three Human Practices slides in the NEUMA visual identity.

Run `node presentacion/build_assets.js` first (map, chip, plasmid figures and icons), then
`python3 presentacion/build_deck.py`.
"""
from pathlib import Path

import qrcode
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
A = HERE / "assets"
ROOT = HERE.parent
WIKI_HP = "https://2026.igem.wiki/puebla/human-practices"

MAROON_DARK, MAROON, CRIMSON = "59181E", "732231", "750E1E"
NAVY, NAVY2, DEEP = "152340", "1D2C40", "001A3B"
TEAL, AMBER, CREAM, CREAM2, PAPER = "014040", "FDAF36", "F2EED8", "EDE9C2", "FFFDF3"
TITLE, BODY = "Bebas Neue", "Source Sans Pro"


def rgb(h):
    return RGBColor.from_string(h)


def box(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, radius=None, dash=False, lw=1.0):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = rgb(fill)
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = rgb(line); s.line.width = Pt(lw)
        if dash:
            s.line.dash_style = 4  # dash
    else:
        s.line.fill.background()
    s.shadow.inherit = False
    s.text_frame.text = ""
    return s


def text(slide, x, y, w, h, runs, size=14, color=CREAM, font=BODY, bold=True, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, italic=False, spacing=None, shape=None):
    """runs: a string, or a list of paragraphs, each a string or a list of (text, overrides) tuples."""
    tb = shape or slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(0.04))
    paras = [runs] if isinstance(runs, str) else runs
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if spacing:
            p.space_after = Pt(spacing)
        for t, o in ([(para, {})] if isinstance(para, str) else para):
            r = p.add_run()
            r.text = t
            f = r.font
            f.name = o.get("font", font); f.size = Pt(o.get("size", size)); f.bold = o.get("bold", bold)
            f.italic = o.get("italic", italic); f.color.rgb = rgb(o.get("color", color))
    return tb


def pic(slide, path, x, y, w=None, h=None):
    return slide.shapes.add_picture(str(path), Inches(x), Inches(y), Inches(w) if w else None, Inches(h) if h else None)


def icon(slide, name, color, x, y, size):
    return pic(slide, A / "icons" / f"{name}-{color}.png", x, y, size, size)


def line(slide, x1, y1, x2, y2, color, width=1.5, dash=False):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color); c.line.width = Pt(width)
    if dash:
        c.line.dash_style = 4
    return c


def arrow(slide, x, y, w, h, color):
    return box(slide, x, y, w, h, fill=color, shape=MSO_SHAPE.RIGHT_ARROW)


def background(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(color)


def header(slide, dark):
    text(slide, 0.5, 0.22, 6, 0.32, "NEUMA  ·  HUMAN PRACTICES", size=15, font=TITLE, bold=False,
         color=AMBER if dark else MAROON)
    pic(slide, ROOT / "animacion" / "logo.png", 12.2, 0.22, 0.82, 0.82)


def notes(slide, body):
    slide.notes_slide.notes_text_frame.text = body


def slide1(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, DEEP)
    header(s, True)
    text(s, 0.5, 0.5, 9, 0.85, "DIAGNOSIS CULTURE IN MEXICO (PUEBLA)", size=46, font=TITLE, bold=False, color=CREAM)
    icon(s, "scan-search", "amber", 0.5, 1.38, 0.42)
    text(s, 1.0, 1.36, 7, 0.45, "Interpretive paradigm  ·  Qualitative approach", size=19, color=CREAM2)

    tiles = [("25", "stethoscope", "clinical\nspecialists"), ("2", "hospital", "public\nhospitals"),
             ("3", "users", "focus\ngroups"), ("20", "messages-square", "voices"), ("8", "microscope", "biosensor\nexperts")]
    for i, (num, ic, label) in enumerate(tiles):
        x = 0.5 + i * 1.43
        box(s, x, 2.05, 1.3, 1.72, fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
        icon(s, ic, "cream", x + 0.14, 2.17, 0.4)
        text(s, x + 0.1, 2.52, 1.15, 0.7, num, size=46, font=TITLE, bold=False, color=AMBER)
        text(s, x + 0.12, 3.15, 1.15, 0.55, label.split("\n"), size=12, color=CREAM)
    text(s, 0.5, 3.85, 7.1, 0.55, [
        [("Hospitals  ", {"color": AMBER}), ("IMSS HGZ No. 20 “La Margarita”  ·  ISSSTE Puebla", {})],
        [("Experts  ", {"color": AMBER}), ("INAOE  ·  UNAM  ·  industry", {})]], size=12, color=CREAM2)

    text(s, 0.5, 4.5, 3, 0.35, "CONTEXT", size=17, font=TITLE, bold=False, color=AMBER)
    for x, fill, num, label, src in [(0.5, TEAL, "77.6%", "of the population is publicly insured", "Commonwealth Fund, 2026"),
                                     (4.1, MAROON, "82%", "of NSCLC cases are diagnosed at a metastatic stage", "Añorve Bailon et al., 2024")]:
        box(s, x, 4.85, 3.45, 1.1, fill=fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
        text(s, x + 0.15, 4.88, 1.35, 0.75, num, size=40, font=TITLE, bold=False, color=CREAM, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x + 1.45, 4.95, 1.9, 0.9, [label, [(src, {"size": 9, "bold": False, "color": CREAM2})]], size=12, color=CREAM)

    box(s, 0.5, 6.18, 0.07, 0.75, fill=AMBER)
    text(s, 0.72, 6.13, 5.2, 0.85, [[("“Culture is an object of interpretation”", {})],
                                    [("Our lens, after Geertz (1973)", {"size": 11, "bold": False, "color": CREAM2, "italic": False})]],
         size=20, color=CREAM, italic=True)
    pic(s, A / "qr_hp.png", 6.25, 6.0, 1.05, 1.05)
    text(s, 6.1, 7.05, 1.4, 0.3, "Human Practices · wiki", size=8, color=CREAM2, align=PP_ALIGN.CENTER, bold=False)

    pic(s, A / "map.png", 8.15, 1.0, 4.4, 4.4)
    for i in range(3):
        x = 7.9 + i * 1.68
        box(s, x, 5.5, 1.55, 1.35, fill=NAVY, line=CREAM2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08, dash=True)
        icon(s, "user-round", "cream", x + 0.6, 5.62, 0.35)
        text(s, x + 0.05, 6.02, 1.45, 0.8, ["Interview / focus", "group photo", [("only with image consent", {"size": 8, "bold": False, "color": AMBER})]],
             size=10, color=CREAM, align=PP_ALIGN.CENTER)
    text(s, 7.9, 6.95, 5.0, 0.3, "Map: svg-maps/mexico (CC BY 4.0), schematic inset", size=8, color=CREAM2, bold=False)
    notes(s, "Sources: Commonwealth Fund (2026), 77.6% of the population covered by public insurance; "
             "Añorve Bailon et al. (2024), ~82% of NSCLC in Mexico diagnosed at a metastatic stage; Geertz (1973), "
             "culture as 'webs of significance' analysed by an interpretive science in search of meaning.\n"
             "Photos: replace the three placeholders only with people marked as consenting in the Notion table.\n"
             f"QR: {WIKI_HP}")


def slide2(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, CREAM)
    header(s, False)
    text(s, 0.5, 0.5, 4, 0.85, "WHAT WE HEARD", size=46, font=TITLE, bold=False, color=DEEP)
    b = box(s, 4.25, 0.7, 7.7, 0.58, fill=MAROON, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
    text(s, 0, 0, 0, 0, "Late diagnosis is systemic, not a lack of education", size=20, color=CREAM,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=b)

    # systemic iceberg
    text(s, 0.45, 1.5, 3.5, 0.35, "THE SYSTEMIC ICEBERG", size=16, font=TITLE, bold=False, color=MAROON)
    box(s, 0.45, 2.95, 3.5, 4.25, fill=NAVY2, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    tip = s.shapes.build_freeform(Inches(1.35), Inches(2.97))
    tip.add_line_segments([(Inches(1.8), Inches(2.48)), (Inches(2.1), Inches(2.66)), (Inches(2.45), Inches(2.32)),
                           (Inches(3.05), Inches(2.97))])
    t = tip.convert_to_shape(); t.fill.solid(); t.fill.fore_color.rgb = rgb(PAPER); t.line.color.rgb = rgb(NAVY); t.shadow.inherit = False
    body = s.shapes.build_freeform(Inches(1.1), Inches(2.99))
    body.add_line_segments([(Inches(3.3), Inches(2.99)), (Inches(3.75), Inches(4.6)), (Inches(3.45), Inches(6.5)),
                            (Inches(2.2), Inches(7.05)), (Inches(0.8), Inches(6.45)), (Inches(0.6), Inches(4.5))])
    bd = body.convert_to_shape(); bd.fill.solid(); bd.fill.fore_color.rgb = rgb(CREAM2); bd.line.fill.background(); bd.shadow.inherit = False
    text(s, 0.45, 1.82, 3.5, 0.4, "LATE DIAGNOSIS", size=24, font=TITLE, bold=False, color=DEEP, align=PP_ALIGN.CENTER)
    for i, (lab, fill) in enumerate([("Economic pressure", DEEP), ("Referral times", DEEP), ("First-level gaps", DEEP), ("Fear", MAROON)]):
        c = box(s, 1.0, 3.35 + i * 0.85, 2.4, 0.55, fill=fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
        text(s, 0, 0, 0, 0, lab, size=14, color=CREAM, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=c)

    # patient pathway
    text(s, 4.25, 1.5, 6, 0.35, "THE PATIENT PATHWAY (PUBLIC INSURANCE)", size=16, font=TITLE, bold=False, color=MAROON)
    nodes = ["First-level care", "Internal medicine", "Pathology", "Pulmonology & oncology"]
    widths = [1.75, 1.75, 1.45, 2.3]
    x = 4.25
    for i, (n, w) in enumerate(zip(nodes, widths)):
        c = box(s, x, 1.9, w, 0.62, fill=NAVY if i < 3 else TEAL, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.25)
        text(s, 0, 0, 0, 0, n, size=13, color=CREAM, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=c)
        x += w
        if i < 3:
            arrow(s, x + 0.05, 2.08, 0.3, 0.26, MAROON)
            x += 0.4
    line(s, 4.3, 2.72, 12.0, 2.72, MAROON, 1.5)
    for xx in (4.3, 12.0):
        line(s, xx, 2.62, xx, 2.82, MAROON, 1.5)
    box(s, 7.15, 2.55, 2.35, 0.36, fill=CREAM)
    icon(s, "clock", "maroon", 7.2, 2.57, 0.32)
    text(s, 7.55, 2.53, 2.0, 0.4, "3 to 8 months", size=15, color=MAROON)

    # findings
    text(s, 4.25, 3.08, 4.4, 0.35, "IN THEIR WORDS AND OURS", size=16, font=TITLE, bold=False, color=MAROON)
    findings = ["“Just a little cough”", "The patient is the family’s provider", "3 to 8 months to a diagnosis",
                "No national lung cancer screening program", "“It happens to smokers”", "“Diagnosis” sounds like a “verdict”",
                "People act when someone they trust tells them to", "Family pays · pushes · receives the result"]
    for i, f in enumerate(findings):
        cx, cy = 4.25 + (i % 2) * 2.2, 3.45 + (i // 2) * 0.66
        c = box(s, cx, cy, 2.1, 0.58, fill=PAPER, line=MAROON, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.2, lw=1.25)
        text(s, 0, 0, 0, 0, f, size=11.5, color=DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=c,
             italic=f.startswith("“"))

    # culture map, family at the centre
    text(s, 8.85, 3.08, 4.1, 0.35, "CULTURE MAP · SIMPLIFIED", size=16, font=TITLE, bold=False, color=MAROON)
    cx, cy = 10.9, 4.55
    for (dx, dy, lab, ic) in [(-1.45, -0.75, "Cost", "wallet"), (1.45, -0.75, "Motivation", "megaphone"), (0, 1.0, "Result delivery", "heart-handshake")]:
        line(s, cx, cy, cx + dx, cy + dy, MAROON, 2)
    for (dx, lab) in [(-1.6, "Beliefs"), (1.6, "Routines")]:
        c = box(s, cx + dx - 0.5, cy + 0.2, 1.0, 0.36, fill=CREAM2, line=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, lw=0.75)
        text(s, 0, 0, 0, 0, lab, size=10.5, color=NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=c)
    fam = box(s, cx - 0.55, cy - 0.55, 1.1, 1.1, fill=MAROON, shape=MSO_SHAPE.OVAL)
    icon(s, "users", "cream", cx - 0.22, cy - 0.42, 0.44)
    text(s, cx - 0.55, cy + 0.02, 1.1, 0.4, "FAMILY", size=17, font=TITLE, bold=False, color=CREAM, align=PP_ALIGN.CENTER)
    for (dx, dy, lab, ic) in [(-1.45, -0.75, "Cost", "wallet"), (1.45, -0.75, "Motivation", "megaphone"), (0, 1.0, "Result delivery", "heart-handshake")]:
        w = 1.55 if lab == "Result delivery" else 1.25
        c = box(s, cx + dx - w / 2, cy + dy - 0.21, w, 0.42, fill=DEEP, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
        icon(s, ic, "amber", cx + dx - w / 2 + 0.08, cy + dy - 0.15, 0.3)
        text(s, cx + dx - w / 2 + 0.36, cy + dy - 0.21, w - 0.4, 0.42, lab, size=11.5, color=CREAM, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 8.85, 5.85, 4.1, 0.3, "Diagnosis culture: shared beliefs, expectations and routines", size=9, color=NAVY, bold=False,
         align=PP_ALIGN.CENTER)

    # quote cards
    quotes = [("“I feel sick, but I’ll go tomorrow because I have to work; otherwise, what will my family eat?”",
               "Jorge Jiménez Vargas · Nurse, HGZ No. 20"),
              ("“A strategy as such? No… it is almost always a finding rather than an early detection.”",
               "Dr. Gilberto Pérez Luna · Epidemiology, ISSSTE"),
              ("“Now everyone is prone.”", "Focus group 3 · working adults, Puebla")]
    for i, (q, who) in enumerate(quotes):
        x = 4.25 + i * 2.93
        box(s, x, 6.2, 2.83, 1.05, fill=DEEP, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
        box(s, x, 6.2, 0.08, 1.05, fill=AMBER)
        text(s, x + 0.15, 6.24, 2.62, 1.0, [[(q, {"italic": True})], [(who, {"size": 8.5, "color": AMBER})]],
             size=10.5 if len(q) > 60 else 14, color=CREAM, anchor=MSO_ANCHOR.MIDDLE)
    notes(s, "Findings and quotes come from the NEUMA Human Practices interviews (HGZ No. 20 and ISSSTE Puebla) and the three focus groups. "
             "3 to 8 months: Internal Medicine, ISSSTE (Dr. Ana Cabrera). No national screening program: Pulmonology HGZ No. 20 (Int. 17), "
             "Epidemiology ISSSTE. Named quotes are from stakeholders who allowed the use of their names. Quotes translated from Spanish.")


def slide3(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    background(s, DEEP)
    header(s, True)
    text(s, 0.5, 0.5, 6, 0.85, "HP REACHED THE BENCH", size=46, font=TITLE, bold=False, color=CREAM)
    text(s, 6.4, 0.72, 5.5, 0.5, "Every requirement has a name", size=22, color=AMBER, italic=True)

    # timeline
    line(s, 0.6, 1.85, 12.75, 1.85, CREAM2, 2)
    for x, when, what, before, after in [(0.6, "INAOE  ·  JUNE–JULY 2026", "Immobilization redesigned", "Cys–S–Au", "Biotin–SA"),
                                         (6.75, "UNAM  ·  SEPTEMBER 2026", "Expression redesigned", "1 vector", "2 vectors")]:
        box(s, x + 0.0, 1.73, 0.24, 0.24, fill=AMBER, shape=MSO_SHAPE.OVAL)
        text(s, x + 0.35, 1.45, 3.4, 0.36, when, size=20, font=TITLE, bold=False, color=AMBER)
        text(s, x + 0.35, 1.95, 3.0, 0.4, what, size=14, color=CREAM)
        for j, (lab, fill) in enumerate([(before, NAVY2), (after, TEAL)]):
            c = box(s, x + 3.45 + j * 1.35, 1.95, 1.05, 0.38, fill=fill, line=CREAM2 if j == 0 else None,
                    shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5, lw=0.75)
            text(s, 0, 0, 0, 0, lab, size=11, color=CREAM, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, shape=c)
        arrow(s, x + 4.55, 2.03, 0.22, 0.22, AMBER)

    # figures
    for x, img, cap in [(0.5, "chip.png", [[("INAOE  ", {"color": MAROON}), ("Cysteine anchoring on gold → AviTag-biotin and streptavidin  ·  validated streptavidin SPR chips", {})]]),
                        (6.75, "plasmids.png", [[("UNAM  ", {"color": MAROON}), ("Bicistronic dCas9-AviTag/BirA → two separate vectors  ·  in vitro biotinylation", {})]])]:
        box(s, x, 2.55, 6.08, 2.95, fill=CREAM, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
        pic(s, A / img, x + 0.39, 2.6, 5.3, 2.41)
        text(s, x + 0.1, 5.03, 5.9, 0.42, cap, size=10, color=DEEP, align=PP_ALIGN.CENTER)

    # Table A, simplified, with the stakeholder behind each requirement
    text(s, 0.5, 5.58, 8, 0.32, "HP IN LAB  ·  REQUIREMENT → TECHNIQUE → WHO RAISED IT", size=16, font=TITLE, bold=False, color=AMBER)
    rows = [("Requirement", "Lab technique", "Raised by"),
            ("Reliable", "Three controls · several gRNAs screened", "Dr. Irma Cruz Solís (controls) · biosensor workshop experts (gRNAs)"),
            ("Specific", "dCas9 recognition checked per target", "Biosensor workshop experts"),
            ("Reproducible", "Standardized expression and purification", "Biosensor workshop experts · Dr. Armando Hernández García, UNAM"),
            ("Affordable", "Simpler, cheaper SPR chip", "Workshop experts (6 of 8) · nursing and internal medicine, HGZ No. 20"),
            ("Low burden", "Single blood sample · ctDNA liquid biopsy", "Dr. Gilberto Pérez Luna, ISSSTE · focus group 2")]
    tbl = s.shapes.add_table(len(rows), 3, Inches(0.5), Inches(5.9), Inches(12.33), Inches(1.4)).table
    for j, w in enumerate((1.7, 4.2, 6.43)):
        tbl.columns[j].width = Inches(w)
    for i, row in enumerate(rows):
        tbl.rows[i].height = Inches(0.233)
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(MAROON if i == 0 else (NAVY if i % 2 else NAVY2))
            cell.margin_top = cell.margin_bottom = Inches(0.02)
            cell.margin_left = Inches(0.08)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.text = ""
            r = tf.paragraphs[0].add_run(); r.text = val
            f = r.font; f.name = BODY; f.size = Pt(10); f.bold = True
            f.color.rgb = rgb(CREAM if i == 0 else (AMBER if j == 0 else (CREAM if j == 1 else CREAM2)))
    # drop the default table style banding so our fills show
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0"); tblPr.set("bandRow", "0")
    notes(s, "INAOE (June–July 2026): immobilization moved from cysteine anchoring on gold to AviTag-biotin on streptavidin SPR chips. "
             "UNAM, Instituto de Química (21–25 September 2026): dCas9 did not express from the bicistronic dCas9-AviTag/BirA construct; "
             "Dr. Hernández García's lab advised two separate vectors and in vitro biotinylation (designed and checked in silico). "
             "Stakeholders per requirement are taken from the Human Practices record (workshop form, Dr. Cruz Solís interview, "
             "clinical interviews and focus groups).")


def main():
    img = qrcode.make(WIKI_HP, border=2, box_size=12)
    img = img.convert("RGB")
    px = img.load()
    for yy in range(img.height):
        for xx in range(img.width):
            px[xx, yy] = (0, 26, 59) if px[xx, yy][0] < 128 else (242, 238, 216)
    img.save(A / "qr_hp.png")

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    slide1(prs); slide2(prs); slide3(prs)
    out = HERE / "NEUMA_HP.pptx"
    prs.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
