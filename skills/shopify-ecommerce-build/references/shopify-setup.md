# Connexion d'une nouvelle boutique Shopify

## Préparer sans mélanger les clients
Relever domaine canonique myshopify.com, organisation propriétaire, nom de boutique, devise, marchés, canal voulu, produits existants et mode de paiement. Dossier `sites/site-<client>` pour Next.js et `integrations/<client>-shopify` pour l'administration. Confirmer le projet Vercel dans `.vercel/project.json`, pas seulement son nom. Nouveau répertoire de secrets sous `~/.config/<client>/`, nouveau cache de jeton, nouveaux secrets de cookies et stockage email isolé.

Ne jamais faire pointer l'outil Admin d'un client existant vers une autre boutique en modifiant simplement son domaine : son allowlist est volontaire. Créer une configuration et une cible propres au nouveau client, avec les mêmes protections et des tests spécifiques.

## Storefront et Headless
Installer/configurer le canal Headless autorisé dans la boutique cible, créer le storefront et son accès adapté. Le jeton Storefront n'est pas le client_secret de l'app Admin. Rendre les produits disponibles sur le canal voulu ; ACTIVE seul ne garantit pas leur présence dans Storefront. Lire catalogue et variantes depuis Storefront et comparer au catalogue Admin. Le frontend peut rester entièrement Next.js/Vercel ; aucun thème Shopify à reconstruire si le brief est headless.

Le runtime de la boutique horlogère emploie SHOPIFY_STORE_DOMAIN, SHOPIFY_STOREFRONT_ACCESS_TOKEN et SHOPIFY_API_VERSION côté serveur. Pinner une version stable disponible après vérification officielle, ne pas employer `unstable` en production. La version 2026-07 est celle vérifiée sur ce projet, pas automatiquement celle du prochain. Configurer Production ET Preview durablement ; un simple `.env.local` sur le VPS n'est pas envoyé à Vercel.

## Administration et authentification
Le client_credentials grant convient à une app installée sur une boutique appartenant à la même organisation Shopify que l'app. Pour une app distribuée à d'autres marchands, choisir le flux approprié ; ne pas supposer que ce grant marche partout. Créer l'app dans le Dev Dashboard, sélectionner les scopes nécessaires dans sa version, installer cette version sur la boutique, puis échanger client_id/client_secret contre un token côté serveur. Lire expires_in et renouveler, ne pas copier un token éphémère comme configuration permanente.

Pour la boutique horlogère : outil Python stdlib avec cache atomique mode 600, dossier 700, expiration anticipée de 60 s, renouvellement après 401, refus des redirections et hôte exact HTTPS. Reproduire ces propriétés pour le prochain client. Ne pas afficher les secrets dans shell, logs, rapports, screenshots ou commandes utilisateur ; aucune clé Admin dans NEXT_PUBLIC, frontend ou déploiement du site.

Scopes : demander ceux nécessaires à la tâche, vérifier ceux réellement accordés avec auth-check. Produits, inventaire, fichiers, réductions et emplacements sont distincts ; publication de canal peut nécessiter un autre scope. Les clients/commandes ne sont pas nécessaires à une simple gestion du catalogue. Documenter les manques avant l'opération, pas après un faux succès.

## Import et mapping
Si des produits existent, lire et exporter d'abord. Le CSV sert à un import initial maîtrisé, pas aux modifications courantes de prix/stocks. Mapper une clé de présentation stable vers handle, SKU et option ; récupérer les vrais GID de variantes par lecture. Vérifier unicité des SKU, nombre d'options, noms de coloris, images, variantes sans option et produits archivés. Ne pas créer une deuxième fois le catalogue pour résoudre une erreur de mapping.

Les prix viennent de Shopify en mode commerce. Faire les mutations de prix/stock seulement pour la demande explicite, à partir des IDs lus, avec export avant écriture, userErrors inspectés puis relecture. Une publication produit et un changement de canal ne sont pas implicites dans un changement de design.

## Sources officielles à relire
- https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant
- https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started
- https://shopify.dev/docs/api/storefront/latest/mutations/cartCreate

Ces pages ont été consultées le 11 septembre 2026. Les instructions spécifiques de l'outil et les vérifications du projet complètent ces sources ; ne pas copier leurs exemples avec un ancien numéro d'API sans vérification.
