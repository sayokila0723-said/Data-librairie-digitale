# Catalogue réel, 2e relevé du logiciel de caisse (novembre 2026) : bureau, papeterie, petite fourniture, livres
# Entrée : (capture, position, clé sous-rayon, type, reste du nom, prix, référence)
# Le nom FR = type FR + reste ; EN = reste + type EN ; AR = type AR + reste. type "" = titre de livre (identique dans les 3 langues).

TY = {
 "panier": ("Panier à courrier", "letter tray", "سلة الرسائل"), "ens": ("Ensemble de bureau", "desk set", "طقم مكتب"),
 "pot": ("Pot à crayons", "pen holder", "حامل أقلام"), "pcach": ("Porte-cachets", "stamp rack", "حامل الأختام"),
 "nb": ("Notebook", "notebook", "دفتر ملاحظات"), "ag": ("Agenda", "diary", "أجندة"),
 "bloc": ("Bloc-notes", "notepad", "مذكرة"), "carnet": ("Carnet", "pocket notebook", "دفتر صغير"),
 "ram": ("Ramette papier A4", "A4 copy paper ream", "رزمة ورق A4"), "chem": ("Chemise", "folder", "غلاف ورقي"),
 "roul": ("Rouleau thermique", "thermal paper roll", "لفافة ورق حراري"), "env": ("Enveloppe", "envelope", "ظرف"),
 "copd": ("Copies doubles", "double exam sheets", "أوراق مزدوجة"), "cops": ("Copies simples", "single sheets", "أوراق بسيطة"),
 "milli": ("Papier millimétré", "graph paper", "ورق ملليمتري"), "calq": ("Papier calque", "tracing paper", "ورق شفاف"),
 "carb": ("Papier carbone", "carbon paper", "ورق الكربون"), "mini": ("Papier ministre", "ministre paper", "ورق المنستر"),
 "fbr": ("Fiches bristol", "bristol cards", "بطاقات بريستول"), "calc": ("Calculatrice", "calculator", "آلة حاسبة"),
 "etiqm": ("Étiqueteuse", "price labeller", "آلة الملصقات"), "regle": ("Règle", "ruler", "مسطرة"),
 "equ": ("Équerre", "set square", "كوس"), "rapp": ("Rapporteur", "protractor", "منقلة"),
 "kit": ("Kit de traçage", "geometry set", "طقم الهندسة"), "comp": ("Compas", "compass", "بركار"),
 "gom": ("Gomme", "eraser", "ممحاة"), "cis": ("Ciseaux", "scissors", "مقص"), "tc": ("Taille-crayon", "pencil sharpener", "مبراة"),
 "cblanc": ("Colle blanche", "white glue", "غراء أبيض"), "cliq": ("Colle liquide", "liquid glue", "غراء سائل"),
 "cstick": ("Colle en bâton", "glue stick", "غراء أصبع"), "ctube": ("Colle en tube", "glue tube", "غراء أنبوب"),
 "dev": ("Dévidoir", "tape dispenser", "موزع الشريط اللاصق"), "rub": ("Ruban adhésif", "adhesive tape", "شريط لاصق"),
 "sglue": ("Super glue", "super glue", "غراء فوري"), "agrf": ("Agrafeuse", "stapler", "دباسة"), "agr": ("Agrafes", "staples", "دبابيس الدباسة"),
 "arr": ("Arrache-agrafes", "staple remover", "نازعة الدبابيس"), "notes": ("Notes repositionnables", "sticky notes", "أوراق لاصقة"),
 "ephem": ("Bloc éphéméride", "tear-off calendar", "تقويم يومي"), "pun": ("Punaises", "thumbtacks", "دبابيس ضاغطة"),
 "elas": ("Élastiques", "rubber bands", "أربطة مطاطية"), "attp": ("Attaches parisiennes", "paper fasteners", "مشابك باريسية"),
 "pdc": ("Pince double clip", "binder clip", "مشبك مزدوج"), "tromb": ("Trombones", "paper clips", "مشابك الورق"),
 "etq": ("Étiquettes", "labels", "ملصقات"), "gommet": ("Gommettes", "dot stickers", "ملصقات دائرية"), "stk": ("Stickers", "stickers", "ملصقات مرحة"),
 "perf": ("Perforateur", "hole punch", "ثقابة"), "moui": ("Mouilleur", "finger moistener", "مبلل الأصابع"),
 "oeil": ("Œillets", "reinforcement rings", "حلقات التقوية"), "couvpvc": ("Couvertures PVC transparentes", "clear PVC binding covers", "أغلفة PVC شفافة"),
 "plast": ("Pochettes de plastification", "laminating pouches", "أكياس التصفيح"), "carton": ("Couvertures cartonnées", "card binding covers", "أغلفة كرتونية"),
 "poch": ("Pochettes perforées", "punched pockets", "جيوب مثقبة"), "serre": ("Serre-feuilles", "binding bar", "مشبك أوراق"),
 "spir": ("Spirale plastique", "plastic binding comb", "لولب بلاستيكي"), "cach": ("Cachet", "self-inking stamp", "ختم"),
 "dat": ("Dateur", "date stamp", "ختم التاريخ"), "encre": ("Encre pour tampon", "stamp ink", "حبر الأختام"),
 "tamp": ("Tampon encreur", "ink pad", "وسادة الحبر"), "pbl": ("Porte-bloc", "clipboard", "حامل أوراق"),
 "chev": ("Chevalet tableau en bois", "wooden easel", "حامل سبورة خشبي"), "ardb": ("Ardoise blanche", "whiteboard slate", "لوحة بيضاء"),
 "arde": ("Ardoise électronique", "LCD writing tablet", "لوحة كتابة إلكترونية"), "ardn": ("Ardoise noire", "chalk slate", "لوحة سوداء"),
 "brosse": ("Brosse tableau", "board eraser", "ممسحة السبورة"), "craie": ("Craie", "chalk", "طباشير"),
 "fact": ("Carnet de factures", "invoice book", "دفتر الفواتير"), "recu": ("Carnet de reçus", "receipt book", "دفتر الوصولات"),
 "gpq": ("Paquet de gommettes", "pack of stickers", "علبة ملصقات"), "": ("", "", ""),
}

