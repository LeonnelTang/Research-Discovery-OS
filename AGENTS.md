# AGENTS.md — Research Discovery OS

Repository-wide operating instructions for Codex and compatible coding agents. **RDOS is Codex-native:** Codex performs reasoning, literature work, coding and experiments directly through its authorized tools. This repository **does not call an LLM API**, run its own LLM agent framework, or promise unattended operation after a Codex session ends.

## Mission and current scope

RDOS exists to transform vague scientific interests into traceable, falsifiable hypotheses and reproducible experiments while developing better research judgment. The near-term deliverable is a **human-supervised, repository-persistent research loop**, not an autonomous scientist. Read `README.md`, `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` before architectural changes.

### Core invariants

1. **Evidence is not belief.** Store external claims, original observations, interpretations and hypotheses distinctly. An LLM statement is never proof.
2. **No fabricated sources or results.** Never invent paper titles, DOIs, quotes, benchmark measurements, timestamps, executed commands or study outcomes. If lookup is unavailable, mark `unverified`.
3. **Every scientific claim is scoped.** Record conditions, sources, counterevidence, uncertainty and limits of inference. Do not use unsupported calibrated probabilities.
4. **No silent rewriting.** Preserve previous hypotheses, negative findings and decision records. Revisions link to their predecessors; corrections add new records rather than altering original evidence.
5. **Reproducibility over polish.** Experiments must specify inputs, code revision, environment, seeds, baseline, metrics and execution artifacts. An experiment that ran successfully is not necessarily scientifically valid.
6. **Codex is the executor, not the authority.** Codex may propose actions and edit workspace files, but local validators enforce schema and state rules. Human approval is needed before costly, destructive, privileged or external-side-effecting actions.
7. **No new model stack.** Do not install OpenAI SDKs, agent orchestration frameworks, model gateways, API servers, databases or cloud infrastructure unless the user explicitly changes this architecture.
8. **No hidden autonomous loop.** Do not claim research continues after the Codex session unless an explicitly configured and authorized scheduling mechanism exists.

## Start-of-session protocol

1. Inspect repository and `git status` without overwriting user changes.
2. Read `README.md`, this file, `docs/ARCHITECTURE.md` and relevant skill(s).
3. Locate the current goal and latest research decision in `research/`; if there is no goal, request or establish one explicitly, marking assumptions.
4. State the proposed task, expected artifacts, tools and cost/risk before substantial execution.
5. Prefer a short verified step over a large unverified chain.
6. At the end, write a decision record or research update and accurately report commands run, results and remaining uncertainty.

## Repository map

- `.agents/skills/`: reusable Codex research procedures, not autonomous services.
- `research/goals/`: goals, constraints, success conditions.
- `research/hypotheses/`: hypothesis specifications and revisions.
- `research/evidence/`: source metadata, evidence links and provenance.
- `research/experiments/`: preregistered plans, run manifests, results and analysis.
- `research/decisions/`: choices, alternatives, rationale and next actions.
- `docs/`: architecture, methodology and roadmap.
- `scripts/`: deterministic local validators/utilities, not LLM callers.
- `tests/`: reproducible tests for local tools.

## Research workflow

Use the [skill catalogue](.agents/skills/README.md) to select the appropriate Codex workflow; for end-to-end work start with `research-orchestrator`, and for a new idea start with `hypothesis-discovery`. Default sequence:

1. **Frame goal** — important question, resource limits and success criteria.
2. **Map literature** — identify nearest prior work from verified accessible sources; note searches attempted and publication cutoff.
3. **Find gaps** — failures, contradictions, implicit assumptions, simplifications and cross-domain mechanisms.
4. **Propose hypotheses** — competing causal explanations with falsifiers and observable predictions.
5. **Adversarial review** — attempt to disprove novelty and identify confounders; treat unsupported novelty as `unverified`.
6. **Choose next action** — prioritize an inexpensive discriminating experiment or a specific missing evidence lookup.
7. **Record** — update research artifacts, including negative/inconclusive results and why a decision was made.

Do not infer a hypothesis is novel solely from lack of retrieval hits. A failed search is not proof of novelty.

## Data and lifecycle conventions

Use the schemas and directory contract in `docs/ARCHITECTURE.md`. IDs should be stable (e.g. `G-0001`, `H-0001`, `E-0001`, `X-0001`, `D-0001`). File names must include stable IDs. Prefer YAML front matter plus Markdown bodies for human-readable records; tools must parse and validate required fields before accepting transitions.

Hypothesis states: `PROPOSED → GROUNDED → TESTABLE → QUEUED → TESTING → EVALUATED`. `SUPPORTED`, `REFUTED`, `INCONCLUSIVE`, `SUPERSEDED` are **evaluation dispositions**, not claims of universal truth. Do not advance a hypothesis without required evidence or experiment links; when validation tooling is unavailable, label a status as *proposed*, not authoritative.

## Engineering standards

- Prefer Python standard library for initial scripts; add dependencies only when they solve a concrete need.
- Use typed interfaces, small functions, explicit errors and portable relative paths.
- Never use shell wildcard deletion, force-push, reset, destructive migrations or secret exfiltration without authorization.
- Avoid secrets in commits, prompts and experiment logs. Inspect generated diffs.
- Keep test fixtures deterministic and offline; no live model calls in automated tests.
- Before declaring completion, run relevant tests/validators, report exact commands and any failures; never claim checks ran if they did not.
- Keep changes scoped. Do not change unrelated experimental records or rewrite history for convenience.

## Experiment safety and integrity

Before executing generated or untrusted code, inspect it and use an appropriately isolated, resource-bounded environment. Do not assume a container is secure if it is privileged or has unrestricted host mounts/network access. Declare controls, baselines, primary metric, termination conditions and resource cap **before** seeing the result. Distinguish infrastructure failure, coding bug, negative result and inconclusive scientific observation. New parameters or metrics after inspection require a new experiment revision.

## Completion report template

- **Goal / change:** what was attempted
- **Artifacts:** paths created/modified
- **Evidence:** sources and outputs actually inspected
- **Verification:** exact checks executed and outcome
- **Limitations:** unknowns, unverified claims and remaining issues
- **Next action:** one concrete recommended step

## Explicit prohibitions

Do not fabricate sources/data; present a speculative idea as a verified finding; silently discard negative results; bypass validation or authorization; run generated code unbounded on host; expose secrets; introduce LLM API integration by default; falsely claim Codex can schedule itself; invent test success; conceal incomplete work; or modify research acceptance criteria after viewing experimental results without recording a revision.

**Operating principle: Codex reasons and executes; the repository remembers; deterministic tools validate; experiments provide evidence; humans retain control.**

## Skill routing and validation

Before research, consult `.agents/skills/README.md`; invoke only the relevant skill(s), do not emulate multiple independent agents or initiate background work. All handoffs follow `docs/SKILL_CONTRACTS.md`. After editing skill files run `python scripts/validate_skills.py`; after editing research records run `python scripts/validate_records.py`. These local checks are structural, **not scientific verification**.
