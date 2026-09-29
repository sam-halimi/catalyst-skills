# Checklist QA de clôture — ordre imposé

Statuts : PASS / BLOCKED (bloquant, avec raison) / N/A (justifié) / OUVERT
(non bloquant → points ouverts du RAPPORT). Les seuils vivent dans le playbook
interne (non publié) et dans le cadre de mission `mission-template` : cette
checklist les exécute, elle ne les redéfinit pas.

## 1. Build — bloquant
- `npm run build` : zéro erreur, zéro warning bloquant.
- Favicon du projet présent (`app/icon.png` — jamais celui de create-next-app).

## 2. Console et hydratation — bloquant
- Chargement de chaque page : zéro erreur console, zéro warning d'hydratation
  (vérifier via le script de captures puppeteer ou une navigation puppeteer :
  les erreurs d'hydratation apparaissent au premier rendu).

## 3. Liens et routes — bloquant
- Tous les liens internes répondent (ancres comprises) ; pages légales
  accessibles depuis le footer ; liens externes réels (sameAs, Avis Google,
  annuaires) valides ; aucun `href="#"` résiduel ; `tel:`/`mailto:` corrects
  (téléphone au format +33 partout — exigence playbook).

## 4. Assets — bloquant si budget dépassé
- Budgets du cadre de mission (`mission-template`) : hero < 200 KB, images
  secondaires < 100 KB, séquence scroll < 3 MB.
- Formats modernes (AVIF/WebP), `next/image`, hero LCP en `priority`.
- `alt` réel sur toute image informative (vide sur décoratif pur).
- Aucun texte IA illisible incrusté dans les images générées (contrôle visuel).

## 5. Responsive — bloquant
- Captures aux 4 largeurs : **360, 390, 768, 1440** (script de captures
  multi-largeurs, desktop + mobile, multi-scroll). Mobile composé, pas empilé ;
  aucun débordement horizontal ; zones tactiles ≥ 44 px.

## 6. Accessibilité — bloquant (gate ≥ 95)
- Lighthouse a11y ≥ 95 ; contrastes AA (y compris footer, souvent oublié) ;
  headings réels hiérarchisés ; `label`/`aria` sur tous les champs ;
  `prefers-reduced-motion` respecté ; décoratifs géants en pseudo-éléments
  (sinon ils polluent l'arbre d'accessibilité) ; navigation clavier complète.

## 7. SEO / GEO / indexation — bloquant (gate SEO ≥ 95)
Recette par item : chaque ligne reçoit un statut explicite — PASS / N/A
(justification consignée au RAPPORT) / BLOCKED (raison). **Un item ● en
BLOCKED interdit la clôture** ; les items ○ sont contextuels (N/A justifié
quand ils ne s'appliquent pas). Le contenu détaillé de chaque item vit dans
`seo-garantie-90` (référence, jamais de copie) ; tout se vérifie sur le HTML
RENDU de l'alias public.
- ● Indexabilité conforme à l'état : `seo.indexation: gate_noindex` → noindex
  effectif ET Lighthouse SEO prouvé sur build local flag ouvert (un site en
  noindex ne peut pas prouver son score SEO en ligne) ;
  `ouverte` → indexable + IndexNow envoyé.
- ● Canonical de l'URL courante.
- ● robots.ts : wildcard + crawlers IA nominatifs.
- ● sitemap.xml complet (pages légales incluses, lastModified réels).
- ● Title + meta description comptés sur le HTML rendu, pour CHAQUE page.
- ● Exactement un h1 par page ; hiérarchie h2/h3 réelle.
- ● JSON-LD parsé (JSON.parse sur le HTML rendu) : @graph complet du skill —
  type métier + Organization, WebPage datée, Person E-E-A-T, Article déclaré
  à l'accueil.
- ● Signaux visibles : date « Mis à jour », liens sociaux / Avis Google réels,
  ol/ul hors accordéon. (Alt des images : déjà couvert au §4.)
- ● llms.txt + security headers + security.txt.
- ● Maillage interne : toute page atteignable par au moins un lien réel
  (footer/menu) — zéro page orpheline. (Validité des liens : déjà §3.)
- ● Article /conseils réel (byline, dates, sources, listes, liens internes) —
  N/A uniquement si le socle enregistré (`seo.socle`) ne le prévoit pas.
- ● Performance : statut repris du §8 (protocole VPS) — ne pas re-mesurer ici.
- ● Mobile : statut repris du §5 (responsive) ; Lighthouse mesuré en mobile.
- ○ Cohérence intention de recherche (`seo.objectif`) : `trafic` → chaque
  requête cible (`seo.requetes_cibles`) servie par une page cohérente — URL,
  title, H1 et contenu alignés ; `vitrine_locale` → les requêtes « métier +
  zone » servies par le title, le H1 et le contenu de la page (jamais une
  grappe de pages locales par défaut) ; `demo` → N/A « objectif démo ».
- ○ SEO local : NAP cohérent site/fiche Maps, geo + horaires réels au JSON-LD
  (N/A si activité sans ancrage local).
- ○ hreflang : mono-langue = fr-FR + x-default (socle) ; site réellement
  multilingue = hreflang complet et réciproque.
- ○ Breadcrumbs (visibles + BreadcrumbList) : uniquement si l'arborescence
  dépasse 2 niveaux — N/A sur mono-page et vitrine.

## 8. Performance — bloquant (gate ≥ 90 mobile)
- Protocole VPS existant, rien d'autre : alias prod public (jamais l'URL de
  déploiement suffixée du slug d'équipe, protégée par l'authentification, ni
  une preview sans cookie bypass), script d'audit Lighthouse mobile lancé sur
  cette URL,
  **best-of-5 si d'autres missions tournent** (vérifier `pgrep -af` + load),
  zombies chrome purgés avec motif crocheté. Retenir best + médiane.

## 9. Formulaires — bloquant
- Soumission valide → succès visible ; invalide → erreurs utiles ; validation
  serveur effective (tester une soumission forgée) ; honeypot/délai actifs ;
  jamais de `action="mailto:"`.

## 10. Popup — bloquant si présent
- Triggers conformes à la spec ; **frequency cap vérifié** (re-visite après
  fermeture) ; réouverture volontaire OK ; mobile : format bottom-sheet/bandeau,
  pas d'exit-intent, pas de plein écran pré-interaction ; clavier : ouverture,
  piège de focus, ESC, retour du focus ; `prefers-reduced-motion` ; zéro
  impact mesurable sur les gates perf (comparer avec/sans si doute).

## 11. Destination des leads — bloquant si capture
- Envoi de bout en bout avec **donnée de test autorisée uniquement** (ou
  confirmation demandée) ; lead arrivé à destination ; mapping des champs
  conforme ; leads « crm_sheet » (destinés au CRM) : valeurs exactes prêtes à
  coller remises à Sam ; aucun secret apparu dans le code/état/rapport au passage.

## 12. Tracking — bloquant si déclaré
- Les 5 événements (impression, engagement, submit, success, close) émettent ;
  variante A/B jointe si A/B actif ; rien ne part avant consentement quand
  `consentement_requis: true`.

## 13. Juridique et marque — bloquant
- Mentions légales + politique de confidentialité conformes au réel ;
  contraintes `production.yaml` (`contraintes.*`) toutes honorées ; cadre
  déontologique d'une profession réglementée le cas échéant (règles publiques
  de la profession : zéro avis, zéro nom de client, mention « spécialiste »
  encadrée, déclaration à l'ordre professionnel avant indexation) ;
  copie sans slop (grep des formules interdites, apostrophes typographiques,
  regex tolérantes `[’']`) ; le prospect ne voit jamais les coulisses.
