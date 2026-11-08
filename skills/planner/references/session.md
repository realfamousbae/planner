# Session setup and model recommendations

## Establish the configuration

For `implement`, read the root `PLANNER.md` first to learn the agreed executor
and effort. For `plan`, use Sol / high unless the user chooses otherwise.
Before substantive investigation or implementation:

1. Identify the host, current model, supported effort levels, and available
   models from trustworthy session metadata or a supported host capability.
   Do not infer the active model from your own prose or from global defaults.
   If unavailable, ask the user to report the relevant picker/status values.
   A public model catalog alone does not prove account access.
2. Show the recommended model and effort alongside any known active settings.
   If they differ, ask whether to keep the active model or switch manually.
   Already explicit choices in the current request need no repeated question.
3. Ask which supported effort to use, presenting the recommendation as the
   default. Do not continue dependent work before an answer. If supported levels
   are unknown, ask for the picker's choices rather than inventing options.
4. Apply the user's effort through a native, session-scoped mechanism only if
   one is actually exposed to you. Otherwise give manual instructions and wait
   for the user's confirmation before substantive work. Merely printing a slash
   command or running it in a shell does not apply a chat setting.

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
