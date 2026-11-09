---
name: research-retrospective
description: Evaluate research decisions, strategy efficiency, failures, costs and future policy adjustments without fabricating counterfactual outcomes. Use after a research cycle.
---

# Research Retrospective

## Purpose

Improve Research Taste through transparent review of which choices generated real information per resource spent.

## Inputs

- Decision history, goal, experiment plans and results
- Actual resource usage and outcomes

## Procedure

### 1. Reconstruct chronology

List candidate actions, selected actions, rationale, predicted outcome and actual observation.

### 2. Separate failure causes

Classify low-quality hypothesis, poor design, implementation bug, weak evidence, constraint mismatch and random uncertainty.

### 3. Assess decision calibration

Compare recorded expectations to outcomes only where comparable and sufficiently numerous; avoid fake probability statistics.

### 4. Estimate discovery efficiency

Count validated results or resolved hypotheses per verified time/compute where meaningful; describe data gaps.

### 5. Identify policy changes

Recommend small, testable changes to search operators, reviewer steps or experiment selection.

### 6. Record future test

Write a before/after comparison proposal for one policy change, with safeguards against retroactive benchmark changes.

## Required artifacts

- `research/retrospectives/<goal-id>-<date>.md`
- New decision record for revised research strategy

## Acceptance checks

- Historical alternatives are not assigned invented outcomes.
- Agent self-assessment is labeled as non-independent.

## Default handoff

Continue with `research-orchestrator` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
