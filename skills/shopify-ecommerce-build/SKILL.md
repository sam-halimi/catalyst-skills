---
name: shopify-ecommerce-build
description: "Construire ou reprendre une boutique Next.js sur VPS/Vercel reliée à Shopify : catalogue, variantes, panier, checkout, Admin API séparée, emails, popup, personnalisation, déploiement et recette. Utiliser aussi pour préparer la connexion Shopify d'une nouvelle boutique client."
---
# Boutique e-commerce, procédure partagée

Objectif : permettre à Claude de construire la prochaine boutique sur le VPS et à Codex de faire des corrections ciblées sans recommencer la connexion ni casser les fonctions déjà livrées. Ne pas cloner l'identité visuelle, les données, les secrets ou les décisions commerciales de la boutique horlogère qui sert de cas de référence.

Lire le projet réel et ses instructions. Identifier si l'on fait une nouvelle boutique, une migration de données, un branchement Shopify ou une correction. Ne rejouer que les décisions manquantes. Les consignes actuelles de Sam priment sur les défauts historiques ; l'autorisation d'une correction n'est pas une autorisation générale de prix, stock, email ou publication de produits.

- Nouvelle connexion : [setup Shopify](references/shopify-setup.md).
- Construction de la boutique : [architecture et fonctionnalités](references/storefront.md).
- Build, publication, reprises : [opérations VPS](references/operations.md).
- Exemple concret et limites : [cas de la boutique horlogère](references/cas-boutique-horlogere.md).
- Hero ou collecte : skills voisins `scroll-frames-3d`, `popup-conversion` et `plinko-popup`.

Pour les prix, scopes et schémas d'API susceptibles d'évoluer, consulter les documents officiels au moment du prochain setup. Ne pas présenter un snapshot de septembre 2026 comme une règle éternelle.
