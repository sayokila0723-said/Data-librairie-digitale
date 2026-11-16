# Produits déclinés en couleurs
# couleur : (fr, en, ar, hex)
COLORS = {
 "bleu": ("Bleu", "Blue", "أزرق", "#1f4fbf"), "noir": ("Noir", "Black", "أسود", "#222222"),
 "rouge": ("Rouge", "Red", "أحمر", "#d62828"), "vert": ("Vert", "Green", "أخضر", "#2a9d4b"),
 "jaune": ("Jaune", "Yellow", "أصفر", "#f7c714"), "rose": ("Rose", "Pink", "وردي", "#ff5fa2"),
 "orange": ("Orange", "Orange", "برتقالي", "#f28c28"), "violet": ("Violet", "Purple", "بنفسجي", "#8e44ad"),
 "blanc": ("Blanc", "White", "أبيض", "#f4f4f0"), "bleuciel": ("Bleu ciel", "Sky blue", "أزرق فاتح", "#3ab0e2"),
}

# groupe : nom FR du parent, (EN, AR), [(couleur, nom FR du produit existant ou None)]
GROUPS = [
 ("Stylo à bille BIC Cristal Original", ("BIC Cristal Original ballpoint pen", "قلم حبر جاف BIC Cristal"),
  [("bleu", "Stylo à bille BIC Cristal Original bleu"), ("noir", "Stylo à bille BIC Cristal Original noir"), ("rouge", "Stylo à bille BIC Cristal Original rouge"), ("vert", "Stylo à bille BIC Cristal Original vert")]),
 ("Stylo gel Pilot G-2 0,7 mm", ("Pilot G-2 0.7 mm gel pen", "قلم جل Pilot G-2 ‏0.7 مم"),
  [("bleu", "Stylo gel Pilot G-2 0,7 mm bleu"), ("noir", "Stylo gel Pilot G-2 0,7 mm noir"), ("rouge", None), ("vert", None)]),
 ("Stylo effaçable Pilot FriXion Clicker 0,7 mm", ("Pilot FriXion Clicker erasable pen 0.7 mm", "قلم قابل للمسح Pilot FriXion"),
  [("bleu", "Stylo effaçable Pilot FriXion Clicker 0,7 mm bleu"), ("noir", None), ("rouge", None), ("vert", None)]),
 ("Marqueur permanent Edding 3000", ("Edding 3000 permanent marker", "قلم ماركر دائم Edding 3000"),
  [("noir", "Marqueur permanent Edding 3000 noir"), ("bleu", None), ("rouge", None), ("vert", None)]),
 ("Surligneur Stabilo Boss Original", ("Stabilo Boss Original highlighter", "قلم تمييز Stabilo Boss"),
  [("jaune", "Surligneur Stabilo Boss Original jaune"), ("vert", None), ("rose", None), ("orange", None), ("bleuciel", None)]),
 ("Cahier piqûre 96 pages grands carreaux 17×22", ("96-page notebook, large squares 17×22", "دفتر 96 صفحة مربعات كبيرة 17×22"),
  [("bleu", "Cahier piqûre 96 pages grands carreaux 17×22"), ("rouge", None), ("vert", None), ("jaune", None), ("violet", None)]),
 ("Classeur à levier dos 8 cm", ("Lever arch file 8 cm", "ملف برافعة 8 سم"),
  [("bleu", "Classeur à levier dos 8 cm bleu"), ("noir", "Classeur à levier dos 8 cm noir"), ("rouge", "Classeur à levier dos 8 cm rouge"), ("vert", None), ("jaune", None)]),
 ("Chemise à rabats élastique 24×32", ("Elastic flap folder 24×32", "حافظة بأجنحة ومطاط 24×32"),
  [("bleu", "Chemise à rabats élastique 24×32"), ("rouge", None), ("vert", None), ("noir", None), ("jaune", None)]),
 ("Cartable primaire 2 compartiments", ("Primary school bag, 2 compartments", "محفظة ابتدائي بقسمين"),
  [("bleuciel", "Cartable primaire 2 compartiments"), ("rose", None), ("rouge", None), ("vert", None)]),
 ("Trousse double zip", ("Double-zip pencil case", "مقلمة بسحابين"),
  [("violet", "Trousse double zip"), ("bleu", None), ("rose", None), ("noir", None)]),
 ("Ciseaux écolier 13 cm bouts ronds", ("13 cm school scissors, round tips", "مقص مدرسي 13 سم برأس مستدير"),
  [("vert", "Ciseaux écolier 13 cm bouts ronds"), ("bleu", None), ("rose", None)]),
 ("Peinture acrylique 100 ml", ("Acrylic paint 100 ml", "صباغة أكريليك 100 مل"),
  [("bleu", "Peinture acrylique 100 ml bleu"), ("rouge", "Peinture acrylique 100 ml rouge"), ("jaune", None), ("vert", None), ("blanc", None), ("noir", None)]),
]

LABELS = {
 "fr": dict(color="Couleur", colors="couleurs", choose="Choisir", pick="Choisissez une couleur"),
 "en": dict(color="Colour", colors="colours", choose="Choose", pick="Choose a colour"),
 "ar": dict(color="اللون", colors="ألوان", choose="اختر", pick="اختر اللون"),
}

# ---- groupes du catalogue réel ----
import real_catalog as _RC
_N = {(r[0], r[1]): r[3][0] for r in _RC.R}
for (_fr, _en, _ar), _ms in _RC.GROUPS:
    GROUPS.append((_fr, (_en, _ar), [(c, _N[k]) for c, k in _ms]))
