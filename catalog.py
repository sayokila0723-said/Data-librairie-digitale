# Catalogue LCH Library — prix indicatifs en Dhs (marché marocain, 2026)
# (nom, prix normal, prix promo ou None, description courte, type d'image, couleur, drapeaux)
# drapeaux : "f" = coup de cœur (mis en avant), "n" = nouveauté

C = {}

def cat(path, items):
    C[path] = items

# ───────────── 1. ÉCRITURE & CORRECTION ─────────────
cat("Écriture & Correction > Stylos à bille", [
    ("Stylo à bille BIC Cristal Original bleu", 2, None, "Le classique indémodable : pointe moyenne 1 mm, encre fluide, corps transparent.", "pen", "#1f4fbf", "f"),
    ("Stylo à bille BIC Cristal Original noir", 2, None, "Pointe moyenne 1 mm, écriture nette et régulière.", "pen", "#222222", ""),
    ("Stylo à bille BIC Cristal Original rouge", 2, None, "Idéal pour la correction et les titres.", "pen", "#d62828", ""),
    ("Stylo à bille BIC Cristal Original vert", 2, None, "Pointe moyenne 1 mm, couleur verte franche.", "pen", "#2a9d4b", ""),
    ("Boîte de 50 stylos BIC Cristal bleu", 95, 85, "Le format économique pour le bureau ou la classe.", "penbox", "#1f4fbf", "f"),
    ("Stylo 4 couleurs BIC classique", 15, None, "Bleu, noir, rouge et vert dans un seul stylo rétractable.", "pen4", "#1f4fbf", "f"),
    ("Stylo à bille Faber-Castell Tri-Flow 1 mm bleu", 3, None, "Corps triangulaire pour une prise en main confortable.", "pen", "#2457a6", ""),
])
cat("Écriture & Correction > Stylos gel & effaçables", [
    ("Stylo gel Pilot G-2 0,7 mm bleu", 13, None, "Encre gel rétractable, écriture douce et sans bavure.", "gelpen", "#1f4fbf", "f"),
    ("Stylo gel Pilot G-2 0,7 mm noir", 13, None, "Le stylo gel préféré des étudiants.", "gelpen", "#222222", ""),
    ("Stylo effaçable Pilot FriXion Clicker 0,7 mm bleu", 16, None, "Effacez et réécrivez sans abîmer le papier.", "gelpen", "#2c7be5", "fn"),
    ("Stylo gel BIC Gel-ocity 0,5 mm noir", 6, None, "Pointe fine, séchage rapide.", "gelpen", "#333333", ""),
    ("Lot de 3 recharges FriXion bleu", 22, None, "Recharges pour stylos effaçables Pilot FriXion 0,7 mm.", "refill", "#2c7be5", ""),
])
cat("Écriture & Correction > Feutres & marqueurs", [
    ("Marqueur permanent Edding 3000 noir", 14, None, "Écrit sur presque tout : carton, plastique, métal.", "marker", "#222222", ""),
    ("Marqueur tableau blanc Maped — lot de 4", 32, 28, "Bleu, noir, rouge, vert. Effaçable à sec.", "markerset", "#1f4fbf", "f"),
    ("Feutre fin Stabilo Point 88 — étui de 10", 85, None, "Pointe fine 0,4 mm, 10 couleurs vives pour l'écriture et le dessin.", "fineliners", "#f28c28", "n"),
    ("Marqueur tableau blanc Pentel noir", 12, None, "Pointe ogive, encre sans odeur forte.", "marker", "#111111", ""),
])
cat("Écriture & Correction > Surligneurs", [
    ("Surligneur Stabilo Boss Original jaune", 9, None, "Le surligneur de référence, encre anti-séchage 4 h.", "highlighter", "#f7e017", "f"),
    ("Surligneurs Stabilo Boss — pochette de 4", 36, 32, "Jaune, vert, rose et orange.", "hlset", "#f7e017", ""),
    ("Surligneurs pastel Stabilo Boss — pochette de 6", 58, None, "Six teintes douces pour des fiches de révision élégantes.", "hlset", "#f4a6c9", "n"),
])
cat("Écriture & Correction > Crayons & porte-mines", [
    ("Crayon graphite HB Staedtler Noris", 4, None, "Le crayon d'écolier jaune et noir, mine résistante.", "pencil", "#f7c714", ""),
    ("Boîte de 12 crayons HB Staedtler Noris", 42, None, "Avec gomme en bout. Pour l'école et le bureau.", "pencilbox", "#f7c714", "f"),
    ("Porte-mine Pentel 0,5 mm", 18, None, "Mécanisme précis, grip caoutchouc.", "mechpencil", "#1b1f2a", ""),
    ("Étui de mines 0,5 mm HB", 8, None, "12 mines de rechange pour porte-mine.", "leads", "#444444", ""),
])
cat("Écriture & Correction > Gommes & taille-crayons", [
    ("Gomme blanche Staedtler Mars Plastic", 6, None, "Efface proprement sans abîmer le papier.", "eraser", "#1f4fbf", ""),
    ("Taille-crayon double avec réservoir Maped", 9, None, "Deux trous, lames en acier, réservoir transparent.", "sharpener", "#2a9d4b", ""),
    ("Lot gomme + taille-crayon Maped", 12, None, "Le duo indispensable de la trousse.", "eraser", "#e63946", ""),
])
cat("Écriture & Correction > Correcteurs", [
    ("Correcteur en ruban Tipp-Ex Mini Pocket Mouse", 14, None, "Ruban 5 mm × 6 m, réécriture immédiate.", "tape_corr", "#e63946", "f"),
    ("Correcteur liquide en flacon 20 ml", 9, None, "Pinceau applicateur, séchage rapide.", "bottle", "#ffffff", ""),
    ("Stylo correcteur pointe métal", 10, None, "Pour corrections précises sur les petits caractères.", "corrpen", "#ffffff", ""),
])

