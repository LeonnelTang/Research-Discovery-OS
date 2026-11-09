---
name: research-landscape
description: Build a structured field map of research approaches, claims, disagreements, assumptions, and opportunity boundaries. Use after literature review before ideation.
---

# Research Landscape

## Purpose

Map scientific mechanisms and uncertainties so hypothesis search is guided by gaps rather than paper-title combinations.

## Inputs

- Verified evidence records and source search log
- Goal, constraints and current hypotheses

## Procedure

### 1. Define axes

Choose meaningful comparison axes: scientific question, causal mechanism, assumptions, data, setting, cost, strengths, failure modes.

### 2. Build method matrix

Classify sources using evidence-backed statements. Mark missing information instead of filling by intuition.

### 3. Construct claim graph

Identify support, contradiction, refinement, dependence and disputed generalizations; preserve context-dependent results.

### 4. Locate underexploration

Distinguish empirical blind spots, measurement gaps, theoretical assumptions and engineering constraints. Do not claim universal absence.

### 5. Prioritize gaps

Score qualitatively for scientific significance, tractability, testability and coverage uncertainty, giving evidence for each judgment.

### 6. Handoff

Prepare gap statements and relevant source IDs for `gap-analysis` or `hypothesis-discovery`.

## Required artifacts

- `research/literature/<goal-id>-landscape.md`
- Optional `research/decisions/D-....md` if a branch is selected

## Acceptance checks

- Matrix comparisons use consistent dimensions.
- Every flagged contradiction records differing experimental conditions.

## Default handoff

Continue with `gap-analysis` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
