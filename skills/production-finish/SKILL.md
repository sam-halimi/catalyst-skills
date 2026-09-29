---
name: production-finish
description: "Clôture d'une mission site Catalyst. Lit l'état .catalyst/production.yaml, REFUSE de marquer terminé si des gates bloquants restent ouverts, déroule la checklist QA dans l'ordre (build, console, liens, assets, responsive, a11y, SEO/GEO, perf protocole VPS, formulaires, popup, leads, tracking, juridique/marque), crée ou met à jour <projet>/RAPPORT.md, puis applique l'apprentissage contrôlé : leçons candidates présentées une à une avec destination et diff exact, promotion uniquement sur validation explicite de Sam. Déclencheurs : clôture, finir la mission, production finish, enrichis nos données."
argument-hint: "[nom du projet]"
---

# /production-finish — clôture contrôlée d'une mission Catalyst

## 1. Lire l'état, refuser si gates ouverts

- Localiser le projet (mêmes règles que `project-resume` : chemin affiché,
  jamais de sélection silencieuse) et lire `.catalyst/production.yaml`
  (validé par `python3 ~/.claude/skills/website-production/scripts/validate-state.py`).
  Sans état : proposer d'abord une reprise `/project-resume` — pas de clôture
  à l'aveugle.
- **Refus de clôturer** tant que `qa.gates_bloquants_ouverts` n'est pas vide ou
  qu'un item bloquant de la checklist échoue. Le refus liste précisément ce qui
  bloque et la prochaine action. Un point non bloquant va dans
  `points_ouverts` du RAPPORT, pas dans l'oubli.

## 2. Vérifier, dans l'ordre

Checklist détaillée, item par item, avec commandes :
[references/qa-checklist.md](references/qa-checklist.md). Ordre imposé :
1. Build propre.
2. Erreurs console / hydratation.
3. Liens et routes.
4. Assets : poids, formats, alt.
5. Responsive 360 / 390 / 768 / 1440.
6. Accessibilité.
7. SEO / GEO / indexation (socle `seo-garantie-90` — par référence).
8. Performance selon le **protocole VPS existant** (playbook interne, non
   publié : alias prod public, best-of-N si missions parallèles, script
   d'audit Lighthouse mobile ; seuil : performance mobile ≥ 90).
9. Formulaires.
10. Popup : triggers, frequency cap, mobile, clavier.
11. Destination des leads.
12. Tracking.
13. Contraintes juridiques et marque (dont cadre déontologique d'une
    profession réglementée si applicable).

**Toute action externe de test de lead** (envoi réel vers email/Brevo/Klaviyo/
webhook) utilise une donnée de test **explicitement autorisée** ou demande
confirmation avant l'envoi. Jamais de donnée inventée vers un vrai service.

## 3. Produire ou mettre à jour `<projet>/RAPPORT.md`

Gabarit : [templates/RAPPORT.md](templates/RAPPORT.md) (le nom canonique du
rapport est `RAPPORT.md` — décision Sam 2026-08-16 ; ne jamais créer de
`PRODUCTION_REPORT.md`). Si un `RAPPORT.md` existe déjà (missions précédentes),
le **mettre à jour** en conservant son historique — jamais l'écraser.
Contenu obligatoire : périmètre, URL/commit/date, décisions, checkpoints,
fichiers majeurs, tests et scores, popup/intégrations, erreurs rencontrées et
résolues, points ouverts, procédure de rollback, leçons candidates.

Mettre à jour l'état : `statut: cloture`, `checkpoint: cloture`, scores dans
`qa.scores`, entrée `validations` datée.

## 4. Apprentissage contrôlé — promotion des leçons

Règle d'apprentissage contrôlé des instructions globales (2026-08-16) : les
leçons vivent en LOCAL
(`.catalyst/lessons-candidates.md`, `DECISIONS.md`, `RAPPORT.md`) et **rien
n'est promu automatiquement** vers le fichier d'instructions globales
(`CLAUDE.md`), le playbook interne, un skill spécialisé ou une mémoire globale.

Procédure :
1. Rassembler les candidates (fichier local + leçons relevées en session).
2. Pour CHACUNE, préparer : destination exacte proposée (`CLAUDE.md` /
   section précise du playbook interne / skill nommé / mémoire nommée) +
   **texte ou diff exact** prêt à appliquer.
3. AskUserQuestion **item par item** (par lots de 3-4 maximum) : Promouvoir
   telle quelle / Promouvoir modifiée (texte de Sam) / Garder locale /
   Abandonner.
4. N'appliquer QUE les promotions validées, exactement comme validées ;
   consigner le sort de chaque candidate dans le RAPPORT.
5. Registre rotation palettes/typos (tenu dans le playbook interne) : même
   régime, proposer la ligne exacte, attendre validation.

## 5. Fin de mission

- Rappel des actions qui restent à Sam : valeurs à reporter dans le CRM de
  prospection (lecture seule pour l'agent), déclarations externes éventuelles
  (ordre professionnel, fiche Google).
- Ne rien supprimer, ne rien archiver, ne rien déployer de nouveau à cette
  étape sans demande explicite.
