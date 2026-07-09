---
type: Design Note
title: Installed Agent Model
description: How public archetypes become local initialized organization agents.
tags: [agents, installation, factory, local-instance]
okf_version: "0.1"
status: draft
---

# Installed Agent Model

`architectonic/agents` is the factory starter kit.

A local workspace may instantiate agents as thick local bundles:

```text
MyBusiness/
  constitution/
  doctrine/
  skills/
  knowledge/
  projects/
  clients/
  agents/
    coder/
    brazilian-tax-reviewer/
    market-intel-analyst/
```

The installed agent is allowed to carry copied files because it must be usable without repeatedly consulting upstream packages at runtime.

The public package must still preserve upstream references and provenance so updates are reviewable instead of silent drift.

## Install-time expansion

An installer can expand `archetypes/legal-reviewer/agent.bundle.json` into:

```text
agents/brazilian-tax-reviewer/
  agent.md
  identity.md
  doctrine.md
  skills.json
  skills/
    source-review.md
    assumption-grilling.md
  models.json
  knowledge-sets.json
  prompts/system.md
  prompts/task.md
  evals.md
  upkeep.md
```

## Update behavior

- never overwrite local doctrine without review;
- never overwrite locally modified skills without diffing provenance;
- never attach a private knowledge base without explicit local configuration;
- never promote autonomy level without permission review.
