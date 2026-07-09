---
type: Contract
title: Agent CLI Install Contract
description: Contract for expanding archetype bundles and install specs into thick local installed agents.
tags: [agents, cli, install, archetype, specialization]
okf_version: "0.1"
status: draft
---

# Agent CLI Install Contract

This contract describes the future `npx architectonic add agents` expansion behavior.

The current repo provides a reference script:

```bash
python scripts/instantiate_agent.py \
  --spec examples/install-specs/brazilian-tax-reviewer.json \
  --output /tmp/brazilian-tax-reviewer
```

## Inputs

```text
archetype bundle        archetypes/<id>/agent.bundle.json
install spec            examples/install-specs/<id>.json or local org spec
optional specialization specializations/<id>/...
output path             local organization workspace path
```

## Output

Every expansion must produce:

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

1. Read the archetype bundle.
2. Apply install-spec local identity, authority, doctrine, knowledge attachments, and model overrides.
3. Preserve skill provenance from the archetype bundle.
4. Preserve inherited doctrine and make local doctrine subordinate.
5. Emit a manifest with source archetype, specializations, generated files, and update rules.
6. Refuse to overwrite an existing output unless `--force` is explicit.

## Non-goals

This does not yet:

- copy skill bodies into the installed agent;
- integrate with `architectonic` npm CLI;
- resolve dist-only skill slugs;
- implement runtime permissions;
- attach real private knowledge bases.

## Update rules

- Do not overwrite local doctrine without review.
- Do not overwrite locally modified skills without diffing provenance.
- Do not attach private knowledge bases without explicit local configuration.
- Do not increase autonomy without permission review.
