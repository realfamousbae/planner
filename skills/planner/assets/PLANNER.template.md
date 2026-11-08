# <Task title>

## Handoff

- Goal: <observable user outcome>
- Status: <approved | in progress | blocked | completed>
- Plan revision: <identifier for the approved specification>
- Approval: <explicit approval, source and date for this revision; not inferred>
- Planning model / effort: <selected values; confirmed source or unverified>
- Accepted implementation model / effort: <available model and supported effort>
- Recommendation rationale: <why this executor fits this task>
- Latest execution model / effort: <not started, or values and confirmation source>
- Repository: <repository identity; no machine-specific absolute paths>
- Baseline: <branch/commit if available, relevant dirty changes and assumptions>

## Requirements and decisions

<User requirements, constraints, scope boundaries, and chosen solutions with
reasons. Resolve high-impact choices; do not leave architecture alternatives
for the executor to choose. Include only context needed for this task.>

## Implementation stages

### 1. <Outcome>

- Status: pending
- Dependencies: <earlier stages or prerequisites; none if independent>
- Changes: <concrete components and required behavior>
- Interfaces/data: <necessary API/type/schema changes; omit if inapplicable>
- Failure handling: <relevant failures and intended behavior>
- Acceptance: <observable criterion and relevant verification>

<Repeat stages as needed. Use repository-relative paths and existing symbols
where they clarify the work. Include migration/compatibility steps when needed.>

## Validation and final acceptance

| Check / command | Expected result | Actual result |
| --- | --- | --- |
| <real command or manual check with working directory> | <success criterion> | Not run |

<Overall done criteria and any task-specific deployment or migration constraints.
Separate local validation from actions requiring external authorization.>

## Agreed changes

<None initially. Record material changes, reasons, revision and explicit approval;
record compatible additional instructions without pretending they were in v1.>

## Progress and continuation

- Completed: <none initially; concrete stage outcomes during execution>
- Blockers / limitations: <none or evidence and unresolved issue>
- Next action: <precise first remaining action, relevant files and prerequisites>
- Continuation model / effort: <accepted pair, or agreed change and rationale>
- Next session: <host-specific planner implement invocation>

<During execution record meaningful check results and continuation facts here,
without copying the conversation or storing secrets.>
