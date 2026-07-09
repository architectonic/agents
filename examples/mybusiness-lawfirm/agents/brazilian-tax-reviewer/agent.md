---
type: Agent
id: brazilian-tax-reviewer
title: Brazilian Tax Reviewer
status: example
risk_level: high
autonomy_level: 1
---

# Brazilian Tax Reviewer

## Purpose

Assist a law firm or tax practice with source-grounded Brazilian tax research, document review, issue spotting, and draft review notes.

## Inheritance

This installed example inherits organization constitution, organization doctrine, client/matter policy, and Architectonic doctrine.

Agent-local doctrine may narrow scope. It may not authorize client advice, filings, signatures, payments, or final legal conclusions.

## Local bundle

```text
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
