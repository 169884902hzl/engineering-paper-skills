# Related Work

Use this for English Related Work or literature positioning folded into the
Introduction.

## Folded or Standalone

Fold into Introduction when:

- page budget is tight
- the gap can be established in one or two paragraphs
- a full taxonomy would distract from the main argument

Use standalone Related Work when:

- the paper crosses several technical axes
- a taxonomy improves positioning
- nearest-neighbor distinction is central to the contribution

## Standalone Structure

1. Axis A: what this class solves and what remains missing.
2. Axis B: how this class differs and why it still misses the target setting.
3. Nearest-neighbor work: most similar prior work and the exact distinction.
4. Gap bridge: what combination remains uncovered.

## Paragraph Pattern

```text
[Work class] addresses [problem] by [common mechanism]. These methods are
effective when [condition], but they still assume [limitation]. This leaves
[specific gap] unresolved for [this paper's setting].
```

## Avoid

- paper-by-paper lists
- chronological ordering unless history is the argument
- hiding the nearest neighbor in a citation string
- ending a paragraph without a limitation or distinction
- writing that a paper is "inspired by" another work without stating the
  technical difference

## Source-Learning Card

For each neighboring paper, record:

| Paper | Technical axes | Nearest neighbor location | Segment-ending gap | Bridge back to this work |
|---|---|---|---|---|

If the note only contains author names and one-sentence summaries, it is not a
useful Related Work extraction.

## Citation Boundary

- Do not invent references, authors, titles, venues, years, or BibTeX entries.
- Use only papers provided by the user, already present in the manuscript, or
  found through an explicit source-grounded search.
- If sources are not available, write a taxonomy scaffold with citation
  placeholders.

Use:

```text
| Axis | Provided or verified sources | What they solve | Remaining gap | Our distinction |
```
