# Venue Checklist

Use this when the target venue family is known or the user asks whether a paper
is safe to submit.

```text
Venue readiness check
| Venue family | Required item | Official source URL | Source date | Evidence checked | Status | Fix |
```

Check items commonly include page limit, anonymity, supplement policy,
reproducibility checklist, limitations, ethics or impact statement, AI-tool
disclosure, citation integrity, and figure/table formatting.

If the official venue instructions were not inspected in this session, mark the
venue check `NOT_RUN` or `PARTIAL`.

## Official-Policy Mode

For a named venue, do not rely only on the static profile files. Inspect the
current official venue page or state that the official policy check was not run.

```text
Official policy check
| Venue | Source URL | Source date | Requirement | Evidence in manuscript | Status | Fix |
```

Required statuses:

- `PASS`: the official page was inspected in this session and the manuscript
  evidence satisfies the requirement.
- `FAIL`: the official page was inspected and the manuscript conflicts with the
  requirement.
- `PARTIAL`: the official page was inspected but manuscript evidence is
  incomplete.
- `NOT_RUN`: the official page was not inspected.

## Venue Profiles To Instantiate

Use these as conservative prompts for what to verify. They are not substitutes
for current official venue instructions.

| Venue family | Required checks | Common failure |
|---|---|---|
| Nature / Science / Cell style | summary claim scope, Methods sufficiency, figure legend clarity, data/code availability, AI-use disclosure and human accountability | broad significance stated without independent evidence |
| NeurIPS / ICML / ICLR | checklist, limitations, assumptions, reproducibility, baselines, variance/statistics, data/code policy, ethics/LLM-use statement when applicable | benchmark result written as deployment reliability |
| CoRL / ICRA / IROS / RA-L / RSS | page limit, anonymity when applicable, real-robot protocol, trial count, failure modes, hardware/task scope, AI-use policy, rebuttal/revision stage boundary | one robot or one fixture written as general robustness |
| IEEE / ACM systems | artifact/reproducibility policy, workload, baseline fairness, measured tradeoffs, configuration details | architecture described like product reliability |

## Output Expansion

```text
Venue readiness check
| Requirement | Evidence inspected | Status | Blocking issue | Next action |
```

If page count, bibliography, final PDF, venue policy, or AI disclosure text is
not available, keep the venue readiness result `NOT_RUN` or `PARTIAL`.

## Profile Files

The repository includes static profile prompts under
`skills/engineering-validation/venue_profiles/`. They are reminders of fields
to verify, not official policy snapshots. If the user needs readiness for a
specific venue, inspect the current official venue instructions in the current
session or mark official policy verification `NOT_RUN`.
