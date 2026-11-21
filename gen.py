"""Générateur du site statique trilingue « Librairie digitale » (FR / EN / AR)."""
import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__)) + "/"
import os, re, json, shutil, html, unicodedata, sys
sys.path.insert(0, os.path.dirname(__file__))
import catalog, i18n_products as IP, site_i18n as SI, nova_i18n as NV, variants as VR, pay_i18n as PJ

OUT = sys.argv[1] if len(sys.argv) > 1 else _os.path.join(BASE, "..", "site")
WA = "212760923785"; PHONE = "+212 760-923785"
LANGS = ["fr", "en", "ar"]
PER_PAGE = 24
E = html.escape

# ---------------- icônes ----------------
ICONS = {
 'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 'cart': '<path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/>',
 'phone': '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'menu': '<path d="M3 6h18M3 12h18M3 18h18"/>', 'close': '<path d="M6 6l12 12M18 6 6 18"/>',
 'chevron': '<path d="m9 6 6 6-6 6"/>', 'left': '<path d="m15 6-6 6 6 6"/>',
 'grid': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 'truck': '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/>',
 'cash': '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 9v.01M18 15v.01"/>',
 'shield': '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'list': '<path d="M9 6h12M9 12h12M9 18h12"/><path d="m3 6 1 1 2-2M3 12l1 1 2-2M3 18l1 1 2-2"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'pencil': '<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="m14 6 3 3"/>',
 'printer': '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M6 14h12v7H6z"/>',
 'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'building': '<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-4h6v4M8 8h2M14 8h2M8 12h2M14 12h2"/>',
 'briefcase': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
 'file': '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'graduation': '<path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
 'download': '<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
 'clipboard': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h4"/>',
 'cv': '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="12" cy="9" r="2.5"/><path d="M8 16c1-2 2.5-3 4-3s3 1 4 3"/>',
 'doc': '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/>',
 'keyboard': '<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7 14h10"/>',
 'book': '<path d="M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4zM20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6z"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 'copy': '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
 'scan': '<path d="M4 8V5a1 1 0 0 1 1-1h3M16 4h3a1 1 0 0 1 1 1v3M20 16v3a1 1 0 0 1-1 1h-3M8 20H5a1 1 0 0 1-1-1v-3M4 12h16"/>',
 'camera': '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
 'layers': '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
 'bind': '<rect x="6" y="3" width="13" height="18" rx="1"/><path d="M4 6h4M4 10h4M4 14h4M4 18h4"/>',
 'card': '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 11h6M7 14h4"/>',
 'image': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/>',
 'at': '<circle cx="12" cy="12" r="4"/><path d="M16 12v1.5a2.5 2.5 0 0 0 5 0V12a9 9 0 1 0-4 7.5"/>',
 'send': '<path d="M21 3 3 10l7 3 3 7z"/><path d="m10 13 4-4"/>',
 'lock': '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'bank': '<path d="M3 10 12 4l9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
 'card': '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
 'trash': '<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>',
 'store': '<path d="M3 9 5 4h14l2 5"/><path d="M4 9v11h16V9"/><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M10 20v-5h4v5"/>',
 'home2': '<path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/>',
 'check': '<path d="m5 12 5 5 9-10"/>',
 'mouse': '<rect x="6" y="3" width="12" height="18" rx="6"/><path d="M12 7v4"/>',
 'books': '<path d="M4 4h4v16H4zM9 4h4v16H9z"/><path d="m14.5 5.2 3.8-1 3.7 15.5-3.8 1z"/><path d="M4 8h4M9 8h4M4 16h4M9 16h4"/>',
 'backpack': '<path d="M5 10a7 7 0 0 1 14 0v10a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1z"/><path d="M9 3h6v3H9zM8 21v-6h8v6M10 10h4"/>',
 'abacus': '<rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 8h18M3 13h18M3 18h18"/><circle cx="8" cy="8" r="1.4"/><circle cx="11" cy="8" r="1.4"/><circle cx="15" cy="13" r="1.4"/><circle cx="7" cy="13" r="1.4"/><circle cx="12" cy="18" r="1.4"/><circle cx="16" cy="18" r="1.4"/>',
 'palette': '<path d="M12 3a9 9 0 0 0 0 18c1.1 0 1.6-.9 1.2-1.8-.5-1-.2-2.2 1.2-2.2H17a4 4 0 0 0 4-4c0-5.5-4-10-9-10z"/><circle cx="7.5" cy="11" r="1.2"/><circle cx="10" cy="7" r="1.2"/><circle cx="15" cy="7.5" r="1.2"/>',
 'rocket': '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M9 15l-3-3c1-4 4-8 10-9 1 0 2 1 2 2-1 6-5 9-9 10z"/><circle cx="14.5" cy="9.5" r="1.6"/><path d="M6 12H3l2-4h4M12 18v3l4-2v-4"/>',
 'play': '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3z"/>',
 'share': '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="m8.2 10.8 7.6-3.6M8.2 13.2l7.6 3.6"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'star': '<path d="m12 3 2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8 6.6 19.7l1.1-6.1L3.2 9.4l6.1-.8z"/>',
 'megaphone': '<path d="M3 10v4h3l7 4V6L6 10z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11"/>',
 'chart': '<path d="M3 20h18"/><path d="M6 16v-5M11 16V7M16 16v-8M21 4l-5 4-5-3-5 4"/>',
 'moon': '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
}
WA_ICON = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'
def ic(name, s=20):
    if name == "whatsapp": return WA_ICON.format(s=s)
    if name not in ICONS: name = "grid"
    return f'<svg width="{s}" height="{s}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def icon_sprite():
    sym = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{v}</symbol>' for k, v in ICONS.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">{sym}</svg>'

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def wa(msg=""):
    from urllib.parse import quote
    return f"https://wa.me/{WA}" + (f"?text={quote(msg)}" if msg else "")

# ---------------- données ----------------
import time as _t
ASSET_V = _t.strftime("%Y%m%d%H%M")
P = catalog.products()
P.sort(key=lambda p: not (p.get("real") and p.get("photo")))  # produits « À venir » toujours en dernier
TOPS = catalog.TOP_ORDER
SUBS = {}  # top -> [sub...]
for p in P:
    t, s = p["cats"].split(" > ")
    p["top"], p["sub"] = t, s
    SUBS.setdefault(t, [])
    if s not in SUBS[t]: SUBS[t].append(s)
    p["slug"] = "p-" + p["sku"].lower()
    p["img"] = f"img/p/{p['sku'].lower()}.jpg"
    if p.get("real"):
        ref = p.get("ref")
        IP.T[p["name"]] = (p["en"], p["short3"][1] + (f" Ref. {ref}." if ref else ""), p["ar"], p["short3"][2] + (f" المرجع: {ref}." if ref else ""))
import json as _json, real_catalog as _RC
_BYNAME = _json.load(open(BASE + "imgs-byname/index.json"))
CAT_IMG = _json.load(open(BASE + "real/cats/index.json"))
for _k, _v in _RC.SUBS.items():
    IP.CATS.setdefault(_v[1], (_v[2], _v[3]))
IP.CATS["Cahiers"] = ("Notebooks", "الدفاتر")
IP.CATS["Papeterie & blocs-notes"] = ("Paper & notepads", "الورق والمذكرات")
IP.CAT_DESC["Écriture & Correction"] = ("Ballpoint pens, rollerballs, pencils, markers, highlighters and correction pens.", "أقلام الحبر الجاف والسائل، أقلام الرصاص، الماركر، أقلام التمييز والتصحيح.")
IP.CAT_DESC["Cahiers"] = ("A5 and A4 notebooks, spiral, practical-work notebooks, homework diaries and registers.", "دفاتر A5 وA4، حلزونية، دفاتر الأشغال التطبيقية، دفاتر النصوص والسجلات.")
IP.CAT_DESC["Classement & Archivage"] = ("Archive boxes, binders, display books and signature books.", "علب الأرشيف، الملفات، حافظات الوثائق ودفاتر التوقيع.")
IP.CAT_DESC["Papeterie & blocs-notes"] = ("Notepads, Post-it notes, A4 and coloured paper, envelopes.", "المذكرات، أوراق Post-it، ورق A4 والورق الملون، الأظرفة.")
IP.CAT_DESC["Livres"] = ("Textbooks, dictionaries, revision guides, novels and children's books.", "الكتب المدرسية، القواميس، الكتب الموازية، الروايات وكتب الأطفال.")

def cname(fr, L):
    return fr if L == "fr" else IP.CATS[fr][0 if L == "en" else 1]
def cslug(fr): return "c-" + slug(fr)

import groups as _GR
GROUPS = _GR.GROUPS
for _k, _v in _GR.NEW_SUBS.items(): IP.CATS.setdefault(_k, _v)
def leaf(e): return isinstance(e, tuple) and len(e[3]) == 1 and not e[4]
def gname(g, L): return g[{"fr": 0, "en": 1, "ar": 2}[L]]
def gslug(g): return "g-" + slug(g[0])
def eslug(e):  # entrée de famille : sous-groupe ou sous-rayon
    if isinstance(e, tuple): return cslug(e[4]) if e[4] else (cslug(e[3][0]) if len(e[3]) == 1 else "g-" + slug(e[0]))
    return cslug(e)
def ename(e, L): return gname(e, L) if isinstance(e, tuple) else cname(e, L)
def esubs(e): return e[3] if isinstance(e, tuple) else [e]
def gsubs(g): return [x for e in g[5] for x in esubs(e)]
# ---- produits déclinés en couleurs ----
_byname = {p["name"]: p for p in P}
_byname_all = {p["sku"]: p["name"] for p in P}
_bysku_all = {p["sku"]: p for p in P}
for _parent, (_en, _ar), _members in VR.GROUPS:
    if any(n and n not in _byname for c, n in _members): continue
    _ex = [_byname[n] for c, n in _members if n]
    _base = _ex[0]
    _base["parent_names"] = {"fr": _parent, "en": _en, "ar": _ar}
    _vs = []
    for c, n in _members:
        if n:
            q = _byname[n]; _vs.append(dict(color=c, sku=q["sku"], img=q["img"], regular=q["regular"], sale=q["sale"]))
        else:
            sku = _base["sku"] + "-" + c[:3].upper()
            _vs.append(dict(color=c, sku=sku, img=f"img/p/{sku.lower()}.jpg", regular=_base["regular"], sale=_base["sale"], gen=True))
    _base["variants"] = _vs
    if _base.get("real"):  # la référence fabricant dépend de la couleur : on la retire de la description commune
        _base["short"] = _base["short3"][0]
        IP.T[_base["name"]] = (IP.T[_base["name"]][0], _base["short3"][1], IP.T[_base["name"]][2], _base["short3"][2])
    for q in _ex[1:]: P.remove(q)

