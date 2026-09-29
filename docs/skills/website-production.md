# website-production

Onboarding orchestrator for website missions: it runs a batched multiple-choice questionnaire, shows an editable recap, writes a validated per-project state file, and routes to the specialised skills without duplicating them.

## What it does

- Frames a new website mission, a resume or a special mission before the first art-direction checkpoint (GO DA).
- Asks its questions through `AskUserQuestion` in batches of 3 to 4, with conditional branches (CRM, niche, break_the_rules, lead capture).
- Writes nothing during the questionnaire. The state is recorded only after an explicit validation of a full recap.
- Records the mission in `<project>/.catalyst/production.yaml` (schema version 2), declared the source of truth so that a session can be rebuilt after `/clear`.
- Checks that state with a deterministic Python validator that also rejects secret-like patterns.
- Decides nothing on substance (design, SEO, popup, execution autonomy). It references the existing authorities: the global CLAUDE.md, an internal playbook, `da-moderne`, `seo-garantie-90`, `scroll-frames-3d`, `mission-template`, `popup-conversion`, `project-resume`, `production-finish`.

## When it runs

- Slash command: `/website-production [prospect or project name]`.
- The frontmatter sets `disable-model-invocation: true`: the skill starts only on the explicit command.
- No trigger phrase is listed in the skill files.

## Inputs and outputs

Inputs:

- Optional argument: a prospect or project name, passed as the search term to `scripts/discover-project.sh`.
- Existing project folders under the sites and archives roots, scanned read-only (state file, `DECISIONS.md`, `RAPPORT.md`, `CLAUDE.md`, `package.json`, `docs/checkpoint*`, last git commit, count of uncommitted files).
- The answers to the 19 mandatory onboarding points, plus point 11 bis (search objective) and the break_the_rules questions when that mode is active.
- The existing `production.yaml` when the project already exists.
- The prospect's row in the private prospecting CRM, read during the launch sequence (read-only).

Outputs:

- A displayed list of candidate projects tagged `CANDIDAT`, `MATCH_EXACT` or `MATCH_FUZZY`. The script never selects one.
- A displayed recap: all answers, the exact project path, the exact list of files to create or modify.
- The minimal project folder `site-<slug>/` and `.catalyst/production.yaml`.
- The validator verdict (`VALIDE`, `INVALIDE`, `AVERTISSEMENT`) with exit codes 0, 1 and 2.
- `DECISIONS.md` kept or created, and `.catalyst/lessons-candidates.md` created empty or at the first lesson.
- Updates of `production.yaml` at each checkpoint crossed (status, checkpoint, validations, timestamps).

## How it works

1. Context resolution, read-only: run `discover-project.sh` with the given term and display the candidates. If the mode is a resume, switch to `project-resume`.
2. Onboarding questionnaire with no write: Lot 1 mission frame (mission type, CRM, niche, autonomy), Lot 2 creative frame (rules regime, art direction mode, hero type, assets source), Lot 3 content and foundation (sections, content and research, SEO foundation, search objective, lead capture), Lot 4 conversion (offer, popup type, triggers and frequency, lead destination) only if capture is not "aucune", the break_the_rules lot if active, Lot 5 compliance and locking.
3. Editable final recap, then one question: validate and record the state, modify answers (only the affected batches are replayed), or cancel.
4. Recording: display the exact path, create the folder and the state file, run `validate-state.py` immediately. For an existing project, show the diff before overwriting.
5. Pre-GO frame: run the launch sequence of the global CLAUDE.md in order, then stop at checkpoint 1 (DESIGN READ plus 2 to 3 art directions).
6. After GO DA: interactive session or routing to `mission-template` depending on the autonomy level, `popup-conversion` if capture is planned, closure with `/production-finish`.

## Human gates

- Choice of the project when several candidates or a doubt exist.
- Point 19: validation of the mission architecture (perimeter, applicable checkpoints, autonomy, deliverables).
- Final recap: validate, modify or cancel.
- Diff shown before any overwrite of an existing `production.yaml`.
- break_the_rules: which rules are lifted, one reason per rule, confirmation that the invariants stay active.
- Checkpoint 1 (art direction): mandatory stop, explicit GO from Sam on one direction.
- Checkpoint 2 (hero): the hero alone, at final level, validated before going further.
- Checkpoint 3 (acceptance) before deployment.
- A checkpoint is recorded in `validations` only on an explicit decision ("GO", "validé"), never inferred from silence.
- Closure: candidate lessons are presented one by one, with no promotion without Sam's validation.

## Autonomy

- `guidee`: validation at every step. Interactive session following `da-moderne` and the playbook, with checkpoints 2 (hero) and 3 (acceptance).
- `checkpoints_cles`: validation at checkpoints 1, 2 and 3 of the playbook. Same interactive session.
- `autonome_apres_go_da`: after the explicit GO DA, the skill routes to `mission-template` with a closed perimeter derived from `production.yaml` (to-do list, do-not-touch list, numeric constraints). Security, legality, an ambiguous path and any external action (test lead, publication, email) remain blocking.
- `break_the_rules`: a rules regime, not an autonomy level. It lifts only the niche and pattern defaults that are listed with a reason in `break_rules.rules_lifted`. A rule that is not listed stays in force, and the mode is recalled at each checkpoint. Invariants kept in all cases: real facts, security, legality, consent, accessibility, build and QA, performance budgets, traced decisions.

## Hard rules and budgets

- Questions in batches of 3 to 4 at most; 19 mandatory onboarding points.
- During the questionnaire: zero file, zero folder, zero state. On cancel, no file or folder may exist.
- Before GO DA: no application code, component, final asset, build or deployment. Only steering and research files are allowed, and this exception is not a production GO.
- An invalid state must never be left on disk.
- No secret or token in the state, the reports or the repository. Integrations are referenced by service name only.
- No local CRM: the private CRM sheet is the single source, read-only.
- No deletion of backups or existing files: report, do not clean.
- Never an open question when 2 to 3 concrete options with a recommendation are possible.
- Exit-intent trigger on desktop only, never by default on mobile.
- 3D scroll-frames hero only if the narrative carries a travelling shot.
- Exit gates, by reference: 4 Lighthouse categories on the public production alias, Performance >= 90, SEO >= 95, Accessibility >= 95, Best Practices >= 90, best-of-N if the server is loaded, at most 3 corrective passes.
- `schema_version` must be 1 or 2; version 2 requires `seo.objectif`.
- `seo.objectif: trafic` requires 3 to 5 non-empty target queries.
- The slug must match the basename of the path (`site-<slug>`); timestamps are ISO 8601.
- `niche: avocat` requires `contraintes.cadre_avocat: true`.
- Capture `popup` or `les_deux` requires `conversion.popup.type`; any capture other than `aucune` requires a non-empty destination.
- `validations` is an append-only journal.

## Measured results

None stated in the skill.

## Files

- `SKILL.md`: authority and position, the 6-step flow, break_the_rules mode, permanent prohibitions.
- `references/onboarding.md`: the canonical questionnaire (Lots 1 to 5, break_the_rules questions, recap template).
- `references/checkpoints.md`: mapping between the `checkpoint` field of the state and the existing authorities and gates.
- `references/state-schema.md`: schema version 2 of `production.yaml`, conditional fields, v1 to v2 migration.
- `scripts/discover-project.sh`: read-only project discovery, exact then case-insensitive substring match. Roots set by `CATALYST_SITES_DIR` and `CATALYST_ARCHIVES_DIR`.
- `scripts/validate-state.py`: deterministic validator (enums, conditional fields, slug and path coherence, ISO 8601, secret patterns). Requires PyYAML.