_D = {
 "bur": ("Pour un bureau bien rangé et organisé.", "For a tidy, well-organised desk.", "لمكتب مرتب ومنظم."),
 "nb": ("Notebook pour vos notes, idées et rendez-vous.", "Notebook for your notes, ideas and appointments.", "دفتر لتدوين ملاحظاتك وأفكارك ومواعيدك."),
 "ag": ("Agenda pour organiser votre année.", "Diary to organise your year.", "أجندة لتنظيم سنتك."),
 "bloc": ("Bloc-notes pratique pour l'école et le bureau.", "Handy notepad for school and the office.", "مذكرة عملية للمدرسة والمكتب."),
 "pap": ("Papier de qualité pour l'école et le bureau.", "Quality paper for school and the office.", "ورق جيد للمدرسة والمكتب."),
 "calc": ("Calculatrice fiable pour l'école et le bureau.", "Reliable calculator for school and the office.", "آلة حاسبة موثوقة للمدرسة والمكتب."),
 "geo": ("Matériel de géométrie précis pour l'école.", "Accurate geometry tools for school.", "أدوات هندسة دقيقة للمدرسة."),
 "pf": ("Petite fourniture indispensable pour l'école et le bureau.", "Essential small supplies for school and the office.", "لوازم صغيرة ضرورية للمدرسة والمكتب."),
 "couv": ("Pour relier, protéger et présenter vos documents.", "To bind, protect and present your documents.", "لتجليد وثائقك وحمايتها وعرضها."),
 "cach": ("Cachets, dateurs et encres pour le bureau.", "Stamps, daters and inks for the office.", "أختام وأختام التاريخ وأحبار للمكتب."),
 "tab": ("Ardoises, brosses, craies et chevalets.", "Slates, board erasers, chalk and easels.", "ألواح وممسحات وطباشير وحوامل."),
 "recu": ("Carnets pour vos factures et reçus.", "Books for your invoices and receipts.", "دفاتر لفواتيرك ووصولاتك."),
 "man": ("Manuel scolaire du programme marocain.", "Textbook for the Moroccan curriculum.", "كتاب مدرسي وفق المنهاج المغربي."),
 "para": ("Manuel et cahier pour l'enseignement privé et le soutien scolaire.", "Textbook and workbook for private schools and tutoring.", "كتاب ودفتر للتعليم الخصوصي والدعم المدرسي."),
 "lit": ("Livre de lecture, roman ou recueil d'histoires.", "Reading book, novel or story collection.", "كتاب قراءة أو رواية أو مجموعة قصص."),
 "isl": ("Mushaf et livres islamiques.", "Qur'an and Islamic books.", "مصاحف وكتب إسلامية."),
}
def S(top, fr, en, ar, d): return (top, fr, en, ar, _D[d])
B, PB, SC, LV, BA = "Bureau & Organisation", "Papeterie & blocs-notes", "Scolaire", "Livres", "Beaux-arts & Loisirs créatifs"
SUBS2 = {
 "paniers": S(B, "Paniers à courrier", "Letter trays", "سلال الرسائل", "bur"),
 "ensbur": S(B, "Ensembles de bureau", "Desk sets", "أطقم المكتب", "bur"),
 "nbook": S(PB, "Notebooks", "Notebooks", "دفاتر الملاحظات", "nb"),
 "agenda": S(PB, "Agendas & calendriers", "Diaries & calendars", "الأجندات والتقويمات", "ag"),
 "blocsp": S(PB, "Blocs-notes à spirale", "Spiral notepads", "مذكرات حلزونية", "bloc"),
 "blocss": S(PB, "Blocs-notes & carnets sans spirale", "Notepads & pocket books", "مذكرات ودفاتر صغيرة", "bloc"),
 "papa4": S(PB, "Papier blanc A4 (ramettes)", "A4 copy paper (reams)", "ورق أبيض A4 (رزم)", "pap"),
 "chem": S(PB, "Chemises", "Folders", "الأغلفة الورقية", "pap"),
 "roul": S(PB, "Rouleaux papier", "Paper rolls", "لفائف الورق", "pap"),
 "env": S(PB, "Enveloppes", "Envelopes", "الأظرفة", "pap"),
 "copie": S(PB, "Copies & recharges", "Loose-leaf exam paper", "الأوراق المزدوجة والبسيطة", "pap"),
 "milli": S(PB, "Papier millimétré", "Graph paper", "الورق الملليمتري", "pap"),
 "calq": S(PB, "Papier calque", "Tracing paper", "ورق الشفاف", "pap"),
 "carb": S(PB, "Papier carbone", "Carbon paper", "ورق الكربون", "pap"),
 "mini": S(PB, "Papier ministre", "Ministre paper", "ورق المنستر", "pap"),
 "brist": S(PB, "Fiches & bristol", "Index cards & bristol", "بطاقات البريستول", "pap"),
 "calc": S(B, "Calculatrices", "Calculators", "الآلات الحاسبة", "calc"),
 "etiq": S(B, "Étiqueteuses", "Price labellers", "آلات الملصقات", "pf"),
 "regle": S(SC, "Règles", "Rulers", "المساطر", "geo"), "equ": S(SC, "Équerres", "Set squares", "الكوسات", "geo"),
 "rapp": S(SC, "Rapporteurs", "Protractors", "المنقلات", "geo"), "kit": S(SC, "Kits de traçage", "Geometry sets", "أطقم الهندسة", "geo"),
 "comp": S(SC, "Compas", "Compasses", "البركار", "geo"),
 "gom": S("Écriture & Correction", "Gommes", "Erasers", "الممحاة", "pf"),
 "cis": S(SC, "Ciseaux", "Scissors", "المقصات", "pf"), "taille": S(SC, "Taille-crayons", "Pencil sharpeners", "المبراة", "pf"),
 "colle": S(B, "Colles, scotch & dévidoirs", "Glue, tape & dispensers", "الغراء والأشرطة اللاصقة", "pf"),
 "agrf": S(B, "Agrafeuses", "Staplers", "الدباسات", "pf"), "agr": S(B, "Agrafes", "Staples", "دبابيس الدباسة", "pf"),
 "arr": S(B, "Arrache-agrafes", "Staple removers", "نازعات الدبابيس", "pf"),
 "postit": S(B, "Post-it & notes repositionnables", "Sticky notes", "الأوراق اللاصقة", "pf"),
 "fix": S(B, "Punaises", "Thumbtacks", "الدبابيس الضاغطة", "pf"), "elas": S(B, "Élastiques", "Rubber bands", "الأربطة المطاطية", "pf"),
 "tromb": S(B, "Trombones & attaches", "Paper clips & fasteners", "مشابك الورق", "pf"),
 "etiqa": S(B, "Étiquettes adhésives", "Adhesive labels", "الملصقات اللاصقة", "pf"),
 "perf": S(B, "Perforateurs", "Hole punches", "الثقابات", "pf"), "moui": S(B, "Mouilleurs", "Finger moisteners", "مبللات الأصابع", "pf"),
 "oeil": S(B, "Œillets", "Reinforcement rings", "حلقات التقوية", "pf"),
 "couv": S(B, "Couvertures & plastification", "Covers & laminating", "الأغلفة والتصفيح", "couv"),
 "poch": S(B, "Pochettes perforées", "Punched pockets", "الجيوب المثقبة", "couv"),
 "serre": S(B, "Serre-feuilles & spirales", "Binding bars & combs", "مشابك ولوالب التجليد", "couv"),
 "cach": S(B, "Cachets", "Self-inking stamps", "الأختام", "cach"), "dat": S(B, "Dateurs", "Date stamps", "أختام التاريخ", "cach"),
 "encr": S(B, "Encres & tampons encreurs", "Stamp ink & pads", "الحبر ووسادات الأختام", "cach"),
 "pbloc": S(B, "Porte-blocs", "Clipboards", "حوامل الأوراق", "bur"),
 "chev": S(B, "Chevalets", "Easels", "الحوامل", "tab"), "brosse": S(B, "Brosses tableau", "Board erasers", "ممسحات السبورة", "tab"),
 "craie": S(B, "Craies", "Chalk", "الطباشير", "tab"),
 "ardel": S(SC, "Ardoises électroniques", "LCD writing tablets", "الألواح الإلكترونية", "tab"),
 "ardn": S(SC, "Ardoises noires", "Chalk slates", "الألواح السوداء", "tab"),
 "ardb": S(SC, "Ardoises blanches", "Whiteboard slates", "الألواح البيضاء", "tab"),
 "recus": S(B, "Reçus & bons", "Receipt & voucher books", "دفاتر الوصولات والسندات", "recu"),
 "m_ar": S(LV, "Manuels arabe", "Arabic textbooks", "كتب اللغة العربية", "man"),
 "m_fr": S(LV, "Manuels français", "French textbooks", "كتب اللغة الفرنسية", "man"),
 "m_en": S(LV, "Manuels anglais", "English textbooks", "كتب اللغة الإنجليزية", "man"),
 "m_ma": S(LV, "Manuels mathématiques", "Mathematics textbooks", "كتب الرياضيات", "man"),
 "m_pc": S(LV, "Manuels physique-chimie", "Physics & chemistry textbooks", "كتب الفيزياء والكيمياء", "man"),
 "m_svt": S(LV, "Manuels SVT", "Life & earth sciences textbooks", "كتب علوم الحياة والأرض", "man"),
 "m_isl": S(LV, "Manuels éducation islamique", "Islamic education textbooks", "كتب التربية الإسلامية", "man"),
 "m_hg": S(LV, "Manuels histoire-géographie", "History & geography textbooks", "كتب التاريخ والجغرافيا", "man"),
 "m_ph": S(LV, "Manuels philosophie", "Philosophy textbooks", "كتب الفلسفة", "man"),
 "m_art": S(LV, "Manuels éducation artistique", "Art education textbooks", "كتب التربية الفنية", "man"),
 "para": S(LV, "Parascolaire", "Revision guides", "الكتب الموازية", "para"),
 "dico": S(LV, "Dictionnaires", "Dictionaries", "القواميس", "lit"),
 "rar": S(LV, "Romans arabes", "Arabic novels", "روايات عربية", "lit"),
 "rfr": S(LV, "Romans & littérature", "Novels & literature", "الروايات والأدب", "lit"),
 "devp": S(LV, "Développement personnel", "Personal development", "التنمية الذاتية", "lit"),
 "isl": S(LV, "Livres islamiques", "Islamic books", "إسلاميات", "isl"),
 "edu": S(LV, "Livres éducatifs", "Educational books", "الكتب التعليمية", "lit"),
 "gomt": S(BA, "Pâte à modeler & créatif", "Modelling clay & crafts", "عجينة التشكيل والأنشطة الإبداعية", "pf"),
}

