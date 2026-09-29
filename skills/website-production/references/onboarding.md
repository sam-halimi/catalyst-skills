# Onboarding /website-production — questionnaire canonique

Règles de conduite : AskUserQuestion par **lots de 3-4 questions maximum**,
labels courts + descriptions qui expliquent les conséquences, une
recommandation marquée quand elle existe. **Aucune écriture pendant le QCM.**
Chaque réponse alimente le champ `production.yaml` indiqué entre crochets
(schéma : [state-schema.md](state-schema.md)). Les branches sautent les lots
non pertinents ; en reprise, ne rejouer QUE les questions manquantes/rouvertes.

## Lot 1 — Cadre de mission

1. **Type de mission** [mode] : nouveau projet / reprise / mission spéciale.
   - *Reprise* → sortir du QCM, dérouler le skill `project-resume`.
   - *Mission spéciale* → préciser en texte libre la nature (stockée dans
     `mode_detail`), puis continuer le QCM normalement.
2. **Prospect au CRM ?** [crm.statut] : oui / non / cas spécial.
   - *Oui* → la ligne sera lue dans le CRM de prospection (Google Sheet privé,
     en lecture seule) pendant la séquence de lancement. [crm.ligne_ref]
   - *Non* → demander si une qualification est voulue d'abord (hors périmètre
     de ce skill : le signaler et enregistrer `crm.statut: absent`).
3. **Niche** [niche] : immobilier / avocat / commerce-hospitality / éditorial /
   personnalité-sport / autre.
   - *Avocat* → activer `contraintes.cadre_avocat: true` : le cadre
     réglementaire enregistré dans `da-moderne` et la leçon « site d'avocat » du
     playbook (§7) s'appliquent AVANT production — ne rien recopier ici, les
     relire à la séquence de lancement. Poser en plus : indexation ouverte ou
     gate noindex jusqu'à validation de l'Ordre ? [seo.indexation]
   - *Personnalité-sport* → proposer explicitement le mode break_the_rules (Lot 2).
4. **Autonomie** [autonomie] : guidée (validation à chaque étape) /
   checkpoints clés (1-2-3 du playbook) / autonome après GO DA
   (→ `mission-template`, périmètre fermé).

## Lot 2 — Cadre créatif

5. **Régime des règles** [break_rules.active] : standard Catalyst /
   break_the_rules (voir §Break en fin de fichier — questions supplémentaires).
6. **Direction artistique** [da.mode] : libre (2-3 directions proposées par
   `da-moderne`) / imposée (brief ou références de Sam → les collecter en
   texte libre dans `da.brief`) / hybride (contraintes partielles + marge).
7. **Hero** [hero.type] : 3D scroll-frames (UNIQUEMENT si le récit porte un
   travelling — règle `scroll-frames-3d`) / image animée (pattern
   « projection », défaut prospection du playbook) / statique / typographique /
   recommandation (l'agent proposera au checkpoint 1 selon le récit).
8. **Assets** [assets.source] : fournis par Sam / trouvés sur internet
   (photos réelles du lieu, protocole playbook §5) / générés IA
   (Higgsfield, étalonnés palette) / mixtes. Préciser dans `assets.notes`
   ce qui existe déjà.

## Lot 3 — Contenu et socle

9. **Sections** [sections.mode] : libres (squelette proposé au checkpoint 1) /
   imposées (liste fournie → `sections.liste`) / hybrides. Rappel non
   négociable : le BOTTOM verrouillé du playbook (§3 bis) s'applique en régime
   standard — Contact / FAQ / footer administratif.
10. **Contenu et recherche** [contenu.mode] : fourni / recherche complète
    (scraping, Maps, presse — faits réels only) / adaptation de l'existant /
    hybride.
11. **SEO** [seo.socle] : socle complet `seo-garantie-90` (défaut, dès la V1) /
    local renforcé / éditorial-GEO / noindex temporaire (gate
    `INDEXATION_OUVERTE`, cas réglementé type avocat) / exception (justifier →
    `seo.exception_raison` ; les engagements commerciaux du CLAUDE.md restent
    la référence).
11 bis. **Objectif de recherche** [seo.objectif] : démo (prospection — le SEO
    prouve la garantie, aucune ambition de ranking) / vitrine locale (défaut
    site client : le site doit répondre aux requêtes « métier + zone » — title,
    H1 et contenu de la page les servent, sans jamais multiplier des pages
    locales artificielles) / trafic (le client attend des visites organiques →
    collecter 3 à 5 requêtes cibles en texte libre [seo.requetes_cibles] ;
    l'architecture — pages services ou localisations dédiées, breadcrumbs si
    l'arborescence devient profonde — s'arbitre au checkpoint 1 au regard de
    ces requêtes, et la cohérence URL/title/H1/contenu se vérifie à la clôture,
    qa-checklist §7 de `/production-finish`).
12. **Capture de leads** [conversion.capture] : aucune / inline (formulaire en
    page) / popup / les deux.
    - *Aucune* → sauter le Lot 4 entier, `conversion` réduit à
      `capture: aucune`. C'est un choix valide (un site sans cookie ni
      formulaire est un argument, cf. socle SEO).

