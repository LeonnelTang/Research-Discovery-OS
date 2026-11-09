# RDOS Codex Skills

**16 skills**. These are reusable Codex procedures, not independently running agents or API wrappers.

## Choose a skill

| Skill | Trigger |
|---|---|
| [`research-orchestrator`](research-orchestrator/SKILL.md) | Coordinate an end-to-end scientific discovery cycle across RDOS skills within one authorized Codex session. |
| [`research-resume`](research-resume/SKILL.md) | Resume a research project from persisted repository state across separate Codex sessions. |
| [`research-intake`](research-intake/SKILL.md) | Frame a research goal into a scoped project with explicit resources, success criteria, constraints, and uncertainty. |
| [`literature-review`](literature-review/SKILL.md) | Find, verify, read and compare primary scientific literature with provenance and explicit search coverage. |
| [`research-landscape`](research-landscape/SKILL.md) | Build a structured field map of research approaches, claims, disagreements, assumptions, and opportunity boundaries. |
| [`gap-analysis`](gap-analysis/SKILL.md) | Identify meaningful scientific knowledge gaps and competing explanatory questions from evidence maps, failures, contradictions and assumptions. |
| [`hypothesis-discovery`](hypothesis-discovery/SKILL.md) | Generate, challenge and prioritize falsifiable hypotheses.. |
| [`novelty-audit`](novelty-audit/SKILL.md) | Adversarially audit a research hypothesis against the closest verified prior art and determine precisely what remains unverified. |
| [`critical-review`](critical-review/SKILL.md) | Red-team a research hypothesis, experiment or conclusion for logical failures, alternative explanations, prior work and scientific overclaiming. |
| [`experiment-design`](experiment-design/SKILL.md) | Design preregistered, resource-bounded, reproducible experiments that distinguish competing scientific hypotheses. |
| [`experiment-execution`](experiment-execution/SKILL.md) | Safely implement, execute and record reproducible computational experiments with immutable run artifacts. |
| [`result-analysis`](result-analysis/SKILL.md) | Analyze experiment outputs with appropriate statistics, uncertainty, robustness and competing interpretations. |
| [`evidence-management`](evidence-management/SKILL.md) | Maintain provenance-aware scientific evidence records, contradictions, source verification status and updates to hypothesis support. |
| [`research-synthesis`](research-synthesis/SKILL.md) | Synthesize a goal-level research dossier from verified evidence, hypotheses, experiments and decisions with clear supported and unresolved claims. |
| [`research-retrospective`](research-retrospective/SKILL.md) | Evaluate research decisions, strategy efficiency, failures, costs and future policy adjustments without fabricating counterfactual outcomes. |
| [`research-taste-evaluation`](research-taste-evaluation/SKILL.md) | Evaluate research decision quality and discovery efficiency using controlled tasks, equal budgets, predefined scoring and leakage safeguards. |

## Default end-to-end path

```text
research-resume / research-intake
  → literature-review → research-landscape → gap-analysis
  → hypothesis-discovery → novelty-audit → critical-review
  → experiment-design → [human authorization] → experiment-execution
  → result-analysis → evidence-management → research-synthesis
  → research-retrospective → next research decision
```

The `research-orchestrator` selects the next bounded procedure; it does not create an autonomous background agent. `research-taste-evaluation` is an optional controlled research/evaluation branch.

## Invocation

Open this repository in Codex and ask:

> Read AGENTS.md and use the research-orchestrator skill for goal G-0001. Resume from persisted files and complete only the next authorized, verifiable research step.

For a narrow step, request the skill by name (e.g., `novelty-audit`). Codex should read that skill file. Skills do not automatically run on a timer.

## Core handoff contract

For every completed step, persist a relevant research record with stable ID, source pointers, status, open unknowns, and explicit next action. Handoff does not mean the next skill ran.

## Shared standards

- [`docs/RESEARCH_METHODOLOGY.md`](../../docs/RESEARCH_METHODOLOGY.md): evidence and hypothesis rules.
- [`docs/SKILL_CONTRACTS.md`](../../docs/SKILL_CONTRACTS.md): artifact and handoff requirements.
- [`AGENTS.md`](../../AGENTS.md): global safety and developer instructions.
- [`docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md): source-of-truth representation.

## Offline validation

```bash
python scripts/validate_skills.py
python scripts/validate_records.py
python -m unittest discover -s tests -v
```

These commands do not use any model API or require network access.
