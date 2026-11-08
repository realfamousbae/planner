# Session setup and model recommendations

## Establish the configuration

For `implement`, read the root `PLANNER.md` first to learn the agreed executor
and effort. For `plan`, use Sol / high unless the user chooses otherwise.
Before substantive investigation or implementation:

1. Identify the host and look for the current model and effort in trustworthy
   session metadata or a supported host capability available to the agent.
   Do not infer active settings from your own prose, global defaults, a model
   catalog, or a shell command that starts a separate session. A public catalog
   alone does not prove account access. Discover supported options when needed.
2. Compare both active values with the recommended pair for `plan` or the
   agreed pair in `PLANNER.md` for `implement`. If both reliably match, briefly
   report the match and proceed without asking the user to select them again.
3. If a known active value differs, present the active and recommended values
   and ask whether to keep the current configuration or switch. Respect an
   explicit choice in the current request without asking for that choice again.
   If either active value cannot be determined, state which values are unknown
   and ask the user to check the picker/status and confirm whether it shows
   the expected pair, for example: "Does the picker show Terra / medium?"
   Offer a clear yes / no choice using the host's question tool when available
   and permitted, otherwise ask in chat. A yes confirms the pair as user-reported;
   on no, ask for the actual values and whether to keep them or switch. If only
   one value is unknown, ask about that value without re-confirming the known
   one. Do not invent supported options or claim an unverified match. Wait for
   the answer before dependent work; a preselected option is not an answer.
4. If a change is needed, use a native, session-scoped mechanism only if it is
   exposed to you. Otherwise give manual instructions and wait for the user's
   confirmation before substantive work. Merely printing a slash command or
   running it in a shell does not apply a chat setting.

Distinguish **recommended**, **user-selected**, and **confirmed active** settings.
Confirmation can come from host state or the user's report; record its source.
If the active value is still unknown, label it unverified. Do not claim that the
skill changed a setting when the user changed it. Some changes only take effect
on the next turn: yield and resume after they take effect. Never edit global
configuration or persistent preferences to achieve a session setting.

If effort is unsupported, explain that fact and ask to use the model's native
default or select a model with effort control. Record `not supported` rather
than pretending medium/high was applied. Explicit user selection is still
required for this alternative. Native Plan Mode itself has no fallback.

## Select an executor after investigation

Start with Terra / medium where available. Assess uncertainty, architectural
coupling, failure impact, task size, and the strength of existing tests. A long
but repetitive change can be easier than a short, ambiguous migration.

- Keep the default for well-specified changes with effective validation.
- Recommend a stronger configuration, such as Sol, when implementation still
  needs substantial cross-system reasoning. Explain the concrete reason.
- For small, isolated work, a cheaper available model can be proposed when its
  capabilities are known. Higher effort does not guarantee stronger capability.
- If the preferred names are unavailable, propose an available stronger planner
  and cheaper executor, explain the tradeoff, and obtain confirmation. Do not
  treat unfamiliar model names as evidence of capability or price. Consult
  official current information when those facts are needed and accessible;
  otherwise ask the user and state uncertainty.

Resolve the candidate set before finalizing the handoff. Record the accepted
executor, its effort, and rationale in the plan. Do not silently replace the
user's choice or increase spend. A custom profile in the invocation overrides
the default; do not persist it globally.
