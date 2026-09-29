---
name: mission-template
description: "Format standard de toute mission autonome Catalyst (build, refonte, prompt de production, session sans humain). Use this skill whenever writing or starting an autonomous mission brief, a production prompt, launching or redesigning a site-* project, or running a hands-off session. Trigger on any mention of: mission autonome, prompt de production, lancement de site, refonte, session autonome, nouveau site-*, \"aucune question\", \"mission 2h\", or whenever a task must run to completion without asking the user. Impose the 7-part structure below and finish with a RAPPORT.md. IMPORTANT: le cadre autonome ne démarre qu'APRÈS le GO explicite de Sam sur la direction artistique (checkpoint 1 de la séquence de lancement du CLAUDE.md global), ou si son prompt demande expressément une exécution autonome après ce checkpoint. Avant le GO : séquence de lancement obligatoire, arrêt au checkpoint 1, aucun code applicatif, composant, asset final, build ou déploiement — seuls les fichiers de pilotage et de recherche (dossier projet minimal, .catalyst/production.yaml, docs, DESIGN READ) sont autorisés après validation de l'onboarding, selon l'exception étroite du CLAUDE.md global."
---

# Mission autonome Catalyst — format standard

## 0. Quand ce skill s'applique — le GO d'abord (préalable NON NÉGOCIABLE)

Ce skill cadre l'**exécution** d'une mission, pas son lancement. Toute nouvelle mission site commence par la **séquence de lancement obligatoire du `CLAUDE.md` global**, dans cet ordre : playbook interne (à lire en entier), notes internes obligatoires (historique des démos, CRM, déploiement, protocole de mesure Lighthouse), ligne du prospect dans le CRM de prospection (Google Sheet privé), vérifications de fraîcheur, recherches propres, puis skills applicables (`da-moderne`, `seo-garantie-90`, `scroll-frames-3d` si travelling).

- **Le checkpoint 1 reste obligatoire** : présenter à Sam le DESIGN READ + 2-3 directions de DA avec recommandation, puis **attendre son arbitrage**.
- La règle « mission autonome, aucune question » ne s'applique qu'**APRÈS le `GO` explicite de Sam sur la direction artistique**, ou si son prompt demande expressément une exécution autonome après ce checkpoint.
- **Avant le `GO` : aucune production du site — aucun code applicatif, composant, asset final, build ou déploiement.** Seuls les fichiers de pilotage et de recherche nécessaires à la continuité sont autorisés après validation du récapitulatif d'onboarding (`/website-production`) : dossier projet minimal, `.catalyst/production.yaml`, documents de recherche et checkpoint DESIGN READ — exception étroite du CLAUDE.md global, qui ne constitue pas un GO de production. Après le `GO` : exécution autonome possible selon ce skill.

**Hiérarchie en cas de conflit entre sources** (la plus haute gagne) :
1. les instructions globales (`~/.claude/CLAUDE.md`)
2. le playbook interne
3. les mémoires Catalyst à jour
4. les skills spécialisés (dont celui-ci)
5. les instructions propres au projet

---

Une fois le GO obtenu, toute mission autonome (création de site, refonte, prompt de production) suit **cette structure exacte, dans cet ordre**. On copie le squelette, on le remplit, on exécute de haut en bas. La règle cardinale — valable seulement après le GO : **aucune question posée**. Toute ambiguïté est tranchée selon les skills et **loggée dans `DECISIONS.md`**.

Ce skill fige le *cadre* d'exécution. Les décisions de *design* viennent du skill `da-moderne` (la loi, cf. CLAUDE.md global — d'éventuels cadres segment le complètent sans le supplanter) ; les conventions de *code/perf* viennent du CLAUDE.md global et, s'il existe, du `CLAUDE.md` du projet. Ce template les orchestre.

---

## Le squelette (à copier au démarrage de CHAQUE mission)

### 1. EN-TÊTE
> **Mission autonome — aucune question.** Décisions ambiguës tranchées selon les
> skills applicables et **loggées dans `DECISIONS.md`** (un fichier par mission,
> à la racine du projet). Aucune interruption pour validation humaine.

