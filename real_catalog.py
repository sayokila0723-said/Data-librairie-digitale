# Catalogue réel de la librairie (relevé du logiciel de caisse, novembre 2026)
# Chaque produit : capture (sNN), position de la vignette, sous-rayon, noms FR/EN/AR, prix (Dhs), référence, drapeaux
# Les photos sont découpées des captures (real/crops/sNN_KK.png).

COL = {
    "bleu": ("bleu", "blue", "أزرق"), "noir": ("noir", "black", "أسود"), "rouge": ("rouge", "red", "أحمر"),
    "vert": ("vert", "green", "أخضر"), "bleu ciel": ("bleu ciel", "sky blue", "أزرق فاتح"),
    "orange": ("orange", "orange", "برتقالي"), "rose": ("rose", "pink", "وردي"), "jaune": ("jaune", "yellow", "أصفر"),
    "blanc": ("blanc", "white", "أبيض"),
}

def _mods(mods):
    out = []
    for m in mods:
        out.append(COL[m] if isinstance(m, str) else m)
    return out

def fam(tfr, ten, tar):
    def mk(brand, *mods):
        ms = _mods(mods)
        fr = " ".join(x for x in [tfr, brand] + [m[0] for m in ms] if x)
        en = " ".join(x for x in [brand, ten] if x) + ("" if not ms else ", " + ", ".join(m[1] for m in ms))
        ar = " ".join(x for x in [tar, brand] + [m[2] for m in ms] if x)
        return fr, en, ar
    return mk

def T(fr, en, ar): return (fr, en, ar)

BILLE = fam("Stylo à bille", "ballpoint pen", "قلم حبر جاف")
ENCRE = fam("Stylo à encre", "rollerball pen", "قلم حبر سائل")
EFF = fam("Stylo effaçable", "erasable pen", "قلم قابل للمسح")
CRAY = fam("Crayon", "pencil", "قلم رصاص")
MTAB = fam("Marqueur tableau", "whiteboard marker", "قلم سبورة")
MPERM = fam("Marqueur permanent", "permanent marker", "قلم ماركر دائم")
SURL = fam("Surligneur", "highlighter", "قلم تمييز")
CORR = fam("Correcteur", "correction pen", "قلم تصحيح")
RECH = fam("Recharge marqueur tableau", "whiteboard marker refill ink", "حبر احتياطي لقلم السبورة")
ARCH = fam("Boîte d'archives en carton", "cardboard archive box", "علبة أرشيف من الكرتون")
CLAS = fam("Classeur", "binder", "ملف")
PDOC = fam("Porte-documents", "display book", "حافظة وثائق")

def P(n): return T(f"{n} pages", f"{n} pages", f"{n} صفحة")
A5 = T("A5 (17×22)", "A5 (17×22)", "A5 (17×22)")
A4 = T("A4 (21×29,7)", "A4 (21×29.7)", "A4 (21×29.7)")
R10, R5 = T("10/10", "10/10", "10/10"), T("5/5", "5/5", "5/5")
CAH = fam("Cahier", "notebook", "دفتر")
SPI = fam("Cahier à spirale", "spiral notebook", "دفتر حلزوني")
TP = fam("Cahier de travaux pratiques", "practical work (TP) notebook", "دفتر الأشغال التطبيقية")
TXT = fam("Cahier de textes", "homework diary", "دفتر النصوص")
def REG(mains, pages, brand, *mods):
    ms = _mods(mods)
    return (" ".join([f"Registre {mains} mains", brand, f"{pages} pages"] + [m[0] for m in ms]),
            f"{brand} {mains}-quire register, {pages} pages" + ("" if not ms else ", " + ", ".join(m[1] for m in ms)),
            " ".join([f"سجل {mains} أجزاء", brand, f"{pages} صفحة"] + [m[2] for m in ms]))
def SUJ(n, pages, brand, *mods):
    ms = _mods(mods)
    pg = [f"{pages} pages"] if pages else []
    return (" ".join([f"Cahier {n} sujets", brand] + pg + [m[0] for m in ms]),
            f"{brand} {n}-subject notebook" + (f", {pages} pages" if pages else "") + ("" if not ms else ", " + ", ".join(m[1] for m in ms)),
            " ".join([f"دفتر {n} مواد", brand] + ([f"{pages} صفحة"] if pages else []) + [m[2] for m in ms]))
SPIR = T("à spirale", "spiral-bound", "حلزوني")
BOX = T("(boîte)", "(box)", "(علبة)")