def pname(p, L):
    if "parent_names" in p: return p["parent_names"][L]
    return p["name"] if L == "fr" else IP.T[p["name"]][0 if L == "en" else 2]
def pshort(p, L): return p["short"] if L == "fr" else IP.T[p["name"]][1 if L == "en" else 3]
def cl(c, L): return VR.COLORS[c][{"fr": 0, "en": 1, "ar": 2}[L]]
def swatches_mini(p, L, pre):
    if "variants" not in p: return ""
    dots = "".join(f'<span class="sw" style="--c:{VR.COLORS[v["color"]][3]}" title="{E(cl(v["color"], L))}" data-img="{pre}{v["img"]}"></span>' for v in p["variants"])
    return f'<div class="nb-sw">{dots}<small>{len(p["variants"])} {E(VR.LABELS[L]["colors"])}</small></div>'
def money(v, L):
    s = f"{float(v):.2f}"
    return f"{s} {'درهم' if L == 'ar' else 'Dhs'}"
def cat_first_img(fr):
    if fr in CAT_IMG: return "img/c/" + CAT_IMG[fr]
    for p in P:
        if p["top"] == fr or p["sub"] == fr: return p["img"]
    return ""

# ---------------- gabarit ----------------
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Marcellus&family=Cairo:wght@400;600;700;800&family=El+Messiri:wght@600;700&display=swap">')

def head(L, title, root, desc=""):
    U = SI.UI[L]
    d = ' dir="rtl"' if L == "ar" else ""
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{root}{"" if l == "fr" else l + "/"}{{FILE}}">' for l in LANGS)
    return (f'<!doctype html><html lang="{L}"{d}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{E(title)} – {E(U["brand"])}</title><meta name="description" content="{E(desc or U["footer_about"])}">'
            f'<link rel="icon" href="{root}img/favicon.png">{alt}{FONTS}<link rel="stylesheet" href="{root}assets/site.css?v={ASSET_V}"><link rel="stylesheet" href="{root}assets/digitale.css?v={ASSET_V}"><link rel="stylesheet" href="{root}assets/nova.css?v={ASSET_V}"><link rel="stylesheet" href="{root}assets/dark.css?v={ASSET_V}">'
            '<script>(function(){var t=null;try{t=localStorage.getItem("ld_theme")}catch(e){}if(t==="dark"||(!t&&window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches))document.documentElement.setAttribute("data-theme","dark")})()</script></head>')

def catmenu(L, root, services=True):
    chev = ic("chevron", 14)
    out = ['<ul class="catmenu catmenu--groups">']
    if services:
        out.append(f'<li class="catmenu__item catmenu__item--svc has-children"><a href="services.html"><span class="catmenu__icon catmenu__icon--svc">{ic("monitor", 18)}</span><span class="catmenu__label">{E(NV.N[L]["svc_cat"])}</span><span class="catmenu__arrow">{chev}</span></a>'
                   f'<button class="catmenu__toggle" aria-label="+">{chev}</button><ul class="catmenu__sub catmenu__casc">')
        for gid, gic, gn, gd in SI.SERVICE_GROUPS:
            items = [sv for sv in SI.SERVICES if sv[0] == gid]
            out.append(f'<li class="has-children"><a href="services.html#{gid}"><span>{E(gn[L])}</span>{chev}</a><button class="catmenu__toggle" aria-label="+">{chev}</button>'
                       f'<ul class="catmenu__sub catmenu__casc catmenu__casc--3">' +
                       "".join(f'<li><a href="services.html#s-{slug(sv[5]["fr"][0])}"><span>{E(sv[5][L][0])}</span></a></li>' for sv in items) + '</ul></li>')
        out.append('</ul></li>')
    for g in GROUPS:
        out.append(f'<li class="catmenu__item has-children"><a href="{gslug(g)}.html"><span class="catmenu__icon catmenu__icon--line">{ic(g[3], 20)}</span><span class="catmenu__label">{E(gname(g, L))}</span><span class="catmenu__arrow">{chev}</span></a>'
                   f'<button class="catmenu__toggle" aria-label="+">{chev}</button><ul class="catmenu__sub catmenu__casc">')
        for e in g[5]:
            if leaf(e):
                out.append(f'<li><a href="{eslug(e)}.html"><span>{E(ename(e, L))}</span></a></li>')
            elif isinstance(e, tuple):
                out.append(f'<li class="has-children"><a href="{eslug(e)}.html"><span>{E(ename(e, L))}</span>{chev}</a><button class="catmenu__toggle" aria-label="+">{chev}</button>'
                           f'<ul class="catmenu__sub catmenu__casc catmenu__casc--3">' +
                           "".join(f'<li><a href="{cslug(x)}.html"><span>{E(cname(x, L))}</span></a></li>' for x in e[3]) + '</ul></li>')
            else:
                out.append(f'<li><a href="{cslug(e)}.html"><span>{E(cname(e, L))}</span></a></li>')
        out.append('</ul></li>')
    out.append('</ul>')
    return "".join(out)

THEME_L = {"fr": ("Mode nuit", "Mode jour"), "en": ("Dark mode", "Light mode"), "ar": ("الوضع الليلي", "الوضع النهاري")}
def theme_btn(L):
    d, l = THEME_L[L]
    return (f'<button type="button" class="theme-toggle" data-theme-toggle aria-pressed="false" title="{E(d)} / {E(l)}">'
            f'<span class="ic-moon">{ic("moon", 14)}</span><span class="ic-sun">{ic("sun", 14)}</span>'
            f'<span class="theme-toggle__lbl-l">{E(d)}</span><span class="theme-toggle__lbl-d">{E(l)}</span></button>')

def header(L, file, root, active=""):
    U = SI.UI[L]
    langs = "".join(f'<a href="{root}{"" if l == "fr" else l + "/"}{file}" class="{"is-active" if l == L else ""}" hreflang="{l}" lang="{l}">{SI.UI[l]["lang_name"]}</a>' for l in LANGS)
    opts = "".join(f'<option value="{slug(t)}">{E(cname(t, L))}</option>' for t in TOPS)
    nav = [("index.html", U["home"]), ("boutique.html", U["shop"]), ("services.html", U["services"]),
           (gslug(GROUPS[0]) + ".html", gname(GROUPS[0], L)), (gslug(GROUPS[4]) + ".html", gname(GROUPS[4], L)), (gslug(GROUPS[3]) + ".html", gname(GROUPS[3], L)), ("contact.html", U["contact"])]
    navh = "".join(f'<li class="{"current-menu-item" if f == active else ""}"><a href="{f}">{E(t)}</a></li>' for f, t in nav)
    home = file == "index.html"
    return f'''<body class="nova style-pro woocommerce woocommerce-page{' rtl' if L == 'ar' else ''} lang-{L}{' home' if home else ''}">{icon_sprite()}
<a class="skip-link" href="#main">↓</a>
<div class="topbar"><div class="container topbar__inner">
 <div class="topbar__contact"><a href="tel:{PHONE.replace(' ', '').replace('-', '')}">{ic("phone", 14)} <span dir="ltr">{PHONE}</span></a><span class="topbar__hours">{ic("clock", 14)} {E(U["hours_v"])}</span><a class="topbar__find" href="{E(GO_URL)}" target="_blank" rel="noopener">{ic("pin", 14)} {E(FIND[L]["top"])}</a>{theme_btn(L)}</div>
 <p class="topbar__msg">{E(U["topbar"])}</p>
 <nav class="toplinks"><a href="boutique.html">{E(U["shop"])}</a><a href="services.html">{E(U["services"])}</a><a href="contact.html">{E(U["contact"])}</a></nav>
 <nav class="langs" aria-label="Langue">{langs}</nav>
</div></div>
<header class="site-header" data-sticky><div class="container header__inner">
 <button class="icon-btn header__burger" data-drawer-open aria-label="{E(U["menu"])}">{ic("menu", 22)}</button>
 <div class="header__logo"><a class="text-logo" href="index.html" rel="home"><span class="brandmark"><img src="{root}img/logo-entete2.png" alt="{E(U["brand"])}" width="500" height="498"></span><span class="text-logo__txt"><strong>{E(U["brand"])}</strong><small>{E(U["tagline"])}</small></span></a></div>
 <form class="search" role="search" method="get" action="recherche.html">
  <select name="cat" class="search__cat" aria-label="{E(U["cats"])}"><option value="">{E(U["all"])}</option>{opts}</select>
  <input class="search__input" type="search" name="s" placeholder="{E(NV.N[L]["search_ph"])}" aria-label="{E(U["search"])}">
  <button class="search__btn" type="submit" aria-label="{E(U["search"])}">{ic("search", 20)}</button>
 </form>
 <div class="header__actions"><a class="nb-hbtn nb-hbtn--map" href="{E(GO_URL)}" target="_blank" rel="noopener" title="{E(FIND[L]["float_"])}">{ic("pin", 20)}<span>{E(FIND[L]["btn"])}</span></a><a class="nb-hbtn nb-hbtn--cart" href="panier.html">{ic("cart", 20)}<span>{E(PJ.J[L]["cart"])}</span><b class="cart-count" data-cart-count hidden>0</b></a><a class="nb-hbtn nb-hbtn--icon js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic("whatsapp", 20)}</a></div>
</div>
<nav class="mainnav"><div class="container mainnav__inner">
 <div class="allcats{' allcats--home' if home else ''}"><button class="allcats__btn" type="button">{ic("menu", 18)} {E(U["all_cats"])}</button>{'' if home else '<div class="allcats__panel"><div class="js-catmenu"></div></div>'}</div>
 <ul class="mainnav__menu">{navh}</ul>
 <a class="mainnav__wa js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener">{ic("whatsapp", 16)} {E(U["order_wa"])}</a>
</div></nav></header>
<div class="drawer" data-drawer aria-hidden="true"><div class="drawer__panel"><div class="drawer__head"><strong>{E(U["cats"])}</strong><button class="icon-btn" data-drawer-close aria-label="{E(U["close"])}">{ic("close", 22)}</button></div>
<div class="js-catmenu"></div><ul class="drawer__menu">{navh}</ul><nav class="langs langs--drawer">{langs}</nav></div><div class="drawer__overlay" data-drawer-close></div></div>
<main id="main" class="site-main">'''

