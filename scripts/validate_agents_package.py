#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_BUNDLE_KEYS = {
    "schema_version",
    "id",
    "title",
    "type",
    "risk_level",
    "autonomy_level",
    "identity",
    "doctrine",
    "skill_bundle",
    "models",
    "knowledge_sets",
    "prompts",
    "upkeep",
}
REQUIRED_INSTALLED_FILES = [
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
FORBIDDEN_WORK_AUTHORITIES = [
    "operations/board.json",
    "operations/log.md",
    "operations/daily/2026-07-09/status.json",
    "operations/daily/2026-07-09/queues.json",
]
RAIL_STATUSES = {"inbox", "ready", "in_progress", "blocked", "done", "cancelled"}
RAIL_PRIORITIES = {"P0", "P1", "P2", "P3"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    for path in ROOT.rglob("*.json"):
        try:
            load_json(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)} invalid JSON: {type(exc).__name__}: {exc}")

    ledger_path = ROOT / "operations/ledger.json"
    if not ledger_path.exists():
        errors.append("missing canonical Rail ledger: operations/ledger.json")
    else:
        ledger = load_json(ledger_path)
        if ledger.get("schema_version") != "1.0":
            errors.append("operations/ledger.json schema_version must be 1.0")
        if not ledger.get("project") or not ledger.get("updated"):
            errors.append("operations/ledger.json must identify project and updated date")

        items = ledger.get("items")
        if not isinstance(items, list):
            errors.append("operations/ledger.json items must be an array")
            items = []

        ids = [item.get("id") for item in items if isinstance(item, dict)]
        known_ids = {item_id for item_id in ids if item_id}
        if len(ids) != len(known_ids):
            errors.append("operations/ledger.json item ids must be present and unique")

        statuses = {
            item.get("id"): item.get("status")
            for item in items
            if isinstance(item, dict) and item.get("id")
        }
        for item in items:
            if not isinstance(item, dict):
                errors.append("operations/ledger.json items must be objects")
                continue
            item_id = item.get("id", "<missing-id>")
            for key in ("title", "owner_role", "acceptance", "depends_on", "evidence"):
                if key not in item:
                    errors.append(f"operations/ledger.json {item_id} missing {key}")
            if item.get("status") not in RAIL_STATUSES:
                errors.append(f"operations/ledger.json {item_id} has invalid status")
            if item.get("priority") not in RAIL_PRIORITIES:
                errors.append(f"operations/ledger.json {item_id} has invalid priority")
            for dependency in item.get("depends_on", []):
                if dependency not in known_ids:
                    errors.append(f"operations/ledger.json {item_id} has unknown dependency {dependency}")
                elif item.get("status") in {"ready", "in_progress", "done"} and statuses.get(dependency) != "done":
                    errors.append(
                        f"operations/ledger.json {item_id} is {item.get('status')} but dependency {dependency} is not done"
                    )
            if item.get("status") == "done":
                if not item.get("evidence"):
                    errors.append(f"operations/ledger.json {item_id} is done without evidence")
                if not item.get("completed_at"):
                    errors.append(f"operations/ledger.json {item_id} is done without completed_at")

    for relative_path in FORBIDDEN_WORK_AUTHORITIES:
        if (ROOT / relative_path).exists():
            errors.append(f"legacy parallel work authority must not exist: {relative_path}")

    archetype_dir = ROOT / "archetypes"
    bundles = sorted(archetype_dir.glob("*/agent.bundle.json")) if archetype_dir.exists() else []
    if not bundles:
        errors.append("no archetype bundles found")

    for path in bundles:
        data = load_json(path)
        missing = REQUIRED_BUNDLE_KEYS - set(data)
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing keys: {sorted(missing)}")
        if data.get("risk_level") == "high" and int(data.get("autonomy_level", 99)) > 2:
            errors.append(f"{path.relative_to(ROOT)} high-risk archetype has autonomy > 2")
        for skill in data.get("skill_bundle", []):
            for key in ("id", "source_repo", "source_path", "source_ref"):
                if not skill.get(key):
                    errors.append(f"{path.relative_to(ROOT)} skill missing {key}: {skill}")

    example = ROOT / "examples/mybusiness-lawfirm/agents/brazilian-tax-reviewer"
    for name in REQUIRED_INSTALLED_FILES[:-1]:
        if not (example / name).exists():
            errors.append(f"missing example file: {example.relative_to(ROOT)}/{name}")

    install_spec_dir = ROOT / "examples/install-specs"
    specs = sorted(install_spec_dir.glob("*.json")) if install_spec_dir.exists() else []
    if not specs:
        errors.append("no install specs found in examples/install-specs")

    generator = ROOT / "scripts/instantiate_agent.py"
    if not generator.exists():
        errors.append("missing scripts/instantiate_agent.py")
    else:
        for spec in specs:
            data = load_json(spec)
            for key in ("schema_version", "agent_id", "title", "archetype"):
                if not data.get(key):
                    errors.append(f"{spec.relative_to(ROOT)} missing {key}")
            with tempfile.TemporaryDirectory() as td:
                output = Path(td) / data.get("agent_id", "agent")
                result = subprocess.run(
                    [sys.executable, str(generator), "--spec", str(spec.relative_to(ROOT)), "--output", str(output)],
                    cwd=ROOT,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if result.returncode != 0:
                    errors.append(
                        f"{spec.relative_to(ROOT)} failed instantiate_agent.py: {result.stderr.strip() or result.stdout.strip()}"
                    )
                for name in REQUIRED_INSTALLED_FILES:
                    if not (output / name).exists():
                        errors.append(f"{spec.relative_to(ROOT)} generated output missing {name}")

    if errors:
        print("\n".join(errors))
        return 1
    print("agents package validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
