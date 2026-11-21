#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There — Republika Farlane.

Deterministic PIL render of an open passport spread (1024x1024 PNG).
Invented lighthouse-and-ferry archipelago republic. No network, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"

# ---------- fonts ----------
FONT_DIRS = ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/dejavu"]

def font(names, size):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

SERIF_B = lambda s: font(["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"], s)
SERIF   = lambda s: font(["LiberationSerif-Regular.ttf", "DejaVuSerif.ttf"], s)
SERIF_I = lambda s: font(["LiberationSerif-Italic.ttf", "DejaVuSerif.ttf"], s)
SANS_B  = lambda s: font(["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"], s)
SANS    = lambda s: font(["LiberationSans-Regular.ttf", "DejaVuSans.ttf"], s)
MONO    = lambda s: font(["LiberationMono-Regular.ttf", "DejaVuSansMono.ttf"], s)

# ---------- palette ----------
INK      = (30, 46, 78)      # deep lighthouse blue
INK_SOFT = (80, 94, 120)
PAPER    = (247, 242, 228)
PAPER_R  = (245, 240, 224)
RULE     = (150, 160, 178)
RED      = (146, 44, 48)
GREEN    = (44, 110, 84)
BLUE     = (52, 84, 150)
TEAL     = (38, 110, 108)
GREY_TXT = (96, 104, 118)

img = Image.new("RGB", (W, H), (18, 18, 20))
d = ImageDraw.Draw(img)

# pages
LX0, LX1 = 30, 502
RX0, RX1 = 522, 994
PY0, PY1 = 28, 996
d.rectangle([LX0, PY0, LX1, PY1], fill=PAPER)
d.rectangle([RX0, PY0, RX1, PY1], fill=PAPER_R)
# spine shadow
for i in range(10):
    shade = 232 - i * 6
    d.line([(502 + i, PY0), (502 + i, PY1)], fill=(shade, shade - 8, shade - 28))
    d.line([(522 - i, PY0), (522 - i, PY1)], fill=(shade, shade - 8, shade - 28))
d.rectangle([LX0, PY0, LX1, PY1], outline=(190, 184, 162), width=1)
d.rectangle([RX0, PY0, RX1, PY1], outline=(190, 184, 162), width=1)

def text(x, y, s, f, fill=INK, anchor="la", spacing=0):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor, spacing=spacing)

def tw(s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]

