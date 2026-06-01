# Open Source QA

Run these checks before publishing, tagging, or accepting a pull request.

## Repository QA

```bash
python scripts/validate_repo.py
python scripts/check_expected_behavior.py --spec-dir tests/expected
python scripts/check_expected_behavior.py --spec-dir tests/expected --outputs-dir tests/outputs/golden
python scripts/check_quality_assets.py
python scripts/check_response_diff.py
python scripts/check_venue_profiles.py
python scripts/check_metadata_files.py
python scripts/write_behavior_eval_stub.py --help
python scripts/run_prompt_regression.py
```

This checks:

- required skill files
- `SKILL.md` frontmatter and reference tables
- relative Markdown links
- agent metadata fields
- private-path and stale-wording patterns
- structured expected minimal, realistic, and adversarial prompt specs
- optional prompt regression output checks when outputs are provided
- golden output snapshots under `tests/outputs/golden`
- long-form flawed manuscript fixtures under `tests/fixtures/long`
- full-paper flawed manuscript fixture and full-paper golden audit
- recorded gold-fixture review results under `evals/results`
- recorded local model-run outputs under `tests/outputs/model_runs`
- model-run review records under `evals/results`
- response diff fixture and response-truthfulness sanity check
- venue profile JSON files that require official source URL and source date
- venue profile structure through `scripts/check_venue_profiles.py`
- metadata, Pages, sitemap, robots, workflow, CFF, changelog, and known-good
  commit structure through `scripts/check_metadata_files.py`
- manual top-tier writing rubric under `evals/`
- structured semantic expectations in selected `tests/expected/*.yaml` specs
- behavior-regression eval-stub writer interface for CI/manual artifacts

These checks are repository-quality checks. Golden outputs and recorded model
runs are review artifacts; they do not prove stable behavior on arbitrary
unseen full manuscripts. Treat prompt regression as behavior evidence only when
`scripts/run_prompt_regression.py` is executed with a real command template and
the resulting outputs are scored.

## Behavior Regression

Main CI includes an optional prompt-regression step. It runs only when the
repository has a `PROMPT_REGRESSION_COMMAND_TEMPLATE` GitHub Actions secret.
The separate `Behavior Regression` workflow can also be triggered manually; it
fails if the command template secret is missing and uploads the generated
regression outputs as a workflow artifact. On a successful behavior run, it
also writes `behavior_eval_stub.jsonl` with the commit hash, output hash,
artifact name, and `ci_single_run` evidence level. That stub is not a quality
score until a human or semantic review is added.

This repository does not require GitHub releases. For external reviews, use the
current `main` commit hash plus the recorded model-run and eval artifacts. See
`docs/quality-gates.md` for the no-release quality contract.

The command template must accept `{prompt}`, `{output}`, and `{name}`
placeholders. Example shape:

```bash
python scripts/run_prompt_regression.py \
  --require-command \
  --case full_paper_realistic_audit \
  --output-dir /tmp/engineering-paper-skill-regression \
  --command-template "$PROMPT_REGRESSION_COMMAND_TEMPLATE"
```

If the secret is not configured, CI prints that behavior regression was not run.
That state must not be described as behavior proof.

## Codex Skill Validation

```bash
for s in skills/engineering-*; do
  python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$s"
done
```

## Manual Scans

```bash
rg -n "TO[D]O|\\[TO[D]O\\]|dissertio[n]|Us[e] -" skills
rg -n "[\\p{Han}]" skills
```

For this package, validation was run on both installed skill sources and copied
package skill directories:

- `engineering-paper-auditor`
- `engineering-writing`
- `engineering-polishing`
- `engineering-figure-table`
- `engineering-response`
- `engineering-validation`
- `engineering-paper-router`

The shared reference directory `skills/_shared/` is also checked by repository
QA and should be copied during installation.

All returned `Skill is valid!` during the hardening pass.

## Manual Review Checklist

- Each skill has a focused trigger description.
- Each skill states handoff boundaries to the other skills.
- Each skill keeps the entry `SKILL.md` concise and routes details to
  `references/`.
- Each skill has examples and failure modes.
- English manuscript output is the default.
- Fact-boundary rules are explicit.
- Claim-evidence mapping is explicit.
- Figure/table responsibility is explicit.
- Comment-response workflow requires acceptance evidence.
- Validation workflow requires fresh command evidence.
- Validation outputs distinguish `PASS`, `FAIL`, `PARTIAL`, `NOT_RUN`, and
  `UNKNOWN`.
- Minimal and adversarial prompt specs still match the intended behavior.
- Expected prompt behavior uses structured `.yaml` specs with forbidden claims,
  forbidden regexes, forbidden claim patterns, required sections, status
  expectations, and allowed behavior.
- Third-party license notices are preserved.
