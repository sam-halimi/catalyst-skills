# Autonomy modes

How much the agent decides alone is chosen at onboarding and written in the state file. It is a setting of the mission, not a mood of the session.

## Three levels of autonomy

| Level | Value in the state file | The agent stops |
|---|---|---|
| Guided | `guidee` | At every step |
| Key checkpoints | `checkpoints_cles` | At checkpoints 1, 2 and 3: art direction, hero, acceptance |
| Autonomous after the art-direction GO | `autonome_apres_go_da` | At checkpoint 1 only, then runs to the end |

## What never becomes autonomous

**Art direction.** The design skill states that it does not run in one shot. Choosing a palette, a typeface or a hero is always arbitrated by a human, on two or three concrete options with a recommendation.

**Anything before the GO.** Whatever the level, the launch sequence runs and the agent stops at checkpoint 1.

**Four kinds of decision stay blocking even in autonomous mode:** security, legality, an ambiguous path, and any action outside the project such as sending a real lead to an external service.

## What an autonomous mission looks like

After the GO, the mission follows a fixed seven-part brief:

1. Header
2. Prerequisites, to be read in full before touching the code
3. Restore point
4. Scope, explicit and closed: a to-do list and a do-not-touch list
5. Numeric constraints
6. Exit gate, in order, no step skipped
7. Deliverable: a report

Rules of the run:

- **No question asked.** Every ambiguity is settled according to the skills and logged in `DECISIONS.md`.
- **Closed scope.** An idea outside the scope is written down, not executed.
- **Restore point.** The initial state is committed before any change, then commits are atomic.
- **Bounded exit loop.** Build, deploy, audit, fix: three passes at most.

## break_the_rules

`break_the_rules` is a **rules regime**, not a level of autonomy. It can be combined with any of the three levels.

Each trade has design defaults: a lawyer's site is sober, a luxury site opens on an image with no call to action. `break_the_rules` lifts some of those defaults for a mission that needs it, for example a personal site for an athlete.

| Lifted | Never lifted |
|---|---|
| Only the defaults listed by name at onboarding | Real facts |
| Each one with its own reason, tied to the story or the brand | Security |
| | Legality |
| | Consent |
| | Accessibility |
| | Build and quality checks |
| | Performance budgets |
| | Traced decisions |

The mode is not activated until the list of invariants has been shown and confirmed. A rule that is not listed as lifted stays in force.

The lifted rules are recorded in the state file under `break_rules.rules_lifted`, and the mode is recalled at every checkpoint so that nobody forgets the mission is running outside the defaults.
