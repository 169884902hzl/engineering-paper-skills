## Draft

We presented a suction bin-picking pipeline for transparent and reflective parts that plans grasps from one overhead depth camera. The method combines depth completion, collision-aware candidate re-ranking, a surface-normal consistency filter, and seal-pressure retry to turn incomplete depth on difficult surfaces into executable suction picks. In the supplied evaluation, the full system achieved 81% average pick success compared with 38% for the best learned grasp baseline, and the ablation results show that depth completion and candidate re-ranking are important to the final performance. These results support a bounded claim that recovering surface geometry before grasp selection improves picking reliability under the tested bin conditions.

The current method remains limited by part geometry, part arrangement, and evaluation scope. Small parts with highly curved surfaces and densely interlocked parts remain difficult, and the evidence comes from one real robot platform without an industrial deployment evaluation. Future work should therefore focus on seal prediction for curved surfaces and separation strategies for interlocked parts, and on testing the pipeline across additional robot platforms and part families.

## Why this works

- Paragraph job: two-paragraph Conclusion.
- Claim flow: method -> strongest evidence -> bounded takeaway -> assumptions and future work.
- Why this order: the boundary follows directly from the supplied robustness limits.

## Evidence used

- Method components supplied in the prompt.
- 81% full-system success and 38% best learned grasp baseline.
- Ablation note about depth completion and candidate re-ranking.
- Boundary notes about curved small parts, interlocked parts, one platform, and no deployment evaluation.

## Boundary / do-not-claim

- Do not introduce new modules, benchmarks, or results.
- Do not claim deployment validation.
- Do not claim that all curved-part or interlocked-part cases are solved.
