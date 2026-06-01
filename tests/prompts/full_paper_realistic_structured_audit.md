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
  `evidence_anchor`, and `repair`.
- Every `paragraph_transitions` row must include `from`, `to`, `relation`,
  `issue`, and `repair`.
- Every `response_truthfulness` row must include `response_claim`, `status`,
  `manuscript_anchor`, and `repair`.
- Every `section_dependencies` row must include `section`, `promise`, `proof`,
  `boundary`, and `status`.
- Do not claim build, citation verification, official venue policy checks,
  stress-test completion, final line-number verification, or response-diff
  verification unless those artifacts are supplied and inspected.
