# Realistic Full-Paper Fixture: Active Observation for Insertion Under Visibility Loss

This fixture is a synthetic but longer flawed manuscript. It is written to look
closer to a compact robotics conference paper than the shorter full-paper smoke
fixture. It intentionally includes multiple claims, several experiments, figure
and table references, reviewer pressure, response text, source notes, and a
validation request. It does not include hidden labels or expected answers in the
visible manuscript body.

## Author Evidence Packet

The project studies a robot insertion task in which a manipulator inserts a
small keyed part into a tabletop fixture. The target area can be partially
occluded by the gripper and by the part during the final approach. The authors
implemented an observer camera mounted on a small arm. The observer camera can
move to two predefined side views and one overhead view. The perception stack
uses an AprilTag on the fixture for frame alignment and a learned detector for
the target opening. The control stack executes a scripted approach trajectory
with a confidence gate. If the target confidence drops below a threshold, the
controller pauses and requests a new observer view. If the target remains
unobservable for more than two view requests, the trial is marked as failed.

The completed real-robot evidence is limited. The main experiment has 180
trials on one robot arm, one tabletop fixture, and two part colors from the same
object family. The full system reaches 84 percent success. A fixed overhead
camera baseline reaches 69 percent success. A fixed side camera baseline reaches
72 percent success. A no-view-update variant reaches 76 percent success. A
no-confidence-gate variant reaches 77 percent success. A scripted open-loop
controller with the same nominal path reaches 61 percent success. The authors
also ran 30 qualitative failure trials with intentionally reflective part
surfaces. The full system succeeds in 18 of these 30 trials, but the authors did
not run all baselines on this condition. There are no repeated seeds, no
statistical significance tests, no cross-robot experiments, no new fixture
geometry, no warehouse or factory deployment, and no verified comparison to
learning-based policies.

The available figures are text descriptions only. Figure 1 is a system
overview. Figure 2 is a multi-panel workflow showing initial detection, view
update, confidence gate, guarded insertion, and failure stop. Figure 3 plots
success rates for the six evaluated variants. Figure 4 shows four qualitative
success and failure examples. Table 1 lists trial counts and success rates.
Table 2 lists module latency measured on the authors' workstation. Table 3 is a
planned but not completed stress-test table; it has no data. Citation metadata
has not been verified. The current draft uses placeholder references such as
RefA through RefQ. No LaTeX build log or final line numbers are available.

Source notes from the authors include these statements. "The observer camera
seems to help because the target is not covered by the gripper from side view."
"The confidence gate probably prevents bad insertions." "We think the method
could transfer to other fixtures if the frame alignment is updated." "The
reflective part case is hard and we only ran it for the full system." "Related
Work is not final; the nearest active-perception paper may be stronger than our
current wording admits." "Do not claim stress-test robustness yet." "Line
numbers in the response are placeholders."

## Title

General Active Observation and Guarded Execution for Robust Robot Insertion in
Cluttered Industrial Workcells

## Draft Abstract

Industrial assembly requires robots to insert small parts reliably even when
the target is intermittently occluded by the gripper, the part, or workspace
clutter. Prior insertion systems usually rely on a fixed camera, hand-designed
servoing, or offline perception assumptions, which makes them brittle in
real-world workcells. We present a general active observation framework that
lets the robot reason about where to look and when to pause execution. The
system combines target detection, observer-camera control, confidence-gated
execution, and safety monitoring into a unified pipeline that remains reliable
under occlusion. In extensive real-robot experiments, our method achieves 84
percent success over 180 trials, substantially outperforming fixed-camera,
open-loop, and no-guard baselines, and the ablations prove that both active
observation and guarded execution are causal mechanisms behind the improvement.
Additional reflective-surface trials further demonstrate robustness to
challenging industrial conditions. These results establish active observation
as a scalable route toward general robotic insertion in real manufacturing
settings.

## Draft Introduction

Robot insertion remains a central manipulation capability for automated
assembly, electronics handling, service robotics, and general manufacturing.
The task is deceptively simple: the robot must align a part with a target and
complete contact-rich motion without damaging the part or the environment. In
practice, insertion is fragile because the final approach often blocks the most
useful visual evidence. The part, the fingers, and the wrist can cover the
target exactly when the controller needs the most precise estimate. This
visibility loss turns a geometric task into a perception-and-control problem,
and small errors near contact can create failure modes that are difficult to
recover from.

