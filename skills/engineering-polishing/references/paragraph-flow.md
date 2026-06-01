# Paragraph Flow

Use this when prose is hard to follow.

For sentence-level necessity, placement, and non-redundancy checks, use
[`../../_shared/sentence-role-and-story-flow.md`](../../_shared/sentence-role-and-story-flow.md).

## Reverse Outline

For each paragraph, identify:

- job: background, gap, method, evidence, interpretation, limitation, transition
- first sentence role
- evidence anchor
- final sentence role

If the paragraph has two jobs, split it.

## Flow Patterns

Useful patterns:

- `claim -> evidence -> interpretation -> boundary`
- `problem -> limitation of prior route -> proposed route`
- `setup -> comparison -> observed pattern -> implication`
- `mechanism -> operating condition -> downstream role`
- `need -> conflict -> prior limitation -> this work -> method path -> result`

Avoid:

- list of modules without relation
- result numbers without interpretation
- repeated sentence skeletons
- paragraph ending that does not connect to the next point

## First Sentence Test

The first sentence should tell the reader what the paragraph will do. If it only
uses a vague phrase such as `This is important`, rewrite it around the concrete
object and claim.

## Concrete Support Rule

After an abstract judgment, add a concrete object, metric, mechanism,
constraint, or scenario. Do not leave words such as `important`, `effective`,
`improved`, or `optimized` alone.

## Source Anchor Check

If a Results paragraph invokes prior theory, a mechanism explanation, or a
field-level interpretation, add a source anchor:

- measured result in this paper
- cited prior work
- explicit hypothesis or limitation

Without one of these, keep the interpretation local and hedged.

## Sentence Chain Check

After reverse outlining, audit each sentence:

```text
Sentence role audit
| Sentence/span | Job | Needed because | Connection to previous/next | Evidence boundary | Action |
```

Use `delete` for decorative repetition, `add bridge` when the reader can jump
to a wrong conclusion, and `move` when a sentence belongs to another section or
paragraph.
