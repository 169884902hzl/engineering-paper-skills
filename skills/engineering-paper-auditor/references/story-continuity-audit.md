# Story Continuity Audit

Use this when a manuscript sounds polished but the paper story may be broken.

## Audit

```text
Story continuity audit
| Story node | Where promised | Where explained | Where proved | Boundary | Status | Repair |
```

Mark `FAIL` when a node is promised but not proved, or proved without having
been motivated.

## Common Breaks

- Abstract promises robustness, but Experiments only show one condition.
- Introduction claims a gap, but Related Work does not name the nearest route.
- Methods introduce modules, but no mechanism links them to the gap.
- Results show metrics, but no paragraph states which contribution is proven.
- Conclusion restates a stronger claim than Results support.