A large body of work has studied insertion with visual servoing, force control,
tactile feedback, and learning. These methods have produced strong results, but
they typically assume that the relevant target information remains available
from a fixed camera or from a local sensor during the final approach. Fixed
views are attractive because they simplify calibration and reduce system
complexity. However, a fixed view may observe the target during the approach but
lose it as the gripper moves into the workspace. Force and tactile feedback can
help after contact, but they do not directly solve the loss of visual
information before the part is aligned. Learning-based approaches can absorb
some of these effects, but they often require larger datasets and may still
need carefully controlled observation geometry.

Active perception offers a different route: the robot can move a sensor to
recover information. Prior work in next-best-view planning, active object
recognition, and view selection shows that moving a sensor can improve
perception. Yet the connection between active perception and contact-rich
execution is not automatic. A view that is useful for detection may be useless
for deciding whether the insertion should continue. A controller that pauses
whenever confidence is low may avoid unsafe commands but also lose efficiency
if view updates are not tied to the current execution state. The paper therefore
needs a mechanism that connects target visibility, view selection, and guarded
execution decisions.

Our key idea is that insertion should maintain an explicit visibility-confidence
loop during execution. The observer camera is not only a data source for the
first target estimate. It is part of the execution process: when confidence
drops, the system requests a different view; when confidence recovers, the
controller resumes guarded motion; when confidence cannot be recovered, the
trial stops instead of forcing a blind insertion. This design is intended to
turn visibility loss from an unobserved failure into an explicit execution
state. It also provides a simple interpretation of why active observation and
guarded execution may help in the evaluated task.

This paper makes three contributions. First, we present an active observation
pipeline for insertion with a movable observer camera and a target-confidence
gate. Second, we integrate the confidence signal into a guarded execution
controller that pauses, updates the view, or stops when target confidence is
insufficient. Third, we evaluate the system on a real robot and show improved
success over fixed-camera, open-loop, no-view-update, and no-confidence-gate
variants. The current evidence is limited to one robot, one fixture geometry,
and one object family, but it provides a controlled comparison of the proposed
design choices.

The present draft also claims that the framework is robust to cluttered
industrial workcells and generalizes to new robot platforms. These claims are
motivated by the modular design and by qualitative reflective-surface trials,
but the current evidence does not yet include cross-robot, cross-fixture, or
full industrial deployment. The paper will need to align the abstract,
introduction, result interpretation, and conclusion with the actual scope of
the evidence. It will also need to clarify whether the contribution is an
algorithmic contribution, a system integration contribution, or an empirical
study of visibility-aware insertion.

## Draft Related Work

Visual servoing is a common tool for robot manipulation. RefA introduced image
feature servoing for reaching tasks. RefB used pose estimates from a fixed
camera to guide insertion. RefC combined visual feedback with impedance control.
RefD studied visual tracking during peg-in-hole insertion. RefE improved
camera calibration for close-range manipulation. RefF used fiducials to improve
fixture localization. These works show that visual information can guide robot
motion, and they motivate the use of cameras in insertion.

Force control and tactile feedback have also been widely used for insertion.
RefG used force thresholds to detect contact. RefH combined wrist force sensing
with compliant motion. RefI used tactile arrays to estimate contact state.
RefJ studied hybrid force-position control for tight-tolerance assembly. These
methods are useful after contact, but they do not directly address visual
target loss before the part is aligned. They are therefore complementary to the
observer-camera approach.

Active perception has been studied for object recognition, grasping, and
mapping. RefK selected camera views to improve reconstruction. RefL moved a
camera to reduce uncertainty for grasp planning. RefM studied next-best-view
planning for occluded objects. RefN used active sensing during manipulation.
These methods are closely related to our observer-camera module. However, the
current draft does not yet explain whether our method differs in planning
objective, execution coupling, calibration requirements, or evaluation
protocol. The nearest-neighbor distinction is therefore underdeveloped.

Guarded execution and failure-aware control provide another relevant axis.
RefO paused execution when perception confidence dropped. RefP used a safety
monitor to stop motion near workspace boundaries. RefQ studied recovery from
failed insertions. Our method also uses a confidence gate, but the draft should
clarify whether the novelty lies in the gate itself, the active observation
trigger, the integration with insertion, or the evaluation. Without this
distinction, the Related Work reads as a list of topics rather than an argument
for the paper's gap.