def rows(shot, key, items, start=0):
    return [(shot, start + i, key) + tuple(it) for i, it in enumerate(items)]

R2 = []
R2 += rows("s30", "paniers", [("panier", "métal 3 niveaux Document Basket Tray", 140, "JS3001"), ("panier", "Deli File Tray", 230, "9181"), ("panier", "métal Crown", 140, "JS2001")])
R2 += rows("s31", "ensbur", [("ens", "Tidy Desktop ARK", 50, "2041"), ("ens", "Office Set ARK", 45, "1305"), ("pot", "Pen Office ARK", 12, "552"), ("pot", "Pen Stand", 15, "DG-6905"), ("pcach", "Exa File", 33, "EX-122")])
R2 += rows("s33", "nbook", [("nb", x, p, r) for x, p, r in [
 ("Luky Stitch à spirale A5", 35, "1103"), ("Ambassador Mini A7", 8, "A7-11"), ("Ambassador A5", 25, "A5-13"), ("Blue Star", 20, "00199500"),
 ("Sky Bluestar à spirale A6", 20, "BTB-5011"), ("Ultra 240 pages B-M à spirale A5", 25, ""), ("à spirale avec stylo", 20, "PP3601"), ("Ambassador A4", 70, ""),
 ("Ambassador A5", 30, "05"), ("Ambassador A6", 20, "A6"), ("Ambassador", 25, "R24"), ("Ambassador", 25, "2511"), ("Ambassador", 45, "6002"),
 ("Ambassador à spirale A5", 20, ""), ("Blue Star", 20, "325039"), ("Car Beaut A6", 22, "5702-1"), ("China", 20, "11-36"), ("China", 25, "LP64K-0619"),
 ("China Palliet", 15, ""), ("Cute Clip A5", 25, "JT7225-2"), ("Cute Clip A6", 21.38, "JT7250-2"), ("Draw Book", 30, "978-2-36091-366-4"),
 ("General", 45, "T1438"), ("Guangben China", 25, "25100-71")]])
R2 += rows("s34", "nbook", [("nb", x, p, r) for x, p, r in [
 ("Hualian A5", 25, "782"), ("Hualian A6", 20, "783"), ("Le Game Book", 30, "978-2-36091-363-3"), ("M&G A5", 45, "APY1FK78"), ("M&G A5", 45, "T1438"),
 ("M&G A6", 8, "A6501"), ("Marocain", 25, ""), ("Tulip China", 12, "1500-17"), ("Ambassador", 20, "NB-06")]])
R2 += rows("s35", "agenda", [("ag", x, p, r) for x, p, r in [("2024 A5", 35, "AG-2501-1"), ("2024 A5", 50, "AG-MJ01"), ("2025 A5 Ambassador", 35, "AG-2501-1"),
 ("2026 A5 Ambassador", 50, "AG-2501-2"), ("2026 A5", 45, "NB1901-1"), ("Hauser 2025 A5", 40, "")]])
R2 += rows("s36", "blocsp", [("bloc", "B-M 100 pages 5/5 à spirale A4", 10, ""), ("bloc", "Ecolo 124 pages à spirale A5", 12, "BLS8003"), ("bloc", "Ecolo 124 pages à spirale A5", 12, "")], 2)
R2 += rows("s37", "blocsp", [("bloc", x, p, r) for x, p, r in [
 ("Ambassador 124 pages à spirale A5", 12, ""), ("B-M 96 pages 5/5 à spirale A4", 20, ""), ("Addouha blanc à spirale A4", 20, ""), ("Addouha à spirale A4", 20, ""),
 ("Addouha à spirale A5", 10, ""), ("Ambassador à spirale A5", 8, "BS01T"), ("Ambassador à spirale A5", 15, "BS05T"), ("B-M à spirale A6", 8, "DF-0002"),
 ("blanc à spirale A5", 12, ""), ("Bleu Star à spirale A4", 20, "BST-A4"), ("Mintra à spirale A5", 30, "10800"), ("Oxford 160 pages à spirale A4", 80, ""),
 ("Oxford 160 pages à spirale A5", 60, ""), ("Panda Express blanc à spirale A4", 20, "DF-0005"), ("Panda Express à spirale A5", 10, "DF-0002"),
 ("blanc à spirale A5", 15, "325041"), ("Steno à spirale A4", 20, ""), ("Steno à spirale A4", 20, "BLS8004")]] + [("carnet", "Koutoubia 96 pages A5", 8, "")])
R2 += rows("s38", "blocss", [("bloc", "Alberta 5/5 100 pages A4", 20, ""), ("bloc", "B-M 5/5 140 pages A6", 8, ""), ("bloc", "Selecta 5/5 100 pages A4", 20, ""),
 ("bloc", "5/5 A5", 7, ""), ("bloc", "AZ 96 pages A5", 18, "1292"), ("bloc", "AZ A6", 14, "1292"), ("bloc", "Med Paper 140 pages A5", 15, ""),
 ("bloc", "Oxford 160 pages A4", 60, ""), ("carnet", "Essentiel 140 pages 5/5 A5", 6, "04.4.002"), ("carnet", "Sylver 96 pages 5/5 A5", 8, ""),
 ("carnet", "B-M 5/5 140 pages A5", 10, ""), ("carnet", "B-M 5/5 140 pages A7", 7, ""), ("carnet", "Essentiel 140 pages A5", 7, ""),
 ("carnet", "Essentiel 96 pages A5", 8, ""), ("carnet", "Sylver 5/5 96 pages A5", 7, "")])
