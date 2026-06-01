# Full-Paper Fixture: Low-Latency Dataflow Runtime for Robot Logs

This synthetic fixture tests whether the skills can audit a systems-style
engineering paper with artifact, latency, reproducibility, and deployment
claims.

## Evidence Packet

The authors implemented a dataflow runtime for replaying large robot logs. The
runtime stores compressed camera frames, joint states, and metadata in chunked
files. The completed evaluation uses one workstation, two public log datasets,
and one lab dataset. The runtime reduces median query latency from 420 ms to
170 ms on Dataset A and from 510 ms to 220 ms on Dataset B. Throughput improves
for sequential replay but not for random access under small batch sizes. The
authors did not evaluate distributed storage, cloud deployment, multi-user
contention, GPU decoding, or production robot fleets. The artifact is not yet
packaged, and the build instructions are incomplete. The paper includes a
planned artifact-evaluation appendix, but it is not finished.

## Draft Abstract

Robot learning needs reliable access to massive multimodal logs. We present a
production-ready dataflow runtime that delivers real-time replay, scalable
storage, and general deployment across robot fleets. Across public and lab
datasets, our runtime outperforms existing systems and establishes a new
standard for reproducible robot-data infrastructure.

## Draft Introduction

Large robot datasets are difficult to query because images, joint states, and
metadata arrive at different rates and are often stored in ad hoc formats. This
paper proposes a chunked dataflow runtime that improves replay and query
latency for robot-learning workflows. The current motivation is useful, but the
draft escalates from local workstation evidence to production-fleet claims.

The Related Work lists database systems, video codecs, robotics datasets, and
ML data loaders. It does not identify the nearest data-loading or robotic-log
runtime systems, nor does it separate storage layout, indexing, decoding,
scheduling, and artifact-evaluation axes. Without this distinction, the gap
claim is too broad.

## Draft Methods

The runtime has an importer, chunk writer, metadata index, replay scheduler,
and Python API. The draft describes these modules but does not define the
central system object: a chunked time-indexed log representation with aligned
modalities and replay cursors. It also does not specify failure behavior when
frames are missing, timestamps drift, or metadata is inconsistent.

## Draft Experiments

The experiments show median latency improvements on two public datasets and one
lab dataset. These numbers support a bounded systems claim about local query
latency and sequential replay under the evaluated workstation setup. They do
not support production readiness, distributed scalability, or robot-fleet
deployment. The paper also claims reproducibility, but the artifact is not
packaged and build instructions are incomplete.

Figure 1 shows the runtime architecture. Figure 2 plots median latency. Table 1
lists dataset sizes and query patterns. Table 2 reports throughput. Table 3 is
planned for artifact-evaluation results but is empty.

## Draft Discussion

The strongest limitation is artifact maturity. A systems paper can still be
valuable with a local runtime and clear benchmarks, but it must not imply
production deployment or reproducibility until users can build and run the
artifact. The discussion should distinguish local benchmark evidence from
deployment claims.

## Draft Conclusion

The draft concludes that the runtime is a production-ready infrastructure layer
for robot-data workloads. The supplied evidence supports only a local
workstation systems result: lower median latency and better sequential replay
under the evaluated datasets, with distributed storage, artifact packaging,
build reproducibility, and fleet deployment untested.

## Reviewer Comments

**R1.** The paper claims production readiness but the artifact cannot yet be
built from public instructions.

**R2.** The method section lists modules without defining the central system
object or failure behavior.

**R3.** The response says distributed experiments and Table 3 were added, but
the supplied evidence says Table 3 is empty and distributed storage was not
tested.

## Draft Response Letter

We thank the reviewers. We have packaged the artifact, added Table 3 with
artifact-evaluation results, and clarified that the runtime is production-ready
for robot fleets. We also added distributed-storage experiments and final build
instructions.
