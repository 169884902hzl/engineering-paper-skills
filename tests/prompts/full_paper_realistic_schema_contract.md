Use $engineering-paper-auditor to audit
`tests/fixtures/full_paper/robot_active_observation_realistic_8page.md`.

Return JSON only. Do not return Markdown.

The JSON object must contain:

- `verdict`
- `claim_evidence`
- `paragraph_transitions`
- `section_dependencies`
- `response_truthfulness`
- `validation_status`

Rules:

- Every `claim_evidence` row must include `claim_id`, `claim`, `status`,
  `source_span`, `evidence_span`, `evidence_anchor`, `decision`,
  `forbidden_strengthening`, and `repair`.
- Every `paragraph_transitions` row must include `from`, `to`, `relation`,
  `issue`, `terminology_drift`, `claim_strength_drift`, and `repair`.
- Every `response_truthfulness` row must include `reviewer_comment_id`,
  `complaint_type`, `response_claim`, `status`, `old_problem_span`,
  `new_fix_span`, `semantic_match`, `manuscript_anchor`, `remaining_gap`, and
  `repair`.
- Every `section_dependencies` row must include `section`, `promise`, `proof`,
  `boundary`, and `status`.
- `validation_status` must include machine-readable fields:
  `overall_readiness`, `build`, `citations`, `official_venue_policy`,
  `response_diff`, and `final_line_numbers`.
- If the supplied fixture does not include a build log, bibliography/source
  metadata, official venue instructions, revised manuscript diff, or final line
  numbers, set the corresponding fields to `NOT_RUN`.
- Set `overall_readiness` to `CANNOT_DETERMINE`, `NOT_READY`, or
  `CANNOT_MARK_READY`; do not use `READY`.
- `source_span`, `evidence_span`, `old_problem_span`, and `new_fix_span` must
  be copied or tightly quoted from the supplied fixture when available.
- Do not claim build, citation verification, official venue policy checks,
  stress-test completion, final line-number verification, or response-diff
  verification unless those artifacts are supplied and inspected.
