# Build, publication et mémoire commune

## Reprise rapide
Sur VPS : confirmer le chemin absolu et lire CLAUDE.md/AGENTS.md, docs d'opérations, package.json, versions de dépendances et état actuel. Sur un checkout sans Git, faire une archive ciblée horodatée ; ne pas inventer un commit. Avec Git, conserver les modifications utilisateur et comparer les fichiers touchés avant écrasement. Entre Codex local et Claude VPS, transférer seulement les fichiers concernés avec leurs empreintes attendues.

Un correctif autorisé n'exige pas de refaire le questionnaire de nouvelle mission. Les règles d'onboarding de DA s'appliquent aux décisions de design non prises, pas à une réparation de loader ou de formulaire déjà demandée. Les identifiants Admin restent dans le dossier d'intégration ; les modifications de frontend et Vercel se font dans le projet site.

## Build Vercel
VPS référence : Node et npm existants, Next.js App Router/TypeScript/Tailwind ; vérifier package-lock, utiliser npm ci sur un nouveau checkout, éviter les mises à jour majeures opportunistes. Exécuter npm test puis npm run build. Les warnings et erreurs de réseau Shopify doivent être compris, pas cachés en désactivant SHOPIFY_ENABLED. Une erreur d'offset Framer peut survenir seulement au navigateur : faire aussi la recette UI.

Équipe Vercel `<equipe>`, nom/projet exact dans `.vercel/project.json`. Authentification existante via un jeton Vercel chargé depuis l'environnement, sans l'afficher ; ne pas ouvrir ni copier les secrets dans la documentation. CLI observée `vercel@59.15.1`. Une preview et une production peuvent avoir des env différentes ; vérifier les noms/cibles sans sortir les valeurs. S'assurer que les flags de commerce et de checkout persistent dans Production ET Preview. Publier selon l'autorisation du fil, puis tester l'alias réel et relever l'identifiant du déploiement dans le journal d'exploitation.

Ne pas lancer plusieurs builds dans le même dossier .next ni tuer les processus d'autres sites. Pour les médias, uploader un dossier versionné avant son composant et préserver l'ancien rollback. Les déploiements peuvent exclure .env.local : ne jamais compter dessus pour la configuration distante.

## Capitalisation
Les quatre skills partagés ont une seule source de référence sur le VPS ; les dossiers `~/.claude/skills/<skill>/` correspondants pointent dessus. La copie locale Codex est un instantané, non une synchronisation automatique. Avant un edit du skill, récupérer la version distante ; après validation, synchroniser et comparer les SHA-256. Les instructions doivent utiliser des chemins relatifs vers leurs références et citer les chemins d'exploitation seulement dans les documents de cas.

Mettre à jour le journal d'exploitation du projet (`docs/OPERATIONS-<CLIENT>.md`) et les repères CLAUDE.md/AGENTS.md du projet après changement matériel. Dans la mémoire globale, un court index mène au document précis ; éviter cinq copies contradictoires d'une même procédure. Conserver anciens rapports comme historiques datés. Une autorisation de capitalisation donnée par Sam pour un cycle ne crée pas une autorisation perpétuelle pour modifier tout son système sans demande.

## Exploiter le stockage de leads d'une boutique
Cas de la boutique horlogère : service Docker dédié, code dans `<projets>/integrations/<client>-leads/`, volume data persistant. HTTPS sur un port dédié, certificat privé épinglé via CA Base64 côté Vercel, secret bearer serveur. Config dans `~/.config/<client>/leads/`, permissions 700/600 ; ne pas copier ce dossier dans les assets ou les skills. Le certificat doit être renouvelé avant sa date notAfter puis la CA Vercel mise à jour et le site redéployé. Ne jamais contourner TLS avec rejectUnauthorized=false.

Contrôler docker ps et /health ; si échec, vérifier uid/gid réels de l'utilisateur de service (ne pas supposer 1000), droits du volume, logs sans données personnelles, certificat, connexion depuis Vercel, quota mémoire. Le serveur accepte seulement ses actions RPC définies, pas de SQL arbitraire. Une base SQLite n'est pas copiée à chaud avec cp : employer sqlite3.Connection.backup. Pour restauration, arrêter seulement ce service, conserver une copie de la base courante, restaurer la sauvegarde choisie et vérifier avant reprise.
