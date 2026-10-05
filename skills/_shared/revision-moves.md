# Revision Moves

Use this when revising an existing draft. Revise from global to local: wording
polish is wasted on a sentence that a structural change will delete.

## Order

1. Argument. Check that the one-sentence contribution still holds. Build a
   reverse outline: write each paragraph's main point in one line, then check
   that the topic sentence says that point, that no two paragraphs carry the
   same point, and that the order follows the argument.
2. Evidence design. Run [reviewer-attack-patterns.md](reviewer-attack-patterns.md).
   Fix comparisons, assumptions, and missing measurements before softening
   any verbs.
3. Section moves (below).
4. Sentences (below).
5. Mechanical checks: numbering order, cross-references, labels, citations,
   build (`engineering-validation`).

## Section Moves From Expert Revisions

These moves were observed in a senior author's revision of a robotics draft.
Use them as options to check, not as a template.

1. Cut the "tool X has become powerful" paragraph from the Introduction.
   Derive what the method must provide from the task difficulty just
   described, then present the method as meeting that requirement. The
   problem drives the story, not the tool.
2. State the key idea in the Introduction as the principle it changes (what is
   replaced by what), and keep the sequence of operations for Methods. A claim
   that only holds through a derivation belongs in Methods.
3. Adopt the field's canonical term, the one used in surveys and titles,
   instead of a near-synonym. Reviewers and search engines both look for it.
4. Support external and contestable claims in the Introduction with sources
   the author has supplied and verified; replace placeholder citations with
   such sources before polishing. Claims about this paper's own method or
   results point to its sections, not to outside literature.
5. Make each contribution a testable sentence. The system, the mechanism, and
   the evidence are useful lenses for checking the list, but the number of
   contributions follows the independent, supported advances, and validation
   alone is not a separate innovation.
6. In Related Work, give the nearest neighbors as much detail as the
   positioning needs and summarize distant work briefly. State only
   limitations or differences the sources support; a difference can be cost
   or applicability rather than a missing capability. Close the section by
   pointing to the paper's formulation.
7. In Methods, use one symbol for each actor or model throughout, and formalize
   interfaces (inputs, outputs, output schema) so later sections can refer to
   them precisely.
8. In Results, write cumulative ablations as "adding X changes success from a
   to b", followed by the interpretation the evidence supports and a pointer
   to the qualitative figure; note that the order of addition matters. For
   each robustness axis: the trend, the likely route by which the factor
   affects the method (as an interpretation unless measured), what still
   works, and representative examples, including observed failures.

## From Numbers To Findings

In a blind writing test, expert results paragraphs made these moves and model
drafts written from the same notes mostly did not. Each move needs support in
the data at hand; when the data do not isolate the cause, write it as an
interpretation ("suggests", "is consistent with").

- Name the bottleneck from the largest delta: the component that adds the most
  points points to where the problem was.
- Attribute a gain to the stage it can affect: a module that only executes
  improves realization, not reasoning, when the predictions themselves are
  unchanged.
- Read flat results across a factor as robustness to that factor within the
  tested range, and state the range.
- Give a verdict per method family when several methods of one family behave
  alike, and name the exception.
- Use a concessive contrast when a method that scores lower shows a property
  worth keeping ("X scores lower, yet its maps are the least sensitive to
  noise").
- Close the section with the lesson for the field or the next design
  direction, hedged, instead of ending on a restated number.
- When criticizing prior datasets or methods, name the concrete shortcoming
  (unrealistic alignment, fixed lighting) rather than a vague limitation.

## Sentence Level

- Put old, linking information at the start of a sentence and the new point at
  the end, where readers place emphasis. Keep subject and verb close (Gopen
  and Swan).
- Make the actors subjects and the actions verbs; unpack nominalizations
  (Williams).
- One term per concept across the paper; see
  [terminology-ledger.md](terminology-ledger.md).
- Check single words that change the technical claim: "dedicated" or
  "additional" implies added hardware; "verify" implies correctness checking;
  "generalization" implies held-out conditions.
- For authors writing in a second language, the largest problems are usually
  sentence construction, word choice, and cohesion between sentences. Check
  those before grammar.

## Do Not Over-Correct

- Do not soften verbs to compensate for an unfair comparison; fix the
  comparison or demote the claim.
- Do not end paragraphs with disclaimers or repeat them in adjacent
  sentences. Keep the necessary scope where a passage is read on its own:
  the Abstract, the headline result, and the Conclusion.
- Treat automated style and grammar flags as suggestions. In one author's
  multi-round experience, structural suggestions from AI reviewers were
  usually right, while 20-30% of style and grammar flags were false positives
  (for example, flagging a standard "where" clause after an equation).

## Sources

- G. Gopen and J. Swan, "The Science of Scientific Writing," American
  Scientist, 1990.
- J. Williams, "Style: Lessons in Clarity and Grace."
- Reverse outlining: https://dept.writing.wisc.edu/wac/using-a-reverse-outline-to-revise/
- Writing difficulties of Chinese science and engineering academics, PLOS One
  2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12111667/