# ───────────── 2. CAHIERS & PAPETERIE ─────────────
cat("Cahiers & Papeterie > Cahiers petit format 17×22", [
    ("Cahier piqûre 48 pages grands carreaux 17×22", 6, None, "Papier 72 g, couverture souple.", "notebook", "#e63946", ""),
    ("Cahier piqûre 96 pages grands carreaux 17×22", 8, None, "Le cahier le plus demandé sur les listes scolaires.", "notebook", "#1f4fbf", "f"),
    ("Cahier piqûre 192 pages grands carreaux 17×22", 16, None, "Pour les matières principales, papier 72 g.", "notebook", "#2a9d4b", ""),
    ("Cahier de textes 128 pages 17×22", 15, None, "Pour noter devoirs et leçons tout au long de l'année.", "notebook", "#8e44ad", ""),
])
cat("Cahiers & Papeterie > Cahiers grand format A4 & 24×32", [
    ("Cahier A4 96 pages Seyès", 17, None, "Grand format 21×29,7, papier 72 g.", "notebook", "#f28c28", ""),
    ("Cahier 24×32 96 pages Seyès", 19, None, "Format classeur, idéal pour coller les photocopies.", "notebook", "#1f4fbf", ""),
    ("Cahier A4 200 pages grands carreaux", 20, None, "Gros volume pour toute l'année.", "notebook", "#2a9d4b", ""),
    ("Cahier spirale A4 180 pages petits carreaux", 32, 28, "Spirale double, pages microperforées.", "spiral", "#1d3557", "n"),
])
cat("Cahiers & Papeterie > Cahiers TP, dessin & musique", [
    ("Cahier de travaux pratiques 96 pages 17×22", 10, None, "Une page dessin, une page grands carreaux.", "notebook", "#f7c714", ""),
    ("Cahier de dessin 24×32 48 pages 120 g", 18, None, "Papier blanc épais pour crayons et feutres.", "sketch", "#ffffff", ""),
    ("Cahier de musique 48 pages", 12, None, "Portées imprimées, format 17×22.", "notebook", "#6c4ab6", ""),
])
cat("Cahiers & Papeterie > Blocs-notes & Post-it", [
    ("Bloc-notes A5 spirale 100 feuilles", 14, None, "Feuilles détachables, petits carreaux.", "spiral", "#2c7be5", ""),
    ("Post-it 76×76 mm jaune — bloc de 100", 12, None, "Notes repositionnables, adhésif fiable.", "postit", "#f7e017", "f"),
    ("Post-it néon 76×76 — lot de 6 blocs", 62, 55, "Couleurs vives pour ne rien oublier.", "postitset", "#ff5fa2", ""),
    ("Marque-pages adhésifs 5 couleurs", 15, None, "Index transparents pour annoter livres et dossiers.", "flags", "#2a9d4b", "n"),
])
cat("Cahiers & Papeterie > Papier A4 & papier couleur", [
    ("Ramette papier A4 80 g Navigator — 500 feuilles", 65, None, "Papier premium, blancheur extrême, pour toutes imprimantes.", "ream", "#1d3557", "f"),
    ("Ramette papier A4 80 g économique — 500 feuilles", 52, 49, "Le bon rapport qualité-prix pour l'impression courante.", "ream", "#2a9d4b", ""),
    ("Carton de 5 ramettes A4 80 g", 260, 240, "L'approvisionnement du mois pour le bureau.", "reambox", "#1d3557", ""),
    ("Papier couleur A4 80 g pastel assorti — 100 feuilles", 28, None, "5 couleurs douces pour affiches et travaux manuels.", "colorpaper", "#ffd6a5", ""),
    ("Papier dessin Canson 24×32 180 g — 10 feuilles", 25, None, "Grain fin, pour crayons, feutres et gouache.", "sketch", "#ffffff", ""),
])
cat("Cahiers & Papeterie > Enveloppes & courrier", [
    ("Enveloppes blanches 11×22 — boîte de 50", 25, None, "Fermeture autocollante, format courrier.", "envelope", "#ffffff", ""),
    ("Enveloppes kraft A4 — paquet de 10", 18, None, "Pour documents grand format sans pliage.", "envelope", "#c9a26b", ""),
    ("Étiquettes adhésives A4 — 100 feuilles", 75, None, "Planches pour adresses et classement, compatibles imprimante.", "labels", "#ffffff", ""),
])

