# Comment Routing

Use this before editing the manuscript.

## Comment Types

- `[Logic]`: claim, evidence, interpretation, contribution, or gap problem
- `[Structure]`: section order, paragraph job, reader path, or missing transition
- `[Expression]`: wording, tone, overclaiming, unclear sentence
- `[Data]`: missing experiment, metric, statistical support, or data detail
- `[Citation]`: missing, weak, or wrong citation support
- `[Format]`: figure, table, caption, template, page, or style issue

## Routing Table

| Comment shape | Real issue | First target | Second target | Avoid first |
|---|---|---|---|---|
| Introduction too scattered | positioning not established | Introduction | Related Work | Methods |
| Related work is a list | taxonomy and nearest neighbor missing | Related Work | Introduction | Experiments |
| Methods reads like modules | reader path missing | Methods | Introduction | Conclusion |
| Experiments are just reports | evidence not tied to contribution | Experiments | Introduction | Related Work |
| Ablation weak | mechanism-evidence alignment missing | Experiments | Methods | Conclusion |
| Figure/caption unclear | visual responsibility unclear | Figure/Table | Related prose | Whole paper |
| Claim too strong | claim exceeds evidence | Experiments | Introduction | Methods |
| Conclusion empty | final evidence and boundary missing | Conclusion | Experiments | Related Work |

## Rule

Do not convert every comment into "polish this paragraph." Most comments are
about section responsibility or evidence support.
