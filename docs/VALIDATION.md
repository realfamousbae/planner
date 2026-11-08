# Validation record

Date: 2026-11-08. This record distinguishes executable filesystem checks from
review of workflow instructions. It does not assert model compliance from
reading a prompt.

## Static validation

- `python3 scripts/validate.py` is the repository's portable check for skill
  metadata, Codex explicit-only settings, template presence and local Markdown
  links. CI runs it alongside installer tests on Linux and macOS.
- The bundled skill-creator `quick_validate.py` passed for `skills/planner`
  using an isolated `uv run --with pyyaml` environment.
- Package YAML and explicit-invocation settings are checked separately for
  Codex and the generated Claude copy. The common SKILL.md uses standard
  `name` and `description`; the Claude-only frontmatter extension is inserted
  at install time, so the common-format validator need not accept that extension.
- Local Markdown links and copied resources are checked for existence/integrity.
- Local executable detection: `codex-cli 0.167.0`, `Claude Code 2.1.310`.
  Detecting an executable is not a test of the client's skill picker.

## Executed installation tests

`python3 -m unittest discover -s tests -v`: **6 passed**.

Temporary-directory tests cover complete copies of resources, the Claude-only
frontmatter addition, unchanged source files, refusal to replace an existing
installation, checking both destinations before writing, broken symlinks,
legacy Codex duplicates, and a missing source entrypoint.

`python3 scripts/install.py --dry-run` selected both detected clients without
installing files. Then `python3 scripts/install.py --agent both` installed
`~/.agents/skills/planner` and `~/.claude/skills/planner`. All seven files in each
copy matched their intended source content, including the Claude-specific
frontmatter addition; explicit-only invocation metadata parsed successfully.
The helper copies files exclusively; it does not merge installations. An I/O
failure during the final copy can leave a partial destination; inspect it before
removing it and retrying. There is no automatic cleanup of an existing target.

## Scenario walkthroughs: instruction review only

The following inputs were traced through the applicable instructions. These
are review results, not conversations executed against separate models.

| Scenario / input | Required route verified in the instructions |
| --- | --- |
| `plan Add pagination`, revise then approve | Setup asks effort; planning investigates in native mode, revises until approval of the exact revision, saves only after mode exit, then hands off. |
| `plan` while native Plan Mode is absent | Planning stops and asks for native mode; no read-only emulation or draft-file workaround. |
| Effort control unavailable or change applies next turn | Session guidance requires manual change/confirmation and yields when necessary; it does not claim a printed command changed settings. |
| Model has no effort control | Explain unsupported effort and ask for explicit native-default selection or another model; do not invent medium/high. |
| Sol/Terra unavailable or candidate list hidden | Ask for available choices, propose confirmed alternatives, and agree the pair; do not infer account access from public documentation. |
| Approval received while writes remain prohibited | Keep approved content in chat, report not yet saved, request mode exit; never begin implementation. |
| `implement` with no file or an unapproved draft | Explain that planning/approval is required; do not implement or manufacture approval evidence. |
| `implement` while Plan Mode remains enabled | Read-only setup can proceed, but no implementation or progress writes until mode exit. |
| HEAD differs or affected code has changed | Compare actual components and assumptions, including dirty changes; do not accept or reject solely by HEAD. |
| Extra instructions contradict a public interface decision | Pause dependent work, agree the concrete revision, update the approval record. |
| Local technical detail differs from plan | Adapt autonomously; material architectural/scope changes require discussion. |
| Implementation interrupted after a stage | Update results, blockers and next action; the next invocation verifies artifacts and resumes with a fresh effort selection. |
| New task over an unfinished or completed plan | Clarify revision/replacement for unfinished work; replace completed work only when the new plan is approved; no archive. |
| Concurrent changes to PLANNER.md | Re-read before updating, preserve changes, resolve ambiguity instead of writing a stale whole-file copy. |
| User only mentions the command, or asks for an ordinary code fix | Explicit invocation metadata and the body guard prevent intentional workflow activation from examples or unrelated requests. |

## Not executed

- Interactive skill selection and full end-to-end conversations in Codex and
  Claude Code, including actual native mode/effort switching.
- Independent-agent behavioral evaluation or paid API/model calls.
- Comparative Sol/Terra/Luna quality, latency, token usage, or total-cost trials.

For a future live check, use a disposable Git repository with a small executable
test suite. Plan a concrete change, reject one draft, approve its revision,
switch out of Plan Mode to save only, then open the executor session and interrupt
after the first stage. Resume and check real code, acceptance tests, progress,
and settings confirmation. Repeat with an unapproved file and conflicting
additional instructions. Record actual transcripts and results before claiming
behavioral reliability or measured savings.
