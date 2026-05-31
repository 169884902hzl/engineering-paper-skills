# Shared Citation Boundary

Use this whenever the task mentions references, related work, prior work, or
citation support.

## Rules

- Do not invent citations, author names, venues, years, titles, DOIs, or BibTeX.
- Use only sources provided by the user, sources already present in the project,
  or sources found through an explicit source-grounded search.
- If no source is available, write a taxonomy scaffold with citation
  placeholders.
- Separate literature positioning from manuscript claims.

## Safe Placeholder

```text
[citation needed: source-grounded paper supporting this route or limitation]
```

## Source-Grounded Search Record

When search is available, keep enough evidence to avoid citation drift:

```text
| Query | Source | Verified claim | Citation placeholder | Notes |
|---|---|---|---|---|
```

The verified claim must be narrower than or equal to what the source actually
supports.

## Related Work Output

```text
| Axis | Provided/verified sources | What they solve | Remaining gap | Relation to this work |
```

Never fill the source column with plausible but unchecked papers.
