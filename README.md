# Research Discovery OS (RDOS)

**A Codex-native workspace for evidence-driven scientific discovery.**

RDOS helps turn a research goal into verifiable literature maps, competing falsifiable hypotheses, discriminating experiments and an auditable record of what was learned. **Codex is the only AI execution agent** in the default architecture; RDOS does not call an LLM API or maintain a separate always-on agent service.

## Why this exists

Good research is not simply idea generation. It requires tracking uncertainty, identifying important scientific gaps, testing competing explanations and revising beliefs when evidence changes. RDOS provides a durable structure for that process, so each Codex session can resume from explicit files rather than hidden chat history.

## How it works

1. Open this repository in Codex.
2. Ask Codex to read `AGENTS.md`, `docs/ARCHITECTURE.md` and the appropriate skill.
3. Define a research goal in `research/goals/`.
4. Use the [16-skill catalogue](.agents/skills/README.md), starting with `research-orchestrator` or `hypothesis-discovery`, to move from verified sources through experiments and research retrospectives.
5. Preserve sources, hypotheses, decisions and experiment results in `research/`.
6. Resume in a future Codex session by reading the saved research state.

Example instruction:

> Read AGENTS.md and the hypothesis-discovery skill. Investigate event-triggered online learning under fixed update-compute budgets. Verify nearest prior work, propose three competing falsifiable hypotheses, choose the cheapest discriminating experiment and save the research artifacts. Do not execute costly experiments without asking.

## Architecture

```text
Researcher → Codex + Skills → Local scripts and authorized tools → Versioned research files
```

See `docs/ARCHITECTURE.md` for object contracts and lifecycle rules, and `docs/ROADMAP.md` for planned implementation stages.

## Project status

**Phase 0: complete skill catalogue and local validation tooling.** Research Skills, templates and offline skill/record validators are present. A sandboxed experiment runner and empirical Research Taste evaluation remain future work.

## Design principles

- No independent model API calls, API keys or custom LLM-agent scheduler.
- Persistent files and Git as the initial source of truth.
- Explicit provenance, uncertainty and negative evidence.
- Falsifiable hypotheses and precommitted experiment criteria.
- Deterministic validation scripts before automation.
- Human approval for expensive or high-impact actions.

## Research directions

First domain: machine learning research, including online adaptation, continual learning, world models and research agent architectures. The process is designed to generalize beyond this domain.

## License

To be determined.

## Skill catalogue and local checks

See [`.agents/skills/README.md`](.agents/skills/README.md) for all research procedures and their handoffs. To verify repository instructions and records without any model API:

```bash
python scripts/validate_skills.py
python scripts/validate_records.py
python -m unittest discover -s tests -v
```
