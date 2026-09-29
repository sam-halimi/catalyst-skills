# Références canoniques — audits design réels

Audits réalisés le 2026-07-27 : captures desktop 1440px sur toute la hauteur de page + extraction des tokens calculés (`getComputedStyle`). **Une référence canonique par mode (sections 1 à 4).** Depuis le 2026-09-29, trois **références de variante** (sections 5 à 7) précisent un mode pour un cas de figure donné : elles ne créent pas de nouveau mode et ne remplacent jamais le canon. Relire l'audit du mode concerné avant de composer, puis celui de la variante si elle s'applique. Ces audits servent à comprendre *pourquoi* ces sites ont l'air chers — jamais à les cloner : on transpose les mécanismes, pas les tokens.

---

## 1. casperscaviar.com — canon du mode Produit (luxe centré objet)

**Tokens mesurés**
- Fond : ivoire froid `#F2F2F2` alterné avec du noir presque pur `#202020`. Le site respire en clair, dramatise en sombre.
- Encre : noir `#000`–`#202020` sur clair, blanc sur sombre. Neutre chaud `#B1ADA7` pour le secondaire.
- Aucun accent coloré : **les seules couleurs vives sont les étiquettes des boîtes** (vert, bleu). Le produit est l'accent.
- Typo : sans condensé (interstate-condensed) pour les displays, script calligraphique réservé au logotype, Lexend Giga en micro-étiquettes. Displays 71–95px, corps 11.9px → **ratio 8:1**, bien au-delà du minimum 6:1.
- Micro-labels en très petites capitales espacées (« WHITE STURGEON — STARTS AT $135 ») : le prix est typographié comme un cartel de musée, pas comme un tag e-commerce.

**Composition observée**
- Hero : photo macro du caviar plein cadre sur fond noir, logotype centré par-dessus, nav réduite à 5 mots dans les coins. Zéro CTA visuel lourd — l'objet EST le hero.
- Alternance de blocs sombres (émotion, matière) et clairs (offre, information). Le rythme sombre/clair structure la page mieux que n'importe quel séparateur.
- Les produits ne sont jamais en grille e-commerce : **triptyque éditorial** packshot / carte typographique avec prix / photo culinaire stylisée. Trois colonnes, trois natures d'image différentes.
- Rupture narrative en pleine page : « NOT JUST CAVIAR, A MODERN RITUAL. » en condensé géant sur photo d'ambiance laiton/champagne. Une seule idée, formulée une seule fois, énorme.
- Éléments de marque annexes (tampon rosette, malle métallique) photographiés comme des objets de luxe à part entière.

**À transposer** : l'alternance sombre/clair comme rythme ; le produit macro plein cadre en ouverture ; le triptyque éditorial à la place de la grille ; le prix traité en cartel ; le ratio typographique extrême ; la rupture narrative géante aux deux tiers de la page.
**Piège si on copie mal** : sans photos produit d'un niveau irréprochable, ce système s'effondre — il ne tient que par l'image.

---

## 2. ballenacabo.com — canon du mode Expérience (faire rêver, couleurs & images)

**Tokens mesurés**
- Fond : crème chaud `#F8F2E5`. Encre : noir bleuté `#03090D` (jamais de noir pur).
- Blocs de couleur pleins prélevés du lieu : terracotta, vert sauge, marine profond. La palette N'EST PAS décorative — chaque couleur vient d'une matière du restaurant (terre, végétation, mer, nuit).
- Typo : Sweet Sans Pro (display) + TT Commons Pro (corps). Display 68px en capitales avec **espacement positif** (+1.7px) et interligne serré (0.9) — le code typographique « resort de luxe ». Micro-labels 11.7px en capitales espacées.

