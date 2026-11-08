# Add an optional limit to the greeting CLI

This is a fictional example of an approved handoff before implementation.
Its paths and commands describe an imaginary repository, not Planner itself.
It is not approval to change the repository where you are reading this example.

## Handoff

- Goal: let users print the first N greetings without changing default output.
- Status: approved
- Plan revision: 1
- Approval: fictional user approved revision 1 on 2026-11-08.
- Planning model / effort: Sol / high; user-reported in this fictional session.
- Accepted implementation model / effort: Terra / medium.
- Rationale: isolated CLI behavior with no schema changes and an existing test suite.
- Latest execution settings: not started.
- Repository: example-greetings.
- Baseline: main, clean working tree; implementation must verify the actual checkout.

## Requirements and decisions

Add an optional `--limit N` flag to the `greet` command. N must be a positive
integer. Invalid input exits with status 2 and an actionable CLI error. Without
the flag, output and exit status stay unchanged. Preserve greeting order and
print all available greetings if N exceeds their count. No new dependencies.

## Implementation stages

### 1. Add the flag and apply the limit

- Status: pending.
- Dependencies: none.
- Changes: in `greetings/cli.py`, add the optional integer argument to the
  existing parser, validate positivity, and apply it to the existing output
  sequence before printing. Reuse parser error handling.
- Acceptance: default behavior matches existing output; `--limit 2` prints the
  first two greetings; invalid values produce status 2 without a traceback.

### 2. Verify and document

- Status: pending.
- Dependencies: stage 1.
- Changes: extend `tests/test_cli.py` for absent flag, limit 1, an oversized
  limit, zero, negative values, and non-integer input. Add usage to README.md.
- Acceptance: all existing and added tests pass, and `--help` shows the option.

## Validation and final acceptance

Run from repository root:

| Check | Expected | Actual |
| --- | --- | --- |
| `python -m unittest discover -s tests -v` | All tests pass | Not run |
| `python -m greetings --help` | Documents `--limit` | Not run |
| `python -m greetings --limit 2` | First two greetings, status 0 | Not run |
| `python -m greetings --limit 0` | CLI validation error, status 2 | Not run |

No deployment is part of this task. Complete only when requirements and checks
above are satisfied.

## Agreed changes

None.

## Progress and continuation

- Completed: no implementation stages.
- Blockers: none recorded; validate assumptions against the checkout first.
- Next action: inspect the existing parser and CLI tests, then implement stage 1.
- Continuation configuration: Terra / medium, subject to a session settings check.
- New Codex session: `$planner implement`.
- New Claude Code session: `/planner implement`.
