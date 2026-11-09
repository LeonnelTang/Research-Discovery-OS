# RDOS Architecture — Codex-Native Edition

**Status:** v0.2 proposed baseline. Supersedes any design requiring a standalone LLM API agent runtime.

## 1. Architectural decision

RDOS runs **inside a Codex workspace**. Codex is the sole AI research executor: it reads repository instructions and skills, researches via available authorized tools, writes code, runs local utilities, and updates persistent research artifacts. RDOS itself makes **no LLM API calls** and operates without a permanent backend service.

```text
Human research objective
          │
          ▼
    Codex session  ──► relevant .agents/skills/* procedures
          │
          ▼
  RDOS local toolchain (validators / scripts / experiments)
          │
          ▼
  Persistent repository research records + Git history
          │
          └──► next session reloads goal, evidence, decisions
```

Codex session termination stops the AI work unless the user has explicitly arranged a supported automation. Files survive; an autonomous process does not.

## 2. Components and boundaries

| Component | Responsibility | Phase 0 implementation |
|---|---|---|
| Codex | Research planning, tool selection, writing, critique, implementation | Interactive Codex session |
| Research skills | Stepwise procedures and output contracts | `.agents/skills/*/SKILL.md` |
| Research memory | Stable research objects, provenance and decisions | Versioned Markdown with YAML front matter |
| Local state tools | Enforce required fields and transitions | Small Python CLI (later milestone) |
| Experiment harness | Reproducible runs and artifacts | Python scripts + versioned manifests (later milestone) |
| Evaluation | Test scientific strategy and system reliability | Offline fixtures, tests and benchmarks (later milestone) |

No FastAPI, persistent worker daemon, Redis, PostgreSQL, external LLM SDK, or dedicated agent framework is required for the MVP. SQLite may be added later as an index **derived from files**, not as a competing source of truth.

## 3. Domain objects and identifiers

Records use UTF-8 Markdown with YAML front matter initially; machine-readable structured alternatives may be introduced without invalidating IDs.

| Type | Prefix | Location | Minimum fields |
|---|---|---|---|
| ResearchGoal | `G-` | `research/goals/` | `id,title,status,question,success_criteria,constraints` |
| Hypothesis | `H-` | `research/hypotheses/` | `id,goal_id,version,status,claim,assumptions,predictions,falsifiers` |
| Evidence | `E-` | `research/evidence/` | `id,source_type,source_ref,verification_status,observation` |
| Experiment | `X-` | `research/experiments/` | `id,hypothesis_ids,status,protocol,primary_metric,controls,budget` |
| ResearchDecision | `D-` | `research/decisions/` | `id,goal_id,options,selected,rationale,next_action` |

A ResearchProcess in the original API-oriented design becomes a **research project folder and decision history**, not a background worker. KnowledgeClaims can be represented in evidence records and explicit claim links in the MVP; standalone claim records may be added when evidence graph complexity justifies them.

Each record includes `created_at` in ISO 8601 with timezone, provenance where applicable, and links to related IDs. Never silently reuse an identifier. Changes to important interpretations create a new version with `supersedes` or an append-only update log; Git history is a supplementary audit trail, not the sole provenance mechanism.

## 4. Trust and authority

- **Codex drafts** hypotheses, interpretations, experiment plans and narrative.
- **Deterministic scripts** validate schema, links, statuses, hashes, experiment invariants and local records.
- **Source artifacts** (paper excerpts, PDFs, datasets, logs) are untrusted until verified.
- **Researcher** approves expensive, destructive or externally consequential operations.
- **Scientific findings** require traceable evidence; an LLM conclusion cannot validate itself.

Do not confuse an agent's confident statement, an experiment's execution success, a scientific result, and a generalizable conclusion.

## 5. Research workflow contract

### 5.1 Goal framing

Define the question, why it matters, resources, scope, completion criteria and any publication cutoff. Save a goal artifact before significant long-form research.

### 5.2 Literature and evidence

Record primary sources with reliable identifiers when verified, retrieval date, exact claim and limitations. Separate **source says X** from **X is experimentally supported**. Preserve conflicting evidence and unknowns.

