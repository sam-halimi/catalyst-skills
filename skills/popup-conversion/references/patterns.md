# Patterns de capture — catalogue et critères

Pour chaque pattern : quand il marche, quand il dessert, exigences propres.
Tous héritent des règles transverses du SKILL.md (une offre réelle, une
demande, sortie évidente, zéro dark pattern) et des tokens `da-moderne` du
site — jamais de style générique de librairie.

## Lead magnet classique
Formulaire simple contre un livrable réel (guide, checklist, estimation PDF).
- **Marche** : niches à cycle long (immobilier, B2B) où le livrable prouve
  l'expertise ; c'est le défaut le plus sûr.
- **Dessert** : si le livrable n'existe pas encore — ne jamais promettre un
  document non produit ; le livrable fait partie du périmètre de mission.

## Micro-engagement
Une question à choix (« Vous êtes propriétaire ou locataire ? ») AVANT le
champ email — l'utilisateur investi convertit mieux, la réponse qualifie.
- **Marche** : quand la réponse change réellement la suite (segmentation du
  message de confirmation, du lead transmis).
- **Dessert** : question décorative dont la réponse ne sert à rien — c'est du
  friction theater, s'abstenir.

## Quiz
3-5 questions → résultat personnalisé contre email.
- **Marche** : éditorial, personnalité/sport, commerce à conseil (quel vin,
  quel bien, quel accompagnement).
- **Exigences** : barre de progression honnête, résultat réellement
  différencié (pas 4 chemins vers le même texte), abandon possible à tout
  moment sans perdre la navigation.

## Visual quiz
Quiz dont les réponses sont des images (styles, ambiances, biens).
- **Marche** : niches visuelles (immobilier premium, hospitality, DA forte) —
  cohérent avec la promesse « show don't tell ».
- **Exigences** : images étalonnées palette du site (générées/retouchées selon
  le pipeline assets du projet), poids surveillé (lazy, WebP), alt text réels.

## Scratch (carte à gratter)
Révélation d'une offre par interaction de grattage.
- **Marche** : commerce/hospitality à offre concrète (dégustation, remise
  d'accueil) sur une marque qui assume le ludique.
- **Dessert** : luxe sobre, avocat, éditorial sérieux — l'écart de ton coûte
  plus que la conversion ne rapporte.
- **Exigences** : le gain est réel et unique (pas de « re-gratter pour
  perdre ») ; équivalent clavier/lecteur d'écran obligatoire (bouton
  « révéler l'offre »).
- **Référence auditée et spécification complète** (parcours en 3 écrans,
  mesures, seuil de révélation, gain signé serveur, recette) :
  [scratch-card.md](scratch-card.md), d'après le popup public d'une marque de boisson.

## Mystery reward
« Une attention vous attend » — contenu révélé après email.
- **Marche** : hospitality, commerce de plaisir (caviste, restaurant) — si la
  récompense est définie À L'AVANCE et honorée.
- **Dessert** : toute niche où l'opacité évoque l'arnaque (immobilier, droit,
  finance).
- **Exigences** : contenu réel documenté dans la spec ; formulation qui ne
  promet pas plus que le contenu.

## Gamification (roue, jeu, défi)
- **SEULEMENT si cohérente** avec la marque et validée par Sam : jamais sur le
  luxe sobre, le réglementé, le premium discret — c'est-à-dire l'essentiel du
  portfolio Catalyst. La charge de la preuve est sur le POUR.
- **Exigences** si retenue : probabilités honnêtes affichables, gains réels,
  une participation par cap de fréquence, même a11y que le scratch.

## Classique (newsletter / rappel)
Bandeau ou modal sobre « Être rappelé » / « Recevoir les nouveautés ».
- **Marche** : partout où le reste serait trop ; défaut du cadre avocat si une
  capture est voulue (sobre, factuel, sans promesse).

## Choisir — grille rapide

| Contexte | 1er choix | 2e choix |
|---|---|---|
| Immobilier | lead magnet (estimation/guide) | micro-engagement |
| Avocat | classique sobre (ou aucune capture) | — |
| Commerce / hospitality | mystery reward ou scratch (si ton assumé) | quiz |
| Éditorial | quiz | classique |
| Personnalité / sport | visual quiz | micro-engagement |
| Doute | inline seul, pas de popup | — |
