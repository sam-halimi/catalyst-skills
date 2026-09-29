---
name: plinko-popup
description: "Implémenter ou corriger le popup de capture avec boule qui tombe (jeu Plinko) d'une boutique e-commerce : physique, lots signés serveur, reprise, consentement, stockage réel et récompenses Shopify. Utiliser si Sam demande le jeu Plinko ou ce composant précis ; ne pas imposer ce jeu à tout popup."
---
# Popup boule qui tombe

Lire [le fonctionnement](references/implementation.md), puis [le contrat de stockage et récompenses](references/capture.md). Réutiliser la logique validée sans recopier la marque, les offres ni la configuration d'un client dans un autre.

Source de référence : dossiers `components/plinko/` et `lib/plinko/`, routes `app/api/plinko/` du projet de la boutique horlogère (non publié). Lire les fichiers présents avant de patcher : les commentaires historiques décrivent parfois d'anciens comportements. Les instructions générales de choix de popup sont dans le skill `popup-conversion`, la mise en vente dans `shopify-ecommerce-build`.

L'utilisateur peut autoriser directement une correction ou une intégration ; ne pas lui redemander de valider une spécification déjà tranchée. Pas d'envoi d'email/campagne au nom du client sans demande correspondante.
