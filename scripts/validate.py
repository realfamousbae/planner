#!/usr/bin/env python3
"""Validate distributable skill metadata, resources, and local documentation links."""

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root):
    skill = root / "skills" / "planner"
    content = (skill / "SKILL.md").read_text(encoding="utf-8")
    parts = content.split("---", 2)
    require(content.startswith("---\n") and len(parts) == 3, "Missing frontmatter")
    fields = yaml.safe_load(parts[1])
    require(isinstance(fields, dict), "Frontmatter must be a mapping")
    require(fields.get("name") == skill.name, "Skill name must match directory")
    description = fields.get("description")
    require(isinstance(description, str) and 0 < len(description) <= 1024,
            "Description must be 1–1024 characters")
    require(set(fields) <= {"name", "description", "license", "compatibility", "metadata"},
            "Keep provider-specific frontmatter out of the common package")
    config = yaml.safe_load((skill / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    require(config["policy"]["allow_implicit_invocation"] is False,
            "Codex must require explicit invocation")
    require("$planner" in config["interface"]["default_prompt"],
            "Default prompt must invoke planner")
    require(25 <= len(config["interface"]["short_description"]) <= 64,
            "UI description must be 25–64 characters")
    require((skill / "assets" / "PLANNER.template.md").is_file(), "Missing plan template")
    count = 0
    for path in root.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            require((path.parent / target).is_file(), f"Broken link in {path}: {target}")
            count += 1
    return count


if __name__ == "__main__":
    try:
        links = validate(ROOT)
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"Package valid; {links} local documentation links checked.")
