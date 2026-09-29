# popup-conversion

Decides whether a site should have a lead-capture popup at all, then specifies (and implements when asked) the pattern, triggers, consent, lead destination and tracking, with dark patterns banned.

## What it does

- Answers first whether a popup serves the site. It may conclude `capture: inline` or `capture: aucune` and says why.
- Chooses a capture pattern from a catalogue of 8: classic lead magnet, micro-engagement, quiz, visual quiz, scratch card, mystery reward, gamification, classic newsletter or callback.
- Specifies triggers, frequency cap, mobile format, accessibility, performance, SEO and consent.
- Specifies the lead destination (email, CRM spreadsheet, Brevo, Klaviyo, webhook), server validation, anti-spam, event tracking and A/B variants.
- Contains a full scratch-card specification derived from a measured audit of a public reference popup.
- Covers the correction of an existing popup without replaying the onboarding.

## When it runs

- Slash command: `/popup-conversion`.
- Called by `/website-production`, or on its own.
- Triggers stated in the frontmatter: "popup", "capture de leads", "lead magnet", "formulaire de conversion", "quiz de qualification".

## Inputs and outputs

Inputs:
- The `conversion` block and `tracking.consentement_requis` of the project's `production.yaml`.
- The site's `da-moderne` design tokens.
- The niche of the site and the real offer exchanged for the email.
- The chosen lead destination. For a webhook, the URL supplied by the owner.
- For a correction: the existing popup code and the recorded decisions.

Outputs:
- A complete `conversion` block (plus `tracking`) ready for `production.yaml`, conforming to the state schema of the `website-production` skill.
- An implementation plan: components, hook points, states, French copy.
- A list of open points, such as the offer to confirm or the emailing service to choose.
- Leads destined for the CRM spreadsheet, handed over as exact values to paste. The skill never writes to it.
- When implementation is requested: the popup component and a server route handler (`app/api/lead/route.ts`), with the field mapping kept in the spec and as a comment in the route.

## How it works

1. Relevance: refuse the popup when there is no real offer, when the niche forbids it, when the site is a prospecting demo, or when inline capture is enough.
2. Pattern: pick from the catalogue with the context grid (first and second choice per niche).
3. Triggers and cadence: set the triggers, the frequency cap, the reopening conditions, the excluded pages, the mobile format, accessibility, performance, SEO and consent.
4. Destination: define the destination, the field mapping, server validation, anti-spam, the end-to-end test and the event schema.
5. Check the device against the list of banned dark patterns.
6. Deliver the `conversion` block, the implementation plan and the open points.
7. Implementation or correction: read the code and decisions, keep the chosen offer, implement the requested changes and verify the full path. Stored collection, provider subscription, email sent and discount actually applicable are checked as four separate facts.

## Human gates

- Gamification is allowed only if coherent with the brand and validated by the owner.
- The offer and the emailing service are left as open points for the owner.
- Any external test action (a real lead sent to a service) requires explicitly authorised test data or prior confirmation.
- No new third-party tracking tool without a decision from the owner.
- A dedicated subscriber base for a shop is persisted only when the owner asks for it.

## Autonomy

The skill files do not define a behaviour per autonomy mode (guided, key checkpoints, autonomous after art-direction GO, break_the_rules). What the files state:

- In `recommandation`, the skill proposes 2 quantified options with a recommendation, never an open question.
- A correction request on an existing popup does not replay the onboarding.
- The external test gate above applies in every case.

## Hard rules and budgets

- One offer, one ask (email), an exit that is always obvious.
- Exit-intent: desktop only, never by default on mobile.
- Delay trigger: 20 to 40 s, never under 10 s. Scroll trigger: 50 to 70 % of the page. Page-view trigger: 2 pages or more.
- Default combination: click plus one single passive trigger.
- Frequency cap: 1 passive display per 7 days, stored in `localStorage` under a versioned key. A refusal counts like a close. After a successful submission, no passive display ever again.
- Mobile: bottom sheet or banner, close zone of 44 x 44 px minimum, tested at 360, 390, 768 and 1440.
- Accessibility is blocking: `role="dialog"`, `aria-modal`, `aria-labelledby`, focus trapped then returned to the trigger, ESC, overlay click, AA contrast on all states.
- Performance: component loaded with `next/dynamic` after the first interaction or idle, no extra font, scores measured before and after integration.
- Anti-spam: honeypot plus rejection of submissions under 2 s after opening, no visual CAPTCHA by default, per-IP rate limit.
- No secret in state, committed code or report. Keys live in environment variables referenced by name.
- The browser never talks to a third-party service with a key. Never `mailto:` as a form action.
- Event schema shared by every pattern: `impression`, `engagement`, `submit`, `success`, `close`.
- A/B: one variable at a time, stable assignment per visitor, 50/50.
- Entry animation budget: 1 per section, 500 to 900 ms, custom `cubic-bezier`.
- Quiz: 3 to 5 questions.
- Scratch card: reveal threshold 45 to 50 %, fade of 500 to 700 ms, round brush of 36 to 44 px, alpha sampling of 1 pixel in 16 at most once every 150 ms.
- Scratch card trigger: scroll of 40 to 50 %, or second page view, or 30 s of active presence. Desktop modal 420 to 480 px wide.
- Scratch card budgets: background image WebP of 60 KB maximum, component JavaScript of 8 KB gzip maximum with no third-party scratch library, host page mobile performance unchanged at 90 or more.
- Scratch card prize: decided and signed server side before display (signed token, single use, validity period), one prize per visitor per cap period.
- State machine of 4 states: `invitation`, `revelation`, `capture`, `confirmation`, persisted in `localStorage`.

## Measured results

- Lighthouse Best Practices fell to 77 on an earlier project because of a `mailto:` form action (mixed content). This is the origin of the rule above.
- Observations on the audited reference popup, which are not results of the skill: display between 3 and 6 seconds after load, card of 300 x 220 CSS px on a 600 x 440 canvas, full reveal after 3 finger passes.
- No conversion rate, lead volume or A/B result is stated in the skill.

## Files

- `skills/popup-conversion/SKILL.md`: relevance gate, non-negotiable rules, banned dark patterns, outputs, implementation and resume.
- `skills/popup-conversion/references/patterns.md`: pattern catalogue and context grid.
- `skills/popup-conversion/references/triggers-consent.md`: triggers, frequency cap, mobile, accessibility, performance, SEO, consent.
- `skills/popup-conversion/references/integrations-tracking.md`: destinations, validation, mapping, end-to-end test, events, A/B.
- `skills/popup-conversion/references/scratch-card.md`: reference audit, what is not reused, transposition spec, acceptance checklist.

Related skills: `da-moderne`, `seo-garantie-90`, `website-production`, `plinko-popup`.