### 2. PRÉREQUIS (à lire INTÉGRALEMENT avant de toucher au code)
> Normalement déjà couverts par la séquence de lancement (§0) — vérifier que rien ne manque, ne pas re-dérouler ce qui a déjà été fait dans la session.
- [ ] Le playbook interne en entier (processus 6 phases, gates, registre rotation, leçons).
- [ ] Notes internes obligatoires : historique des démos, CRM, déploiement, protocole de mesure Lighthouse (+ les autres selon besoin).
- [ ] Skill `da-moderne` (la loi design) — et le cadre segment enregistré dedans s'il existe (ex. une profession réglementée).
- [ ] `CLAUDE.md` du projet s'il existe (sinon en créer un minimal qui pointe `da-moderne` comme source de vérité design).
- [ ] **Ligne du prospect** dans le CRM de prospection (Google Sheet privé, identifiant tenu hors dépôt) : nom exact, titre/spécialité, ville, coordonnées, brief, statut, notes déjà relevées. **Source UNIQUE. Aucun CRM local ne doit être utilisé ni recréé** : jamais de fiche locale, de copie CSV ou de duplicata.

### 3. POINT DE RESTAURATION
- [ ] `git init` si nécessaire, puis **`git commit` de l'état initial AVANT tout travail** (point de retour propre).
- [ ] Commits atomiques ensuite (1 changement logique = 1 commit, messages FR, conventional commits).

### 4. PÉRIMÈTRE (explicite et fermé)
**NE BOUGE PAS** (hors périmètre — laisser strictement intact) :
- _(lister : copywriting, structure, JSON-LD, optimisations perf existantes, contenu légal…)_

**À FAIRE** (liste numérotée et **fermée** — rien en dehors) :
1. …
2. …
3. …

> Si une idée surgit hors de cette liste : la noter dans `DECISIONS.md` (« hors périmètre, non fait »), ne pas la faire.

### 5. CONTRAINTES CHIFFRÉES
- **Budgets images** : hero < 200 KB (hors séquence) · images secondaires < 100 KB · séquence scroll < 3 MB total. Dimensions : hero ≤ 1920px, sections ≤ 1200px, macros ≤ 1600px. Format WebP/AVIF, `q≈78`.
- **Seuils Lighthouse** : les **4 catégories ≥ 90** (performance, accessibilité, best-practices, SEO), mobile, en prod.
- **Breakpoints** : mobile 360–767 (tester en priorité, cible iPhone), tablette 768–1023, desktop ≥ 1024. Mobile-first absolu.
- _(ajouter les seuils spécifiques à la mission : nb de frames, poids bundle, etc.)_

### 6. GATE DE SORTIE (dans l'ordre, aucune étape sautée)
1. **Build** : `npm run build` — zéro erreur, zéro warning bloquant.
2. **Deploy** : mise en ligne Vercel (prod).
3. **Audit** : audit Lighthouse mobile des 4 catégories sur l'URL de production (script d'audit interne, non publié) → relève les 4 scores.
4. **Boucle corrective** : si une catégorie < 90 → corriger la cause, redéployer, re-auditer. **Maximum 3 passes.** Au-delà, consigner le blocage dans `RAPPORT.md` (points ouverts) et **s'arrêter** — ne jamais boucler indéfiniment.

### 7. LIVRABLE
- [ ] **`RAPPORT.md`** à la racine du projet, contenant :
  - **Ce qui a été fait** (aligné sur la liste « À FAIRE » du §4).
  - **Scores Lighthouse finaux** (tableau, URL, date, nb de passes correctives).
  - **Décisions clés** (renvoi à `DECISIONS.md` pour le détail des arbitrages).
  - **Points restés ouverts** (hors périmètre, images à régénérer, données « à compléter »).
- [ ] `DECISIONS.md` à jour (journal des arbitrages autonomes).

---

## Exemple rempli : refonte visuelle du site du joaillier (démo de prospection, 2026)

