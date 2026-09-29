# Historique seulement — prescriptions remplacées par le guide actuel

Description d'origine de cette version : technique Catalyst validée sur deux projets clients (le joaillier en 2026-07, l'agence immobilière A en 2026-08) pour une séquence 3D pilotée au scroll, soit une vidéo générée découpée en frames WebP et un canvas scrub. À utiliser UNIQUEMENT quand le récit du site porte un travelling (traversée d'un lieu, orbite produit), jamais pour décorer. Contient la chaîne complète keyframes → vidéo → frames → composant, les budgets perf et toutes les erreurs déjà payées. Les coûts en crédits du fournisseur vidéo ont été retirés de cette copie publique.

# Scroll-frames 3D — séquence vidéo pilotée au scroll

**Quand l'utiliser** : le concept du site EST un déplacement (entrer dans un
lieu, s'approcher d'un objet, survoler un territoire). Un seul moment
spectaculaire par site (règle da-moderne) — si le scrub est ce moment, rien
d'autre ne doit briller. Ne jamais l'imposer : c'est du cas par cas, le mode
et le concept passent d'abord.

## Chaîne de production (ordre strict)

### 1. Keyframes (nano_banana_pro, 16:9)
- 2 keyframes suffisent (départ + arrivée) si la vidéo est UN SEUL plan ;
  n'ajouter des intermédiaires que pour un trajet impossible en un plan.
- Bloc de style commun dans chaque prompt (heure, lumière, palette hex du
  site) = étalonnage gratuit, et les keyframes se recyclent en images de
  sections.
- **PIÈGE PAYÉ : ne jamais écrire « drone view/hovering » — le modèle DESSINE
  le drone dans l'image.** Écrire « aerial POV » + « strictly no visible
  drone, no aircraft, no people, no text ».
