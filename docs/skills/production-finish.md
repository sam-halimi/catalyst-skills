# production-finish

Controlled close-out of a website mission: it refuses to close while blocking gates are open, runs a 13-section QA checklist in a fixed order, writes or updates `RAPPORT.md`, and promotes lessons learned only after per-item validation by the owner.

## What it does

- Reads the project state file `.catalyst/production.yaml` and refuses to mark the mission finished while `qa.gates_bloquants_ouverts` is not empty or a blocking checklist item fails. The refusal lists what blocks and the next action.
- Runs the QA checklist in an imposed order, each item receiving a status: PASS, BLOCKED (with reason), N/A (justified) or OUVERT (non-blocking, goes to the open points of the report).
- Creates the project report from a template, or updates an existing one while keeping the history of earlier missions.
- Applies "controlled learning": candidate lessons stay in local project files, and each one is presented with a proposed destination and the exact text or diff before anything is written to a global file.

## When it runs

- Slash command: `/production-finish [nom du projet]`.
- Triggers stated in the frontmatter: "clôture", "finir la mission", "production finish", "enrichis nos données".

## Inputs and outputs

Inputs:
- Optional project name.
- `<projet>/.catalyst/production.yaml`, validated by the `validate-state.py` script of the `website-production` skill.
- State fields used by the checklist: `qa.gates_bloquants_ouverts`, `seo.indexation`, `seo.socle`, `seo.objectif`, `seo.requetes_cibles`, `contraintes.*`, `consentement_requis`.
- `.catalyst/lessons-candidates.md`, `DECISIONS.md`, any existing `RAPPORT.md`, and lessons noted during the session.
- The public production alias of the site. Checks are made on its rendered HTML.
- The popup specification and the lead destination, when the site captures leads.

Outputs:
- `<projet>/RAPPORT.md`, created or updated.
- Updated state file: `statut: cloture`, `checkpoint: cloture`, scores in `qa.scores`, a dated `validations` entry.
- A refusal with the list of blockers when the mission cannot be closed.
- The validated lesson promotions, applied exactly as validated, and the fate of every candidate recorded in the report.
- A reminder of the actions left to the owner: values to paste in the prospecting CRM, external declarations.

## How it works

1. Locate the project with the same rules as `project-resume` and display the path. Read the validated state file.
2. Refuse closure if a blocking gate is open or a blocking item fails. Non-blocking points go to the open points of the report.
3. Run the checklist in order: build, console and hydration, links and routes, assets, responsive, accessibility, SEO/GEO/indexation, performance, forms, popup, lead destination, tracking, legal and brand constraints.
4. Write or update `RAPPORT.md` with the mandatory content: scope, URL/commit/date, decisions, checkpoints, major files, tests and scores, popup and integrations, errors met and resolved, open points, rollback procedure, candidate lessons.
5. Update the state file.
6. Gather the candidate lessons, prepare for each one a destination and the exact text or diff, ask the owner, apply only what was validated.
7. Propose the line for the palette and typography rotation registry under the same regime.
8. Remind the owner of the remaining manual actions.

## Human gates

- Project selection: the resolved path is displayed, never chosen silently.
- No state file: the skill proposes `/project-resume` first and does not close.
- Each candidate lesson is submitted through AskUserQuestion with four options: promote as is, promote modified, keep local, abandon.
- The rotation registry line is written only after validation.
- A real lead test sent to an external service (email, Brevo, Klaviyo, webhook) needs explicitly authorised test data or a confirmation before sending.
- Nothing is deleted, archived or deployed at close-out without an explicit request.
- CRM values are handed to the owner, the CRM being read-only for the agent.

## Autonomy

The skill files do not define a behaviour per autonomy mode (guided, key checkpoints, autonomous after art-direction GO, break_the_rules). What the files state applies in every case: closure is refused while a blocking gate is open, and no lesson is promoted to a global file without explicit validation by the owner.

## Hard rules and budgets

- Checklist of 13 sections in an imposed order.
- Build: zero error, zero blocking warning. Project favicon present, never the create-next-app one.
- Console: zero error and zero hydration warning on every page.
- Links: no residual `href="#"`, phone numbers in +33 format everywhere.
- Assets: hero < 200 KB, secondary images < 100 KB, scroll sequence < 3 MB. AVIF/WebP, `next/image`, hero LCP with `priority`.
- Responsive: captures at 4 widths (360, 390, 768, 1440), no horizontal overflow, touch targets >= 44 px.
- Accessibility gate: Lighthouse a11y >= 95, AA contrast including the footer, `prefers-reduced-motion` respected, full keyboard navigation.
- SEO gate >= 95. A mandatory SEO item in BLOCKED status forbids closure. Contextual items may be N/A only with a justification recorded in the report.
- Exactly one h1 per page. Title and meta description counted on the rendered HTML of every page. JSON-LD verified with `JSON.parse` on the rendered HTML.
- With the noindex gate active, the Lighthouse SEO score is proven on a local build with the flag opened.
- Performance gate >= 90 mobile, measured on the public production alias, best-of-5 when other missions run on the same machine, best and median both retained.
- Forms: server-side validation tested with a forged submission, honeypot or delay active, never `action="mailto:"`.
- Popup: frequency cap verified by a revisit. On mobile, no exit-intent and no full screen before interaction. Focus trap, ESC and focus return. No measurable impact on the performance gates.
- Tracking: 5 events (impression, engagement, submit, success, close). Nothing is sent before consent when `consentement_requis: true`.
- Never invented data sent to a real service. No secret in code, state or report.
- The report is named `RAPPORT.md`, never `PRODUCTION_REPORT.md`, and an existing report is never overwritten.
- Lesson questions are asked in batches of 3 to 4 at most.

## Measured results

None stated in the skill.

## Files

- `skills/production-finish/SKILL.md`: the five steps of the close-out.
- `skills/production-finish/references/qa-checklist.md`: the checklist, item by item, with statuses and thresholds.
- `skills/production-finish/templates/RAPPORT.md`: the report template.

Related skills referenced by the files: `project-resume`, `website-production`, `seo-garantie-90`, `mission-template`.
