# Agents

**Architectonic layer:** [main CLI and adaptive profiles](https://github.com/architectonic/architectonic)

> **Status: experimental, pre-1.0.** This package defines public agent archetypes and installation contracts. It does not create runtime authority, prove autonomy, attach private knowledge, or authorize external effects.

```text
public archetype  reusable pattern in this package
installed agent   local files specialized for one workspace
runtime agent     executing process with tools, state, permissions, and evidence
```

The package may be inspected or installed alone as an archetype library:

```bash
npx architectonic@latest add agents --source npm
```

Use the `agent-team` profile when operational agents also need identity, reviewed skills, knowledge attachments, model policy, Rail, and upkeep:

```bash
npx architectonic@latest init my-team --preset agent-team --source npm
```

An installed agent has no authority merely because its files exist. Local configuration must define the human owner, purpose, skills, knowledge, model policy, permissions, budgets, review gates, escalation, and stopping rights.

Recurring agents should use bounded loop engineering rather than “run forever” prompts. When durable work crosses a session, role, dependency, review, or approval boundary, agents consume the one ledger named by [Architectonic Rail](https://github.com/architectonic/rail). Agent-local boards, queues, daily status files, and handoff ledgers must not become competing work authorities.

See [`docs/LOOP_ENGINEERING.md`](./docs/LOOP_ENGINEERING.md).
