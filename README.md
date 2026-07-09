---
type: Entry Point
title: agents
description: Runtime-neutral Architectonic package for composing thick installed agent bundles from identity, doctrine, pinned skills, models, knowledge attachments, prompts, evals, and upkeep policy.
tags: [agents, identity, doctrine, skills, models, knowledge, meta, okf]
okf_version: "0.1"
status: draft
---

# agents

`agents` is the Architectonic package for reusable agent factories and thick installed agent bundles.

An agent is not just a prompt. A useful installed agent carries initialized identity, agent-local doctrine, pinned or vendored skills, model policy, knowledge attachments, prompt surfaces, verification gates, and upkeep policy.

## Core distinction

```text
archetype        reusable public factory pattern
installed agent  initialized local worker inside an org/project/workspace
runtime agent    executing session with tools, logs, memory, and permissions
```

`architectonic/agents` contains public-safe archetypes, schemas, templates, examples, and install contracts. A concrete organization may instantiate private local agents with organization doctrine, client/project scope, private knowledge bases, and jurisdiction/domain corpora.

## Installed agent minimum

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

## Layering rule

```text
Architectonic doctrine
  < organization doctrine
    < project/client doctrine
      < agent-local doctrine
        < task instructions
```

Lower layers may narrow or specialize higher layers. They must not contradict, bypass, or weaken them.

## Skill rule

Installed agents may vendor/copy skills from `architectonic/skills`, but every copied skill must preserve provenance: source repo, path, ref/SHA, copied path, and local modification status.

## Knowledge rule

Agents attach to knowledge bases. They do not own every corpus they use. For example, a law firm can attach an agent to `knowledge/jurisdictions/br/tax-code`, `clients/<client>`, and `projects/<matter>` with scope, privacy, freshness, and review rules.

## First value path

```text
agents-bootstrap-package-001
-> agents-schema-and-contract-001
-> agents-core-archetypes-seed-001
-> agents-installed-template-001
-> agents-knowledge-set-attachment-policy-001
-> agents-dist-catalog-001
```

## Status

Draft bootstrap. Not yet wired into `npx architectonic add agents`.
