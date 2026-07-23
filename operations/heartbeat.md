# Agents Heartbeat

The agents package follows Rail-bound operation.

## Loop

1. Fetch exact default-branch state.
2. Read `operations/ledger.json`, `operations/gates.md`, and the selected item's sources.
3. Take the human-assigned item or select exactly one dependency-clear ready item.
4. Produce an artifact or record a concrete blocker with evidence.
5. Run validation.
6. Update only `operations/ledger.json` when coordination survives the run.

`operations/value-ledger.json` is qualified outcome history. It is not read for work selection and is updated only when a completed outcome has distinct value worth preserving.

## Current mission

Build a useful agent factory starter kit that produces thick local installed agents, not thin prompt references.