def pay_badges(L, big=False):
    J = PJ.J[L]
    b = [('<span class="pb pb--visa" dir="ltr">VISA</span>'), ('<span class="pb pb--mc" dir="ltr"><i></i><i></i>mastercard</span>'), ('<span class="pb pb--cmi" dir="ltr">CMI</span>'),
         f'<span class="pb">{ic("cash", 16)} {E(J["badge_cod"])}</span>', f'<span class="pb">{ic("bank", 16)} {E(J["badge_bank"])}</span>', f'<span class="pb">{ic("store", 16)} {E(J["badge_store"])}</span>']
    return f'<div class="paybadges{" paybadges--big" if big else ""}" aria-label="{E(J["pays_t"])}"><a href="paiement.html" class="pb pb--lock">{ic("lock", 16)} {E(J["secure"])}</a>{"".join(b)}</div>'

def footer(L, file, root):
    U = SI.UI[L]
    cats = "".join(f'<li><a href="{gslug(g)}.html">{E(gname(g, L))}</a></li>' for g in GROUPS)
    info = "".join(f'<li><a href="{f}">{E(t)}</a></li>' for f, t in [("services.html", U["services"]), ("a-propos.html", U["about"]), ("paiement.html", PJ.J[L]["pays_t"]), ("livraison-retours.html", U["delivery"]), ("conditions-generales-de-vente.html", U["terms"]), ("contact.html", U["contact"])])
    langs = "".join(f'<a href="{root}{"" if l == "fr" else l + "/"}{file}" class="{"is-active" if l == L else ""}" lang="{l}">{SI.UI[l]["lang_name"]}</a>' for l in LANGS)
    i18n = {k: U[k] for k in ["wa_hello", "wa_name", "wa_addr", "wa_unit", "wa_service", "toast", "results_for", "no_result", "all_products", "order", "in_stock"]}
    i18n.update({k: v for k, v in PJ.J[L].items() if isinstance(v, str)}); i18n["cur"] = "درهم" if L == "ar" else "Dhs"
    i18n = json.dumps(i18n, ensure_ascii=False)
    return f'''</main>
<footer class="site-footer"><div class="container footer__grid">
 <div class="footer__col footer__about"><div class="footer__logo"><img src="{root}img/logo-data.png" alt="{E(U["brand"])}" class="footer__brand"></div><p>{E(U["footer_about"])}</p></div>
 <div class="footer__col"><h4 class="widget-title">{E(U["cats"])}</h4><ul class="footer__links">{cats}</ul></div>
 <div class="footer__col"><h4 class="widget-title">{E(U["info"])}</h4><ul class="footer__links">{info}</ul></div>
 <div class="footer__col"><h4 class="widget-title">{E(U["contact"])}</h4><ul class="footer__contact">
  <li>{ic("phone", 16)} <a href="tel:{PHONE.replace(' ', '').replace('-', '')}" dir="ltr">{PHONE}</a></li>
  <li>{ic("whatsapp", 16)} <a class="js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener">{E(U["write_wa"])}</a></li>
  <li>{ic("building", 16)} <a href="{PLACE_URL}" target="_blank" rel="noopener">{E(U["address_v"])}</a></li>
  <li>{ic("clock", 16)} {E(U["hours_v"])}</li></ul>
  <nav class="langs langs--footer">{langs}</nav></div>
</div><div class="footer__bottom"><div class="container footer__bottom-inner"><span>© 2026 {E(U["brand"])} — {E(U["rights"])}</span>{pay_badges(L)}</div></div></footer>
<a class="map-float" href="{E(GO_URL)}" target="_blank" rel="noopener" aria-label="{E(FIND[L]["float_"])}" title="{E(FIND[L]["float_"])}">{ic("pin", 26)}<span>{E(FIND[L]["btn"])}</span></a><a class="wa-float js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic("whatsapp", 30)}</a>
<div id="toast" class="toast" hidden></div>
<script>window.I18N={i18n};window.ROOT="{root}";window.LANG="{L}";</script>
<script src="{root}config.js"></script><script src="{root}assets/app.js?v={ASSET_V}"></script>
</body></html>'''

SOON_T = {"fr": "À venir", "en": "Coming soon", "ar": "قريباً"}
ASK_T = {"fr": "Demander sur WhatsApp", "en": "Ask on WhatsApp", "ar": "استفسر عبر واتساب"}
def soon(p): return not (p.get("real") and p.get("photo"))  # pas de photo ou de prix réels → « À venir »
def soon_price(L): return f'<span class="soon-price">{E(SOON_T[L])}</span>'

def card(p, L, pre=""):
    U = SI.UI[L]
    on = ""
    if p["sale"]:
        pct = round(100 - float(p["sale"]) / float(p["regular"]) * 100); on = f'<span class="onsale" dir="ltr">-{pct}%</span>'
        price = f'<del>{money(p["regular"], L)}</del> <ins>{money(p["sale"], L)}</ins>'
    else:
        price = money(p["regular"], L)
    n = pname(p, L)
    if soon(p):
        on, price = "", soon_price(L)
        return (f'<li class="product nb-card is-soon"><a href="{p["slug"]}.html" class="woocommerce-LoopProduct-link"><span class="nb-card__img"><img src="{pre}{thumb(p["img"])}" alt="{E(n)}" loading="lazy" width="400" height="400"></span>'
                f'<h2 class="woocommerce-loop-product__title">{E(n)}</h2><span class="price">{price}</span></a>'
                f'<div class="nb-card__foot"><a href="{p["slug"]}.html" class="nb-buy nb-buy--soon">{ic("whatsapp", 16)} {E(ASK_T[L])}</a></div></li>')
    return (f'<li class="product nb-card">{on}<a href="{p["slug"]}.html" class="woocommerce-LoopProduct-link"><span class="nb-card__img"><img src="{pre}{thumb(p["img"])}" alt="{E(n)}" loading="lazy" width="400" height="400"></span>'
            f'<h2 class="woocommerce-loop-product__title">{E(n)}</h2><span class="price">{price}</span></a>{swatches_mini(p, L, pre)}'
            + (f'<div class="nb-card__foot"><a href="{p["slug"]}.html" class="nb-buy nb-buy--choose">{ic("grid", 16)} {E(VR.LABELS[L]["choose"])}</a><span class="nb-stock">{E(U["in_stock"])}</span></div></li>' if "variants" in p else
               f'<div class="nb-card__foot"><a href="#" class="nb-buy js-add" {cdata(p, n, pre)}>{ic("cart", 16)} {E(PJ.J[L]["add"])}</a><span class="nb-stock">{E(U["in_stock"])}</span></div></li>'))

def cdata(p, n, pre, img=None, sku=None):
    return f'data-id="{sku or p["sku"]}" data-name="{E(n)}" data-p="{float(p["sale"] or p["regular"]):.2f}" data-img="{img or p["img"]}" data-url="{p["slug"]}.html"'

def section(L, title, sub, link, items, pre):
    items = [p for p in items if p.get("real") and p.get("photo")]  # jamais de produit « À venir » sur l'accueil
    U = SI.UI[L]
    if not items: return ""
    head_ = f'<header class="psection__head"><div><h2 class="psection__title">{E(title)}</h2>' + (f'<p class="psection__sub">{E(sub)}</p>' if sub else "") + '</div><div class="psection__actions">'
    if link: head_ += f'<a class="psection__all" href="{link}">{E(U["see_all"])}</a>'
    head_ += f'<button class="carousel-btn" data-dir="-1" aria-label="{E(U["prev"])}">{ic("left", 18)}</button><button class="carousel-btn" data-dir="1" aria-label="{E(U["next"])}">{ic("chevron", 18)}</button></div></header>'
    return f'<section class="psection nb-sec container">{head_}<div class="woocommerce"><ul class="products carousel">{"".join(card(p, L, pre) for p in items)}</ul></div></section>'

def services_cards(L, items, pre):
    U = SI.UI[L]
    out = []
    for (g, icon, pf, pe, pa, names, feat) in items:
        n, d = names[L]; price = {"fr": pf, "en": pe, "ar": pa}[L]
        out.append(f'<article class="svc" id="s-{slug(names["fr"][0])}"><span class="svc__icon">{ic(icon, 26)}</span><h3 class="svc__name">{E(n)}</h3><p class="svc__desc">{E(d)}</p>'
                   f'<div class="svc__foot"><a href="#" class="svc__btn js-service" data-service="{E(n)}">{ic("whatsapp", 16)} {E(U["svc_ask"])}</a></div></article>')
    return "".join(out)

