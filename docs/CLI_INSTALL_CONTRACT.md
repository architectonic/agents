---
type: Contract
title: Agent CLI Install Contract
description: Contract for expanding a public archetype and local install specification into a reviewable installed agent bundle.
tags: [agents, cli, install, archetype, specialization]
protocol_version: "0.2.0"
status: experimental
---

# Agent CLI Install Contract

The Architectonic CLI exposes installed-agent creation as an explicit operation separate from installing this package:

```bash
npx architectonic@latest agent create \
  --spec ./agents/examples/install-specs/brazilian-tax-reviewer.json \
  --output ./organization/agents/brazilian-tax-reviewer
```

The CLI delegates generation to this package's `scripts/instantiate_agent.py` reference implementation.

## Inputs

```text
archetype bundle         archetypes/<id>/agent.bundle.json
install specification    examples/install-specs/<id>.json or a local organization spec
optional specialization  specialization files selected by the specification
output path               controlled organization or project workspace
```

## Required output

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
manifest.json
```

## Expansion rules

1. Read the archetype bundle and explicit install specification.
2. Apply local identity, authority, doctrine, knowledge attachments, model constraints, and permitted overrides.
3. Preserve skill provenance and inherited doctrine.
4. Emit a manifest with source archetype, generated files, and review rules.
5. Refuse to overwrite an existing output unless `--force` is explicit.
6. Do not treat generation as runtime authorization.

## Current boundary

The generator creates a local, reviewable installed-agent bundle. Runtime credentials, actual tool permissions, private knowledge access, external execution, and autonomy changes remain separate actions governed by the host organization and runtime.

## Update rules

- never overwrite local doctrine without review;
- never overwrite locally modified skills without comparing provenance;
- never attach a private knowledge base without explicit local configuration;
- never increase autonomy or permissions without authority review.
