# Architecture et physique

## Carte des fichiers
- `plinko-trigger.tsx` : routes autorisées, attente après hero, cadence, stockage UI, priorité aux autres modales, chargement dynamique.
- `plinko-lead-capture.tsx` : étapes intro → drawing → dropping → landed → email → claiming → done, focus et fermeture, formulaire, résultat, tracking.
- `board.tsx` : plateau SVG, bille, position instantanée de lâcher (`billeEtat`).
- `trajectory.ts` : trajectoire échantillonnée, collisions et arrivée contrôlée. Lire le code et les tests avant de modifier restitution/gravité.
- `lib/plinko/shared.ts` : géométrie, types, lots et chemins partagés, sans Node ni secret.
- `server.ts` : HMAC, choix du lot, code, rate limit, intégration Klaviyo côté serveur.
- `config.ts` : timing, textes FR/EN, fréquence et clés de persistance.
- `/api/plinko/draw`, `/claim`, `/reset` : contrats serveur et cookies HttpOnly.

## Règles validées sur le projet de référence
Plateau logique largeur 400 ; centres des cinq cases x=40,120,200,280,360. Récompenses seulement aux indices 0,2,4. La case gagnante est la récompense la plus proche de la position exacte de lâcher reçue en `dropX`, et non un tirage pondéré hérité d'une version antérieure, même s'il subsiste dans le code comme fonction historique. Ne pas annoncer des probabilités que le jeu n'applique pas. La bille doit descendre vers son lot signé sans se téléporter vers une autre case.

La position de départ et la vitesse doivent partir de la bille réellement visible. Garder le premier point, les contacts picots et la dernière arrivée cohérents. Un résultat serveur ne peut pas être remplacé par la case où une animation improvisée semble tomber. Conserver les tests géométriques, la sélection du lot au point de lâcher, les cas limites à x=120 et 280, les zones décoratives et les reprises.

## Déclenchement
Le jeu ne s'ouvre pas pendant le hero. Le chronomètre s'arme à sa sortie ; réglage de référence : desktop délai 10 s ou scroll 40 %, mobile 12 s ou 45 % ; exit intent desktop seulement. Exclure panier/checkout/cart. Ne pas empiler le jeu sur la personnalisation ou une autre modale : céder la place et attendre. Une ouverture forcée pour la recette ne prouve pas que le déclenchement normal est correct. La remise à zéro de l'état UI puis des cookies serveur sert uniquement à la recette ciblée.

Le cap utilise localStorage versionné, la session conserve son délai entre pages. En phase de collecte réelle, figer la variable de version d'état du popup ; ne plus utiliser Date.now à chaque build, sinon tous les refus sont oubliés. Une modification d'assets du hero n'autorise pas à relancer le popup chez chaque visiteur. Vérifier fermeture, subscriber, gain déjà réclamé et reprise d'un gain non réclamé.

## UI et recette
Fermeture visible, Échap, clic fond ; focus piégé puis rendu à l'ouvreur. Le mobile court doit montrer action, plateau et formulaire sans zone hors d'atteinte. Mode mouvement réduit : trajectoire abrégée et résultat inchangé. Préserver les textes FR/EN, le bouton de réessai, les erreurs réseau et l'état de gain lors d'un échec.

Tester les trois destinations, plusieurs vitesses, dimensions 1440×900/390×844/390×700, fermeture/réouverture autorisée, navigation, interaction avec le panier et la personnalisation. La simulation de physique passe par des tests, puis le vrai rendu doit être regardé. Un screenshot de la case finale ne valide pas le trajet.