- **Géométrie simple pour la caméra (l'agence immobilière B, 2026-08)** : un escalier
  DROIT se remonte proprement, un colimaçon produit des raccords louches et
  des traversées de mur. Pour franchir une porte : la keyframe de départ doit
  MONTRER la porte (fermée) et le prompt vidéo exiger « the door swings open
  BEFORE the camera passes, the camera only ever passes through the open
  doorway, never through walls ».
- **Tout détail incrusté dans une keyframe se retrouve dans TOUTES les
  frames** (serrure, logo, objet daté…). Inspecter chaque keyframe comme un
  décor de cinéma. Correction : édition image-to-image nano banana (medias
  role "image" + « Change strictly nothing else in the image ») puis
  re-génération du plan — jamais de retouche frame par frame.
- **Checkpoint Sam sur les keyframes AVANT toute vidéo** (protège les crédits).

### 1 bis. Choix du sujet — le rendu IA se voit dans le PRÉCIS (l'agence immobilière C, 2026-08)
- **Retour Sam payé : « la vidéo fait trop IA, il ne faut pas choisir une vidéo
  trop précise. »** Les artefacts génératifs vivent dans la géométrie proche et
  détaillée (façades au ras de la caméra, menuiseries, enseignes, intérieurs
  meublés) ; les PLANS LARGES les masquent (ciel, fleuve, mer de toits, paysage).
  Composer le trajet pour ne JAMAIS approcher la caméra d'une surface détaillée ;
  si le récit exige un objet précis (devanture, produit), le donner en photo
  RÉELLE dans une section, pas dans le scrub.
- **Ascension validée** (l'inverse des descentes habituelles) : départ au ras de
  l'eau (POV bateau sur un fleuve) → montée continue PAR-DESSUS le pont
  (« climbing OVER the bridge well before reaching it, never passing under or
  through anything ») → grande aérienne. Une keyframe déjà validée d'une version
  précédente se recycle en end_image (aucune nouvelle génération, étalonnage garanti).

- **Le scrub généré peut être retoqué même en plans larges (l'agence immobilière C,
  boucle 2)** : après une descente « trop précise » PUIS une ascension 100 %
  plans larges, Sam a tranché « le hero fait encore très IA, pas de Higgsfield
  pour le hero » → bascule hero photo RÉELLE (Unsplash, pattern projection).
  Avant d'engager la chaîne vidéo sur une démo, considérer qu'une vraie photo
  aérienne de qualité bat souvent le généré au premier regard ; le scroll-frames
  se réserve aux récits qu'une photo ne peut pas raconter (traversée d'un lieu
  précis du client, orbite produit).

### 2. Vidéo (Kling 3.0 de préférence)
- **Un seul plan continu bat des clips raccordés** : `kling3_0`, 15 s, mode
  pro, `sound: "off"`, `start_image` + `end_image`. Prompt =
  le trajet caméra complet, « one single continuous smooth camera move, no
  cuts, fluid decelerating motion ».
- **`mode: "pro"` doit être passé EXPLICITEMENT** — le défaut est std 720p,
  insuffisant en arrêt sur image. Stratégie validée : un run
  std pour valider la trajectoire à bas coût, puis le run pro (1080p) pour la découpe finale. Le MCP peut proposer un preset hors sujet
  (« IN THE DARK ») : décliner via `declined_preset_id` et relancer littéral.
- Upload des keyframes : `media_upload` (JPG opaque ≥ 1000 px, jamais de
  transparent) → curl PUT → `media_confirm`.
- **Vérifier la facturation Higgsfield AVANT de promettre** : en période de
  grâce, TOUS les modèles vidéo sont bridés à 1/jour (`grace_daily_limit_
  reached`) même avec des crédits. `balance` ne le montre pas.
- Fallback sans vidéo (validé mais inférieur, Sam le repère) : zoom 2.5D
  ffmpeg (crops interpolés easeInOutSine + blend entre keyframes) — bon pour
  débloquer, à remplacer par la vraie vidéo dès que possible.
- Contrôle : extraire 6 frames réparties (`ffmpeg -ss T -frames:v 1`) et les
  REGARDER avant de découper.

### 2 bis. Stabilisation + sur-fluidité (validé pour l'agence immobilière B, 2026-08)
Kling a toujours un micro-tremblement « caméra portée ». Si Sam demande plus
de fluidité / zéro vibration, c'est du POST-TRAITEMENT, pas une re-génération :
1. `ffmpeg -i in.mp4 -vf "vidstabdetect=shakiness=5:accuracy=15:result=t.trf" -f null -`
2. `ffmpeg -i in.mp4 -vf "vidstabtransform=input=t.trf:smoothing=30:zoom=2:interpol=bicubic,unsharp=5:5:0.4:3:3:0.2" -c:v libx264 -crf 12 -preset slow stab.mp4`
3. `ffmpeg -i stab.mp4 -vf "minterpolate=fps=48:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -c:v libx264 -crf 14 stab48.mp4`
→ 719 frames au lieu de 360 : pas de scrub deux fois plus fin, zéro artefact
visible sur un dolly lent d'intérieur (l'interdit d'interpoler ne vaut que
pour la découpe brute — APRÈS stabilisation, minterpolate sur mouvement lent
et régulier est propre ; contrôler 6 frames comme d'habitude). Mobile passe à
1 frame sur 6. Budget : ~27 Mo à 1440px q58, toujours invisible pour
Lighthouse grâce au préchargement au premier geste.

### 2 ter. Qualité 4K (validé pour le caviste, 2026-08)
Quand la netteté des frames est demandée (« 4K ») : vidstab local sur le pro
1080p (SANS minterpolate) → upload du master stabilisé (`media_upload` video)
→ `upscale_video` bytedance `resolution:"4k"`, `fps:60`, `preset:"aigc"`
(remplace le minterpolate local : interpolation pro + 4K en un job, ~2 min)
→ découpe locale `fps=30..48,scale=1440` : chaque frame est suréchantillonnée
du 4K, nettement plus fine qu'une découpe 1080p. ATTENTION au poids : un
contenu extérieur lumineux (ciel, lac, feuillage) pèse 2-3× un intérieur —
102 Mo à 1920px/48fps, ramené à 45 Mo via 1440px/30fps (450 frames). Le
levier de poids est la CADENCE et la définition, pas la quality WebP
(q45→q34 ne gagne que ~15 %). Mobile : pas adapté au compte (1/5 pour 450).
- **Le maximum de fluidité réelle = le nombre de frames de la source**
  (15 s à 24 i/s = 361). Vérifier : `ffprobe -count_frames`. Au-delà =
  interpolation artificielle, artefacts — refuser, SAUF via le pipeline
  stabilisation + minterpolate du § 2 bis (mouvement lent et régulier only).
- Découpe : `ffmpeg -i video.mp4 -vf "fps=N/DUR,scale=1440:-2:flags=lanczos"
  -frames:v N -f image2 -c:v libwebp -quality 55 f-%03d.webp`
  (**`-f image2` obligatoire** sinon un unique webp animé). La numérotation
  de sortie commence à 001 : renommer en 000..N-1 (boucle mv) et caler
  NB_FRAMES sur le compte RÉEL de fichiers (minterpolate peut sortir N-1).
- Budgets constatés : 1440 px q55 ≈ 60 Ko/frame photographique urbaine ;
  360 frames ≈ 22 Mo desktop. Mobile : le composant charge 1 frame sur 3.
- Poster HD séparé (frame 0, 1600 px q80) pour le LCP.

### 4. Composant (modèle : `components/HeroScrub.tsx` du site de l'agence immobilière A, non publié)
- Wrapper `h-[320svh]`, canvas sticky `h-svh`, `useScroll` +
  `useMotionValueEvent` → index = `round(progress × N / pas) × pas`.
- drawImage en « cover » manuel, DPR plafonné à 2.
- **Préchargement au PREMIER GESTE utilisateur** (scroll/touchstart/
  pointermove `once` + filet 3,5 s) : Lighthouse ne fait jamais de geste →
  les frames n'existent pas dans sa fenêtre → Perf intacte (médiane 85 → 92
  constatée). Un préchargement au `load` coûte 6-9 points dès ~8 Mo.
- `fetchPriority = "low"` sur chaque frame.
- **Écran de chargement signé** pendant le préchargement (validé pour l'agence immobilière A) :
  fond couleur de marque, pictogramme SVG silhouette (SANS détails intérieurs
  type porte — Sam les fait retirer) colorié du haut vers le bas par
  `clip-path: inset(0 0 X% 0)`, pourcentage dessous, `role="status"`.
  Fondu de sortie 450 ms. Le poster couvre l'attente.
- Textes du scrub : 2-3 moments courts fondus par plages de progress, le
  dernier = H1. `prefers-reduced-motion` → image finale statique + H1.
- Section suivante : penser au piège sticky (`relative z-10` ou plus, car un
  élément sticky peint au-dessus des sections statiques qui le suivent).

## Gates avant deploy
- Perf alias public best-of-5 ≥ 90 (les frames ne doivent apparaître dans
  AUCUNE requête de la fenêtre d'audit — vérifier au besoin dans le trace).
- Contrôle visuel de 6 frames + le scrub au vrai Chrome (captures multi-
  scroll) ; zéro violation CSP.
- Mobile réel : le pas adaptatif suffit, ne pas charger les 360.