# ───────────── 3. CLASSEMENT & ARCHIVAGE ─────────────
cat("Classement & Archivage > Classeurs & intercalaires", [
    ("Classeur à levier dos 8 cm bleu", 28, None, "Format 32×28, mécanisme à levier robuste.", "binder", "#1d3557", "f"),
    ("Classeur à levier dos 8 cm noir", 28, None, "Format 32×28, étiquette de dos interchangeable.", "binder", "#222222", ""),
    ("Classeur à levier dos 8 cm rouge", 28, None, "Couleur vive pour repérer vos dossiers.", "binder", "#c62828", ""),
    ("Classeur 4 anneaux dos 4 cm", 22, None, "Couverture rigide, pour cours et documents.", "binder", "#2a9d4b", ""),
    ("Jeu de 12 intercalaires plastique couleur", 25, None, "Onglets imprimables pour organiser vos classeurs.", "dividers", "#f28c28", ""),
])
cat("Classement & Archivage > Chemises & pochettes", [
    ("Chemise cartonnée — lot de 10 couleurs", 15, None, "Carte 180 g, couleurs assorties.", "folders", "#f7c714", ""),
    ("Chemise à rabats élastique 24×32", 9, None, "Trois rabats et élastique de fermeture.", "folder", "#1f4fbf", ""),
    ("Pochettes perforées A4 — paquet de 100", 35, None, "Transparentes, 11 trous, pour classeurs.", "sleeves", "#dfe8f3", "f"),
    ("Porte-vues 40 vues A4", 22, None, "Présentez et protégez vos documents.", "displaybook", "#222222", ""),
])
cat("Classement & Archivage > Boîtes d'archives", [
    ("Boîte d'archives carton dos 10 cm", 11, None, "Montage facile, carton recyclé.", "archive", "#c9a26b", ""),
    ("Boîte d'archives carton dos 16 cm", 13, None, "Grande capacité pour l'archivage annuel.", "archive", "#e9e3d6", ""),
    ("Lot de 10 boîtes d'archives dos 10 cm", 100, 95, "Le pack économique pour vos archives.", "archive", "#c9a26b", ""),
])
cat("Classement & Archivage > Trieurs & parapheurs", [
    ("Trieur 12 compartiments à soufflet", 45, None, "Pour trier factures et courriers.", "accordion", "#1d3557", ""),
    ("Parapheur 18 compartiments", 65, None, "Dos extensible, pages buvard.", "parapheur", "#7a1f2b", ""),
])