# ---------- left page header ----------
cx = (LX0 + LX1) // 2
# emblem: circle, lighthouse with beams over waves
ex, ey, er = cx, 86, 30
d.ellipse([ex - er, ey - er, ex + er, ey + er], outline=INK, width=2)
d.ellipse([ex - er + 4, ey - er + 4, ex + er - 4, ey + er - 4], outline=INK, width=1)
# lighthouse tower
d.polygon([(ex - 6, ey + 16), (ex - 4, ey - 6), (ex + 4, ey - 6), (ex + 6, ey + 16)], outline=INK, width=2)
d.rectangle([ex - 5, ey - 13, ex + 5, ey - 6], outline=INK, width=2)
d.line([(ex - 8, ey - 13), (ex + 8, ey - 13)], fill=INK, width=2)
d.line([(ex, ey - 18), (ex, ey - 13)], fill=INK, width=2)
# light beams
d.line([(ex - 6, ey - 10), (ex - 17, ey - 14)], fill=INK, width=1)
d.line([(ex + 6, ey - 10), (ex + 17, ey - 14)], fill=INK, width=1)
# waves
for wy in (ey + 20, ey + 25):
    pts = []
    for t in range(-14, 15, 2):
        pts.append((ex + t, wy + (2 if (t // 4) % 2 == 0 else -1)))
    d.line(pts, fill=INK, width=1)

text(cx, 128, "REPUBLIKA FARLANE", SERIF_B(25), anchor="ma")
text(cx, 160, "REPUBLIC OF FARLANE", SANS(11), fill=INK_SOFT, anchor="ma")
# letter-spaced PASAPORT
pas = "P A S A P O R T"
text(cx, 180, pas, SANS_B(13), anchor="ma")
d.line([(LX0 + 26, 208), (LX1 - 26, 208)], fill=INK, width=2)

# ---------- portrait ----------
PX0, PYp0, PX1, PYp1 = LX0 + 28, 224, LX0 + 196, 430
d.rectangle([PX0, PYp0, PX1, PYp1], fill=(203, 211, 220), outline=INK, width=2)
ncx = (PX0 + PX1) // 2
# long hair back panel (behind shoulders)
d.rectangle([ncx - 42, PYp0 + 30, ncx + 42, PYp1 - 30], fill=(58, 44, 38))
# shoulders / shirt
d.polygon([(PX0 + 18, PYp1), (PX0 + 34, PYp1 - 52), (PX0 + 62, PYp1 - 62),
           (PX1 - 62, PYp1 - 62), (PX1 - 34, PYp1 - 52), (PX1 - 18, PYp1)], fill=(36, 96, 96))
# collar
d.polygon([(PX0 + 62, PYp1 - 62), (ncx, PYp1 - 40), (PX1 - 62, PYp1 - 62),
           (ncx, PYp1 - 56)], fill=(232, 234, 236))
# neck
d.rectangle([ncx - 12, PYp0 + 118, ncx + 12, PYp0 + 148], fill=(222, 178, 146))
# face
d.ellipse([ncx - 32, PYp0 + 34, ncx + 32, PYp0 + 128], fill=(232, 190, 158))
# hair top cap + side strands (rounded ends so the hair reads as hair, not a block)
d.pieslice([ncx - 35, PYp0 + 22, ncx + 35, PYp0 + 96], start=175, end=365, fill=(58, 44, 38))
d.chord([ncx - 35, PYp0 + 22, ncx + 35, PYp0 + 96], start=175, end=365, fill=(58, 44, 38))
d.rectangle([ncx - 40, PYp0 + 52, ncx - 30, PYp0 + 122], fill=(58, 44, 38))
d.rectangle([ncx + 30, PYp0 + 52, ncx + 40, PYp0 + 122], fill=(58, 44, 38))
d.ellipse([ncx - 40, PYp0 + 112, ncx - 30, PYp0 + 132], fill=(58, 44, 38))
d.ellipse([ncx + 30, PYp0 + 112, ncx + 40, PYp0 + 132], fill=(58, 44, 38))
# centre part line
d.line([(ncx, PYp0 + 28), (ncx, PYp0 + 44)], fill=(96, 78, 66), width=2)
# ears + small earrings
d.ellipse([ncx - 37, PYp0 + 78, ncx - 30, PYp0 + 94], fill=(228, 184, 150))
d.ellipse([ncx + 30, PYp0 + 78, ncx + 37, PYp0 + 94], fill=(228, 184, 150))
d.ellipse([ncx - 36, PYp0 + 96, ncx - 32, PYp0 + 100], fill=(196, 158, 74))
d.ellipse([ncx + 32, PYp0 + 96, ncx + 36, PYp0 + 100], fill=(196, 158, 74))
# brows, eyes, nose, mouth
d.line([(ncx - 20, PYp0 + 76), (ncx - 8, PYp0 + 74)], fill=(58, 44, 38), width=3)
d.line([(ncx + 8, PYp0 + 74), (ncx + 20, PYp0 + 76)], fill=(58, 44, 38), width=3)
d.ellipse([ncx - 17, PYp0 + 82, ncx - 10, PYp0 + 88], fill=(30, 30, 34))
d.ellipse([ncx + 10, PYp0 + 82, ncx + 17, PYp0 + 88], fill=(30, 30, 34))
d.line([(ncx, PYp0 + 88), (ncx - 3, PYp0 + 104), (ncx + 4, PYp0 + 106)], fill=(190, 140, 108), width=2)
d.line([(ncx - 9, PYp0 + 116), (ncx + 9, PYp0 + 116)], fill=(160, 100, 92), width=3)
text(PX0, PYp1 + 8, "FOTOGRAFIA / PHOTOGRAPH", SANS(8), fill=GREY_TXT)

# ---------- data fields ----------
FX = LX0 + 216
fields = [
    ("TIP / TYPE", "P"),
    ("KOD / CODE", "FAR"),
    ("PASAPORT NR / PASSPORT NO.", "FAR 011207"),
    ("PREZIME / SURNAME", "TORVANE"),
    ("IME / GIVEN NAMES", "MARA ILSE"),
    ("DRZAVLJANSTVO / NATIONALITY", "FARLANIAN"),
    ("RODEN / DATE OF BIRTH", "14 MAY 1991"),
    ("MJESTO RODENJA / PLACE OF BIRTH", "PORT LANT"),
    ("SPOL / SEX", "F"),
    ("IZDANO / DATE OF ISSUE", "03 FEB 2023"),
    ("VRIJEDI DO / DATE OF EXPIRY", "03 FEB 2033"),
    ("TIJELO / AUTHORITY", "LIGHTHOUSE OFFICE, PORT LANT"),
]
fy = 224
for label, val in fields:
    text(FX, fy, label, SANS(8), fill=GREY_TXT)
    text(FX, fy + 12, val, SANS_B(14), fill=INK)
    fy += 40
    if label.startswith("TIJELO"):
        fy -= 6

# signature (nudged down after first render so it clears the authority field)
sy = 732
text(LX0 + 30, sy, "Mara Ilse Torvane", SERIF_I(24), fill=(30, 44, 92))
d.line([(LX0 + 30, sy + 34), (LX0 + 250, sy + 34)], fill=INK_SOFT, width=1)
text(LX0 + 30, sy + 40, "POTPIS / HOLDER'S SIGNATURE", SANS(8), fill=GREY_TXT)

# ---------- MRZ (ICAO 9303, weights 7-3-1) ----------
def cd(s):
    vals = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    vals["<"] = 0
    w = [7, 3, 1]
    return str(sum(vals.get(c, 0) * w[i % 3] for i, c in enumerate(s)) % 10)

line1 = ("P<FARTORVANE<<MARA<ILSE" + "<" * 44)[:44]
pno = "FAR011207"
dob, exp = "910514", "330203"
personal = "<" * 14
line2 = pno + cd(pno) + "FAR" + dob + cd(dob) + "F" + exp + cd(exp) + personal + cd(personal)
line2 += cd(line2[:10] + line2[13:20] + line2[21:43])
assert len(line1) == 44 and len(line2) == 44, (line1, line2)

MX0, MY0, MX1, MY1 = LX0 + 26, 812, LX1 - 26, 916
d.rectangle([MX0, MY0, MX1, MY1], fill=(240, 234, 216), outline=INK_SOFT, width=1)
text(MX0 + 14, MY0 + 18, line1, MONO(15), fill=(30, 34, 40))
text(MX0 + 14, MY0 + 52, line2, MONO(15), fill=(30, 34, 40))
text(LX0 + 28, 952, "2", SERIF(13), fill=GREY_TXT)

# faint watermark emblem, left page (kept clear of the data fields)
wx, wy = LX0 + 112, 560
d.ellipse([wx - 52, wy - 52, wx + 52, wy + 52], outline=(238, 232, 214), width=2)
d.polygon([(wx - 9, wy + 24), (wx - 6, wy - 8), (wx + 6, wy - 8), (wx + 9, wy + 24)], outline=(238, 232, 214), width=2)
d.rectangle([wx - 7, wy - 18, wx + 7, wy - 8], outline=(238, 232, 214), width=2)

# ---------- right page ----------
text(RX0 + 26, 52, "VIZE / VISAS", SERIF_B(24))
text(RX1 - 26, 58, "12", SERIF(13), fill=GREY_TXT, anchor="ra")
d.line([(RX0 + 26, 92), (RX1 - 26, 92)], fill=INK, width=2)
text(RX0 + 26, 102, "ENTRY AND EXIT STAMPS — TRAVEL HISTORY", SANS(9), fill=GREY_TXT)

stamps = [
    ("FARLANE", "DEPARTURE", "PORT LANT", "18 APR 2023", RED, -3, "rect"),
    ("OSTRAVIA", "ARRIVAL", "GREY QUAY", "19 APR 2023", BLUE, 2, "rect"),
    ("OSTRAVIA", "DEPARTURE", "GREY QUAY", "02 MAY 2023", BLUE, -2, "rect"),
    ("FARLANE", "ARRIVAL", "PORT LANT", "03 MAY 2023", RED, 3, "rect"),
    ("FARLANE", "DEPARTURE", "PORT LANT", "11 OCT 2023", RED, 2, "oval"),
    ("KORVIA", "ARRIVAL", "HAVEN PIER", "12 OCT 2023", TEAL, -3, "oval"),
    ("KORVIA", "DEPARTURE", "HAVEN PIER", "27 OCT 2023", TEAL, 2, "oval"),
    ("FARLANE", "ARRIVAL", "PORT LANT", "28 OCT 2023", RED, -2, "oval"),
]

def stamp(x, y, w, h, country, kind, port, date, color, angle, shape):
    s = Image.new("RGBA", (w + 8, h + 8), (0, 0, 0, 0))
    sd = ImageDraw.Draw(s)
    if shape == "oval":
        sd.ellipse([3, 3, w + 4, h + 4], outline=color + (255,), width=3)
        sd.ellipse([8, 8, w - 1, h - 1], outline=color + (255,), width=1)
    else:
        sd.rounded_rectangle([3, 3, w + 4, h + 4], radius=10, outline=color + (255,), width=3)
        sd.rounded_rectangle([8, 8, w - 1, h - 1], radius=7, outline=color + (255,), width=1)
    f1, f2, f3 = SANS_B(14), SANS(9), SANS_B(12)
    cxx = (w + 8) // 2
    sd.text((cxx, 16), country, font=f1, fill=color + (255,), anchor="ma")
    sd.text((cxx, 36), kind, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 49), port, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 64), date, font=f3, fill=color + (255,), anchor="ma")
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(s, (x, y), s)

SW, SH = 196, 92
pos = [(RX0 + 30, 132), (RX0 + 244, 130), (RX0 + 30, 242), (RX0 + 244, 244),
       (RX0 + 30, 352), (RX0 + 244, 350), (RX0 + 30, 462), (RX0 + 244, 464)]
for (c, k, p, dt, col, ang, sh), (x, y) in zip(stamps, pos):
    stamp(x, y, SW, SH, c, k, p, dt, col, ang, sh)

# conditions box
BX0, BY0, BX1, BY1 = RX0 + 26, 592, RX1 - 26, 806
d.rectangle([BX0, BY0, BX1, BY0 + 32], fill=INK)
text(BX0 + 14, BY0 + 7, "CONDITIONS OF ISSUE", SANS_B(14), fill=(247, 242, 228))
d.rectangle([BX0, BY0, BX1, BY1], outline=INK, width=2)
lines = [
    "Valid only on scheduled ferries between the seven",
    "Lantern Isles. The bearer must present this passport",
    "to the lamp-keeper of the nearest lighthouse within",
    "24 hours of landing for countersignature. Not valid",
    "for private crossings after dark without a permit.",
]
ly = BY0 + 46
for ln in lines:
    text(BX0 + 14, ly, ln, SERIF(13.5), fill=(52, 58, 72))
    ly += 21
text(BX0 + 14, ly + 6, "No. 011207  ·  Fee paid at issue", SANS(9), fill=GREY_TXT)

# fee stamp (circle, overlapping box corner)
fs = Image.new("RGBA", (150, 150), (0, 0, 0, 0))
fd = ImageDraw.Draw(fs)
fd.ellipse([4, 4, 146, 146], outline=RED + (255,), width=3)
fd.ellipse([12, 12, 138, 138], outline=RED + (255,), width=1)
fd.text((75, 42), "LAMP DUES", font=SANS_B(15), fill=RED + (255,), anchor="ma")
fd.text((75, 64), "PAID", font=SANS_B(17), fill=RED + (255,), anchor="ma")
fd.text((75, 90), "3 FEB", font=SANS_B(15), fill=RED + (255,), anchor="ma")
fs = fs.rotate(-12, expand=True, resample=Image.BICUBIC)
img.paste(fs, (BX1 - 138, BY1 - 104), fs)

text(RX0 + 26, 838, "This passport remains the property of the Republic of Farlane.", SERIF_I(12), fill=GREY_TXT)
text(RX0 + 26, 858, "If found, please return to any Farlanian consulate or lighthouse station.", SERIF_I(12), fill=GREY_TXT)

os.makedirs("/output", exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}: {os.path.getsize(OUT)} bytes, {img.size}")
