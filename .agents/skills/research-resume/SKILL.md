---
name: research-resume
description: Resume a research project from persisted repository state across separate Codex sessions. Use at start of a continued research task.
---

# Research Resume

## Purpose

Restore the current research frontier without relying on hidden chat memory or hallucinated past work.

## Inputs

- Goal ID or project topic
- Repository research records and last decision

## Procedure

### 1. Check repository

Read AGENTS.md, status, architecture and skill index; inspect git status without overwriting changes.

### 2. Locate project

Find goal, recent decisions, active hypotheses, latest evidence and experiment state.

### 3. Reconcile state

Identify stale links, uncommitted files, incomplete runs and contradictions. Do not assume queued/running work actually continues.

### 4. Produce concise checkpoint

Report known facts, open questions, blocked work, resource constraints and last authorized next action.

### 5. Choose narrow continuation

Ask only if an essential authorization/goal is missing; otherwise propose a bounded next step and invoke relevant skill.

### 6. Record material deviation

If route differs from last decision, save new decision rationale, not silent drift.

## Required artifacts

- Session checkpoint in final report
- `research/decisions/D-....md` if changing direction

## Acceptance checks

- No claim that unfinished background work completed itself.
- Latest persisted state takes precedence over previous chat recollection.

## Default handoff

Continue with `research-orchestrator` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
