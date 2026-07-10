---
type: Entry Point
title: agents
description: Runtime-neutral package for composing software agents from identity, doctrine, skills, model policy, knowledge attachments, prompts, evaluations, permissions, and upkeep rules.
tags: [agents, identity, doctrine, skills, models, knowledge, meta, okf]
okf_version: "0.2"
status: draft
---

# agents

```bash
npx architectonic add agents
```

`agents` defines reusable structures for configuring software agents within an Architectonic system.

An agent is a composed software actor. A concrete configuration may include identity, scoped doctrine, selected skills, model policy, knowledge attachments, prompt surfaces, verification gates, permissions, and upkeep rules.

## In the ensemble

```text
constitution      composition contract for the ensemble
doctrine          purpose, principles, ontology, epistemology, ethics, governance, incentives
identity          actors, roles, authority, delegation, incentives, privacy
project           operating-unit context, sources, decisions, risks, continuity
skills            reusable procedures, verification, failure handling
knowledge         claims, sources, evidence, uncertainty, known unknowns
models            model metadata, evaluations, capability requirements, routing policy
agents            software actors composed from identity, skills, models, knowledge, permissions
living-knowledge  optional: governed maintenance of frequently changing corpora
meta              audit, upkeep, drift review, revision policy
```

```text
archetype        reusable public pattern (this repository)
installed agent  initialized local configuration in a workspace
runtime agent    executing session with tools, logs, memory, permissions
```

This repository contains public-safe archetypes, schemas, templates, and installation contracts. Private agents are instantiated in organization, project, or user workspaces.

## Commands

```bash
npx architectonic add agents
npx architectonic add agents --source npm
npx architectonic init
npx architectonic list
npx architectonic doctor
```

CLI: https://github.com/architectonic/architectonic

## Minimal composition

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

## Skills, knowledge, models

- **Skills** — agents may copy or vendor skills from `architectonic/skills` with preserved provenance.
- **Knowledge** — agents attach to knowledge sources; they do not become the canonical owner of every corpus they can access.
- **Models** — model selection is implementation policy. Describe capability requirements, cost and latency constraints, and fallback behavior without treating one model as universally preferable.

## Boundary

This public repository should not contain personal profiles, client data, private prompts, credentials, runtime logs, or project-specific operational state.
