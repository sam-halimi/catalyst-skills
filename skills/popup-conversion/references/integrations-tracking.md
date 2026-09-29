# Destinations des leads, validation, tracking, A/B

## Règle zéro — secrets et CRM

- **Aucun secret** dans `production.yaml`, le code committé, les rapports :
  clés API et tokens vivent dans les variables d'environnement Vercel
  (`vercel env`), référencées par NOM (`BREVO_API_KEY`) jamais par valeur.
- **CRM de prospection de l'agence (Google Sheet privé) = lecture seule** :
  l'intégration ne peut pas éditer de cellule, les leads « crm_sheet » sont
  donc remis à Sam en **valeurs exactes à coller**
  (ligne formatée). Aucune écriture directe, aucun CRM local, aucune copie
  CSV (règle globale de l'agence).

## Destinations

| Destination | Implémentation | Notes |
|---|---|---|
| `email` | Route handler Next → service d'envoi transactionnel côté serveur | Jamais de `mailto:` en action de formulaire (mixed content : Best Practices Lighthouse tombé à 77 sur un projet antérieur) ; composer côté serveur ou en JS à l'envoi. |
| `crm_sheet` | File des leads restituée à Sam (valeurs à coller) | Voir règle zéro. Peut compléter une autre destination. |
| `brevo` | API contacts/events via route handler serveur | Clé en env Vercel ; double opt-in selon l'usage. |
| `klaviyo` | API profiles/events via route handler serveur | Idem. |
| `webhook` | POST serveur → URL fournie par Sam | URL du client = configuration, pas un secret, mais vérifier qu'elle n'embarque pas de token signé avant de la mettre dans l'état ; sinon env var. |
| `autre` | À spécifier au cas par cas | Documenter dans la spec, secrets en env. |

Toujours passer par une **route handler serveur** (`app/api/lead/route.ts`) :
le navigateur ne parle jamais directement à un service tiers avec une clé.

## Validation et anti-spam

- Validation HTML5 (type, required) POUR l'UX, **re-validation serveur POUR la
  vérité** : format email, longueurs, champs attendus uniquement.
- Anti-spam discret par défaut : champ honeypot invisible + rejet des
  soumissions < 2 s après ouverture. Pas de CAPTCHA visuel par défaut (coût
  UX + a11y) ; l'envisager seulement sur abus constaté.
- Rate-limit simple par IP sur la route (mémoire ou en-tête Vercel).
- Réponses d'erreur utiles côté client, sans détail technique côté serveur.

## Stockage et mapping

- Définir le mapping AVANT l'implémentation : champ formulaire → champ
  destination (ex. `email` → contact Brevo `EMAIL`, `reponse_quiz` → attribut
  `SEGMENT`). Le mapping vit dans la spec (et en commentaire de la route).
- Horodatage + page d'origine + variante A/B joints à chaque lead.
- La base abonnés propre à une boutique peut être persistée sur une infrastructure dédiée lorsque Sam le demande, dans un service isolé et documenté. Cela ne change pas l'interdiction de recopier le CRM de prospection de l'agence.

## Test de bout en bout

Toute action externe de test utilise une **donnée de test explicitement
autorisée** (email de Sam ou alias dédié convenu) ou demande confirmation
avant l'envoi. Jamais d'email inventé vers un vrai service, jamais de test
silencieux.

## Tracking des événements

Schéma unique, quel que soit le pattern :

| Événement | Quand |
|---|---|
| `impression` | Popup affiché (passif ou clic) |
| `engagement` | Première interaction (réponse de quiz, grattage, focus champ) |
| `submit` | Soumission envoyée |
| `success` | Confirmation serveur |
| `close` | Fermeture sans soumission (+ raison : bouton, ESC, overlay) |

- Implémentation minimale par défaut : compteur first-party (route handler ou
  Vercel Analytics si déjà présent) — pas de nouvel outil tiers sans décision
  de Sam (et consentement le cas échéant).
- Les événements ne partent qu'après consentement quand
  `tracking.consentement_requis: true`.

## Variantes et A/B

- Tester UNE variable à la fois (offre, titre, trigger, pattern) — deux popups
  entiers différents ne s'interprètent pas.
- Assignation stable par visiteur (localStorage), 50/50, variante jointe aux
  événements et au lead.
- Durée minimale avant conclusion : dépendre du trafic réel de la démo — sur
  un site de prospection à faible trafic, préférer les décisions de design aux
  micro-tests sans puissance statistique (le dire plutôt que de simuler un
  A/B décoratif).
