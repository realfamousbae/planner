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
available models, checks session settings, and discusses alternatives when needed.

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

Choose the method that fits your app. **Installing the skill does not add native
Plan Mode or repository access**: the full workflow needs both. A successful
upload into a regular chat is not a verified coding integration.

| Method | Where | Requirements |
| --- | --- | --- |
| Ask the agent to install | Codex desktop, CLI, IDE; Claude Code | Agent access to local files and GitHub |
| Python installer | Codex and/or Claude Code | Python 3.9+; Git or a downloaded repository ZIP |
| Copy the folder manually | User-wide or project-only | File manager; no Python or Git required |
| Upload a skill ZIP | Claude web/Desktop skill settings | Skill upload enabled; workflow compatibility must be checked separately |
| Host's normal skill installer | Other Agent Skills hosts | Native Plan Mode and repository access for the full workflow |

The skill itself is Markdown and YAML and needs no runtime dependencies or API
credentials. The steps below are alternatives; install only one copy per host.

### 1. Through an agent conversation

In **Codex desktop**, open a coding session with local filesystem access and send:

```text
$skill-installer install the skill from https://github.com/realfamousbae/planner/tree/main/skills/planner
```

The same prompt works in Codex CLI or its IDE extension when the bundled
skill-installer is available. This is installation through the app conversation,
not a terminal command. If the installer is unavailable, use the Python helper
or manual copying. See [Codex's official installation guidance](https://learn.chatgpt.com/docs/build-skills).

In **Claude Code**, including a desktop Code session with local file access,
you can ask the agent to perform a manual installation:

```text
Install Planner from https://github.com/realfamousbae/planner/tree/main/skills/planner
into my user skills directory. Copy the complete folder, including references,
assets, agents, and LICENSE. Add disable-model-invocation: true to SKILL.md's
YAML frontmatter. Preserve any existing installation and report its path.
```

This is a request for the coding agent to install files, not a built-in Claude
installation command. Review the resulting path. It requires permission to write
local files; an ordinary cloud chat cannot be assumed to have that access.

### 2. Python installer

Clone the repository, inspect it, preview destinations, and install:

```sh
git clone https://github.com/realfamousbae/planner.git
cd planner
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

Without Git, use **Code → Download ZIP** on the
[repository page](https://github.com/realfamousbae/planner), extract it, and open
a terminal in the extracted folder before running the two Python commands.
On Windows, use `py` instead of `python3` if that is your Python launcher.

The helper detects `codex` and `claude` on PATH. Choose explicitly when needed,
including when an app's CLI is not on PATH:

```sh
python3 scripts/install.py --agent codex
python3 scripts/install.py --agent claude
python3 scripts/install.py --agent both
```

These are alternative target selections. The helper creates independent copies
at the user paths below, preserving existing destinations, broken symlinks, and
legacy Codex `~/.codex/skills/planner` installations. It refuses replacement and
adds Claude's explicit-only frontmatter automatically.

### 3. Manual installation: user-wide or project-only

Download and extract the repository ZIP, or clone it. Copy the **entire**
`skills/planner` folder, not just SKILL.md, to one of these locations:

| Client | All your projects | Only one repository |
| --- | --- | --- |
| Codex | `~/.agents/skills/planner` | `<repository>/.agents/skills/planner` |
| Claude Code | `~/.claude/skills/planner` | `<repository>/.claude/skills/planner` |

`~` means your user home directory; on Windows the corresponding paths start
with `%USERPROFILE%`, for example `%USERPROFILE%\.agents\skills\planner`.
Create missing parent directories. In macOS Finder, use **Go → Go to Folder**
(`Cmd+Shift+G`) to open hidden home directories. In Windows Explorer, paste the
path into the address bar.

For a manual **Claude Code** copy, add this key inside the existing YAML
frontmatter at the top of SKILL.md:

```yaml
disable-model-invocation: true
```

Codex uses the included `agents/openai.yaml` for explicit-only invocation.
Do not install both user-wide and project copies for the same host.
See [Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

### 4. Claude web/Desktop: ZIP upload through the GUI

Claude supports custom skill uploads through
**Customize → Skills → + → Create skill → Upload a skill**. Code execution/file
creation must be enabled, and organization settings can restrict uploads.
See [Claude's official upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

To prepare a ZIP using your file manager:

1. Download and extract this repository.
2. Inside `skills`, compress the `planner` folder into `planner.zip`.
3. Check that the ZIP contains `planner/SKILL.md` and its sibling resource folders.
4. Upload that ZIP and enable the skill in Claude.

Do **not** upload the entire GitHub source archive as a skill. No prebuilt upload
ZIP is currently published. This describes Claude's generic skill-upload route;
Planner's upload and execution in Claude web/Desktop chat have **not been
verified**. Uploaded skills may have different metadata and invocation behavior
from local Claude Code skills. Do not assume `/planner` works in an ordinary chat.
Planner still requires native Plan Mode and repository access, so use a compatible
coding session for the full workflow. Uploading alone does not establish that
compatibility.

### 5. Other compatible agents

Install the common `skills/planner` folder through your host's documented skill
mechanism. Native Plan Mode and repository access are required. Configure
explicit-only invocation if the host supports it; otherwise the instructions
still require an explicit request. Do not assume Codex/Claude command syntax or
model names work elsewhere.

### Verify, update, and remove

Open a new session after installation and check that Planner is listed in the
skill selector. If it is missing, check the destination, folder nesting, and
whether your client supports that installation route. Interactive end-to-end
verification is still pending; local installation tests cover the Python helper.

Installed local copies do not update automatically. To update, inspect the old
copy, remove or relocate it, obtain the latest source, and reinstall with your
chosen method. Do not overwrite local customizations without reviewing them.
To uninstall a local copy, remove only its `planner` folder. For an uploaded
Claude skill, disable or delete it in Customize → Skills. Removing the skill
does not remove task plans from repositories.

## Plan in the first session

When the host exposes session renaming, Planner titles the planning session
`Plan P: <task name>` and the implementation session `Plan I: <task name>`.
Otherwise it suggests a title and continues.

Select the planning model, preferably Sol, and enable native Plan Mode. Then:

```text
# Codex
$planner plan Add pagination to the activity feed.

# Claude Code
/planner plan Add pagination to the activity feed.
```

The skill checks the session model and effort (Sol / high is recommended), then
investigates the repository and
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

The skill reads the plan, checks the session settings against the agreed pair,
and checks the plan against current code. If reliable active settings match, it
continues without a repeated question. If they differ, it asks whether to keep
them or switch; if settings are unavailable, it asks you to confirm whether the
picker shows the expected pair, and asks for actual values if it does not. An
explicit choice in the current request does not need repeating, but is not proof
that the setting is active. When switching requires manual action, the skill
waits for confirmation. Displaying a command does not execute it. Persistent
global preferences are not changed.

When the host exposes a suitable question tool, the confirmation uses selectable
answers; otherwise the skill asks in chat.

Local implementation decisions are autonomous. Changes to scope, architecture,
or public interfaces are discussed and recorded before dependent work continues.
The implementation session continues through the remaining stages and checks;
an intermediate milestone is not a reason to start another session. If work
must pause, it records why and how to continue, normally in the same session.
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
