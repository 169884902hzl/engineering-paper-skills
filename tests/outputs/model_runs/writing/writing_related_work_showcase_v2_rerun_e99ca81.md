## Draft

Contact-rich insertion sits at the intersection of sensing geometry, pose estimation, and guarded motion rather than within a single manipulation module. Fixed-view insertion systems can provide repeatable observations under controlled camera placement, but their sensing geometry is selected before visibility changes caused by approach, occlusion, or near-contact alignment become decisive [FixedViewInsertion]. Active-perception methods relax this assumption by acquiring additional views, yet that axis is often organized around object coverage or detection confidence rather than using confidence drops to trigger insertion-pose refinement before execution [ActivePerceptionManipulation]. Force-guarded insertion controllers address a complementary part of the problem: they monitor contact during motion and can slow or stop execution, but the guard reacts to contact consequences rather than resolving visual pose ambiguity upstream [ForceGuardedInsertion]. The closest neighboring line combines perception with guarded insertion, linking visual estimates to contact-aware execution [PerceptionGuardedInsertion]. The technical gap considered here is the bounded same-loop bridge between confidence-triggered view acquisition, refined insertion-pose estimation, and force/pose guarded execution for contact-rich insertion.

## Evidence boundary

- Citation placeholders are retained as requested.
- The paragraph does not assert definitive novelty.
- Nearest-neighbor citation audit remains required before replacing placeholders.
- Claims about prior work are limited to the assumptions stated in the prompt.