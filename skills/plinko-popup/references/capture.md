# Collecte, consentement et réalité du cadeau

Trois modes séparés : aperçu sans capture ; réservation avec email réellement conservé, aucun code prétendument utilisable ; récompense échangeable avec vrai code Shopify et conditions vérifiées. Ne pas activer le drapeau des codes Shopify simplement pour enlever l'aperçu.

## Contrat serveur
Le serveur signe le lot, la graine, l'horodatage et la variante. Le navigateur envoie attemptId, email, consentement explicite, langue et champs contextuels bornés ; jamais un prizeId faisant autorité. Exiger un secret stable aléatoire en production (pas un secret de démo connu), comparer signature et cookie, rejeter corps invalide, email invalide, honeypot, tentative trop récente/expirée et consentement absent. Rate limit en mémoire = protection best effort, pas quota global entre instances serverless.

À la réclamation, enregistrer email normalisé, source plinko, langue, consentement, version du texte, lot et événement. Aucun succès si stored=false. L'utilisateur peut réessayer avec le même lot après panne. Cookie claimed uniquement après réussite. Les retries doivent garder le même code et ne pas distribuer un nouveau lot ; les événements de capture sont un journal, pas une preuve de vente.

La réservation renvoie `rewardStatus: reserved`, `code: null`, `stored: true` ; afficher un message de réservation explicite et préciser à partir de quand la récompense sera utilisable. Ne pas annoncer un email envoyé si l'on a seulement enregistré l'adresse. Le mode échangeable requiert le code de la récompense dans l'env et sa réalité dans Shopify ; afficher le code seulement après les vérifications et la persistance.

## Stockage (projet de référence)
Un adaptateur de stockage côté serveur parle à un service HTTPS dédié sur un serveur distinct de l'hébergement du site, authentifié par jeton bearer et certificat approuvé explicitement. Son adresse, son jeton et son certificat sont des variables serveur ; jamais NEXT_PUBLIC. La base SQLite vit dans le dossier de données du service de leads, jamais dans le build Vercel ni dans /tmp. Upstash reste un adaptateur possible selon le client. Sans adaptateur : aucun succès de collecte. Le journal ne doit pas conserver les emails ni le texte des messages dans les logs.

Newsletter et contact partagent le stockage, mais message contact ≠ abonnement marketing. Le panier Shopify ne doit pas devenir artificiellement un lead marketing sans consentement. Export protégé par un jeton d'administration transmis dans l'en-tête Authorization, pas dans l'URL. Les campagnes et confirmations d'achat nécessitent un fournisseur et des événements réels, elles ne sont pas automatiquement actives parce que des segments existent.

## Shopify : conditions à implémenter avant activation
Remise en pourcentage sur la commande : périmètre des produits, exclusions, cumul, validité et minimum convenus. Cadeau physique offert : variante réellement ajoutée et remise applicable, stock/livraison vérifiés, pas seulement code affiché. Remise sur le deuxième article : règle de quantité et de prix (le moins cher si c'est la promesse), tester un article, deux articles différents, même modèle en quantité 2, accessoires, suppression d'un article. Une remise globale du même taux n'est pas équivalente ; une Function ou une règle buy-X-get-Y peut être nécessaire selon le besoin et le plan. Ne pas créer ces règles sans la demande appropriée.

## Recette de persistance
Tests unitaires avec store mock pour succès, refus consentement, token falsifié, cookie absent, stockage hors ligne et code manquant. Pour le bout en bout, utiliser un marqueur technique sur domaine .invalid dans une base contrôlée, sans appeler de fournisseur d'envoi, vérifier sa lecture puis le supprimer précisément ; les données de véritables abonnés ne sont jamais supprimées pour « nettoyer un test ». Pour tester un véritable email, utiliser l'adresse autorisée par Sam.
