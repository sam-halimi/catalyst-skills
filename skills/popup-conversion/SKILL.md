---
name: popup-conversion
description: "Spécification d'un dispositif de capture de leads pour un site Catalyst (popup, inline ou refus motivé). Invoqué par /website-production ou seul. Décide d'abord SI un popup est pertinent, puis spécifie pattern, triggers, frequency cap, mobile, accessibilité, performance, SEO, consentement, validation anti-spam, destination des leads (email, tableur CRM, Brevo, Klaviyo, webhook) et tracking/A-B. Aucun dark pattern, exit-intent jamais par défaut mobile. Déclencheurs : popup, capture de leads, lead magnet, formulaire de conversion, quiz de qualification."
---

# /popup-conversion — capture de leads sans dark pattern

Ce skill cadre le dispositif puis permet son implémentation quand elle est demandée. Pour une nouvelle spécification, compléter le bloc `conversion` de
`production.yaml` et le plan d'implémentation. La DA du dispositif
reste soumise à `da-moderne` (tokens du site, jamais un style par défaut) ;
la performance et le SEO restent soumis aux gates du playbook interne et à
`seo-garantie-90`.

## 0. Pertinence d'abord — le popup n'est pas un défaut

Avant tout pattern, répondre : **un popup sert-il ce site ?** Refuser (et le
dire) quand : il n'y a pas d'offre réelle à échanger contre l'email ; la niche
l'interdit ou le rend indigne (cadre avocat : sobriété réglementaire — pas de
gamification) ; le site est une démo de prospection où le dispositif nuirait à
l'effet « production d'agence chère » ; la capture inline suffit (formulaire
contact déjà dans le bottom verrouillé). Conclusion possible et respectable :
`capture: inline` ou `capture: aucune`. Un site sans cookie ni formulaire est
un argument commercial documenté.

Si un popup est retenu : une seule offre, une seule demande (email — chaque
champ supplémentaire coûte), une sortie toujours évidente.

## 1. Choisir le pattern

Catalogue, critères de choix et anti-patterns :
[references/patterns.md](references/patterns.md). Types couverts : lead magnet
classique, micro-engagement, quiz, visual quiz, scratch, mystery reward,
gamification (SEULEMENT si cohérente avec la marque), classique. En
`recommandation` : proposer 2 options chiffrées avec recommandation, jamais
une question ouverte.

## 2. Triggers, cadence, mobile, a11y, consentement

Règles complètes : [references/triggers-consent.md](references/triggers-consent.md).
Non négociables (rappel) :
- **Exit-intent : desktop uniquement, JAMAIS par défaut sur mobile.**
- Frequency cap obligatoire + conditions de réouverture explicites.
- Fermeture toujours possible : bouton visible, ESC, clic hors zone ; focus
  piégé pendant l'ouverture, rendu au déclencheur à la fermeture.
- Chargement différé (`next/dynamic`, après interaction ou idle) : zéro impact
  LCP/TBT, le popup n'existe pas dans le chemin critique.
- Pas d'interstitiel intrusif au sens Google : jamais au chargement de la
  page, jamais plein écran sur mobile avant interaction.
- Consentement/cookies : le dispositif respecte le régime déclaré dans
  `production.yaml` (`tracking.consentement_requis`).

## 3. Destination, validation, tracking

Règles complètes : [references/integrations-tracking.md](references/integrations-tracking.md).
Non négociables (rappel) :
- **Jamais de secret dans l'état, le code committé ou le rapport** — noms de
  services seulement, clés en variables d'environnement Vercel.
- **Tableur CRM de l'agence = lecture seule** : les leads qui lui sont
  destinés sont remis à Sam en valeurs exactes à coller. Aucun CRM local,
  jamais.
- Validation serveur systématique (l'HTML5 seul ne suffit pas) + anti-spam
  discret (honeypot + délai minimal), jamais de CAPTCHA visuel par défaut.
- Événements : impression, engagement, submit, success, close — schéma unique
  quel que soit le pattern, pour comparer les variantes A/B.

## 4. Interdits absolus (dark patterns)

- Pas de « confirm shaming » (« Non merci, je préfère rater des clients »).
- Pas de faux compte à rebours, fausse rareté, faux tirage.
- Pas de case pré-cochée, pas d'inscription implicite.
- Pas de récompense annoncée non tenue (un « mystery reward » a un contenu
  réel, défini à l'avance).
- Pas de popup qui se rouvre à chaque page vue après un refus.
- Un refus se respecte : le cap de fréquence s'applique au refus comme à la
  fermeture.

## 5. Sortie du skill

1. Bloc `conversion` complet (+ `tracking`) prêt pour `production.yaml`,
   conforme au schéma d'état du skill `website-production`
   ([state-schema.md](../website-production/references/state-schema.md)).
2. Plan d'implémentation (composants, points d'accroche, états, textes FR
   sobres sans slop).
3. Points ouverts (offre à confirmer par Sam, service d'emailing à trancher…).
Toute action externe de test (envoi d'un lead réel vers un service) exige une
donnée de test explicitement autorisée ou une confirmation préalable.

## Implémentation et reprise

Une demande de correction d'un popup existant ne relance pas tout l'onboarding. Lire le code et les décisions, conserver l'offre choisie, implémenter les changements demandés et vérifier le chemin complet. Pour le jeu boule qui tombe, lire le skill voisin `../plinko-popup/SKILL.md`. Pour la carte à gratter, lire [references/scratch-card.md](references/scratch-card.md). Pour le stockage et les récompenses Shopify, lire sa référence `../plinko-popup/references/capture.md`. Ce pattern est optionnel : un popup classique reste un premier choix possible selon le site.

Distinguer toujours collecte stockée, inscription chez le fournisseur, email envoyé et remise réellement applicable. Un HTTP 200 sans stockage n'est pas un formulaire fonctionnel. Le CRM de prospection de l'agence et la base consentie des abonnés d'une boutique sont deux systèmes distincts ; une autorisation de Sam pour une base e-commerce dédiée doit être respectée. Ne jamais recopier le CRM de prospection dans cette base.
