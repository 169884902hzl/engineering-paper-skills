# Adding Experience From Private Material

1. Keep raw reviews, unpublished manuscripts, identifying terms, and working
   notes outside this repository. The test fixtures are entirely invented.
2. Generalize each useful lesson into a **trigger**, an **objection**, and a
   **fix**. Describe the pattern, never the paper: omit task, robot, model, and
   method names, and all numbers from the paper.
3. Paraphrase the reasoning in your own words. Do not quote confidential
   reviews or copy manuscript passages.
4. Tag evidence with aggregate counts, such as `review 2/2`, rather than
   identities or source details. Use the structure in
   [Reviewer Attack Patterns](../../skills/_shared/reviewer-attack-patterns.md).
5. Before committing, run the overlap checker from the repository root with
   every relevant private file and a terms file containing distinctive names,
   one per line. For example, keep those inputs in a sibling directory:

   ```sh
   python3 scripts/check_private_overlap.py --private ../private-material/manuscript.tex ../private-material/reviews.txt --terms ../private-material/terms.txt
   ```

   The default checks six-word overlaps and whole-word terms across tracked
   and untracked non-ignored text files. Resolve every hit by generalizing or
   paraphrasing. Use `--allow ../private-material/generic-phrases.txt` only for
   genuinely generic wording, one phrase per line; a longer allowed phrase
   covers its contained matches. `--paths` narrows the scan to selected files
   or directories; `--json` produces structured results. Inputs are excluded
   from scanning. The checker writes no files and reports only repository
   locations and matched phrases or terms. Avoid saving its output in the
   repository because a reported match may itself be private.

   PDF input requires `pdftotext`; an unavailable converter produces a warning
   and skips that PDF. Convert or check skipped inputs before committing.
   Exit codes are `1` for overlaps, `0` for no detected overlaps, and `2` for
   an input or scan error. A clean scan still needs human review for identifying
   details that do not share wording.
6. Run the repository checks:

   ```sh
   python3 scripts/validate_repo.py
   ```

7. Git history is public. If a leak was pushed, adding a removal commit is
   insufficient: rewrite the affected history and coordinate cleanup of
   published copies.
