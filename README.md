---
type: Entry Point
title: agents
description: Runtime-neutral Architectonic package for composing specialized agent bundles from identity, doctrine, skills, models, knowledge, prompts, and upkeep policy.
tags: [agents, identity, skills, models, knowledge, doctrine, meta, okf]
okf_version: "0.1"
status: draft
---

# agents

`agents` is the Architectonic package for reusable agent bundles.

An agent is not just a prompt. An agent is a composable operating identity that can be instantiated inside an organization, project, workspace, or public product surface.

Install target, when wired into the CLI:

```bash
npx architectonic add agents
```

## Core definition

```text
Agent =
  identity
+ role and authority contract
+ agent-local doctrine
+ inherited organization doctrine
+ skill bundle
+ model routing policy
+ knowledge-set attachments
+ prompt surfaces
+ tools and permission policy
+ verification gates
+ upkeep policy
```

## Important distinction

This package contains reusable archetypes, schemas, templates, examples, and public-safe starter specializations.

A concrete organization may instantiate its own agents with private doctrine, private knowledge bases, client/project scopes, and jurisdiction/domain-specific corpora.

Example:

```text
MyBusiness/
  constitution/
  doctrine/                 # organization doctrine
  skills/                   # organization skill overrides/additions
  knowledge/                # organization knowledge corpus
  agents/
    tax-reviewer-br/         # local specialized agent instance
      agent.md
      identity.md
      doctrine.md            # agent-local doctrine
      skills.json
      models.json
      prompts/
      knowledge-sets.json    # attaches to org/client/legal corpora
```

The public archetype stays reusable. The local instance carries the specific professional posture, org constraints, client/project scope, and knowledge attachments.

## Relationship to Architectonic layers

```text
constitution      = root scaffold / bundle contract
doctrine          = upstream and organization governing principles
identity          = actor, role, authority, privacy, delegation
skills            = reusable procedures
models            = model routing and trust tiers
knowledge         = reviewed claims, sources, evidence, uncertainty
living-knowledge  = optional governed upkeep for dynamic corpora
meta              = drift detection, audits, recursive improvement
agents            = composition layer for reusable and local agent identities
```

## What belongs here

```text
public-safe agent archetypes
agent schemas and templates
composition rules
model/skill/knowledge attachment contracts
safety and high-stakes boundaries
dist catalogs and install manifests
example bundles without private data
operator state for maintaining the package
```

## What does not belong here

```text
private client files
private user profiles
confidential organization doctrine
full copies of legal, medical, financial, or proprietary corpora
runtime secrets
unreviewed autonomous action policies
claims that a high-stakes agent is a licensed professional
```

## First value path

```text
agents-bootstrap-package-001
-> agents-schema-and-contract-001
-> agents-core-archetypes-seed-001
-> agents-local-specialization-contract-001
-> agents-knowledge-set-attachment-policy-001
-> agents-model-policy-wiring-001
-> agents-dist-catalog-001
```

## Status

Draft bootstrap. The package currently defines the contract and seed archetypes; it does not yet publish an npm package or integrate with `architectonic add agents`.