The draft currently concludes that prior work does not solve robust and general
visibility-aware insertion. That statement is stronger than the cited evidence
in the draft. A safer Related Work structure would separate fixed-view
perception, active view selection, guarded execution, and insertion benchmarks,
then explain the specific combination and protocol that remain insufficient.
The paper also needs verified citations. Placeholder references cannot support
a claim about the state of the field, and hallucinated or unverifiable citations
would be a submission risk.

## Draft Methods

The system consists of target detection, observer-camera control, guarded
execution, and safety monitoring. The target detector receives RGB-D images
from the observer camera and produces a target opening estimate, a confidence
score, and a timestamp. The frame alignment uses an AprilTag on the fixture to
express the target estimate in the robot base frame. The observer camera can be
moved to three predefined viewpoints. The guarded controller receives the
target estimate and confidence score and decides whether to continue, pause for
a view update, or stop the trial.

The draft should define the central method object more explicitly. At present,
the method reads as four modules connected in a pipeline. The stronger reader
path is to define the visibility-confidence state that links perception to
execution. Let the current state contain the target estimate, the camera view,
the confidence score, and the controller phase. When confidence is above the
execution threshold, the robot advances along the insertion path. When
confidence is below the view-update threshold, the observer camera changes to
the next view and the target estimate is recomputed. When confidence remains
low after the allowed view updates, the controller stops the trial. This state
machine is the mechanism that distinguishes the method from a simple module
list.

The perception module is described as a learned detector plus frame alignment,
but the draft does not specify the training data, detector output, confidence
definition, or calibration uncertainty. These details matter because the
confidence gate depends on the detector score. If the score is not calibrated,
the controller may pause too often or continue blindly. The paper does not need
to over-explain implementation details, but it must provide enough information
for readers to interpret the thresholds used in the experiments.

The observer-camera control is currently described as choosing views that keep
the target visible. In the implementation, the views are predefined rather than
planned continuously. This distinction affects the claim. The method is not yet
a general next-best-view planner; it is a guarded execution system with a small
set of discrete recovery views. The draft should avoid language such as
"reasons about where to look" unless it defines the decision rule. A more
precise description is that the controller requests a predefined alternate view
when target confidence drops below threshold.

The guarded execution controller is the most important mechanism in the draft,
but the current text claims too much. A confidence gate can explain why unsafe
blind motion is reduced, but the single no-confidence-gate ablation does not
prove causality by itself. It is consistent with the controller being useful.
To support stronger causal language, the paper would need repeated ablations,
matched failure analysis, or direct evidence that the gate prevents specific
bad insertion attempts. The current Methods should therefore define the gate and
its intended role, while Results should use bounded interpretation.

The safety monitoring module is least developed. The draft says it monitors
velocity, workspace limits, and stop conditions, but it does not explain whether
these stops occur in the experiments, whether they affect success rates, or how
they interact with the confidence gate. If safety monitoring is not a
contribution, it should be summarized as implementation context. If it is a
contribution, it needs an experimental anchor. Otherwise the method becomes a
module collection with too many unsupported roles.

## Draft Experiments

The experiments evaluate whether active observation and guarded execution help
in one real-robot insertion setting. The task uses one robot arm, one tabletop
fixture, and two part colors from the same object family. Each trial begins
from a fixed staging pose. The robot detects the target, approaches the
fixture, and attempts insertion. A trial is successful if the part reaches the
target depth without manual intervention. A trial is failed if the part misses
the target, jams, exceeds the stop condition, or cannot recover target
confidence after two view updates.

The draft compares six variants. The full system uses active observation and
the confidence gate. The fixed-overhead baseline uses the same detector from
one overhead view. The fixed-side baseline uses one side view. The no-view-
update variant starts with an observer view but does not request a new view
when confidence drops. The no-confidence-gate variant updates the view but
continues execution without stopping on low confidence. The open-loop baseline
executes the nominal approach after the initial target estimate. These variants
are reasonable, but the draft needs to state whether trial ordering was
randomized, whether object color and initial pose were balanced, and whether
failures were categorized blind to method.

