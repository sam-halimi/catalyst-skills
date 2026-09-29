# da-moderne

Art direction method that derives a client-specific visual system for each site, through an interactive loop with numeric design budgets.

## What it does

- Defines a method for deriving palette, typography, layout, motion and imagery from the client's real material, instead of applying a theme.
- Provides four modes (Produit, Expérience, Fonctionnel, Vision), each tied to one audited public reference site.
- Provides three variants (Commerce éditorial, Produit-héros, Tech institutionnelle) that refine a parent mode for a given case.
- Holds the audits of the seven reference sites: measured tokens, observed composition, mechanisms to transpose, and the trap if copied badly.
- Accumulates dated production lessons from real projects, a default framework for lawyer websites, a 14-item pre-delivery checklist and a final test.

## When it runs

- Skill name: `da-moderne`. No slash command is defined in the skill files.
- Trigger stated in the frontmatter: any request to design, mock up, restyle or critique a client site (home page, landing page, redesign, palette, typography, layout or animation choices), even when the request mentions neither "design" nor "DA".

## Inputs and outputs

Inputs (the minimal brief):

- The client's trade and the sector's trust object: the thing the visitor must see to believe.
- What the visitor must do at the end: call, book, visit, request a quote.
- Available material: real product photos, photos of the place, logo, existing colours.
- Three adjectives the client would use to describe itself.
- What the client does not want to look like.
- The audit of the chosen mode in `references.md`, and of the variant if one applies.

Outputs:

- A dominant mode for the site. A second mode may colour one section at most.
- 2 to 3 palette and typography directions submitted for arbitration.
- A plain-text section hierarchy without style.
- The hero composed alone at final level, then sections composed one by one.
- A motion pass, done last.
- The completed pre-delivery checklist and the result of the final test.
- The skill files name no output file or path.

## How it works

1. Framing: ask the minimal brief questions before writing any code. Do not start if the trust object is not identified.
2. Choose the dominant mode and re-read its audit in `references.md`. Transpose the mechanisms of the reference, never its tokens.
3. Tokens: propose 2 to 3 palette and typography directions, then stop.
4. Skeleton: section hierarchy in plain text, then stop.
5. Hero alone: compose only the first screen, at final level, then stop. Nothing below is composed until the hero is approved.
6. Section by section: one section, one validation.
7. Motion pass: animation comes last, never during composition.
8. Run the pre-delivery checklist (14 items).
9. Final test: remove the logo and the client name. If the site could belong to another business of the same sector, restart at the tokens step.

## Human gates

- Before starting: the trust object must be identified.
- After the tokens proposal: stop and wait for arbitration.
- After the skeleton: stop and wait for arbitration.
- After the hero: stop. The hero validates the rest of the site.
- Each section gets its own validation.
- A variant is proposed at the tokens checkpoint as one direction among the 2 or 3, never applied by default.
- Any unproven association between a real photo and real data is flagged to the owner, who arbitrates before the prospect sees it.
- Lawyer sites: the site is declared to the bar before public launch. This is implemented as an `INDEXATION_OUVERTE` gate (noindex plus robots disallow), flipped after validation.

## Autonomy

- The skill files state that the skill does not run in one shot and that a complete site is never generated in a single pass.
- Autonomous missions without intermediate validation are stated as reserved for performance, SEO and CRM work, not for art direction.
- The lessons describe a short protocol of 3 checkpoints (tokens and concept, hero, acceptance), followed by 2 to 4 feedback loops after the first go-live.
- The modes named guided, key checkpoints, autonomous after art-direction GO and break_the_rules do not appear in the skill files. Their behaviour is not defined here.

## Hard rules and budgets

- Palette: 1 dominant background (never pure `#FFFFFF` or `#000000`), 1 ink (never pure black), 1 accent, 3 neutrals derived from the background.
- Accent surface: under 5 %. Up to 10 % in Expérience mode when it comes from a real light of the place. One documented exception in Vision mode, where the background is the brand colour.
- Typography: 2 families maximum, 2 weights per family maximum, display to body ratio of at least 6:1.
- Hero display size: 56 to 120px on desktop, set with `clamp()`.
- Body text: 17 to 19px, line height 1.6 to 1.75, line length 60 to 72 characters.
- Title line height: 0.95 to 1.1.
- Section vertical padding: 120 to 200px on desktop.
- Grid: 12 columns, broken at least once per page.
- Motion: 1 entrance animation per section maximum, 500 to 900ms, custom `cubic-bezier` curves only, stagger 60 to 120ms, parallax offset 15 % maximum, `prefers-reduced-motion` handled.
- Hover zoom in Produit mode: 1.02 to 1.04.
- Scroll zoom on textured backgrounds: about 1 to 1.09. Hero image scroll zoom: 1 to 1.08.
- Commerce éditorial variant: ratio may go down to 4:1 when each banner is a full-frame campaign image. Below about fifteen products, stay on the canonical Produit mode.
- E-commerce variants: one discreet call to action allowed in the hero.
- Booking widget in a hero: 3 to 4 fields maximum.
- White text on dark textured backgrounds: titles at full opacity, body at 85 %, captions at 70 %.
- Small labels on an accent background must reach a 4.5:1 contrast.
- Stats band: 3 to 4 sourced figures. No review rating is displayed unless verified.
- One spectacular moment per site, never duplicated.
- No em dash in visible copy. French non-breaking spaces applied.
- Lawyer sites: no reviews, testimonials or ratings, no `AggregateRating` in JSON-LD, no client names, 3 dominant practice areas maximum, real portrait only.
- PageSpeed mobile of at least 90, stated as non-negotiable.

## Measured results

- One real estate demo cycle took 7 versions, with 4 feedback loops after the first approval.
- Generated texture backgrounds: about 5 KB in WebP; 1600px at quality 62 gives 4 to 45 KB; 1400px at quality 42 to 50 gives 4 to 40 KB.
- An ochre accent was lightened to reach a 4.5:1 contrast with the ink.
- Reference audits, display to body ratios: 8:1 (casperscaviar.com, displays 71 to 95px on 11.9px body), up to 15:1 (supadupa.nl), about 6:1 (aerodynamics.nl), 3:1 to 4:1 (skims.com), about 4.5:1 (drinkupdate.com), 6:1 (mistral.ai).
- Reference audit, page length: 16 500px (aerodynamics.nl).
- No measured PageSpeed or Lighthouse score is stated in the skill. Only the target of 90 appears.

## Files

- `skills/da-moderne/SKILL.md`: method, shared system, modes, variants, production lessons, lawyer framework, checklist, final test.
- `skills/da-moderne/references.md`: audits of the seven reference sites and two syntheses.
- Related skill cited: `popup-conversion` (reference file `scratch-card.md`).
