# Sources du site Data Librairie digitale

Cette branche contient les fichiers qui **fabriquent** le site. Le site publié (branche `main`) est généré à partir d'eux.

## Régénérer le site
```bash
pip install pillow opencv-python-headless numpy
python3 gen.py ../site        # génère le site complet (FR/EN/AR) dans ../site
```
Puis copier le contenu de `../site` sur la branche `main` (en gardant `README.md`).

## Où modifier quoi
| Fichier | Contenu |
|---|---|
| `real_catalog.py` | **Produits réels** : noms FR/EN/AR, prix, références, sous-rayons, groupes de couleurs |
| `real/photos/` | Photos des produits réels (600×600, fond blanc) |
| `real/shots/` | Captures d'origine du logiciel de caisse |
| `catalog.py` | Organisation des rayons, produits d'exemple restants |
| `variants.py` | Produits déclinés en couleurs |
| `site_i18n.py`, `nova_i18n.py`, `pay_i18n.py` | Textes du site en 3 langues, services |
| `web_services.py` | Services marketing digital & packs |
| `gen.py` | Générateur (pages, coordonnées Google Maps : `SHOP_LL`, `PLACE_URL`) |
| `config.js` | WhatsApp, téléphone, adresse, paiements |
| `assets/` | CSS, JavaScript, logos, polices |
| `videos/` | Vidéos d'itinéraire |