# ───────────── 4. SCOLAIRE ─────────────
cat("Scolaire > Cartables & sacs à dos", [
    ("Cartable primaire 2 compartiments", 175, 159, "Dos rembourré, bretelles réglables, poche frontale.", "bag", "#2c7be5", "f"),
    ("Cartable à roulettes 18 pouces", 420, 389, "Poignée télescopique et roulettes silencieuses.", "trolley", "#e63966", "f"),
    ("Sac à dos collège 3 poches", 249, None, "Grand volume, compartiment ordinateur 15\".", "bag", "#1d3557", ""),
    ("Sac à goûter isotherme", 59, None, "Garde le goûter au frais toute la journée.", "lunchbag", "#2a9d4b", "n"),
])
cat("Scolaire > Trousses", [
    ("Trousse double zip", 39, None, "Deux compartiments, tissu résistant.", "pouch", "#8e44ad", ""),
    ("Trousse ronde simple", 25, None, "Compacte et légère.", "pouch", "#e63946", ""),
    ("Trousse garnie 25 pièces", 129, 115, "Stylos, crayons, feutres, règle, gomme… prête pour la rentrée.", "pouchfull", "#2c7be5", "f"),
])
cat("Scolaire > Géométrie", [
    ("Règle plate 30 cm", 6, None, "Graduation lisible, plastique transparent.", "ruler", "#dfe8f3", ""),
    ("Kit de traçage 4 pièces 30 cm Maped", 25, None, "Règle, équerre, rapporteur, double décimètre.", "geoset", "#2c7be5", "f"),
    ("Compas Maped Study avec crayon", 18, None, "Bague de serrage, mine incluse.", "compass", "#1d3557", ""),
    ("Équerre 21 cm 60°", 15, None, "Flexible et incassable.", "setsquare", "#f28c28", ""),
    ("Rapporteur 180° 12 cm", 5, None, "Double graduation.", "protractor", "#dfe8f3", ""),
])
cat("Scolaire > Colle, ciseaux & accessoires", [
    ("Bâton de colle UHU Stic 21 g", 15, None, "Sans solvant, lavable, pour papier et carton.", "gluestick", "#f7c714", ""),
    ("Bâton de colle UHU Stic 40 g", 27, None, "Grand format pour toute l'année.", "gluestick", "#f7c714", ""),
    ("Ciseaux écolier 13 cm bouts ronds", 12, None, "Lames inox, poignée souple.", "scissors", "#2a9d4b", ""),
    ("Protège-cahiers 17×22 — lot de 10 couleurs", 25, None, "PVC épais avec porte-étiquette.", "covers", "#e63946", ""),
])
cat("Scolaire > Ardoises", [
    ("Ardoise blanche effaçable + feutre + chiffon", 29, None, "Format A4, double face lignée/blanche.", "slate", "#ffffff", "n"),
    ("Ardoise noire avec cadre bois", 22, None, "Pour la craie, cadre solide.", "slate", "#1b1f2a", ""),
    ("Boîte de 100 craies blanches", 18, None, "Craies antipoussière.", "chalk", "#ffffff", ""),
])
cat("Scolaire > Calculatrices scientifiques", [
    ("Calculatrice scientifique Casio fx-82MS", 149, None, "240 fonctions, idéale du collège au lycée.", "calc_sci", "#1b1f2a", "f"),
    ("Calculatrice scientifique Casio fx-991ES Plus", 260, 239, "417 fonctions, affichage naturel des formules.", "calc_sci", "#2b2f3a", ""),
    ("Calculatrice de poche 8 chiffres", 15, None, "Simple et légère pour le primaire.", "calc", "#e63946", ""),
])

