---
name: seo-garantie-90
description: Playbook Catalyst pour atteindre la garantie SEO dès la V1 de tout site livré, soit Lighthouse SEO 100, Performance mobile ≥ 90 et audit tiers (seaudit.fr) ≥ 90. Utilise ce skill à la création de tout nouveau site client ou démo, avant tout audit SEO, quand un score d'audit stagne, ou quand il faut expliquer la garantie SEO de l'agence. Contient la checklist de build V1, les erreurs coûteuses documentées avec leur coût mesuré (projet de référence d'un joaillier, 83 → 93), le protocole d'audit par URL fraîche et la méthode de rétro-analyse d'un outil d'audit (la grille détaillée reste privée).
---

# SEO Garantie 90 : playbook Catalyst

Issu du projet de référence, le site d'un joaillier (2026-08) : audit
seaudit.fr passé de 83 à **93/100** (Confiance 100, Contenu 100, Performance
92, Technique 91, GEO 87) en 4 itérations documentées. Objectif de ce skill :
que le **prochain site atteigne ce score dès la V1**, sans itérations.

## La cible mesurable

Trois gates, dans cet ordre :
1. **Lighthouse SEO = 100, A11y ≥ 95, Perf mobile ≥ 90** (best-of-3 : un
   Lighthouse local sur un serveur partagé ne mesure pas le TBT de façon
   fiable, voir les notes internes).
2. **Audit seaudit.fr ≥ 90**, l'outil de référence de Sam (méthode ci-dessous).
3. Zéro régression DA : chaque signal ajouté doit être invisible ou validé.

## Grille de l'outil d'audit (rétro-analysée, vérifiée 2026-08, non publiée)

La grille de notation de l'outil a été reconstruite à partir de sa méthodologie
publique (pages méthodologie et FAQ de l'outil) et d'audits mesurés, puis
vérifiée par recalcul exact des scores obtenus sur le site du joaillier. Elle
couvre cinq axes (Technique, GEO/IA, Contenu, Performance, Confiance) et elle
est **100 % on-page**. Les pondérations par axe et par item restent privées :
elles ne figurent pas dans cette copie publique. La checklist ci-dessous en est
la traduction opérationnelle, et la méthode pour reconstruire la grille d'un
autre outil est décrite en fin de document.

Trois faits de fonctionnement à connaître, sans lesquels le reste se lit mal :
- L'axe Performance vient de Lighthouse mobile via l'API PSI. **Si l'API PSI
  est en quota (429 fréquent), l'axe affiche « — » et la moyenne se rééquilibre
  sur les 4 autres** — ce n'est PAS un problème du site, re-auditer plus tard.
- Le schema Article est un critère conditionnel (articles de blog) : le crédit
  plein semble réservé au cas où l'URL auditée EST l'article, d'où un plafond
  GEO d'environ 85-87 sur une page d'accueil (87 observé chez le joaillier).
- Le hreflang reçoit un crédit partiel, même sur un site mono-langue.

Critères des axes GEO/IA et Confiance, tels que la méthodologie publique de
l'outil les énonce (sans leurs poids) : JSON-LD présent, entité Organization,
FAQPage avec `acceptedAnswer`, format question/réponse, listes structurées
visibles (ul/ol), llms.txt à la racine, schema Article, E-E-A-T (auteur et
date) ; auteur déclaré avec `sameAs` vers ses profils, date de publication ou
de modification visible ET en schema, Organization complète (logo, sameAs,
founder), Open Graph (og:title et og:image).

Critères de contenu et de technique que la grille vérifie, à tenir comme des
règles de build : title 30-70 caractères, meta description 70-170 (charte
Catalyst : 120-160), **exactement un h1**, au moins 2 h2, au moins 300 mots
(hors pages légales), attribut alt sur au moins 50 % des images, HTTPS,
viewport, canonical, robots.txt, sitemap.xml bien formé.

Ce que seaudit ne mesure PAS : backlinks, visibilité LLM live, trafic réel.
Donc **pas de plafond vercel.app sur cet outil** — le 100 en Confiance est
atteignable dès la démo. (Les outils qui notent l'âge du domaine et les avis
existent aussi : ne jamais garantir un composite sans connaître l'outil.)

## Checklist de build V1 — tout faire d'entrée

### Architecture (à poser AVANT la première ligne)
- **`app/site.ts` : `export const SITE_URL = "..."` — TOUTES les URLs absolues
  en dérivent** (metadata, JSON-LD, sitemap, robots, llms.txt). Aucune URL en
  dur ailleurs. C'est ce qui rend le protocole d'audit par URL fraîche trivial.
- `llms.txt` en route handler (`app/llms.txt/route.ts`, `dynamic =
  "force-static"`, template literal avec `${SITE_URL}`), PAS en fichier public.

### Metadata (layout + chaque page)
- Title 30-70 chars, **sans tiret cadratin** (utiliser « · »). Compter avec
  `wc -m`, pas estimer. Description 120-160, à **compter sur le HTML RENDU**
  (curl + len(), les entités et apostrophes typographiques changent le compte :
  l'agence immobilière B affichait 167 → Contenu 82 ; retaillée 144 → 92).
- `alternates`: canonical + `languages: { "fr-FR": path, "x-default": path }`
  (rendu `hrefLang` en casse React : valide, ne pas « corriger »).
- `authors: [{ name: "Prénom Nom" }]` (nom complet réel), `creator`, OG + Twitter
  card avec image.

### JSON-LD — un seul bloc `@graph` dans le layout
Entités liées par `@id` (`#organisation`, `#site`, `#page`, `#offres`) :
1. **[TypeMétier, "Organization"]** : NAP complet, `geo` (GeoCoordinates
   vérifiées via Nominatim), `openingHoursSpecification` (horaires RÉELS
   fournis, sinon omettre), `sameAs` = TOUS les profils réels (réseaux +
   annuaires : les annuaires généralistes type Pages Jaunes ou Mappy et les
   annuaires spécialisés du métier sont légitimes), `founder` Person avec `url` (mentions légales) +
   `sameAs` LinkedIn, `logo`, `foundingDate`, `knowsAbout`, `priceRange`.
2. **WebSite** : `publisher → @id org`, `inLanguage`.
3. **WebPage** : `datePublished`, **`dateModified`**, `author → @id org`,
   `isPartOf`, `about`, `speakable` (cssSelector vers FAQ et address).
4. **ItemList** des produits/prestations avec `url` vers de vraies ancres
   `id=` sur les sections.
5. **FAQPage** dans la page (mainEntity mappé sur le tableau FAQ du code).

NO-GO validés (bruit ou warnings Search Console) : `contactPoint`,
`areaServed`, `currenciesAccepted`/`paymentAccepted`, **Product avec Offer
sans prix**, aggregateRating auto-proclamé.

### Signaux VISIBLES (leçon n°1 du projet de référence : le JSON-LD seul ne suffit pas)
- **Footer** : © année, liens sociaux réels cliquables (Instagram, Facebook,
  LinkedIn), **lien « Avis Google »** vers la fiche réelle, liens pages
  légales, **« Mis à jour : mois année »** en opacité réduite.
- **Date de publication/modification visible** quelque part (footer + pages
  légales « Dernière mise à jour »). C'est l'item qui a fait passer le site du
  joaillier de 80 à 100 en Confiance.
- FAQ visible (6-8 questions, `<details>` sobre) placée après le CTA, **avec au
  moins une liste `<ol>`/`<ul>` dans une réponse**.
- Téléphone en `tel:`, email en `mailto:`, horaires en texte.
- Hiérarchie réelle : 1 h1, h2 par section (labels de section en h2/h3 : le
  preflight Tailwind fait hériter taille et graisse → zéro impact visuel).

### La page Article (débloque le dernier item GEO)
Une page `/conseils` (gabarit des pages légales, zéro DA nouvelle) : un
article de ~800 mots sur LA question client type du métier (par exemple
« Comment conserver une bouteille ouverte » pour un caviste). Byline visible
« Par Prénom Nom », date visible, schema **Article** (author Person +
publisher → @id org, dates, image), listes ul + ol, liens internes (ancres des
produits, CTA rendez-vous), **sources externes citées** (organismes de
certification du métier). Lien « Conseils » au footer, entrée sitemap, section
dans llms.txt. Copywriting charte : sobre, zéro cadratin, zéro chiffre ou
engagement inventé (« sur devis », « plusieurs semaines »).

**CRUCIAL (l'agence immobilière A, 2026-08, GEO 76 malgré la page)** : seaudit
n'audite que l'URL SOUMISE. L'Article doit AUSSI être déclaré dans le `@graph`
de l'accueil (entité Article avec url vers /conseils, author/publisher → @id
org, dates, + `hasPart` sur la WebPage). Sans ça, l'item Article reste
non coché. Si aucun nom de personne réel n'est connu, author = Organization
(ne JAMAIS inventer un nom).

### Format Q/R et listes : sur la page auditée, en vrais éléments
(l'agence immobilière A, 2026-08 : trois items GEO perdus alors que « tout
existait »)
- Les questions d'une FAQ en `<summary>` ne comptent PAS comme format Q/R :
  mettre un **vrai `<h3>` À L'INTÉRIEUR du summary** (HTML valide, styles
  identiques, zéro impact visuel) — les questions deviennent des sections.
- Toute grille numérotée (méthode I/II/III, étapes) doit être une **vraie
  `<ol>`** ; au moins un `<ul>` visible en plus (une réponse de FAQ avec
  liste fait l'affaire). Un seul conteneur stylé en grid sur `<ol>`/`<li>`
  rend exactement pareil.
- **Des listes uniquement DANS des `<details>` repliés semblent sous-comptées**
  (l'agence immobilière B : GEO 70 avec ol+ul en FAQ seulement, +4 après
  sémantisation hors accordéon). Réflexe : toute grille de cartes/offres déjà
  visible = `<ul>`/`<li>` avec `list-none p-0` (rendu identique), idem rangées
  de liens du footer. Si une section liste disparaît sur retour DA, recaser
  les listes ailleurs LE JOUR MÊME : c'est un des items les plus lourds de
  l'axe GEO.
- **E-E-A-T veut une Person, pas seulement l'Organization** (l'agence
  immobilière B : +4 GEO). Quand aucun humain n'est connu chez le client, il y
  en a souvent un de FACTUEL : le président de la société, et si le président
  est une personne morale, le représentant légal de celle-ci, tel qu'il figure
  au registre du commerce (consultable sur Pappers). C'est légalement le directeur de la publication →
  mentions légales (« Directeur de la publication : X, pour Y, président »),
  entité Person dans le @graph (jobTitle, url mentions légales, worksFor →
  org), author de WebPage et Article pointés dessus, byline /conseils, authors
  des metadata, ligne llms.txt. Zéro invention : tout est au RCS.

### Technique
- `next.config.ts` : `images: { formats: ["image/avif", "image/webp"],
  minimumCacheTTL: 2678400 }` + `headers()` avec X-Content-Type-Options,
  Referrer-Policy, Permissions-Policy, X-Frame-Options, **CSP avec
  `'unsafe-inline'`** (obligatoire pour JSON-LD + hydratation ; `'unsafe-eval'`
  UNIQUEMENT en dev via `NODE_ENV`). **Ne pas dupliquer HSTS** (Vercel l'envoie).
  Une CSP imparfaite score toujours mieux qu'aucune CSP.
- `app/robots.ts` : règles **nominatives** par crawler IA (GPTBot,
  ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-User, Claude-SearchBot,
  PerplexityBot, Perplexity-User, Google-Extended, Bingbot, Applebot-Extended,
  CCBot) + wildcard — les auditeurs GEO vérifient les règles explicites.
- `public/.well-known/security.txt` (Contact, Expires, Preferred-Languages).
- Sitemap : toutes les pages, pages légales incluses, lastModified réels.
- Polices : **greper chaque variable `--font-*` avant de livrer**. Le site du
  joaillier embarquait 6 familles dont 4 jamais utilisées (perf gratuite).
- IndexNow : clé hex 32 dans `public/<clé>.txt` + script `npm run indexnow`
  (un script Node du projet, `scripts/indexnow.mjs`, qui soumet les URLs du
  sitemap). L'index Bing alimente Copilot ET ChatGPT Search. Bing Webmaster
  Tools + Bing Places restent manuels (compte Microsoft).

## Validation n°2 : le cabinet de syndic (2026-08, socle V1 sans rattrapage)

**seaudit 95/100 AU PREMIER AUDIT** (Confiance 100, Contenu 100, Perf 95,
Technique 93, GEO 91), record Catalyst (le joaillier 93 en 4 itérations,
l'agence immobilière A 89), zéro version corrective. Lighthouse
95-98/100/100/100. La preuve définitive que le socle appliqué À LA CRÉATION
coûte une heure et rend la garantie ≥ 90 automatique. Confirmations et ajouts :
- **Re-fetcher la méthodologie de l'outil avant chaque audit** (30 s,
  WebFetch) : grille inchangée confirmée 2026-08, rééquilibrage PSI compris.
- La **vérification finale se fait sur le HTML RENDU** (curl + node, ~10 lignes) :
  title/desc comptés, hreflang, ratio alt, h1/h2/h3, ol/ul, details, ~mots,
  date visible, canonical — tout vert AVANT de donner l'URL à auditer.
- `openingHoursSpecification` : seulement si les horaires sont AFFICHÉS sur le
  site, et en **2 plages** s'il y a une pause déjeuner (par exemple 9-12 +
  14-18), jamais une plage continue mensongère.
- Enrichissements sans risque : `description` sur WebSite ET WebPage,
  `primaryImageOfPage`, `memberOf` (syndicat professionnel réel du métier).
- Pour un métier doté d'un registre public (pour un syndic, le registre
  national des copropriétés) : ce registre fournit des chiffres sourcés,
  matière chiffrée idéale (stats visibles, llms.txt, copie).
- Rappel payé 2× : le logotype décoratif géant du footer en **pseudo-élément
  CSS** (axe teste le contraste des textes aria-hidden).

## Validation n°3 : le caviste (2026-08, 95/100 au 1er audit)

Socle V1 complet appliqué à la création (LiquorStore+Organization, Person
directeur de la publication, Article déclaré à l'accueil, h3-in-summary,
ol/ul hors accordéon posés dès la V1 après vérif HTML rendu) → **95/100 dès
le premier audit**, égal au record du cabinet de syndic, zéro version
corrective. Confirme que la checklist V1 + la vérification sur HTML rendu
AVANT de donner l'URL rendent le ≥ 90 systématique. Trois validations (le
cabinet de syndic 95, l'agence immobilière B 90 en 3 itérations quand des
items manquaient en V1, le caviste 95 direct) : la différence entre
« 95 direct » et « des itérations » est UNIQUEMENT le respect intégral de la
checklist à la création.

## Protocole d'audit (seaudit ne re-note pas une URL déjà vue)

Chaque audit exige une URL fraîche : v2, v3, v4…
1. Changer `SITE_URL` dans `app/site.ts` (une ligne).
2. `npm run build && npx vercel deploy --prod --yes --scope <equipe>`.
3. `npx vercel domains add <projet-vN>.vercel.app --scope <equipe>`, et
   **PAS `alias set`** (l'alias répond en 302 quand la protection des
   déploiements de l'équipe est active ; seul `domains add` rend l'URL
   publique).
4. `npm run indexnow`.
5. Vérifier : `curl` 200 + canonical vN + headers présents, avant de donner
   l'URL à auditer.

## Vérifications avant livraison (toutes obligatoires)

1. `npm run build` sans erreur, puis `next start` local.
2. Node : parser les blocs JSON-LD du HTML rendu (JSON.parse = validation),
   vérifier @graph, dates, sameAs, compteur de `<details>`, longueur description.
3. **Puppeteer sur Chrome réel** : hydratation OK, canvas/animations OK,
   **zéro violation CSP en console** (seul vrai risque de casse).
4. Lighthouse local SEO/A11y/BP (fiables) + Perf best-of-3 (indicatif) ;
   PSI prod pour le chiffre officiel (quota : réessayer plus tard, pas insister).
5. Captures avant/après des zones touchées (footer, FAQ) — zéro dérive DA.

## Erreurs documentées (ne pas les repayer)

1. **Signaux uniquement en JSON-LD** → Confiance/GEO immobiles pendant 2
   versions. Les auditeurs veulent des signaux VISIBLES (liens sociaux, date).
2. **Aucune date nulle part** → item E-E-A-T pénalisé, Confiance plafonnée
   à 80. Une ligne de footer + 2 propriétés schema = +20 points.
3. **Tiret cadratin dans le title** — violation charte passée inaperçue.
4. **`vercel alias set` au lieu de `domains add`** → URL d'audit en 302.
5. **Chercher le point de Perf perdu dans son code** alors que c'est l'API PSI
   de l'auditeur qui est en quota (axe « — », moyenne rééquilibrée). Refaire
   le calcul pondéré avant de déboguer quoi que ce soit. Vérification sur
   l'agence immobilière B : « Performance — » et 90 affiché, alors que la
   moyenne pondérée des 4 axes restants (100, 74, 92, 100) donne 89,9. Le
   recalcul qui tombe juste PROUVE le quota ; re-auditer plus tard sur une URL
   fraîche vN+1.
6. **Chiffres/URLs/horaires inventés** : jamais. Les subagents SEO en proposent
   (« à partir de X € », « suivi à vie ») : refuser, formuler « sur devis ».
7. **Compter sur les sous-pages pour les items GEO** (l'agence immobilière A,
   GEO 76) : l'outil n'audite que l'URL soumise. Article déclaré à l'accueil
   (@graph + hasPart), questions FAQ en h3 dans les summary, vraies ol/ul, DÈS
   LA V1.
8. **Aucun réseau social réel** : ne pas en inventer. Les annuaires
   professionnels vérifiés du métier et les annuaires d'entreprises
   (societe.com, Pages Jaunes) sont des
   `sameAs` et liens footer légitimes qui remplissent le même rôle (Confiance
   100 obtenue ainsi sur l'agence immobilière A).
9. **Casser un item SEO par un retour design sans le recaser** (l'agence
   immobilière B : la suppression d'une section de contenu a emporté les
   seules ol/ul visibles → GEO 66). Après CHAQUE boucle de retours design,
   re-vérifier sur le HTML rendu : compte ul/ol, description, h1/h2/h3, mots.
   30 secondes de curl évitent une itération d'audit entière.

## Si un score stagne malgré tout

Méthode qui a débloqué le projet de référence : **rétro-analyser l'outil, pas
le site.**
1. Demander l'URL exacte de l'outil d'audit à Sam.
2. WebFetch sa méthodologie/FAQ ; reconstruire la grille et les pondérations.
3. Vérifier la grille par recalcul exact du score obtenu.
4. Croiser item par item avec le HTML rendu (curl, pas le code source).
5. Corriger uniquement les items non cochés ; re-auditer sur URL fraîche.
