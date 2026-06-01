Audit verdict
- Overall status: CANNOT_DETERMINE
- Highest-risk issue: readiness and robustness claims exceed available checks
- Not verified: build log, citation list, final line numbers

Story-spine findings
| Story node | Finding | Evidence anchor | Risk | Repair route |
| Problem | visibility-loss task is present | draft problem statement | acceptable | engineering-writing |
| Gap | fixed-view gap is only partially supported | 71% fixed-camera row | weak if Related Work makes broad claims | engineering-writing |
| Insight | active observation plus guarded execution is stated | Methods draft | needs reader path | engineering-writing |
| Evidence | 86 vs 71 supports bounded success improvement | Table result | does not establish robustness | engineering-writing |
| Boundary | stress/failure scope is missing | no stress-test evidence | Abstract and Conclusion may overclaim | engineering-validation |

Claim-evidence audit
| Claim | First stated | Method anchor | Experiment anchor | Figure/table anchor | Status | Repair route |
| improves insertion success | thesis | observer and guarded controller | 86 vs 71 over 120 trials | Table result | PASS | engineering-writing |
| robust to occlusion | claims | active observation | no stress test | Fig. 5 workflow only | FAIL | engineering-writing |
| guarded execution is causal mechanism | claims | guarded controller | one ablation row | Table result | PARTIAL | engineering-writing |

Sentence role findings
| Sentence/span | Issue | Evidence anchor | Action | Safe wording |
| robust to occlusion | generalization claim without stress protocol | none | downgrade | improves success in the evaluated visibility-loss setting |
| causal-mechanism proof claim | causality claim from one ablation row | Table result only | hedge | is consistent with the guarded-execution contribution |

Section-boundary findings
| Location | Symptom | Why it matters | Repair route |
| Methods | module list risk | reader path is needed | engineering-writing |

Figure/table findings
| Item | Claim requested | Evidence visible/tabulated | Must not claim | Repair route |
| Fig. 5 | robustness | workflow montage | robustness validation | engineering-figure-table |

Prioritized action list
| Priority | Action | Owner skill | Required input | Stop condition |
| High | downgrade robustness and readiness claims | engineering-validation | build and citation evidence | stop until checks run |