R2 += rows("s40", "papa4", [("ram", x, p, "") for x, p in [("Archer", 60), ("Sigma", 50), ("Copy Paper", 50), ("Copy Star", 50), ("Everyday", 50), ("Inacopia", 70),
 ("Maram", 60), ("Mondi IQ Economy", 50), ("Multicopy", 50), ("Navigator", 70), ("Omnia", 50), ("UPM", 50), ("Superior Extra", 50)]])
R2 += rows("s41", "chem", [("chem", "cartonnée Roling 180 g", 1, ""), ("chem", "cartonnée Safridos 180 g", 1, ""), ("chem", "cartonnée Safridos 180 g", 1, ""),
 ("chem", "à bulle jaune 180 g (200 pièces)", 50, ""), ("chem", "à bulle couleur 180 g (250 pièces)", 60, ""), ("chem", "à bulle Extra jaune 180 g (250 pièces)", 45, ""),
 ("chem", "à bulle GoodBn jaune 180 g (200 pièces)", 45, ""), ("chem", "à bulle Noblesse couleur 180 g A4 (100 pièces)", 50, ""),
 ("chem", "à rabat cartonnée dure", 13, ""), ("chem", "à rabat cartonnée normale", 10, ""), ("chem", "à rabat cartonnée", 10, "HDR-2432")])
R2 += rows("s42", "roul", [("roul", "Panda Express 57/50 mm", 8, ""), ("roul", "Panda Express 80/80 mm", 17, ""), ("roul", "TPE Topkall 57×35 mm", 6, "FB-7326"), ("roul", "TPE 55 g", 6, "")])
R2 += rows("s43", "env", [("env", "jaune A4", 2, ""), ("env", "plastique A4 My Clear", 5, "W-209"), ("env", "jaune A5", 1.5, ""), ("env", "jaune A6", 0.5, ""),
 ("env", "blanche A4", 3, ""), ("env", "blanche Express (paquet)", 35, "XO-0977")])
R2 += rows("s44", "copie", [("copd", "B-M 80 pages 10/10 A4", 12, ""), ("copd", "Essentiel 80 pages 10/10 A4", 10, ""), ("copd", "Mintra 80 pages 17×22", 13, ""),
 ("copd", "B-M 80 pages A5", 6, ""), ("cops", "B-M 80 pages 5/5 A4", 12, ""), ("cops", "Boost-Star 80 pages 5/5 A4", 10, "BO212798055"), ("cops", "Ramette 80 pages 17×22", 6, "")])
R2 += rows("s45", "milli", [("milli", "", 70, "")])
R2 += rows("s46", "calq", [("calq", "Échelle A4", 1, "17-143"), ("calq", "Express A4", 40, "XO-4944"), ("calq", "Sawour A4", 1, "AQ0015")])
R2 += rows("s47", "carb", [("carb", "Copytech noir A4", 60, ""), ("carb", "Express bleu A4", 60, "XO-3886"), ("carb", "Ambassador noir A4", 60, ""),
 ("carb", "Ecolo noir A4", 60, "PPC-1930"), ("carb", "Gestetner jaune", 60, "")])
R2 += rows("s48", "mini", [("mini", "Atlas 5/5 A4", 70, "")])
R2 += rows("s49", "brist", [("fbr", "Anuelle blanc 180 g 5/5 65×50 A1", 3, ""), ("fbr", "blanc 180 g 5/5 A4", 60, ""), ("fbr", "blanc 180 g 5/5 A5", 30, ""),
 ("fbr", "vert 180 g 5/5 A5", 30, ""), ("fbr", "rose 180 g 5/5 A5", 30, ""), ("fbr", "jaune 180 g 5/5 A5", 30, ""), ("fbr", "bleu 180 g 5/5 A5", 30, "")])
R2 += rows("s50", "calc", [("calc", "Deli", 130, "M888")], 2)
R2 += rows("s51", "etiq", [("etiqm", "KEYIDE 2 lignes", 150, "EOS 5500"), ("etiqm", "M&G", 170, "3C117")])
R2 += rows("s52", "calc", [("calc", x, p, r) for x, p, r in [("Accord", 100, "AC-82ES Plus"), ("Atima", 45, "AT-2343B"), ("Casio", 200, "GX-12B-BK"),
 ("Casio fx-991ES Plus", 150, ""), ("Casio fx-991ES Plus", 170, ""), ("Catiga", 100, "CD-2648"), ("Deli", 120, "1654C"), ("Gitizen", 120, "FX-991ES"),
 ("Gitizen", 25, "CT-5 Plus"), ("Kaerda", 60, "KA-82MS"), ("Karuida", 50, "KK-82MS-D"), ("M&G", 40, "ADG981B9"), ("Shina", 22, "")]])
R2 += rows("s54", "regle", [("regle", x, p, r) for x, p, r in [("Ark 30 cm", 5, "179"), ("Ark 50 cm", 10, "145"), ("Boost 20 cm", 4, "BS-RL400"), ("Deli 20 cm", 4, "H10"),
 ("Deli 20 cm", 4, "G00212"), ("Deli 30 cm", 6, "G00312"), ("Express 100 cm", 25, "PR-1"), ("Express 30 cm", 5, "XO5569"), ("Express flexible 20 cm", 4, "XJ-3695"),
 ("M-School 20 cm", 3, "MS-2434"), ("Maped 20 cm", 5, "14108"), ("Maxime 20 cm", 2, "R-20")]])
R2 += rows("s55", "equ", [("equ", x, p, r) for x, p, r in [("Deli 11 cm", 5, "G10112"), ("Express flexible 12 cm", 4, "XJ-5729"), ("M-School 12 cm", 3, "MS-2444"),
 ("Maped Cristal", 5, "146120"), ("Turbo", 3, "JM4802")]])
R2 += rows("s56", "rapp", [("rapp", x, p, r) for x, p, r in [("Ambassador", 3, "TC-4810-1"), ("Ark 180°", 3, "180/008"), ("Deli", 4, "G102"), ("M-School", 3, "MS-2454"), ("Maped", 5, "146134")]])
R2 += rows("s57", "kit", [("kit", "Ark", 20, "023-6C"), ("kit", "Deli", 15, "G00412"), ("kit", "Deli", 15, "H22")])
R2 += rows("s58", "comp", [("comp", x, p, r) for x, p, r in [("Accord", 20, "SPM1471"), ("Aosdu", 20, ""), ("China", 20, "3017"), ("China", 10, "V90"), ("écolier Rio", 8, "C1809"),
 ("ensemble Y-Plus", 35, "MS250100"), ("métal Aosdu", 10, "A-003"), ("métal Express", 10, "4009"), ("métal Hi-Pro", 25, "C598"), ("métal King Gift", 12, "4506"),
 ("métal Smart", 25, "2506"), ("métal Maped Study", 25, "119410"), ("métal Deli", 20, "G20102"), ("métal Deli", 25, "8601"), ("métal Deli", 35, "8604"),
 ("métal Deli", 20, "G-20402"), ("métal Y-Plus", 20, "CS180400")]])
