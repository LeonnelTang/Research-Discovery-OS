---
name: experiment-execution
description: Safely implement, execute and record reproducible computational experiments with immutable run artifacts. Use only after experiment design and approval.
---

# Experiment Execution

## Purpose

Produce inspectable raw experimental evidence, not just an LLM narrative of what supposedly happened.

## Inputs

- Approved experiment contract `X-...`
- Pinned code/data/environment and execution authorization
- Compute/time/storage caps

## Procedure

### 1. Check readiness

Read plan and approval, verify data rights, dependencies, baseline and resources. Do not run if essential constraints are missing.

### 2. Review generated code

Inspect for filesystem/network side effects, credentials, destructive commands and unsafe execution.

### 3. Prepare reproducible run

Record git revision or file hashes, environment, exact command, input hash, seed and timeout; prefer sandboxed execution.

### 4. Execute bounded attempts

Keep each run separate; enforce limits where supported. On interruption, record partial outputs and reason.

### 5. Capture raw artifacts

Save stdout/stderr, exit code, measurement files, environment details and artifact hashes without rewriting earlier runs.

### 6. Check execution integrity

Verify run status and input-output completeness; distinguish code failures from negative scientific results.

### 7. Handoff

Send raw run manifest to result-analysis; never upgrade hypothesis to SUPPORTED automatically.

## Required artifacts

- `research/experiments/runs/<experiment-id>/<run-id>/manifest.json`
- Raw metrics/logs/files from run
- Updated experiment status notes

## Acceptance checks

- Plan and approval verified before execution.
- Run manifest names actual code, data, environment, commands and exit status.
- Scientific conclusions reserved for subsequent analysis.

## Default handoff

Continue with `result-analysis` only when the handoff prerequisites are met. An explicit user instruction or a documented research blocker may override this path.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
