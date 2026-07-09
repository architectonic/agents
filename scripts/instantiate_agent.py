#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "agent.md",
    "identity.md",
    "doctrine.md",
    "skills.json",
    "models.json",
    "knowledge-sets.json",
    "prompts/system.md",
    "prompts/task.md",
    "evals.md",
    "upkeep.md",
    "manifest.json",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def as_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None declared."


def render_agent_md(spec: dict[str, Any], bundle: dict[str, Any]) -> str:
    return f'''---
type: Agent
id: {spec['agent_id']}
title: {spec['title']}
status: installed-template
risk_level: {bundle.get('risk_level', 'medium')}
autonomy_level: {spec.get('autonomy_level', bundle.get('autonomy_level', 1))}
---

# {spec['title']}

## Purpose

{spec.get('purpose') or bundle.get('identity', {}).get('purpose', 'Local installed agent purpose.')}

## Source archetype

```text
{bundle['id']}
```

## Specializations

```text
{', '.join(spec.get('specializations', [])) or 'none'}
```

## Inheritance

This installed agent inherits Architectonic doctrine, organization doctrine, and any project/client/matter policy declared by the local workspace.

Agent-local doctrine may narrow scope. It may not weaken higher doctrine, widen authority, or increase autonomy without review.

## Local bundle

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
'''


def render_identity_md(spec: dict[str, Any], bundle: dict[str, Any]) -> str:
    identity = bundle.get("identity", {})
    return f'''# Identity

## Role

{spec.get('role') or identity.get('role', 'Local installed agent.')}

## Purpose

{spec.get('purpose') or identity.get('purpose', 'Local installed agent purpose.')}

## Authority

{spec.get('authority') or identity.get('authority', 'Declare local authority before use.')}

## Privacy

{spec.get('privacy') or 'Use only knowledge attachments and workspace data allowed by local policy.'}

## Escalation

{spec.get('escalation') or identity.get('escalation', 'Escalate authority conflicts, sensitive data, external mutation, and high uncertainty.')}
'''


def render_doctrine_md(spec: dict[str, Any], bundle: dict[str, Any]) -> str:
    doctrine = bundle.get("doctrine", {})
    inherits = doctrine.get("inherits", [])
    local_rules = doctrine.get("local_rules", []) + spec.get("local_rules", [])
    forbidden = doctrine.get("forbidden", []) + spec.get("forbidden", [])
    return f'''# Agent-local Doctrine

This doctrine is subordinate to organization, project/client, and Architectonic doctrine.

## Inherits

{as_lines(inherits)}

## Local rules

{as_lines(local_rules)}

## Forbidden

{as_lines(forbidden)}

## Stop conditions

{as_lines(spec.get('stop_conditions', [
    'Requested action exceeds declared authority.',
    'Source evidence is missing or stale for a high-impact claim.',
    'Task requires external mutation, secrets, payments, filings, deployments, or client-facing action without approval.',
]))}
'''


def render_prompts(spec: dict[str, Any], bundle: dict[str, Any]) -> tuple[str, str]:
    prompts = bundle.get("prompts", {})
    system = f'''# System Prompt

You are `{spec['agent_id']}`, the installed local agent described by this folder.

{prompts.get('system', 'Read local identity, doctrine, skills, models, knowledge attachments, evals, and upkeep before acting.')}

You inherit organization and constitution doctrine. You may narrow scope through local doctrine, but you may not override higher authority.
'''
    task = f'''# Task Prompt

{prompts.get('task', 'Complete the task within local authority, verify evidence, and report uncertainty.')}

1. Read local identity and doctrine.
2. Identify governing authority and task scope.
3. Use pinned or vendored skills.
4. Consult knowledge attachments only within allowed scope.
5. Produce result, uncertainty, verification, and next action.
6. Escalate when authority, evidence, privacy, or external action boundaries are crossed.
'''
    return system, task


def install_from_spec(spec_path: Path, output: Path, force: bool = False) -> None:
    spec = load_json(spec_path)
    bundle_path = ROOT / "archetypes" / spec["archetype"] / "agent.bundle.json"
    if not bundle_path.exists():
        raise FileNotFoundError(f"missing archetype bundle: {bundle_path}")
    bundle = load_json(bundle_path)

    if output.exists():
        if not force:
            raise FileExistsError(f"output exists; pass --force to replace: {output}")
        shutil.rmtree(output)

    models = dict(bundle.get("models", {}))
    models.update(spec.get("model_overrides", {}))

    knowledge_sets = {
        "schema_version": "0.1",
        "attachments": spec.get("knowledge_attachments") or bundle.get("knowledge_sets", []),
    }

    skills = {
        "schema_version": "0.1",
        "mode": "vendored_or_pinned",
        "skills": bundle.get("skill_bundle", []),
    }

    manifest = {
        "schema_version": "0.1",
        "agent_id": spec["agent_id"],
        "title": spec["title"],
        "source_archetype": bundle["id"],
        "source_archetype_path": str(bundle_path.relative_to(ROOT)),
        "specializations": spec.get("specializations", []),
        "generated_files": REQUIRED_FILES,
        "update_rules": [
            "Do not overwrite local doctrine without review.",
            "Do not overwrite locally modified skills without diffing provenance.",
            "Do not attach private knowledge bases without explicit local configuration.",
            "Do not increase autonomy without permission review.",
        ],
    }

    write(output / "agent.md", render_agent_md(spec, bundle))
    write(output / "identity.md", render_identity_md(spec, bundle))
    write(output / "doctrine.md", render_doctrine_md(spec, bundle))
    write(output / "skills.json", json.dumps(skills, indent=2, sort_keys=True))
    write(output / "models.json", json.dumps(models, indent=2, sort_keys=True))
    write(output / "knowledge-sets.json", json.dumps(knowledge_sets, indent=2, sort_keys=True))

    system_prompt, task_prompt = render_prompts(spec, bundle)
    write(output / "prompts/system.md", system_prompt)
    write(output / "prompts/task.md", task_prompt)

    write(output / "evals.md", '''# Evals

## Acceptance checks

- Reads local identity and doctrine.
- Uses pinned or vendored skills.
- Respects knowledge attachment scope.
- Applies model trust policy.
- Escalates forbidden or high-uncertainty actions.

## Failure modes

- Treating archetype defaults as local authority.
- Weakening organization doctrine.
- Using stale copied skills without provenance.
- Treating attached knowledge as globally authoritative.
''')

    write(output / "upkeep.md", '''# Upkeep

## Recurring checks

- Inspect drift between local doctrine and organization doctrine.
- Check pinned skills for upstream updates.
- Check model routing policy freshness.
- Check knowledge attachments for stale or missing sources.
- Record changes, open questions, and required human approvals.

## Self-improvement limit

The agent may propose changes to its own identity, doctrine, skills, models, prompts, evals, or knowledge attachments. It may not silently apply changes that widen authority, weaken boundaries, or increase autonomy.
''')

    write(output / "manifest.json", json.dumps(manifest, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description="Instantiate a thick local Architectonic agent from an archetype bundle.")
    parser.add_argument("--spec", required=True, help="Path to install spec JSON.")
    parser.add_argument("--output", required=True, help="Output directory for installed agent.")
    parser.add_argument("--force", action="store_true", help="Replace output directory if it exists.")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = ROOT / spec_path
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output

    install_from_spec(spec_path, output, force=args.force)
    print(f"installed agent -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
