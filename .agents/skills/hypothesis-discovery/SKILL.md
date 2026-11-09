---
name: hypothesis-discovery
description: Discover, critically review, and prioritize falsifiable scientific hypotheses with verified literature, competing mechanisms, and minimum discriminating experiments. Use for research ideation, novelty audits, gap analysis, and choosing the next research action in RDOS.
---

# Hypothesis Discovery — Codex Skill

## Purpose

Turn a research objective into a small, evidence-grounded portfolio of scientifically significant, explicitly testable hypotheses. **Never equate novelty of wording with novelty of scientific contribution.** This skill uses Codex directly; it requires no separate LLM API.

## Inputs

- `goal_id` and goal file in `research/goals/`, or a new user-provided research objective.
- Current research scope, publication cutoff (if relevant), resource/time budget.
- Existing hypotheses, evidence records and latest decision, if any.
- Available authorized research tools. If literature access is unavailable, explicitly flag unverified novelty and missing evidence rather than fabricating sources.

## Procedure

### 1. Load and clarify the research state

Read `AGENTS.md`, `docs/ARCHITECTURE.md`, goal and existing artifacts. Identify important question, success criteria, constraints and prior decisions. Avoid reopening settled work without new reason.

### 2. Build an evidence map

Search for foundational work, closest prior contributions, contradictory results, negative findings and recent developments (when authorized). Prioritize primary papers and original artifacts. For each source record title, authors, year, persistent URL/DOI when verified, the relevant claim, conditions, weaknesses and exact provenance. Distinguish *retrieved*, *read*, and *independently verified*. Maintain search queries and cutoff. Never fabricate references.

### 3. Identify gaps using distinct operators

Use at least three of:

- `INVERT`: Which assumption can be relaxed or reversed?
- `EXPLAIN_FAILURE`: What mechanism could explain a known failure?
- `ABSTRACT`: Is there a shared mechanism across seemingly different results?
- `TRANSFER`: Can a formal mechanism apply across domains?
- `SIMPLIFY`: Can fewer assumptions/components explain the results?
- `CONTRADICTION`: Which results disagree, and are conditions responsible?

Generate diverse mechanisms, not cosmetic variations.

### 4. Produce falsifiable candidate hypotheses

For each candidate capture:

1. Specific claim with scope and conditions.
2. Scientific significance: what knowledge changes if true?
3. Nearest prior work and precise proposed difference, or `novelty_unverified`.
4. Mechanistic explanation and explicit assumptions.
5. Observable predictions and competing hypotheses.
6. Strongest possible counterargument.
7. Minimal discriminating experiment with baselines, controls, primary metric, confounders and expected results under competing explanations.
8. Budget estimate, risks and clear falsification/stop criteria.

Prefer 3–5 strong candidates over 20 shallow ones unless the user requests a broad scan.

### 5. Perform adversarial novelty and feasibility review

Attempt to show every proposed idea is already known, internally inconsistent, non-causal, underdetermined or untestable. Look for the closest related work, not just generic background sources. Mark unverifiable statements explicitly. Never declare a new scientific contribution confirmed solely because a search returned no match.

### 6. Select the next information-rich action

Recommend a portfolio rather than one unqualified winner: (a) a near-term testable direction and (b) a high-risk/high-potential direction if justified. Choose the cheapest experiment or evidence lookup that can materially differentiate competing hypotheses. Explain the choice and what outcome would change it. Avoid arbitrary LLM scores masquerading as calibrated probabilities.

### 7. Persist artifacts

- Save an updated/new goal in `research/goals/` if needed.
- Save candidate hypotheses in `research/hypotheses/` following the architecture contract and `research/hypotheses/TEMPLATE.md`.
- Save verified source/evidence records in `research/evidence/` or mark them unverified.
- Save decision with alternatives, reasoning and next action in `research/decisions/`.
- Do **not** claim schema/state validation succeeded unless an actual validator was run.

## Mandatory output format

Finish with:

1. **Research question and boundaries**.
2. **Verified prior work and remaining search gaps**.
3. **Candidate comparison** — mechanism, precise novelty claim, counterargument, decisive experiment, feasibility.
4. **Recommendation** — top actionable hypothesis and one genuinely different alternative.
5. **Next action** — an executable test or targeted retrieval step with approximate cost.
6. **Artifacts written** — exact relative paths.
7. **Verification status** — what was actually looked up/read/run; sources of uncertainty.

## Failure and stop conditions

Stop and report the constraint if evidence cannot be accessed, a required experiment is unsafe or unauthorized, the goal is too underspecified to make scientifically meaningful predictions, or an idea has no falsifiable observation. It is acceptable to produce a rigorously labeled partial result instead of inventing certainty.

## Examples of bad behavior

- “This is the first work to...” without exhaustive defensible novelty evidence.
- A hypothesis that only says “combine Transformers and RL.”
- Changing the success metric after seeing results.
- Calling LLM agreement independent validation.
- Deleting failed directions because they clutter the project.

## Shared contracts and constraints

- Read repository `AGENTS.md`, `docs/ARCHITECTURE.md`, and `.agents/skills/README.md` as needed. Codex is the only AI executor; **do not call an LLM API, launch a separate agent framework, or imply unattended background work**.
- Reuse existing goal and entity IDs. Follow `research/*/TEMPLATE.md`; put verified outputs under `research/`, not solely in the conversation. When local validators exist, run them and report results; otherwise explicitly label records unvalidated.
- Use relative paths; preserve raw artifacts, rejected ideas, contradictory evidence and decision history. Avoid unapproved expensive execution, external side effects, destructive commands or credential disclosure.
- Separate **observed**, **source-reported**, **inferred**, **hypothesized**, and **not verified**. No source IDs, benchmark scores, experiments or quantitative evidence may be invented.
- End with: completed work; evidence actually inspected; artifacts and exact paths; checks actually run; unresolved risks; next bounded action.
