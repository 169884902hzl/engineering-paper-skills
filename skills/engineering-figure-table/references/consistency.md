# Consistency

Use this before finalizing figures, tables, and captions.

## Coordinated Rename Rule

When a category, object class, baseline, metric, or method abbreviation changes,
update all of:

1. prose
2. table headers
3. table notes
4. figure labels
5. figure captions
6. Results discussion
7. Conclusion if the term appears there

Partial renames make the paper look stitched together.

## Caption Style

Keep caption syntax consistent across main figures and tables:

```latex
\caption{\textbf{Title.} Description.}
```

If the venue template requires another style, follow the venue.

## Table Style

Check:

- spacing parameters
- row height
- horizontal rules
- decimal precision
- metric direction
- abbreviation notes
- best-result marking

## Cross-Reference Check

For every visual:

- label exists
- text reference exists
- panel letters match
- metric names match
- caption does not introduce a new term
- visual claim is supported in Results or Methods

## Useful Scans

```bash
rg -n "success rate|Success Rate|SR" .
rg -n "Fig\\.|Figure|Table|Tab\\." .
rg -n "\\\\label\\{|\\\\ref\\{|\\\\Cref\\{" .
rg -n "baseline|ablation|w/o|without" .
```

Use scans to find inconsistent names; do not blindly replace terms without
checking meaning.
