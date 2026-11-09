---
name: research-orchestrator
description: Coordinate an end-to-end scientific discovery cycle across RDOS skills within one authorized Codex session. Use when user asks to investigate a goal end to end.
---

# Research Orchestrator

## Purpose

Choose the next skill and persist handoffs; do not simulate a daemon or separate LLM agent framework.

## Inputs

- Research goal and scope
- Current state and latest decision
- Authorization and resource budget

## Procedure

### 1. Restore state

Start with research-resume or research-intake. Read source-of-truth files rather than assuming previous conversation context.

### 2. Identify current bottleneck

Determine whether the next step is missing literature, unclear gap, invalid hypothesis, unreviewed experiment, or unanalyzed result.

### 3. Select bounded skill

Invoke only relevant one or two skills at a time. For new projects follow intake → literature → landscape → gaps → hypotheses → novelty → critique.

### 4. Use approval gates

Before execution ensure experiment-design, review, budget and authorization. If unavailable, stop at a complete plan.

### 5. Persist handoffs

Each executed skill writes required artifacts and next action; avoid relying on chat-only outcomes.

### 6. Close loop

After experiment execution use result-analysis → evidence-management → synthesis → retrospective as appropriate.

### 7. Report completion honestly

List actual work, exact artifacts, validation outcomes, unresolved uncertainty and proposed next turn.

## Required artifacts

- Updated goal-linked records from delegated skills
- Decision and next-action record

## Acceptance checks

- No silent infinite recursive skill loop.
- No autonomous background operation or model API invocation.
- Every important decision and experiment has a persisted handoff.

## Default handoff

Continue with `research-resume` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
