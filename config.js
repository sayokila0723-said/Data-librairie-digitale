/* ===== RÉGLAGES DE VOTRE BOUTIQUE / SHOP SETTINGS / إعدادات المتجر =====
   Modifiez les valeurs entre guillemets puis redéployez le dossier sur Netlify. */
window.BOUTIQUE = {
  whatsapp: "212760923785",        // numéro WhatsApp, format international, sans + ni espaces
  telephone: "+212 760-923785",    // numéro affiché
  email: "",                       // ex. "contact@librairie-digitale.ma" — vide = masqué
  adresse: "514 Charaf, Mag 2, Marrakech",

  /* ----- MODES DE PAIEMENT (page « Bon de commande ») ----- */
  paiement: {
    livraison: true,               // paiement à la livraison (espèces)
    magasin: true,                 // paiement en magasin (si retrait en magasin)
    virement: {                    // virement bancaire — laissez rib vide pour envoyer le RIB par WhatsApp
      actif: true,
      titulaire: "",               // ex. "LIBRAIRIE DIGITALE SARL"
      banque: "",                  // ex. "CIH Bank"
      rib: ""                      // ex. "230 450 0000000000000000 00" (24 chiffres)
    },
    carte: {                       // carte bancaire via CMI (contrat à signer avec votre banque)
      actif: false,                // passez à true quand votre banque vous a donné un lien de paiement CMI
      lien: ""                     // lien de paiement CMI / « Pay by link » fourni par la banque
    }
  }
};
