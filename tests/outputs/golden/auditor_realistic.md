Audit verdict
- Overall status: CANNOT_DETERMINE
- Highest-risk issue: readiness and robustness claims exceed available checks
- Not verified: build log, citation list, final line numbers

Claim-evidence audit
| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Repair route |
| improves insertion success | thesis | observer and guarded controller | 86 vs 71 over 120 trials | Table result | PASS | engineering-writing |
| robust to occlusion | claims | active observation | no stress test | Fig. 5 workflow only | FAIL | engineering-writing |
| guarded execution is causal mechanism | claims | guarded controller | one ablation row | Table result | PARTIAL | engineering-writing |

Section-boundary findings
| Location | Symptom | Why it matters | Repair route |
| Methods | module list risk | reader path is needed | engineering-writing |

Figure/table findings
| Item | Claim requested | Evidence visible/tabulated | Must not claim | Repair route |
| Fig. 5 | robustness | workflow montage | robustness validation | engineering-figure-table |

Prioritized action list
| Priority | Action | Owner skill | Required input | Stop condition |
| High | downgrade robustness and readiness claims | engineering-validation | build and citation evidence | stop until checks run |
