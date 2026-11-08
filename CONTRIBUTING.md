# Contributing to Planner

Bug reports and focused pull requests are welcome. Explain the user scenario,
expected behavior, and observed result. Redact proprietary code, credentials,
and private conversations. Use [issues](https://github.com/realfamousbae/planner/issues)
for non-sensitive problems and [security reporting](SECURITY.md) for sensitive ones.

## Development

Python 3.9+ is supported. No runtime dependencies are needed by the skill or
installer. PyYAML is used by the development validator only.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

Do not install into your real skill directories to test filesystem behavior.
Installer tests use temporary directories and must preserve existing files.
CI runs package validation and installer tests on Linux and macOS.

## Changing the workflow

Keep shared instructions in `skills/planner/SKILL.md`, mode details in
`references/`, and the handoff template in `assets/`. Keep provider-specific
settings in adapters; the installer adds Claude's explicit-only metadata.
Do not hardcode a changing model catalog or claim measured savings without data.

Preserve reliable session-settings checks, native Plan Mode, approval of the actual
plan revision, save-only handoff, and continuation from recorded progress.
Exercise affected scenarios from [validation notes](docs/VALIDATION.md).
Distinguish prompt review from actual model-driven results in your PR.

Keep the English and Russian READMEs aligned and record user-facing changes in
the Unreleased section of [the changelog](CHANGELOG.md). Never commit personal
task plans, secrets, installed skill copies, or paid API test credentials.
