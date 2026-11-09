---
name: literature-review
description: Find, verify, read and compare primary scientific literature with provenance and explicit search coverage. Use for state-of-the-art reviews and source-grounded claims.
---

# Literature Review

## Purpose

Produce a trustworthy, reproducible literature evidence set, not a polished list of unverified citations.

## Inputs

- Research question and domain, goal ID
- Search horizon and as-of cutoff; available libraries/search tools
- Existing evidence and prior search log

## Procedure

### 1. Plan search

Develop multiple keyword families, synonyms, foundational and closest-method queries, reverse/forward citation searches when available. Record cutoff, databases and queries.

### 2. Retrieve and verify

Prefer primary publications and official proceedings/arXiv/preprints. Check title, author, year, venue and persistent URL/DOI against actual retrieved content. Do not invent missing fields.

### 3. Read method and limitations

Record exact claim, task, baseline, metric, sample/evaluation design, conditions and reported limitations. Mark abstract-only review explicitly.

### 4. Contrast research

Group papers by claim and mechanism; flag contradictory results, unresolved comparisons, weak baselines and negative findings.

### 5. Save provenance

Create source-level `E-....md` records with source_ref, verification status and precise sections/pages where available. Log queries and whether full text was accessed.

### 6. Handoff

Deliver verified reading list and unresolved coverage gaps to `research-landscape`, `novelty-audit`, or `critical-review`.

## Required artifacts

- `research/evidence/E-....md` source records
- `research/literature/<goal-id>-search-log.md`
- `research/literature/<goal-id>-review.md`

## Acceptance checks

- Every externally derived factual claim has a traceable source.
- No novelty claim from failed search alone; no fabricated DOI.
- Publication cutoff and incomplete retrieval are explicit.

## Default handoff

Continue with `research-landscape` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
