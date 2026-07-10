---
type: Entry Point
title: agents
description: Runtime-neutral package for composing reusable agent definitions from identity, doctrine, skills, model policy, knowledge attachments, prompts, evaluations, and upkeep rules.
tags: [agents, identity, doctrine, skills, models, knowledge, meta, okf]
okf_version: "0.1"
status: draft
---

# agents

`agents` defines reusable structures for configuring software agents within an Architectonic system.

An agent is more than a prompt. A concrete agent configuration may include identity, scoped doctrine, selected skills, model policy, knowledge attachments, prompt surfaces, verification gates, permissions, and upkeep rules.

## Core distinction

```text
archetype        reusable public pattern
installed agent  initialized local configuration inside an organization, project, or workspace
runtime agent    executing session with tools, logs, memory, and permissions
```

`architectonic/agents` contains public-safe archetypes, schemas, templates, examples, and installation contracts. A concrete organization may instantiate private agents with organization rules, project scope, private knowledge bases, and domain-specific material.

## Installed agent minimum

A minimal instance may contain:

```text
agent.md
identity.md
doctrine.md
skills.json
models.json
knowledge-sets.json
prompts/system.md
prompts/task.md
evals.md
upkeep.md
```

Not every file is mandatory in every implementation. Separate files should exist only when they preserve a meaningful boundary or are maintained independently.

## Layering rule

```text
general doctrine
  -> organization rules
    -> project or client rules
      -> agent-specific constraints
        -> task instructions
```

More specific layers may narrow or specialize broader layers within their delegated authority. Conflicts should be surfaced rather than silently resolved in favor of the most local instruction.

## Skill rule

Installed agents may copy or vendor skills from `architectonic/skills`. Copied material should preserve recoverable provenance: source repository, path, ref or commit SHA, destination path, and local modification status.

## Knowledge rule

Agents attach to knowledge sources; they do not become the canonical owner of every corpus they can access. Each attachment should define scope, privacy, freshness, authority, and review expectations.

## Model rule

Model selection is an implementation policy, not an identity trait. Agent definitions should describe capability requirements, cost or latency constraints, fallback behavior, and verification needs without claiming that one model is universally best.

## Relationship to the stack

```text
doctrine   = principles and boundaries
identity   = actor, role, authority, privacy, and delegation
project    = operating context
skills     = reusable procedures
models     = evidence-backed model selection policy
knowledge  = attached claims, sources, and evidence
meta       = maintenance and revision policy
agents     = composition of these concerns for a concrete software actor
```

## Boundary

This public repository should not contain personal profiles, client data, private prompts, credentials, runtime logs, or project-specific operational state.

## Status

Draft. Not yet wired into `npx architectonic add agents`.
