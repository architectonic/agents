---
type: Entry Point
title: agents
description: Runtime-neutral package for composing software agents from identity, doctrine, skills, model policy, knowledge attachments, prompts, evaluations, permissions, and upkeep rules.
tags: [agents, identity, doctrine, skills, models, knowledge, meta, okf]
okf_version: "0.2"
status: draft
---

# agents

`agents` defines reusable structures for configuring software agents within an Architectonic system.

Install it with:

```bash
npx architectonic add agents
```

An agent is a composed software actor. A concrete configuration may include identity, scoped doctrine, selected skills, model policy, knowledge attachments, prompt surfaces, verification gates, permissions, and upkeep rules.

## Core distinction

```text
archetype        reusable public pattern
installed agent  initialized local configuration inside an organization, project, or workspace
runtime agent    executing session with tools, logs, memory, and permissions
```

This repository contains public-safe archetypes, schemas, templates, examples, and installation contracts. Private agents are instantiated in organization, project, or user workspaces.

## Minimal composition

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

Separate files should exist only when they preserve a meaningful boundary or are maintained independently.

## Layering

```text
general doctrine
  -> organization rules
    -> project or client rules
      -> agent-specific constraints
        -> task instructions
```

More specific layers may narrow broader layers within delegated authority. Conflicts should be surfaced rather than silently resolved in favor of the most local instruction.

## Skills

Installed agents may copy or vendor skills from `architectonic/skills`. Copied material should preserve source repository, path, ref or commit SHA, destination path, and local modification status.

## Knowledge

Agents attach to knowledge sources; they do not become the canonical owner of every corpus they can access. Each attachment should define scope, privacy, freshness, authority, and review expectations.

## Models

Model selection is an implementation policy rather than an identity trait. Agent definitions should describe capability requirements, cost and latency constraints, fallback behavior, and verification needs without treating one model as universally preferable.

## Relationship to the ensemble

```text
constitution      = composes the ensemble
doctrine          = principles and boundaries
identity          = actor, role, authority, privacy, incentives, and delegation
project           = operating context
skills            = reusable procedures and verification
knowledge         = attached claims, sources, evidence, uncertainty, and gaps
models            = evidence-backed capability and routing policy
agents            = composition of these concerns for a software actor
living-knowledge  = maintenance of changing attached corpora
meta              = audit, upkeep, and revision policy
```

## Boundary

This public repository should not contain personal profiles, client data, private prompts, credentials, runtime logs, or project-specific operational state.

## Status

Draft package included in the Architectonic ensemble.