### 5.3 Hypothesis search

Use independent strategies: inversion, failure analysis, abstraction, transfer, simplification and competing mechanisms. Every shortlisted hypothesis must include falsifiers, predicted observations, closest verified work, counterarguments and a minimum discriminating test. Novelty must be marked `unverified` until checked against appropriate prior work.

### 5.4 Experiment and feedback

Write a plan **before** execution: code revision, input data, baseline, controls, primary metric, success/failure criterion, seeds, budget and safety constraints. Store each attempt separately. Save raw results; analyses may be revised without overwriting raw files. Update evidence, hypothesis evaluation and research decision history accordingly.

### 5.5 Session restart

Read goal, latest decision, active hypotheses and evidence status. Summarize outstanding uncertainty, choose the next bounded action, and resume from disk rather than depending on hidden conversation context.

## 6. Hypothesis semantics

Operational lifecycle:

```text
PROPOSED → GROUNDED → TESTABLE → QUEUED → TESTING → EVALUATED
```

Evaluation dispositions after evaluation: `SUPPORTED`, `REFUTED`, `INCONCLUSIVE`, `SUPERSEDED`; these must be scoped to a given experiment and conditions. A hypothesis can be reopened by a **new version** with explicit lineage.

Transition guards:

- `GROUNDED`: closest related literature reviewed; provenance or explicit verification gaps recorded.
- `TESTABLE`: nonempty assumptions, observable predictions, falsifiers, controlled experiment proposal.
- `QUEUED`: frozen experiment plan with budget and permissions.
- `TESTING`: authorized execution attempt linked to the plan.
- `EVALUATED`: results inspected and evidence record linked; status disposition documented.

Until local validation scripts are implemented, Codex must not claim a machine-enforced transition occurred.

## 7. Experiments and provenance

Every experiment has a stable ID, immutable per-run directory, and links to hypothesis IDs. Each run records: code revision, input files or hashes, environment/dependencies, commands, seeds, budget, exit status, stdout/stderr or appropriate log references, metrics and scientific interpretation. Record failures without discarding attempts.

Generated code must not run with unrestricted filesystem, network or privilege access. Run only with appropriate authorization and resource limits. Avoid touching private data or third-party services unless explicitly approved.

## 8. Research Taste feedback

Store decisions along with options considered, expected value, uncertainties, selected action, cost estimate and observed outcomes. Evaluate research quality using verified discoveries per fixed budget, calibration, novelty audit accuracy, reproducibility and information gained from experiments. Do not treat language-model preferences or citation counts as ground truth scientific value.

Do not fine-tune models or add a learning service in the MVP. First collect well-formed trajectories and demonstrate a complete research loop.

## 9. Proposed future Python CLI

CLI is a planned local tool, not yet implemented in this scaffold:

```text
rdos validate [path]
rdos new goal|hypothesis|evidence|experiment|decision
rdos transition H-0001 --to TESTABLE
rdos links check
rdos experiment verify X-0001
rdos summary G-0001
```

Commands must validate input before writing and use atomic file replace or append semantics for persistent records. An index can be rebuilt from repository files. Hard-to-reverse format changes should be recorded as ADRs.

## 10. MVP phases

0. **Documentation and one skill:** architecture, agent instructions, hypothesis-discovery workflow, templates.
1. **Local memory validation:** schema/links validator, stable ID creation, reproducible tests.
2. **Research loop:** evidence intake, hypothesis revisions, decision trail, human-reviewed experiment plan.
3. **Experiment harness:** controlled runner, manifests, artifact integrity and reproducibility.
4. **Research Taste evaluation:** compare hypothesis exploration and experiment selection strategies at equal budgets.

## 11. Acceptance conditions for initial release

A user can start Codex in the repository, select a goal, invoke hypothesis discovery, inspect trustworthy source references, obtain competing falsifiable hypotheses, choose and document the next experiment, and resume later using versioned artifacts. No separate model API keys or always-on RDOS service are required.

**North star:** Codex acts; structured research records persist; deterministic tools check; evidence revises beliefs.
