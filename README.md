# Agents

> **Status: experimental, pre-1.0.** This package defines agent composition and installation contracts. It does not create runtime authority merely by being installed.

An Architectonic agent is a composed software actor with explicit identity, scoped doctrine, selected skills, model policy, knowledge attachments, prompts, evaluations, permissions, and upkeep rules.

## Three distinct objects

```text
public archetype  reusable pattern published by this package
installed agent   local initialized bundle inside an organization or project
runtime agent     executing session with tools, credentials, logs, and permissions
```

Installing the `agents` layer installs public archetypes, schemas, templates, validators, and the reference generator. Creating an installed agent is a separate explicit action:

```bash
npx architectonic@latest agent create \
  --spec ./agents/examples/install-specs/brazilian-tax-reviewer.json \
  --output ./organization/agents/brazilian-tax-reviewer
```

## Composition order

```text
general doctrine
  -> organization rules
    -> project or client rules
      -> agent-specific constraints
        -> task instructions
```

More specific layers may narrow broader layers only within delegated authority. Conflicts are surfaced rather than silently resolved.

## Safety rules

- preserve skill provenance;
- never overwrite local doctrine without review;
- never attach private knowledge without explicit local configuration;
- never increase autonomy or permissions without authority review;
- high-risk archetypes remain at bounded autonomy;
- installing a package is not granting runtime permission.
