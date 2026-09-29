---
name: project-resume
description: "Reprise d'un projet site Catalyst après /clear ou changement de session — aussi utilisé comme branche « reprise » de /website-production. Retrouve le projet (exact puis fuzzy sous sites/, puis archives-sites/), lit .catalyst/production.yaml en priorité, sinon reconstruit un aperçu proposé depuis Git, CLAUDE.md, DECISIONS.md, RAPPORT.md, docs/checkpoint* et la structure, à faire valider AVANT toute matérialisation. Affiche checkpoint courant, éléments verrouillés, travail en cours, points ouverts, prochaine action. Déclencheurs : reprise, reprendre le projet X, où en est le site Y, continuer la mission."
argument-hint: "[nom du projet]"
---

# /project-resume — reprise d'un projet Catalyst

Objectif : après `/clear`, l'état local suffit à une reprise complète. Ce
skill lit, propose, et n'écrit qu'avec validation explicite.

## 1. Localiser le projet (lecture seule)

- Lancer `bash ~/.claude/skills/website-production/scripts/discover-project.sh "<terme>"`
  (recherche exacte puis fuzzy sous `<projets>/sites/`, puis
  `<projets>/archives-sites/` ; les deux racines se règlent par les variables
  d'environnement `CATALYST_SITES_DIR` et `CATALYST_ARCHIVES_DIR`).
- **Ambiguïté (0 ou ≥ 2 candidats plausibles)** → AskUserQuestion avec, par
  option : chemin complet, date du dernier commit git (ou « git absent »),
  fichiers d'état présents. Jamais de sélection silencieuse ; toujours
  afficher le chemin retenu avant de continuer.
- Un candidat sous `archives-sites/` se signale comme ARCHIVE : demander si la
  reprise se fait sur place (lecture) ou passe par une nouvelle mission
  (`/website-production`) — ne jamais déplacer ni modifier une archive.

## 2. Lire l'état — `production.yaml` en priorité

**Cas A — `.catalyst/production.yaml` existe** : le valider
(`python3 ~/.claude/skills/website-production/scripts/validate-state.py <fichier>`),
puis charger. Compléter le contexte avec `DECISIONS.md` et le `RAPPORT.md`
s'ils existent. Un état invalide se signale avec les erreurs exactes : proposer
la correction en diff, ne pas corriger silencieusement.

**Cas B — pas d'état** : reconstruire un **aperçu proposé** (rien n'est écrit)
à partir de, dans l'ordre :
1. Git : `git log --oneline -15`, dernier commit, fichiers non commités.
2. `CLAUDE.md` / `AGENTS.md` du projet (pointeurs d'autorité).
3. `DECISIONS.md` (arbitrages) et `RAPPORT.md` (versions, scores, points ouverts).
4. `docs/checkpoint*`, `docs/*` (recherches, DESIGN READ).
5. `package.json` + structure (`app/`, `components/`, `public/`) — stack,
   sections existantes, séquences de frames.

L'aperçu proposé remplit le gabarit de `production.yaml`
(schéma : `~/.claude/skills/website-production/references/state-schema.md`)
avec les valeurs DÉDUITES marquées comme telles et `points_ouverts` pour tout
ce qui reste incertain. Puis AskUserQuestion :
- **Valider et matérialiser l'état** (créer `.catalyst/production.yaml` — le
  chemin exact est affiché avant l'écriture)
- **Corriger l'aperçu** (rejouer les points contestés)
- **Continuer sans état** (session en lecture seule, rien n'est écrit)

**Interdits sans validation explicite** : matérialiser un fichier d'état,
`git init`, créer un commit, modifier quoi que ce soit dans le projet.

## 3. Restituer la situation

Afficher, dans cet ordre :
1. **Dernier checkpoint franchi** (mapping :
   `~/.claude/skills/website-production/references/checkpoints.md`) et statut.
2. **Éléments verrouillés** (direction DA validée, textes figés, sections
   « n'y touche plus », bottom verrouillé…) — depuis `validations` et
   `DECISIONS.md`.
3. **Travail en cours** (fichiers non commités, section entamée).
4. **Points ouverts** (données « à compléter », questions rouvertes).
5. **Prochaine action** recommandée, une seule, concrète.

## 4. Reprendre sans re-questionner

Ne rejouer que les questions **manquantes ou explicitement rouvertes** du
questionnaire d'onboarding
(`~/.claude/skills/website-production/references/onboarding.md`) — jamais le
QCM complet si l'état répond déjà. Les règles pré-GO (exception étroite du
CLAUDE.md), les checkpoints et l'apprentissage contrôlé s'appliquent à
l'identique en reprise.

## Dépendance

Ce skill s'appuie sur cinq fichiers du skill `website-production`, à installer
à côté de lui : `scripts/discover-project.sh`, `scripts/validate-state.py`,
`references/state-schema.md`, `references/checkpoints.md` et
`references/onboarding.md`.
