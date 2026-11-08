# Host guidance

Read only the section for the current host. Capabilities and command syntax can
vary by version. Prefer exposed session tools and visible host state. A command
available to the user is not automatically an agent-callable tool.

## Codex

- Invocation: `$planner plan <task>` or `$planner implement <instructions>`.
- In a `plan` session, Codex's plan-approval message "Implement the plan."
  does not switch the skill to `implement`: follow the save-only transition in
  planning guidance, then stop. Do not prompt for executor session settings.
- For `implement`, if the user explicitly requests a persistent Codex Goal,
  use the exposed native goal capability when available and permitted, scoped
  to completing the approved `PLANNER.md` and its validation. Check for an
  existing goal first and do not replace an unrelated active goal. Preserve the
  plan's scope and required user decisions; do not set a budget unless requested.
  A goal can enable continuation across turns but does not guarantee it. Do not
  create a goal merely because this skill was invoked. If the native capability
  is unavailable, explain and offer the host's supported `/goal` control.
- When the current chat title tool is exposed and permitted, use it to set the
  mode-specific `Plan P: <task>` or `Plan I: <task>` title. Target only the current chat; do not create a chat or
  attempt to rename one by printing a command.
- `agents/openai.yaml` disables implicit invocation. Do not edit user config.
- The native `/plan` command enters Plan Mode in supported surfaces; in the app
  use its Plan control. Use the actual mode state or ask the user to confirm it.
  Follow the host's native plan presentation and approval conventions.
- The model picker or `/model` shows available models. In versions supporting
  direct settings, `/model --reasoning=high` changes reasoning for the current
  session; `/status` can verify settings. Use the UI if the command is absent.
  Ask the user to operate these controls unless an exposed native tool can do so.
- Do not use shell invocations of `codex`, config edits, or subagents to pretend
  the current conversation's model or effort changed. Never create a new chat
  automatically as part of the handoff.
- User installation: `~/.agents/skills/planner`; repository installation:
  `.agents/skills/planner`. Avoid duplicate installations of the same skill.

Sources: [skills](https://learn.chatgpt.com/docs/build-skills),
[session commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

## Claude Code

- Invocation: `/planner plan <task>` or `/planner implement <instructions>`.
  The host supplies arguments from the slash invocation; preserve the remaining
  task text as user data, including quotes and multiline instructions.
- The installer adds `disable-model-invocation: true` to the installed SKILL.md.
  This is a Claude-specific extension, not a portable Agent Skills requirement.
- Use native Plan Mode (the host's permission-mode selector; Shift+Tab cycles
  modes in supported terminals). If a native enter/exit-plan tool is exposed,
  it may be used according to the host's rules; otherwise ask the user.
- `/model` is a user control for model selection. Prefer `/effort <level>` for
  an intentional session change only after checking its persistence behavior
  in the installed version. Some picks are saved per model. Where that would
  persist preferences, ask the user to open a session using the supported
  `claude --effort <level>` launch flag instead, or use an exposed temporary
  override. Never silently write settings or environment files.
- Some effort changes only affect the next user message, and higher-priority
  environment or organization settings can override them. Confirm the effective
  value when available; otherwise label it user-reported or unverified.
- Do not set a fixed `model`, `effort`, or `context: fork` in this two-mode skill:
  the two stages need different settings in the user's main sessions. Do not
  spawn subagents as a substitute for the user's chosen session configuration.
- User installation: `~/.claude/skills/planner`; repository installation:
  `.claude/skills/planner`.

Sources: [skills](https://code.claude.com/docs/en/skills),
[model and effort](https://code.claude.com/docs/en/model-config),
[native Plan Mode](https://code.claude.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis).

## Other compatible hosts

Use the installed host's skill invocation mechanism and discover native planning
and session controls. Honor the explicit-invocation rule even if the host has no
metadata switch for it. Do not assume Codex/Claude commands work elsewhere.
Ask for unavailable model/effort information and resolve the pair as described
in session setup.
Without native Plan Mode, stop `plan` with an explanation. Without an effort
control, follow the explicit unsupported-effort choice in session setup.
