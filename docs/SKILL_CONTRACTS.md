# Skill handoff contracts

All research stages run within the current authorized Codex session. Skills are *procedures*, not separate Agent processes.

## Identity and artifact storage

- ResearchGoal `G-####`: `research/goals/G-####.md`
- Hypothesis `H-####`: `research/hypotheses/H-####.md`
- Evidence `E-####`: `research/evidence/E-####.md`
- Experiment `X-####`: `research/experiments/X-####.md`
- ResearchDecision `D-####`: `research/decisions/D-####.md`
- Search log/review: `research/literature/`
- Critical/novelty reviews: `research/reviews/`
- Run outputs: `research/experiments/runs/X-####/<run-id>/`
- Result analyses: `research/findings/`
- Dossiers: `research/reports/`
- Retrospectives: `research/retrospectives/`
- Taste evaluation: `research/evaluations/`

Use existing Markdown front-matter templates under `research/*/TEMPLATE.md`. Do not assume records are valid without checking.

## Handoff content

1. Goal ID and bounded research question.
2. Files read and evidence actually checked, with exact citation/source paths.
3. New/updated artifact paths and status of validation.
4. Current hypotheses, competing explanations and strongest objections.
5. What was tried and observed (separate from interpretations).
6. Resource budget, approvals, pending dependencies.
7. One explicit next research action and its stop/decision criterion.

## Scientific evidence levels (descriptive, not probabilities)

- **Unverified**: proposed or cited without inspecting source.
- **Source-reported**: source checked but underlying result not reproduced.
- **Reproduced**: validated by recorded local rerun under stated conditions.
- **Conflicting**: credible evidence disagrees; retain both.
- **Invalidated**: artifact or methodology compromised; never silently delete.

## Experiment gate

No experiment execution without a frozen plan, appropriate sandbox/limits and required user authorization. Execution `COMPLETED` is distinct from scientific disposition `SUPPORTED`, `REFUTED` or `INCONCLUSIVE`.

## Session boundary

A future Codex session resumes via `research-resume`, not hidden chat history. Do not claim the system runs after the session ends.
