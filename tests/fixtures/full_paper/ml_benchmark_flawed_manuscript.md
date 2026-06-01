# Full-Paper Fixture: Retrieval-Augmented Policy Learning Benchmark

This synthetic fixture tests whether the skills can audit a machine-learning
benchmark paper rather than only a robotics systems paper. It intentionally
mixes benchmark, method, dataset, and deployment claims.

## Evidence Packet

The authors introduce a retrieval-augmented policy-learning benchmark for
offline robot-control datasets. The method retrieves similar training episodes
before policy decoding. The completed experiments cover two public simulation
datasets and one small internal tabletop dataset. The main reported metric is
task success. Retrieval improves average simulated success from 62 percent to
68 percent on Dataset A and from 55 percent to 59 percent on Dataset B. On the
internal tabletop dataset, retrieval improves success from 41 percent to 46
percent across 30 evaluation episodes. The authors did not run real-robot
rollouts, did not compare against the strongest current retrieval baseline, did
not report confidence intervals, and did not release the internal dataset. The
paper includes a planned user study and a planned cross-domain transfer table,
but neither is complete.

## Draft Abstract

We present the first general retrieval-augmented benchmark for reliable robot
policy learning across simulation and real-world deployment. Our method
retrieves relevant demonstrations and enables robust generalization across
tasks, datasets, and embodiments. Extensive experiments show consistent gains
over strong baselines, and a tabletop evaluation demonstrates transfer to real
robot settings. The benchmark establishes retrieval as a scalable foundation
for deployable robot learning.

## Draft Introduction

Offline policy learning has become a central route for scaling robot behavior.
However, policies trained on heterogeneous demonstrations often fail when the
current observation differs from the training distribution. Retrieval provides a
natural mechanism for conditioning a policy on related prior experience. The
paper therefore proposes a retrieval-augmented benchmark for studying when
example-based context improves robot policy learning.

The current introduction claims that existing datasets do not evaluate
retrieval under realistic robot deployment. That claim is not yet grounded in
verified nearest-neighbor work. The draft lists behavior cloning, diffusion
policies, retrieval-augmented language models, and offline RL as related
topics, but it does not identify the closest retrieval policy papers or explain
whether the contribution is a benchmark, a retrieval method, or an empirical
analysis.

## Draft Methods

The method encodes the current observation, searches a demonstration memory,
selects the top-k neighbors, and passes the retrieved context to the policy
decoder. The draft calls this a general retrieval policy architecture. However,
the implementation uses a fixed embedding model, a fixed k, and a single
concatenation strategy. No ablation isolates embedding quality, retrieval k,
context length, or decoder architecture. The method section therefore reads as
a reasonable system recipe but not yet as a general architecture.

## Draft Experiments

The paper evaluates three datasets. Dataset A and Dataset B are simulation
benchmarks. The internal tabletop dataset has only 30 evaluation episodes. The
paper reports average success rates but does not report seeds, confidence
intervals, per-task variance, or failure categories. The results support a
bounded claim that retrieval improves average success in the evaluated
conditions. They do not support reliable deployment, broad embodiment transfer,
or superiority over the strongest retrieval baselines.

Table 1 reports the main success rates. Table 2 is planned for cross-domain
transfer but has no completed data. Figure 2 shows a retrieval workflow. Figure
3 plots aggregate success rates. The current caption for Figure 3 says the
method "proves scalable transfer," which is stronger than the supplied results.

## Draft Discussion

The benchmark is useful if positioned as an empirical probe of retrieval under
specified datasets. The current discussion instead claims that retrieval is a
general foundation for deployable robot learning. A stronger paper would state
the narrower contribution, explain dataset limits, and use the missing
strong-baseline comparison as a limitation rather than hiding it.

## Draft Conclusion

The draft concludes that retrieval-augmented policy learning is ready to scale
robot behavior across simulation and deployment. The supplied evidence supports
a narrower conclusion: retrieval improves average success in the evaluated
simulation datasets and one small internal tabletop dataset, with major
baseline, uncertainty, reproducibility, and deployment limits still unresolved.

## Reviewer Comments

**R1.** The paper claims deployment and embodiment generalization, but the
experiments are mostly simulation and one small internal tabletop dataset.

**R2.** The nearest retrieval-policy baselines are missing, so the benchmark
positioning is not convincing.

**R3.** The response claims Table 2, confidence intervals, and internal dataset
release were added, but these artifacts are not supplied.

## Draft Response Letter

We added the cross-domain transfer table, released the internal dataset, and
clarified that the method is deployment-ready. We also added confidence
intervals and compared to the strongest retrieval baseline.
