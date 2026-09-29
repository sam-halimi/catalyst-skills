# Schéma d'état `.catalyst/production.yaml` — version 2

Un fichier par projet : `<projet>/.catalyst/production.yaml`. C'est la source
de vérité de la mission (la conversation ne l'est jamais). Toute session doit
pouvoir reprendre depuis ce fichier seul + `DECISIONS.md` + les docs du projet.
Validation déterministe : `python3 ../scripts/validate-state.py <fichier>`.

## Règles

- `schema_version` obligatoire (entier, actuellement `2`). Toute évolution du
  schéma incrémente la version et documente la migration ici.
  - **Migration v1 → v2 (2026-08-23)** : ajout de `seo.objectif` et
    `seo.requetes_cibles`. Les états v1 restent valides tels quels
    (`objectif: demo` implicite) ; toute reprise qui rouvre le lot SEO les
    passe en v2.
- **Aucun secret** : jamais de token, clé API, mot de passe, URL signée. Les
  intégrations sont référencées par NOM de service ; les secrets vivent dans
  les variables d'environnement Vercel. Le validateur refuse les motifs
  suspects.
- Timestamps ISO 8601 (`YYYY-MM-DDTHH:MM:SS+02:00` ou suffixe `Z`).
- Le slug doit correspondre au basename du path (`site-<slug>`).
- Mise à jour à chaque checkpoint franchi, décision structurante ou
  verrouillage (le détail narratif reste dans `DECISIONS.md`).

## Schéma (champs et valeurs autorisées)

```yaml
schema_version: 2

projet:
  nom: "Maison Exemple"          # nom commercial réel
  slug: "maison-exemple"          # => dossier site-maison-exemple
  path: "<projets>/sites/site-maison-exemple"

mode: new                         # new | resume | special
mode_detail: null                 # texte libre si special
statut: pre_da                    # onboarding | pre_da | production | recette | iterations | cloture | archive
checkpoint: onboarding_valide     # onboarding_valide | design_read | checkpoint_1_da | go_da |
                                  # checkpoint_2_hero | checkpoint_3_recette | gates_sortie | cloture

crm:
  statut: present                 # present | absent | special
  ligne_ref: "CRM de prospection / Maison Exemple"   # référence lisible, jamais de copie de données

niche: commerce_hospitality       # immobilier | avocat | commerce_hospitality | editorial | personnalite_sport | autre
autonomie: checkpoints_cles       # guidee | checkpoints_cles | autonome_apres_go_da

break_rules:
  active: false
  rules_lifted: []                # requis non vide si active
  reasons: {}                     # une raison par règle levée
  invariants_confirmes: false     # doit être true si active

contraintes:
  cadre_avocat: false
  juridiques: []                  # textes libres (réglementation, mentions…)
  marque: []                      # chartes, interdits client

recherche:
  mode: recherche_complete        # fourni | recherche_complete | adaptation | hybride
  sources: []                     # docs produits dans <projet>/docs/

da:
  mode: libre                     # libre | imposee | hybride
  brief: null
  direction_validee: null         # rempli au GO DA (nom de la direction retenue)

hero:
  type: recommandation            # scroll_frames_3d | image_animee | statique | typographique | recommandation

assets:
  source: mixtes                  # fournis_sam | internet | generes_ia | mixtes
  notes: null

sections:
  mode: libres                    # libres | imposees | hybrides
  liste: []

contenu:
  mode: recherche_complete        # fourni | recherche_complete | adaptation | hybride

seo:
  socle: complet                  # complet | local | editorial_geo | noindex_temporaire | exception
  objectif: demo                  # demo | vitrine_locale | trafic
  requetes_cibles: []             # requis (3 à 5 entrées) si objectif: trafic
  indexation: ouverte             # ouverte | gate_noindex
  exception_raison: null

conversion:
  capture: aucune                 # aucune | inline | popup | les_deux
  offre: null
  popup:                          # requis si capture in (popup, les_deux)
    type: null                    # micro_engagement | quiz | visual_quiz | scratch | mystery_reward |
                                  # gamification | classique | recommandation
    triggers: []                  # delai | scroll | exit_desktop | clic | pages | comportement
    frequency_cap: null           # ex. "1 / 7 jours, réouverture sur clic"
    exclusions: []
  destination: []                 # email | crm_sheet | brevo | klaviyo | webhook | autre

tracking:
  consentement_requis: false
  events: []                      # impression | engagement | submit | success | close
  ab_test: false
  variantes: []

qa:
  gates_bloquants_ouverts: []     # vide = clôturable ; sinon liste des gates
  scores: {}                      # derniers scores mesurés (lighthouse, seaudit…)

validations:                      # journal des GO de Sam (append-only)
  - date: "2026-08-16T12:00:00+02:00"
    objet: "onboarding"
    decision: "valide"

points_ouverts: []                # questions rouvertes / données « à compléter »

timestamps:
  created: "2026-08-16T12:00:00+02:00"
  updated: "2026-08-16T12:00:00+02:00"
```

## Champs conditionnels (imposés par le validateur)

| Condition | Exigence |
|---|---|
| `break_rules.active: true` | `rules_lifted` non vide, une `reasons.<règle>` par entrée, `invariants_confirmes: true` |
| `conversion.capture` ∈ {popup, les_deux} | bloc `conversion.popup` présent avec `type` non nul |
| `conversion.capture` ≠ aucune | `conversion.destination` non vide |
| `seo.socle: exception` | `seo.exception_raison` non nul |
| `seo.objectif: trafic` | `seo.requetes_cibles` : 3 à 5 requêtes non vides |
| `niche: avocat` | `contraintes.cadre_avocat: true` |

## Fichiers frères dans `.catalyst/`

- `lessons-candidates.md` — leçons locales en attente de promotion validée
  (`/production-finish`). Jamais promues automatiquement.
- Pas d'`events.jsonl` en MVP (décision Sam 2026-08-16) : `production.yaml` +
  `DECISIONS.md` couvrent la reprise.