R2 += rows("s59", "gom", [("gom", x, p, r) for x, p, r in [("Accord", 4, ""), ("Accord", 5, "GB0063"), ("BIC", 8, "AXPQ557"), ("Deli", 8, "H03110"), ("Deli", 8, "H308"),
 ("Hashtag Savor", 3, "GM0052"), ("M&G", 7, "AXPQ4271"), ("M&G Roller", 8, "AXPQ5571"), ("Maped Technic", 4, "011300"), ("Maped Technic", 8, "011600"),
 ("Yoeker", 1, "YK-688"), ("Yoeker grand modèle", 2, "YK-688")]])
R2 += rows("s60", "cis", [("cis", x, p, r) for x, p, r in [("Boost", 10, "806"), ("DL", 30, "3189"), ("DL", 25, "3189"), ("Deli", 25, "6009"), ("Deli", 25, "6013"), ("Deli", 40, "77750"),
 ("Express Junior", 8, "XJ-5071"), ("M&G", 30, "ASS913A3"), ("M&G", 25, "ASS91435"), ("Maped", 15, "464412"), ("Maxime écolier", 10, "SP100/30"), ("Smart", 10, "AS009"),
 ("Deli avec protège-lame", 10, "D60200"), ("Nepo Cisorex avec protège-lame", 8, "359-2")]])
R2 += rows("s61", "taille", [("tc", x, p, r) for x, p, r in [("Ballon China", 5, ""), ("Deli", 5, "H-010-EG"), ("Deli", 10, "H-011-EG"), ("Deli", 10, "H551"), ("Keyroad métal", 2, "KR971132"),
 ("King Story", 3, "KG1052"), ("M-School", 5, "MS-378A"), ("M-School", 5, "MS-379"), ("M-School", 5, "MS-8132"), ("Maped", 10, ""), ("Polot", 5, "PO-088"),
 ("Y-Plus", 10, "G-F"), ("Y-Plus+", 10, ""), ("Deli", 8, "0545"), ("Deli", 8, "0594"), ("Handli", 5, "CL-128"), ("Tip-Top", 4, "900"), ("Deli", 10, "39768"),
 ("Y-Plus+", 3, "SX120700"), ("Deli", 10, "0576"), ("Mash Malow 2 trous", 4, "KR971684")]])
R2 += rows("s62", "colle", [("cblanc", "Boost 80 g", 10, "BO-CB80G"), ("cliq", "", 3, ""), ("cstick", "BIC 21 g", 10, ""), ("cstick", "BIC 36 g", 15, ""),
 ("cstick", "Deli 15 g", 7, "7104"), ("cstick", "Deli 36 g", 13, "7103"), ("cstick", "Deli 9 g", 5, "7101"), ("cstick", "Savour 21 g", 8, "GLS0021"),
 ("cstick", "Savour 36 g", 10, "GLS0036"), ("cstick", "Smart 9 g", 5, "S999"), ("cstick", "UHU 21 g", 15, ""), ("cstick", "UHU 8,5 g", 8, ""),
 ("ctube", "UHU n°12", 8, ""), ("ctube", "UHU n°13", 15, ""), ("ctube", "UHU 21 g", 10, "12"), ("ctube", "UHU 7 g", 5, ""),
 ("dev", "DL Office", 22, "DL20051"), ("dev", "DL Office", 40, "DL2208"), ("dev", "Deli", 25, "814A"), ("dev", "School Smart", 40, "17802"),
 ("rub", "Dophine grand format jaune", 10, ""), ("rub", "Scotch grand format jaune", 10, ""), ("rub", "Scotch grand format marron", 10, ""), ("rub", "Scotch grand format marron renforcé", 15, "")])
R2 += rows("s63", "colle", [("rub", "Scotch grand format rouge", 10, ""), ("rub", "Scotch grand format transparent", 17, ""), ("rub", "Scotch grand format vert", 10, ""),
 ("rub", "Scotch petit format blanc (lot de 2)", 3, ""), ("rub", "Scotch petit format noir", 4, ""), ("rub", "grand format transparent", 15, ""),
 ("rub", "Ecolo petit format blanc", 4, "RLSE1833"), ("rub", "double face Mounting Tape 900 g", 10, ""), ("rub", "décoratif", 4, "DRP18T4C1"), ("sglue", "Mika Fix", 10, "")])
R2 += rows("s64", "agrf", [("agrf", x, p, r) for x, p, r in [("Accord 24/6", 60, "G1"), ("Alevar Jolly 6/2", 45, "64-JOLLY"), ("Boost 24/6", 10, "BO-0368"), ("Boston 24/6", 60, "BS1212"),
 ("DL 24/6", 35, "DL0318"), ("DL", 15, "DL0152"), ("DL", 25, "DL0397"), ("Deli", 35, "0435"), ("Deli à pince", 60, "0346"), ("Deli Pro", 300, "0487"),
 ("Deli", 35, "0300"), ("Deli", 35, "0350"), ("Deli", 60, "0357"), ("Ecolo à pince", 60, "AGFE150"), ("Express 24/6", 60, "XO-755"), ("Huisheng à pince", 65, "HS850-30"),
 ("Deli à pince Pro", 60, "0346S"), ("Deli à pince", 80, "39803")]])
R2 += rows("s65", "agr", [("agr", x, p, r) for x, p, r in [("Boost 24/6", 7, "BO-2222"), ("Boston n°10", 5, ""), ("DL Dingli 24/6", 8, "DL.519"), ("DL n°10", 4, ""),
 ("DL 24/6", 5, "DL2222"), ("Deli 10/10", 6, "0010N"), ("Deli 24/6", 7, "0012N"), ("Delta 24/6", 8, "1551"), ("Grat Hall 24/6", 4, "369"), ("8/4A", 3, "")]])
R2 += rows("s66", "arr", [("arr", "Accord", 10, "AAG001"), ("arr", "Deli", 10, "0231")])
R2 += rows("s67", "postit", [("notes", "Beautone Stickon", 15, ""), ("ephem", "2025", 20, "550050"), ("notes", "Info Notes 125×75 mm", 15, "5655-32"),
 ("notes", "Note Paper 80×80 mm (600 feuilles)", 30, "ZH-701"), ("notes", "Post-it ARK blanc", 25, "5671"), ("notes", "Post-it China", 10, "GS-02"),
 ("notes", "Stick Note", 12, "GS-19"), ("notes", "Kai Si Te A05", 15, "A05")])
R2 += rows("s68", "fix", [("pun", "DL Office 10 mm", 4, "DL121"), ("pun", "Thumb Tacks 10 mm", 4, "")])
R2 += rows("s69", "elas", [("elas", x, p, r) for x, p, r in [("Rubber Hand 200 g", 25, ""), ("Alba 80/60 100 g", 17, ""), ("Deli boîte 70 mm 50 g", 20, "3214"),
 ("Panda Express 100 g", 17, ""), ("Panda Express 50 g", 10, ""), ("Rubber Hand 50 g", 10, "")]])
R2 += rows("s70", "tromb", [("attp", "Everywhere", 10, ""), ("attp", "China", 15, ""), ("pdc", "Deli 19 mm", 2, "8555S"), ("tromb", "DL Office 32 mm", 7, ""),
 ("tromb", "Boston 28 mm", 7, "2111"), ("tromb", "Fermacli 32 mm", 7, ""), ("tromb", "M Office 50 mm", 8, ""), ("tromb", "couleur Haoxiang 33 mm", 6, "83330")])
