---
name: gap-analysis
description: Identify meaningful scientific knowledge gaps and competing explanatory questions from evidence maps, failures, contradictions and assumptions. Use to choose worthwhile problems.
---

# Gap Analysis

## Purpose

Distinguish a true knowledge gap from a missing keyword match or low-value benchmark opportunity.

## Inputs

- Landscape and verified literature
- Research goal constraints and prior failed directions

## Procedure

### 1. Enumerate gap types

Look for conflicting findings, untested causal claims, implicit assumptions, missing discriminating experiments and measurement limitations.

### 2. Apply discovery operators

Use INVERT, EXPLAIN_FAILURE, ABSTRACT, SIMPLIFY, TRANSFER, CONTRADICTION with explicit source grounding.

### 3. Specify each gap

For each, describe what is known, what remains unknown, why it matters, and what observation would resolve it.

### 4. Stress-test importance

Ask whether solving gap generalizes, changes an explanation, unlocks capability, or is merely a local metric tweak.

### 5. Check feasibility

Outline minimal evidence collection or experiment needed; flag missing assets and hard constraints.

### 6. Select opportunities

Keep diverse gap candidates; avoid assigning arbitrary precise confidence numbers. Route selected gap to hypothesis discovery.

## Required artifacts

- `research/literature/<goal-id>-gaps.md`
- `research/decisions/D-....md` for a narrowed problem

## Acceptance checks

- No gap inferred purely from search silence.
- Each retained gap contains an observable resolution criterion.

## Default handoff

Continue with `hypothesis-discovery` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
