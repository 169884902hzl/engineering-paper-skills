## 1. Related-work risk diagnosis

The strongest novelty claim is not yet safe. The supplied notes support a positioning hypothesis, not a fully verified literature gap: the paper appears to combine confidence-triggered additional RGB-D views with guarded contact-rich insertion, but the author has not yet shown that prior work lacks this exact combination.

Main risks:

- Group A is task-nearest because it addresses insertion, but the supplied distinction is only camera policy: fixed camera versus requested additional views.
- Group B is mechanism-nearest because it uses active perception, but the supplied notes do not verify contact-rich insertion.
- Group C is execution-nearest because it uses force-guarded insertion, but the supplied notes do not verify view-request policies.
- Group D is dangerous because industrial insertion systems may combine sensing, guarding, and specialized fixtures; no exact citations or comparable protocols are supplied.
- The current evidence supports one tabletop setting, 84% success over 180 trials, and comparisons to fixed-view and open-loop baselines. It does not yet support broad claims about industrial deployment, generality across insertion geometries, or superiority over all active-perception or force-control methods.

## 2. Technical axes table

| Axis | Group A: fixed-camera insertion | Group B: active perception for manipulation | Group C: force-guarded insertion controllers | Group D: industrial insertion systems | Current paper |
|---|---|---|---|---|---|
| Primary task | Insertion | Grasping or inspection, based on supplied notes | Insertion | Insertion or assembly likely, but unspecified | Contact-rich insertion under partial visual occlusion |
| Visual setup | One overhead or side camera | Viewpoint selection | Not specified in supplied notes | Not specified | Multi-view RGB-D with additional view requested when confidence is low |
| During-execution view request | Not supplied; notes say they do not request additional views during execution | Yes for manipulation viewpoints, but task scope is unclear | Not supplied | Unknown | Yes, confidence-triggered additional observation |
| Contact-rich execution | Yes, by task class | Not verified | Yes | Likely but uncited | Yes |
| Guarding mechanism | Not supplied | Not supplied | Force-threshold stopping or adjustment | Unknown | Stops under force or pose-deviation limits |
| Closest similarity | Same task setting | Same perception mechanism | Same guarded execution regime | Possible practical competitor | Integrated perception-request and guarded execution system |
| Current distinction | Dynamic view request under uncertainty | Contact-rich insertion plus guarded execution must be verified | View-request policy must be verified | Cannot distinguish without citations/protocols | Evaluated in one tabletop setup with fixed-view and open-loop baselines |
| Missing evidence | Exact papers and protocols | Evidence that they do or do not handle insertion | Evidence that they do or do not use active view requests | Exact citations and comparable protocols | Broader tasks, stress tests, industrial baselines, and source-grounded prior-work comparison |

## 3. Nearest-neighbor distinction

The safest nearest-neighbor structure is a three-way distinction rather than a single invented nearest paper.

Task-nearest neighbor: Group A fixed-camera insertion systems.  
Distinction: both address insertion, but Group A is described as using a fixed overhead or side camera, while the current system requests an additional RGB-D view when confidence is low. The paper can claim this distinction only after identifying representative Group A papers and verifying that they do not include during-execution view requests.

Mechanism-nearest neighbor: Group B active perception for manipulation.  
Distinction: both use viewpoint selection or additional sensing, but Group B is only described for grasping or inspection. The current paper targets contact-rich insertion with guarded execution. The missing check is whether any Group B work already handles contact-rich insertion or assembly.

Execution-nearest neighbor: Group C force-guarded insertion controllers.  
Distinction: both address contact-rich insertion and use force-based guarding, but Group C is not described as using view-request policies. The current paper should position guarded execution as necessary but not sufficient: the added claim is coupling guard limits with confidence-triggered perception. This requires verified examples showing what Group C senses and when.

Industrial-nearest unknown: Group D industrial insertion systems.  
Distinction cannot be safely written yet. These systems may be the most practically relevant comparators, but the author has not supplied exact citations, sensors, fixtures, tasks, or protocols.

## 4. Safe Related Work paragraph scaffold

Prior work on robotic insertion has studied fixed-camera perception pipelines, active perception for manipulation, and force-guarded execution. Fixed-camera insertion systems address the same task family but typically assume a fixed overhead or side view during execution [citation needed: fixed-camera insertion systems]. Active-perception methods select viewpoints for manipulation tasks such as grasping or inspection, but the supplied sources do not yet establish that they address contact-rich insertion under partial occlusion [citation needed: active perception for manipulation scope]. Force-guarded insertion controllers reduce execution risk by stopping or adjusting motion under force thresholds, but the supplied notes do not show that they request additional views when visual confidence is low [citation needed: force-guarded insertion controllers]. Against these axes, the present system should be positioned as a tabletop contact-rich insertion pipeline that couples confidence-triggered RGB-D view requests with force and pose-deviation guards, supported by an 84% success rate over 180 trials against fixed-view and open-loop baselines. This claim should remain bounded to the reported setup until industrial systems, broader insertion geometries, and comparable active-perception insertion baselines are source-grounded.

## 5. Citation/evidence still needed

- Representative Group A papers with exact camera assumptions, insertion task definitions, and whether they use any during-execution view update.
- Representative Group B papers with task scope: grasping, inspection, insertion, assembly, or contact-rich manipulation.
- Representative Group C papers with guard type, sensor inputs, control loop, and whether perception is fixed or adaptive.
- Exact Group D industrial insertion citations, including hardware, fixture assumptions, sensing, guard logic, and evaluation protocols.
- A checked statement on whether any prior system combines active view requests with force- or pose-guarded contact-rich insertion.
- Comparable protocols beyond the current fixed-view and open-loop baselines, especially if the paper wants a strong novelty or superiority claim.
- Evidence for generality beyond one tabletop setup, if the manuscript wants to claim robustness across occlusion patterns, parts, fixtures, or deployment environments.