R2 += rows("s71", "etiqa", [("etq", "adhésives en rouleau", 15, ""), ("etq", "rondes Ambassador", 10, "2018"), ("etq", "Ambassador", 10, "ET05"),
 ("etq", "autoadhésives (10 feuilles)", 10, ""), ("etq", "scolaires Ambassador", 5, "BSD-106"), ("etq", "scolaires Ecolo", 5, "ETS525"),
 ("etq", "scolaires Ecolo illustrées", 15, "ETS525"), ("etq", "de prix Super Market", 5, "400F-R"), ("gommet", "Ambassador", 8, "BSD-100"),
 ("stk", "Smile", 5, ""), ("stk", "Happy", 3, "")])
R2 += rows("s72", "perf", [("perf", "Accord 2 trous", 25, "SPM0542")])
R2 += rows("s73", "moui", [("moui", "Deli", 25, "9190"), ("moui", "humidificateur", 7, "")])
R2 += rows("s74", "oeil", [("oeil", "Ecolo (200 pièces)", 8, "ETS-1171")])
R2 += rows("s75", "couv", [("couvpvc", "Casber A4", 80, "A4-150"), ("couvpvc", "Express A4", 2, "A4-150"), ("plast", "216×303 mm 125 µ A4", 150, ""),
 ("carton", "Eurochrome blanc A4 250 g", 2, "C250G")], 2)
R2 += rows("s76", "poch", [("poch", "Deli", 70, "F20102"), ("poch", "Bendermax A4 (100 pièces)", 1, "W-25-1"), ("poch", "Memory (100 pièces)", 50, "EF-303"),
 ("poch", "Express (100 pièces)", 50, "EF-303"), ("poch", "OBO A4 (100 pièces)", 80, "EF-303")])
R2 += rows("s77", "serre", [("serre", "20 mm", 4, "NSR20"), ("serre", "8 mm", 3, "NSR8"), ("spir", "16 mm", 3, ""), ("spir", "20 mm", 4, "")])
R2 += rows("s79", "cach", [("cach", "Imprint 11 38×14 mm", 60, "8912"), ("cach", "Imprint 12 47×18 mm", 50, "8912"), ("cach", "MobiStamps 12 18×47 mm", 60, "C4312"),
 ("cach", "MobiStamps 22×58 mm", 60, "C4313"), ("cach", "MobiStamps rond RC30", 80, "C4312"), ("cach", "« Payé »", 25, "CS-001")])
R2 += rows("s80", "dat", [("dat", "Accord arabe", 10, "Datar12"), ("dat", "Boston français", 10, "D4"), ("dat", "ZhongYuan français", 15, "ZY-400")])
R2 += rows("s81", "encr", [("encre", "Crown", 8, "E030B"), ("encre", "Huhua Endorsing", 8, "30CC"), ("tamp", "Boost", 15, "BO-126RD"), ("tamp", "Memory bleu", 15, "126B"),
 ("tamp", "Memory rouge", 15, "126R"), ("tamp", "Memory vert", 15, "126V"), ("encre", "Ecolo", 8, "Ink024B")])
R2 += rows("s82", "pbloc", [("pbl", "illustré Chine", 15, "TC23-1454")])
R2 += rows("s83", "chev", [("chev", "Ambassador", 150, "120")], 3)
R2 += rows("s84", "ardb", [("ardb", "M-School", 20, "MS-B03020B")], 3)
R2 += rows("s85", "ardel", [("arde", 'Saving 10"', 30, ""), ("arde", 'Saving 8,5"', 25, "LC1522"), ("arde", 'Smart 10"', 35, "AM10"), ("arde", 'Smart 12"', 50, "AM12"), ("arde", 'Smart 8,5"', 30, "AM08")])
R2 += rows("s86", "ardn", [("ardn", "Express", 10, "XJ-0243"), ("ardn", "double face Alif", 12, "AL-3169"), ("ardn", "double face Ambassador", 10, ""), ("ardn", "Alif", 10, "AI-00229")])
R2 += rows("s87", "ardb", [("ardb", "BIC Velleda", 35, ""), ("ardb", "Esloma", 10, "A-4"), ("ardb", "Y-Plus", 30, "WB240102"), ("ardb", "Alif", 20, "AF-6020"), ("ardb", "Alif", 10, "AL-3152")])
R2 += rows("s88", "brosse", [("brosse", x, p, r) for x, p, r in [("China", 5, ""), ("Ambassador", 8, "223"), ("blanche Ambassador", 8, "168"), ("blanche Deli", 10, "7837"),
 ("blanche Gnawi", 5, "G-1141"), ("blanche Magic", 5, "LF-513"), ("blanche Sourie", 10, ""), ("blanche Stylex", 15, "ART-606"), ("Express", 5, "XJ-0113")]])
R2 += rows("s89", "craie", [("craie", x, p, r) for x, p, r in [("blanche Giotto Robercolor", 8, ""), ("couleur Giotto Robercolor", 10, ""), ("blanche Maped", 10, "593500"),
 ("blanche Express", 5, "X04852"), ("couleur Express", 8, "XO-4869"), ("couleur Maped", 12, "593501"), ("blanche Veda", 7, "DCC-3")]])
R2 += rows("s90", "recus", [("fact", "Al Yakin A5", 8, "50×2"), ("fact", "El Ouardi", 8, ""), ("recu", "El Ouardi 80 feuilles", 10, ""), ("recu", "80 feuilles", 10, "")])

# ---- Livres : titres (identiques dans les 3 langues) ; sous-rayon déterminé par la matière ----
def subj(t):
    l = t.lower()
    if any(k in t for k in ("الفلسفة",)): return "m_ph"
    if any(k in t for k in ("التربية الاسلامية", "التربية الإسلامية")): return "m_isl"
    if any(k in t for k in ("التربية الفنية", "التشكيلية", "التربية الفني")): return "m_art"
    if any(k in t for k in ("الاجتماعيات", "التاريخ")): return "m_hg"
    if "الرياضيات" in t or "math" in l: return "m_ma"
    if any(k in l for k in ("physique", "pc 3ac")): return "m_pc"
    if any(k in l for k in ("svt", "sciences", "science")): return "m_svt"
    if any(k in l for k in ("english", "spotlight")): return "m_en"
    if any(k in l for k in ("fran", "parcours")): return "m_fr"
    return "m_ar"