# Sous-rayons : clé -> (rayon, sous-rayon FR, EN, AR, description FR/EN/AR des produits)
SUBS = {
 "bille": ("Écriture & Correction", "Stylos à bille", "Ballpoint pens", "أقلام الحبر الجاف",
           ("Stylo à bille pour l'école et le bureau.", "Ballpoint pen for school and the office.", "قلم حبر جاف للمدرسة والمكتب.")),
 "encre": ("Écriture & Correction", "Stylos à encre & recharges", "Rollerball pens & refills", "أقلام الحبر السائل والعبوات",
           ("Écriture fluide et régulière.", "Smooth, even writing.", "كتابة سلسة ومنتظمة.")),
 "eff": ("Écriture & Correction", "Stylos effaçables", "Erasable pens", "أقلام قابلة للمسح",
         ("Écrivez, effacez, réécrivez sans abîmer la feuille.", "Write, erase and rewrite without damaging the page.", "اكتب وامسح وأعد الكتابة دون إتلاف الورقة.")),
 "cray": ("Écriture & Correction", "Crayons", "Pencils", "أقلام الرصاص",
          ("Crayon graphite pour l'écriture et le dessin.", "Graphite pencil for writing and drawing.", "قلم رصاص للكتابة والرسم.")),
 "mtab": ("Écriture & Correction", "Marqueurs tableau", "Whiteboard markers", "أقلام السبورة",
          ("Marqueur effaçable à sec pour tableau blanc.", "Dry-erase marker for whiteboards.", "قلم قابل للمسح الجاف للسبورة البيضاء.")),
 "mperm": ("Écriture & Correction", "Marqueurs permanents", "Permanent markers", "أقلام الماركر الدائمة",
           ("Encre permanente, écrit sur carton, plastique et métal.", "Permanent ink, writes on cardboard, plastic and metal.", "حبر دائم يكتب على الكرتون والبلاستيك والمعدن.")),
 "surl": ("Écriture & Correction", "Surligneurs", "Highlighters", "أقلام التمييز",
          ("Couleur fluo pour faire ressortir l'essentiel.", "Fluorescent colour to make key points stand out.", "لون فوسفوري لإبراز الأهم.")),
 "corr": ("Écriture & Correction", "Correcteurs", "Correction pens", "أقلام التصحيح",
          ("Correction nette et rapide, séchage rapide.", "Clean, quick correction, fast drying.", "تصحيح نظيف وسريع الجفاف.")),
 "rech": ("Écriture & Correction", "Recharges marqueur tableau", "Whiteboard marker refills", "عبوات أقلام السبورة",
          ("Recharge d'encre pour marqueurs tableau blanc.", "Ink refill for whiteboard markers.", "حبر احتياطي لأقلام السبورة البيضاء.")),
 "a5": ("Cahiers", "Cahiers petit format A5 (17×22)", "Small notebooks A5 (17×22)", "دفاتر صغيرة A5 (17×22)",
        ("Cahier petit format pour l'école.", "Small-format school notebook.", "دفتر صغير الحجم للمدرسة.")),
 "a4": ("Cahiers", "Cahiers grand format A4 (21×29,7)", "Large notebooks A4 (21×29.7)", "دفاتر كبيرة A4 (21×29.7)",
        ("Cahier grand format, couverture illustrée.", "Large-format notebook with illustrated cover.", "دفتر كبير الحجم بغلاف مصوّر.")),
 "spa5": ("Cahiers", "Cahiers à spirale A5", "Spiral notebooks A5", "دفاتر حلزونية A5",
          ("Reliure spirale, s'ouvre bien à plat.", "Spiral binding, opens flat.", "تجليد حلزوني يُفتح بشكل مسطّح.")),
 "spa4": ("Cahiers", "Cahiers à spirale A4", "Spiral notebooks A4", "دفاتر حلزونية A4",
          ("Reliure spirale, s'ouvre bien à plat.", "Spiral binding, opens flat.", "تجليد حلزوني يُفتح بشكل مسطّح.")),
 "tpa5": ("Cahiers", "Cahiers de travaux pratiques A5", "Practical work notebooks A5", "دفاتر الأشغال التطبيقية A5",
          ("Pages alternées lignées et blanches pour les sciences.", "Alternating lined and plain pages for science.", "صفحات مسطّرة وأخرى بيضاء بالتناوب للعلوم.")),
 "tpa4": ("Cahiers", "Cahiers de travaux pratiques A4", "Practical work notebooks A4", "دفاتر الأشغال التطبيقية A4",
          ("Pages alternées lignées et blanches pour les sciences.", "Alternating lined and plain pages for science.", "صفحات مسطّرة وأخرى بيضاء بالتناوب للعلوم.")),
 "txt": ("Cahiers", "Cahiers de textes", "Homework diaries", "دفاتر النصوص",
         ("Pour noter devoirs et leçons toute l'année.", "To note homework and lessons all year.", "لتدوين الواجبات والدروس طوال السنة.")),
 "reg": ("Cahiers", "Registres & cahiers à sujets", "Registers & subject notebooks", "السجلات والدفاتر متعددة المواد",
         ("Pour la comptabilité, les archives ou plusieurs matières.", "For accounts, records or several subjects.", "للمحاسبة والأرشيف أو لعدة مواد.")),
 "arch": ("Classement & Archivage", "Boîtes d'archives", "Archive boxes", "علب الأرشيف",
          ("Pour ranger et protéger vos dossiers.", "To store and protect your files.", "لترتيب ملفاتك وحمايتها.")),
 "clas": ("Classement & Archivage", "Classeurs & intercalaires", "Binders & dividers", "الملفات والفواصل",
          ("Pour des dossiers bien organisés.", "For well-organised files.", "لملفات منظّمة بشكل جيد.")),
 "pdoc": ("Classement & Archivage", "Porte-documents", "Display books", "حافظات الوثائق",
          ("Pochettes transparentes pour présenter vos documents.", "Clear pockets to present your documents.", "جيوب شفافة لعرض وثائقك.")),
 "trieur": ("Classement & Archivage", "Trieurs & parapheurs", "Sorters & signature books", "المصنفات ودفاتر التوقيع",
            ("Pour trier et faire signer le courrier.", "To sort mail and collect signatures.", "لفرز البريد وتوقيع الوثائق.")),
 "toner": ("Informatique & Consommables", "Cartouches & toners", "Cartridges & toners", "الخراطيش والأحبار",
           ("Cartouche compatible, rendement garanti.", "Compatible cartridge, guaranteed yield.", "خرطوشة متوافقة بمردود مضمون.")),
 "manuel": ("Livres", "Manuels scolaires", "School textbooks", "الكتب المدرسية",
            ("Manuel scolaire du programme marocain.", "Textbook for the Moroccan curriculum.", "كتاب مدرسي وفق المنهاج المغربي.")),
 "roman": ("Livres", "Romans & littérature", "Novels & literature", "الروايات والأدب",
           ("Œuvre au programme, édition de poche.", "Set text, pocket edition.", "عمل مقرر، طبعة جيب.")),
 "ciseaux": ("Scolaire", "Colle, ciseaux & accessoires", "Glue, scissors & accessories", "الغراء والمقصات والإكسسوارات",
             ("Ciseaux d'écolier, bouts ronds.", "School scissors, round tips.", "مقص مدرسي برأس مستدير.")),
 "glitter": ("Beaux-arts & Loisirs créatifs", "Pâte à modeler & créatif", "Modelling clay & crafts", "عجينة التشكيل والأنشطة الإبداعية",
             ("Colle pailletée pour décorer et créer.", "Glitter glue to decorate and create.", "غراء لامع للتزيين والإبداع.")),
}

