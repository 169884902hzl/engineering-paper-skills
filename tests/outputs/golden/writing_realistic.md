One-sentence thesis
In robotic insertion, active observation and guarded execution address target visibility loss, supported by 120-trial comparisons under the stated failure boundary.

Story spine
| Node | Section location | Claim | Evidence anchor | Boundary | If removed, what breaks? |
| Problem | Introduction | target visibility loss can interrupt insertion | source notes | insertion-only task | reader misses why observation matters |
| Gap | Introduction/Related Work | fixed-view execution is insufficient under target loss | 71% fixed-camera row | no broad prior-work claim without sources | contribution looks unnecessary |
| Insight | Methods | active observation plus guarded execution keeps the target observable during execution | observer and confidence-gate notes | mechanism not directly proven | modules read as a directory |
| Method | Methods | observer camera and guarded controller define the execution path | method notes | threshold details missing | Results cannot be interpreted |
| Evidence | Results | full system reaches 86% over 120 trials | result table | no stress-test claim | thesis lacks measured support |
| Boundary | Discussion | complete target invisibility remains outside current support | source notes | boundary must stay visible | Abstract would overclaim robustness |

Source-note triage
| Source item | Fact / Assumption / Unsupported | Can enter prose? | Handling |
| Full system 86% | Fact | yes | Results evidence |
| complete target invisibility | Fact | yes | boundary |

Methods reader path
| Block | Paragraph job | Source anchor | Missing input |
| gate | explain confidence stop | guarded controller note | threshold details |

Result paragraph
The full system reaches 86% over 120 trials, compared with 71% for the fixed camera baseline and 74% without guarded execution.

Sentence role audit
| SID | Sentence/span | Job | Claim type | Evidence anchor | Needed because | Placement | Previous link | Next obligation | Ambiguity risk | Redundancy source | AI-smell pattern | Claim-strength risk | Action | Safe rewrite | Evidence needed for stronger wording |
| S1 | The full system reaches 86% over 120 trials, compared with 71% for the fixed camera baseline and 74% without guarded execution. | Evidence | Comparative result | result table | gives the measured support for the thesis | keep in Results | follows evaluation question | interpret what this supports and what it does not | low | none | none | improvement wording must stay bounded | keep | The full system reaches 86% over 120 trials under the evaluated insertion condition, compared with 71% for the fixed-camera baseline and 74% without guarded execution. | repeated seeds, stress conditions, and statistical test |

Claim-evidence map
| Claim | First stated in | Mechanism support | Evidence support | Boundary/overclaim risk | Repair |
| guarded execution supports success | Results | confidence gate | 74% ablation row | no untested causal mechanism | bounded wording |

Unsupported or downgraded claims
- no stress-test, citation, or broader mechanism claim is available.
