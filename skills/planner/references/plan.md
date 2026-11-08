# Planning mode

## Enter and investigate

Complete session setup. Confirm native Plan Mode through host state or an
explicit user report. If it is off, ask the user to enable it using the host's
native control. If unavailable, explain the requirement and stop. Do not
substitute a read-only prompt or conduct the planning investigation outside it.

Locate the repository root (normally `git rev-parse --show-toplevel`; otherwise
use the confirmed project root). In monorepos use the repository root, not the
current package. If multiple roots are plausible, clarify which owns the task.
Read governing repository instructions, existing `PLANNER.md`, working-tree
changes, relevant code, interfaces, and available validation commands. Do not
overwrite unrelated user changes. Record the branch/commit when available and
relevant uncommitted work; a commit alone does not describe a dirty worktree.

If an existing plan is unfinished, ask whether this request revises that task
or replaces it. Obtain explicit replacement intent before discarding it. A
completed plan can be replaced when the next plan is approved. An unrelated
pre-existing `PLANNER.md` must not be overwritten without resolving the collision.

Explore discoverable facts before asking about them. Discuss requirements,
success criteria, scope, design choices, and meaningful tradeoffs. Use native
question tools when available. Resolve decisions that would otherwise force
the executor to redesign the feature; leave ordinary local coding details open.

## Prepare and approve

Use the [plan template](../assets/PLANNER.template.md) as the handoff structure.
Translate headings and explanatory text into the user's language. Replace
template prompts with concrete facts; omit inapplicable detail rather than
inventing it. The document is Markdown for humans and agents, not a rigid API.

Include concrete behavior, affected components, necessary interface/data
changes, dependencies and order, meaningful failure handling, acceptance
criteria, and actual repository validation commands. Include migrations and
rollout considerations only when the task needs them. Do not embed large code
blocks, secrets, private transcripts, or unsupported benchmark claims.

Recommend and agree the executor configuration using session guidance. Present
the complete plan for review in the host's native planning format. Ask for
explicit approval; a question, silence, or a requested revision is not approval.
Revise and present the complete updated plan until the user approves the exact
revision, including the accepted executor configuration.

Keep the draft in conversation while native Plan Mode forbids writing. Do not
write a draft file, run code-generating commands, or use a shell workaround to
escape that restriction. Any host-managed plan artifact is not a replacement
for the final repository-root handoff.

## Save after leaving Plan Mode

On approval, explain that the next action is **save the approved plan only**.
Ask the user to leave native Plan Mode if required. Do not assume an approval
button or a normal chat message changed the host's mode. When implementation
permission is restored, save `PLANNER.md` in the same planning session.

Before writing, re-read an existing file to detect concurrent edits. If the
approved content or repository facts materially changed, resolve that difference
and obtain approval of the revised plan. Do not lose the user's approved draft
or quietly substitute a freshly summarized version. Record approval of this
revision, its source, date, agreed model settings, and initial pending progress.
Write the final content and read it back to confirm it was saved correctly.
Never start implementation as a side effect of leaving Plan Mode.

End with the saved path, accepted executor model/effort, and a copyable prompt
for a **new session in the same repository/worktree**. For example, localize:

> Planning is complete and PLANNER.md is saved. Open a new session on the
> agreed model with the agreed effort, then send `$planner implement` (Codex)
> or `/planner implement` (Claude Code). The new session will read the plan and
> check the session settings before implementing. You may append extra instructions.

If saving is still blocked, say the plan is approved but **not yet saved** and
request the required mode switch; do not send the user to implementation yet.