# (capture, position, sous-rayon, (fr, en, ar), prix, référence, drapeaux)
R = [
 # ---- capture 1 : divers ----
 ("s01", 1, "roman", T("Antigone — Jean Anouilh", "Antigone — Jean Anouilh", "أنتيغون — جان أنوي"), 35, "", ""),
 ("s01", 2, "ciseaux", T("Ciseaux Casber", "Casber scissors", "مقص Casber"), 8, "501-Y", ""),
 ("s01", 3, "glitter", T("Colle pailletée Glitter Glue 50 ml", "Glitter Glue 50 ml", "غراء لامع Glitter Glue ‏50 مل"), 10, "", ""),
 ("s01", 4, "cray", CRAY("Deli", T("HB", "HB", "HB")), 4, "38029N", ""),
 ("s01", 5, "roman", T("La Ficelle — Boule de suif (Maupassant)", "La Ficelle — Boule de suif (Maupassant)", "الخيط — كرة الشحم (موباسان)"), 15, "", ""),
 ("s01", 6, "manuel", T("La Cité des sciences CE1", "La Cité des sciences — Year 2 (CE1)", "La Cité des sciences — المستوى الثاني ابتدائي"), 70, "", "n"),
 ("s01", 7, "roman", T("Kalila wa Dimna — Ibn al-Muqaffa", "Kalila wa Dimna — Ibn al-Muqaffa", "كليلة ودمنة — عبد الله بن المقفع"), 40, "", ""),
 # ---- stylos à bille ----
 ("s03", 0, "bille", T("Stylo calligraphie Al Khatat", "Al Khatat calligraphy pen", "قلم الخطاط للخط العربي"), 15, "", "n"),
 ("s03", 1, "bille", BILLE("BIC Cristal", "bleu"), 2, "", "f"),
 ("s03", 2, "bille", BILLE("BIC Cristal", "noir"), 2, "", ""),
 ("s03", 3, "bille", BILLE("Casber", T("gel 6 couleurs", "gel, 6 colours", "جل 6 ألوان")), 12, "CQ905-6", ""),
 ("s03", 4, "bille", BILLE("Deli", "vert"), 2, "Q19-GN", ""),
 ("s03", 5, "bille", BILLE("Hauser"), 2, "", ""),
 ("s03", 6, "bille", BILLE("Monami", "bleu ciel"), 2, "", ""),
 ("s03", 7, "bille", BILLE("", T("10 couleurs", "10 colours", "10 ألوان")), 15, "", ""),
 ("s03", 8, "bille", BILLE("BIC", T("4 couleurs", "4 colours", "4 ألوان")), 17, "", "f"),
 ("s03", 9, "bille", BILLE("BIC Cristal Up"), 2.5, "", ""),
 ("s03", 10, "bille", BILLE("Casber Color Pen", T("pochette de 12", "pack of 12", "علبة 12")), 20, "", ""),
 ("s03", 11, "bille", BILLE("Deli", "bleu"), 2, "Q19-BL", ""),
 ("s03", 12, "bille", BILLE("Hauser", "bleu", T("boîte de 50", "box of 50", "علبة 50")), 80, "", ""),
 ("s03", 13, "bille", BILLE("Hauser", "noir"), 2, "", ""),
 ("s03", 14, "bille", BILLE("M&G", T("4 couleurs", "4 colours", "4 ألوان")), 10, "ABP80371", ""),
 ("s03", 15, "bille", BILLE("M&G", T("4 couleurs, modèle classique", "4 colours, classic model", "4 ألوان، نموذج كلاسيكي")), 10, "ABP803R4", ""),
 ("s03", 16, "bille", BILLE("M&G", "bleu", T("gel 0,7 mm", "gel 0.7 mm", "جل 0.7 مم")), 10, "AGP11171", ""),
 ("s03", 17, "bille", BILLE("M&G Eraser", T("effaçable 0,7 mm", "erasable 0.7 mm", "قابل للمسح 0.7 مم")), 10, "AKPH32R7", ""),
 ("s03", 18, "bille", BILLE("Smart", "noir", T("1,0 mm", "1.0 mm", "1.0 مم")), 2, "960BS", ""),
 ("s03", 19, "bille", BILLE("Smart", "rouge", T("1,0 mm", "1.0 mm", "1.0 مم")), 2, "650R", ""),
 ("s03", 20, "bille", BILLE("Styl Fifty", T("lot de 6", "pack of 6", "مجموعة 6")), 12, "", ""),
 # ---- stylos à encre ----
 ("s04", 0, "encre", ENCRE("Pilot G-2", "bleu", T("0,7 mm", "0.7 mm", "0.7 مم")), 17, "BL-G2-7-L", "f"),
 ("s04", 1, "encre", ENCRE("Pilot G-2", "noir", T("0,7 mm", "0.7 mm", "0.7 مم")), 17, "BL-G2-7-B", ""),
 # ---- effaçables ----
 ("s05", 0, "eff", EFF("Deli", T("0,5 mm", "0.5 mm", "0.5 مم"), BOX), 120, "G95-BL", ""),
 ("s05", 1, "eff", EFF("Jiandan", T("0,5 mm", "0.5 mm", "0.5 مم")), 10, "JD-2257", ""),
 ("s05", 2, "eff", EFF("M&G", T("0,5 mm", "0.5 mm", "0.5 مم")), 10, "AKPH32R6", "n"),
 # ---- crayons ----
 ("s06", 0, "cray", CRAY("Deli", T("2B", "2B", "2B")), 3, "U533", ""),
 ("s06", 1, "cray", CRAY("Express", T("HB2", "HB2", "HB2")), 2, "XO-2995", ""),
 ("s06", 2, "cray", CRAY("Y-Plus", T("HB", "HB", "HB")), 4, "PX120200", ""),
 ("s06", 3, "cray", CRAY("BIC", T("HB-2", "HB-2", "HB-2")), 4, "", ""),
 ("s06", 4, "cray", CRAY("Maped", T("HB-2", "HB-2", "HB-2")), 3, "", ""),
 ("s06", 5, "cray", CRAY("Maped", T("HB2 Black'Peps", "HB2 Black'Peps", "HB2 Black'Peps")), 3, "", ""),
 ("s06", 6, "cray", T("Crayons de dessin M&G G5", "M&G G5 drawing pencils", "أقلام رسم M&G G5"), 10, "AWP357G5", ""),
 # ---- marqueurs tableau ----
 ("s07", 0, "mtab", MTAB("Deli", "bleu"), 12, "6993", ""),
 ("s07", 1, "mtab", MTAB("Deli Think", "bleu"), 10, "U10130", ""),
 ("s07", 2, "mtab", MTAB("Deli Think", "bleu", T("pointe biseautée", "chisel tip", "رأس مشطوف")), 10, "U00230", ""),
 ("s07", 3, "mtab", MTAB("Deli Think", "noir"), 10, "U00120", ""),
 ("s07", 4, "mtab", MTAB("Deli", "noir", T("modèle White Board", "White Board model", "نموذج White Board")), 8, "U00120", ""),
 ("s07", 5, "mtab", MTAB("Deli Think", T("pochette de 4 couleurs", "wallet of 4 colours", "علبة 4 ألوان")), 30, "EU00101", "f"),
 ("s07", 6, "mtab", MTAB("Deli Think", "rouge"), 10, "U00140", ""),
 ("s07", 7, "mtab", MTAB("Express", "bleu"), 7, "XO-8362", ""),
 ("s07", 8, "mtab", MTAB("Express", "bleu", T("modèle 2", "model 2", "نموذج 2")), 7, "XO-8379", ""),
 ("s07", 9, "mtab", MTAB("Express X-Mark", "bleu"), 10, "XO-5040", ""),
 ("s07", 10, "mtab", MTAB("Express X-Mark", "noir"), 10, "XO-5156", ""),
 ("s07", 11, "mtab", MTAB("M&G", "bleu"), 8, "AWMY2271", ""),
 ("s07", 12, "mtab", MTAB("Memory", T("lot de 4", "pack of 4", "مجموعة 4")), 30, "2008/4", ""),
 ("s07", 13, "mtab", MTAB("rechargeable", T("lot", "pack", "مجموعة")), 10, "G-201", ""),
 ("s07", 14, "mtab", MTAB("rechargeable Deli", "noir"), 12, "6820", ""),
 ("s07", 15, "mtab", MTAB("SigmaFlow", T("lot de 4", "pack of 4", "مجموعة 4")), 15, "", ""),
 ("s07", 16, "mtab", MTAB("BIC Velleda", "bleu"), 10, "", "f"),
 ("s07", 17, "mtab", MTAB("BIC Velleda", "noir"), 10, "", ""),
 ("s07", 18, "mtab", MTAB("Fenlot", "noir"), 8, "FL-7026", ""),
 ("s07", 19, "mtab", MTAB("Memory", "noir", BOX), 10, "M6012N", ""),
 # ---- marqueurs permanents ----
 ("s08", 0, "mperm", MPERM("Chilang", "noir"), 10, "C-470", ""),
 ("s08", 1, "mperm", MPERM("Deli Think", "rouge"), 10, "U10140", ""),
 ("s08", 2, "mperm", MPERM("Memory", "bleu"), 10, "4007BB", ""),
 ("s08", 3, "mperm", MPERM("Memory", "noir"), 10, "4007BN", ""),
 ("s08", 4, "mperm", MPERM("Permano", "noir"), 8, "CR-2004", ""),
 # ---- surligneurs ----
 ("s09", 0, "surl", SURL("Uni-Mark", "vert"), 8, "A-811", ""),
 ("s09", 1, "surl", SURL("High Lighter", T("lot de 6", "pack of 6", "مجموعة 6")), 20, "A-811", ""),
 ("s09", 2, "surl", SURL("Faber-Castell", "bleu"), 10, "154851", ""),
 ("s09", 3, "surl", SURL("Faber-Castell", "orange"), 10, "154815", ""),
 ("s09", 4, "surl", SURL("Faber-Castell", "rose"), 10, "154628", ""),
 ("s09", 5, "surl", SURL("Faber-Castell", "vert"), 10, "154807", "f"),
 # ---- correcteurs ----
 ("s10", 0, "corr", CORR("Accord", T("8 ml, couleurs pastel", "8 ml, pastel colours", "8 مل، ألوان باستيل")), 10, "BL0019", ""),
 ("s10", 1, "corr", CORR("Accord", T("8 ml", "8 ml", "8 مل")), 8, "BL0019", ""),
 ("s10", 2, "corr", CORR("Boston", T("18 ml", "18 ml", "18 مل")), 10, "324", ""),
 ("s10", 3, "corr", CORR("Deli", T("12 ml", "12 ml", "12 مل")), 10, "H10490", ""),
 ("s10", 4, "corr", CORR("Deli Cover Up", T("18 ml", "18 ml", "18 مل"), BOX), 144, "H10310", ""),
 ("s10", 5, "corr", CORR("Deli", T("3 ml", "3 ml", "3 مل"), BOX), 144, "H10590", ""),
 ("s10", 6, "corr", CORR("Deli Cover Up", T("5 ml", "5 ml", "5 مل"), BOX), 96, "H10000", ""),
 ("s10", 7, "corr", CORR("Deli", T("6 ml", "6 ml", "6 مل")), 6, "H10800", ""),
 ("s10", 8, "corr", CORR("Deli", T("6 ml, présentoir", "6 ml, display box", "6 مل، علبة عرض")), 9.33, "H10800", ""),
 ("s10", 9, "corr", CORR("Express", T("8 ml", "8 ml", "8 مل")), 6, "XO-1103", ""),
 ("s10", 10, "corr", CORR("Express", T("8 ml, embout métal", "8 ml, metal tip", "8 مل، رأس معدني")), 8, "XO-1301", ""),
 ("s10", 11, "corr", CORR("M&G", T("8 ml", "8 ml", "8 مل")), 6, "H10490", ""),
 ("s10", 12, "corr", CORR("Nepo", T("4 ml", "4 ml", "4 مل")), 8, "Nepo-147", ""),
 ("s10", 13, "corr", CORR("Smart Kids", T("18 ml", "18 ml", "18 مل")), 8, "4829", ""),
 ("s10", 14, "corr", CORR("Deli Uspire", T("10 ml", "10 ml", "10 مل")), 10, "3992", ""),
 # ---- recharges marqueur tableau ----
 ("s12", 0, "rech", RECH("Deli", "noir", T("24 pcs", "24 pcs", "24 قطعة")), 120, "6993", ""),
 ("s12", 1, "rech", RECH("Refill", "bleu", T("24 pcs", "24 pcs", "24 قطعة")), 3, "G-201T", ""),
 # ---- boîtes d'archives ----
 ("s14", 0, "arch", ARCH("Sicla", T("blanc, dos 100 mm", "white, 100 mm spine", "أبيض، ظهر 100 مم")), 10, "100", ""),
 ("s14", 1, "arch", ARCH("Sicla", T("blanc, dos 135 mm", "white, 135 mm spine", "أبيض، ظهر 135 مم")), 12, "135", ""),
 ("s14", 2, "arch", ARCH("Sicla", T("blanc, dos 85 mm", "white, 85 mm spine", "أبيض، ظهر 85 مم")), 8, "85", "f"),
 ("s14", 3, "arch", ARCH("Sicla", T("blanc, dos 160 mm", "white, 160 mm spine", "أبيض، ظهر 160 مم")), 13, "160", ""),
 # ---- classeurs ----
 ("s15", 0, "clas", CLAS("Ambassador", T("A4", "A4", "A4")), 25, "", ""),
 ("s15", 1, "clas", CLAS("Ann Sweet", T("A4", "A4", "A4")), 25, "", ""),
 ("s15", 2, "clas", CLAS("Algo", T("à levier", "lever arch", "برافعة")), 35, "2203", ""),
 ("s15", 3, "clas", CLAS("Ambassador", T("A5", "A5", "A5")), 15, "002", ""),
 ("s15", 4, "clas", CLAS("Alba Rado", T("à levier", "lever arch", "برافعة")), 25, "MK106", ""),
 ("s15", 5, "clas", CLAS("Sicla", T("à levier noir", "lever arch, black", "برافعة أسود")), 35, "", "f"),
 ("s15", 6, "clas", T("Porte-revues Corner Box ARK noir", "ARK Corner Box magazine holder, black", "حامل مجلات ARK Corner Box أسود"), 45, "2050N", ""),
 ("s15", 7, "clas", T("Jeu de 6 intercalaires AL-MPF", "Set of 6 dividers AL-MPF", "مجموعة 6 فواصل AL-MPF"), 15, "", ""),
 ("s15", 8, "clas", T("Intercalaires OBO 12 positions plastique 1-12", "OBO 12-tab plastic dividers 1-12", "فواصل OBO بلاستيكية 12 قسماً 1-12"), 20, "", ""),
 # ---- porte-documents ----
 ("s16", 0, "pdoc", PDOC("Cally", T("100 vues", "100 pockets", "100 جيب")), 35, "", ""),
 ("s16", 1, "pdoc", PDOC("Exa File", T("100 vues", "100 pockets", "100 جيب")), 35, "ex-100V", ""),
 ("s16", 2, "pdoc", PDOC("", T("100 vues jaune", "100 pockets, yellow", "100 جيب أصفر")), 35, "ex-100V", ""),
 ("s16", 3, "pdoc", PDOC("", T("20 vues rose", "20 pockets, pink", "20 جيب وردي")), 15, "9902", ""),
 ("s16", 4, "pdoc", PDOC("Ecolo", T("20 vues", "20 pockets", "20 جيب")), 15, "", ""),
 ("s16", 5, "pdoc", PDOC("", T("200 vues", "200 pockets", "200 جيب")), 50, "9910", ""),
 ("s16", 6, "pdoc", PDOC("Ecolo", T("40 vues", "40 pockets", "40 جيب")), 20, "", ""),
 ("s16", 7, "pdoc", PDOC("", T("40 vues A4", "40 pockets A4", "40 جيب A4")), 20, "9904", "f"),
 ("s16", 8, "pdoc", PDOC("", T("60 vues violet", "60 pockets, purple", "60 جيب بنفسجي")), 25, "9906", ""),
 ("s16", 9, "pdoc", PDOC("Ecolo", T("60 vues", "60 pockets", "60 جيب")), 25, "", ""),
 ("s16", 10, "pdoc", PDOC("Glo Box", T("60 vues", "60 pockets", "60 جيب")), 30, "6453", ""),
 ("s16", 11, "pdoc", PDOC("Rio", T("60 vues", "60 pockets", "60 جيب")), 30, "B1402", ""),
 ("s16", 12, "pdoc", PDOC("Ambassador", T("80 vues", "80 pockets", "80 جيب")), 30, "", ""),
 ("s16", 13, "pdoc", PDOC("Cally", T("80 vues", "80 pockets", "80 جيب")), 30, "", ""),
 ("s16", 14, "pdoc", PDOC("", T("80 vues orange", "80 pockets, orange", "80 جيب برتقالي")), 30, "9907", ""),
 ("s16", 15, "pdoc", PDOC("Boston", T("120 vues", "120 pockets", "120 جيب")), 30, "", ""),
 ("s16", 16, "pdoc", PDOC("Cally", T("120 vues", "120 pockets", "120 جيب")), 37, "", ""),
 ("s16", 17, "pdoc", PDOC("Reinyom", T("140 vues", "140 pockets", "140 جيب")), 40, "", ""),
 ("s16", 18, "pdoc", PDOC("Reinyom", T("160 vues", "160 pockets", "160 جيب")), 45, "", ""),
 ("s16", 19, "pdoc", PDOC("Reinyom", T("180 vues", "180 pockets", "180 جيب")), 47, "", ""),
 ("s16", 20, "pdoc", PDOC("Reinyom", T("200 vues", "200 pockets", "200 جيب")), 50, "", ""),
 # ---- parapheur, toner ----
 ("s17", 0, "trieur", T("Parapheur luxe 18 volets 35×24 bordeaux", "Deluxe 18-flap signature book 35×24, burgundy", "دفتر توقيع فاخر 18 قسماً 35×24 عنابي"), 70, "", ""),
 ("s18", 0, "toner", T("Toner laser compatible Word", "Word compatible laser toner", "حبر ليزر متوافق Word"), 150, "", ""),
 # ---- cahier hors rayon ----
 ("s19", 8, "a4", CAH("Sylver", P(196), R10, A4), 17, "", ""),
 # ---- cahiers A5 ----
 ("s20", 0, "a5", CAH("B-M", P(144), R10, A5), 15, "", ""),
 ("s20", 1, "a5", CAH("Sylver", P(144), R10, A5), 8, "", ""),
 ("s20", 2, "a5", CAH("B-M", P(192), R10, A5), 10, "", ""),
 ("s20", 3, "a5", CAH("Essentiel", P(192), R10, A5), 10, "", ""),
 ("s20", 4, "a5", CAH("Maped", P(192), R10, A5), 17, "", ""),
 ("s20", 5, "a5", CAH("Pegasus", P(288), R10, A5), 15, "", ""),
 ("s20", 6, "a5", CAH("Sylver", P(288), R10, A5), 15, "", ""),
 ("s20", 7, "a5", CAH("Alice", P(288), R5, A5), 25, "", ""),
 ("s20", 8, "a5", CAH("Essentiel", P(288), R10, A5), 15, "", ""),
 ("s20", 9, "a5", CAH("Maped", P(288), R10, A5), 25, "", ""),
 ("s20", 10, "a5", CAH("B-M", P(384), R10, A5), 17, "", ""),
 ("s20", 11, "a5", CAH("Pegasus", P(384), R10, A5), 17, "", ""),
 ("s20", 12, "a5", CAH("Sylver", P(384), R10, A5), 17, "", ""),
 ("s20", 13, "a5", CAH("B-M", P(384), R5, A5), 25, "", ""),
 ("s20", 14, "a5", CAH("Essentiel", P(384), R10, A5), 17, "", ""),
 ("s20", 15, "a5", CAH("Essentiel", P(48), R10, A5), 3, "", ""),
 ("s20", 16, "a5", CAH("Sylver", P(48), R10, A5), 3, "", ""),
 ("s20", 17, "a5", CAH("Pegasus", P(48), R10, A5), 3, "", ""),
 ("s20", 18, "a5", CAH("B-M", P(96), R10, A5), 5, "", ""),
 ("s20", 19, "a5", CAH("Maped", P(96), R10, A5), 10, "", ""),
 ("s20", 20, "a5", CAH("Maped", P(96), R10, A5, T("modèle 2", "model 2", "نموذج 2")), 7, "", ""),
 ("s20", 21, "a5", CAH("Sopalemb", P(96), R10, A5), 5, "", ""),
 ("s20", 22, "a5", CAH("Essentiel", P(96), R10, A5), 5, "", "f"),
 ("s20", 23, "a5", CAH("Sylver", P(96), R10, A5), 5, "", ""),
 # ---- cahiers A4 ----
 ("s21", 0, "a4", CAH("Essentiel", P(140), A4), 21, "", ""),
 ("s21", 1, "a4", CAH("Sylver", P(144), R5, A4), 15, "", ""),
 ("s21", 2, "a4", CAH("Sylver", P(144), R10, A4), 15, "", ""),
 ("s21", 3, "a4", CAH("B-M", P(192), R10, A4), 17, "", ""),
 ("s21", 4, "a4", CAH("B-M", P(192), R10, A4, T("modèle 2", "model 2", "نموذج 2")), 17, "", ""),
 ("s21", 5, "a4", CAH("Boost", P(192), R10, A4), 17, "bs-CP192A4", ""),
 ("s21", 6, "a4", CAH("Essentiel", P(192), A4, T("Basketball", "Basketball", "كرة السلة")), 17, "", ""),
 ("s21", 7, "a4", CAH("Essentiel", P(192), A4, T("modèle 2", "model 2", "نموذج 2")), 17, "", ""),
 ("s21", 8, "a4", CAH("Sherazed", P(192), R5, A4), 25, "", ""),
 ("s21", 9, "a4", CAH("Sylver", P(192), R5, A4), 17, "", ""),
 ("s21", 10, "a4", CAH("B-M", P(288), R10, A4), 25, "", ""),
 ("s21", 11, "a4", CAH("Sylver", P(288), R5, A4), 25, "", ""),
 ("s21", 12, "a4", CAH("Essentiel", P(288), A4), 25, "", ""),
 ("s21", 13, "a4", CAH("Pegasus", P(288), R10, A4), 25, "", ""),
 ("s21", 14, "a4", CAH("B-M", P(384), R10, A4), 30, "", ""),
 ("s21", 15, "a4", CAH("Boost", P(384), R10, A4, T("Maroc", "Morocco", "المغرب")), 30, "", "f"),
 ("s21", 16, "a4", CAH("Boost", P(384), R10, A4), 30, "BS-CB384A4", ""),
 ("s21", 17, "a4", CAH("Sylver", P(384), R10, A4), 30, "", ""),
 ("s21", 18, "a4", CAH("B-M", P(96), R10, A4), 10, "", ""),
 ("s21", 19, "a4", CAH("Pegasus", P(96), R10, A4), 10, "", ""),
 ("s21", 20, "a4", CAH("Sylver", P(96), R10, A4), 10, "", ""),
 ("s21", 21, "a4", CAH("Essentiel", P(96), R10, A4), 10, "", ""),
 ("s21", 22, "a4", CAH("Maped", P(96), R10, A4), 17, "", ""),
 ("s21", 23, "a4", CAH("Maped", P(192), R10, A4), 25, "", ""),
 # ---- spirale ----
 ("s22", 0, "spa5", SPI("B-M", P(144), T("A5", "A5", "A5")), 8, "", ""),
 ("s23", 0, "spa4", SPI("Sylver", P(120), R5, T("A4", "A4", "A4")), 15, "", ""),
 ("s23", 1, "spa4", SPI("L'Horizon", P(140), R5, T("A4", "A4", "A4")), 20, "530 366", ""),
 ("s23", 2, "spa4", SPI("L'Horizon", P(240), R10, T("A4", "A4", "A4")), 25, "530 371", ""),
 ("s23", 3, "spa4", SPI("L'Horizon", P(300), R10, T("A4", "A4", "A4")), 30, "530 372", ""),
 ("s23", 4, "spa4", CAH("Pegasus", P(384), R10, A4), 30, "", ""),
 ("s23", 5, "spa4", SPI("L'Horizon", P(240), R10, T("A4 rose", "A4, pink", "A4 وردي")), 25, "530 367", ""),
 ("s23", 6, "spa4", SPI("L'Horizon", P(300), R5, T("A4", "A4", "A4")), 30, "530 374", ""),
 # ---- TP A5 ----
 ("s24", 0, "tpa5", TP("Maârif", P(192), T("A5", "A5", "A5")), 12, "", ""),
 ("s24", 1, "tpa5", TP("Sylver", P(192), T("A5", "A5", "A5")), 15, "", ""),
 ("s24", 2, "tpa5", TP("B-M", P(192), T("A5", "A5", "A5")), 15, "", ""),
 ("s24", 3, "tpa5", TP("Sylver", P(96), R10, T("A5", "A5", "A5")), 8, "", ""),
 ("s24", 4, "tpa5", TP("B-M", P(96), T("A5", "A5", "A5")), 8, "", ""),
 ("s24", 5, "tpa5", TP("Essentiel", P(96), T("A5", "A5", "A5")), 8, "", ""),
 # ---- TP A4 ----
 ("s25", 0, "tpa4", TP("Essentiel", P(144), R10, T("A4", "A4", "A4")), 17, "", ""),
 ("s25", 1, "tpa4", TP("Essentiel", P(192), R10, T("A4", "A4", "A4")), 20, "", ""),
 ("s25", 2, "tpa4", TP("Shems", P(192), R10, T("A4", "A4", "A4")), 20, "", ""),
 ("s25", 3, "tpa4", TP("Boost", P(192), R10, T("A4", "A4", "A4")), 15, "", ""),
 ("s25", 4, "tpa4", TP("Sylver", P(192), R10, T("A4", "A4", "A4")), 20, "", ""),
 ("s25", 5, "tpa4", TP("B-M", P(288), R10, T("A4", "A4", "A4")), 25, "", ""),
 ("s25", 6, "tpa4", TP("B-M", P(96), R10, T("A4", "A4", "A4")), 12, "", ""),
 ("s25", 7, "tpa4", TP("Essentiel", P(96), R10, T("A4", "A4", "A4")), 12, "", ""),
 ("s25", 8, "tpa4", TP("Happy", P(96), R10, T("A4", "A4", "A4")), 12, "", ""),
 ("s25", 9, "tpa4", TP("Safari", P(96), R10, T("A4", "A4", "A4")), 12, "", ""),
 # ---- cahiers de textes ----
 ("s26", 0, "txt", TXT("B-M", P(128), T("A5", "A5", "A5")), 20, "", ""),
 ("s26", 1, "txt", TXT("B-M", P(128), T("à spirale A5", "spiral-bound A5", "حلزوني A5")), 20, "", ""),
 ("s26", 2, "txt", TXT("Essentiel", P(128), T("A5", "A5", "A5")), 20, "", "f"),
 # ---- registres & cahiers à sujets ----
 ("s27", 0, "reg", REG(2, 192, "B-M", R5, T("A4", "A4", "A4")), 25, "", ""),
 ("s27", 1, "reg", REG(2, 192, "B-M", R5, T("A4, modèle 2", "A4, model 2", "A4، نموذج 2")), 15, "", ""),
 ("s27", 2, "reg", REG(2, 192, "M-Office", R5, T("A4", "A4", "A4")), 25, "", ""),
 ("s27", 3, "reg", REG(3, 288, "B-M", R5, T("A4", "A4", "A4")), 30, "", ""),
 ("s27", 4, "reg", REG(3, 288, "Essentiel", R5, T("A4", "A4", "A4")), 30, "", ""),
 ("s27", 5, "reg", REG(3, 388, "Essentiel", R5, T("A4", "A4", "A4")), 30, "", ""),
 ("s27", 6, "reg", REG(4, 384, "B-M", R5, T("A4", "A4", "A4")), 45, "", ""),
 ("s27", 7, "reg", REG(5, 432, "B-M", R5, T("A4", "A4", "A4")), 50, "", ""),
 ("s27", 8, "reg", SUJ(5, 240, "B-M", R10, T("A4", "A4", "A4")), 60, "1920", ""),
 ("s27", 9, "reg", SUJ(5, 240, "B-M", R5, SPIR, T("A4", "A4", "A4")), 35, "", ""),
 ("s27", 10, "reg", SUJ(5, 240, "Besty", R5, T("A4", "A4", "A4")), 50, "MMA745144Y", ""),
 ("s27", 11, "reg", SUJ(5, 240, "King School", R5, SPIR, T("A5", "A5", "A5")), 25, "", ""),
 ("s27", 12, "reg", SUJ(5, None, "SkyBleu", R5, SPIR, T("A5", "A5", "A5")), 35, "TBB-325008", ""),
 ("s27", 13, "reg", SUJ(6, 288, "B-M", R5, SPIR, T("A4", "A4", "A4")), 55, "", ""),
 ("s27", 14, "reg", SUJ(7, 336, "B-M", R5, SPIR, T("A4", "A4", "A4")), 65, "", ""),
 ("s27", 15, "reg", SUJ(7, 336, "B-M", R5, SPIR, T("A5", "A5", "A5")), 40, "", ""),
 ("s27", 16, "reg", SUJ(7, 336, "Sylver", R5, SPIR, T("A4", "A4", "A4")), 55, "", ""),
 ("s27", 17, "reg", SUJ(8, 384, "B-M", R5, SPIR, T("A4", "A4", "A4")), 75, "", ""),
 ("s27", 18, "reg", SUJ(8, None, "B-M", R5, SPIR, T("A5", "A5", "A5")), 35, "", ""),
 ("s27", 19, "reg", SUJ(9, 432, "B-M", R5, SPIR, T("A4", "A4", "A4")), 80, "", ""),
]

