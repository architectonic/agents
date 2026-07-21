# Loop Engineering for Agents

Use a loop only when work must recur across runs, schedules, workers, or handoffs.

## Required contract

```text
bounded objective and value hypothesis
trigger or schedule
durable state outside model context
work selection and claim rule
worker and verifier
approved skills and tools
cost, token, time, and spawn budgets
mutation, privacy, and external-effect boundary
human approval and kill authority
run evidence
stop and retirement conditions
```

## Parallel work

Parallel agents require isolation, ownership, and reconciliation. Use separate branches, worktrees, tickets, leases, or artifact claims where appropriate. Do not let several agents silently mutate the same canonical file.

## Knowledge boundary

A run output is not automatically knowledge. Promote claims only after source, evidence, uncertainty, and review requirements are met.

## Workframe

Workframe may execute loops as governed runs, leases, approvals, and ledger entries. The agent package remains runtime-neutral; another scheduler or direct human supervision may implement the same contracts.
