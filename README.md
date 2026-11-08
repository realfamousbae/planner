# Planner

[English](README.md) · [Русский](README.ru.md)

[![Checks](https://github.com/realfamousbae/planner/actions/workflows/checks.yml/badge.svg)](https://github.com/realfamousbae/planner/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Think it through. Hand it off. Build from the same plan.**

A two-session Agent Skill for preparing repository changes on one model and
implementing the approved plan on another. One repository-root `PLANNER.md`
carries the task's decisions, acceptance criteria, and implementation progress.

Default profile: **Sol / high → Terra / medium**. This is a configurable starting
point, not a benchmark result or a guarantee of lower total cost. The skill uses
available models, discusses alternatives, and asks for effort in both stages.

```text
Session 1                         Session 2
Sol / high                        Terra / medium
Investigate → discuss → approve   Read → verify → implement → test
                       │          ▲
                       └─ PLANNER.md
```

## Why Planner

Use Planner for a feature, refactor, or multi-component change where another
session needs the decisions behind the work. It carries requirements, design
decisions, concrete stages, validation commands, and a continuation point.
It can also hand off between different compatible agents using the same checkout.

Planner is an instruction package, not a model launcher. You choose models and
open sessions; automatic effort changes depend on controls the host exposes.
Small fixes may not justify a separate planning session. Both Codex and Claude
Code have installation adapters; interactive end-to-end verification is still
pending. Other Agent Skills hosts need native Plan Mode and suitable controls.

## Install

Python 3.9+ is needed only for this install helper; the skill itself is Markdown
and YAML, with no runtime scripts or API credentials.

Clone and inspect the package, then install:

```sh
git clone https://github.com/realfamousbae/planner.git
cd planner
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

The helper detects `codex` and `claude` on PATH and installs independent copies:

| Client | User location | Explicit invocation setting |
| --- | --- | --- |
| Codex | `~/.agents/skills/planner` | `agents/openai.yaml`: `allow_implicit_invocation: false` |
| Claude Code | `~/.claude/skills/planner` | Installed frontmatter: `disable-model-invocation: true` |

Use `--agent codex`, `--agent claude`, or `--agent both` to select targets
explicitly, including clients whose executables are not on PATH. Existing
destinations, broken symlinks, and legacy Codex `~/.codex/skills/planner`
installations are preserved: the helper refuses replacement. For an update,
inspect and remove or relocate the previous copy yourself, then reinstall.
Copies do not update automatically when this checkout changes.

Open a new session after installation and verify Planner appears in the skill
selector. Do not install duplicate copies in user and repository locations.

For project-only installation, copy `skills/planner` into
`.agents/skills/planner` (Codex) or `.claude/skills/planner` (Claude Code).
For a manual Claude copy, add `disable-model-invocation: true` to the YAML
frontmatter. Other hosts can install the common package using their normal
Agent Skills mechanism; host-level explicit-only discovery varies, and the
instructions also require an explicit request. Native Plan Mode is required.

## Plan in the first session

Select the planning model, preferably Sol, and enable native Plan Mode. Then:

```text
# Codex
$planner plan Add pagination to the activity feed.

# Claude Code
/planner plan Add pagination to the activity feed.
```

The skill asks for effort (high by default), investigates the repository, and
discusses requirements and design. It proposes an executor (Terra / medium by
default) and explains any stronger or cheaper recommendation. In other model
ecosystems it proposes available alternatives for confirmation. If it cannot
inspect available choices, it asks you to report them.

Review and approve the complete plan, including the executor configuration.
Then leave native Plan Mode and tell the same session:

```text
Save the approved plan to PLANNER.md only. Do not implement it.
```

The skill verifies the saved file and supplies a prompt for the next session.
While Plan Mode prohibits writes, the draft stays in the conversation. A plan
shown in chat or a host-managed plan file is not yet the repository handoff.
Without native Plan Mode, planning stops with instructions instead of emulating it.

## Implement in a new session

Open the same repository/worktree in a new session. Select the model recommended
in `PLANNER.md` and leave Plan Mode off:

```text
# Codex
$planner implement

# Claude Code
/planner implement
```

You may append instructions, for example:

```text
$planner implement Use high effort. Preserve compatibility with existing clients.
```

The skill reads the plan, asks for effort (the agreed value, usually medium),
and checks it against current code. An explicit effort in the current request
counts as the selection. When no session control is exposed to the agent, it
guides you through manual switching and waits for confirmation. Displaying a
command does not execute it. Persistent global preferences are not changed.

Local implementation decisions are autonomous. Changes to scope, architecture,
or public interfaces are discussed and recorded before dependent work continues.
Stages, real check results, and the next action are written back to `PLANNER.md`,
so another `implement` session can resume. Plan approval does not grant extra
permissions to deploy or publish.

One file holds one task. An unfinished task is not discarded without your
agreement; a completed plan is replaced when a new one is approved. No plan
archive or secondary state file is created. Instructions and references are
English; task dialogue, the generated plan, and reports follow your language.

## Validate

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Tests exercise installation and preservation of existing files in temporary
directories. [Validation notes](docs/VALIDATION.md) distinguish static checks,
scenario walkthroughs, and model-based runs. No paid model evaluation or
Sol/Terra quality/cost comparison is bundled.

## Project resources

- [Example handoff](examples/PLANNER.example.md) — a fictional completed plan for review before implementation.
- [Contributing](CONTRIBUTING.md) — local checks and workflow changes.
- [Security](SECURITY.md) — reporting sensitive issues privately.
- [Changelog](CHANGELOG.md) — release history.
- [Issues](https://github.com/realfamousbae/planner/issues) — bugs and proposals.

Planner is licensed under [MIT](LICENSE). This project is independent and is not
affiliated with OpenAI or Anthropic.

The package follows the [Agent Skills format](https://agentskills.io/specification).
See [Codex skill installation](https://learn.chatgpt.com/docs/build-skills),
[Claude Code skills](https://code.claude.com/docs/en/skills), and the bundled
[host guidance](skills/planner/references/hosts.md) for client-specific controls.
