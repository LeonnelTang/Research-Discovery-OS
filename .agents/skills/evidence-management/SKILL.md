---
name: evidence-management
description: Maintain provenance-aware scientific evidence records, contradictions, source verification status and updates to hypothesis support. Use whenever integrating findings.
---

# Evidence Management

## Purpose

Keep research knowledge accurate and reconstructible despite revisions, invalidated evidence and conflicting results.

## Inputs

- Raw source artifact or validated experiment output
- Existing claims, hypotheses and evidence
- Citation/provenance information

## Procedure

### 1. Classify input

Distinguish paper-reported claim, direct observation, simulation output, reasoning and speculation.

### 2. Verify provenance

Capture source identifier, specific section or artifact path, verification method and access limitations.

### 3. Register evidence

Create stable evidence record with source_ref, verification_status, observation and relevant conditions.

### 4. Link and qualify

Record what it supports, contradicts or qualifies, and any untested mechanism or alternative interpretation.

### 5. Handle corrections append-only

Invalidate/supersede records with reason, rather than silently deleting negative evidence.

### 6. Check consistency

Run available local validators and reconcile dangling links; report unresolved conflicts.

## Required artifacts

- `research/evidence/E-....md`
- Provenance/contradiction links in related hypotheses
- Decision record when belief shifts materially

## Acceptance checks

- Source text/report is not equated to verified truth.
- Corrections preserve original evidence ID and history.

## Default handoff

Continue with `research-synthesis` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
