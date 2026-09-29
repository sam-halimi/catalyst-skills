# Triggers, cadence, mobile, accessibilité, consentement

## Triggers disponibles

| Trigger | Défaut conseillé | Notes |
|---|---|---|
| Délai | 20-40 s (jamais < 10 s) | Seul, c'est le plus faible signal d'intérêt. |
| Scroll | 50-70 % de la page | Bon proxy d'engagement sur les mono-pages Catalyst. |
| Exit-intent | **desktop uniquement** | Détection souris vers le haut. **JAMAIS par défaut sur mobile** — pas d'équivalent fiable, et les heuristiques (scroll-up rapide, back) punissent la navigation normale. |
| Clic | CTA dédié (« Recevoir le guide ») | Le plus propre : intention explicite, zéro intrusion. À privilégier quand l'offre a une place naturelle dans une section. |
| Pages vues | ≥ 2 pages | Rarement utile sur les mono-pages ; pertinent sur les sites éditoriaux. |
| Comportement | temps sur une section clé, retour sur les prix | Ne l'utiliser que si l'événement a un sens métier démontrable. |

Combinaison recommandée par défaut : **clic (toujours disponible) + un seul
trigger passif** (scroll OU délai OU exit desktop). Deux triggers passifs qui
peuvent se cumuler = impression de harcèlement.

## Frequency cap et réouverture

- Cap par défaut : **1 affichage passif / 7 jours**, stocké en
  `localStorage` (clé versionnée `popup_<slug>_v1`).
- Fermeture ou refus = même cap qu'une non-conversion. Un refus se respecte.
- Succès (lead soumis) = plus jamais d'affichage passif (flag permanent).
- **Réouverture volontaire toujours possible** via le CTA cliquable — le cap ne
  s'applique qu'aux déclenchements passifs.
- Pages exclues par défaut : mentions légales, politique de confidentialité,
  /conseils (lecture), pages d'erreur.

## Mobile

- Format : bottom-sheet ou bandeau, jamais un plein écran qui couvre le
  contenu au chargement (interstitiel intrusif → pénalité SEO + gate du
  playbook interne).
- Déclenchement passif mobile : scroll profond ou clic uniquement.
- Zone de fermeture ≥ 44×44 px, atteignable au pouce.
- Tester aux breakpoints du cadre : 360, 390, 768, 1440.

## Accessibilité (bloquant en recette)

- `role="dialog"` + `aria-modal="true"` + `aria-labelledby` sur le titre.
- Focus déplacé dans le popup à l'ouverture, **piégé** pendant, **rendu à
  l'élément déclencheur** à la fermeture.
- Fermeture : bouton visible et labellisé, touche ESC, clic sur l'overlay.
- Scroll de fond verrouillé pendant l'ouverture ; `prefers-reduced-motion`
  respecté sur l'animation d'entrée (budget mouvement de l'agence : une
  animation d'entrée par section, 500 à 900 ms, `cubic-bezier` personnalisé).
- Contrastes AA sur tous les états, y compris placeholder et erreurs.

## Performance (gates du playbook interne inchangés)

- Composant en `next/dynamic`, chargé après première interaction utilisateur
  ou idle — jamais dans le chemin critique, zéro impact LCP/TBT mesurable.
- Assets du popup (images de quiz, textures) : lazy, WebP, budgets images du
  cadre mission ; aucune police supplémentaire dédiée au popup.
- Le popup ne doit faire bouger AUCUN score des gates de sortie : mesurer
  avant/après son intégration.

## SEO

- Pas d'interstitiel au chargement, pas de plein écran mobile pré-interaction
  (critères « intrusive interstitials » Google).
- Le contenu du popup n'est pas du contenu SEO : rien d'indexable d'important
  ne doit vivre uniquement dedans.

## Consentement et confidentialité

- Si le dispositif se limite à un envoi volontaire (formulaire) + localStorage
  fonctionnel (frequency cap) : pas de bandeau cookies requis — le dire dans
  la politique de confidentialité (base légale : consentement à l'envoi ;
  finalité et destinataire nommés).
- Tout tracking tiers (pixel, analytics marketing) ou cookie non exempté →
  `tracking.consentement_requis: true` dans l'état, bandeau AVANT dépôt, et le
  popup ne déclenche ses événements qu'après consentement.
- Case d'opt-in newsletter séparée et NON pré-cochée si l'email doit servir
  au-delà de la demande initiale ; mention de désinscription dans chaque envoi.
- Minimisation : ne collecter que ce que l'offre justifie.
