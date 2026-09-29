---
name: da-moderne
description: Direction artistique Catalyst pour composer des sites premium sur-mesure en session interactive. Utilise ce skill dès qu'il s'agit de concevoir, maquetter, restyler ou critiquer un site client — page d'accueil, landing, refonte, choix de palette, de typographie, de mise en page ou d'animation — même si la demande ne mentionne ni "design" ni "DA". Contient 4 modes (Produit, Expérience, Fonctionnel, Vision) et un protocole de composition interactive à respecter obligatoirement.
---

# DA Moderne — système de direction artistique Catalyst

Ce skill ne produit pas un style. Il produit une **méthode pour dériver un style propre à chaque client**, plus les contraintes qui garantissent que le résultat ait l'air cher.

## Règle zéro : ce skill ne s'exécute pas en one-shot

La composition sur-mesure se fait **en session interactive** : Sam est devant l'écran, l'agent exécute, Sam tranche. Ne jamais générer un site complet d'un seul jet.

Boucle obligatoire :

1. **Cadrage** — poser les questions de la section « Brief minimal » avant d'écrire une ligne de code.
2. **Tokens** — proposer 2 à 3 directions de palette + typo. **S'arrêter. Attendre l'arbitrage.**
3. **Squelette** — hiérarchie des sections en texte brut, sans style. **S'arrêter. Attendre l'arbitrage.**
4. **Hero seul** — composer uniquement le premier écran, en entier, au niveau final. **S'arrêter.** Le hero valide le reste du site ; tant qu'il n'est pas jugé bon, on ne descend pas.
5. **Section par section** — une section, une validation.
6. **Passe de mouvement** — l'animation vient en dernier, jamais pendant la composition.

Les missions autonomes (sans validation intermédiaire) sont réservées à la performance, au SEO et au CRM. Pas à la DA.

---

## Le fil rouge (non négociable, tous modes confondus)

1. **Aucun composant à son style par défaut.** Si un bouton, une carte, un champ ou une ombre ressemble à ce que sort la librairie sans modification, il est faux. Chaque composant est redessiné dans les tokens du client.
2. **Mouvement maîtrisé.** Le mouvement souligne une intention, il ne décore jamais. Peu d'animations, mais chacune est lente, précise et justifiable en une phrase.
3. **Sur-mesure total.** Palette, typographie et images sont dérivées de la matière du client — sa boutique, ses produits, ses couleurs réelles, son quartier. Jamais un thème appliqué.
4. **La respiration est le premier signe de prix.** Un site cher est un site vide. Dans le doute, retirer un élément et doubler l'espace.
5. **Une seule idée forte par page.** Si le visiteur doit retenir deux choses, il n'en retient aucune.
6. **Le premier écran ne vend pas.** Sur un site de luxe, le hero se limite au nom et à une image de matière ou d'objet — zéro argumentaire, zéro CTA, zéro lien superflu. Pousser produit + texte + bouton dès l'ouverture est le code du discount (les places de marché à bas prix). L'action (rendez-vous, réservation) arrive plus bas, avec un vrai CTA mis en scène. Exception : le mode Fonctionnel, où l'action DANS le hero est précisément le luxe (cf. aerodynamics.nl).

---

## Brief minimal (à obtenir avant toute production)

- Le métier, et **l'objet de confiance** du secteur : la chose que le client doit voir pour croire (la pièce pour un joaillier, l'assiette pour un restaurant, le chantier fini pour un artisan, le visage pour un cabinet).
- Ce que le visiteur doit faire à la fin : appeler, réserver, venir, demander un devis.
- La matière disponible : photos produit réelles, photos du lieu, logo, couleurs existantes.
- Trois adjectifs que le client emploierait pour se décrire.
- Ce qu'il ne veut surtout pas ressembler (souvent plus informatif que le reste).

Si l'objet de confiance n'est pas identifié, **ne pas commencer**.

---

## Choix du mode