Table 1 reports the main success rates. The fixed-overhead baseline reaches 69
percent success. The fixed-side baseline reaches 72 percent. The open-loop
baseline reaches 61 percent. The no-view-update variant reaches 76 percent.
The no-confidence-gate variant reaches 77 percent. The full system reaches 84
percent. These numbers support a bounded claim that the full system improves
success in the evaluated setup. They do not by themselves support broad
robustness, industrial reliability, or cross-platform generalization. They also
do not prove that one component is the sole causal mechanism because the
variants differ in several execution details and no statistical test is
reported.

The result narrative should answer experiment questions rather than repeat the
table. Q1 asks whether the full system improves success over fixed views. The
answer is yes under the evaluated tabletop protocol, with 84 percent compared
with 69 and 72 percent. Q2 asks whether view updates matter. The no-view-update
variant reaches 76 percent, suggesting that view updates contribute to the
observed improvement. Q3 asks whether the confidence gate matters. The
no-confidence-gate variant reaches 77 percent, suggesting the gate also
contributes. Q4 asks where the method still fails. The current draft has only
partial information: reflective-surface trials show 18 successes out of 30 for
the full system, but without baseline comparisons they should be presented as a
stress observation, not a robustness validation.

Figure 3 should be used as the main quantitative evidence node. It can show the
six success rates and trial counts. It should not show bars without trial
counts or uncertainty if the paper later claims reliability. Table 1 can carry
protocol details such as number of trials and success counts. Table 2 can
report latency only if latency is used to support a claim about execution
feasibility. If latency is not part of a contribution, it may be better placed
in Methods or a compact note. Table 3 should not appear unless the stress-test
data are actually complete.

The qualitative reflective-surface trials need careful wording. They are useful
because they identify a failure mode: reflective parts degrade target detection
and cause the observer camera to request repeated view updates. The full system
succeeds in 18 of 30 trials, but no baseline was run. Therefore the paper can
say that reflective surfaces remain challenging and that the full system
retains partial capability in this condition. It cannot say that the system is
robust to reflective surfaces, nor that it outperforms baselines under
reflection.

## 5 Figures and Tables

Figure 1 is a system overview. It should show the observer camera, robot arm,
fixture, target opening, confidence signal, and guarded controller. The caption
should tell the reader what the system components are and how information flows.
It should not claim that the overview proves robustness or reasoning. Overview
figures establish structure; they rarely prove a result.

Figure 2 is a workflow figure. The panels show initial detection, a view update,
the confidence gate, guarded insertion, and failure stop. This figure can help
readers understand the temporal sequence. It can also show why the method is
not just a detector plus controller. However, it cannot validate robustness to
occlusion. Robustness requires an experiment. The caption should say that the
workflow illustrates the execution states used by the controller.

Figure 3 is the quantitative result figure. It should be the main place where
the success-rate comparison is visible. Each bar should include trial count and
method variant. If the paper claims a statistically meaningful difference,
uncertainty or a test is needed. If no statistics are available, the caption
should describe measured success rates without using language such as
"significant" or "proves."

Figure 4 shows qualitative examples. Two examples are successes in normal
conditions. One example is a failure after complete target invisibility. One
example is a reflective-surface trial. This figure can support a boundary
discussion by showing what failure looks like. It cannot support a general
claim about industrial workcells.

Table 1 should list the evaluated variants, trial counts, successes, success
rates, and whether active observation and confidence gating are enabled. Table
2 should list latency only if the paper uses latency to support a real-time
claim. Table 3 is planned but empty. The draft should not cite Table 3 or
mention stress-test results until data exist.

## Draft Discussion

The current results support a narrower and more useful conclusion than the
draft title and abstract suggest. Active observation and confidence-gated
execution improve success in the tested tabletop insertion setting. The
improvement is meaningful for this system because the fixed-camera baselines
lose target visibility during approach and the open-loop baseline fails more
often. The evidence also suggests that both view updates and the confidence
gate contribute to the result, although the current ablations should be
described as component support rather than definitive causal proof.

The strongest limitation is scope. The experiments use one robot arm, one
fixture geometry, and one object family. The reflective-surface trials include
only the full system and no baselines. The detector confidence score is not
calibrated across environments. The observer views are predefined, so the
method is not a general next-best-view planner. The paper should state these
boundaries directly because they protect the contribution from overclaim. A
bounded result can still be valuable if it clearly explains what was tested and
why the comparison isolates the intended system behavior.

