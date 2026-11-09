---
name: experiment-design
description: Design preregistered, resource-bounded, reproducible experiments that distinguish competing scientific hypotheses. Use before coding or launching an experiment.
---

# Experiment Design

## Purpose

Turn research hypotheses into a decisive test with frozen primary metrics and controls.

## Inputs

- One or more linked hypotheses and falsifiers
- Baselines, datasets, tools, compute budget and approvals

## Procedure

### 1. Define discriminating question

State which hypotheses an experiment differentiates, and predictions under each.

### 2. Specify protocol

Write datasets/splits, baseline implementations, interventions, controls, seeds, environment, metric computation and confounder handling.

### 3. Precommit evaluation

Freeze primary metric, success/negative/inconclusive interpretation, stopping criteria and analysis plan before running.

### 4. Estimate resources

Record compute, wall time, storage, dependencies, data rights and any external side effects.

### 5. Assess safety and authorization

Require approval for costs, destructive operations, privileged code or network-enabled experiments.

### 6. Register experiment

Write `research/experiments/X-....md` as DRAFT; do not mark as run or validated until corresponding checks occur.

## Required artifacts

- `research/experiments/X-....md` planned protocol
- Optional `research/decisions/D-....md` comparing candidate tests

## Acceptance checks

- Primary metric defined before outcomes.
- Design includes matched baselines, controls and explicit falsifiers.
- No implicit permission to spend or to execute unsafe code.

## Default handoff

Continue with `experiment-execution` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
