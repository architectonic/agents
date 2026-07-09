# AGENTS.md

This repository defines the Architectonic `agents` package.

## Rules

- Treat public archetypes as factories, not private instances.
- Treat installed agents as thick local bundles: identity, doctrine, skills, models, knowledge attachments, prompts, evals, and upkeep.
- Agent-local doctrine may narrow but not weaken organization or constitution doctrine.
- Preserve provenance for all pinned or vendored skills.
- Do not store private client files, secrets, confidential org doctrine, or private user profiles in this public repo.
- High-stakes archetypes default to low autonomy.

## Validation

Run:

```bash
python scripts/validate_agents_package.py
```