# ───────────── 5. BUREAU & ORGANISATION ─────────────
cat("Bureau & Organisation > Agrafage & perforation", [
    ("Agrafeuse de bureau 24/6 métal", 55, None, "Capacité 25 feuilles, chargement par le dessus.", "stapler", "#1b1f2a", "f"),
    ("Agrafes 24/6 — boîte de 1000", 6, None, "Compatibles avec la plupart des agrafeuses.", "staples", "#9aa3ad", ""),
    ("Mini agrafeuse + agrafes n°10", 15, None, "Format poche, idéale pour la trousse.", "stapler", "#2c7be5", ""),
    ("Perforatrice 2 trous 20 feuilles", 49, None, "Guide de format, réservoir à confettis.", "punch", "#222222", ""),
    ("Dégrafeuse", 8, None, "Retire les agrafes sans déchirer.", "remover", "#e63946", ""),
])
cat("Bureau & Organisation > Petite fourniture", [
    ("Trombones 28 mm — boîte de 100", 6, None, "Acier nickelé, anti-rouille.", "clips", "#9aa3ad", ""),
    ("Pinces double clip 32 mm — boîte de 12", 18, None, "Tiennent fermement jusqu'à 120 feuilles.", "binderclip", "#222222", ""),
    ("Ruban adhésif transparent 19 mm × 33 m", 6, None, "Invisible et résistant.", "tape", "#dfe8f3", ""),
    ("Dévidoir de bureau + ruban adhésif", 35, None, "Base lestée, coupe nette.", "dispenser", "#1d3557", ""),
    ("Cutter 18 mm lame sécable", 15, None, "Blocage de lame, poignée antidérapante.", "cutter", "#f7c714", ""),
    ("Élastiques assortis — sachet de 100 g", 12, None, "Caoutchouc naturel.", "rubberbands", "#c9a26b", ""),
])
cat("Bureau & Organisation > Calculatrices de bureau", [
    ("Calculatrice de bureau 12 chiffres", 65, None, "Grand écran, double alimentation solaire/pile.", "calc", "#1b1f2a", "f"),
    ("Calculatrice imprimante Casio HR-8RCE", 449, 419, "Impression des tickets, idéale pour la comptabilité.", "calc_print", "#2b2f3a", ""),
])
cat("Bureau & Organisation > Rangement de bureau", [
    ("Module de rangement 4 tiroirs", 180, 159, "Tiroirs coulissants, empilable.", "drawers", "#e63966", "f"),
    ("Corbeille à courrier A4 empilable", 29, None, "Pour trier entrées et sorties de courrier.", "tray", "#1d3557", ""),
    ("Pot à crayons métal maille", 25, None, "Design épuré, base antidérapante.", "penholder", "#222222", ""),
    ("Organiseur de bureau en bois 6 cases", 145, None, "Range stylos, notes et documents.", "organizer", "#d9b98a", "n"),
])
cat("Bureau & Organisation > Tableaux & cachets", [
    ("Tableau blanc magnétique 60×90 cm", 320, 289, "Cadre aluminium, auget porte-marqueurs.", "whiteboard", "#ffffff", ""),
    ("Brosse magnétique pour tableau blanc", 25, None, "Efface proprement, se range sur le tableau.", "brush_board", "#1d3557", ""),
    ("Tampon dateur automatique", 89, None, "Date en français, encrage automatique.", "stamp", "#1b1f2a", ""),
])