| Mode | Quand | Référence canonique |
|---|---|---|
| **Produit** | Luxe centré sur l'objet. L'objet vaut cher et se regarde : joaillerie, épicerie fine, mobilier, maroquinerie. | casperscaviar.com |
| **Expérience** | Faire rêver. Le client vend une projection, un ailleurs, une sensation — la DA couleurs + images porte tout : hôtellerie, voyage, restaurant, bien-être. | ballenacabo.com |
| **Fonctionnel** | Agences avec réservations, hôtels, tout site dont le cœur est la résa ou la prise de rendez-vous. Hyper fonctionnel, avec une DA solide mais au service de l'action. | aerodynamics.nl |
| **Vision** | Startups et entreprises où le témoignage, la modernité et la technologie sont au centre. | supadupa.nl |

**Ces 4 références sont les seuls canons. Avant de composer dans un mode, relire son audit détaillé dans `references.md`** (tokens mesurés, composition observée, ce qu'il faut transposer, le piège si on copie mal). On transpose les mécanismes de la référence, jamais ses tokens.

Trois **variantes** précisent un mode pour un cas de figure donné (détail dans « Variantes de mode » plus bas) :

| Variante | Mode parent | Quand | Référence |
|---|---|---|---|
| **Commerce éditorial** | Produit | Boutique en ligne à catalogue large, mode, beauté, lifestyle. | skims.com |
| **Produit-héros** | Produit | Marque à produit unique ou gamme courte vendue en ligne. | drinkupdate.com |
| **Tech institutionnelle** | Vision | Éditeur de logiciel, IA, B2B technique qui vend à des grands comptes. | mistral.ai |

Une variante se propose à Sam au checkpoint tokens, comme une direction parmi les 2 ou 3, jamais d'office.

Les modes se mélangent rarement bien. Un site a un mode dominant ; un deuxième mode peut colorer une section unique, pas plus.

---

## Système partagé

### Dérivation de la palette

Toujours dériver, jamais choisir dans le vide.

- **1 fond dominant** — clair chaud ou sombre profond. Jamais `#FFFFFF` ni `#000000` purs.
- **1 encre** — la couleur du texte, jamais du noir pur ; teintée du fond.
- **1 accent, un seul**, prélevé dans la matière réelle du client (une pierre, un packaging, l'enseigne, la lumière du lieu).
- **3 neutres** dérivés du fond par variation de luminosité, pas des gris génériques.

Règle d'usage : **l'accent occupe moins de 5 % de la surface.** S'il en occupe plus, le site devient bon marché.

Chaque référence canonique donne à la couleur vive **un rôle unique et exclusif** : le produit (Caspers), le lieu (Ballena), l'action (Aerodynamics), la marque (Supadupa). Choisir ce rôle avant de choisir la couleur. Exception documentée : en mode Vision « brand-loud » (cf. supadupa.nl dans `references.md`), le fond peut être la couleur de marque elle-même, l'encre en étant dérivée — c'est la seule entorse admise aux 5 %.

### Typographie

- **Deux familles maximum.** Une de caractère pour les titres, une neutre et très lisible pour le texte.
- **Contraste d'échelle obligatoire.** Le rapport entre le plus grand titre et le corps de texte doit être d'au moins 6:1. Un site où tout fait 16 à 32px a l'air gratuit.
- Display en `clamp()` : viser 56–120px sur desktop pour un hero.
- Corps de texte : 17–19px, interlignage 1.6–1.75, largeur de ligne 60–72 caractères.
- Les titres se resserrent (`letter-spacing` négatif léger, `line-height` 0.95–1.1). Le corps de texte, jamais.
- Interdit : plus de deux graisses par famille, du texte centré sur plus de deux lignes, des majuscules sur un paragraphe.

### Espacement et grille

- Échelle d'espacement unique, géométrique (par exemple 4 / 8 / 16 / 32 / 64 / 128 / 200). Aucune valeur hors échelle.
- Padding vertical de section : **120–200px sur desktop**. C'est le premier réglage à monter quand un site a l'air cheap.
- Grille de 12 colonnes, mais **au moins un moment par page où la grille se casse** : une image en pleine largeur, un bloc décalé, un chevauchement. Un site parfaitement aligné du haut en bas a l'air d'un template.

### Mouvement

- Budget : **une animation d'entrée par section, maximum.**
- Durées : 500–900ms. En dessous de 400ms ça a l'air d'un plugin ; au-dessus de 1200ms ça agace.
- Courbes personnalisées uniquement (`cubic-bezier`), jamais `ease`, `linear` ou `ease-in-out` par défaut.
- Décalage en cascade entre éléments d'un même bloc : 60–120ms.
- Le mouvement le plus rentable est le plus discret : une image qui se révèle par un masque, un titre qui monte de 20px, un léger parallaxe (jamais plus de 15 % de décalage).
- `prefers-reduced-motion` respecté systématiquement.

### Images

- Cohérence d'étalonnage sur tout le site : une même dominante, un même contraste. Deux photos qui ne se ressemblent pas cassent l'illusion de prix plus vite que n'importe quel défaut de mise en page.
- Recadrages francs et assumés, formats variés (portrait haut, panoramique large), jamais que du 16:9.
- **L'objet de confiance doit être réel.** L'ambiance, les textures, les fonds peuvent être générés ou retouchés ; le produit et le lieu du client, non.

---

## Mode 1 — Produit

**Intention** : faire désirer un objet. Le site est un écrin, pas un catalogue.

- **Signature de mise en page** : très peu d'éléments par écran. L'objet est grand, centré ou fortement décalé, entouré de vide. Une seule ligne de texte à côté.
- **Typographie** : titres sobres, presque muets. Le produit parle, pas le texte. Les descriptions sont courtes et factuelles — matière, origine, geste.
- **Images** : détail macro, matière, lumière rasante. Alterner plan très large et plan très serré, jamais de plan moyen.
- **Mouvement** : révélation lente des visuels, zoom léger au survol (1.02 à 1.04, pas plus).
- **Sections** : hero objet — le geste / la fabrication — les pièces — la matière — visite ou contact.
- **Échec typique** : la grille produit régulière façon e-commerce. Dès qu'on voit trois cartes alignées identiques, la valeur s'effondre.

## Mode 2 — Expérience

**Intention** : faire ressentir un lieu ou un moment. On vend une projection.

- **Signature de mise en page** : image plein écran comme fond permanent, texte posé dessus, peu nombreux. Le scroll est une traversée.
- **Typographie** : c'est le mode où un display expressif est permis. Grand, aéré, avec du caractère.
- **Palette** : la plus saturée des quatre. L'accent peut monter à 10 % de surface s'il vient d'une lumière réelle du lieu.
- **Images** : atmosphère avant tout — heure dorée, mouvement, présence humaine floue. C'est le mode le plus tolérant à la génération d'ambiance.
- **Mouvement** : parallaxe assumé, transitions de section fondues, texte qui apparaît au rythme du scroll.
- **Sections** : hero immersif — la promesse en une phrase — trois moments de l'expérience — le lieu — réserver.
- **Échec typique** : le texte illisible sur l'image. Toujours un voile ou un dégradé, contraste vérifié.

## Mode 3 — Fonctionnel

**Intention** : faire agir sans friction, tout en restant premium. Le luxe ici, c'est que ce soit facile.

- **Signature de mise en page** : structuré, lisible, dense mais aéré. L'action principale est visible en permanence.
- **Typographie** : neutre et impeccable. Hiérarchie très nette, aucune fantaisie.
- **Palette** : la plus sobre. L'accent est réservé aux actions — et à rien d'autre.
- **Images** : illustratives et fonctionnelles ; elles montrent le service en train de se faire.
- **Mouvement** : uniquement du retour d'interaction — états de survol, transitions d'étapes, confirmations. Aucune animation décorative.
- **Sections** : hero avec l'action — comment ça marche en 3 étapes — le module de réservation — preuves — questions fréquentes.
- **Échec typique** : sacrifier l'ergonomie au style. Les champs de formulaire restent grands, étiquetés, avec des erreurs claires. Un formulaire joli et pénible est un échec total.

## Mode 4 — Vision

**Intention** : installer la confiance dans une compétence. On vend une tête, une méthode, une équipe — avec la modernité et la technologie comme preuve, et le témoignage comme pièce maîtresse.

- **Signature de mise en page** : éditoriale. Colonnes de texte lisibles, citations mises en valeur, rythme de magazine.
- **Typographie** : c'est le mode où le texte porte le design. Soigner les intertitres, les exergues, les listes.
- **Images** : portraits réels, coulisses, lieu de travail. Zéro stock photo de poignée de main.
- **Mouvement** : sobre — apparitions au scroll, compteurs si les chiffres sont vrais.
- **Sections** : hero de positionnement — le problème — la méthode — preuves chiffrées — témoignages nommés — qui nous sommes — contact.
- **Échec typique** : les témoignages anonymes. Un témoignage sans nom, sans photo et sans entreprise vaut moins que pas de témoignage du tout.

---

## Variantes de mode (ajoutées le 2026-09-29)

Une variante hérite de tout son mode parent et du système partagé. Elle ne documente que ce qui change. Audits complets : `references.md`, sections 5 à 7.

**Entorse commune aux deux variantes e-commerce** : le fil rouge n° 6 (« le premier écran ne vend pas ») est levé. Un seul CTA est admis dans le hero, discret (lien souligné ou bouton filet), jamais un bouton plein saturé ni un bandeau de promotion.

### Commerce éditorial (parent : Produit, référence skims.com)

**Intention** : vendre un catalogue large sans jamais avoir l'air d'un catalogue. La page d'accueil est un magazine dont chaque double page mène à un rayon.

- **Unité de page** : la campagne. Une collection = un décor, une lumière, une bannière pleine largeur. Les rayons s'intercalent en rangées de tuiles portrait.
- **Palette** : interface en neutres chauds (blanc, encre brun-noir, taupe). Aucun accent d'interface : la couleur vient des photos.
- **Typographie** : condensée grasse en capitales pour les titres, neutre pour le reste. Le ratio peut descendre à 4:1 SI chaque bannière est une image plein cadre de niveau campagne.
- **Hero** : image plein cadre, texte en bas à gauche, lien souligné comme unique action.
- **Mobile** : tuiles en 2 colonnes, recherche pleine largeur sous le logo, bannières recadrées en portrait (un second cadrage de la même campagne, pas un recadrage automatique).
- **Capture** : inscription aux lancements, avec une question de préférence avant l'email et un refus à égalité visuelle.
- **Échec typique** : des bannières aux lumières disparates. Sans unité photographique, il ne reste qu'un thème de boutique blanc.
- **Seuil** : en dessous d'une quinzaine de produits, rester sur le mode Produit canonique.

### Produit-héros (parent : Produit, référence drinkupdate.com)

**Intention** : faire d'un produit de série un objet de désir, en le photographiant comme une pièce unique.

- **Palette** : studio monochrome. Une encre teintée, un fond clair, un gris de carte. **Le produit et ses déclinaisons sont la seule couleur du site.**
- **Typographie** : une grotesque et sa déclinaison mono. La mono porte les boutons, onglets, étiquettes et preuves : elle installe le registre technique.
- **Composants** : angles vifs, filets de 1px, fonds transparents. Aucun bouton plein hors état actif.
- **Hero** : packshot sur fond studio dégradé, titre en bas de casse, bouton filet.
- **Signatures** : bandeau défilant de preuves, produit coupé par le bas de sa carte, accordéon à filets, fondateur mis en situation avec le produit.
- **Capture** : la carte à gratter est cohérente avec cette variante. Voir `popup-conversion`, référence `scratch-card.md`.
- **Échec typique** : des packshots moyens. Ce système n'a aucune béquille décorative : si l'image produit n'est pas de niveau publicitaire, générer ou faire produire les visuels avant de composer.

### Tech institutionnelle (parent : Vision, référence mistral.ai)

**Intention** : rassurer un acheteur grand compte. La rigueur visible de la mise en page fait la preuve de la rigueur technique.

- **Signature de mise en page** : grille apparente. Des filets de 1px délimitent la nav, les colonnes, les cellules de logos, le pied de page. Aucune ombre, aucun arrondi marqué.
- **Palette** : fond papier chaud, encre presque noire, et une palette de marque posée en aplats géométriques. Pas de dégradé lisse, pas de violet, pas de « lueur » derrière les visuels.
- **Typographie** : grotesque en graisse moyenne pour les titres (interligne 1, espacement négatif), mono en petites capitales pour les étiquettes. Ratio 6:1 tenu.
- **Motif de marque** : un seul motif graphique dérivé du logo du client, décliné partout (pictogrammes, flèches, fonds, pied de page). Il se cherche dans la matière du client, comme l'accent.
- **Preuve** : logos d'institutions en grandes cellules, études de cas en cartes photo étalonnées dans la palette. Les témoignages nommés du mode Vision restent la pièce maîtresse quand ils existent.
- **Mobile** : le CTA remonte dans la barre haute, la grille passe à une colonne en gardant ses filets horizontaux.
- **Échec typique** : le site « IA » générique (fond sombre, dégradé violet, halo, particules). Si le résultat ressemble à une page de startup IA quelconque, la variante est ratée.
- **Par rapport au canon Supadupa** : même mode, tempérament opposé. Supadupa pour une marque expressive qui vend à des équipes, Mistral pour une marque sobre qui vend à des directions.

---

## Leçons de production (validées sur projet réel, 2026-07)

Règles apprises en session, au rang de loi. Elles ne décrivent PAS une composition à reproduire — chaque site garde sa propre structure — mais des erreurs à ne plus jamais refaire.

**Rédaction et typographie française**
- **Jamais de tiret cadratin** dans une chaîne visible (titres d'onglet compris) : c'est la signature de l'écriture IA. Virgules, deux-points ou parenthèses. Relire chaque chaîne du site avant livraison, le client le remarque immédiatement.
- Espaces insécables françaises : avant » ; : ! ? et après «. Un guillemet fermant ne se retrouve jamais orphelin en bout de ligne.

**Composition et effets**
- **Un seul moment spectaculaire par site.** Une animation signature (scroll-frames, ouverture, morphing) a de la valeur parce qu'elle est unique ; la dupliquer sur d'autres produits la banalise et alourdit. Les autres produits vivent très bien en présentation fixe.
- Trop de texte au premier écran fait discount même avec une belle typo ; mais une page sans AUCUNE respiration photographique entre les blocs produits fait catalogue. Alterner produit / matière.
- Les fonds de sections gagnent à être des **matières quasi-unies** (velours, plâtre, pierre, soie) dérivées de la palette plutôt que des aplats CSS — texture à peine perceptible, contraste texte préservé, léger zoom au scroll (≈1→1.09) pour la fluidité. Jamais de texture sous une séquence d'animation frames.
- La devise/citation du client est un excellent moment typographique, mais elle doit être **portée par une section** (histoire, atelier) — posée en marge d'une grille, elle flotte.
- Une FAQ n'est pas incompatible avec le luxe : accordéon replié, typographie soignée, placée sous le CTA final. Elle sert le SEO/IA sans peser sur le parcours.

**Images**
- Détourage d'une photo prise sur fond blanc : un liseré clair de 1-2 px subsiste toujours, invisible sur fond clair, rédhibitoire sur fond sombre. Défranger systématiquement (érosion alpha) avant toute pose sur fond sombre.
- Vidéo générative produit : donner l'image de départ ET d'arrivée (deux vraies photos) contraint le modèle à n'interpoler que le mouvement — la seule façon fiable de garder le produit exact.

## Leçons du cycle de l'agence immobilière A (2026-08, 7 versions ; ces règles ne décrivent PAS un modèle à reproduire)

**Le processus** (un site « validé » a demandé 4 boucles de retours après le premier GO)
- Le protocole court (3 checkpoints : tokens+concept / hero / recette) est le bon rythme, MAIS prévoir 2-4 boucles de retours APRÈS la première mise en ligne : Sam juge sur le site vivant, pas sur des captures. Livrer tôt une version propre et itérer vite bat « finir » avant de montrer.
- **Le mode dominant peut basculer en cours de route** (l'agence immobilière A : Fonctionnel → Expérience sur « le hero doit juste faire rêver »). Ce n'est pas un échec de cadrage : re-choisir le mode explicitement, réappliquer sa grammaire entière, ne pas rafistoler l'ancien.
- Sam tranche mieux sur 2-3 options concrètes (palettes chiffrées avec préviews, concepts d'image nommés) que sur une question ouverte. Toujours proposer avec une recommandation, jamais demander « tu veux quoi ? ».
- Chaque site reste un concept propre : ne pas templater sur le précédent, ne pas imposer une technique (scroll-frames, scrub…) parce qu'elle a marché ailleurs — cas par cas, le récit décide.

**Goûts récurrents constatés (à proposer d'office, Sam reste l'arbitre)**
- Fonds de section en **matières générées** (plâtre doré, chaux ardoise, terracotta — image quasi-unie ~5 Ko WebP) plutôt qu'en grain CSS : demandé explicitement quand j'avais mis du CSS.
- Alignements stricts : une image en vis-à-vis d'un texte commence et finit à SA hauteur (crop assumé) ; les cartes d'une rangée = dimensions identiques, même ligne de base.
- Les preuves chiffrées sobres (bandeau FIN de stats) l'emportent sur les moments lyriques : un moment typographique lyrique, validé en checkpoint, a été retiré en itération pour « 3-4 grosses stats de confiance ». En stat : UNIQUEMENT du sourçable (un ordre de grandeur annoncé par le client autorise un arrondi prudent, jamais plus) ; JAMAIS de note d'avis sans l'avoir vérifiée sur la fiche Maps (puppeteer) — aucune note trouvée = aucune note affichée.
- Contact = utilitaire pur : tél (+33, même corps que les emails), emails, horaires, carte Google Maps embarquée (iframe lazy), CTA. Zéro phrase d'accroche. FAQ dans SA section, autre couleur.
- Pictogrammes de marque (loader…) en silhouette pleine, sans détails intérieurs (un détail dessiné à l'intérieur du pictogramme a été retiré en itération).
- Un loader signé (couleur de marque + pictogramme qui se remplit + pourcentage) transforme une attente technique en moment de marque — à proposer dès qu'un asset lourd se précharge.

**Vérité des matériaux**
- Vérifier l'INDÉPENDANCE du prospect (groupe/franchise) avant toute démo : un prospect s'est révélé filiale d'un groupe en plein cadrage.
- Un cartel de bien ne contient que le visible sur la photo ou l'écrit dans l'annonce (une mention non sourcée = retirée).
- Les photos réelles du client, même avec son filigrane, sont un signal d'authenticité assumé, pas un défaut à cacher.

## Leçons du cycle du cabinet de syndic (2026-08 : hero « projection », fonds texturés)

- **En prospection, le hero par défaut est une IMAGE** : un hero 100 % typographique
  impeccable a été rejeté d'une phrase (le visiteur doit pouvoir se projeter). Le
  pattern validé : image générée étalonnée pleine page + zoom léger au scroll
  (1→1.08) + nom ou une phrase, l'accent de la palette DANS l'image (un détail
  d'architecture teinté de l'accent : le client se reconnaît). Les alternatives (scroll-frames, typo pure)
  restent des choix de récit, pas le défaut.
- **Grammaire des fonds texturés** : clairs = soie/plâtre subtils (peu d'ombres) ;
  foncés = laqué mat lisse ou velours — les aspérités chaulées passent en clair
  mais font cheap en foncé ; le minéral veiné (quartz, marbre) est trop présent
  sous du texte. Une page vivante alterne image+voile (1-2 max), aplats unis et
  textures quasi-unies, avec des respirations claires entre les masses sombres.
- **Répartir les fonds selon le texte accentué** : un accent saturé ne tient pas
  sur les fonds sombres — placer les sections à texte accentué sur les fonds
  clairs, basculer numéros/filets en ivoire ailleurs. Éviter deux saturés
  complémentaires côte à côte (rouge/vert).
- **Le bottom Catalyst est FIXE** (exigence Sam) : Contact utilitaire 2 colonnes
  (tél display/email/adresse/horaires + carte Maps lazy) → FAQ (air au-dessus de
  la 1re question) → footer administratif (liens réels, © + date, logotype tronqué
  en pseudo-élément CSS). Seuls les fonds changent, jamais la disposition.
- **Bandeau de stats** : horizontal, fin, couleur UNIE (pas de texture), 3-4
  chiffres sourcés en tabular, labels eyebrow. La preuve sociale sobre, tôt dans
  la page.
- Toute image générée se CONTRÔLE avant intégration : le modèle écrit du faux
  texte lisible (titre de livre) même sans le demander — « strictly no lettering ».

## Leçons du cycle du caviste (2026-08 : images en prospection, corrections Sam)

- **Un PAYSAGE de hero doit faire rêver, pas dramatiser** : le clair-obscur
  appliqué à un extérieur (vieux ceps noueux dans la brume sombre) a été rejeté
  en une phrase : le paysage faisait peur au lieu de faire envie. La grammaire sombre/chiaroscuro
  reste valable pour les intérieurs (cave) ; dès qu'on photographie le dehors,
  basculer en lumière dorée, luxuriant, accueillant (« warm honey light,
  luminous, inviting, the kind of view that makes you dream of… »). La palette
  du site peut rester sombre : c'est l'IMAGE qui s'éclaire, le voile fait la
  jonction.
- **Un still-life IA « produit iconique » se crame instantanément** : le verre
  de vin généré en pleine page a été rejeté (l'objet généré en fond sonne
  faux) : sur un sujet archi-photographié (verre, assiette, tasse),
  l'œil détecte l'IA immédiatement. En fond de section : vraie photo du lieu,
  texture quasi-unie, ou RIEN (supprimer la section vaut mieux qu'une image
  qui sonne faux). Les générations restent bonnes pour les ambiances larges
  (paysage, cave, façade) où il n'y a pas d'objet-étalon.
- **Les fonds texturés quasi-unis sont le DÉFAUT, pas une option** (3e
  confirmation sur trois démos successives : Sam les redemande à
  CHAQUE fois qu'une V1 sort en aplats CSS) : dès la V1, poser soie/plâtre/lin
  générés (1600px q62, 4-45 Ko) sous les sections claires, avec bg-color de
  secours. Ne plus attendre le retour.
- **La photo RÉELLE du lieu bat toute génération** dans une section lieu/cave :
  utiliser les photos fournies par le client ou dont les droits sont acquis,
  les agrandir en 2K si besoin. Le prospect reconnaît SA boutique, l'effet
  « c'est déjà mon site » est immédiat.

## Leçons du cycle de l'agence immobilière B (2026-08 ; ces règles complètent celles de l'agence immobilière A, elles ne décrivent pas un gabarit)

**Copie — la coulisse est invisible**
- **Le prospect ne doit JAMAIS voir les coulisses de la mission** : pas de
  « figurait déjà sur son ancien site », pas de référence aux
  versions ou aux sources. Un fait historique s'intègre au présent (« aucun
  incident au compteur ») ; la traçabilité de la source reste dans le
  RAPPORT, pas dans la page.
- Cartels d'annonces immobilières : infos CLASSIQUES (type, m², ville) — le
  lyrisme de matière (les détails de décor) est hors sujet pour
  Sam sur une carte d'annonce. Les descriptions sensorielles vivent dans la
  prose des sections, pas dans les cartels.

**Preuves chiffrées**
- Un bandeau de stats ne se garde que s'il a des chiffres FORTS et sourcés
  (fondation, « 0 incident »…). Des stats de remplissage (nombre de métiers,
  localisation) affaiblissent : Sam a fini par supprimer le bandeau
  entier. Le chiffre manquant le plus vendeur (nombre de ventes) se demande
  au prospect, il ne s'invente pas.
- Format bandeau validé avant suppression : libellé eyebrow AU-DESSUS,
  chiffre display EN DESSOUS, fond uni vif — mais vérifier le contraste des
  petits libellés sur l'accent (l'ocre a dû être éclairci d'un cran
  pour passer 4,5:1 avec l'encre).

**Fonds texturés générés — grammaire confirmée (3 sections)**
- Une texture par section sombre/claire alternée : soie marine à plis rares
  (« VERY FEW folds, almost perfectly flat »), chaux vert profond, chaulé
  sable. Compression : 1400px q42-50 → 4-40 Ko. Les plis d'une soie se
  commandent dans le prompt ; « moins de plis » est un retour récurrent.
- Écritures blanches sur fond sombre texturé : titres pleins, corps à 85 %,
  légendes à 70 % — les trois passent le contraste sur un marine profond.

**Signal confirmé sur les deux démos immobilières**
- L'association photo réelle ↔ donnée réelle non prouvée (photos d'archives
  vs annonces d'archives) doit être SIGNALÉE à Sam, qui arbitre en
  connaissance : c'est lui le gate humain avant le prospect.

## Cadre segment AVOCAT (validé sur le site du cabinet d'avocat, 2026-08 ; s'applique PAR DÉFAUT à tout site d'avocat)

**La règle d'or, fixée par Sam : un site d'avocat est SOBRE et PRO. Pas de site
spectaculaire, pas de 3D/scroll-frames — SAUF s'il le demande explicitement.**
Un seul geste visuel : hero image pleine page + zoom léger au scroll, le reste
vit par la typographie, les fonds texturés et le rythme des sections.

**Mode et preuve**
- Mode Vision, version sobre. Son pilier « témoignage roi » est **interdit par
  la déontologie** → la preuve se déplace : parcours factuel, institutions
  (barreau d'inscription, institutions de référence du domaine, université), méthode en `<ol>`,
  publications (/conseils). Portrait RÉEL obligatoire (monogramme en attendant,
  jamais de portrait IA).
- Stats : uniquement des faits sobres vérifiables (année de serment, langues,
  domaines pratiqués). Jamais de chiffres de résultats (« X M€ gagnés »).

**Déontologie qui contraint la DA et la copie (RIN art. 10/10.5 + vade-mecum
CNB 2023 + règles du barreau concerné)**
- AUCUN avis, témoignage, note ou widget Google Reviews (lien nu vers la fiche
  toléré) ; pas d'AggregateRating dans le JSON-LD.
- AUCUN nom de client, même consentant — copie générique (une catégorie de
  clientèle, sans nom ni région identifiable).
- « Spécialiste » interdit sans certificat → « intervient en » ; max 3 domaines
  d'activités dominantes.
- Ton RIN : dignité, délicatesse, modération — zéro superlatif commercial.
- Domaine contenant le nom de l'avocat ; **déclaration du site à l'Ordre AVANT
  mise en ligne publique** → gate `INDEXATION_OUVERTE` (noindex + robots
  disallow) dans site.ts, flip + IndexNow après validation ; l'audit seaudit
  n'a de sens qu'après la levée du noindex.
- Mentions légales : médiateur de la consommation de la profession + « EI » si
  exercice individuel + directeur de publication + hébergeur.

**Hero avocat — le vocabulaire validé**
- JAMAIS de cliché : balance, marteau, colonne de prétoire frontale, paperasse,
  poignée de main, portrait IA.
- Validé (goût client confirmé) : **architecture de la ville du client en abstraction
  graphique** — mécanisme lenzstaehelin.com : ombres longues d'heure dorée,
  silhouettes anonymes minuscules, géométrie (arcades en perspective fuyante
  retenues ; zénithale de place possible), **texte central « chuchoté »**
  (capitales trackées ~2rem, pas de logotype monumental), scrim doux + légères
  text-shadows. L'accent de la palette vit DANS l'image (porte, store).
- Codes typographiques qui ont plu (référence Céline) : logotype et wordmarks
  en capitales sans-serif trackées, serif éditorial (romain+italique) pour les
  phrases et titres de sections.

**Fonds** : alternance de textures sobres quasi-unies — lin/soie ivoire en
clair, UNE soie profonde à plis rares (navy) en bloc de milieu de page, colophon
sombre distinct conservé. Grammaire des textures : leçons du cabinet de syndic et de l'agence immobilière B.

**Ce qui reste vrai du reste du skill** : rotation palette+fonts obligatoire
entre avocats (registre interne de rotation), bottom verrouillé, protocole interactif
complet (checkpoints, 2-3 options chiffrées avec reco à chaque indécision).

## Contrôle avant livraison

- [ ] Aucun composant n'a son style par défaut.
- [ ] L'accent respecte son budget de surface.
- [ ] Le rapport display/corps est d'au moins 6:1.
- [ ] Le padding de section est à 120px minimum sur desktop.
- [ ] La grille se casse au moins une fois.
- [ ] Toutes les images sont étalonnées ensemble.
- [ ] L'objet de confiance (ou sa matière) apparaît dans le premier écran — sans argumentaire ni CTA (sauf mode Fonctionnel et variantes e-commerce : un seul CTA discret).
- [ ] Une seule idée forte par page, formulable en une phrase.
- [ ] Toutes les durées d'animation sont entre 500 et 900ms, avec des courbes personnalisées.
- [ ] `prefers-reduced-motion` géré.
- [ ] Mobile composé à part, pas juste empilé.
- [ ] Zéro tiret cadratin dans les textes ; insécables françaises posées (» ; : ! ?).
- [ ] Un seul moment spectaculaire dans la page, pas dupliqué.
- [ ] PageSpeed mobile ≥ 90 — engagement commercial Catalyst, non négociable.

## Test final

Retirer le logo et le nom du client. Si le site pourrait appartenir à un autre commerce du même secteur, il n'est pas sur-mesure — recommencer à l'étape des tokens.
