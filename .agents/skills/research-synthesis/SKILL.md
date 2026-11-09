---
name: research-synthesis
description: Synthesize a goal-level research dossier from verified evidence, hypotheses, experiments and decisions with clear supported and unresolved claims. Use for reviews and progress reports.
---

# Research Synthesis

## Purpose

Create an auditable current scientific picture rather than smoothing away contradictions.

## Inputs

- Goal, hypotheses, evidence, findings and decisions
- Audience and report cutoff

## Procedure

### 1. Load record graph

Read goal and relevant artifacts; prioritize latest decisions and include dissenting evidence.

### 2. Separate status tiers

List established observations, provisional conclusions, contested claims and untested ideas separately.

### 3. Trace each conclusion

Cite evidence IDs and source locations; avoid inventing missing support.

### 4. Explain evolution

Describe how hypotheses and experiment results changed direction, including failed branches.

### 5. Summarize next decisions

Recommend bounded next actions with uncertainties, dependencies and cost.

### 6. Save dossier

Write dated goal-level synthesis, including sources inspected, limitations and reproduction links.

## Required artifacts

- `research/reports/<goal-id>-<date>-dossier.md`
- Optional project status summary

## Acceptance checks

- Every factual conclusion traces to a record.
- Negative and inconclusive findings remain visible.

## Default handoff

Continue with `research-retrospective` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