# ───────────── 6. BEAUX-ARTS & LOISIRS CRÉATIFS ─────────────
cat("Beaux-arts & Loisirs créatifs > Crayons de couleur", [
    ("Crayons de couleur Maped Color'Peps — 12", 25, None, "Mine tendre, corps triangulaire.", "colorpencils", "#e63946", "f"),
    ("Crayons de couleur Faber-Castell — 24", 49, None, "Couleurs lumineuses, mine résistante.", "colorpencils", "#2a9d4b", ""),
    ("Crayons de couleur Jumbo — 12", 45, 39, "Gros format pour les petites mains.", "colorpencils", "#f28c28", ""),
    ("Boîte métal 36 crayons de couleur", 120, None, "Pour les artistes en herbe, boîte de rangement.", "colortin", "#1d3557", "n"),
])
cat("Beaux-arts & Loisirs créatifs > Feutres de coloriage", [
    ("Feutres de coloriage Maped — 12", 22, None, "Encre lavable, pointe bloquée.", "felts", "#2c7be5", ""),
    ("Feutres de coloriage Maped — 24", 39, None, "24 couleurs lavables.", "felts", "#8e44ad", "f"),
    ("Feutres pinceau aquarellables — 12", 89, None, "Pointe pinceau souple pour lettering et aquarelle.", "brushpens", "#ff5fa2", "n"),
])
cat("Beaux-arts & Loisirs créatifs > Peinture", [
    ("Gouache en tubes — 10 couleurs", 45, None, "Couleurs couvrantes et mélangeables.", "tubes", "#f7c714", "f"),
    ("Peinture acrylique 100 ml bleu", 22, None, "Séchage rapide, résistante à l'eau.", "acrylic", "#2c7be5", ""),
    ("Peinture acrylique 100 ml rouge", 22, None, "Séchage rapide, résistante à l'eau.", "acrylic", "#e63946", ""),
    ("Coffret aquarelle 24 pastilles", 65, None, "Avec pinceau, pour débuter l'aquarelle.", "watercolor", "#2a9d4b", ""),
])
cat("Beaux-arts & Loisirs créatifs > Pinceaux & accessoires", [
    ("Set de 12 pinceaux synthétiques", 55, None, "Pointes rondes et plates, toutes tailles.", "brushes", "#8b5a2b", "f"),
    ("Palette de peinture 10 godets", 12, None, "Plastique facile à nettoyer.", "palette", "#ffffff", ""),
    ("Gobelet anti-renversement", 15, None, "Pour rincer les pinceaux sans dégâts.", "cup", "#2c7be5", ""),
])
cat("Beaux-arts & Loisirs créatifs > Carnets de croquis & toiles", [
    ("Carnet de croquis A4 spirale 100 g — 50 feuilles", 35, None, "Papier dessin blanc pour tous médiums secs.", "sketchbook", "#1b1f2a", ""),
    ("Toile sur châssis 30×40 cm", 48, None, "Coton apprêté, prête à peindre.", "canvas", "#ffffff", ""),
    ("Lot de 3 toiles 20×20 cm", 55, 49, "Parfait pour les petits formats et les ateliers.", "canvas", "#ffffff", ""),
])
cat("Beaux-arts & Loisirs créatifs > Pâte à modeler & créatif", [
    ("Pâte à modeler 10 couleurs", 25, None, "Ne sèche pas, couleurs vives.", "clay", "#e63946", ""),
    ("Papier crépon — 10 rouleaux couleurs", 39, None, "Pour décorations et travaux manuels.", "crepe", "#ff5fa2", ""),
    ("Kit de perles et bijoux enfant", 79, None, "Plus de 500 perles pour créer bracelets et colliers.", "beads", "#8e44ad", "n"),
])

# ───────────── 7. INFORMATIQUE & CONSOMMABLES ─────────────
cat("Informatique & Consommables > Clés USB & stockage", [
    ("Clé USB 32 Go USB 3.0", 69, None, "Transfert rapide, capuchon de protection.", "usb", "#1b1f2a", ""),
    ("Clé USB 64 Go USB 3.0", 95, 85, "Grande capacité pour cours, photos et projets.", "usb", "#2c7be5", "f"),
    ("Disque dur externe 1 To", 590, None, "Portable, USB 3.0, pour sauvegarder tous vos fichiers.", "hdd", "#222222", ""),
])
cat("Informatique & Consommables > Claviers, souris & casques", [
    ("Souris sans fil", 89, 75, "Récepteur nano, autonomie 12 mois.", "mouse", "#1b1f2a", "f"),
    ("Clavier AZERTY USB", 99, None, "Touches silencieuses, résistant aux éclaboussures.", "keyboard", "#1b1f2a", ""),
    ("Pack clavier + souris sans fil", 199, 179, "Un seul récepteur pour les deux.", "kbmouse", "#2b2f3a", ""),
    ("Casque filaire avec micro", 129, None, "Pour les cours en ligne et les appels.", "headset", "#1b1f2a", "n"),
])
cat("Informatique & Consommables > Cartouches & toners", [
    ("Cartouche d'encre HP 305 noire", 145, None, "Cartouche d'origine pour imprimantes HP DeskJet.", "cartridge", "#1b1f2a", ""),
    ("Cartouche d'encre HP 305 couleur", 165, None, "Cyan, magenta, jaune.", "cartridge", "#2c7be5", ""),
    ("Cartouche Canon PG-445 noire", 159, None, "Pour imprimantes Canon PIXMA.", "cartridge", "#e63946", ""),
    ("Toner compatible HP 85A", 230, 210, "Environ 1600 pages, qualité laser nette.", "toner", "#1b1f2a", ""),
])
cat("Informatique & Consommables > Câbles & piles", [
    ("Piles alcalines AA — lot de 4", 25, None, "Longue durée pour calculatrices et télécommandes.", "batteries", "#f28c28", ""),
    ("Piles alcalines AAA — lot de 4", 25, None, "Pour souris, jouets et petits appareils.", "batteries", "#2c7be5", ""),
    ("Câble HDMI 1,5 m", 39, None, "Haute définition pour écran et vidéoprojecteur.", "cable", "#1b1f2a", ""),
])

