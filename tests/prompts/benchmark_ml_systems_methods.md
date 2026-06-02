# Benchmark ML Systems Methods Prompt

Use $engineering-writing to draft a Methods overview paragraph first.

Paper type:
ML systems paper.

Task:
Reduce stale feature reads in an online ranking service.

Method notes:

- input: request-level feature keys, cache state, and freshness metadata
- intermediate object: a freshness-aware feature bundle
- transformation: check local cache, fetch only stale keys, merge fresh values
  with cached values, and pass the bundle to the ranker
- safety boundary: if fetch fails, the service falls back to cached values and
  marks the request for logging
- no latency numbers, formulas, production incident counts, or SLA claims are
  supplied
- rough concern: do not write a component inventory

Requirements:

- Start from the organizing principle.
- Explain input -> intermediate object -> transformation -> handoff ->
  execution boundary.
- Do not invent latency, thresholds, formulas, or deployment guarantees.
