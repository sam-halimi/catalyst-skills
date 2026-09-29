# plinko-popup

Implements or fixes a falling-ball (Plinko) lead-capture popup for an e-commerce store: ball physics, server-signed prizes, resume, consent, real lead storage and Shopify reward conditions.

## What it does

The skill documents one specific lead-capture component: a popup where a ball falls onto a board and lands on a prize. It gives the file map of the component, the validated geometry and physics rules, the trigger and frequency-cap rules, the accessibility requirements and the QA protocol.

It defines a server contract in which the server signs the prize and the browser never sends an authoritative prize id. It separates three operating modes: preview without capture, reservation with a stored email and no code, redeemable reward with a real Shopify code.

The logic was validated on the watch store project. The skill states that it is reused without copying one client's brand, offers or configuration into another client's project.

## When it runs

- Skill name: `plinko-popup`. No slash command is written in the skill files.
- Trigger stated in the description: Sam asks for the Plinko game or for this precise component.
- The game is not imposed on every popup. The general choice of a popup belongs to `popup-conversion`, the store launch to `shopify-ecommerce-build`.

## Inputs and outputs

Inputs:
- The existing component sources (`components/plinko/`, `lib/plinko/`, `app/api/plinko/`), read before any patch.
- The exact drop position of the ball, received by the server as `dropX`.
- Claim payload from the browser: attemptId, email, explicit consent, language, bounded context fields.
- Server environment variables: signing secret, storage service address, token and certificate, Shopify code flag and reward codes. The popup state version is a separate variable.
- The reward conditions agreed for the Shopify discounts.

Outputs:
- Code patches to the component, its library and its API routes (`/api/plinko/draw`, `/claim`, `/reset`).
- A stored lead record at claim time: normalized email, source, language, consent, consent text version, prize, event.
- Reservation response: `rewardStatus: reserved`, `code: null`, `stored: true`.
- No report file is declared by the skill.

## How it works

1. Read `references/implementation.md`, then `references/capture.md`.
2. Read the existing source files before patching, because historical comments sometimes describe old behaviour.
3. Follow the file map: trigger, capture steps (intro, drawing, dropping, landed, email, claiming, done), SVG board, sampled trajectory, shared geometry, server signing, config, API routes.
4. Keep the board and physics rules: the prize comes from the exact drop position, and the ball travels to its signed prize from the position and velocity of the visible ball.
5. Configure triggering and the frequency cap.
6. Implement the UI and accessibility requirements.
7. Choose one of the three operating modes.
8. Implement the server contract: signing, rejection cases, claim persistence, idempotent retries.
9. Wire the lead storage adapter. Without an adapter there is no collection success.
10. Implement and test the Shopify discount conditions before activation, only when requested.
11. Run the QA on the real render, then the persistence tests.

## Human gates

- No email or campaign is sent on behalf of the client without a corresponding request.
- Shopify discount rules are not created without the appropriate request.
- A test with a real email uses only the address authorized by Sam.
- The real render must be looked at after the physics tests. A screenshot of the final slot does not validate the path.
- Counter-rule: the user can directly authorize a fix or an integration, and is not asked again to validate a specification already decided.

## Autonomy

The skill files name no autonomy mode (guided, key checkpoints, autonomous after art-direction GO, break_the_rules). The only related statement is the counter-rule above: an already decided specification is not submitted for validation a second time.

## Hard rules and budgets

- Board logical width 400. Five slot centres at x = 40, 120, 200, 280, 360. Rewards only at indices 0, 2, 4.
- The winning slot is the reward closest to `dropX`, not a legacy weighted draw. Probabilities that the game does not apply are never advertised.
- The ball never teleports to another slot. Edge cases at x = 120 and x = 280 stay under test.
- The popup does not open during the hero. The timer arms when the hero is left.
- Reference trigger setting: desktop 10 s or 40 % scroll, mobile 12 s or 45 % scroll, exit intent on desktop only.
- Cart and checkout pages are excluded. The game yields to any other modal.
- The state version is frozen during real collection. A build-time `Date.now` version makes every refusal forgotten.
- Visible close, Escape, backdrop click, focus trapped then returned to the opener.
- Reduced motion: shortened trajectory, unchanged result.
- QA viewports: 1440x900, 390x844, 390x700. Three destinations and several speeds are tested.
- The server signs prize, seed, timestamp and variant. Production requires a stable random secret.
- Rejected: invalid body, invalid email, honeypot hit, attempt too recent or expired, absent consent.
- The in-memory rate limit is best effort, not a global quota across serverless instances.
- No success if `stored=false`. The claimed cookie is set only after success. Retries keep the same code.
- Storage variables are server-only. The database is neither in the Vercel build nor in `/tmp`. Logs keep no email and no message text.
- A contact message is not a marketing subscription. A cart does not become a marketing lead without consent.
- A global discount is not equivalent to a discount on the second item. Tested cases: one item, two different items, same model in quantity 2, accessories, removal of one item.
- End-to-end tests use a technical marker on a `.invalid` domain, with no sending provider. Data of real subscribers is never deleted to clean up a test.

## Measured results

None stated in the skill.

## Files

- `skills/plinko-popup/SKILL.md`: scope, reading order, reuse rule, related skills.
- `skills/plinko-popup/references/implementation.md`: file map, board and physics rules, triggering, UI and QA.
- `skills/plinko-popup/references/capture.md`: operating modes, server contract, storage, Shopify conditions, persistence tests.
