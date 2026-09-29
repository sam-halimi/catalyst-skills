# project-resume

Session recovery for a website project: it finds the project, reads its state file or rebuilds a proposed state from local evidence, reports where the mission stands, and writes nothing without explicit validation.

## What it does

- Locates a project by name, exact match first and fuzzy match second, under the active projects folder and then under the archives folder.
- Reads `.catalyst/production.yaml` first when it exists, after validating it with a script.
- When no state file exists, rebuilds a proposed preview of the state from Git, project instruction files, the decision log, the report, the docs and the code structure. Nothing is written at this stage.
- Reports the situation in a fixed five-part format that ends with one recommended next action.
- Resumes the mission without replaying the onboarding questionnaire, except for missing or explicitly reopened questions.

## When it runs

- Slash command: `/project-resume [nom du projet]`.
- As the "resume" branch of `/website-production`.
- After `/clear` or a change of session.
- Triggers stated in the frontmatter: "reprise", "reprendre le projet X", "où en est le site Y", "continuer la mission".

## Inputs and outputs

Inputs:
- Optional project name or search term.
- `<projet>/.catalyst/production.yaml` when present.
- `DECISIONS.md` and `RAPPORT.md` when present.
- For the reconstruction: Git history and uncommitted files, the project `CLAUDE.md` / `AGENTS.md`, `docs/checkpoint*` and `docs/*`, `package.json`, and the `app/`, `components/`, `public/` folders.
- Reference files of the `website-production` skill: state schema, checkpoint mapping, onboarding questionnaire.

Outputs:
- The resolved project path, displayed before anything else happens.
- A situation report: last checkpoint passed, locked elements, work in progress, open points, next action.
- In the case without a state file: a proposed preview that fills the `production.yaml` template, with deduced values marked as deduced.
- `.catalyst/production.yaml`, created only if the owner chooses to materialize the preview.
- For an invalid state file: the exact validation errors and a proposed correction as a diff.

## How it works

1. Run `discover-project.sh "<term>"` from the `website-production` skill. The search is read-only. The two search roots are set by the environment variables `CATALYST_SITES_DIR` and `CATALYST_ARCHIVES_DIR`.
2. If there are 0 candidates or 2 or more plausible candidates, ask the owner. Each option shows the full path, the date of the last Git commit (or "git absent") and the state files present.
3. If the candidate is in the archives folder, flag it as ARCHIVE and ask how to proceed.
4. Case A, the state file exists: validate it with `validate-state.py`, load it, then complete the context with `DECISIONS.md` and `RAPPORT.md`.
5. Case B, no state file: read the evidence in this order: Git (`git log --oneline -15`, last commit, uncommitted files), then project `CLAUDE.md` / `AGENTS.md`, then `DECISIONS.md` and `RAPPORT.md`, then `docs/checkpoint*` and `docs/*`, then `package.json` and the structure (stack, existing sections, frame sequences).
6. Fill the state template with the deduced values marked as such. Anything uncertain goes to `points_ouverts`.
7. Ask the owner to choose: validate and materialize the state, correct the preview, or continue without a state file.
8. Display the five-part situation report.
9. Resume, replaying only the missing or explicitly reopened onboarding questions.

## Human gates

- Project selection when the search is ambiguous. The selection is never silent.
- Archive candidate: the owner chooses between a read-only resume in place and a new mission through `/website-production`.
- Invalid state file: the correction is proposed as a diff and is not applied silently.
- Reconstructed preview: the owner validates it before the state file is created. The exact path is displayed before the write.
- Explicit validation is required before materializing a state file, running `git init`, creating a commit, or modifying anything in the project.

## Autonomy

The skill file does not define a behaviour per autonomy mode (guided, key checkpoints, autonomous after art-direction GO, break_the_rules). What the file states applies in every case:

- The skill reads and proposes, and writes only with explicit validation.
- The option "continue without state" keeps the session read-only.
- The rules that apply before the art-direction GO, the checkpoints and the controlled learning rule apply identically on resume.

## Hard rules and budgets

- Ambiguity threshold: 0 or >= 2 plausible candidates triggers a question to the owner.
- The retained path is always displayed before continuing.
- An archive is never moved or modified.
- Git history window for the reconstruction: the last 15 commits (`git log --oneline -15`).
- Reconstruction sources are read in a fixed order of 5 steps.
- The situation report has 5 parts in a fixed order.
- Exactly 1 recommended next action, concrete.
- 3 options are offered after the reconstructed preview.
- The full onboarding questionnaire is never replayed when the state already answers.

## Measured results

None stated in the skill.

## Files

- `skills/project-resume/SKILL.md`: the four steps (locate, read the state, report, resume) and the dependency note.

Files of the `website-production` skill used by this skill:

- `skills/website-production/scripts/discover-project.sh`: read-only project search.
- `skills/website-production/scripts/validate-state.py`: state file validation.
- `skills/website-production/references/state-schema.md`: schema of `production.yaml`.
- `skills/website-production/references/checkpoints.md`: checkpoint mapping.
- `skills/website-production/references/onboarding.md`: onboarding questionnaire.
