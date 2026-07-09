---
type: Contract
title: Agent Contract
description: Contract for thick Architectonic agent bundles.
tags: [agents, contract, identity, doctrine, skills, knowledge, models]
okf_version: "0.1"
status: draft
---

# Agent Contract

An Architectonic agent is a local operating identity, not a prompt.

## Installed-agent minimum

Every installed agent must carry:

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

## Doctrine layering

```text
Architectonic doctrine
  < organization doctrine
    < project/client doctrine
      < agent-local doctrine
        < task instructions
```

Lower layers may narrow or specialize higher layers. They must not contradict, bypass, or weaken them.

## Skill handling

Installed agents may vendor/copy skills from `architectonic/skills`, but every copied skill must preserve provenance:

```json
{
  "id": "source-review",
  "source_repo": "architectonic/skills",
  "source_path": "skills/source-review.md",
  "source_ref": "051df1294ec1264d8f34237a9a630ebd755e33ba",
  "copied_path": "skills/source-review.md",
  "local_modifications": false,
  "review_required_before_update": true
}
```

## Knowledge handling

Agents attach to knowledge bases. They do not own every corpus they use. Attachments must declare scope, access mode, privacy, freshness, and review requirements.

## Autonomy levels

```text
0 prompt-only
1 assisted
2 tool-using
3 repo-operator
4 supervised external actor
5 autonomous actor
```

High-stakes agents default to levels 0-2 unless explicit permissions, audit, rollback, and human approval paths exist.
