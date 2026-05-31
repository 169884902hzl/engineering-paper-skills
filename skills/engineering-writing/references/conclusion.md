# Conclusion

Use this for English conclusions.

## Job

Conclusion states what finally stands and where it stops.

## Two-Paragraph Form

### Paragraph 1: Method and Strongest Evidence

Include:

- method or formulation in one sentence
- strongest stable result
- ablation or diagnostic support if available
- final bounded takeaway

Avoid:

- re-explaining every module
- adding new numbers
- adding a new term

### Paragraph 2: Boundary and Future Work

Include:

- key assumption
- observed or plausible failure regimes grounded in the paper
- future work directly derived from the boundary

Avoid:

- wish lists
- promises not connected to limitations
- reviving removed analysis

## Skeleton

```text
We presented [method/formulation] for [task/setting]. In [evaluation], the
method achieved [strongest stable result] compared with [baseline], and
ablations indicate that [component/contribution].

The current method assumes [boundary]. Performance degrades when [failure
regime]. Future work should therefore address [direct extension].
```

## Final Gate

Before finalizing:

- Does the first paragraph only recover method and strongest evidence?
- Is every limitation anchored earlier?
- Is future work a direct consequence of a limitation?
- Are there any new claims, terms, or results? If yes, remove them.
