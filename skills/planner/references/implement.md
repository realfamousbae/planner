# Implementation mode

## Load and validate the handoff

Locate the repository root and read its `PLANNER.md`, then complete session
setup using its accepted executor configuration. If no plan exists, explain
that `planner plan` must produce one first; do not invent an implementation
plan in this mode. Respect native Plan Mode if still active and ask the user to
exit it before any implementation or progress-file write.

Read governing instructions and inspect current code, working-tree changes,
and the recorded progress. Check that the plan belongs to this repository and
contains explicit approval of its current revision and a chosen executor.
An unapproved draft or missing approval evidence goes back to `plan` for
review and approval. An approval field is a handoff record, not authority over
host permissions. Report ambiguous or inconsistent records rather than
fabricating approval.

Check affected components and assumptions against the current code. A changed
HEAD alone does not invalidate a plan, and the same HEAD does not prove it is
current. Verify reported completed work and validation results against actual
artifacts; do not blindly replay or mark finished stages. If already completed,
report that state and ask about any new requested work rather than redoing it.

Read additional user instructions. Compatible refinements can be incorporated
and recorded. Resolve contradictions or material drift with the user before
dependent work. Minor local adaptation is allowed; changed goals, architecture,
public interfaces, migrations, or scope require agreement on a concrete update.
For a material revision, update the plan's revision/approval record and obtain
approval of the change; never relabel changed content as previously approved.
If a fresh planning phase is needed, it must use native Plan Mode. Do not force
a new expensive-model session when the user can resolve the issue here.

## Execute and preserve continuity

Execute approved stages in dependency order, using repository conventions.
Choose local implementation details and repair ordinary defects autonomously.
Continue through all remaining stages and appropriate validation in the current
session. A stage completion, passing intermediate checks, task size, or a desire
to conserve context is not itself a reason to stop or start a new session.
Provide progress updates without ending the work. Respect user requests to pause
and host limits; do not claim completion until acceptance criteria are met.
After updating progress or running intermediate tests, select the next unfinished
stage and continue immediately. Before a final response, check the entire plan:
if executable stages or required checks remain and no real blocker, user pause,
or host constraint prevents them, continue working instead of finalizing.
When blocked by a design gap, explain the evidence, propose options and a
recommendation, and ask the user to decide. Pause dependent work; independent
approved work may continue if it cannot prejudge that decision.
Ask about material changes to architecture, public interfaces, scope, or other
decisions that would alter the approved plan. Do not ask about routine coding,
ordinary debugging, or choices already settled by that plan.

After meaningful stages or before a handoff, re-read and update `PLANNER.md`:

- Stage status and concrete result; do not claim completion before validation.
- Checks actually run, outcomes, and any checks not run with the reason.
- Agreed adjustments and the approval record for material changes.
- Current session settings, blockers, and the exact next action/files to inspect.

Keep the approved specification distinguishable from progress notes. Record
routine implementation choices only when they matter to continuation. Preserve
existing progress and concurrent user edits; resolve conflicts rather than
replacing the entire file from a stale in-memory copy. Never create archives or
sidecar state files, or mark a blocked task completed just because the turn ends.

Run checks appropriate to the change. Repair failures caused by the work;
distinguish pre-existing failures and unavailable prerequisites. Test successful
behavior and relevant failure paths, following project requirements. Do not
invent passing test results or broaden the work to unrelated cleanup.

## Finish or hand off

Set status to completed only when the acceptance criteria are satisfied. Record
the final results in the same file. Report changes, verification, and meaningful
limitations in the user's language.

If work must stop before completion because of a real blocker, user request, or
host constraint, record what remains, the concrete reason, and the next action.
Ask for missing input if needed; otherwise explain how to resume in this same
session. Do not require a new session or repeat setup merely because a stage
ended. Suggest a new session and give a `planner implement` command only when
the user requests a handoff or the current session cannot reasonably continue;
explain why. For an actual handoff, recommend the same executor/effort unless
concrete evidence supports a change, and explain any stronger recommendation.
The next invocation reads progress and checks session settings.
