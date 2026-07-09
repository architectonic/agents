# Agents Heartbeat

The agents package follows board-first operation.

## Loop

1. Fetch exact default-branch state.
2. Read `operations/board.json`, `operations/gates.md`, `operations/value-ledger.json`, today's daily state, and relevant ticket inputs.
3. Select exactly one ready ticket.
4. Produce an artifact or block/kill the ticket with evidence.
5. Run validation.
6. Update board, ledger, daily state, and log.

## Current mission

Build a useful agent factory starter kit that produces thick local installed agents, not thin prompt references.
