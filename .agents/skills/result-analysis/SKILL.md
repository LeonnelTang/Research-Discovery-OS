---
name: result-analysis
description: Analyze experiment outputs with appropriate statistics, uncertainty, robustness and competing interpretations. Use after reproducible run artifacts exist.
---

# Result Analysis

## Purpose

Convert raw outcomes into carefully scoped findings while preserving alternative explanations and negative evidence.

## Inputs

- Experiment plan and frozen analysis criteria
- Raw runs/manifests, baselines, seeds, metrics and available code

## Procedure

### 1. Validate inputs

Check manifest integrity, split consistency, failure rates, missing seeds, computation matching and actual evaluation protocol.

### 2. Reproduce aggregation

Calculate primary metric as preregistered; explicitly label exploratory analyses.

### 3. Estimate uncertainty

Use an appropriate uncertainty approach for study design; report sample sizes and effect sizes without invented precision.

### 4. Assess confounds

Test whether gains arise from extra compute, leaks, preprocessing, data selection or failed baselines.

### 5. Interpret outcomes

Distinguish supported, refuted and inconclusive *under tested conditions*; consider competing predictions.

### 6. Record findings

Save analysis, attach evidence with source run paths, and request hypothesis evaluation through repository conventions.

## Required artifacts

- `research/findings/<experiment-id>-analysis.md`
- `research/evidence/E-....md` derived from actual artifacts
- Decision record for next discriminating action

## Acceptance checks

- Numerical results match raw artifacts.
- Primary vs post-hoc metrics differentiated.
- No sweeping scientific claims beyond tested scope.

## Default handoff

Continue with `evidence-management` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
