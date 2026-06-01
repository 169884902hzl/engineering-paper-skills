# Venue Checklist

Use this when the target venue family is known or the user asks whether a paper
is safe to submit.

```text
Venue readiness check
| Venue family | Required item | Evidence checked | Status | Fix |
```

Check items commonly include page limit, anonymity, supplement policy,
reproducibility checklist, limitations, ethics or impact statement, AI-tool
disclosure, citation integrity, and figure/table formatting.

If the official venue instructions were not inspected in this session, mark the
venue check `NOT_RUN` or `PARTIAL`.

## Venue Profiles To Instantiate

Use these as conservative prompts for what to verify. They are not substitutes
for current official venue instructions.

| Venue family | Required checks | Common failure |
|---|---|---|
| Nature / Science / Cell style | summary claim scope, Methods sufficiency, figure legend clarity, data availability, AI-use disclosure | broad significance stated without independent evidence |
| NeurIPS / ICML / ICLR | checklist, limitations, assumptions, reproducibility, baselines, variance/statistics, data/code policy | benchmark result written as deployment reliability |
| CoRL / ICRA / IROS / RA-L / RSS | page limit, anonymity when applicable, real-robot protocol, trial count, failure modes, hardware/task scope, AI-use policy | one robot or one fixture written as general robustness |
| IEEE / ACM systems | artifact/reproducibility policy, workload, baseline fairness, measured tradeoffs, configuration details | architecture described like product reliability |

## Output Expansion

```text
Venue readiness check
| Requirement | Evidence inspected | Status | Blocking issue | Next action |
```

If page count, bibliography, final PDF, venue policy, or AI disclosure text is
not available, keep the venue readiness result `NOT_RUN` or `PARTIAL`.
