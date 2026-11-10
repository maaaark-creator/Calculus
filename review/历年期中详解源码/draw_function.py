"""Generate the vector sketch for 2024 Q14; requires reportlab."""
from pathlib import Path
from math import exp, sqrt
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white

ROOT = Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont("CN", "C:/Windows/Fonts/msyh.ttc", subfontIndex=0))
c = canvas.Canvas(str(ROOT / "function-24-q14.pdf"), pagesize=(500, 415))
c.setTitle("2024 Q14 function sketch")
INK, CURVE, GRID = map(HexColor, ("#173F5F", "#227C83", "#dce5e9"))


def panel(box, limits, title, xticks, yticks, detail=False):
    left, bottom, width, height = box
    xmin, xmax, ymin, ymax = limits

    def pt(x, y):
        return (left + (x - xmin) / (xmax - xmin) * width,
                bottom + (y - ymin) / (ymax - ymin) * height)

    def line(x1, y1, x2, y2):
        c.line(*pt(x1, y1), *pt(x2, y2))

    c.setFont("CN", 10)
    c.setFillColor(INK)
    c.drawString(left, bottom + height + 15, title)
    c.setLineWidth(.35)
    for x in xticks:
        c.setStrokeColor(GRID)
        line(x, ymin, x, ymax)
        c.setFillColor(INK)
        c.setFont("Helvetica", 8)
        c.drawCentredString(pt(x, 0)[0], bottom - 12, str(x))
    for y in yticks:
        c.setStrokeColor(GRID)
        line(xmin, y, xmax, y)
        c.setFillColor(INK)
        c.drawRightString(left - 7, pt(0, y)[1] - 3, str(y))
    c.setStrokeColor(INK)
    c.setLineWidth(.6)
    c.rect(left, bottom, width, height)
    line(xmin, 0, xmax, 0)
    line(0, ymin, 0, ymax)
    c.setFont("Helvetica", 9)
    c.drawString(left + width + 7, pt(0, 0)[1] - 3, "x")

    c.saveState()
    clip = c.beginPath()
    clip.rect(left, bottom, width, height)
    c.clipPath(clip, stroke=0)
    if not detail:
        c.setDash(4, 3)
        c.setStrokeColor(HexColor("#8b9097"))
        line(xmin, xmin + 3, xmax, xmax + 3)
        line(0, ymin, 0, ymax)
        c.setDash()
    c.setStrokeColor(CURVE)
    c.setLineWidth(1.6)
    for a, b in ((xmin, -.005), (.065, xmax)):
        if b <= a:
            continue
        path = c.beginPath()
        started = False
        for i in range(2401):
            x = a + (b - a) * i / 2400
            y = (x + 2) * exp(1 / x)
            if y < ymin - 2 or y > ymax + 2:
                started = False
                continue
            if not started:
                path.moveTo(*pt(x, y))
                started = True
            else:
                path.lineTo(*pt(x, y))
        c.drawPath(path)
    c.restoreState()

    def dot(x, y, label, dx, dy):
        c.setFillColor(CURVE)
        c.circle(*pt(x, y), 2.5, fill=1, stroke=0)
        c.setFont("Helvetica", 8)
        c.setFillColor(INK)
        c.drawString(pt(x, y)[0] + dx, pt(x, y)[1] + dy, label)

    if detail:
        dot(-2, 0, "(-2, 0)", -37, -17)
        dot(-1, 1/exp(1), "(-1, 1/e)", -40, 10)
        dot(-.4, 1.6*exp(-2.5), "(-2/5, 8/(5e^(5/2)))", -116, -14)
        c.setFillColor(white)
        c.setStrokeColor(CURVE)
        c.circle(*pt(0, 0), 3, fill=1, stroke=1)
    else:
        dot(2, 4*sqrt(exp(1)), "(2, 4 sqrt(e))", 8, -17)
        c.setFillColor(INK)
        c.setFont("Helvetica", 9)
        c.drawString(*pt(4.5, 9), "y = x + 3")


panel((48, 245, 425, 140), (-7, 7, -5, 14),
      "整体：两支曲线与渐近线", [-6, -4, -2, 0, 2, 4, 6], [-4, 0, 4, 8, 12])
panel((48, 45, 425, 140), (-2.6, .15, -.35, .55),
      "负半轴放大：零点、极大值点与拐点", [-2.5, -2, -1.5, -1, -.5, 0], [-.2, 0, .2, .4], True)
c.save()
print(ROOT / "function-24-q14.pdf")
