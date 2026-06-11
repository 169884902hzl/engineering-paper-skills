# Positive Pattern Library

Structural skeletons for how strong engineering papers organize their
argument. These are original distillations of common published structures,
not excerpts; do not copy sentences from published papers into manuscripts.

## How to Use

- Pick one pattern per paper or section before drafting; do not blend several
  patterns into one section.
- Patterns fix order and paragraph roles. Facts, numbers, and boundaries still
  come only from the supplied evidence.
- If supplied evidence cannot fill a slot, leave an explicit placeholder
  instead of inventing filler.

## Pattern: Pipeline Systems Paper

- When to use: an integrated robot or system contribution with staged
  components and an end-to-end evaluation.
- Skeleton: task and operating condition, then the failure mode that breaks
  single-stage routes, then the system axis (what object flows through the
  stages), then per-stage claims each tied to stage evidence, then the
  integrated evaluation, then the stress or failure envelope.
- Claim ladder: stage claims stay local; only the integrated evaluation can
  support an end-to-end claim.
- Common failure: module-directory prose that lists components without naming
  what flows between them or which claim each stage carries.

## Pattern: Component Method Paper (Ablation-Led)

- When to use: one new component inside a known pipeline, with the
  contribution shown through deltas.
- Skeleton: bottleneck in the known pipeline, then the component object and
  its decision rule, then the main comparison, then an ablation ladder from
  naive to full, then a role interpretation for each major delta, then what
  the ablation does not prove.
- Claim ladder: each delta supports a component role, not a causal mechanism,
  unless isolation and statistics are supplied.
- Common failure: reading the ablation table row by row without assigning a
  contribution role to any delta.

## Pattern: Rethinking or Simplification Paper

- When to use: a strong simple baseline reframes what actually mattered in a
  task the community treats as solved by complexity.
- Skeleton: the accepted assumption, then the minimal change that questions
  it, then an equal-budget comparison, then where simplicity wins or ties,
  then the boundary where the complex route is still needed.
- Claim ladder: parity evidence supports a parity claim; do not sell parity
  as superiority.
- Common failure: claiming the field was wrong instead of showing where the
  assumption stops holding.

## Pattern: Benchmark or Dataset Paper

- When to use: the contribution is an evaluation capability, not a method.
- Skeleton: the capability gap in current evaluations, then design axes and
  coverage, then the collection or generation protocol, then reference
  results for representative methods, then diagnostic findings, then intended
  and unintended uses.
- Claim ladder: reference results support difficulty and coverage claims, not
  method superiority claims.
- Common failure: presenting the benchmark as proof that prior methods are
  weak rather than as a measurement instrument.

## Pattern: Results Narrative Ladder

- When to use: inside any Experiments section, independent of paper type.
- Skeleton: main-table claim first, then per-axis diagnosis, then
  mechanism-level interpretation where diagnostics permit, then the failure
  envelope, then the operating boundary as scientific scope.
- Claim ladder: interpretation sentences must trace to a supplied diagnostic
  axis, category split, or failure observation.
- Common failure: a paragraph of table narration with no sentence explaining
  why the ranking occurs.
