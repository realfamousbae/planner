#!/usr/bin/env python3
"""Install independent skill copies without replacing existing installations."""

import argparse
from pathlib import Path
import shutil
import tempfile


SOURCE = Path(__file__).resolve().parents[1] / "skills" / "planner"


def exists(path):
    # Path.exists() alone misses broken symlinks, which must also be preserved.
    return path.exists() or path.is_symlink()


def destination(home, agent):
    directory = ".agents" if agent == "codex" else ".claude"
    return home / directory / "skills" / "planner"


def preflight(source, home, agents):
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Missing skill entrypoint: {source / 'SKILL.md'}")
    for agent in agents:
        target = destination(home, agent)
        if exists(target):
            raise FileExistsError(f"Existing installation preserved: {target}")
        if agent == "codex":
            # Older installations may still be discovered in this location.
            legacy = home / ".codex" / "skills" / "planner"
            if exists(legacy):
                raise FileExistsError(f"Existing legacy installation preserved: {legacy}")


def install(source, target, agent):
    if exists(target):
        raise FileExistsError(f"Existing installation preserved: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".planner-install-", dir=target.parent) as tmp:
        staged = Path(tmp) / "planner"
        shutil.copytree(source, staged)
        if agent == "claude":
            entrypoint = staged / "SKILL.md"
            content = entrypoint.read_text(encoding="utf-8")
            if not content.startswith("---\n"):
                raise ValueError("Skill entrypoint must begin with YAML frontmatter")
            entrypoint.write_text(
                "---\ndisable-model-invocation: true\n" + content[len("---\n"):],
                encoding="utf-8",
            )
        # copytree creates the destination exclusively; an existing target,
        # including one created after preflight, is never merged or replaced.
        shutil.copytree(staged, target)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=("available", "codex", "claude", "both"),
                        default="available")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.agent == "available":
        agents = [agent for agent in ("codex", "claude") if shutil.which(agent)]
    else:
        agents = ["codex", "claude"] if args.agent == "both" else [args.agent]
    if not agents:
        parser.exit(1, "No Codex or Claude Code executable found. Select --agent explicitly.\n")
    home = Path.home()
    try:
        # Check all destinations before installing either client.
        preflight(SOURCE, home, agents)
        for agent in agents:
            target = destination(home, agent)
            if not args.dry_run:
                install(SOURCE, target, agent)
            print(f"{'Would install' if args.dry_run else 'Installed'} {agent}: {target}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