def packs_block(L, pre, home=False):
    from web_services import PACKS, PACK_UI
    K = PACK_UI[L]; out = []
    for pid, icon, prices, best, data in PACKS:
        n, tag, items = data[L]; price = prices[{"fr": 0, "en": 1, "ar": 2}[L]]
        li = "".join(f'<li>{ic("check", 16)} {E(x)}</li>' for x in items)
        out.append(f'<article class="pack{" pack--best" if best else ""}" id="{pid}">' + (f'<span class="pack__badge">{E(K["best"])}</span>' if best else "") +
                   f'<span class="pack__ic">{ic(icon, 28)}</span><h3 class="pack__name">{E(n)}</h3><p class="pack__tag">{E(tag)}</p>'
                   f'<p class="pack__incl">{E(K["incl"])}</p><ul class="pack__list">{li}</ul>'
                   f'<a href="#" class="btn pack__btn js-service" data-service="{E(n)}">{ic("whatsapp", 18)} {E(K["ask"])}</a></article>')
    head_ = (f'<header class="packs__head"><h2>{E(K["packs_t"])}</h2><p>{E(K["packs_s"])}</p></header>')
    return (f'<section class="packs{" packs--home container" if home else ""}">{head_}<div class="packs__grid">{"".join(out)}</div>'
            f'<p class="packs__custom">{ic("whatsapp", 16)} <a href="#" class="js-service" data-service="{E(K["packs_t"])} — sur mesure">{E(K["custom"])}</a></p></section>')

GITIGNORE = """# Secrets & environment files — never commit
.env
.env.*
!.env.example
*.pem
*.key

# OS / editor junk
.DS_Store
Thumbs.db
desktop.ini
.vscode/
.idea/

# Logs & temp
*.log
*.tmp
*.bak

# Netlify local state
.netlify/
"""

# Position exacte de la librairie (fiche Google Maps « Data Librairie Charaf L.C.H »)
SHOP_LL = "31.6737339,-8.0206104"
PLACE_URL = "https://maps.app.goo.gl/At59k2epAYsSkAC46"
GO_URL = "https://maps.app.goo.gl/At59k2epAYsSkAC46"
GO_T = {"fr": "Y aller depuis ma position", "en": "Directions from my location", "ar": "الطريق من موقعي الحالي"}

FIND = {
 "fr": dict(top="Nous trouver", btn="Itinéraire", float_="Itinéraire vers la librairie", t="Venez nous voir", s="514 Charaf, Mag 2, Marrakech — ouvert du lundi au samedi, de 9h à 22h.",
            go="Y aller avec Google Maps", see="Voir la fiche Google Maps", call="Appeler la librairie", near="À quelques minutes de Marjane, route de Casablanca."),
 "en": dict(top="Find us", btn="Directions", float_="Directions to the bookshop", t="Come and visit us", s="514 Charaf, Shop 2, Marrakech — open Monday to Saturday, 9 am to 10 pm.",
            go="Get directions with Google Maps", see="See our Google Maps listing", call="Call the bookshop", near="A few minutes from Marjane, Casablanca road."),
 "ar": dict(top="موقعنا", btn="الطريق", float_="الطريق إلى المكتبة", t="زورونا في المكتبة", s="514 الشرف، المحل 2، مراكش — مفتوح من الإثنين إلى السبت، من 9:00 إلى 22:00.",
            go="الوصول عبر خرائط Google", see="صفحتنا على خرائط Google", call="اتصل بالمكتبة", near="على بعد دقائق من مرجان، طريق الدار البيضاء."),
}

def write(L, file, content):
    d = OUT if L == "fr" else os.path.join(OUT, L)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, file), "w").write(content.replace("{FILE}", file))

def page(L, file, title, body, active="", desc=""):
    root = "" if L == "fr" else "../"
    write(L, file, head(L, title, root, desc) + header(L, file, root, active) + body + footer(L, file, root))
    if file == "index.html": write(L, "menu.html", catmenu(L, root))

# ---------------- pages ----------------
def thumb(img):
    return img.replace("img/p/", "img/t/")

def nb_img(p, pre, cls=""):
    return f'<span class="nb-poly {cls}"><img src="{pre}{thumb(p["img"])}" alt="" loading="lazy"></span>'

