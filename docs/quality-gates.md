# Quality Gates

This repository does not require GitHub releases to be useful. The public
tracking unit is the current `main` branch plus explicit commit hashes in audit
reports.

## Required Repository Checks

```bash
python scripts/validate_repo.py
python scripts/check_expected_behavior.py --spec-dir tests/expected
python scripts/check_expected_behavior.py --spec-dir tests/expected --outputs-dir tests/outputs/golden
python scripts/check_quality_assets.py
python scripts/check_response_diff.py
python scripts/check_venue_profiles.py
python scripts/check_metadata_files.py
python scripts/write_behavior_eval_stub.py --help
```

## Behavior Evidence

Behavior evidence requires a real command template:

```bash
python scripts/run_prompt_regression.py \
  --require-command \
  --case full_paper_realistic_audit \
  --output-dir /tmp/engineering-paper-skill-regression \
  --command-template "$PROMPT_REGRESSION_COMMAND_TEMPLATE"
```

If the command template is absent, prompt regression is `NOT_RUN`. That state
must not be described as behavior proof.

When the manual behavior workflow succeeds, it writes a
`behavior_eval_stub.jsonl` artifact with the commit hash, output hash, case, and
`ci_single_run` evidence level. That stub is provenance only until a human or
semantic judge scores the output.

The repository also keeps failed local behavior attempts when they reveal a real
contract gap. For example, the `6bec865` and `80d9c23` structured-audit attempts
are recorded as `local_single_run_failed`, not as passing model runs.

## Versioning Without Releases

- Use commit hashes in external reviews and model-run records.
- Keep model-run artifacts under `tests/outputs/model_runs/`.
- Keep human or local model-run score records under `evals/results/`.
- Use `CITATION.cff` and `codemeta.json` for research-software metadata.
- Use Pages and README demo links for discovery.
- Use `KNOWN_GOOD.md` as the current commit-based beta anchor.
- Use `CHANGELOG.md` for no-release quality-gate history.

## Evidence Boundary

Golden outputs, static checks, and local model-run artifacts are review
evidence. They are not proof of stable top-tier behavior on arbitrary unseen
manuscripts.
