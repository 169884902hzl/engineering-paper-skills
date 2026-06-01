# Structured Contract Failure Analysis

This note records why the local structured behavior attempts were kept as
evidence instead of being converted into passing results.

## What The Model Got Right

- It identified the central overclaim pattern: local evidence from one robot,
  one fixture, and one object family was strengthened into broad industrial,
  general, causal, and deployment-ready claims.
- It refused to verify citations, LaTeX build status, source data, official
  venue policy, final line numbers, and response-diff claims that were not
  supplied.
- It produced useful audit structure: claim evidence, paragraph transitions,
  section dependencies, response truthfulness, and validation status.

## What The Strict Contract Rejected

- The output did not always use the exact expected readiness field or label.
- Several claim rows used reasonable audit categories but did not match the
  hidden gold `claim_id`, `status`, `decision`, `source_span`, and
  `evidence_span` values exactly.
- Some source and evidence spans were semantically relevant but not the exact
  hidden gold span.
- Some paragraph-transition and response-truthfulness rows covered the right
  issue family but not the exact expected row.

## Evaluation Design Diagnosis

The failure is useful because it separates three different checks:

- strict schema checks: JSON validity, required keys, required fields, and
  status vocabulary;
- grounded evidence checks: whether source and evidence spans are traceable to
  the fixture or author evidence packet;
- behavior checks: whether the model found the core overclaims, false response
  claims, missing verification, and safe repair direction.

The old contract over-weighted exact hidden-gold row matching. That is useful
for a parser test, but too brittle for model behavior evidence because multiple
audit rows can correctly identify the same manuscript problem.

## Current Contract Direction

- Keep schema checks strict.
- Keep span grounding strict enough to reject invented spans, but allow
  fixture-contained spans and high source-token coverage rather than only exact
  hidden-gold strings.
- Evaluate behavior by issue class and status class, such as unsupported
  overclaim, bounded support, unverifiable response, and not-ready validation.
- Treat local model-run artifacts as behavior evidence, not readiness proof.

## Remaining Limit

This still does not prove top-tier readiness. A stronger claim would require
CI-controlled model runs, de-identified real manuscript excerpts, independent
human scoring, and official venue or citation checks when those claims are
made.
