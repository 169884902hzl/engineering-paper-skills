Panel-claim map
| Panel | Visible evidence | Claim supported | Must not claim |
|---|---|---|---|
| Figure 1a | RGB view | target view used by the system | reasoning, robustness, or deployment reliability |
| Figure 1b | confidence trace | confidence changes during execution | causal proof or cross-fixture performance |
| Figure 1c | guarded execution transition | state transition logic | generalization across industrial settings |

Table-claim map
| Table | Tabulated evidence | Claim supported | Must not claim |
|---|---|---|---|
| Table 1 | 84 percent full system, 69 percent fixed camera, 77 percent no gate | bounded comparison on one robot, one fixture, one object family | statistical significance, deployment reliability, or industrial generalization |

Unsupported caption claims
- `proves` is too strong for a workflow figure.
- `robustly generalizes` is unsupported because cross-fixture and lighting-change data are not supplied.
- Statistical-significance language is unsupported because p-values, confidence intervals, repeated seeds, and variance are not supplied.
- `deployment reliability` is unsupported because no deployment study is supplied.

Safe caption

Figure 1 illustrates the sensing, confidence-tracking, and guarded execution
states used by the insertion system. The figure shows the execution workflow; it
does not by itself establish robustness or generalization.

Safe table note

Table 1 reports success rates for one robot, one fixture, and one object family.
The table supports a bounded comparison under the supplied protocol, but it does
not establish statistical significance or deployment reliability without
additional uncertainty estimates and deployment evidence.