def build_home(L):
    U = SI.UI[L]; V = NV.N[L]; pre = "" if L == "fr" else "../"
    by = {p["name"]: p for p in P}
    _ALT = {"Calculatrice scientifique Casio fx-82MS": "Calculatrice Casio fx-991ES Plus", "Kit de traçage 4 pièces 30 cm Maped": "Kit de traçage Deli",
            "Dictionnaire Le Robert Micro": "Larousse — Mon premier dictionnaire", "Organiseur de bureau en bois 6 cases": "Ensemble de bureau Office Set ARK", "Crayons de couleur Maped Color'Peps — 12": "Crayons de couleur Maped", "Feutres de coloriage Maped — 24": "Feutres de coloriage Maped 12 couleurs", "Set de 12 pinceaux synthétiques": "Pinceaux Arco 6 pièces", "Cartable primaire 2 compartiments": "Cartable Be-Bolol", "Trousse garnie 25 pièces": "Trousse M-School", "Cartable à roulettes 18 pouces": "Cartable UniStyl Trolley 3 pièces", "Bâton de colle UHU Stic 21 g": "Colle en bâton UHU 21 g"}
    g = lambda n: by[_ALT[n]] if n in _ALT and _ALT[n] in by else by[n]
    # bandeaux (slider)
    s1 = (f'<div class="hero__slide nb-s1 is-active"><div class="nb-s1__blob"></div>'
          f'<div class="nb-s__text"><p class="nb-k">{E(V["s1_k"])}</p><h2 class="nb-t">{E(V["s1_t"])}</h2><p class="nb-y">{E(V["s1_y"])}</p><p class="nb-ribbon">{E(V["s1_b"])}</p>'
          f'<a class="nb-cta" href="boutique.html">{E(V["order_now"])}</a></div>'
          f'<div class="nb-collage">{nb_img(g("Cartable primaire 2 compartiments"), pre, "c1")}{nb_img(g("Crayons de couleur Maped Color'Peps — 12"), pre, "c2")}{nb_img(g("Cahier Essentiel 96 pages 10/10 A5 (17×22)"), pre, "c3")}{nb_img(g("Calculatrice scientifique Casio fx-82MS"), pre, "c4")}</div></div>')
    chips = "".join(f'<span class="nb-chip">{ic(sv[1], 16)} {E(sv[5][L][0])}</span>' for sv in ([x for x in SI.SERVICES if x[5]["fr"][0].startswith("Titre de propriété")] + [x for x in SI.SERVICES if x[6]])[:6])
    s2 = (f'<div class="hero__slide nb-s2"><div class="nb-s__text"><p class="nb-k">{E(V["s2_k"])}</p><h2 class="nb-t">{E(V["s2_t"])}</h2><p class="nb-y">{E(V["s2_y"])}</p>'
          f'<a class="nb-cta" href="services.html">{E(V["s2_b"])}</a></div><div class="nb-chips">{chips}</div></div>')
    s3 = (f'<div class="hero__slide nb-s3"><div class="nb-s__text"><p class="nb-k">{E(V["s3_k"])}</p><h2 class="nb-t">{E(V["s3_t"])}</h2><p class="nb-y">{E(V["s3_y"])}</p>'
          f'<a class="nb-cta nb-cta--wa js-wa" href="{wa(U["wa_list"])}" target="_blank" rel="noopener">{ic("whatsapp", 18)} {E(V["s3_b"])}</a></div>'
          f'<div class="nb-collage">{nb_img(g("Trousse garnie 25 pièces"), pre, "c1")}{nb_img(g("Kit de traçage 4 pièces 30 cm Maped"), pre, "c2")}{nb_img(g("Bâton de colle UHU Stic 21 g"), pre, "c3")}{nb_img(g("Feutres de coloriage Maped — 24"), pre, "c4")}</div></div>')
    hero = (f'<div class="hero nb-hero" data-slider><div class="hero__track">{s1}{s2}{s3}</div><button class="hero__nav hero__nav--prev" aria-label="{E(U["prev"])}">{ic("left", 22)}</button>'
            f'<button class="hero__nav hero__nav--next" aria-label="{E(U["next"])}">{ic("chevron", 22)}</button><div class="hero__dots nb-dots"><button class="is-active"></button><button></button><button></button></div></div>')
    box = f'<aside class="nb-cats"><h2 class="nb-cats__title">{E(V["cats_title"])}</h2><div class="js-catmenu"></div></aside>'
    top = f'<section class="nb-top">{box}{hero}</section>'
    # tuiles colorées
    def tile(cls, href, title, img, btn, ext=""):
        im = nb_img(img, pre, "nb-tile__img") if img else ""
        return f'<a class="nb-tile {cls}" href="{href}"{ext}><span class="nb-tile__orb" aria-hidden="true"></span><span class="nb-tile__t">{title}</span><span class="nb-tile__b">{E(btn)} <span class="nb-tile__arr" aria-hidden="true">→</span></span>{im}</a>'
    tiles = (f'<a class="nb-tile nb-tile--svc" href="services.html"><span class="nb-tile__orb" aria-hidden="true"></span><img class="nb-tile__logo" src="{pre}img/emblem-navy.svg" alt=""><span class="nb-tile__t">{E(V["t_svc"])}</span><span class="nb-tile__s">{E(V["t_svc_s"])}</span></a>'
             + tile("nb-tile--dark", cslug("Scolaire") + ".html", E(V["t_sco"]), g("Cartable à roulettes 18 pouces"), V["shop_now"])
             + tile("nb-tile--orange", cslug("Livres") + ".html", E(V["t_liv"]), g("Dictionnaire Le Robert Micro"), V["shop_now"])
             + tile("nb-tile--blue", cslug("Bureau & Organisation") + ".html", E(V["t_bur"]), g("Organiseur de bureau en bois 6 cases"), V["shop_now"])
             + tile("nb-tile--red", cslug("Beaux-arts & Loisirs créatifs") + ".html", E(V["t_art"]), g("Set de 12 pinceaux synthétiques"), V["shop_now"])
             + f'<a class="nb-tile nb-tile--list js-wa" href="{wa(U["wa_list"])}" target="_blank" rel="noopener"><span class="nb-tile__orb" aria-hidden="true"></span><span class="nb-tile__t">{E(V["t_list"])}</span><span class="nb-tile__b">{ic("whatsapp", 14)} {E(V["t_list_b"])}</span></a>')
    tiles = f'<section class="nb-tiles">{tiles}</section>'
    def band(title, sub, link, items):
        items = [p for p in items if p.get("real") and p.get("photo")]
        if not items: return ""
        more = f'<a class="nb-more" href="{link}">{E(V["more"])} {ic("chevron", 14)}</a>' if link else ""
        return (f'<section class="nb-block"><header class="nb-band"><h2>{E(title)}</h2><p>{E(sub)}</p>{more}'
                f'<span class="nb-arrows"><button class="carousel-btn" data-dir="-1" aria-label="{E(U["prev"])}">{ic("left", 18)}</button><button class="carousel-btn" data-dir="1" aria-label="{E(U["next"])}">{ic("chevron", 18)}</button></span></header>'
                f'<div class="woocommerce"><ul class="products carousel">{"".join(card(p, L, pre) for p in items)}</ul></div></section>')
    body = '<div class="nb-wrap">' + top + tiles
    order = ["Écriture & Correction", "Cahiers", "Classement & Archivage", "Scolaire", "Bureau & Organisation", "Livres", "Papeterie & blocs-notes", "Beaux-arts & Loisirs créatifs", "Informatique & Consommables", "Jeux & Loisirs"]
    for i, t in enumerate(order):
        items = [p for p in P if p["top"] == t]
        items = sorted(items, key=lambda p: (not p["featured"]))[:10]
        body += band(cname(t, L).upper() if L != "ar" else cname(t, L), V["sec_sub"].format(c=cname(t, L)), cslug(t) + ".html", items)
        if i == 1:
            feat = [x for x in SI.SERVICES if x[6]][:8]
            body += (f'<section class="nb-block"><header class="nb-band"><h2>{E(V["services_sec"].upper() if L != "ar" else V["services_sec"])}</h2><p>{E(V["services_sub"])}</p>'
                     f'<a class="nb-more" href="services.html">{E(V["more"])} {ic("chevron", 14)}</a></header><div class="svc-grid">{services_cards(L, feat, pre)}</div></section>')
            body += f'<section class="nb-block nb-block--packs">{packs_block(L, pre)}</section>'
        if i == 3:
            news = [p for p in P if p["new"]]
            body += band(V["new_sec"].upper() if L != "ar" else V["new_sec"], V["new_sub"], "boutique.html", news)
    body += band(V["promo_sec"].upper() if L != "ar" else V["promo_sec"], V["promo_sub"], "", [p for p in P if p["sale"]])
    F = FIND[L]
    emb = f"https://maps.google.com/maps?q={SHOP_LL}&z=17&hl={L}&output=embed"
    body += (f'<section class="nb-block findus" id="nous-trouver"><div class="findus__map"><iframe src="{E(emb)}" title="{E(F["t"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
             f'<a class="findus__overlay" href="{E(PLACE_URL)}" target="_blank" rel="noopener" aria-label="{E(F["see"])}"></a></div>'
             f'<div class="findus__info"><span class="findus__pin">{ic("pin", 30)}</span><h2>{E(F["t"])}</h2><p class="findus__addr">{E(F["s"])}</p><p class="findus__near">{E(F["near"])}</p>'
             f'<a class="findus__go" href="{E(GO_URL)}" target="_blank" rel="noopener">{ic("send", 20)} {E(F["go"])}</a>'
             f'<div class="findus__row"><a class="findus__alt" href="{E(PLACE_URL)}" target="_blank" rel="noopener">{ic("pin", 16)} {E(F["see"])}</a>'
             f'<a class="findus__alt" href="tel:{PHONE.replace(" ", "").replace("-", "")}">{ic("phone", 16)} {E(F["call"])}</a></div></div></section>')
    body += '</div>'
    page(L, "index.html", U["brand"], body, "index.html")

def build_home_old(L):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    slides = [("hero_title", "hero_text", "hero_btn", "boutique.html", 0), ("hero2_title", "hero2_text", "hero2_btn", "services.html", 1), ("hero3_title", "hero3_text", "hero3_btn", wa(U["wa_list"]), 2)]
    sl = "".join(f'<div class="hero__slide hero__slide--{k}{" is-active" if k == 0 else ""}">' + (f'<img class="hero__photo" src="{pre}img/emblem.svg" alt="" aria-hidden="true">' if k == 0 else '<div class="hero__art" aria-hidden="true"><span></span><span></span><span></span></div>') +
                 f'<div class="hero__content" data-kicker="{E(U["hero_kicker"])}"><h2 class="hero__title{" hero__title--brand" if k == 0 else ""}">{E(U[t])}</h2><p class="hero__text">{E(U[x])}</p><a class="btn btn--accent{" js-wa" if "wa.me" in h else ""}" href="{h}"{" target=_blank rel=noopener" if "wa.me" in h else ""}>{E(U[b])}</a></div></div>'
                 for t, x, b, h, k in slides)
    hero = (f'<div class="hero" data-slider><div class="hero__track">{sl}</div><button class="hero__nav hero__nav--prev" aria-label="{E(U["prev"])}">{ic("left", 22)}</button>'
            f'<button class="hero__nav hero__nav--next" aria-label="{E(U["next"])}">{ic("chevron", 22)}</button><div class="hero__dots"><button class="is-active"></button><button></button><button></button></div></div>')
    promos = (f'<div class="promos"><a class="promo promo--1" href="services.html"><span class="promo__body"><span class="promo__title">{E(U["promo1_t"])}</span><span class="promo__text">{E(U["promo1_s"])}</span><span class="promo__btn">{E(U["promo1_b"])} {ic("chevron", 14)}</span></span></a>'
              f'<a class="promo promo--2 js-wa" href="{wa(U["wa_list"])}" target="_blank" rel="noopener"><span class="promo__body"><span class="promo__title">{E(U["promo2_t"])}</span><span class="promo__text">{E(U["promo2_s"])}</span><span class="promo__btn">{E(U["promo2_b"])} {ic("chevron", 14)}</span></span></a></div>')
    top = f'<section class="home-top container"><aside class="catbox"><div class="js-catmenu"></div></aside>{hero}{promos}</section>'
    feats = "".join(f'<div class="feature"><span class="feature__icon">{ic(i, 26)}</span><div><strong>{E(U[a])}</strong><small>{E(U[b])}</small></div></div>' for i, a, b in [("truck", "f1", "f1s"), ("cash", "f2", "f2s"), ("monitor", "f3", "f3s"), ("shield", "f4", "f4s")])
    feats = f'<section class="features container">{feats}</section>'
    ray = "".join(f'<a class="rayon" href="{cslug(t)}.html"><span class="rayon__media"><img src="{pre}{cat_first_img(t)}" alt="" loading="lazy"></span><span class="rayon__name">{E(cname(t, L))}</span><span class="rayon__count">{sum(1 for p in P if p["top"] == t)} {E(U["products"])}</span></a>' for t in TOPS)
    ray = f'<section class="rayons container"><header class="psection__head"><div><h2 class="psection__title">{E(U["nos_rayons"])}</h2><p class="psection__sub">{E(U["nos_rayons_sub"])}</p></div><div class="psection__actions"><a class="psection__all" href="boutique.html">{E(U["all_shop"])} {ic("chevron", 14)}</a></div></header><div class="rayons__grid rayons__grid--9">{ray}</div></section>'
    feat_svc = [s for s in SI.SERVICES if s[6]][:8]
    svc = (f'<section class="svc-home container"><header class="psection__head"><div><h2 class="psection__title">{E(U["svc_title"])}</h2><p class="psection__sub">{E(U["svc_sub"])}</p></div>'
           f'<div class="psection__actions"><a class="psection__all" href="services.html">{E(U["see_all"])} {ic("chevron", 14)}</a></div></header><div class="svc-grid">{services_cards(L, feat_svc, pre)}</div></section>')
    news = [p for p in P if p["new"]] + [p for p in P if not p["new"]][::-1][:4]
    favs, groups = [], {}
    for p in P:
        if p["featured"]: groups.setdefault(p["top"], []).append(p)
    while groups:
        for k in list(groups):
            favs.append(groups[k].pop(0))
            if not groups[k]: del groups[k]
    listcta = (f'<section class="listcta container"><div class="listcta__inner"><div class="listcta__icon">{ic("list", 40)}</div><div class="listcta__text"><h2>{E(U["list_t"])}</h2><p>{E(U["list_s"])}</p></div>'
               f'<a class="btn btn--whatsapp js-wa" href="{wa(U["wa_list"])}" target="_blank" rel="noopener">{ic("whatsapp", 20)} {E(U["list_b"])}</a></div></section>')
    body = top + feats + ray + svc + section(L, U["new"], U["new_sub"], "boutique.html", news[:12], pre) + section(L, U["fav"], U["fav_sub"], "", favs[:12], pre)
    for i, t in enumerate(TOPS):
        desc = catalog.CAT_DESC[t] if L == "fr" else IP.CAT_DESC[t][0 if L == "en" else 1]
        body += section(L, cname(t, L), desc, cslug(t) + ".html", [p for p in P if p["top"] == t][:10], pre)
        if i == 1: body += listcta
    body += section(L, U["promo"], U["promo_sub"], "", [p for p in P if p["sale"]], pre)
    page(L, "index.html", U["brand"], body, "index.html")

def pager(L, base, n, cur):
    if n < 2: return ""
    U = SI.UI[L]
    links = "".join(f'<li>{"<span class=current>" + str(i) + "</span>" if i == cur else f"<a href={base}{"" if i == 1 else "-" + str(i)}.html>{i}</a>"}</li>' for i in range(1, n + 1))
    return f'<nav class="woocommerce-pagination"><ul class="page-numbers">{links}</ul></nav>'

def build_listing(L, base, title, desc, items, chips=""):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    pages = max(1, -(-len(items) // PER_PAGE))
    for k in range(pages):
        chunk = items[k * PER_PAGE:(k + 1) * PER_PAGE]
        a, b = k * PER_PAGE + 1, k * PER_PAGE + len(chunk)
        count = f'{len(items)} {U["products"]}' if pages == 1 else f'{a}–{b} {U["of"]} {len(items)}'
        body = (f'<div class="container shop-wrap has-sidebar"><aside class="shop-sidebar"><div class="catbox catbox--static"><h2 class="catbox__title">{ic("grid", 18)} {E(U["cats"])}</h2><div class="js-catmenu"></div></div></aside>'
                f'<div class="shop-content"><nav class="woocommerce-breadcrumb"><a href="index.html">{E(U["home"])}</a><span class="sep">/</span>{E(title)}</nav>'
                f'<h1 class="page-title">{E(title)}</h1>' + (f'<p class="term-desc">{E(desc)}</p>' if desc else "") + chips +
                f'<p class="woocommerce-result-count">{count}</p><div class="woocommerce"><ul class="products columns-4">{"".join(card(p, L, pre) for p in chunk)}</ul></div>{pager(L, base, pages, k + 1)}</div></div>')
        page(L, base + ("" if k == 0 else f"-{k + 1}") + ".html", title + ("" if k == 0 else f" – {U['page_x']} {k + 1}"), body, base + ".html", desc)

def rgrid(L, names, pre, sub=True):
    U = SI.UI[L]
    def n_of(x): return sum(1 for p in P if (p["sub"] if sub else p["top"]) == x)
    return ('<div class="rgrid">' + "".join(
        f'<a class="rtile" href="{cslug(x)}.html"><span class="rtile__img"><img src="{pre}{cat_first_img(x)}" alt="" loading="lazy" width="200" height="200"></span>'
        f'<span class="rtile__name">{E(cname(x, L))}</span><span class="rtile__n">{n_of(x)} {E(U["products"])}</span></a>' for x in names) + '</div>')

def gtiles(L, ents, pre):
    U = SI.UI[L]
    def img(e):
        if isinstance(e, tuple) and e[4]: return cat_first_img(e[4])
        for x in esubs(e):
            if cat_first_img(x): return cat_first_img(x)
        return ""
    def n(e): return sum(1 for p in P if p["sub"] in esubs(e))
    return ('<div class="rgrid">' + "".join(
        f'<a class="rtile" href="{eslug(e)}.html">' + (f'<span class="rtile__img"><img src="{pre}{img(e)}" alt="" loading="lazy" width="200" height="200"></span>' if img(e) else f'<span class="rtile__img rtile__img--icon">{ic("grid", 40)}</span>') +
        f'<span class="rtile__name">{E(ename(e, L))}</span><span class="rtile__n">{n(e)} {E(U["products"])}</span></a>' for e in ents) + '</div>')

def build_groups(L):
    pre = "" if L == "fr" else "../"; k = {"fr": 0, "en": 1, "ar": 2}[L]
    for g in GROUPS:
        build_listing(L, gslug(g), gname(g, L), g[4][k], [p for p in P if p["sub"] in gsubs(g)], gtiles(L, g[5], pre))
        for e in g[5]:
            if isinstance(e, tuple) and not e[4] and len(e[3]) > 1:
                back = (f'<div class="subchips"><a href="{gslug(g)}.html">← {E(gname(g, L))}</a>' +
                        "".join(f'<a href="{cslug(x)}.html">{E(cname(x, L))}</a>' for x in e[3]) + '</div>')
                build_listing(L, eslug(e), ename(e, L), "", [p for p in P if p["sub"] in e[3]], back if len(e[3]) > 1 else back)

SOON = {"fr": ("Bientôt en ligne", "Ces articles sont disponibles en magasin. Demandez-les sur WhatsApp : nous vous répondons avec les modèles et les prix.", "Demander sur WhatsApp"),
        "en": ("Coming soon online", "These items are available in store. Ask us on WhatsApp for models and prices.", "Ask on WhatsApp"),
        "ar": ("قريباً على الموقع", "هذه المنتجات متوفرة في المتجر. اسألنا عبر واتساب عن الأنواع والأسعار.", "اسأل عبر واتساب")}

def build_empty_subs(L):
    known = {x for t in TOPS for x in SUBS[t]}
    done = set()
    for g in GROUPS:
        for e in g[5]:
            for x in esubs(e):
                if x in known or x in done: continue
                done.add(x); t, d, b = SOON[L]
                box = (f'<div class="soon-box">{ic("store", 34)}<h2>{E(t)}</h2><p>{E(d)}</p>'
                       f'<a class="btn btn--whatsapp js-service" href="#" data-service="{E(cname(x, L))}">{ic("whatsapp", 18)} {E(b)}</a>'
                       f'<a class="soon-box__back" href="{gslug(g)}.html">← {E(gname(g, L))}</a></div>')
                build_listing(L, cslug(x), cname(x, L), "", [], box)

def build_categories(L):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    build_groups(L)
    build_empty_subs(L)
    _gt = ('<div class="rgrid">' + "".join(
        f'<a class="rtile" href="{gslug(g)}.html"><span class="rtile__img rtile__img--icon">{ic(g[3], 54)}</span>'
        f'<span class="rtile__name">{E(gname(g, L))}</span><span class="rtile__n">{sum(1 for p in P if p["sub"] in gsubs(g))} {E(U["products"])}</span></a>' for g in GROUPS) + '</div>')
    build_listing(L, "boutique", U["shop"], "", P, _gt)
    for t in TOPS:
        chips = rgrid(L, SUBS[t], pre)
        desc = catalog.CAT_DESC[t] if L == "fr" else IP.CAT_DESC[t][0 if L == "en" else 1]
        build_listing(L, cslug(t), cname(t, L), desc, [p for p in P if p["top"] == t], chips)
        for s in SUBS[t]:
            back = f'<div class="subchips"><a href="{cslug(t)}.html">← {E(cname(t, L))}</a>' + "".join(f'<a href="{cslug(x)}.html" class="{"is-active" if x == s else ""}">{E(cname(x, L))}</a>' for x in SUBS[t]) + '</div>'
            build_listing(L, cslug(s), cname(s, L), "", [p for p in P if p["sub"] == s], back)

def variants_block(p, L, pre):
    if "variants" not in p: return ""
    V0 = p["variants"][0]; LB = VR.LABELS[L]
    btns = "".join(f'<button type="button" class="swatch{" is-active" if i == 0 else ""}" style="--c:{VR.COLORS[v["color"]][3]}" data-img="{pre}{v["img"]}" data-color="{E(cl(v["color"], L))}" data-sku="{v["sku"]}" aria-label="{E(cl(v["color"], L))}" title="{E(cl(v["color"], L))}"><span></span></button>' for i, v in enumerate(p["variants"]))
    return f'<div class="variants" data-variants><p class="variants__label">{E(LB["color"])} : <strong data-vlabel>{E(cl(V0["color"], L))}</strong></p><div class="swatches" role="radiogroup" aria-label="{E(LB["pick"])}">{btns}</div></div>'

def build_products(L):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    EXTRA = {"fr": "Disponible en magasin et livré partout au Maroc. Remises pour les écoles et les entreprises sur demande WhatsApp.",
             "en": "Available in store and delivered all over Morocco. Discounts for schools and companies on request via WhatsApp.",
             "ar": "متوفر في المتجر ويتم توصيله إلى جميع أنحاء المغرب. تخفيضات للمدارس والمقاولات عند الطلب عبر واتساب."}[L]
    for p in P:
        n = pname(p, L)
        if p["sale"]:
            pct = round(100 - float(p["sale"]) / float(p["regular"]) * 100)
            price = f'<del>{money(p["regular"], L)}</del> <ins>{money(p["sale"], L)}</ins>'; on = f'<span class="onsale" dir="ltr">-{pct}%</span>'
        else:
            price, on = money(p["regular"], L), ""
        if soon(p): price, on = soon_price(L), ""
        sim = [q for q in P if q["sub"] == p["sub"] and q is not p][:4] or [q for q in P if q["top"] == p["top"] and q is not p][:4]
        body = (f'<div class="container shop-wrap"><div class="shop-content"><nav class="woocommerce-breadcrumb"><a href="index.html">{E(U["home"])}</a><span class="sep">/</span><a href="{cslug(p["top"])}.html">{E(cname(p["top"], L))}</a><span class="sep">/</span><a href="{cslug(p["sub"])}.html">{E(cname(p["sub"], L))}</a></nav>'
                f'<div class="product single"><div class="pgrid"><div class="pgal">{on}<img id="pimg" src="{pre}{p["img"]}" alt="{E(n)}" width="600" height="600"></div>'
                f'<div class="summary"><h1 class="product_title">{E(n)}</h1><p class="price">{price}</p><div class="pshort"><p>{E(pshort(p, L))}</p></div>{variants_block(p, L, pre)}' + (
                f'<a class="btn btn--whatsapp btn--block js-order-single" href="#" data-name="{E(n)}" data-price="{E(SOON_T[L])}">{ic("whatsapp", 20)} {E(ASK_T[L])}</a>' if soon(p) else
                f'<p class="stock in-stock">{E(U["in_stock"])}</p>'
                f'<form class="cart" onsubmit="return false"><div class="quantity"><label class="screen-reader-text" for="qty">{E(U["qty"])}</label><input id="qty" class="qty" type="number" min="1" value="1"></div>'
                f'<button type="button" class="single_add_to_cart_button button alt js-add js-add-single" {cdata(p, n, pre, (p["variants"][0]["img"] if "variants" in p else None), (p["variants"][0]["sku"] if "variants" in p else None))}>{ic("cart", 18)} {E(PJ.J[L]["add"])}</button></form>'
                f'<a class="btn btn--whatsapp btn--block js-order-single" href="#" data-name="{E(n)}" data-price="{money(p["sale"] or p["regular"], L)}">{ic("whatsapp", 20)} {E(U["order_wa"])}</a>') +
                f'<div class="product_meta"><span>{E(U["ref"])} : <span id="psku">{p["sku"]}</span></span> · <span>{E(U["category"])} : <a href="{cslug(p["sub"])}.html">{E(cname(p["sub"], L))}</a></span></div></div></div>'
                f'<div class="pdesc"><h2>{E(U["desc"])}</h2><p>{E(pshort(p, L))}</p><p>{E(EXTRA)}</p></div></div>'
                f'<section class="related products"><h2>{E(U["similar"])}</h2><div class="woocommerce"><ul class="products columns-4">{"".join(card(q, L, pre) for q in sim)}</ul></div></section></div></div>')
        page(L, p["slug"] + ".html", n, body, cslug(p["top"]) + ".html", pshort(p, L))

def build_services(L):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    groups = ""
    for gid, icon, title, sub in SI.SERVICE_GROUPS:
        items = [s for s in SI.SERVICES if s[0] == gid]
        groups += f'<section class="svc-group" id="{gid}"><header class="svc-group__head"><span class="svc-group__icon">{ic(icon, 28)}</span><div><h2>{E(title[L])}</h2><p>{E(sub[L])}</p></div></header><div class="svc-grid">{services_cards(L, items, pre)}</div></section>'
        if gid == "web": groups = groups[:groups.rfind('<div class="svc-grid">')] + packs_block(L, pre) + groups[groups.rfind('<div class="svc-grid">'):]
    nav = "".join(f'<a href="#{gid}">{ic(icon, 16)} {E(title[L])}</a>' for gid, icon, title, sub in SI.SERVICE_GROUPS)
    steps = "".join(f'<li><span class="step__n">{i + 1}</span><p>{E(t)}</p></li>' for i, t in enumerate(U["svc_steps"]))
    body = (f'<section class="svc-hero"><div class="container"><p class="svc-hero__kicker">{E(U["brand"])}</p><h1>{E(U["svc_title"])}</h1><p>{E(U["svc_sub"])}</p><nav class="svc-nav">{nav}</nav></div></section>'
            f'<div class="container svc-page">{groups}<section class="svc-how"><h2>{E(U["svc_how"])}</h2><ol class="steps">{steps}</ol><p class="svc-note">{E(U["svc_note"])}</p>'
            f'<a class="btn btn--whatsapp js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener">{ic("whatsapp", 20)} {E(U["write_wa"])}</a></section></div>')
    page(L, "services.html", U["services"], body, "services.html", U["svc_sub"])

def build_pages(L):
    U = SI.UI[L]; pre = "" if L == "fr" else "../"
    for slug_, data in SI.PAGES.items():
        t, h = data[L]
        page(L, slug_ + ".html", t, f'<div class="container page-wrap"><header class="page-head"><h1 class="page-title">{E(t)}</h1></header><div class="entry-content">{h}</div></div>')
    contact = (f'<div class="container page-wrap"><header class="page-head"><h1 class="page-title">{E(U["contact"])}</h1></header><div class="entry-content"><div class="contact-card">'
               f'<div class="contact-card__row"><span class="contact-card__icon">{ic("phone", 20)}</span><div><small>{E(U["phone"])}</small><strong><a href="tel:{PHONE.replace(" ", "").replace("-", "")}" dir="ltr">{PHONE}</a></strong></div></div>'
               f'<div class="contact-card__row js-email" hidden><span class="contact-card__icon">{ic("mail", 20)}</span><div><small>E-mail</small><strong><a href="#"></a></strong></div></div>'
               f'<div class="contact-card__row"><span class="contact-card__icon">{ic("building", 20)}</span><div><small>{E(U["address_l"])}</small><strong>{E(U["address_v"])}</strong> · <a href="{PLACE_URL}" target="_blank" rel="noopener">{E(U["map"])}</a></div></div>'
               f'<div class="contact-card__row"><span class="contact-card__icon">{ic("clock", 20)}</span><div><small>{E(U["hours"])}</small><strong>{E(U["hours_v"])}</strong></div></div>'
               f'<a class="btn btn--whatsapp js-wa" href="{wa(U["wa_q"])}" target="_blank" rel="noopener">{ic("whatsapp", 20)} {E(U["write_wa"])}</a></div></div></div>')
    from urllib.parse import quote_plus
    ORIG, DEST = "Marjane Route de Casablanca, Marrakech", SHOP_LL
    emb = f"https://maps.google.com/maps?saddr={quote_plus(ORIG)}&daddr={quote_plus(DEST)}&hl={L}&output=embed"
    dirs = f"https://www.google.com/maps/dir/?api=1&origin={quote_plus(ORIG)}&destination={quote_plus(DEST)}&travelmode=driving"
    plan = (f'<section class="plan container"><header class="plan__head"><h2>{E(U["plan_t"])}</h2><p>{E(U["plan_s"])}</p></header>'
            f'<div class="plan__grid"><div class="plan__map"><iframe src="{E(emb)}" title="{E(U["plan_t"])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'
            f'<div class="plan__info"><ol class="plan__route"><li><span class="plan__dot plan__dot--a">A</span>{E(U["plan_from"])}</li><li><span class="plan__dot plan__dot--b">B</span>{E(U["plan_to"])}</li></ol>'
            f'<a class="btn btn--primary plan__btn" href="{E(dirs)}" target="_blank" rel="noopener">{ic("send", 18)} {E(U["plan_b"])}</a>'
            f'<a class="btn btn--whatsapp plan__btn plan__go" href="{E(GO_URL)}" target="_blank" rel="noopener">{ic("pin", 18)} {E(GO_T[L])}</a>'
            f'<a class="plan__link" href="{E(PLACE_URL)}" target="_blank" rel="noopener">{E(U["plan_o"])}</a>'
            f'<p class="plan__hours">{ic("clock", 16)} {E(U["hours_v"])}</p></div></div></section>')
    VT = {"fr": ("Vidéo : comment venir à pied", "Départ : agence Crédit du Maroc — environ 2 minutes à pied, 8 étapes. Suivez les flèches bleues.", "Choisir la langue de la vidéo"),
          "en": ("Video: how to walk to us", "Start: Crédit du Maroc branch — about a 2-minute walk, 8 steps. Follow the blue arrows.", "Choose the video language"),
          "ar": ("فيديو: كيف تصل إلينا مشياً", "نقطة الانطلاق: وكالة مصرف المغرب (Crédit du Maroc) — حوالي دقيقتين مشياً، 8 مراحل. اتبع الأسهم الزرقاء.", "اختر لغة الفيديو")}
    vids = [("francais", "Français", "fr"), ("english", "English", "en"), ("darija", "الدارجة", "ar")]
    cur = {"fr": "francais", "en": "english", "ar": "darija"}[L]
    tabs = "".join(f'<button type="button" class="vtab{" is-on" if k == cur else ""}" data-vsrc="{pre}video/itineraire-{k}.mp4" data-vposter="{pre}video/poster-{k}.jpg" lang="{lg}" aria-pressed="{"true" if k == cur else "false"}">{E(n)}</button>' for k, n, lg in vids)
    video = (f'<section class="vroute container" id="video"><header class="plan__head"><h2>{ic("play", 22)} {E(VT[L][0])}</h2><p>{E(VT[L][1])}</p></header>'
             f'<div class="vroute__tabs" role="group" aria-label="{E(VT[L][2])}">{tabs}</div>'
             f'<div class="vroute__frame"><video id="vroute" controls playsinline preload="none" poster="{pre}video/poster-{cur}.jpg"><source src="{pre}video/itineraire-{cur}.mp4" type="video/mp4"></video></div></section>')
    contact = contact + plan + video
    page(L, "contact.html", U["contact"], contact, "contact.html")
    page(L, "recherche.html", U["search"], f'<div class="container shop-wrap"><div class="shop-content"><h1 class="page-title" id="titre-recherche">{E(U["search"])}</h1><div class="woocommerce"><ul class="products columns-4" id="resultats"></ul></div><div class="svc-grid" id="resultats-services"></div></div></div>')
    # index de recherche
    idx = [{"t": "p", "n": pname(p, L), "u": p["slug"] + ".html", "i": thumb(p["img"]), "id": p["sku"], "v": f'{float(p["sale"] or p["regular"]):.2f}', "p": SOON_T[L] if soon(p) else money(p["sale"] or p["regular"], L),
            "o": money(p["regular"], L) if p["sale"] and not soon(p) else "", "c": slug(p["top"]), "k": cname(p["top"], L) + " " + cname(p["sub"], L) + " " + p["name"] + " " + " ".join(cl(v["color"], L) + " " + cl(v["color"], "fr") for v in p.get("variants", []))} for p in P]
    idx += [{"t": "s", "n": s[5][L][0], "d": s[5][L][1], "k": s[5]["fr"][0]} for s in SI.SERVICES]
    from web_services import PACKS
    idx += [{"t": "s", "n": d_[L][0], "d": d_[L][1] + " " + ", ".join(d_[L][2]), "p": pr[{"fr": 0, "en": 1, "ar": 2}[L]], "k": d_["fr"][0] + " pack"} for _, _, pr, _, d_ in PACKS]
    d = OUT if L == "fr" else os.path.join(OUT, L)
    json.dump(idx, open(os.path.join(d, "recherche.json"), "w"), ensure_ascii=False)

def build_shop_pages(L):
    U = SI.UI[L]; J = PJ.J[L]
    steps = lambda n: '<ol class="costeps">' + "".join(f'<li class="{"is-done" if i < n else ""}{" is-on" if i == n else ""}"><span>{i + 1}</span>{E(t)}</li>' for i, t in enumerate([J["step1"], J["step2"], J["step3"]])) + '</ol>'
    # panier
    body = (f'<div class="container page-wrap co"><header class="page-head"><h1 class="page-title">{E(J["cart_t"])}</h1></header>{steps(0)}'
            f'<div class="co__grid"><div class="co__main"><div id="cart-box" class="cartbox"></div></div>'
            f'<aside class="co__side"><div class="cosum"><h2>{E(J["summary"])}</h2><div id="cart-sum"></div>'
            f'<a class="btn btn--primary btn--block" id="go-checkout" href="commande.html">{ic("lock", 18)} {E(J["checkout"])}</a>'
            f'<a class="cosum__more" href="boutique.html">{E(J["continue_"])}</a>{pay_badges(L)}</div></aside></div></div>')
    page(L, "panier.html", J["cart_t"], body)
    # bon de commande
    def radio(name, val, icon, t, d, checked=False, extra=""):
        return (f'<label class="opt" data-opt="{val}"{extra}><input type="radio" name="{name}" value="{val}"{" checked" if checked else ""}>'
                f'<span class="opt__ic">{ic(icon, 22)}</span><span class="opt__t"><strong>{E(t)}</strong><small>{E(d)}</small></span></label>')
    fld = lambda n, t, typ="text", req=True, full=False, auto="": f'<label class="fld{" fld--full" if full else ""}"><span>{E(t)}{" *" if req else ""}</span><input name="{n}" type="{typ}"{" required" if req else ""}{f" autocomplete={chr(34)}{auto}{chr(34)}" if auto else ""}></label>'
    form = (f'<form id="coform" class="coform" novalidate>'
            f'<section class="cobox"><h2>{ic("user", 20)} {E(J["your_info"])}</h2><div class="fgrid">{fld("name", J["f_name"], auto="name")}{fld("phone", J["f_phone"], "tel", auto="tel")}'
            f'{fld("city", J["f_city"], auto="address-level2")}{fld("addr", J["f_addr"], auto="street-address")}'
            f'<label class="fld fld--full"><span>{E(J["f_note"])}</span><textarea name="note" rows="2"></textarea></label></div></section>'
            f'<section class="cobox"><h2>{ic("truck", 20)} {E(J["ship_t"])}</h2><div class="opts">'
            f'{radio("ship", "home", "home2", J["ship_home"], J["ship_home_d"], True)}{radio("ship", "store", "store", J["ship_store"], J["ship_store_d"])}</div></section>'
            f'<section class="cobox"><h2>{ic("card", 20)} {E(J["pay_t"])}</h2><div class="opts">'
            f'{radio("pay", "cod", "cash", J["pay_cod"], J["pay_cod_d"], True)}'
            f'{radio("pay", "card", "card", J["pay_card"], J["pay_card_d"], extra=" data-card")}'
            f'{radio("pay", "bank", "bank", J["pay_bank"], J["pay_bank_d"])}'
            f'{radio("pay", "store", "store", J["pay_store"], J["pay_store_d"], extra=" data-storeonly")}</div>'
            f'<p class="co__secure">{ic("lock", 16)} {E(J["sec_d"])}</p></section>'
            f'<label class="co__accept"><input type="checkbox" name="cgv" required> <span>{E(J["accept"])} — <a href="conditions-generales-de-vente.html" target="_blank">{E(U["terms"])}</a></span></label>'
            f'<p class="co__err" id="co-err" hidden>{E(J["required"])}</p>'
            f'<button class="btn btn--primary btn--block co__submit" type="submit">{ic("check", 18)} {E(J["confirm"])}</button></form>')
    done = (f'<div id="codone" class="codone" hidden><span class="codone__ic">{ic("check", 34)}</span><h2>{E(J["thanks"])}</h2><p class="codone__no">{E(J["order_no"])} <strong id="co-no" dir="ltr"></strong></p><p>{E(J["thanks_d"])}</p>'
            f'<div id="co-bank" class="cobank" hidden></div>'
            f'<a class="btn btn--whatsapp btn--block" id="co-wa" href="#" target="_blank" rel="noopener">{ic("whatsapp", 20)} {E(J["send_wa"])}</a>'
            f'<a class="btn btn--primary btn--block" id="co-pay" href="#" target="_blank" rel="noopener" hidden>{ic("card", 20)} {E(J["pay_now"])}</a></div>')
    body = (f'<div class="container page-wrap co"><header class="page-head"><h1 class="page-title">{E(J["order_t"])}</h1></header>{steps(1)}'
            f'<div class="co__grid"><div class="co__main">{form}{done}</div><aside class="co__side"><div class="cosum"><h2>{E(J["summary"])}</h2><div id="co-sum"></div>{pay_badges(L)}</div></aside></div></div>')
    page(L, "commande.html", J["order_t"], body)
    # modes de paiement
    how = "".join(f'<li><span class="step__n">{i + 1}</span><p>{E(t)}</p></li>' for i, t in enumerate(J["how"]))
    cards = "".join(f'<article class="paycard"><span class="paycard__ic">{ic(i, 26)}</span><h3>{E(J[t])}</h3><p>{E(J[d])}</p></article>' for i, t, d in
                    [("cash", "pay_cod", "pay_cod_d"), ("card", "pay_card", "pay_card_d"), ("bank", "pay_bank", "pay_bank_d"), ("store", "pay_store", "pay_store_d")])
    body = (f'<div class="container page-wrap"><header class="page-head"><h1 class="page-title">{E(J["pays_t"])}</h1></header><div class="entry-content paypage">'
            f'<p class="paypage__intro">{E(J["pays_intro"])}</p>{pay_badges(L, True)}<div class="paycards">{cards}</div>'
            f'<section class="svc-how"><h2>{E(J["how_t"])}</h2><ol class="steps">{how}</ol></section>'
            f'<section class="paysec"><h2>{ic("lock", 22)} {E(J["sec_t"])}</h2><p>{E(J["sec_d"])}</p></section></div></div>')
    page(L, "paiement.html", J["pays_t"], body)

def build_404():
    L = "fr"; U = SI.UI[L]
    body = f'<div class="container page-wrap notfound"><p class="notfound__code">404</p><h1 class="page-title">{E(U["notfound"])}</h1><p>{E(U["notfound_t"])}</p><a class="btn btn--primary" href="/">{E(U["back"])}</a> <a class="btn btn--primary" href="/en/">English</a> <a class="btn btn--primary" href="/ar/">العربية</a></div>'
    body = body.replace('href="/"', 'href="index.html"').replace('href="/en/"', 'href="en/index.html"').replace('href="/ar/"', 'href="ar/index.html"')
    s = head(L, U["notfound"], "") + header(L, "index.html", "") + body + footer(L, "index.html", "")
    # page 404 servie à n'importe quelle profondeur : on fixe la base selon l'hébergeur
    # (racine du domaine sur Netlify, /librairie-digitale/ sur GitHub Pages)
    base = ('<script>(function(){var p=location.pathname,m=p.match(/^\\/[^\\/]+\\/(?=.)/),r="/";'
            'if(m&&location.hostname.slice(-10)===".github.io")r=m[0];document.write(\'<base href="\'+r+\'">\')})()</script>')
    s = s.replace("<head>", "<head>" + base, 1)
    open(os.path.join(OUT, "404.html"), "w").write(s.replace("{FILE}", "index.html"))

USE_CNAME = True  # DNS de datalibrairie.com pointé vers GitHub Pages (16 nov. 2026)

if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(os.path.join(OUT, "img", "p")); os.makedirs(os.path.join(OUT, "assets"))
    from draw import draw as DRAW
    os.makedirs(os.path.join(OUT, "img", "c"))
    for f in CAT_IMG.values(): shutil.copy(BASE + "real/cats/" + f, os.path.join(OUT, "img", "c", f))
    for p in P:
        dst = os.path.join(OUT, p["img"])
        if p.get("real"):
            if p.get("photo"): shutil.copy(p["photo"], dst)
            else: DRAW("notebook", "#2a9d4b", p["name"], dst)
        else:
            shutil.copy(f"{BASE}imgs-byname/{_BYNAME[p['name']]}.jpg", dst)
        for v in p.get("variants", []):
            dst = os.path.join(OUT, v["img"])
            if v.get("gen"):
                cache = f"{BASE}imgs-var/{v['sku'].lower()}.jpg"
                if not os.path.exists(cache):
                    os.makedirs(os.path.dirname(cache), exist_ok=True); DRAW(p["kind"], VR.COLORS[v["color"]][3], p["name"] + v["color"], cache)
                shutil.copy(cache, dst)
            elif not os.path.exists(dst):
                q = _bysku_all[v["sku"]]
                shutil.copy(q["photo"] if q.get("real") else f"{BASE}imgs-byname/{_BYNAME[q['name']]}.jpg", dst)
    from PIL import Image as _Im
    os.makedirs(os.path.join(OUT, "img", "t"), exist_ok=True)
    for f in os.listdir(os.path.join(OUT, "img", "p")):
        im = _Im.open(os.path.join(OUT, "img", "p", f)).convert("RGB"); im.thumbnail((300, 300), _Im.LANCZOS)
        im.save(os.path.join(OUT, "img", "t", f), quality=78, optimize=True, progressive=True)
    A = BASE + "assets/"
    for f in ["site.css", "digitale.css", "nova.css", "dark.css", "app.js"]: shutil.copy(A + f, os.path.join(OUT, "assets", f))
    for f in ["emblem.svg", "emblem-navy.svg", "favicon.png", "logo-trilingue-h.png", "logo-data.png", "logo-entete2.png"]: shutil.copy(A + f, os.path.join(OUT, "img", f))
    os.makedirs(os.path.join(OUT, "logos"), exist_ok=True)
    for f in ["logo-trilingue.png", "logo-trilingue-horizontal.png", "logo-trilingue-transparent.png"]: shutil.copy(BASE + "assets/logos/" + f, os.path.join(OUT, "logos", f))
    shutil.copy(BASE + "config.js", os.path.join(OUT, "config.js"))
    shutil.copytree(BASE + "videos", os.path.join(OUT, "video"), dirs_exist_ok=True)
    open(os.path.join(OUT, "_headers"), "w").write(
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n"
        "  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()\n"
        "/img/*\n  Cache-Control: public, max-age=604800\n/video/*\n  Cache-Control: public, max-age=604800\n")
    open(os.path.join(OUT, ".gitignore"), "w").write(GITIGNORE)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")  # GitHub Pages : servir les fichiers tels quels
    if USE_CNAME: open(os.path.join(OUT, "CNAME"), "w").write("datalibrairie.com\n")  # nom de domaine (GitHub Pages)
    for L in LANGS:
        build_home(L); build_categories(L); build_products(L); build_services(L); build_pages(L); build_shop_pages(L)
    build_404()
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print("ok", n, "fichiers")