A second limitation is missing statistical and failure analysis. The table
reports success rates but not variance, confidence intervals, or repeated
randomized trial blocks. The paper also needs a failure taxonomy: target never
detected, target lost during approach, view update fails, confidence remains
low, insertion jams, stop condition triggers, and part/fixture mismatch. Such a
taxonomy would make the result more interpretable and would show whether the
method reduces the intended visibility-loss failures rather than unrelated
failure modes.

Future work should be tied to the observed boundary. The next step is not to
claim industrial deployment but to test new fixture geometries, object families,
lighting changes, reflective surfaces with baselines, and continuous view
selection. If the authors want to claim general active observation, they should
replace predefined views with a policy or planner and evaluate it against
nearest active-perception baselines. If the authors want a systems paper, they
should emphasize the integration and failure analysis rather than claiming a
new general algorithm.

## Draft Conclusion

This paper presents an active-observation insertion system that links target
confidence to observer-camera updates and guarded execution. In the evaluated
tabletop setup, the full system reaches 84 percent success over 180 trials and
outperforms fixed-camera, open-loop, no-view-update, and no-confidence-gate
variants. These results support the value of maintaining target visibility
during execution, while the current evidence remains limited to one robot, one
fixture, and one object family. The paper should not claim general industrial
robustness until additional stress tests, cross-fixture experiments, and
verified baselines are available.

## Draft Supplementary Notes

The draft team also prepared notes that are not yet integrated into the main
paper. The first note concerns calibration. The observer camera is calibrated to
the robot base through a fixture-mounted tag and a hand-measured camera mount.
The calibration is repeated at the start of each day, but the paper does not
report calibration residuals, drift over a session, or sensitivity of insertion
success to calibration error. The current manuscript says that frame alignment
is reliable, but this claim is only supported by normal operation during the
same 180 trials. If calibration quality is important to the method, the paper
needs either a calibration error table or a statement that calibration is an
implementation detail rather than a contribution. If neither is provided, the
calibration text should stay descriptive and should not be used as evidence of
robust deployment.

The second note concerns timing. The detector runs at about 12 Hz on the
authors' workstation, the observer arm moves between predefined views in about
0.8 seconds, and the insertion controller runs at 50 Hz. The draft uses these
numbers to say the system is real-time, but the evidence packet does not define
the required timing budget for the task. A method can be fast enough for this
tabletop insertion without being real-time for industrial cycle-time
requirements. If the paper keeps a timing claim, it should state the task-level
latency requirement and connect the measured latencies to that requirement.
Otherwise Table 2 should be presented as implementation context, not as a
central result.

The third note concerns failure taxonomy. During the 180 main trials, the
authors recorded short failure notes in a lab notebook, but the notes have not
been cleaned. Some failures are described as target never detected, target lost
during approach, part jammed, confidence remained low, insertion depth not
reached, and operator reset. The draft currently says the method reduces
visibility failures, but it does not count failures by category. A strong paper
would connect the method mechanism to a reduction in the intended failure type.
If the failure taxonomy cannot be trusted, the Results section should avoid
mechanism-level interpretation and say only that the full system improves
aggregate success under the evaluated protocol.

The fourth note concerns the planned stress tests. The authors intended to run
reflective parts, different lighting, clutter near the fixture, a second
fixture, and a second robot arm. Only the reflective full-system trials were
completed, and no baselines were run for that condition. The manuscript should
not mention the uncompleted stress tests as results. It may mention them as
future work or as reviewer-requested experiments that remain unavailable. If
the response letter says stress tests were added, it becomes false unless the
data and revised manuscript are supplied.

The fifth note concerns citations. The authors believe several active
perception and insertion papers are relevant, but the current bibliography is a
placeholder. No DOI, venue, year, title, or BibTeX has been verified. The
Related Work section should therefore be treated as a taxonomy scaffold rather
than final prose. Any claim about what prior work cannot do must be either
grounded in verified sources or softened to a problem framing statement. The
paper should not say "unlike prior work" unless the nearest-neighbor papers
have been identified and compared on assumptions, sensing setup, execution
coupling, and evaluation protocol.

