"""Génère assets/dark.css (mode nuit) à partir des feuilles de style existantes."""
import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__)) + "/"
import re, colorsys

FILES = ["site.css", "digitale.css", "nova.css"]
D = BASE + "assets/"
PFX = 'html[data-theme="dark"]'

NAMED = {"white": "#ffffff", "black": "#000000"}

def parse(c):
    c = c.strip().lower()
    c = NAMED.get(c, c)
    if c.startswith("#"):
        h = c[1:]
        if len(h) in (3, 4): h = "".join(x * 2 for x in h)
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1
        return r, g, b, a
    m = re.match(r"rgba?\(([^)]*)\)", c)
    if m:
        p = [x.strip() for x in re.split(r"[ ,/]+", m.group(1)) if x.strip()]
        r, g, b = (float(x) / 255 for x in p[:3]); a = float(p[3]) if len(p) > 3 else 1
        return r, g, b, a
    return None

def hexa(r, g, b, a=1):
    s = "#%02x%02x%02x" % tuple(round(max(0, min(1, x)) * 255) for x in (r, g, b))
    return s if a >= 1 else f"rgba({round(r*255)},{round(g*255)},{round(b*255)},{a:.2f})"

def lum(r, g, b): return 0.2126 * r + 0.7152 * g + 0.0722 * b

def bg_map(rgba):
    r, g, b, a = rgba
    L = lum(r, g, b); h, l, s = colorsys.rgb_to_hls(r, g, b)
    if a < 1 and L > .9:            # voile blanc -> voile clair discret
        return hexa(1, 1, 1, min(a, .08))
    if L >= .97: return "#161c24"
    if L >= .9:
        if s > .35:                 # teinte pastel (vert clair, jaune clair…) -> version sombre teintée
            r2, g2, b2 = colorsys.hls_to_rgb(h, .17, min(s, .45)); return hexa(r2, g2, b2)
        return "#1c232d"
    if L >= .8 and s < .3: return "#252e39"
    return None

def fg_map(rgba):
    r, g, b, a = rgba
    L = lum(r, g, b); h, l, s = colorsys.rgb_to_hls(r, g, b)
    if a < 1: return None
    if L < .2 and (s < .5 or (h > .5 and h < .75)):  # encre / bleu marine
        return "#e7ecf2"
    if L < .5 and s < .25: return "#a7b2bf"            # gris moyen
    if L < .3 and s >= .5:                              # couleur saturée sombre -> éclaircir
        r2, g2, b2 = colorsys.hls_to_rgb(h, .68, s); return hexa(r2, g2, b2)
    return None

def border_map(rgba):
    r, g, b, a = rgba
    if lum(r, g, b) > .7 and colorsys.rgb_to_hls(r, g, b)[2] < .35: return "#2d3743" if a >= 1 else hexa(1, 1, 1, .12)
    return None

COLRE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\bwhite\b|\bblack\b")

def conv(prop, val):
    p = prop.lower()
    if p in ("background", "background-color", "background-image"): f = bg_map
    elif p in ("color", "fill", "stroke", "-webkit-text-fill-color", "caret-color"): f = fg_map
    elif p.startswith("border") or p.startswith("outline"): f = border_map
    else: return None
    if p in ("color", "fill", "stroke") and "var(--primary)" in val:
        return val.replace("var(--primary)", "#9cc3ef")
    if p.startswith("background") and "var(--ink)" in val:
        return val.replace("var(--ink)", "#0b1118")
    changed = False
    def rep(m):
        nonlocal changed
        c = parse(m.group(0))
        if not c: return m.group(0)
        n = f(c)
        if n: changed = True; return n
        return m.group(0)
    out = COLRE.sub(rep, val)
    return out if changed else None

def blocks(css, media=""):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0: break
        sel = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{": depth += 1
            elif css[k] == "}": depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        if sel.startswith("@media") or sel.startswith("@supports"):
            yield from blocks(body, sel)
        elif not sel.startswith("@"):
            yield media, sel, body
        i = k

def scope(sel):
    out = []
    for s in sel.split(","):
        s = s.strip()
        if not s: continue
        if s.startswith(":root") or s in ("html",): out.append(PFX)
        elif s.startswith("html"): out.append(PFX + s[4:])
        else: out.append(f"{PFX} {s}")
    return ", ".join(out)

rules = []
for f in FILES:
    for media, sel, body in blocks(open(D + f).read()):
        decls = []
        bgset = None
        items = [d.split(":", 1) for d in body.split(";") if ":" in d]
        for prop, val in items:
            prop = prop.strip()
            if prop.startswith("--"): continue
            if prop.lower().startswith("background"):
                c = COLRE.search(val)
                bgset = parse(c.group(0)) if c else bgset
            nv = conv(prop, val.strip())
            if nv is not None: decls.append((prop, nv))
        # texte sur fond coloré (jaune, vert…) dans la même règle : garder la couleur d'origine
        if bgset and bg_map(bgset) is None and lum(*bgset[:3]) > .25:
            decls = [d for d in decls if d[0] not in ("color", "fill", "stroke")]
        if decls:
            rules.append((media, scope(sel), decls))

VARS = f"""{PFX} {{
  color-scheme: dark;
  --ink: #e7ecf2; --muted: #9aa6b3; --line: #2b3440; --paper: #0f141a; --card: #161c24; --surface-2: #1c232d; --bg: #0f141a;
  --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px -12px rgba(0,0,0,.6); --shadow-lg: 0 18px 40px -16px rgba(0,0,0,.7);
  --wc-content-bg: #161c24; --wc-subtext: #9aa6b3; --wc-secondary: #1c232d; --wc-secondary-text: #c9d1da;
}}
{PFX} body {{ background: #0f141a; color: #e7ecf2; }}
"""
out = ["/* Mode nuit — généré par make_dark.py */", VARS]
for media, sel, decls in rules:
    body = "; ".join(f"{p}: {v}" for p, v in decls)
    r = f"{sel} {{ {body} }}"
    out.append(f"{media} {{ {r} }}" if media else r)
out.append(open(BASE + "dark_extra.css").read())
open(D + "dark.css", "w").write("\n".join(out))
print(len(rules), "règles")
