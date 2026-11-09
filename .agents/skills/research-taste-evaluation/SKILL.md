---
name: research-taste-evaluation
description: Evaluate research decision quality and discovery efficiency using controlled tasks, equal budgets, predefined scoring and leakage safeguards. Use for Research Taste benchmark studies.
---

# Research Taste Evaluation

## Purpose

Separate measured scientific discovery capability from persuasive research prose or historical popularity proxies.

## Inputs

- Decision logs, task/environment specification
- Baseline strategies, controlled budgets, frozen metrics
- Evaluation cutoff and hidden outcome access policy

## Procedure

### 1. Specify evaluation unit

Define discovery task, known hidden mechanism or expert adjudication, action budget and allowed tools.

### 2. Freeze protocol

Predefine metrics: valid discoveries, mechanism accuracy, cost, calibration, reproducibility; fix seeds and stopping rules.

### 3. Build leakage controls

Separate evaluation targets and historical future data from agent inputs; test contamination pathways.

### 4. Establish baselines

Compare direct Codex workflow, structured skills, retrieval-only, random/greedy strategies where meaningful under equal constraints.

### 5. Execute and log

Record actual actions, results and costs; keep hidden evaluation answers outside agent-visible context.

### 6. Analyze rigorously

Report uncertainty, ablations and failures; avoid inferring broad generalization from tiny synthetic tasks.

### 7. Propose revisions

Translate findings into testable skill or scheduling changes, evaluated on fresh held-out tasks.

## Required artifacts

- `research/evaluations/<evaluation-id>-protocol.md`
- Run results and integrity checks
- `research/evaluations/<evaluation-id>-report.md`

## Acceptance checks

- No test answers in agent prompts or indexed sources.
- No fabricated baselines or cross-run resource equivalence.

## Default handoff

Continue with `research-retrospective` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