LITA = {
 "s91": [("في رحاب التربية الاسلامية 2 ابتدائي", 11), ("Al Moufid Math 3AC", 49), ("English Spotlight 2", 16), ("English Spotlight 2 Activity", 12), ("Étincelle Maths", 40),
  ("Étincelle Physique 1AC", 35), ("Étincelle Physique Chimie 3AC", 35), ("Étincelle SVT Manuel 3AC", 35), ("Je réussis pas à pas Français 1AC", 15),
  ("Je réussis pas à pas en Français 3AC", 15), ("Je réussis pas à pas en Mathématiques 2AC", 17), ("Je réussis pas à pas en Sciences 1AC", 16),
  ("Je réussis pas à pas en Mathématiques 1AC", 17), ("Je réussis pas à pas en Physique Chimie 1AC", 15), ("Je réussis pas à pas en Physique Chimie 2AC", 15),
  ("L'univers Physique Chimie 2AC", 130), ("L'univers de SVT 2AC", 130), ("Le Français au Collège 2AC", 17), ("Mes apprentissages en Français", 22),
  ("Parcours Français 1AC", 18), ("Sigma Physique Chimie 1AC", 30), ("Spotlight 1 Activity", 11), ("Spotlight 1 Student Book", 16), ("SVT Azzedine Alami 3AC", 25)],
 "s92": [("Univers Plus Physique 2AC", 35), ("Univers Plus SVT 3AC", 32), ("Univers Plus PC 3AC", 35), ("احياء التربية الاسلامية 2 اعدادي", 14),
  ("الاساسي في التربية الفنية 3 ابتدائي", 10.5), ("الاساسي في اللغة العربية 3 اعدادي", 25), ("التربية التشكيلية الممتع 1 ابتدائي", 9),
  ("الجديد في الاجتماعيات 5 ابتدائي", 17), ("الجديد في الاجتماعيات 6 ابتدائي", 19), ("الدليل في تطبيقات اللغة العربية 1 ابتدائي", 45),
  ("الدليل في تطبيقات اللغة العربية 3 ابتدائي", 45), ("الرائد في التربية الاسلامية 3 اعدادي", 16), ("الرائد في اللغة العربية 1 اعدادي", 22),
  ("المختار في التربية الفنية 2 ابتدائي", 10.4), ("المرجع في الرياضيات 3 ابتدائي", 14), ("المعتمد في التربية الفنية 6 ابتدائي", 16),
  ("المفيد في الاجتماعيات 5 ابتدائي", 17), ("المفيد في الرياضيات 1 ابتدائي", 11), ("المفيد في اللغة العربية 1 اعدادي", 22),
  ("الممتاز في التربية الاسلامية 3 ابتدائي", 10), ("الممتاز في التربية الاسلامية 5 ابتدائي", 10), ("المنير في التربية الاسلامية 3 ابتدائي", 9.6),
  ("المنير في التربية الفنية 6 ابتدائي", 16), ("المنير في اللغة العربية 5 ابتدائي", 25), ("النجاح في الاجتماعيات 2 اعدادي", 22)],
 "s93": [("حكايتي الجميلة متعتي 5/4 حكاية مشروع 1", 17), ("حكايتي الجميلة متعتي 5/4 حكاية مشروع 2", 17), ("حكايتي الجميلة متعتي 5/4 حكاية مشروع 3", 17),
  ("رؤية 5-6", 24), ("سيكما التاريخ والجغرافية 2 اعدادي", 30), ("طريقي الى النجاح 2 اعدادي", 15), ("طريقي الى النجاح في اللغة العربية 1 اعدادي", 15),
  ("طريقي الى النجاح في اللغة العربية 3 اعدادي", 15), ("عالم التربية الفنية 1 ابتدائي", 9), ("فضاء الاجتماعيات 1 اعدادي", 22), ("فضاء الرياضيات 2 ابتدائي", 13.5),
  ("فضاء في الاجتماعيات 2 اعدادي", 22), ("في رحاب الاجتماعيات 1 اعدادي", 22), ("في رحاب التربية الاسلامية", 12), ("في رحاب التربية الاسلامية 1 ابتدائي", 16),
  ("في رحاب التربية الاسلامية 1 اعدادي", 16), ("في رحاب التربية الاسلامية 5 ابتدائي", 10), ("في رحاب الفلسفة 1 بكالوريا", 23), ("في رحاب اللغة العربية 6 ابتدائي", 25.2),
  ("كتابي في اللغة العربية 1 ابتدائي", 15.5), ("كتابي في اللغة العربية 2 ابتدائي", 18), ("كتابي في اللغة العربية 6 ابتدائي", 26), ("كراسة اللغة العربية 3 ابتدائي", 30),
  ("متعتي في التخطيط والكتابة 5/4", 35), ("متعتي في الكتابة التفاعلية 1 ابتدائي", 40)],
 "s94": [("متعتي في بداية التعلم المشروع 1 الجسم والتغذية والنظافة 5/4", 30), ("متعتي في بداية التعلم المشروع 2 الاسرة والبيت 5/4", 30),
  ("متعتي في بداية التعلم المشروع 3 الحي ومرافقه 5/4", 30), ("مرشدي في اللغة العربية 3 ابتدائي", 23.5), ("مرشدي في اللغة العربية 5 ابتدائي", 25),
  ("منار الاجتماعيات 3 اعدادي", 25), ("منار التربية الاسلامية 1 بكالوريا", 22), ("منار التربية الاسلامية 3 اعدادي", 16), ("منار التربية الاسلامية 5 ابتدائي", 10),
  ("مورد التاريخ والجغرافية 1 بكالوريا", 40), ("واحة اللغة العربية 1 بكالوريا", 32)],
}
for shot, items in LITA.items():
    R2 += [(shot, i, subj(t), "", t, p, "") for i, (t, p) in enumerate(items)]