# ───────────── 8. LIVRES ─────────────
cat("Livres > Dictionnaires", [
    ("Dictionnaire Le Robert Micro", 95, None, "Le dictionnaire de référence du collège au lycée.", "book", "#c62828", "f"),
    ("Dictionnaire Larousse de poche", 69, None, "Compact et complet pour la trousse ou le cartable.", "book", "#2a9d4b", ""),
    ("Dictionnaire bilingue français-arabe de poche", 45, None, "Plus de 30 000 mots dans les deux sens.", "book", "#1d3557", ""),
    ("Dictionnaire d'anglais illustré", 49, None, "Vocabulaire essentiel avec illustrations.", "book", "#2c7be5", ""),
])
cat("Livres > Parascolaire", [
    ("Bescherelle — La conjugaison pour tous", 110, None, "Les tableaux de conjugaison de tous les verbes.", "book", "#e63946", "f"),
    ("Cahier de vacances CE2 vers CM1", 45, None, "Révisions de français et de maths pour l'été.", "book", "#f7c714", ""),
    ("Annales du Bac mathématiques — sujets corrigés", 85, None, "Sujets d'examen avec corrigés détaillés.", "book", "#1d3557", "n"),
])
cat("Livres > Romans & littérature", [
    ("Le Petit Prince — Antoine de Saint-Exupéry", 59, None, "Le conte poétique pour petits et grands.", "book", "#2c7be5", "f"),
    ("Les Misérables — Victor Hugo (édition abrégée)", 75, None, "Le grand roman de Victor Hugo, version accessible.", "book", "#7a1f2b", ""),
    ("La Boîte à merveilles — Ahmed Sefrioui", 35, None, "Classique de la littérature marocaine au programme.", "book", "#c9a26b", ""),
    ("Le Dernier Jour d'un condamné — Victor Hugo", 25, None, "Œuvre étudiée au collège, édition de poche.", "book", "#222222", ""),
])
cat("Livres > Jeunesse", [
    ("Contes classiques illustrés — recueil", 65, None, "Les plus beaux contes pour les 5-8 ans.", "book", "#ff5fa2", ""),
    ("Mon imagier français-arabe", 55, None, "Plus de 300 mots illustrés pour apprendre en s'amusant.", "book", "#2a9d4b", "n"),
    ("Livre de coloriage magique", 25, None, "Coloriages codés pour réviser le calcul.", "book", "#f28c28", ""),
])

# ───────────── 9. JEUX & LOISIRS ─────────────
cat("Jeux & Loisirs > Jeux éducatifs", [
    ("Jeu éducatif des lettres", 85, 69, "Apprendre l'alphabet en s'amusant, dès 4 ans.", "puzzle", "#2a9d4b", "f"),
    ("Boulier de calcul en bois", 59, None, "100 perles pour apprendre à compter.", "abacus", "#c9a26b", ""),
    ("Kit de science « Petit chimiste »", 149, None, "Expériences simples et sans danger, dès 8 ans.", "sciencekit", "#2c7be5", "n"),
])
cat("Jeux & Loisirs > Puzzles", [
    ("Puzzle 500 pièces paysage", 99, None, "Pour un moment de détente en famille.", "puzzle", "#2c7be5", ""),
    ("Puzzle enfant 48 pièces", 45, None, "Grandes pièces épaisses, dès 4 ans.", "puzzle", "#f28c28", ""),
])
cat("Jeux & Loisirs > Jeux de société", [
    ("Jeu d'échecs pliant en bois", 120, None, "Plateau 30×30 cm, pièces rangées à l'intérieur.", "chess", "#8b5a2b", "f"),
    ("Jeu de cartes UNO", 45, None, "Le jeu de cartes familial incontournable.", "cards", "#e63946", ""),
    ("Dominos en bois — 28 pièces", 35, None, "Boîte de rangement incluse.", "dominoes", "#1b1f2a", ""),
])

