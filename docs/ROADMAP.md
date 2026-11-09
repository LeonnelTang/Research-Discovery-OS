# RDOS Roadmap — Codex-native

## Phase 0 — Documentation and complete skill catalogue (current)

- [x] Root instructions in `AGENTS.md`
- [x] Codex-native architecture in `docs/ARCHITECTURE.md`
- [x] 16 Codex-native research skills with shared handoff contracts
- [x] Offline skills and record structural validation scripts and tests
- [x] Human-readable templates for research artifacts
- [ ] Run one manual, source-verified research discovery session in Codex

**Acceptance:** A new Codex session can understand the project without reading prior chat and can prepare a falsifiable hypothesis portfolio with explicit evidence gaps.

## Phase 1 — Durable research state tools

- [x] Implement initial offline structural record validator (`scripts/validate_records.py`)
- [ ] Implement complete `rdos validate` for YAML schemas, cross-record references and provenance
- [ ] Implement stable ID allocation and collision handling
- [ ] Add explicit hypothesis state-transition validation
- [ ] Add deterministic offline unit tests and fixtures
- [ ] Document the record migration/versioning procedure

**Acceptance:** Invalid links, missing falsifiers and illegal transitions are rejected deterministically. No live LLM calls.

## Phase 2 — Evidence-driven research loop

- [ ] Verified literature ingestion workflows
- [ ] Evidence and contradiction linking
- [ ] Structured decision logging and novelty audit
- [ ] Resumable project summary based on repository records

**Acceptance:** One topic can be explored across separate Codex sessions without losing uncertainty or failure history.

## Phase 3 — Reproducible experiments

- [ ] Experiment plan validation and pre-registration
- [ ] Restricted execution entry point with budgets and approvals
- [ ] Immutable per-run manifests, hashes and logs
- [ ] Result interpretation separate from execution status

**Acceptance:** A small controlled experiment is rerunnable, and its outcomes trace to raw artifacts.

## Phase 4 — Research Taste evaluation

- [ ] Controlled scientific discovery tasks
- [ ] Comparable baseline research strategies
- [ ] Metrics for knowledge gain, cost and calibration
- [ ] Reproducible comparisons across unseen tasks

**Acceptance:** The effect of an RDOS workflow on research decision quality is measurable rather than asserted.

## Non-goals for current phases

Standalone model APIs, multi-agent orchestration framework, FastAPI server, PostgreSQL, background autonomous research, automatic submissions and uncontrolled cloud compute.
