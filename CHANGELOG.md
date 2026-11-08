# Changelog

## Unreleased

- Keep Codex's `Implement the plan.` approval in the planning session's
  save-only transition; start implementation only in the separate session.
- Avoid framing every implementation stage as a handoff; record progress when
  useful and continue to the next task.
- Support an explicitly requested Codex Goal for implementation across turns.
- Make completing all approved implementation stages the main skill contract;
  pause for material decisions or actual blockers, not routine milestones.
- Continue implementation and validation in the current session instead of
  suggesting a new session after an intermediate stage; explain real blockers.
- Prefer a permitted interactive question tool for session setting confirmation,
  including asynchronous questions when supported by the host.
- Name planning sessions `Plan P: <task>` and implementation sessions
  `Plan I: <task>` when the host exposes a permitted title control; otherwise
  suggest the title.
- When active settings are unavailable, ask for a simple confirmation of the
  expected model and effort before requesting different values.
- Skip repeated model and effort questions when reliable active session settings
  already match the recommended or agreed configuration.
- Expanded English and Russian installation guides: agent conversations, Python,
  manual user/project copies, Claude GUI uploads, updates, and removal.

Initial public preview:

- Two explicit modes: `plan` and `implement`.
- Native Plan Mode, revision approval, and a save-only transition.
- One repository-root `PLANNER.md` with implementation progress and resumption.
- Configurable Sol/high → Terra/medium default profile and effort selection.
- Codex and Claude Code installation adapters without overwriting existing skills.
- English and Russian guides, example handoff, package validation, and CI.

No model-based performance or cost comparison has been performed.
