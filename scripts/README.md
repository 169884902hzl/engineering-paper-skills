# Maintainer-only QA scripts

Normal skill users do not need to run anything in this directory.

These scripts exist to validate repository structure, provenance labels, demo
artifacts, expected behavior fixtures, venue profile metadata, response-diff
fixtures, and reviewer-facing evidence. They are for maintainers and external
reviewers of this repository, not for ordinary Codex skill use.

For normal use, install the skill folders:

```bash
cp -a skills/_shared skills/engineering-* ~/.codex/skills/
```

Then call a skill such as `$engineering-paper-coach` or
`$engineering-writing` from Codex.

## Script roles

| Script | Role |
|---|---|
| `validate_repo.py` | Checks skill structure, links, prompt coverage, and private/stale patterns. |
| `check_expected_behavior.py` | Validates expected-behavior specs and golden outputs. |
| `check_quality_assets.py` | Checks demo artifacts, eval records, fixtures, documentation markers, and quality evidence. |
| `check_response_diff.py` | Checks old/new manuscript response-diff fixtures and annotations. |
| `check_venue_profiles.py` | Checks static venue profile metadata and optional source URL reachability. |
| `check_metadata_files.py` | Checks citation metadata, Pages discovery files, workflows, and no-release docs. |
| `run_prompt_regression.py` | Optional model-run entry point when a real command template is configured. |
| `write_behavior_eval_stub.py` | Writes provenance records for manual behavior-regression artifacts. |

These checks are review evidence. They do not certify stable behavior on
arbitrary unseen manuscripts.
