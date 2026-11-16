"""Illustrations produits (style catalogue plat) — 1000px puis réduites à 600px."""
import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 1000
import os as _os
F = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "assets", "fonts") + "/"
def font(sz, w="Bold"): return ImageFont.truetype(F + f"Inter-{w}.otf", sz)

def hx(c):
    c = c.lstrip("#"); return tuple(int(c[i:i+2], 16) for i in (0, 2, 4))
def sh(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c)
def mix(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))

PAL = [hx(x) for x in ["#e63946", "#f28c28", "#f7c714", "#2a9d4b", "#2c7be5", "#8e44ad", "#ff5fa2", "#1d3557", "#14b8a6", "#8b5a2b", "#111111", "#9aa3ad"]]

class Canvas:
    def __init__(self, bg=(255, 255, 255)):
        self.im = Image.new("RGB", (S, S), bg)
        self.d = ImageDraw.Draw(self.im)
    def shadow(self, box, r=40, alpha=70):
        m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse(box, fill=alpha)
        m = m.filter(ImageFilter.GaussianBlur(r)); self.im.paste((40, 45, 60), mask=m)
    def rot(self, fn, angle, center=(500, 500)):
        layer = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
        fn(d); layer = layer.rotate(angle, center=center, resample=Image.BICUBIC)
        self.im.paste(layer, (0, 0), layer)
    def out(self, path):
        self.im.resize((600, 600), Image.LANCZOS).save(path, quality=84, optimize=True)

def rr(d, box, r, fill, outline=None, w=0):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)

# ---------- éléments réutilisables ----------
def pen_shape(d, x, y, L, c, wdt=46, clicker=True, body=(240, 244, 250)):
    rr(d, (x, y, x + wdt, y + L), wdt // 2, body, sh(body, .82), 3)
    d.polygon([(x + 4, y + L - 6), (x + wdt - 4, y + L - 6), (x + wdt / 2, y + L + 70)], fill=(225, 228, 235))
    d.polygon([(x + wdt / 2 - 6, y + L + 52), (x + wdt / 2 + 6, y + L + 52), (x + wdt / 2, y + L + 72)], fill=c)
    rr(d, (x + 8, y - 20, x + wdt - 8, y + 70), 12, c)
    if clicker: rr(d, (x + wdt - 6, y + 10, x + wdt + 6, y + 150), 6, c)
    d.line((x + wdt / 2, y + 90, x + wdt / 2, y + L - 30), fill=sh(c, 1.0), width=6)

def pencil_shape(d, x, y, L, c, w=50):
    d.rectangle((x, y, x + w, y + L), fill=c)
    d.rectangle((x + w * .33, y, x + w * .66, y + L), fill=sh(c, .88))
    d.polygon([(x, y + L), (x + w, y + L), (x + w / 2, y + L + 95)], fill=(240, 210, 160))
    d.polygon([(x + w / 2 - 10, y + L + 70), (x + w / 2 + 10, y + L + 70), (x + w / 2, y + L + 95)], fill=(40, 40, 40) if c != (40, 40, 40) else c)
    d.rectangle((x, y - 40, x + w, y), fill=(190, 190, 200)); rr(d, (x, y - 85, x + w, y - 35), 12, (240, 150, 160))

def box3d(d, x, y, w, h, depth, front, top=None, side=None):
    top = top or sh(front, 1.15); side = side or sh(front, .78)
    d.polygon([(x, y), (x + depth, y - depth * .6), (x + w + depth, y - depth * .6), (x + w, y)], fill=top)
    d.polygon([(x + w, y), (x + w + depth, y - depth * .6), (x + w + depth, y + h - depth * .6), (x + w, y + h)], fill=side)
    d.rectangle((x, y, x + w, y + h), fill=front)

def label(d, box, txt, size=44, fg=(255, 255, 255), bg=None):
    if bg: rr(d, box, 10, bg)
    f = font(size); x0, y0, x1, y1 = box
    tw = d.textlength(txt, font=f)
    while tw > (x1 - x0) - 20 and size > 16:
        size -= 2; f = font(size); tw = d.textlength(txt, font=f)
    d.text(((x0 + x1) / 2, (y0 + y1) / 2), txt, font=f, fill=fg, anchor="mm")

def wrap_title(d, txt, box, size, fg):
    words = txt.split(); lines = []; cur = ""
    while size > 22 and max(d.textlength(w, font=font(size)) for w in words) > box[2] - box[0]: size -= 2
    f = font(size)
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > box[2] - box[0]: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur); lines = lines[:5]
    y = box[1]
    for ln in lines:
        d.text((box[0], y), ln, font=f, fill=fg); y += size * 1.2

