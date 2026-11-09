---
name: critical-review
description: Red-team a research hypothesis, experiment or conclusion for logical failures, alternative explanations, prior work and scientific overclaiming. Use before expensive validation.
---

# Critical Review

## Purpose

Expose why an appealing idea might be wrong, already known, noncausal or not worth pursuing.

## Inputs

- Hypothesis/experiment/report to critique
- Evidence and nearest prior work
- Budget and researcher goals

## Procedure

### 1. Restate claim neutrally

Describe a precise falsifiable proposition separate from marketing wording.

### 2. Attack assumptions

Find hidden assumptions, brittle boundary conditions, logical leaps and unrealistic prerequisites.

### 3. Test alternative explanations

Identify at least two viable competing hypotheses and which observations distinguish them.

### 4. Audit evidence and novelty

Inspect citations and compare strongest baselines; indicate where source access is insufficient.

### 5. Test the proposed evaluation

Check leakage, confounds, metric validity, statistical power, compute matching and potential cherry picking.

### 6. Give actionable revision

Provide blocker / major / minor issues, cheapest decisive check and go / revise / stop recommendation with rationale.

## Required artifacts

- `research/reviews/<id>-critical.md`
- Decision record if recommendation changes direction

## Acceptance checks

- Review distinguishes fatal flaws from open uncertainties.
- No assertion of independent validation solely from a second persona in the same Codex session.

## Default handoff

Continue with `experiment-design` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
