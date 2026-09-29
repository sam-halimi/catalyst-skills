# Carte à gratter : audit de référence et spécification

Référence auditée le 2026-09-29 : popup public d'une marque de boisson vendue en ligne (outil de popup tiers, relié à Klaviyo). Observation en mobile 390 × 844, grattage simulé au doigt, aucune adresse saisie ni soumise. Les captures et les deux scripts d'observation puppeteer (l'un observe un popup sans le fermer, l'autre gratte puis ouvre l'étape suivante) sont conservés hors dépôt.

Ce document décrit un mécanisme à transposer. La marque, l'image, l'offre et les textes se redéfinissent pour chaque client dans ses propres tokens `da-moderne`.

## 1. Ce que fait la référence

**Parcours en 3 écrans, un seul champ**
1. **Invitation** : logotype, titre « Try Your Luck », consigne « Scratch below to see your offer », carte à gratter.
2. **Révélation** : la carte découvre le gain (un an de produit à gagner, en capitales) et un bouton « CLAIM » apparaît sous la carte.
3. **Capture** : le titre devient le gain, un champ email, un bouton « CONTINUE ».

**Mesures**
- Apparition entre 3 et 6 secondes après le chargement, sans interaction préalable, en plein écran sur mobile.
- Carte : 300 × 220 px CSS, canvas en double densité (600 × 440), rayon 16px. C'est le seul arrondi de tout le popup.
- Couche à gratter : ardoise texturée `#333B41`, monogramme de marque en ton sur ton, libellé « SCRATCH HERE » en capitales claires.
- Révélation complète après 3 passages de doigt sur la largeur. Le canvas passe alors en `opacity: 0` et `pointer-events: none` : le visiteur ne finit jamais de gratter à la main.
- Boutons et champ : hauteur 56px, largeur 288 à 300px, rayon 0, filet 1px `#2C3138`, fond transparent, libellé 18px graisse 800 en capitales. Champ à fond blanc, filet à 40 % d'opacité.
- Typographie : la grotesque de la marque. Titre 35px graisse 700, consigne 20px.
- Fond : photo produit pleine hauteur (canette qui verse), dégradé studio du gris `#696E76` au gris clair `#E0E2E5`. Le filet de liquide traverse les trois écrans et relie visuellement les étapes.
- Fermeture : croix de 24px en haut à gauche.

**Pourquoi ça marche**
- Le geste précède la demande. Le visiteur a déjà « gagné » quelque chose quand on lui demande son email : l'adresse sert à récupérer un dû, pas à payer un accès.
- Le popup est une image de campagne, pas un formulaire. Aucune boîte, aucune ombre, aucun fond blanc : il a la même qualité que le hero.
- Un champ, un bouton par écran. Rien à lire, rien à choisir.
- Le seuil de révélation bas supprime la corvée : trois gestes et c'est fini.

## 2. Ce qu'on ne reprend pas

| Observé sur la référence | Règle Catalyst |
|---|---|
| Plein écran mobile dès 3 à 6 s, sans interaction | Interdit (interstitiel intrusif). Déclencheur après engagement : scroll de 40 à 50 %, ou 2e page vue, ou 30 s de présence active. |
| « Try Your Luck » alors que le gain est identique pour tous | Pas de faux tirage. Si le gain est unique, le texte parle de découvrir une offre, pas de tenter sa chance. |
| Gain affiché = participation à un tirage au sort | Un tirage au sort est un jeu-concours : règlement accessible, dates, dotation, modalités. Par défaut, préférer un gain certain (remise, échantillon, livraison offerte). |
| Croix de fermeture de 24px | Zone tactile de 44 × 44 px minimum. |
| Aucune alternative au geste de grattage | Bouton « Révéler l'offre » visible, utilisable au clavier et au lecteur d'écran. |
| Aucune mention de consentement visible à l'écran de capture | Mention de consentement et lien vers la politique de confidentialité sous le champ. |

## 3. Spécification de transposition

**Pertinence** : marque qui assume le ludique et dispose d'une offre réelle (voir `patterns.md`, section Scratch). Cohérent avec la variante « Produit-héros » de `da-moderne`. Exclu pour le luxe sobre, le réglementé et les démos de prospection.

**Structure**
- Composant client chargé en différé (`next/dynamic`, `ssr: false`), monté seulement quand le déclencheur est atteint. Aucun octet dans le chemin critique.
- Mobile : feuille plein écran APRÈS engagement. Desktop : modale centrée de 420 à 480px de large, même composition verticale, image de fond conservée.
- Image de fond : visuel produit ou matière du client, étalonné avec le site, WebP de 60 Ko maximum, préchargé au moment du déclenchement et non au chargement de la page.
- Machine à 4 états : `invitation` → `revelation` → `capture` → `confirmation`. L'état est persisté (localStorage) pour qu'un visiteur qui a gratté puis fermé retrouve son gain et non une carte neuve.

**Carte**
- Un `<canvas>` posé sur le contenu du gain. Couche dessinée une fois (texture ou aplat + monogramme du client), puis effacée en `globalCompositeOperation = 'destination-out'` avec un pinceau rond de 36 à 44px.
- Pointer Events (souris, doigt, stylet) avec `touch-action: none` sur la carte pour que le grattage ne fasse pas défiler la page.
- Mesure de la surface découverte par échantillonnage du canal alpha (1 pixel sur 16 suffit), au plus une fois toutes les 150 ms.
- **Seuil de révélation : 45 à 50 %.** Au seuil, fondu de la couche restante en 500 à 700 ms, courbe `cubic-bezier` personnalisée, puis passage à l'état `revelation`.
- Canvas en double densité, dimensionné par `devicePixelRatio`, redessiné au redimensionnement.

**Gain**
- Le gain est décidé et signé côté serveur AVANT l'affichage, jamais calculé dans le navigateur. Même contrat que les lots du skill `plinko-popup` (voir sa référence `capture.md`) : jeton signé, usage unique, durée de validité.
- Le texte du gain n'est injecté dans le DOM qu'à la révélation. Avant, la carte expose seulement son libellé accessible (« Carte à gratter : révélez votre offre »).
- Un gain par visiteur et par période de cap. Pas de seconde carte après un refus ou une fermeture.

**Accessibilité**
- Bouton « Révéler l'offre » sous la carte, présent dès l'état `invitation`.
- `prefers-reduced-motion` : pas de grattage, la carte se révèle au clic par un simple fondu.
- Révélation annoncée dans une région `aria-live="polite"`.
- Focus piégé dans le popup, rendu au déclencheur à la fermeture, ESC actif, fermeture de 44 × 44 px.

**Capture**
- Un champ email (`type="email"`, `autocomplete="email"`, `inputmode="email"`), libellé réel et non un simple placeholder.
- Validation serveur, honeypot, délai minimal. Règles complètes dans `integrations-tracking.md`.
- Écran de confirmation : le gain et son mode d'emploi affichés immédiatement, et envoyés par email. Un gain annoncé est un gain utilisable tout de suite.

**Événements** (schéma commun du skill, plus deux propres au pattern)
`impression`, `engagement` (premier contact avec la carte), `scratch_progress` (25 %, 50 %), `reveal`, `submit`, `success`, `close` (avec l'état atteint).

**Budget**
- JavaScript du composant : 8 Ko gzip maximum, sans librairie de grattage tierce.
- Aucun effet sur LCP, CLS ou TBT de la page hôte : à vérifier en Lighthouse mobile avec le déclencheur forcé.

## 4. Recette

- [ ] Grattage fluide au doigt sur iPhone, sans défilement de la page.
- [ ] Révélation automatique au seuil, jamais de carte à finir à la main.
- [ ] Parcours complet au clavier seul.
- [ ] Parcours complet avec `prefers-reduced-motion`.
- [ ] Fermer puis rouvrir : le gain révélé est conservé.
- [ ] Refus respecté : pas de réapparition avant la fin du cap.
- [ ] Le gain reçu par email est identique au gain affiché, et il fonctionne réellement (code testé au panier).
- [ ] Performance mobile de la page hôte inchangée, à 90 ou plus.
