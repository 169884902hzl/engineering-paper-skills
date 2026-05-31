# LaTeX Build

Use this for compile and output checks.

## Minimum Commands

Adapt paths to the active manuscript root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
grep -c 'bibitem' main.bbl
pdfinfo main.pdf | rg '^Pages:'
git diff --check
```

If the repo is not a git repo, say so and skip `git diff --check`.

## What to Record

- compile success or exact error
- page count
- bibliography count
- undefined references or citations
- overfull boxes if relevant
- changed output files
- whether final sync was checked

## Failure Handling

- Do not call a failed compile "mostly fine."
- Quote the first actionable error.
- After two repeated failures, change diagnosis rather than repeating commands.