> Exemple HISTORIQUE, antérieur au cadre actuel : il s'appuyait sur un skill de DA sectoriel, remplacé depuis par `da-moderne`, et sur le builder interne de l'époque. Aujourd'hui : `da-moderne` = la loi design, CRM = le CRM de prospection (§2), et le GO de Sam sur la DA précède toute exécution (§0). La structure en 7 parties, elle, reste la référence.

### 1. EN-TÊTE
Mission autonome, aucune question. Arbitrages tranchés selon le skill de DA sectoriel (source de vérité design unique à l'époque) et loggés dans `DECISIONS.md`.

### 2. PRÉREQUIS lus
- Le skill de DA sectoriel (SKILL + références + prompts d'images), durci en cours de mission (ajout d'un bloc « Interdits absolus »).
- Le `CLAUDE.md` du builder interne (conventions perf/code).
- Aucun `CLAUDE.md` projet au départ → création d'un `CLAUDE.md` minimal désignant le skill de DA comme source de vérité.
- Ligne CRM : joaillier indépendant, statut et notes lus dans le CRM de prospection (§2).

### 3. POINT DE RESTAURATION
`git commit` de l'état initial avant refonte ; commits atomiques par section refaite.

### 4. PÉRIMÈTRE
**NE BOUGE PAS** : copywriting, structure et ordre des sections, JSON-LD, optimisations perf (décodage différé du hero-scrub, variante mobile 36 frames, server components, images WebP). → *présentation uniquement*.
**À FAIRE** :
1. Dé-cardage global (0 border-radius, 0 ombre, 0 conteneur clair sur ivoire).
2. Nav : réécriture complète du style de l'ancien `tubelight-navbar` (21st.dev) en ligne fine.
3. Hero full-bleed sorti de sa carte, signature de la maison visible d'emblée.
4. Les cinq sections de la page en composition asymétrique à filets.
5. Typo & rythme selon le skill de DA (clamp 56–88px, body 17/1.7, eyebrows 0.18em, padding 120–160px).
6. Vérif mobile par captures.

### 5. CONTRAINTES CHIFFRÉES appliquées
Budgets images du builder (hero < 200 KB, séquence < 3 MB, 36 frames mobile) préservés ; Lighthouse cible 4×≥90 ; breakpoints mobile-first (hero 100svh testé iPhone).

### 6. GATE DE SORTIE
Build OK → deploy sur `https://<projet>.vercel.app` → audit Lighthouse mobile. **Performance 95 dès la 1ʳᵉ passe → 0 boucle corrective nécessaire.**

### 7. LIVRABLE
`RAPPORT.md` produit (scores + fait + traitement fond blanc→ivoire provisoire + images à régénérer + points ouverts) ; `DECISIONS.md` complet (fond blanc vs ivoire, `mix-blend-multiply` & contextes d'empilement, watermarks, tokens neutralisés).

**Scores finaux :**

| Catégorie | Score |
|---|---|
| Performance | 95 |
| Accessibilité | 100 |
| Best-practices | 96 |
| SEO | 100 |

**Points restés ouverts** (hors périmètre) : données pratiques « à compléter », séquence hero à régénérer sur fond ivoire, portrait réel à produire.

---

## Rappels de discipline

- **Le GO d'abord** : ce cadre ne s'active qu'après le `GO` explicite de Sam sur la DA (checkpoint 1) ou une demande expresse d'exécution autonome après ce checkpoint. Avant : séquence de lancement, arrêt au checkpoint 1, zéro code applicatif, zéro asset final, zéro build, zéro deploy — seuls pilotage, recherches et DESIGN READ après validation de l'onboarding (§0).
- **Aucune question** — après le GO uniquement : c'est la nature de la mission. Trancher + logger, jamais bloquer.
- **La liste « À FAIRE » est fermée.** Le scope creep se note dans `DECISIONS.md`, il ne s'exécute pas.
- **Le gate n'est pas optionnel** : pas de mission « terminée » sans build vert + deploy + audit ≥ 90 (ou blocage documenté après 3 passes).
- **Deux livrables toujours** : `DECISIONS.md` (le pourquoi) et `RAPPORT.md` (le quoi + les chiffres).