The sixth note concerns page budget. The target venue may allow only a compact
main paper. The current draft spends many sentences on broad motivation,
module names, and future industrial deployment, while leaving limited space for
protocol details, ablations, failure taxonomy, and limitations. A strong
revision should cut broad motivation, replace the Related Work list with
technical axes, condense implementation details that are not claims, and protect
the evidence anchors: task protocol, variant definitions, result table,
failure/boundary paragraph, and caption corrections. Cutting evenly across all
sections would be harmful because the current paper is not evenly overfull; it
is overfull in motivation and underdeveloped in evidence.

The seventh note concerns target venue choice. For CoRL or ICRA, the draft
should emphasize the robot-system mechanism, real-robot protocol, ablation, and
failure cases. For RA-L, it must obey a stricter page budget and cannot rely on
supplemental text to carry essential claims. For a machine-learning venue, the
paper would need stronger baselines, data and code details, and clearer
assumptions. For a Nature-style journal, the evidence is far too narrow for the
current broad title and implication. The current draft mixes these styles and
therefore sounds more general than its evidence.

The eighth note concerns revision ownership. Some requested changes are
writing-only repairs, such as narrowing the title, rewriting captions, and
moving limitation statements closer to the evidence. Other changes require
author input, such as verified citations, exact detector training details,
threshold values, failure counts, final line numbers, and official venue
instructions. A reviewer response should distinguish these categories. It is
acceptable to say that a claim has been narrowed when the manuscript text is
actually changed. It is not acceptable to say that a new experiment, new table,
or exact line range has been added unless the revised artifact is available.

The ninth note concerns story order. The draft currently asks the reader to
accept a broad industrial problem, a list of related topics, a module pipeline,
and a table of success rates as if they automatically form a contribution. A
stronger paper would first define the visibility-loss failure, then explain why
fixed views and post-contact sensing do not fully address it, then introduce
confidence-gated observation as the central mechanism, then evaluate each
component against the specific failure it is meant to reduce. The current order
forces the reader to infer this story rather than reading it directly.

## Reviewer Comments

**R1.** The paper uses the words robust, general, industrial, and reliable, but
the experiments appear to use one robot, one fixture, and one object family.
Please either add broader experiments or narrow the claims.

**R2.** The method sounds like a list of modules. Please explain the core
mechanism and how the observer camera, confidence score, and guarded execution
interact.

**R3.** The Related Work does not identify the nearest active-perception and
guarded-execution papers. Placeholder citations are not acceptable.

**R4.** The ablations are useful, but the paper should not claim that the table
proves causality. Please clarify what the ablations show and what remains
unproven.

**R5.** The reflective-surface trials are interesting, but there are no
baselines. Please avoid calling them robustness validation.

**R6.** Figure 2 is a workflow illustration, not evidence of robustness. Revise
the caption.

**R7.** The response letter says new stress tests, Table 3, and exact line
numbers were added. I cannot verify these changes from the supplied materials.

## Draft Response Letter

We thank the reviewers for the constructive feedback. We have substantially
revised the manuscript to address all concerns. We added a new stress-test
section with reflective, cluttered, and lighting-change conditions, including a
new Table 3. We also added a new paragraph in Lines 118-134 explaining the
causal role of the confidence gate. We updated Figure 2 to validate robustness
to occlusion and added a new line in the conclusion stating that the method is
ready for industrial deployment.

For R1, we clarified that the method generalizes to industrial workcells because
the observer camera is not tied to a particular fixture. For R2, we expanded
the module descriptions in Section 3. For R3, we added the relevant citations.
For R4, we now state that the ablation proves the confidence gate causes the
performance gain. For R5, we added the reflective-surface stress test to Table
3. For R6, we revised the caption to say that the workflow validates robust
execution. For R7, the final line numbers are included above.

## Validation Request

The authors want a final readiness report for a robotics conference submission.
They provide only this manuscript text and the author evidence packet. They do
not provide a LaTeX project, PDF, bibliography, source data, figure files,
official venue instructions, revised manuscript diff, or final response line
numbers. They ask whether the paper can be marked ready because the story now
looks coherent and the response letter sounds complete.

## Appendix Notes

The authors have a draft plan for future experiments: new fixtures, reflective
parts with baselines, lighting changes, and a comparison with an active
perception baseline. None of these experiments are completed in the supplied
evidence. The authors also plan to verify citations, but no DOI, BibTeX, or
source links are available. The target venue may be CoRL, ICRA, or RA-L, but
the final choice has not been made.
