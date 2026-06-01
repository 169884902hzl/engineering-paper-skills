# Fixture: Source Notes Expansion

## Flawed manuscript input

Source notes translated by the author:

- pose noise hurts insertion
- active observation helps keep the target visible
- maybe observer camera improves contact reasoning
- result: success improves from 71% to 86% in current trials
- limitation: not tested when target is completely invisible

Unsafe English draft:

We propose a robust active-observation framework for contact-rich insertion.
The observer camera improves contact reasoning by maintaining visibility of the
target and gripper throughout execution. This mechanism enables the policy to
generalize to severe occlusion and clutter. Real-robot experiments show that
the system improves success from 71% to 86%, demonstrating reliable deployment
in practical manipulation.

The English draft turns a guess into mechanism fact and broadens the result
beyond the notes. It adds severe occlusion, clutter, reliable deployment, and
generalization, none of which are provided. The safe rewrite must separate
facts, assumptions, unsupported claims, and boundary.

## Expected audit pressure

The skill should run source expansion check and sentence role audit. It should
keep the numbers, preserve the limitation, mark the mechanism as hypothesis,
and remove deployment/generalization language.

## Failure modes

- Source notes expanded into unsupported facts.
- Guess written as mechanism.
- Claim strengthened by translation.
- Boundary dropped.
