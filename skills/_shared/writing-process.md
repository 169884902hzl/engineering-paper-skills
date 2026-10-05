# Writing Process

Use this when starting a paper, deciding what to write next, or writing while
results are still incomplete. It describes the order experienced engineering
authors actually follow, which differs from "draft the Introduction first".

## Default Order

1. Lock one sentence: task, gap, mechanism, evidence, scope. Every later
   sentence either strengthens this sentence or is cut.
2. Allocate the page budget before writing prose. Fill each section of the
   venue template with placeholder blocks of the intended length, so space is
   assigned by importance (Methods and Experiments get most of it) instead of
   by whatever was drafted first.
3. Read related work early; write it late. Before the final experiments, read
   enough to choose baselines, adopt the field's canonical terms, and identify
   the nearest neighbor. Write the Related Work section after Methods and
   Experiments are stable.
4. Design the result tables before running the remaining experiments. Fix the
   rows (methods, matched controls) and columns (conditions, categories). The
   empty cells are the experiment to-do list. The table decides what to
   compare and under which conditions; the number of trials per cell comes
   from the evaluation unit, the expected variability, and the uncertainty the
   claim needs, not from the layout. Before running them, check the plan with
   [experiment-premortem.md](experiment-premortem.md).
5. Design figures from the tables. A teaser figure stays light and contrasts
   the naive approach with the proposed one. The framework figure carries the
   method and doubles as a reading guide for Methods. Qualitative figures
   show representative cases chosen by a stated criterion, including observed
   failures, next to the failure rate they illustrate. Attribute a failure to
   a cause only when there is evidence for it; if a condition produced no
   failures, say so.
6. Write Methods, then Experiments, then Introduction, then Abstract and
   Conclusion. The Abstract is written last.
7. Drafting the argument in the author's first language is fine. Rebuild it in
   English paragraph by paragraph; do not translate sentence by sentence.
8. Before submission, run [reviewer-attack-patterns.md](reviewer-attack-patterns.md)
   and the mechanical checks in `engineering-validation`.

## While Results Are Incomplete

- Keep the slot, state the expected outcome, and say how it would be
  interpreted if it holds. Mark it `[RESULT NEEDED]`.
- Abstract and Conclusion may only claim what filled cells support.
- If a hypothesis changes after the data arrive, change the story; do not keep
  prose that the data no longer support.

## Where Authorities Disagree

- First artifact: a contribution list (Peyton Jones), figures and data
  (Whitesides, Black), or a one-sentence-per-paragraph outline (Durand). For
  experiment-heavy engineering papers, starting from table slots ties every
  claim to evidence earliest.
- Related Work placement: after the idea (Peyton Jones) or near the start
  (Adelson as quoted by Freeman; Burgard et al.). IEEE robotics venues
  conventionally place it as Section II.
- Full paragraphs early: encouraged by Peyton Jones and Black, discouraged by
  Durand until the outline and figures exist. Placeholder outlines satisfy
  both.

## Sources

- S. Peyton Jones, "How to write a great research paper":
  https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/How-to-write-a-great-research-paper.pdf
- G. M. Whitesides, "Whitesides' Group: Writing a Paper," Adv. Mater. 2004,
  doi:10.1002/adma.200400767
- F. Durand, "Notes on writing": https://people.csail.mit.edu/fredo/PUBLI/writing.pdf
- W. Freeman, "How to write a good CVPR submission" (quotes Adelson)
- W. Burgard et al., "How to Write a Paper," Freiburg robotics course:
  http://ais.informatik.uni-freiburg.de/teaching/ws11/robotics2/pdfs/rob2-23-how-to-write-a-paper.pdf
- M. Black, "Writing a good scientific paper":
  https://perceiving-systems.blog/en/post/writing-a-good-scientific-paper