# vignettes sans photo : capture s25 position 2 (Shems) -> illustration générée
NO_PHOTO = {("s25", 2)}

if __name__ == "__main__":
    import collections
    print(len(R), "produits")
    c = collections.Counter(SUBS[r[2]][1] for r in R); print(c)
    names = collections.Counter(r[3][0] for r in R)
    print("doublons :", [n for n, k in names.items() if k > 1])

# ---- Produits déclinés en couleurs (une fiche, plusieurs couleurs) ----
# (nom parent FR, EN, AR), [(couleur, (capture, position))]
GROUPS = [
 (("Stylo à bille BIC Cristal", "BIC Cristal ballpoint pen", "قلم حبر جاف BIC Cristal"), [("bleu", ("s03", 1)), ("noir", ("s03", 2))]),
 (("Stylo à bille Deli Q19", "Deli Q19 ballpoint pen", "قلم حبر جاف Deli Q19"), [("bleu", ("s03", 11)), ("vert", ("s03", 4))]),
 (("Stylo à bille Smart 1,0 mm", "Smart 1.0 mm ballpoint pen", "قلم حبر جاف Smart ‏1.0 مم"), [("noir", ("s03", 18)), ("rouge", ("s03", 19))]),
 (("Stylo à encre Pilot G-2 0,7 mm", "Pilot G-2 0.7 mm rollerball pen", "قلم حبر سائل Pilot G-2 ‏0.7 مم"), [("bleu", ("s04", 0)), ("noir", ("s04", 1))]),
 (("Marqueur tableau Deli Think", "Deli Think whiteboard marker", "قلم سبورة Deli Think"), [("bleu", ("s07", 1)), ("noir", ("s07", 3)), ("rouge", ("s07", 6))]),
 (("Marqueur tableau Express X-Mark", "Express X-Mark whiteboard marker", "قلم سبورة Express X-Mark"), [("bleu", ("s07", 9)), ("noir", ("s07", 10))]),
 (("Marqueur tableau BIC Velleda", "BIC Velleda whiteboard marker", "قلم سبورة BIC Velleda"), [("bleu", ("s07", 16)), ("noir", ("s07", 17))]),
 (("Marqueur permanent Memory", "Memory permanent marker", "قلم ماركر دائم Memory"), [("bleu", ("s08", 2)), ("noir", ("s08", 3))]),
 (("Surligneur Faber-Castell", "Faber-Castell highlighter", "قلم تمييز Faber-Castell"), [("vert", ("s09", 5)), ("bleu", ("s09", 2)), ("orange", ("s09", 3)), ("rose", ("s09", 4))]),
]
