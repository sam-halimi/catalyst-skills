---
name: website-production
description: Orchestrateur d'onboarding des missions site Catalyst. Cadre une nouvelle mission, une reprise ou une mission spéciale AVANT le checkpoint 1 (GO DA) — QCM AskUserQuestion par lots de 3-4 questions avec branches conditionnelles, récapitulatif final éditable, puis écriture de l'état <projet>/.catalyst/production.yaml après validation explicite. Route vers les autorités existantes (CLAUDE.md global, playbook interne, da-moderne, seo-garantie-90, scroll-frames-3d, mission-template, popup-conversion, project-resume) sans jamais en dupliquer le contenu.
disable-model-invocation: true
argument-hint: "[nom du prospect ou du projet]"
---

# /website-production — orchestrateur d'onboarding Catalyst

Ce skill ne décide RIEN sur le fond (DA, SEO, popup, autonomie d'exécution) :
il pose les questions, enregistre les réponses dans un état local reproductible,
et **route vers les autorités existantes**. La conversation n'est jamais la
source de vérité — après `/clear`, `/project-resume` doit pouvoir tout
reconstruire depuis `<projet>/.catalyst/production.yaml`.

## Autorité et position

Hiérarchie (la plus haute gagne) : `~/.claude/CLAUDE.md` >
playbook interne > mémoires validées > skills
spécialisés (dont celui-ci) > projet. Ce skill est subordonné à tout ce qui
précède. Le CLAUDE.md global et le playbook sont des autorités internes, non
publiées : ils sont cités ici par leur nom et leurs numéros de section
uniquement. Il ne remplace ni la séquence de lancement du CLAUDE.md, ni les
checkpoints du playbook, ni `da-moderne` (la loi design), ni `seo-garantie-90`,
ni `scroll-frames-3d`, ni le cadre `mission-template`. Interdiction absolue de
recopier leur contenu ici ou dans l'état : on référence, on ne duplique pas.

## Déroulé

### 0. Résolution du contexte (lecture seule)
- Lancer `scripts/discover-project.sh "<terme>"` (voir [scripts/discover-project.sh](scripts/discover-project.sh)) avec le nom donné en argument.
- **Afficher les candidats trouvés. Jamais de sélection silencieuse** : si
  plusieurs candidats ou un doute, AskUserQuestion (chemin + date git + état).
- Si le mode est une **reprise** → basculer sur le skill `project-resume`
  (branche intégrée : il lit l'état existant et ne rejoue que les questions
  manquantes ou rouvertes).

### 1. QCM d'onboarding — AUCUNE ÉCRITURE pendant cette phase
Dérouler [references/onboarding.md](references/onboarding.md) : lots de 3-4
questions AskUserQuestion, branches conditionnelles (CRM, niche, break the
rules, capture de leads via le skill `popup-conversion`), les 19 points
obligatoires. Pendant tout le QCM : **zéro fichier, zéro dossier, zéro état**.

### 2. Récapitulatif final éditable
Afficher le récapitulatif COMPLET (toutes les réponses, chemin exact du projet
qui sera créé/modifié, liste exacte des fichiers qui seront écrits), puis
AskUserQuestion :
- **Valider et enregistrer l'état**
- **Modifier les réponses** (rejouer uniquement les lots concernés, ré-afficher le récap)
- **Annuler** (fin immédiate : ne laisser AUCUN fichier ni dossier)

### 3. Enregistrement (uniquement après « Valider et enregistrer l'état »)
- **Afficher le chemin exact avant l'écriture**, toujours.
- Créer le dossier projet minimal `<projets>/sites/site-<slug>/` et
  `.catalyst/production.yaml` conforme à [references/state-schema.md](references/state-schema.md).
- Valider immédiatement : `python3 scripts/validate-state.py <chemin>/.catalyst/production.yaml`
  (voir [scripts/validate-state.py](scripts/validate-state.py)) — un état
  invalide ne doit jamais être laissé sur disque.
- **Si le projet existe déjà** : ne modifier son état qu'après validation du
  récapitulatif ; ne jamais écraser un `production.yaml` existant sans avoir
  affiché le diff des changements.
- `DECISIONS.md` est conservé/créé selon le cadre `mission-template` ;
  `.catalyst/lessons-candidates.md` naît vide ou à la première leçon.

### 4. Cadre pré-GO (exception étroite du CLAUDE.md)
Avant le GO DA, **aucune production du site** : aucun code applicatif,
composant, asset final, build ou déploiement. Seuls les fichiers de pilotage
et de recherche nécessaires à la continuité sont autorisés après validation du
récapitulatif : dossier projet minimal, `.catalyst/production.yaml`, documents
de recherche, checkpoint DESIGN READ. **Cette exception ne constitue pas un GO
de production.** Ensuite : séquence de lancement du CLAUDE.md dans l'ordre
(playbook ; mémoires ; ligne du prospect dans le CRM de prospection, un Google
Sheet privé, source unique, jamais de CRM local ; vérifications de fraîcheur ;
recherches propres ; `da-moderne` ; `seo-garantie-90` ; `scroll-frames-3d` si
travelling) → **arrêt au checkpoint 1** (DESIGN READ + 2-3 directions de DA). Voir
[references/checkpoints.md](references/checkpoints.md).

### 5. Après le GO DA
- Autonomie « guidée » ou « checkpoints clés » : session interactive selon
  `da-moderne` et le playbook, checkpoints 2 (hero) et 3 (recette).
- Autonomie « autonome après GO DA » : router vers le skill `mission-template`
  avec un **périmètre fermé** dérivé de `production.yaml` (liste À FAIRE, NE
  BOUGE PAS, contraintes chiffrées). Ne pas casser ses `DECISIONS.md` ni ses
  gates. **Restent bloquantes même en autonomie** : sécurité, légalité, chemin
  ambigu, toute action externe (envoi de lead test, publication, email).
- Capture de leads prévue : invoquer le skill `popup-conversion` pour la
  spécification détaillée (le QCM n'enregistre que les choix de cadrage).
- Clôture : `/production-finish` (gates, RAPPORT.md, leçons candidates).
- Tenir `production.yaml` à jour à chaque checkpoint franchi (statut,
  checkpoint, validations, timestamps) — c'est ce qui rend `/clear` indolore.

## Mode break_the_rules

Pour les projets atypiques (ex. personnalité/sportif). Ce mode ne lève QUE les
defaults de niche/patterns qui brideraient la DA, **après avoir demandé
lesquels et pourquoi** (enregistrés dans `break_rules.rules_lifted` avec
raisons). Invariants NON négociables, conservés quoi qu'il arrive : faits
réels, sécurité, légalité, consentement, accessibilité, build/QA, budgets
performance, décisions tracées. Ce n'est jamais une permission vague de tout
ignorer. Détail : [references/onboarding.md](references/onboarding.md) §Break.

## Interdits permanents

- Aucun secret/token dans `production.yaml`, les rapports ou le dépôt
  (le validateur refuse les motifs de type clé/API/token).
- Aucun CRM local. Source unique : le CRM de prospection (Google Sheet privé),
  en lecture seule ; valeurs exactes à coller par Sam pour toute mise à jour.
- Aucune suppression de backup ou de fichier existant : signaler, ne pas nettoyer.
- Jamais de question ouverte quand 2-3 options concrètes avec recommandation
  sont possibles (préférence Sam documentée au playbook).

## Missions e-commerce et instructions en cours

Pour une boutique e-commerce, lire le skill `shopify-ecommerce-build` et le
skill `scroll-frames-3d`. Une instruction explicite et actuelle du client ou de
Sam prime sur les recettes par défaut d'un skill : les recettes historiques
(sous-échantillonnage mobile, préchargement au geste) ne la remplacent pas. Un
correctif autorisé ne nécessite pas de reprendre les questions déjà tranchées.
