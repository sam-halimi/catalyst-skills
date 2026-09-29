# mission-template

Standard 7-part format for an autonomous website mission: closed scope, numeric budgets, a bounded exit gate (build, deploy, audit, at most 3 corrective passes) and two mandatory deliverables, all of it gated behind the owner's approval of the art direction.

## What it does

- Frames the execution of a mission, not its launch. The launch sequence and the art-direction checkpoint come first and are defined in the global instructions.
- Provides a skeleton to copy at the start of every mission: header, prerequisites, restore point, scope, numeric constraints, exit gate, deliverable.
- Replaces questions by logged decisions: every ambiguity is settled according to the applicable skills and written in `DECISIONS.md`.
- Orchestrates other authorities without replacing them: design decisions come from `da-moderne`, code and performance conventions from the global and project `CLAUDE.md`.
- Includes a filled historical example (visual redesign of the jeweller's prospecting demo) with its final scores.

## When it runs

- Triggers stated in the frontmatter: writing or starting an autonomous mission brief, a production prompt, launching or redesigning a `site-*` project, running a hands-off session.
- Trigger phrases: "mission autonome", "prompt de production", "lancement de site", "refonte", "session autonome", "nouveau site-*", "aucune question", "mission 2h".
- Precondition: the explicit GO of the owner on the art direction (checkpoint 1), or a prompt that expressly asks for autonomous execution after that checkpoint.
- No slash command is defined by this skill. The onboarding recap it refers to is produced by `/website-production`.

## Inputs and outputs

Inputs:
- The internal playbook and the mandatory internal notes (demo history, CRM, deployment, Lighthouse measurement protocol).
- The `da-moderne` skill, plus a segment framework recorded in it when one exists.
- The project `CLAUDE.md`. If absent, a minimal one is created that points to `da-moderne` as the design source of truth.
- The prospect's row in the prospecting CRM (a private Google Sheet): exact name, title or speciality, city, contact details, brief, status, notes.
- The mission's own "do not touch" list and numbered to-do list.

Outputs:
- `RAPPORT.md` at the project root: what was done (aligned with the to-do list), final Lighthouse scores (table, URL, date, number of corrective passes), key decisions, open points.
- `DECISIONS.md` at the project root: the journal of autonomous decisions, one file per mission.
- A git history starting with a commit of the initial state, then atomic commits.
- A production deployment on Vercel.

## How it works

1. Header: declare the mission autonomous, with decisions logged in `DECISIONS.md`.
2. Prerequisites: check that everything from the launch sequence was read, without replaying what the session already did.
3. Restore point: `git init` if needed, then commit the initial state before any work. Afterwards, one logical change per commit, French messages, conventional commits.
4. Scope: write the "do not touch" list and a numbered, closed to-do list. An idea outside the list is noted in `DECISIONS.md` as out of scope and not done.
5. Numeric constraints: apply the image budgets, Lighthouse thresholds and breakpoints, and add the mission's own thresholds (number of frames, bundle weight).
6. Exit gate, in order: `npm run build`, production deploy, mobile Lighthouse audit of the 4 categories on the production URL, corrective loop.
7. Deliverable: write `RAPPORT.md` and bring `DECISIONS.md` up to date.

## Human gates

- Checkpoint 1: the DESIGN READ and 2 to 3 art directions with a recommendation are presented to the owner, and the agent waits for the decision.
- Before the GO: no application code, component, final asset, build or deployment. Only pilot and research files are allowed after the onboarding recap is validated: minimal project folder, `.catalyst/production.yaml`, research documents, DESIGN READ. The files state that this exception is not a production GO.
- After the GO there is no interruption for human validation. The agent stops by itself when the corrective loop reaches its limit of 3 passes.

## Autonomy

- Guided: not named in the files. Before the GO the agent follows the launch sequence and stops at checkpoint 1.
- Key checkpoints: not mentioned in the files.
- Autonomous after art-direction GO: this is the mode the skill defines. The 7 parts are executed top to bottom with no question asked, and every decision is logged. It also applies when the owner's prompt expressly asks for autonomous execution after checkpoint 1.
- break_the_rules: not mentioned in the files.

## Hard rules and budgets

- Source hierarchy in case of conflict, highest wins: global instructions, internal playbook, up-to-date memories, specialised skills (including this one), project instructions.
- Image weights: hero < 200 KB (sequence excluded), secondary images < 100 KB, scroll sequence < 3 MB in total.
- Image dimensions: hero <= 1920 px, sections <= 1200 px, macros <= 1600 px. Format WebP or AVIF, quality about 78.
- Lighthouse: the 4 categories >= 90 (performance, accessibility, best-practices, SEO), mobile, in production.
- Breakpoints: mobile 360 to 767 (tested first, iPhone target), tablet 768 to 1023, desktop >= 1024.
- Build: zero error, zero blocking warning.
- Corrective loop: maximum 3 passes. Beyond that, the blocker is recorded in the open points of `RAPPORT.md` and the agent stops.
- A mission is not finished without a green build, a deployment and an audit >= 90, or a documented blocker after 3 passes.
- The CRM sheet is the single source: no local record, CSV copy or duplicate is used or recreated.
- Two deliverables in every case: `DECISIONS.md` (the why) and `RAPPORT.md` (the what and the numbers).

## Measured results

From the filled historical example (the jeweller's prospecting demo, 2026):

| Category | Score |
|---|---|
| Performance | 95 |
| Accessibility | 100 |
| Best-practices | 96 |
| SEO | 100 |

- Performance 95 on the first pass, 0 corrective loop needed.
- Scope figures of that example: mobile variant of the scroll sequence at 36 frames, type clamp 56 to 88 px, body 17/1.7, eyebrows 0.18em, padding 120 to 160 px.

## Files

- `skills/mission-template/SKILL.md`: the precondition, the 7-part skeleton, the filled example and the discipline reminders.

Related skills referenced by the file: `da-moderne`, `seo-garantie-90`, `scroll-frames-3d`, `website-production`.