# ───────────── CATALOGUE RÉEL (relevé du logiciel de caisse) ─────────────
import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__)) + "/"
import real_catalog as RC
_REPLACED_TOPS = ("Écriture & Correction", "Classement & Archivage")
_REPLACED_SUBS = ("Cahiers & Papeterie > Cahiers petit format 17×22", "Cahiers & Papeterie > Cahiers grand format A4 & 24×32",
                  "Cahiers & Papeterie > Cahiers TP, dessin & musique", "Informatique & Consommables > Cartouches & toners",
                  "Livres > Romans & littérature")
_old = {k: v for k, v in C.items() if k.split(" > ")[0] not in _REPLACED_TOPS and k not in _REPLACED_SUBS}
_old = {k.replace("Cahiers & Papeterie > ", "Papeterie & blocs-notes > "): v for k, v in _old.items()}
_real = {}
for (shot, idx, key, names, price, ref, flags) in RC.R:
    top, sub = RC.SUBS[key][0], RC.SUBS[key][1]
    d = RC.SUBS[key][4]
    extra = dict(photo=None if (shot, idx) in RC.NO_PHOTO else f"{BASE}real/photos/{shot}_{idx:02d}.jpg",
                 ref=ref, en=names[1], ar=names[2], short3=d, real=True)
    short = d[0] + (f" Réf. {ref}." if ref else "")
    _real.setdefault(f"{top} > {sub}", []).append((names[0], price, None, short, "notebook" if key in ("tpa4",) else "pen", "#1f4fbf", flags, extra))

TOP_ORDER = ["Écriture & Correction", "Cahiers", "Classement & Archivage", "Papeterie & blocs-notes", "Scolaire",
             "Bureau & Organisation", "Beaux-arts & Loisirs créatifs", "Informatique & Consommables", "Livres", "Jeux & Loisirs"]
_merged = {}
for t in TOP_ORDER:
    _rk = [f"{v[0]} > {v[1]}" for v in RC.SUBS.values()]
    subs = [k for k in _old if k.split(" > ")[0] == t]
    for k in _rk:
        if k.split(" > ")[0] == t and k in _real and k not in subs: subs.append(k)
    subs.sort(key=lambda k: (0 if ("Manuels" in k) else 1, (_rk.index(k) if k in _rk and k not in _old else 999)))
    for k in subs:
        _merged[k] = _old.get(k, []) + _real.get(k, [])
C = _merged

CAT_DESC = {
    "Écriture & Correction": "Stylos à bille, stylos à encre, crayons, marqueurs, surligneurs et correcteurs.",
    "Cahiers": "Cahiers A5 et A4, à spirale, de travaux pratiques, cahiers de textes et registres.",
    "Classement & Archivage": "Boîtes d'archives, classeurs, porte-documents et parapheurs.",
    "Papeterie & blocs-notes": "Blocs-notes, Post-it, papier A4, papier couleur et enveloppes.",
    "Scolaire": "Cartables, trousses, géométrie et calculatrices pour une rentrée réussie.",
    "Bureau & Organisation": "Agrafeuses, petite fourniture, rangement et tableaux pour le bureau.",
    "Beaux-arts & Loisirs créatifs": "Crayons de couleur, peinture, pinceaux et activités créatives.",
    "Informatique & Consommables": "Clés USB, souris, claviers, cartouches et toners.",
    "Livres": "Manuels scolaires, dictionnaires, parascolaire, romans et livres jeunesse.",
    "Jeux & Loisirs": "Jeux éducatifs, puzzles et jeux de société.",
}

def products():
    out = []
    n = 0
    for path, items in C.items():
        for it in items:
            name, reg, sale, short, kind, color, flags = it[:7]
            extra = it[7] if len(it) > 7 else {}
            n += 1
            out.append(dict(sku=f"LD-{n:03d}", name=name, cats=path, regular=f"{float(reg):g}" if isinstance(reg, float) else str(reg),
                            sale="" if sale is None else str(sale), short=short, kind=kind, color=color,
                            featured="f" in flags, new="n" in flags, **extra))
    return out

if __name__ == "__main__":
    P = products()
    print(len(P), "produits,", len(C), "sous-catégories")
    for p in P:
        assert p["sale"] == "" or float(p["sale"]) < float(p["regular"]), p