## Lot 4 — Conversion (seulement si capture ≠ aucune)

13. **Offre / lead magnet** [conversion.offre] : texte libre — qu'obtient le
    visiteur (estimation, guide, RDV, diagnostic…) et pourquoi c'est crédible
    pour cette niche.
14. **Type de popup** [conversion.popup.type] (si popup ou les-deux) :
    micro-engagement / quiz / visual quiz / scratch / mystery reward /
    gamification (seulement si cohérente avec la marque) / classique /
    recommandation (le skill `popup-conversion` tranchera, pertinence d'abord —
    il peut conclure qu'aucun popup n'est justifié).
15. **Triggers, fréquence, exclusions** [conversion.triggers] : délai / scroll % /
    exit-intent (desktop uniquement, JAMAIS par défaut mobile) / clic /
    nb de pages / comportement ; frequency cap et conditions de réouverture ;
    pages exclues (légales, conseils…). Défauts détaillés : skill
    `popup-conversion` (`references/triggers-consent.md`).
16. **Destination des leads** [conversion.destination] (multi-choix) : email /
    CRM Sheet (lecture seule — les valeurs sont données à Sam à coller, jamais
    d'écriture cellule ni de CRM local) / Brevo / Klaviyo / webhook / autre.
    Les identifiants/clés ne vont JAMAIS dans l'état : nom du service
    uniquement, secret côté Vercel env.

## Lot 5 — Conformité et verrouillage

17. **Consentement, tracking, A/B** [tracking] : bandeau/consentement requis ?
    (si tracking ou cookies non exemptés) ; événements à mesurer (impression,
    engagement, submit, success, close) ; A/B test oui/non + variantes.
    Défaut Catalyst : le minimum qui respecte la promesse « sans cookie » quand
    c'est possible.
18. **Contraintes juridiques et de marque** [contraintes] : cadre réglementé
    (avocat, santé, finance…), chartes/marques imposées, mentions
    obligatoires, interdits client. Pour un cadre inconnu : recherche AVANT
    production, résultat consigné en `docs/`.
19. **Validation de l'architecture de mission** : dernier écran AVANT le
    récapitulatif — confirmer périmètre, checkpoints applicables, autonomie,
    livrables (V1 + boucles de retours + RAPPORT.md). Puis passer au
    récapitulatif final (SKILL.md §2) : Valider et enregistrer l'état /
    Modifier les réponses / Annuler.

## §Break — questions du mode break_the_rules

Posées uniquement si `break_rules.active: true` (lot dédié, avant le Lot 5) :

- **Quelles règles sont levées ?** (multi-choix construit sur les defaults de
  la niche : patterns de composition §3 bis, bottom verrouillé, grammaire de
  palette 70/25/1, light-theme luxe, hero par défaut, ton de copie…) →
  `break_rules.rules_lifted`.
- **Pourquoi, pour chacune ?** → `break_rules.reasons` (une raison par règle ;
  refuser « parce que » — la raison doit tenir au récit ou à la marque).
- **Confirmation des invariants** : afficher la liste et faire valider qu'ils
  restent actifs — faits réels, sécurité, légalité, consentement,
  accessibilité, build/QA, budgets perf, décisions tracées →
  `break_rules.invariants_confirmes: true`. Sans cette confirmation, le mode
  n'est pas activé.

Ce mode s'enregistre dans l'état et se rappelle à chaque checkpoint : une
règle non listée dans `rules_lifted` reste en vigueur.

## Récapitulatif final — gabarit

Afficher, dans cet ordre : identité + chemin exact du projet ; mode/CRM/niche/
autonomie ; régime des règles (+ règles levées et raisons si break) ; DA/hero/
assets/sections/contenu ; SEO ; conversion complète (ou « aucune capture ») ;
tracking/consentement ; contraintes ; checkpoints applicables ; **liste exacte
des fichiers qui seront créés ou modifiés**. Puis la question de validation
unique. En cas d'« Annuler » : aucun fichier ni dossier ne doit exister.
