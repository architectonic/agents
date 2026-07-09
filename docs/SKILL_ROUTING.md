---
type: Design Note
title: Agent Skill Routing
description: Skill bundle selection rules for Architectonic agent archetypes.
tags: [agents, skills, routing, provenance]
okf_version: "0.1"
status: draft
---

# Agent Skill Routing

This pass pins only source-backed canonical skills from `architectonic/skills`.

The `skills` distribution currently exposes a large catalog through `dist/catalog.json` and declares `dist/skills` as the install root. Dist-only slugs are useful for discovery, but this pass avoids pinning a skill unless a canonical source file under `skills/` was verified.

## Source reference

```text
architectonic/skills@9e4b87b90e83d04728e822ff82d56ccf53a195f4
```

## Core mapped skills

| Skill | Canonical path | Primary use |
|---|---|---|
| `source-review` | `skills/source-review.md` | source-first evidence discipline |
| `intent-to-contract` | `skills/intent-to-contract.md` | convert informal requests into bounded work contracts |
| `assumption-grilling` | `skills/assumption-grilling.md` | expose assumptions, missing evidence, and falsification criteria |
| `validation-gated-skill-improvement` | `skills/validation-gated-skill-improvement.md` | bounded self-improvement with validation and rollback evidence |
| `mission-grounded-learning-workspace` | `skills/mission-grounded-learning-workspace.md` | learner mission, source-aware teaching loop, practice artifacts |
| `shared-skill-library-governance` | `skills/shared-skill-library-governance.md` | canonical skill pool, named collections, runtime exposure, provenance |
| `mcp-external-tool-security-review` | `skills/mcp-external-tool-security-review.md` | external tool, MCP, prompt-injection, permissions, and state-mutation review |

## Archetype mapping

| Agent | Skills |
|---|---|
| `coder` | `intent-to-contract`, `source-review`, `assumption-grilling`, `validation-gated-skill-improvement` |
| `operator` | `source-review`, `intent-to-contract`, `assumption-grilling`, `validation-gated-skill-improvement`, `shared-skill-library-governance` |
| `legal-reviewer` | `source-review`, `assumption-grilling`, `intent-to-contract`, `mcp-external-tool-security-review` |
| `teacher` | `mission-grounded-learning-workspace`, `source-review`, `intent-to-contract`, `assumption-grilling` |
| `trader-analyst` | `source-review`, `assumption-grilling`, `intent-to-contract`, `mcp-external-tool-security-review` |

## Selection rules

1. Every agent that interprets external sources gets `source-review`.
2. Every agent that receives vague human intent gets `intent-to-contract`.
3. Every reviewer/analyst gets `assumption-grilling`.
4. Agents that modify reusable future behavior get `validation-gated-skill-improvement`.
5. Agents maintaining skill collections get `shared-skill-library-governance`.
6. Agents that may touch external tools, accounts, client data, broker data, or MCP-like connectors get `mcp-external-tool-security-review`.
7. Teaching agents get `mission-grounded-learning-workspace` instead of generic teaching advice.

## Deferred

The dist catalog contains many domain-specific candidates, including software-engineering, security, business, design, research, and media entries. They should be promoted into agent bundles only when the canonical source path and risk metadata are verified, or when the installer learns how to resolve dist slugs into generated skill copies with provenance.
