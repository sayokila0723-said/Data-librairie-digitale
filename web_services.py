# Marketing digital, communication digitale et création d'écosystème web
# Prix indicatifs « à partir de » — à ajuster selon vos tarifs.

GROUP = ("web", "rocket",
         {"fr": "Marketing digital & création web", "en": "Digital marketing & web creation", "ar": "التسويق الرقمي وإنشاء المواقع"},
         {"fr": "Site web, boutique en ligne, réseaux sociaux et publicité : nous construisons votre présence en ligne de A à Z.",
          "en": "Website, online shop, social media and ads: we build your online presence from A to Z.",
          "ar": "موقع إلكتروني، متجر رقمي، شبكات التواصل والإعلانات: نبني حضورك على الإنترنت من الألف إلى الياء."})

def P(fr, en, ar): return (fr, en, ar)

SERVICES = [
    ("web", "globe", *P("à partir de 3 000 Dhs", "from 3,000 Dhs", "ابتداءً من 3000 درهم"),
     {"fr": ("Création de site web vitrine", "Site moderne et adapté au mobile pour présenter votre activité : pages, formulaire de contact, WhatsApp, carte."),
      "en": ("Business website", "Modern mobile-friendly site to showcase your business: pages, contact form, WhatsApp, map."),
      "ar": ("إنشاء موقع تعريفي", "موقع عصري ومتوافق مع الهاتف لتقديم نشاطك: صفحات، استمارة تواصل، واتساب، خريطة.")}, True),
    ("web", "cart", *P("à partir de 6 000 Dhs", "from 6,000 Dhs", "ابتداءً من 6000 درهم"),
     {"fr": ("Création de boutique en ligne", "E-commerce complet : catalogue produits, panier, commande WhatsApp ou paiement en ligne, livraison."),
      "en": ("Online shop creation", "Complete e-commerce: product catalogue, cart, WhatsApp orders or online payment, delivery."),
      "ar": ("إنشاء متجر إلكتروني", "متجر متكامل: كتالوج المنتجات، سلة، طلب عبر واتساب أو أداء إلكتروني، توصيل.")}, True),
    ("web", "play", *P("à partir de 400 Dhs", "from 400 Dhs", "ابتداءً من 400 درهم"),
     {"fr": ("Création de chaîne YouTube", "Création et configuration de la chaîne, bannière, logo, description optimisée et première vidéo en ligne."),
      "en": ("YouTube channel setup", "Channel creation and setup, banner, logo, optimised description and first video online."),
      "ar": ("إنشاء قناة يوتيوب", "إنشاء القناة وإعدادها، الغلاف، الشعار، وصف محسَّن ونشر أول فيديو.")}, False),
    ("web", "share", *P("à partir de 300 Dhs", "from 300 Dhs", "ابتداءً من 300 درهم"),
     {"fr": ("Page Facebook & compte Instagram", "Création de la page Facebook et du compte Instagram professionnel, visuels de profil et de couverture, liaison WhatsApp."),
      "en": ("Facebook page & Instagram account", "Creation of your Facebook page and Instagram business account, profile and cover visuals, WhatsApp link."),
      "ar": ("صفحة فيسبوك وحساب إنستغرام", "إنشاء صفحة فيسبوك وحساب إنستغرام احترافي، صور الملف والغلاف، وربطهما بواتساب.")}, False),
    ("web", "pin", *P("300 Dhs", "300 Dhs", "300 درهم"),
     {"fr": ("Fiche Google Maps (Google Business)", "Votre commerce visible sur Google Maps et la recherche Google : horaires, photos, téléphone, avis clients."),
      "en": ("Google Maps listing (Google Business)", "Your business on Google Maps and Google Search: hours, photos, phone, customer reviews."),
      "ar": ("بطاقة خرائط Google", "ظهور محلك على خرائط Google ومحرك البحث: الساعات، الصور، الهاتف وآراء الزبناء.")}, False),
    ("web", "star", *P("à partir de 800 Dhs", "from 800 Dhs", "ابتداءً من 800 درهم"),
     {"fr": ("Logo & identité visuelle", "Logo, couleurs et polices de votre marque, déclinés pour le web, les réseaux sociaux et l’impression."),
      "en": ("Logo & visual identity", "Logo, brand colours and fonts, adapted for web, social media and print."),
      "ar": ("الشعار والهوية البصرية", "شعار وألوان وخطوط علامتك، مكيَّفة للإنترنت وشبكات التواصل والطباعة.")}, False),
    ("web", "megaphone", *P("à partir de 1 500 Dhs / mois", "from 1,500 Dhs / month", "ابتداءً من 1500 درهم / شهرياً"),
     {"fr": ("Gestion des réseaux sociaux", "Calendrier de publications, visuels et textes, stories et réponses aux messages, rapport mensuel."),
      "en": ("Social media management", "Posting calendar, visuals and captions, stories and message replies, monthly report."),
      "ar": ("تسيير شبكات التواصل", "برنامج النشر، التصاميم والنصوص، القصص والرد على الرسائل، تقرير شهري.")}, False),
    ("web", "chart", *P("à partir de 600 Dhs + budget pub", "from 600 Dhs + ad budget", "ابتداءً من 600 درهم + ميزانية الإعلان"),
     {"fr": ("Publicité Facebook, Instagram & Google", "Campagnes sponsorisées ciblées sur votre ville et votre clientèle, suivi des résultats."),
      "en": ("Facebook, Instagram & Google ads", "Sponsored campaigns targeted at your city and customers, with results tracking."),
      "ar": ("إعلانات فيسبوك وإنستغرام وGoogle", "حملات ممولة تستهدف مدينتك وزبناءك، مع تتبع النتائج.")}, False),
    ("web", "search", *P("à partir de 1 000 Dhs / mois", "from 1,000 Dhs / month", "ابتداءً من 1000 درهم / شهرياً"),
     {"fr": ("Référencement Google (SEO)", "Optimisation de votre site pour apparaître dans les premiers résultats de Google."),
      "en": ("Google ranking (SEO)", "Optimising your website to appear among the first Google results."),
      "ar": ("تحسين الظهور في Google (SEO)", "تحسين موقعك ليظهر في النتائج الأولى على Google.")}, False),
]