**Composition observée**
- Hero : photo pleine page (table, bois chaud), promesse en capitales espacées crème posée dessus (« SHAPED BY SEA. GROUNDED IN LAND »), bandeau de nav teinté (marine) avec logotype centré et **BOOK NOW persistant** en haut à gauche.
- Signature du site : **le collage bloc-couleur / photo**. Un aplat terracotta porte trois phrases et un lien ; une photo de plat le chevauche ; en dessous, paysage plein cadre. Photo et couleur se répondent, jamais côte à côte sagement.
- La couleur du bandeau de nav change selon la section traversée (marine → sauge) : la palette accompagne le scroll comme une lumière qui tourne.
- Cartes d'exploration (Events / Gallery / Gift Cards) : images hautes, labels capitales, lien « EXPLORE MORE » discret — fonctionnel mais habillé.
- Footer : logotype géant coupé par le bord bas de la page. Geste de confiance typographique repris partout dans les sites chers.

**À transposer** : la palette dérivée du lieu avec blocs pleins assumés ; le chevauchement photo/aplat ; les capitales espacées à interligne serré ; le CTA de réservation persistant mais discret ; le logotype géant tronqué en pied de page ; la nav qui change de teinte par section.
**Piège si on copie mal** : les capitales espacées ne fonctionnent que sur des phrases courtes ; au-delà de 6–7 mots, ça devient illisible et cheap.

---

## 3. aerodynamics.nl — canon du mode Fonctionnel (résa/hôtels/agences, la DA au service de l'action)

**Tokens mesurés**
- Fond : blanc cassé `#FCFDFE`. Encre : marine profond `#05275B` / `#0B2348` — l'identité entière tient dans ce bleu nuit.
- **Accent bleu vif (`#008AFF` / `#2563EB`) réservé exclusivement aux actions** : bouton recherche, CTA « Bereken prijs ». Nulle part ailleurs. C'est l'application la plus stricte de la règle des 5 %.
- Typo : serif display (romain + **italique mélangés dans la même phrase** : « Smooth journeys / *Private skies* ») 88px, tracking négatif −1.76px. Corps sans-serif 14–16px, hiérarchie H2 40–72px très réglée. Ratio ≈ 6:1.

**Composition observée**
- **Le module de réservation est DANS le hero** : carte blanche arrondie avec champs (départ, date, passagers), toggle aller/retour, bouton de recherche bleu — posée sur une photo de ciel pleine page. L'action principale est disponible à la seconde zéro, sans sacrifier l'image.
- Fonctionnel ≠ austère : photos immersives pleine page entre les blocs utiles (cabine du jet à la lumière chaude, tarmac au couchant, hublot).
- Interlude purement typographique au milieu de la page : « the sky is yours » en serif marine géant sur ciel. La page la plus fonctionnelle des quatre s'offre le moment le plus poétique.
- Page très longue (16 500px) mais jamais confuse : blocs de service, preuves, actualités en cartes blanches arrondies, flux Instagram — chaque bloc a une fonction identifiable en une seconde.
- Boutons en pilule, champs grands et étiquetés, calculateur de prix accessible en permanence dans la nav.

**À transposer** : le widget de résa/RDV intégré au hero sur image pleine page ; l'accent strictement réservé aux actions ; le mélange romain/italique dans le display ; l'interlude typographique qui aère un long parcours fonctionnel ; les cartes de contenu (actus, preuves) pour montrer que l'entreprise est vivante.
**Piège si on copie mal** : le widget hero doit rester simple (3–4 champs max) ; au-delà, il faut un parcours par étapes.

---

## 4. supadupa.nl — canon du mode Vision (startups, témoignage, modernité)

