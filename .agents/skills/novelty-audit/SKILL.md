---
name: novelty-audit
description: Adversarially audit a research hypothesis against the closest verified prior art and determine precisely what remains unverified. Use before claiming novelty or writing a proposal.
---

# Novelty Audit

## Purpose

Attack a novelty claim with primary evidence and produce a defensible difference statement.

## Inputs

- Hypothesis ID and proposed novelty statement
- Existing sources, search log, target date cutoff

## Procedure

### 1. Decompose contribution

List each claimed new mechanism, assumption, training signal, setting, metric, and empirical outcome separately.

### 2. Search nearest neighbors

Find same-function methods, synonyms, equivalent formulations, earlier workshops/preprints, and closely related implementations.

### 3. Compare point by point

Create closest-work matrix with exact overlapping and differing elements. Inspect method sections, not just abstracts.

### 4. Try to invalidate novelty

For each claim, actively seek a prior counterexample; note evidence quality and full-text access.

### 5. Return verdict with scope

Choose `overlaps`, `partially_distinct`, or `unverified`; never declare exhaustive worldwide originality.

### 6. Update record

Amend hypothesis novelty status or add explicit audit summary and links without overwriting earlier assessments.

## Required artifacts

- `research/reviews/<hypothesis-id>-novelty.md`
- Updated hypothesis novelty notes or a revision record

## Acceptance checks

- Sources demonstrably retrieved and inspected, not invented.
- No novelty guarantee based on absence of hits.

## Default handoff

Continue with `critical-review` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
