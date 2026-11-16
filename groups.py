# Grandes familles du menu « Catégories » (inspiré de Nova Bureau)
# Chaque famille : (nom FR, EN, AR, icône, description FR/EN/AR, entrées)
# Entrée = sous-groupe (nom FR, EN, AR, [sous-rayons], rayon existant ou None) ou sous-rayon direct (texte)

def SG(fr, en, ar, subs, top=None): return (fr, en, ar, subs, top)

GROUPS = [
 ("Fourniture de bureau", "Office supplies", "اللوازم المكتبية", "briefcase",
  ("Écriture, classement, papeterie et petit matériel pour le bureau.", "Writing, filing, paper and small office equipment.", "الكتابة، الترتيب، الورق واللوازم الصغيرة للمكتب."),
  [SG("Écriture & correction", "Writing & correction", "الكتابة والتصحيح",
      ["Stylos à bille", "Stylos à encre & recharges", "Stylos effaçables", "Crayons", "Marqueurs tableau", "Marqueurs permanents", "Surligneurs", "Correcteurs", "Recharges marqueur tableau"], "Écriture & Correction"),
   SG("Classement & archivage", "Filing & archiving", "الترتيب والأرشفة",
      ["Boîtes d'archives", "Classeurs & intercalaires", "Porte-documents", "Trieurs & parapheurs"], "Classement & Archivage"),
   SG("Papeterie", "Paper", "الورق", ["Blocs-notes & Post-it", "Papier A4 & papier couleur"]),
   SG("Petit matériel de bureau", "Small office equipment", "اللوازم المكتبية الصغيرة",
      ["Agrafage & perforation", "Petite fourniture", "Calculatrices de bureau", "Rangement de bureau"])]),
 ("Informatique & Accessoires", "IT & accessories", "المعلوميات والإكسسوارات", "mouse",
  ("Cartouches, stockage et accessoires informatiques.", "Cartridges, storage and computer accessories.", "الخراطيش، التخزين وإكسسوارات الحاسوب."),
  [SG("Consommables", "Consumables", "المستهلكات", ["Cartouches & toners"]),
   SG("Stockage", "Storage", "التخزين", ["Clés USB & stockage"]),
   SG("Accessoires", "Accessories", "الإكسسوارات", ["Claviers, souris & casques", "Câbles & piles"])]),
 ("Services généraux", "General services", "الخدمات العامة", "star",
  ("Courrier, affichage et tampons pour l'entreprise.", "Mail, display boards and stamps for businesses.", "البريد، السبورات والأختام للمقاولات."),
  [SG("Courrier & expédition", "Mail & shipping", "البريد والإرسال", ["Enveloppes & courrier"]),
   SG("Affichage & tampons", "Boards & stamps", "السبورات والأختام", ["Tableaux & cachets"])]),
 ("Livres et cultures", "Books & culture", "الكتب والثقافة", "books",
  ("Manuels scolaires, parascolaire, dictionnaires, romans et jeunesse.", "Textbooks, revision guides, dictionaries, novels and children's books.", "الكتب المدرسية، الموازية، القواميس، الروايات وكتب الأطفال."),
  ["Manuels scolaires", "Parascolaire", "Dictionnaires", "Romans & littérature", "Jeunesse"]),
 ("Scolaire", "School", "اللوازم المدرسية", "backpack",
  ("Cahiers, cartables, trousses et matériel pour une rentrée réussie.", "Notebooks, school bags, pencil cases and equipment for back to school.", "الدفاتر، المحافظ، المقالم ولوازم الدخول المدرسي."),
  [SG("Cahiers", "Notebooks", "الدفاتر",
      ["Cahiers petit format A5 (17×22)", "Cahiers grand format A4 (21×29,7)", "Cahiers à spirale A5", "Cahiers à spirale A4",
       "Cahiers de travaux pratiques A5", "Cahiers de travaux pratiques A4", "Cahiers de textes", "Registres & cahiers à sujets"], "Cahiers"),
   SG("Cartables & trousses", "School bags & pencil cases", "المحافظ والمقالم", ["Cartables & sacs à dos", "Trousses"]),
   SG("Matériel scolaire", "School equipment", "الأدوات المدرسية", ["Géométrie", "Colle, ciseaux & accessoires", "Ardoises", "Calculatrices scientifiques"])]),
 ("Jeux et loisirs", "Games & leisure", "الألعاب والترفيه", "abacus",
  ("Jeux éducatifs, puzzles et jeux de société.", "Educational games, puzzles and board games.", "ألعاب تعليمية، ألغاز وألعاب جماعية."),
  ["Jeux éducatifs", "Puzzles", "Jeux de société"]),
 ("Beaux arts", "Fine arts", "الفنون الجميلة", "palette",
  ("Crayons de couleur, feutres, peinture, pinceaux et loisirs créatifs.", "Colouring pencils, felt pens, paint, brushes and crafts.", "أقلام التلوين، الأقلام اللبادية، الصباغة، الفرش والأنشطة الإبداعية."),
  ["Crayons de couleur", "Feutres de coloriage", "Peinture", "Pinceaux & accessoires", "Carnets de croquis & toiles", "Pâte à modeler & créatif"]),
]