**Tokens mesurés**
- **Une seule famille : Bricolage Grotesque**, poussée à l'extrême : wordmark 273px graisse 800 tracking −8px → corps 14–18px graisse 400. Le contraste d'échelle (jusqu'à 15:1) remplace la seconde famille.
- Palette-identité : lime `#D3F773`, vert forêt `#163300` (l'encre), orange `#FF9923`, violet `#260A2F`. Ici **le fond EST la couleur de marque** — exception assumée à la règle des 5 % : en mode Vision « brand-loud », l'accent devient le fond et l'encre en dérive (vert forêt = lime assombri). Cette exception ne vaut que pour ce mode.
- Formes de marque récurrentes : étoiles/soleils (starburst), pilules, très grands rayons d'arrondi.

**Composition observée**
- Hero : wordmark géant pleine largeur sur fond vert sombre texturé, eyebrow minuscule au-dessus, **photo d'équipe réelle** en carte flottante en bas — les visages arrivent dès le premier écran.
- Manifeste en très gros, **révélé mot à mot au scroll** (le texte se colore au fur et à mesure) : le seul effet spectaculaire du site, réservé au message central.
- Grille bento de cartes photo à grands arrondis : vraies photos d'atelier/bureau + une carte pleine couleur portant une phrase clé (« There's no change / Without movement. »). Jamais deux cartes identiques côte à côte.
- **Témoignage roi** : carrousel dans un bloc orange plein, cité, nommé, avec fonction et entreprise, et photo du contexte. Exactement l'anti-témoignage-anonyme.
- Fin de page : « Get in touch » en ~200px+, starbursts, pilule CTA. La sortie est aussi dessinée que l'entrée.

**À transposer** : la famille unique poussée aux extrêmes d'échelle et de graisse ; le fond couleur de marque avec encre dérivée ; les vraies photos d'équipe en premier écran ; le manifeste scroll-reveal réservé au message central ; le témoignage nommé mis en scène dans un bloc couleur ; les formes de marque récurrentes comme signature.
**Piège si on copie mal** : ce système exige une vraie personnalité de marque (couleur, formes, ton). Appliqué timidement, il donne juste un site flashy sans identité.

---

## Références de variante (ajoutées le 2026-09-29, demande explicite de Sam)

Audits du 2026-09-29 : captures desktop 1440px et mobile 390px, tokens calculés, couleurs relevées au pixel sur les captures. Captures conservées hors dépôt.

Les trois sites sont des boutiques ou des sites produit à fort trafic : ils assument un CTA dès le premier écran. C'est une entorse au fil rouge n° 6, admise uniquement dans ces variantes (voir SKILL.md, « Variantes de mode »).

---

## 5. skims.com — variante « Commerce éditorial » du mode Produit (boutique à catalogue large)

**Tokens mesurés**
- Fond blanc, encre brun-noir chaud `#2D2A26` (boutons pleins compris). Neutres chauds : taupe `#B49A87`, brun `#62554A`, gris `#F6F6F6` pour le champ de recherche. Aucun accent vif : **la couleur vient des campagnes photo** (herbe, bois, peau, coton).
- Typo : T-Star (grotesque condensée, graisse 900, capitales, espacement +0,025em) pour les titres, Inter pour tout le reste. H1 48px, H2 24 à 36px, corps 12 à 16px. **Ratio 3:1 à 4:1 seulement** : ici l'échelle est portée par l'image plein cadre, pas par la typographie. C'est le seul site du corpus sous le seuil de 6:1, et c'est ce qui le rend « boutique » plutôt que « maison ».
- Logotype dessiné (lettres molles, organiques) en contraste total avec la rigueur du reste : le seul élément expressif de l'interface.

**Composition observée**
- Hero : photo de campagne pleine largeur, cadrage de magazine (modèle allongée, regard caméra). Le texte tient dans le coin bas gauche : titre condensé en capitales, deux lignes de corps, et **un lien souligné « Shop Now » à la place d'un bouton**. La nav blanche se pose en transparence sur l'image puis devient opaque au scroll.
- Sous le hero, rangée de 4 tuiles catégories en portrait, séparées par une gouttière blanche de 24px, libellé en capitales condensées sous l'image. Sur mobile : 2 colonnes, même gouttière.
- Alternance stricte : bannière de campagne pleine largeur (« JUST DROPPED: CLOUD SLEEP ») puis rangée de tuiles, puis bannière. Chaque bannière est une collection, avec son propre décor et sa propre lumière, mais le même traitement de texte.
- Barre d'annonce en haut avec messages rotatifs et **bouton pause** (accessibilité). Recherche persistante : champ en pilule dans la nav desktop, pleine largeur sous le logo en mobile.
- Popup d'inscription : modale 2 colonnes (photo de campagne à gauche, formulaire à droite), titre « NEVER MISS A DROP », **une question de préférence avant l'email** (Womens / Mens / Both), bouton de refus « NO THANKS » au même poids visuel que le bouton d'inscription. Aucune remise promise : l'offre est l'accès aux lancements.

**À transposer** : la campagne photo comme unité de page (une collection = un décor = une bannière) ; le lien souligné à la place du bouton dans le hero ; les tuiles portrait à gouttière blanche ; la palette de neutres chauds qui laisse la couleur aux images ; le vocabulaire du « drop » (lancement daté) comme moteur d'inscription ; le refus à égalité visuelle dans le popup.
**Piège si on copie mal** : sans direction photo cohérente (même grain, mêmes peaux, même lumière chaude d'une campagne à l'autre), il ne reste qu'un thème Shopify blanc. Et ce système suppose du volume : en dessous d'une quinzaine de produits, rester sur le canon Caspers.

---

## 6. drinkupdate.com — variante « Produit-héros » du mode Produit (marque à produit unique, vente en ligne)

**Tokens mesurés**
- Encre ardoise `#2C3138` (texte, barre d'annonce, bandeau défilant, onglet actif), fond blanc, cartes produit gris bleuté `#D8DDE1`. Le hero est un dégradé studio du gris anthracite `#4E4C4F` au gris clair `#C1C2BF`.
- **Aucune couleur d'interface.** Les seules couleurs sont celles des canettes (une teinte métallisée par parfum) et des fruits. Même logique que Caspers, appliquée à un produit de grande consommation.
- Typo : ABC Diatype (titres en graisse 800, 48 à 64px, bas de casse) + sa déclinaison semi-mono pour les boutons, onglets et le bandeau défilant. Corps 14px. Ratio ≈ 4,5:1. La mono apporte le registre « laboratoire » qui crédibilise l'argument scientifique.
- Boutons : rectangle à angles vifs (rayon 0), filet 1px, fond transparent, libellé en capitales semi-mono. Aucun bouton plein en dehors de l'onglet actif.

**Composition observée**
- Hero : packshot vidéo sur fond studio (canette froissée, fruits, verre givré), titre en bas de casse à gauche, trois lignes de corps, bouton filet « SHOP NOW ». Logotype centré dans la nav, liens à gauche, compte et panier à droite.
- Bandeau défilant ardoise sous le hero : les preuves produit en mono (« Zero Sugar », « Paraxanthine Powered »), séparées par des points.
- Carrousel de parfums : cartes gris bleuté, nom du parfum, avis, conditionnement, et **la canette coupée par le bas de la carte**. Onglets « FLAVORS / VARIETY PACK » en segment à angles vifs, barre de progression fine sous le carrousel.
- Bloc argumentaire : accordéon à filets et signes « + » face à un rendu 3D de canette prise dans un métal liquide chromé.
- La fondatrice mise en scène comme une image de campagne (pupitre, micros, canette posée) et non en portrait « à propos ».

**À transposer** : le studio monochrome qui fait du produit la seule couleur ; la paire grotesque + mono pour un produit à argument technique ; le bouton filet à angles vifs ; le packshot recadré par la carte ; la preuve en bandeau défilant ; le fondateur en situation.
**Piège si on copie mal** : le système repose sur des packshots et rendus 3D de niveau publicitaire. Avec des photos produit moyennes sur fond gris, le résultat est terne et non premium.

**Popup carte à gratter** : audit complet et spécification de transposition dans le skill `popup-conversion`, référence `scratch-card.md`.

---

## 7. mistral.ai — variante « Tech institutionnelle » du mode Vision (éditeurs de logiciel, IA, B2B technique)

**Tokens mesurés**
- Fond papier chaud `#FBFBF8`, panneaux `#F5F4EF`, filets `#E4E3DE`, encre `#18181B`. Le site entier est tiède : aucun gris froid, aucun blanc pur.
- Palette de marque en dégradé de chaleur, toujours en aplats : jaune orangé `#FF8204`, orange `#FA500F` / `#F58718`, rouge `#E51300` / `#DC2313`, carmin `#C4001D` / `#BC1029`. Un bleu `#0094EB` apparaît une seule fois, pour distinguer une famille de produits.
- Typo : grotesque maison pour les titres (graisse 500, **96px, interligne 1, espacement −0,02em**), Inter pour le corps (16 à 20px), Space Mono en capitales de 11 à 13px pour les étiquettes. Ratio 6:1. La graisse moyenne, jamais grasse, donne le ton institutionnel.
- Pictogrammes et logo en pixels : le M, les flèches des boutons, un chat en pied de page.

**Composition observée**
- **La grille est visible.** Des filets de 1px délimitent la nav (chaque lien est une cellule), les colonnes du hero, les cases des logos clients, les colonnes du pied de page. La structure est le décor.
- Hero en deux colonnes séparées par un filet : à gauche le titre (« Frontier AI. In your hands. ») ancré en bas de sa cellule, à droite la phrase de positionnement puis un bloc d'actualité. En dessous, une mosaïque de carrés en aplats orange, rouge et carmin.
- Le CTA « Get in touch » est une cellule noire pleine dans l'angle de la nav, avec flèche en pixels. En mobile il passe au centre de la barre haute.
- Preuve par les institutions : logos clients en grandes cellules (assureur, opérateur, ministère), puis études de cas en cartes photo dont **l'image est étalonnée dans la palette de marque** (statue éclairée en orange).
- Sections produit : titre à gauche, bouton gris à droite, visuel d'interface posé sur un fond de pixels, puis rangée d'étiquettes mono en capitales.
- Pied de page : colonnes de liens séparées par des filets, grand M en pixels, bandes horizontales du jaune au carmin. Sélecteur de thème clair / sombre / système.

**À transposer** : la grille apparente en filets fins ; le fond papier chaud pour un sujet froid ; la palette de marque en aplats géométriques plutôt qu'en dégradé lisse ; la mono en étiquettes ; un motif graphique propre (ici le pixel) décliné du logo aux pictogrammes ; les logos d'institutions en cellules ; les photos de cas étalonnées dans la palette.
**Piège si on copie mal** : le motif de marque doit venir du client. Reprendre le pixel ou le dégradé orange revient à cloner Mistral. Et la grille apparente exige un alignement parfait : un seul filet décalé se voit immédiatement.

---

## Synthèse des variantes

1. **Dans les trois, l'interface est neutre et la couleur appartient à autre chose** : la campagne photo (SKIMS), le produit (Update), le motif de marque (Mistral).
2. **Le ratio typographique descend sous 6:1 dès que l'image porte l'échelle** (SKIMS 3 à 4:1, Update 4,5:1). Ce n'est admis qu'avec une image plein cadre de niveau campagne ; sans elle, revenir au seuil du skill.
3. **Une mono en second rôle** (Update, Mistral) signale la précision technique sans alourdir.
4. **Les angles vifs et les filets de 1px** remplacent les ombres et les arrondis : c'est la signature commune 2026 des marques observées.

---

## Synthèse transversale — ce que les 4 canons ont en commun

1. **Un seul système typographique par site**, poussé loin : condensé géant (Caspers), capitales espacées (Ballena), serif romain/italique (Aerodynamics), grotesque à graisse extrême (Supadupa). Aucun n'empile les styles.
2. **Ratio display/corps toujours ≥ 6:1**, souvent 8–15:1.
3. **La couleur vive a un rôle unique et exclusif** : produit (Caspers), lieu (Ballena), action (Aerodynamics), marque (Supadupa). Jamais deux rôles à la fois.
4. **Au moins un moment purement typographique géant** par page, porteur du message central.
5. **Des photos réelles au cœur** : produit, lieu, équipe. Aucun des quatre ne tient sur du stock ou du généré.
6. **Un pied de page dessiné** — logotype géant, appel final énorme : la sortie fait partie de la composition.