PARA = {
 "s95": [("الدليل في تطبيقات اللغة العربية 2 ابتدائي", 45, "24-648-1"), ("Acro Sciences CE1", 50), ("Archipel Maths 1re CP", 110), ("Archipel Maths 2e CE1", 100),
  ("Archipel Maths 5e CM2", 85), ("Archipel Maths CE2", 110), ("Buzz Student Book 6 (Oxford)", 180), ("Buzz Workbook 6 (Oxford)", 110), ("Cap Maths CE2 Maroc — Fichier de l'élève", 130),
  ("Capucines Collection CM2", 290), ("Citronnelle Français CP livres 1 et 2 (éd. 2025)", 145), ("Coccinelle Cahier d'activités 1 CP", 95), ("Coccinelle Cahier d'activités 2 CP", 100),
  ("Coccinelle Cahier d'écriture CP", 95), ("Coccinelle Méthode de lecture CP", 175), ("Capucines CE1 Pack", 285), ("Croque-Feuilles CE2", 365), ("Croque-Pages CE1", 380),
  ("Étincelle SVT Activités 3AC", 90), ("Citronnelle Français CE2", 145), ("Citronnelle Français CE2 Activités", 110), ("Go Global Student Book 5", 150),
  ("Go Global Workbook 5", 115), ("Go Global Workbook 2", 120)],
 "s96": [("Go Global Student Book 2", 140), ("Génie des Sciences CM2 5e", 110), ("Génie des Maths Plus 6 AP", 170), ("Génie des Maths Plus", 150),
  ("Génie des Sciences F-C — دفتر التقصي", 120), ("Hashtag English 2", 270), ("Happy Hearts 1 Activity Book", 115), ("Happy Hearts 1 Pupil's Book", 70),
  ("I Wonder 5 SB+WB", 270), ("Info Robotique & IA 3", 85), ("Informatique Robotique & IA 5 CM2", 90), ("Informatique Robotique & IA 2AC", 98),
  ("Informatique et Robotique 1AC", 90), ("Informatique, robotique et intelligence artificielle 6 AP", 85), ("I Wonder 1 Student Book + Activity Book", 220),
  ("I Wonder 2 Pupil's Book + Activity Book", 270), ("I Wonder 3 Pupil's Book + Activity Book", 260), ("I Wonder 4 Pupil's Book + Activity Book", 270),
  ("Je progresse en écriture CE1", 50), ("Kid's Bridge English 1st SB/WB", 140), ("Kid's Box 1 Activity Book (Cambridge)", 130), ("Kid's Box 1 Pupil's Book (Cambridge)", 150),
  ("Kid's Bridge 3rd Pupil's Book + Activity Book", 150), ("L'Archipel des Maths 2AC", 140), ("L'Azur des Lettres 5", 270)],
 "s97": [("L'Univers des Maths 3AC", 170, "978-9920-766-23-4"), ("La Nouvelle Coccinelle CM2", 220), ("La Cité des sciences CP", 60),
  ("Le Nouveau Vivre le Français — Cahier d'activités 1 CM2", 70), ("Le Nouveau Vivre le Français — Cahier d'activités 2 CM2", 70),
  ("Le Nouveau Vivre le Français — Cahier d'écriture CM2", 45), ("Le Nouveau Vivre le Français — Livre unique CM2", 150), ("Les Cahiers Istra Sciences", 75, "76/3409/8"),
  ("Les Cahiers de la Luciole CM2", 95), ("Mot de Passe — Cahier d'activités CE2", 130), ("Mot de Passe — Livre CE2", 230), ("Maestro Science CE2", 85),
  ("Maestro Science CP — Manuel", 90), ("Micro Maths 1re CP", 100), ("Mon Labo en Sciences CM2", 50), ("Parcours Français 6 AP", 22), ("Ping Pong 2 Activity Book", 85),
  ("Ping Pong 2 Pupil's Book", 130), ("Plan Comptable Général Marocain", 40, "4787339"), ("Plume d'école MS — Cahier d'écriture", 65), ("Plume d'école MS — Cahier de Français", 120),
  ("Plume d'école MS — Cahier de Maths et découverte du monde", 100), ("Plume d'école MS — Pack Album", 200), ("Rives Bleues Français 6e", 220), ("Rives Bleues Français 4e 2AC", 220)],
 "s98": [("Sigma Physique 2AC", 30), ("Splash Activity Book 3", 115), ("Splash Student Book 3", 160), ("Taoki et Compagnie — Cahier d'écriture CP", 90),
  ("Taoki et Compagnie — Cahier d'exercices 1", 110, "62/9770/8"), ("Taoki et Compagnie — Cahier d'exercices 2", 110, "86/8560/4"),
  ("Taoki et Compagnie — Manuel de l'élève", 170, "62/9746/2"), ("Think 1 Workbook 2AP", 130), ("Think 1 Student Book 2AP", 220)],
}
for shot, items in PARA.items():
    R2 += [(shot, i, "para", "", it[0], it[1], it[2] if len(it) > 2 else "") for i, it in enumerate(items)]
R2 += [("s98", 9, "rar", "", "الحب في الربيع — ميخائيل خوري", 70, "")]
R2 += [("s99", 0, "dico", "", "Larousse — Mon premier dictionnaire", 80, "")]
STORIES = {
 "u00": [("Biblio Collège — Contes de Charles Perrault", 70), ("Cinderella", 12), ("Collection Histoires des Prophètes", 10), ("Candide — Voltaire", 40),
  ("Contes du Monde", 10), ("من روائع القصص العالمية — EdiFun", 10), ("سلسلة الطفل المغامر — Edisoft", 10), ("Good Manners", 10), ("Histoires Universelles", 10),
  ("La Boîte à Merveilles — Ahmed Sefrioui", 25), ("La Bonne Moralité", 10), ("Le Bourgeois Gentilhomme — Molière", 35), ("Le Dernier Jour d'un Condamné — Victor Hugo", 20),
  ("Le Bibliobus CE2 Cycle 2 — Ali Baba et les 40 voleurs", 130), ("Les Mille et Une Nuits", 10), ("Les Mères des Croyants", 10),
  ("Série Histoires pour l'éducation positive", 10), ("Wonders of Stories", 10), ("أسرار عقل المليونير — هارف إيكر", 60), ("أمهات المؤمنين", 10),
  ("ألف ليلة وليلة", 10), ("جبل الماس — أحمد عبد السلام البقالي", 10), ("حكايات كان يا مكان", 15), ("حكاية كان يا مكان", 12)],
 "u01": [("دمعة وابتسامة — جبران خليل جبران", 25), ("رجوع إلى الطفولة — ليلى أبو زيد", 23), ("رواية أرض السافلين", 70), ("رواية القادمون", 70), ("رواية أهل الكهف", 20),
  ("سلسلة قصص الحيوانات — خليل بحري", 10), ("قصة الحطاب الأمين", 10), ("من أجمل القصص التربوية", 10), ("نوادر جحا", 12)],
}
import re as _re
for shot, items in STORIES.items():
    for i, (t, p) in enumerate(items):
        k = "devp" if "المليونير" in t else ("rar" if _re.match(r"[؀-ۿ]", t) else "rfr")
        R2.append((shot, i, k, "", t, p, ""))
R2 += [("u02", i, "isl", "", t, p, "") for i, (t, p) in enumerate([("غلاف القرآن الكريم A4", 28), ("غلاف القرآن الكريم A5", 22), ("القرآن الكريم 60 حزب A4", 80),
  ("القرآن الكريم — تفسير ابن كثير 60 حزب A5", 60), ("مصحف التجويد الواضح 60 حزب A5 مغلف", 120), ("مصحف التجويد الواضح 60 حزب A6 مغلف", 55),
  ("الفاتحة وجزء قد سمع", 15), ("سورة البقرة وسورة آل عمران", 20), ("مصحف التجويد الواضح — جزء تبارك", 15), ("مصحف التجويد الواضح — جزء قد سمع", 15),
  ("مصحف التجويد الواضح — سورة البقرة", 25), ("مصحف التجويد — جزء عمّ", 15)])]
R2 += [("u03", 0, "edu", "", "اكتب وامسح — L'Alphabet français", 12, "")]
R2 += [("u04", 17, "gomt", "gpq", "", 10, "")]

NO_PHOTO2 = {("s42", 2), ("s54", 5), ("s93", 3), ("s96", 3), ("s96", 22)}

def build():
    """Renvoie [(shot, idx, key, (fr, en, ar), prix, ref, flags)] sans doublons exacts."""
    out, seen_np, names = [], set(), {}
    for shot, idx, key, ty, rest, price, ref in R2:
        tf, te, ta = TY[ty]
        if ty == "":
            fr = en = ar = rest
        else:
            fr = (tf + " " + rest).strip(); en = (rest + " " + te).strip() if rest else te[0].upper() + te[1:]
            ar = (ta + " " + rest).strip()
            en = en[0].upper() + en[1:]
        k = (fr.lower(), float(price))
        if k in seen_np: continue          # même produit, même prix : affiché une seule fois
        seen_np.add(k)
        if fr in names:                      # même nom, autre modèle : on précise
            names[fr] += 1
            suf = f" réf. {ref}" if ref and f"réf. {ref}" not in fr else f" (modèle {names[fr]})"
            fr2 = fr + suf
            while fr2 in names: names[fr] += 1; fr2 = fr + f" (modèle {names[fr]})"
            sufe = suf.replace("réf.", "ref.").replace("modèle", "model"); sufa = suf.replace("réf.", "المرجع").replace("modèle", "نموذج")
            fr, en, ar = fr2, en + sufe, ar + sufa
        names.setdefault(fr, 1)
        out.append((shot, idx, key, (fr, en, ar), price, ref, ""))
    return out
