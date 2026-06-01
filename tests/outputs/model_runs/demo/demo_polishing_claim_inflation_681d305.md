## 1. Diagnosis

The draft inflates a local quantitative result into broad robustness, generality, industrial relevance, and mechanism claims. The evidence supports a bounded comparison on contact-rich peg insertion under partial visual occlusion, using one robot arm, one tabletop fixture, and one cylindrical peg family. It does not support claims about industrial deployment, cross-robot generality, statistical significance, or a causal mechanism for active observation.

## 2. Claim-strength diff

| Original claim | Revised claim | Strength change | Reason |
|---|---|---:|---|
| “robust and general solution for insertion” | “improves success in the tested peg-insertion setting” | Weaker | Only one robot, fixture, and peg family were tested. |
| “works well in realistic settings” | “achieved 84% success over 180 trials under partial visual occlusion” | More specific | “Realistic” is undefined and unsupported. |
| “strong performance against baselines” | “outperformed the fixed-camera and open-loop comparisons in success rate” | Bounded | No statistical significance test is provided. |
| “demonstrates that active observation is an effective mechanism” | “suggests that the full system benefits from the tested observation setup” | Weaker | No causal ablation isolates active observation. |

## 3. Polished paragraph

In contact-rich peg insertion under partial visual occlusion, the full system achieved an 84% success rate over 180 trials. In the same evaluation setting, the fixed overhead RGB-D camera, fixed side RGB-D camera, and open-loop controller achieved success rates of 69%, 72%, and 61%, respectively. These results indicate that the proposed system improves insertion success in the tested setup, but they do not by themselves establish general robustness, industrial readiness, or a causal effect of active observation across platforms or object families.

## 4. Unsupported wording removed

- “robust”
- “general solution”
- “realistic settings”
- “strong performance”
- “demonstrates”
- “effective mechanism”
- “industrial manipulation”

## 5. Remaining evidence needed

- Cross-robot experiments to support generality.
- Additional fixtures and peg families to support broader insertion claims.
- Industrial or field tests to support industrial relevance.
- Statistical significance testing to support stronger comparison claims.
- A causal ablation isolating active observation from the rest of the system.