# Packs : (id, icône, prix fr/en/ar, mis en avant, {lang: (nom, accroche, [inclus])})
PACKS = [
    ("pack-visibilite", "megaphone", P("4 500 Dhs", "4,500 Dhs", "4500 درهم"), False,
     {"fr": ("Pack Visibilité Web", "Pour être trouvé facilement par vos clients sur internet.",
             ["Site web vitrine (jusqu’à 5 pages)", "Page Facebook + compte Instagram pro", "Fiche Google Maps (Google Business)", "Logo simple & visuels de couverture", "Bouton WhatsApp sur toutes les pages"]),
      "en": ("Web Visibility Pack", "So your customers find you easily online.",
             ["Business website (up to 5 pages)", "Facebook page + Instagram business account", "Google Maps listing (Google Business)", "Simple logo & cover visuals", "WhatsApp button on every page"]),
      "ar": ("باقة الظهور على الإنترنت", "ليجدك زبناؤك بسهولة على الإنترنت.",
             ["موقع تعريفي (حتى 5 صفحات)", "صفحة فيسبوك + حساب إنستغرام احترافي", "بطاقة خرائط Google", "شعار بسيط وتصاميم الغلاف", "زر واتساب في جميع الصفحات"])}),
    ("pack-ecommerce", "rocket", P("8 500 Dhs", "8,500 Dhs", "8500 درهم"), True,
     {"fr": ("Pack Lancement E-commerce", "Tout pour commencer à vendre en ligne dès le premier mois.",
             ["Boutique en ligne (jusqu’à 50 produits)", "Panier + commande WhatsApp, paiement à la livraison", "Photos et fiches produits mises en page", "Facebook, Instagram & chaîne YouTube créés", "Première campagne publicitaire (budget pub en plus)", "Formation pour gérer vos produits et commandes"]),
      "en": ("E-commerce Launch Pack", "Everything you need to start selling online in the first month.",
             ["Online shop (up to 50 products)", "Cart + WhatsApp ordering, cash on delivery", "Product photos and pages laid out", "Facebook, Instagram & YouTube channel created", "First ad campaign (ad budget extra)", "Training to manage your products and orders"]),
      "ar": ("باقة إطلاق التجارة الإلكترونية", "كل ما تحتاجه لتبدأ البيع عبر الإنترنت من الشهر الأول.",
             ["متجر إلكتروني (حتى 50 منتجاً)", "سلة + طلب عبر واتساب، الدفع عند الاستلام", "تنسيق صور وصفحات المنتجات", "إنشاء فيسبوك وإنستغرام وقناة يوتيوب", "أول حملة إعلانية (ميزانية الإعلان إضافية)", "تكوين لتسيير المنتجات والطلبات"])}),
]

PACK_UI = {
    "fr": dict(packs_t="Nos packs digitaux", packs_s="Des offres clés en main pour lancer votre activité sur internet.", incl="Inclus", from_="à partir de", ask="Demander ce pack", best="Le plus complet", custom="Besoin d’une offre sur mesure ? Écrivez-nous sur WhatsApp, devis gratuit."),
    "en": dict(packs_t="Our digital packs", packs_s="Turnkey offers to launch your business online.", incl="Included", from_="from", ask="Request this pack", best="Most complete", custom="Need a custom offer? Message us on WhatsApp for a free quote."),
    "ar": dict(packs_t="باقاتنا الرقمية", packs_s="عروض جاهزة لإطلاق نشاطك على الإنترنت.", incl="تشمل", from_="ابتداءً من", ask="اطلب هذه الباقة", best="الأكثر شمولاً", custom="تحتاج عرضاً خاصاً؟ راسلنا عبر واتساب، عرض الأسعار مجاني."),
}