# ---------- dessins par type ----------
def draw(kind, color, name, path):
    c = hx(color); C = Canvas(); d = C.d
    if c == (255, 255, 255): c = (245, 245, 240)
    dk = sh(c, .75)
    C.shadow((220, 800, 780, 880))
    rnd = random.Random(name)

    if kind == "pen":
        C.rot(lambda d: pen_shape(d, 477, 160, 560, c), -28)
    elif kind == "gelpen":
        C.rot(lambda d: (pen_shape(d, 470, 150, 560, c, 60, body=sh(c, 1.0) if c != (34, 34, 34) else (60, 60, 66)),
                         rr(d, (470, 420, 530, 560), 20, (50, 50, 55))), -28)
    elif kind == "pen4":
        def f(d):
            rr(d, (440, 170, 560, 780), 60, c); rr(d, (440, 170, 560, 260), 30, sh(c, 1.2))
            for i, cc in enumerate([(31, 79, 191), (30, 30, 30), (214, 40, 40), (42, 157, 75)]):
                rr(d, (448 + i * 27, 90, 468 + i * 27, 210), 8, cc)
            d.polygon([(470, 780), (530, 780), (500, 860)], fill=(210, 212, 220))
        C.rot(f, -20)
    elif kind == "penbox":
        box3d(d, 230, 400, 470, 330, 90, c)
        label(d, (260, 560, 670, 640), "50 STYLOS", 48)
        for i in range(9): pen_shape(d, 270 + i * 46, 210, 190, c, 30, False)
        box3d(d, 230, 400, 470, 140, 90, sh(c, .9))
        label(d, (260, 430, 670, 510), "CRISTAL", 54)
    elif kind in ("marker", "highlighter"):
        def f(d):
            w = 120 if kind == "marker" else 140
            body = (245, 245, 245) if kind == "marker" else c
            rr(d, (500 - w / 2, 250, 500 + w / 2, 780), 30, body, sh(body, .85), 3)
            rr(d, (500 - w / 2 - 6, 150, 500 + w / 2 + 6, 380), 30, c if kind == "marker" else sh(c, .85))
            d.polygon([(500 - w / 2 + 10, 780), (500 + w / 2 - 10, 780), (500 + 20, 860), (500 - 20, 860)], fill=sh(c, .7))
            if kind == "marker": label(d, (500 - w / 2 + 10, 480, 500 + w / 2 - 10, 600), "PERM", 34, c)
        C.rot(f, -25)
    elif kind in ("markerset", "hlset", "fineliners", "felts", "brushpens", "colorpencils", "pencilbox"):
        n = {"markerset": 4, "hlset": 4, "fineliners": 10, "felts": 12, "brushpens": 12, "colorpencils": 12, "pencilbox": 12}[kind]
        cols = PAL[:n] if kind != "pencilbox" else [hx("#f7c714")] * n
        if kind == "hlset": cols = [hx(x) for x in ["#f7e017", "#7ed957", "#ff7eb6", "#ffa94d", "#9ad0ff", "#c9a7ff"]][:6 if "6" in name else 4]
        if kind == "markerset": cols = [hx(x) for x in ["#1f4fbf", "#111111", "#d62828", "#2a9d4b"]]
        n = len(cols); W = 560; x0 = 500 - W / 2; step = W / n
        box3d(d, x0 - 20, 560, W + 40, 220, 60, c if kind not in ("pencilbox",) else hx("#1d3557"))
        for i, cc in enumerate(cols):
            x = x0 + i * step + step * .15; w = step * .7
            if kind in ("colorpencils", "pencilbox"):
                d.rectangle((x, 300 + (i % 2) * 20, x + w, 600), fill=cc)
                d.polygon([(x, 300 + (i % 2) * 20), (x + w, 300 + (i % 2) * 20), (x + w / 2, 230 + (i % 2) * 20)], fill=(240, 210, 160))
                d.polygon([(x + w * .3, 255 + (i % 2) * 20), (x + w * .7, 255 + (i % 2) * 20), (x + w / 2, 230 + (i % 2) * 20)], fill=cc if kind != "pencilbox" else (40, 40, 40))
            else:
                rr(d, (x, 260 + (i % 2) * 18, x + w, 600), int(w / 2.5), (245, 245, 245) if kind in ("markerset", "felts", "fineliners", "brushpens") else cc, (210, 210, 210), 2)
                rr(d, (x - 2, 230 + (i % 2) * 18, x + w + 2, 360 + (i % 2) * 18), int(w / 2.5), cc)
        box3d(d, x0 - 20, 600, W + 40, 180, 60, c if kind != "pencilbox" else hx("#1d3557"))
        label(d, (x0, 630, x0 + W, 740), {"markerset": "TABLEAU BLANC", "hlset": "SURLIGNEURS", "fineliners": "FEUTRES FINS", "felts": "FEUTRES", "brushpens": "BRUSH PENS", "colorpencils": "COULEURS", "pencilbox": "HB × 12"}[kind], 52)
    elif kind == "pencil":
        C.rot(lambda d: pencil_shape(d, 475, 200, 470, c, 56), -28)
    elif kind == "mechpencil":
        C.rot(lambda d: (rr(d, (470, 170, 530, 760), 26, c), rr(d, (466, 430, 534, 600), 20, (90, 90, 100)),
                         d.polygon([(476, 760), (524, 760), (500, 840)], fill=(190, 190, 200)), rr(d, (488, 120, 512, 180), 6, (200, 200, 210))), -28)
    elif kind == "leads":
        rr(d, (330, 300, 670, 720), 30, c); rr(d, (360, 330, 640, 420), 14, (230, 230, 235))
        label(d, (360, 330, 640, 420), "HB 0,5", 54, (30, 30, 30))
        for i in range(8): d.line((390 + i * 30, 460, 390 + i * 30, 690), fill=(30, 30, 30), width=8)
    elif kind == "eraser":
        box3d(d, 300, 420, 400, 250, 120, (250, 250, 250))
        d.rectangle((300, 420, 540, 670), fill=c); label(d, (300, 480, 540, 610), "GOMME", 50)
    elif kind == "sharpener":
        box3d(d, 330, 420, 340, 300, 110, c)
        for x in (420, 560): d.ellipse((x - 50, 470, x + 50, 570), fill=sh(c, .55)); d.ellipse((x - 26, 494, x + 26, 546), fill=(30, 30, 30))
        d.rectangle((330, 610, 670, 720), fill=mix(c, (255, 255, 255), .5))
    elif kind == "tape_corr":
        rr(d, (300, 330, 720, 680), 170, c); d.ellipse((420, 420, 600, 600), fill=(255, 255, 255)); d.ellipse((470, 470, 550, 550), fill=sh(c, .8))
        rr(d, (640, 610, 790, 660), 18, (240, 240, 240)); label(d, (330, 610, 560, 670), "5 mm", 34)
    elif kind == "bottle":
        rr(d, (380, 380, 620, 760), 50, (250, 250, 250), (200, 200, 205), 4); rr(d, (430, 260, 570, 400), 20, (230, 57, 70))
        label(d, (395, 520, 605, 640), "CORRECT", 40, (230, 57, 70))
    elif kind == "corrpen":
        C.rot(lambda d: (rr(d, (455, 200, 545, 760), 40, (250, 250, 250), (200, 200, 205), 4), rr(d, (455, 160, 545, 300), 30, hx("#e63946")),
                         d.polygon([(470, 760), (530, 760), (500, 840)], fill=(180, 180, 190))), -25)
    elif kind == "refill":
        for i in range(3): rr(d, (380 + i * 90, 220, 410 + i * 90, 760), 14, (235, 238, 245), (200, 200, 205), 3); d.rectangle((388 + i * 90, 300, 402 + i * 90, 700), fill=c)
    elif kind in ("notebook", "spiral", "sketch", "sketchbook"):
        def f(d):
            x0, y0, x1, y1 = 290, 170, 710, 790
            for k in range(3): rr(d, (x0 + 10 + k * 4, y0 + 10 + k * 4, x1 + 10 + k * 4, y1 + 10 + k * 4), 14, (235, 235, 230))
            cover = c if kind not in ("sketch",) else (250, 250, 248)
            rr(d, (x0, y0, x1, y1), 14, cover, sh(cover, .85), 3)
            if kind in ("spiral", "sketchbook"):
                for yy in range(y0 + 30, y1 - 20, 38): d.ellipse((x0 - 22, yy, x0 + 12, yy + 22), outline=(120, 120, 130), width=6)
            else:
                d.rectangle((x0, y0, x0 + 34, y1), fill=sh(cover, .85))
            rr(d, (x0 + 80, y0 + 110, x1 - 60, y0 + 260), 12, (255, 255, 255) if kind != "sketch" else hx("#1d3557"))
            for k in range(3): d.line((x0 + 100, y0 + 150 + k * 35, x1 - 80, y0 + 150 + k * 35), fill=(200, 210, 230) if kind != "sketch" else (255, 255, 255), width=4)
            tag = "DESSIN" if kind in ("sketch", "sketchbook") else ("SPIRALE" if kind == "spiral" else "CAHIER")
            m = [s for s in name.split() if s.isdigit()]
            label(d, (x0 + 60, y1 - 230, x1 - 40, y1 - 130), tag, 60, (255, 255, 255) if kind != "sketch" else hx("#1d3557"))
            if m: label(d, (x0 + 60, y1 - 130, x1 - 40, y1 - 60), m[0] + " PAGES" if "pages" in name else m[0], 40, (255, 255, 255) if kind != "sketch" else (90, 90, 90))
        C.rot(f, -4)
    elif kind in ("ream", "reambox"):
        if kind == "reambox":
            box3d(d, 230, 350, 520, 400, 120, (214, 190, 150)); label(d, (260, 450, 720, 560), "5 × A4 80 g", 58, (60, 45, 30))
        else:
            box3d(d, 250, 400, 500, 300, 150, (250, 250, 252), (255, 255, 255), (225, 228, 235))
            d.rectangle((250, 400, 750, 700), fill=c); d.rectangle((250, 400, 750, 460), fill=(255, 255, 255))
            label(d, (270, 480, 730, 590), "A4 · 80 g", 72); label(d, (270, 600, 730, 670), "500 FEUILLES", 40)
    elif kind == "colorpaper":
        cols = [hx(x) for x in ["#ffd6a5", "#caffbf", "#9bf6ff", "#bdb2ff", "#ffadad"]]
        for i, cc in enumerate(cols): rr(d, (260 + i * 30, 230 + i * 50, 640 + i * 30, 690 + i * 50), 6, cc, sh(cc, .9), 2)
    elif kind == "envelope":
        rr(d, (230, 330, 770, 690), 10, c, sh(c, .85), 3)
        d.polygon([(230, 330), (770, 330), (500, 540)], fill=sh(c, .93), outline=sh(c, .8))
        d.line((230, 690, 450, 520), fill=sh(c, .85), width=3); d.line((770, 690, 550, 520), fill=sh(c, .85), width=3)
    elif kind == "labels":
        rr(d, (300, 180, 700, 800), 8, (255, 255, 255), (210, 210, 215), 3)
        for r in range(7):
            for k in range(2): rr(d, (330 + k * 180, 210 + r * 82, 490 + k * 180, 275 + r * 82), 10, (235, 240, 248), (200, 205, 215), 2)
    elif kind in ("postit", "postitset", "flags"):
        if kind == "flags":
            for i, cc in enumerate([hx(x) for x in ["#ff5fa2", "#f7e017", "#7ed957", "#2c7be5", "#ffa94d"]]):
                rr(d, (300, 260 + i * 95, 520, 330 + i * 95), 8, (240, 245, 250)); rr(d, (500, 260 + i * 95, 700, 330 + i * 95), 8, cc)
        else:
            cols = [c] if kind == "postit" else [hx(x) for x in ["#ff5fa2", "#f7e017", "#7ed957", "#ffa94d", "#9ad0ff", "#c9a7ff"]]
            for i, cc in enumerate(cols[::-1]):
                off = i * 26 if kind == "postitset" else 0
                for k in range(6): d.rectangle((300 + off, 330 + off - k * 8, 680 + off, 710 + off - k * 8), fill=sh(cc, 1 - k * .02))
                d.polygon([(560 + off, 710 + off - 40), (680 + off, 710 + off - 40), (680 + off, 590 + off - 40)], fill=sh(cc, .85))
    elif kind in ("binder",):
        def f(d):
            d.polygon([(300, 170), (690, 140), (690, 800), (300, 830)], fill=c)
            d.polygon([(300, 170), (380, 164), (380, 826), (300, 830)], fill=sh(c, .75))
            rr(d, (430, 260, 620, 460), 10, (255, 255, 255)); d.line((450, 330, 600, 330), fill=(200, 200, 210), width=5); d.line((450, 380, 580, 380), fill=(200, 200, 210), width=5)
            d.ellipse((318, 640, 366, 688), fill=(30, 30, 30)); d.ellipse((330, 652, 354, 676), fill=sh(c, .75))
        C.rot(f, 0)
    elif kind == "dividers":
        cols = PAL[:6]
        for i, cc in enumerate(cols):
            rr(d, (280 + i * 12, 230 + i * 12, 640 + i * 12, 770 + i * 12), 8, (250, 250, 250), (220, 220, 225), 2)
            rr(d, (640 + i * 12, 250 + i * 80, 700 + i * 12, 320 + i * 80), 10, cc)
    elif kind in ("folder", "folders"):
        cols = [c] if kind == "folder" else [hx(x) for x in ["#e63946", "#f7c714", "#2a9d4b", "#2c7be5", "#f28c28"]]
        for i, cc in enumerate(cols[::-1]):
            o = i * 28
            rr(d, (250 + o, 260 + o, 700 + o, 740 + o), 12, cc, sh(cc, .85), 3); rr(d, (250 + o, 230 + o, 420 + o, 290 + o), 10, cc)
        if kind == "folder": d.line((250, 600, 700, 600), fill=(30, 30, 30), width=10)
    elif kind == "sleeves":
        for i in range(4): rr(d, (300 + i * 18, 200 + i * 18, 660 + i * 18, 760 + i * 18), 6, (225, 236, 248), (170, 190, 215), 3)
        for k in range(11): d.ellipse((318, 260 + k * 45, 334, 276 + k * 45), fill=(255, 255, 255), outline=(170, 190, 215), width=2)
    elif kind == "displaybook":
        rr(d, (290, 190, 710, 790), 14, c); rr(d, (360, 280, 650, 700), 8, (230, 236, 245)); label(d, (360, 420, 650, 560), "40 VUES", 54, c)
    elif kind == "archive":
        box3d(d, 330, 260, 300, 520, 150, c)
        rr(d, (380, 330, 580, 420), 10, (255, 255, 255)); d.ellipse((440, 640, 520, 720), fill=sh(c, .6))
        label(d, (380, 330, 580, 420), "ARCHIVES", 34, (60, 60, 60))
    elif kind == "accordion":
        for i in range(10): d.polygon([(260 + i * 4, 380 + i * 30), (740 - i * 4, 380 + i * 30), (740 - i * 4, 400 + i * 30), (260 + i * 4, 400 + i * 30)], fill=sh(c, 1 - (i % 2) * .15))
        rr(d, (250, 330, 750, 720), 20, c, None); d.rectangle((250, 330, 750, 450), fill=sh(c, .85)); rr(d, (460, 420, 540, 480), 8, (230, 230, 230))
    elif kind == "parapheur":
        rr(d, (260, 240, 740, 760), 16, c); d.rectangle((260, 240, 300, 760), fill=sh(c, .7)); label(d, (330, 450, 700, 560), "PARAPHEUR", 56, (240, 220, 200))
    elif kind in ("bag", "lunchbag"):
        if kind == "lunchbag":
            rr(d, (300, 350, 700, 760), 50, c); rr(d, (300, 350, 700, 470), 50, sh(c, .85)); d.arc((400, 250, 600, 420), 180, 360, fill=sh(c, .7), width=24)
            rr(d, (420, 560, 580, 640), 14, (255, 255, 255))
        else:
            rr(d, (290, 220, 710, 780), 90, c); rr(d, (340, 480, 660, 740), 50, sh(c, .82)); d.arc((390, 120, 610, 320), 180, 360, fill=sh(c, .6), width=26)
            d.line((340, 560, 660, 560), fill=sh(c, .6), width=6); rr(d, (470, 590, 530, 620), 8, (230, 230, 230))
    elif kind == "trolley":
        d.line((330, 120, 330, 640), fill=(140, 145, 155), width=20); d.line((670, 120, 670, 640), fill=(140, 145, 155), width=20); rr(d, (320, 100, 680, 140), 14, (90, 95, 105))
        rr(d, (280, 260, 720, 760), 80, c); rr(d, (330, 480, 670, 730), 50, sh(c, .82))
        for x in (330, 670): d.ellipse((x - 45, 740, x + 45, 830), fill=(40, 40, 45))
    elif kind in ("pouch", "pouchfull"):
        if kind == "pouchfull":
            for i, cc in enumerate(PAL[:7]): rr(d, (330 + i * 50, 200 + (i % 3) * 20, 362 + i * 50, 520), 12, cc)
        rr(d, (200, 400, 800, 680), 130, c); d.line((260, 450, 740, 450), fill=(250, 250, 250), width=8); rr(d, (720, 430, 780, 480), 12, (220, 220, 220))
        if "double" in name.lower(): d.line((260, 540, 740, 540), fill=(250, 250, 250), width=8)
    elif kind in ("ruler", "setsquare", "protractor", "geoset"):
        clear = (210, 230, 250)
        def ruler(d, x, y, L, h, ang):
            def f(dd):
                rr(dd, (x, y, x + L, y + h), 10, clear, (120, 160, 210), 4)
                for k in range(0, L - 20, 22): dd.line((x + 10 + k, y, x + 10 + k, y + (40 if k % 110 == 0 else 22)), fill=(60, 90, 140), width=3)
            C.rot(f, ang)
        if kind in ("ruler", "geoset"): ruler(d, 180, 460, 640, 110, 25 if kind == "ruler" else 0)
        if kind in ("setsquare", "geoset"):
            col = c if kind == "setsquare" else (210, 230, 250)
            d.polygon([(300, 760), (700, 760), (300, 260)] if kind == "setsquare" else [(560, 420), (780, 420), (560, 140)], fill=mix(col, (255, 255, 255), .3), outline=sh(col, .7))
            d.polygon([(370, 700), (560, 700), (370, 460)] if kind == "setsquare" else [(595, 390), (710, 390), (595, 245)], fill=(255, 255, 255), outline=sh(col, .7))
        if kind in ("protractor", "geoset"):
            box = (260, 380, 740, 860) if kind == "protractor" else (230, 590, 530, 890)
            d.pieslice(box, 180, 360, fill=(210, 230, 250), outline=(120, 160, 210), width=4)
            cx, cy, r = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2, (box[2] - box[0]) / 2
            for a in range(0, 181, 10):
                t = math.radians(180 + a); d.line((cx + r * math.cos(t), cy + r * math.sin(t), cx + (r - 30) * math.cos(t), cy + (r - 30) * math.sin(t)), fill=(60, 90, 140), width=3)
        if kind == "geoset": d.rectangle((560, 600, 820, 700), fill=(210, 230, 250), outline=(120, 160, 210), width=4)
    elif kind == "compass":
        d.line((500, 230, 360, 790), fill=(170, 175, 185), width=26); d.line((500, 230, 640, 790), fill=(170, 175, 185), width=26)
        rr(d, (460, 150, 540, 280), 20, c); d.polygon([(625, 760), (660, 760), (645, 840)], fill=(240, 210, 160)); d.line((360, 790, 352, 850), fill=(80, 80, 90), width=8)
        d.line((420, 540, 580, 540), fill=(140, 145, 155), width=12)
    elif kind == "gluestick":
        rr(d, (410, 260, 590, 780), 50, c); rr(d, (400, 200, 600, 360), 50, sh(c, .8)); rr(d, (420, 740, 580, 800), 20, sh(c, .7))
        label(d, (420, 470, 580, 600), "COLLE", 42, (30, 30, 30))
    elif kind == "scissors":
        def f(d):
            d.polygon([(490, 180), (520, 180), (560, 560), (530, 560)], fill=(200, 205, 215)); d.polygon([(510, 180), (540, 180), (470, 560), (440, 560)], fill=(185, 190, 200))
            d.ellipse((330, 540, 500, 760), outline=c, width=40); d.ellipse((500, 540, 670, 760), outline=c, width=40)
        C.rot(f, 0)
    elif kind == "covers":
        for i, cc in enumerate([hx(x) for x in ["#e63946", "#2c7be5", "#2a9d4b", "#f7c714", "#8e44ad"]]):
            rr(d, (260 + i * 30, 240 + i * 30, 640 + i * 30, 720 + i * 30), 10, mix(cc, (255, 255, 255), .25), sh(cc, .8), 3)
    elif kind == "slate":
        rr(d, (220, 260, 780, 740), 24, (200, 160, 110) if c == (27, 31, 42) else (40, 70, 120)); rr(d, (260, 300, 740, 700), 10, c)
        if c != (27, 31, 42):
            for k in range(6): d.line((280, 340 + k * 60, 720, 340 + k * 60), fill=(200, 210, 230), width=3)
    elif kind == "chalk":
        box3d(d, 300, 470, 400, 260, 100, hx("#1d3557")); label(d, (320, 540, 680, 660), "CRAIES", 60)
        for i in range(6): rr(d, (330 + i * 55, 330, 370 + i * 55, 480), 14, (250, 250, 248))
    elif kind in ("calc", "calc_sci", "calc_print"):
        if kind == "calc_print":
            rr(d, (250, 330, 750, 790), 30, c); rr(d, (420, 150, 580, 350), 6, (255, 255, 255), (210, 210, 210), 2); rr(d, (300, 380, 700, 460), 12, (190, 205, 185))
            rows, top = 4, 500
        else:
            w = 360 if kind == "calc_sci" else 420
            rr(d, (500 - w / 2, 170, 500 + w / 2, 830), 40, c); rr(d, (500 - w / 2 + 40, 220, 500 + w / 2 - 40, 340), 14, (190, 205, 185))
            label(d, (500 - w / 2 + 40, 220, 500 + w / 2 - 40, 340), "123456" if kind == "calc" else "fx 3,14", 54, (40, 50, 40))
            rows, top = (6 if kind == "calc_sci" else 5), 380
        x0 = 300 if kind == "calc_print" else 500 - (180 if kind == "calc_sci" else 210) + 40
        x1 = 700 if kind == "calc_print" else 1000 - x0
        cols = 5 if kind != "calc" else 4
        bw = (x1 - x0) / cols
        for r in range(rows):
            for k in range(cols):
                cc = (245, 140, 40) if (kind == "calc" and k == cols - 1) else (235, 237, 242) if r > 1 or kind == "calc" else (90, 95, 110)
                rr(d, (x0 + k * bw + 6, top + r * 70, x0 + (k + 1) * bw - 6, top + r * 70 + 52), 10, cc)
    elif kind in ("stapler",):
        rr(d, (220, 560, 780, 680), 30, sh(c, .7)); d.polygon([(230, 560), (760, 470), (790, 520), (250, 600)], fill=c)
        rr(d, (240, 500, 780, 570), 28, c); rr(d, (280, 510, 480, 540), 10, (180, 185, 195))
    elif kind == "staples":
        box3d(d, 300, 450, 400, 220, 100, (230, 232, 238)); label(d, (320, 500, 680, 620), "24/6 × 1000", 54, (40, 40, 50))
    elif kind == "punch":
        rr(d, (230, 600, 770, 700), 20, sh(c, .8)); rr(d, (300, 440, 700, 620), 40, c); rr(d, (260, 380, 740, 460), 30, (90, 95, 110))
        for x in (380, 620): d.ellipse((x - 26, 610, x + 26, 650), fill=(200, 200, 200))
    elif kind == "remover":
        rr(d, (330, 420, 670, 600), 60, c); d.polygon([(420, 420), (580, 420), (560, 330), (440, 330)], fill=(190, 195, 205))
    elif kind in ("clips", "binderclip", "rubberbands"):
        box3d(d, 310, 500, 380, 230, 100, hx("#1d3557") if kind != "rubberbands" else (210, 180, 140))
        if kind == "clips":
            for i in range(5): d.rounded_rectangle((340 + i * 60, 330, 390 + i * 60, 520), 24, outline=(150, 155, 165), width=8)
            label(d, (330, 560, 670, 680), "100 × 28 mm", 50)
        elif kind == "binderclip":
            for i in range(3):
                x = 360 + i * 110; d.polygon([(x, 470), (x + 90, 470), (x + 80, 380), (x + 10, 380)], fill=(30, 30, 30)); d.arc((x + 10, 280, x + 80, 400), 180, 360, fill=(180, 185, 195), width=8)
            label(d, (330, 560, 670, 680), "DOUBLE CLIP", 46)
        else:
            for i, cc in enumerate([hx(x) for x in ["#e63946", "#f7c714", "#2a9d4b", "#2c7be5"]]): d.ellipse((350 + i * 70, 360, 470 + i * 70, 470), outline=cc, width=10)
            label(d, (330, 560, 670, 680), "ÉLASTIQUES", 48, (60, 45, 30))
    elif kind == "tape":
        d.ellipse((290, 300, 710, 720), fill=(225, 236, 248), outline=(180, 200, 225), width=8); d.ellipse((410, 420, 590, 600), fill=(255, 255, 255), outline=(180, 200, 225), width=6)
    elif kind == "dispenser":
        rr(d, (230, 520, 770, 720), 80, c); d.ellipse((330, 330, 610, 610), fill=(225, 236, 248), outline=(180, 200, 225), width=6); d.ellipse((420, 420, 520, 520), fill=c)
        d.polygon([(640, 520), (760, 520), (740, 470)], fill=(160, 165, 175))
    elif kind == "cutter":
        C.rot(lambda d: (rr(d, (450, 250, 560, 780), 40, c), d.polygon([(470, 250), (540, 250), (505, 120)], fill=(200, 205, 215)), rr(d, (490, 420, 520, 520), 8, (40, 40, 40))), -30)
    elif kind == "drawers":
        rr(d, (250, 200, 750, 800), 14, (250, 250, 250), (220, 220, 220), 4)
        for i in range(4): rr(d, (275, 225 + i * 142, 725, 345 + i * 142), 8, c); rr(d, (450, 270 + i * 142, 550, 295 + i * 142), 10, sh(c, .7))
    elif kind == "tray":
        for i in range(2):
            y = 300 + i * 220; d.polygon([(250, y + 180), (750, y + 180), (720, y), (280, y)], fill=sh(c, 1 - i * .1)); d.polygon([(280, y), (720, y), (700, y + 40), (300, y + 40)], fill=(245, 245, 250))
    elif kind == "penholder":
        rr(d, (370, 420, 630, 780), 20, c);
        for yy in range(440, 760, 30): d.line((380, yy, 620, yy), fill=sh(c, 1.6), width=2)
        for i, cc in enumerate(PAL[:5]): d.line((400 + i * 50, 440, 380 + i * 60, 200 + (i % 2) * 40), fill=cc, width=18)
    elif kind == "organizer":
        d.polygon([(250, 360), (750, 360), (750, 780), (250, 780)], fill=c); d.polygon([(250, 360), (360, 280), (360, 700), (250, 780)], fill=sh(c, .82))
        for i, cc in enumerate(PAL[:4]): d.rectangle((420 + i * 70, 200 + i * 15, 470 + i * 70, 370), fill=cc)
        for k in range(3): d.line((400 + k * 110, 360, 400 + k * 110, 780), fill=sh(c, .7), width=8)
    elif kind == "whiteboard":
        rr(d, (180, 230, 820, 700), 10, (200, 205, 215)); d.rectangle((200, 250, 800, 680), fill=(255, 255, 255)); d.rectangle((260, 700, 740, 730), fill=(170, 175, 185))
        d.line((260, 330, 520, 330), fill=hx("#2c7be5"), width=10); d.line((260, 400, 600, 400), fill=hx("#e63946"), width=10); d.line((260, 470, 450, 470), fill=hx("#2a9d4b"), width=10)
    elif kind == "brush_board":
        rr(d, (300, 380, 700, 560), 30, c); rr(d, (290, 560, 710, 640), 14, (110, 110, 120))
    elif kind == "stamp":
        rr(d, (380, 220, 620, 470), 50, c); rr(d, (320, 470, 680, 720), 20, sh(c, 1.4)); rr(d, (340, 690, 660, 760), 8, (40, 40, 40))
        label(d, (340, 540, 660, 640), "04 NOV 2026", 38, (30, 30, 30))
    elif kind in ("colortin",):
        rr(d, (210, 300, 790, 740), 24, c); rr(d, (250, 340, 750, 700), 14, sh(c, 1.25))
        for i, cc in enumerate(PAL * 2):
            if i >= 18: break
            d.rectangle((265 + i * 26, 420, 285 + i * 26, 680), fill=cc)
        label(d, (260, 350, 740, 410), "36 COULEURS", 44)
    elif kind == "tubes":
        for i, cc in enumerate(PAL[:6]):
            x = 220 + i * 95; rr(d, (x, 380, x + 75, 760), 14, (245, 245, 245), (210, 210, 210), 2); d.rectangle((x, 520, x + 75, 640), fill=cc); rr(d, (x + 18, 320, x + 57, 385), 8, (50, 50, 50))
    elif kind == "acrylic":
        rr(d, (370, 340, 630, 780), 40, (250, 250, 250), (210, 210, 210), 3); rr(d, (400, 250, 600, 350), 20, c if sum(c) < 700 else (200, 200, 205)); d.rectangle((370, 470, 630, 650), fill=c, outline=(200, 200, 205) if sum(c) >= 700 else None, width=3)
        label(d, (370, 470, 630, 650), "100 ml", 50, (60, 60, 70) if sum(c) >= 700 else (255, 255, 255))
    elif kind == "watercolor":
        rr(d, (200, 350, 800, 700), 24, (40, 45, 55))
        for i in range(12):
            r, k = divmod(i, 6); x = 240 + k * 90; y = 400 + r * 140; rr(d, (x, y, x + 70, y + 100), 16, PAL[i % len(PAL)])
    elif kind == "brushes":
        for i in range(6):
            x = 300 + i * 70; d.rectangle((x, 300 + i * 10, x + 22, 820), fill=c); d.rectangle((x - 3, 240 + i * 10, x + 25, 300 + i * 10), fill=(190, 195, 205))
            d.polygon([(x - 3, 240 + i * 10), (x + 25, 240 + i * 10), (x + 11, 160 + i * 5)], fill=(40, 30, 20))
    elif kind == "palette":
        d.ellipse((220, 300, 780, 740), fill=(250, 250, 250), outline=(210, 210, 215), width=4); d.ellipse((560, 560, 640, 640), fill=(255, 255, 255), outline=(210, 210, 215), width=3)
        for i, cc in enumerate(PAL[:6]): ang = math.radians(200 + i * 32); d.ellipse((500 + 190 * math.cos(ang) - 40, 520 + 140 * math.sin(ang) - 30, 500 + 190 * math.cos(ang) + 40, 520 + 140 * math.sin(ang) + 30), fill=cc)
    elif kind == "cup":
        d.polygon([(330, 360), (670, 360), (630, 760), (370, 760)], fill=c); d.ellipse((330, 330, 670, 400), fill=sh(c, 1.25)); d.ellipse((380, 345, 620, 385), fill=sh(c, .7))
    elif kind == "canvas":
        n = 3 if "Lot" in name else 1
        for i in range(n):
            o = i * 60; rr(d, (260 + o, 200 + o, 640 + o, 700 + o), 4, (252, 250, 244), (215, 195, 150), 12)
    elif kind == "clay":
        for i, cc in enumerate(PAL[:10]): rr(d, (230 + (i % 5) * 110, 340 + (i // 5) * 180, 320 + (i % 5) * 110, 490 + (i // 5) * 180), 30, cc)
    elif kind == "crepe":
        for i, cc in enumerate([hx(x) for x in ["#ff5fa2", "#f7c714", "#2c7be5", "#2a9d4b", "#e63946"]]): rr(d, (240 + i * 105, 260 + (i % 2) * 40, 330 + i * 105, 760 - (i % 2) * 40), 20, cc)
    elif kind == "beads":
        rr(d, (220, 300, 780, 760), 30, (240, 240, 245))
        for i in range(40): x = 260 + (i % 8) * 65; y = 340 + (i // 8) * 80; d.ellipse((x, y, x + 46, y + 46), fill=PAL[i % len(PAL)])
    elif kind == "usb":
        C.rot(lambda d: (rr(d, (420, 300, 580, 760), 36, c), rr(d, (445, 180, 555, 310), 6, (200, 205, 215)), d.rectangle((465, 210, 490, 240), fill=(90, 90, 100)), d.rectangle((510, 210, 535, 240), fill=(90, 90, 100)),
                         label(d, (420, 480, 580, 600), (__import__("re").search(r"(\d+)\s*Go", name) or __import__("re").search(r"(\d+)", name)).group(1) + " Go", 40)), -20)
    elif kind == "hdd":
        rr(d, (300, 220, 700, 780), 40, c); d.ellipse((440, 650, 460, 670), fill=(80, 220, 120)); label(d, (300, 400, 700, 520), "1 To", 80)
    elif kind in ("mouse",):
        d.ellipse((370, 220, 630, 780), fill=c); d.line((500, 220, 500, 450), fill=(80, 80, 90), width=6); rr(d, (488, 290, 512, 370), 10, (110, 110, 120))
    elif kind in ("keyboard", "kbmouse"):
        x1 = 760 if kind == "keyboard" else 650
        rr(d, (140, 380, x1, 640), 24, c)
        for r in range(4):
            for k in range(int((x1 - 180) / 50)): rr(d, (165 + k * 50, 405 + r * 55, 205 + k * 50, 445 + r * 55), 6, (70, 72, 80))
        if kind == "kbmouse": d.ellipse((700, 420, 860, 680), fill=c); d.line((780, 420, 780, 530), fill=(80, 80, 90), width=5)
    elif kind == "headset":
        d.arc((280, 200, 720, 700), 180, 360, fill=c, width=44); rr(d, (240, 420, 360, 640), 50, c); rr(d, (640, 420, 760, 640), 50, c)
        d.line((300, 640, 420, 760), fill=c, width=14); d.ellipse((400, 740, 450, 790), fill=c)
    elif kind in ("cartridge", "toner"):
        if kind == "toner":
            rr(d, (180, 400, 820, 640), 30, c); rr(d, (220, 430, 560, 610), 14, (60, 62, 70)); label(d, (580, 450, 800, 600), "85A", 70)
        else:
            box3d(d, 330, 330, 320, 420, 90, (245, 245, 248)); d.rectangle((330, 330, 650, 420), fill=c); label(d, (350, 500, 630, 640), (__import__("re").search(r"[A-Z]*-?\d{3}[A-Z]?", name) or __import__("re").search(r"\w+", "INK")).group(0), 64, (40, 40, 50))
    elif kind == "batteries":
        for i in range(4):
            x = 300 + i * 105; rr(d, (x, 300, x + 85, 760), 18, c); d.rectangle((x, 300, x + 85, 420), fill=(30, 30, 30)); rr(d, (x + 28, 270, x + 57, 305), 6, (190, 190, 200))
    elif kind == "cable":
        d.arc((260, 260, 740, 740), 30, 330, fill=(30, 30, 35), width=24)
        for (x, y) in ((690, 330), (690, 640)): rr(d, (x, y - 40, x + 120, y + 40), 10, (40, 40, 45)); rr(d, (x + 110, y - 25, x + 160, y + 25), 6, (190, 190, 200))
    elif kind == "book":
        def f(d):
            x0, y0, x1, y1 = 300, 160, 700, 810
            d.rectangle((x0 + 20, y0 + 16, x1 + 20, y1 + 16), fill=(235, 232, 225)); rr(d, (x0, y0, x1, y1), 8, c)
            d.rectangle((x0, y0, x0 + 26, y1), fill=sh(c, .75))
            title = name.split(" — ")[0]
            light = sum(c) > 500
            fg = (30, 30, 40) if light else (255, 255, 255)
            d.rectangle((x0 + 60, y0 + 70, x1 - 40, y0 + 76), fill=mix(c, fg, .5))
            wrap_title(d, title.upper(), (x0 + 60, y0 + 110, x1 - 40, y1), 44, fg)
            if " — " in name:
                sub = name.split(" — ")[1].split(" (")[0]
                label(d, (x0 + 40, y1 - 110, x1 - 40, y1 - 60), sub, 28, mix(c, fg, .75))
            rr(d, (x0 + 60, y1 - 220, x1 - 60, y1 - 130), 10, mix(c, fg, .18))
        C.rot(f, -3)
    elif kind in ("puzzle",):
        rr(d, (220, 250, 780, 750), 20, c);
        for i in range(4):
            for k in range(4):
                x = 250 + k * 128; y = 280 + i * 112; rr(d, (x, y, x + 120, y + 104), 10, sh(c, 1.15 - ((i + k) % 2) * .2))
        d.ellipse((560, 300, 680, 420), fill=hx("#f7c714"))
    elif kind == "abacus":
        rr(d, (230, 200, 770, 800), 20, None, c, 26)
        for r in range(8):
            y = 260 + r * 66; d.line((250, y, 750, y), fill=(120, 120, 130), width=6)
            for k in range(6): d.ellipse((290 + k * 50 + (r % 3) * 30, y - 24, 336 + k * 50 + (r % 3) * 30, y + 24), fill=PAL[r % len(PAL)])
    elif kind == "sciencekit":
        box3d(d, 230, 380, 540, 360, 90, c); label(d, (260, 560, 740, 660), "PETIT CHIMISTE", 52)
        for i, cc in enumerate([hx("#2a9d4b"), hx("#e63946"), hx("#f7c714")]): rr(d, (300 + i * 140, 220, 360 + i * 140, 420), 20, (230, 240, 250), (170, 190, 215), 3); rr(d, (306 + i * 140, 320, 354 + i * 140, 414), 18, cc)
    elif kind == "chess":
        rr(d, (220, 260, 780, 820), 14, c)
        for i in range(8):
            for k in range(8):
                if (i + k) % 2: d.rectangle((250 + k * 62.5, 290 + i * 62.5, 312 + k * 62.5, 352 + i * 62.5), fill=(240, 220, 180))
        d.ellipse((470, 140, 530, 200), fill=(30, 30, 30)); rr(d, (455, 190, 545, 300), 20, (30, 30, 30))
    elif kind == "cards":
        for i, cc in enumerate([hx("#e63946"), hx("#f7c714"), hx("#2a9d4b"), hx("#2c7be5")]):
            def f(d, cc=cc, i=i):
                rr(d, (380, 260, 620, 640), 22, (255, 255, 255)); rr(d, (395, 275, 605, 625), 16, cc); d.ellipse((420, 360, 580, 540), fill=(255, 255, 255))
            C.rot(f, 30 - i * 20, (500, 700))
    elif kind == "dominoes":
        for i in range(5):
            x = 230 + i * 110; rr(d, (x, 320 + (i % 2) * 40, x + 90, 680 + (i % 2) * 40), 14, c); d.line((x + 10, 500 + (i % 2) * 40, x + 80, 500 + (i % 2) * 40), fill=(200, 200, 200), width=4)
            for j in range(i % 4 + 1): d.ellipse((x + 35, 350 + (i % 2) * 40 + j * 35, x + 55, 370 + (i % 2) * 40 + j * 35), fill=(255, 255, 255))
    else:
        box3d(d, 300, 380, 400, 340, 100, c)
    C.out(path)

if __name__ == "__main__":
    import sys, json, os
    sys.path.insert(0, os.path.dirname(__file__))
    import catalog
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for p in catalog.products():
        draw(p["kind"], p["color"], p["name"], os.path.join(out, p["sku"].lower() + ".jpg"))
    print("ok")
