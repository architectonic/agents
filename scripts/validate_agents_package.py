#!/usr/bin/env python3
from __future__ import annotations

import json
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


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    for path in ROOT.rglob("*.json"):
        try:
            load_json(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)} invalid JSON: {type(exc).__name__}: {exc}")

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
    for name in [
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
    ]:
        if not (example / name).exists():
            errors.append(f"missing example file: {example.relative_to(ROOT)}/{name}")

    if errors:
        print("\n".join(errors))
        return 1
    print("agents package validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
