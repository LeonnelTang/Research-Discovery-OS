---
name: research-intake
description: Frame a research goal into a scoped project with explicit resources, success criteria, constraints, and uncertainty. Use when starting or changing a research topic.
---

# Research Intake

## Purpose

Convert an open-ended topic into an auditable research goal that can be resumed across Codex sessions.

## Inputs

- Researcher objective, known preferences and scientific scope
- Available time, compute, datasets, desired publication cutoff
- Existing goal and last decision, if continuing

## Procedure

### 1. Inspect existing state

Read repository instructions and goal/decision records. Search for a matching goal before creating one; do not overwrite another project.

### 2. Write the research question

Define population/system, intervention or mechanism, relevant outcomes, and the uncertainty to resolve; avoid deciding the conclusion in advance.

### 3. Bound the project

Record available tools, time, compute/budget caps, approval requirements, access restrictions, and out-of-scope work.

### 4. Define progress and stop conditions

Specify success as testable discoveries or decisions, not paper count. Include viable fallback scope and explicit pause criteria.

### 5. Save goal

Create/update `research/goals/G-....md` and record unresolved assumptions; choose a stable new ID using available local tooling.

### 6. Choose handoff

Route to `literature-review` then `research-landscape`, or to `research-resume` if context already exists.

## Required artifacts

- `research/goals/G-....md`
- `research/decisions/D-....md` when a consequential scope decision was made

## Acceptance checks

- Goal includes measurable success criteria, constraints, and realistic budget.
- No assumed access, benchmark data or resources presented as confirmed.

## Default handoff

Continue with `literature-review` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
