# Captions

Use this for English figure captions and table notes.

## Caption Jobs

A caption should:

- name the visual's job
- define what is shown
- explain reading order when needed
- clarify labels, metrics, and categories
- state boundary if the visual might be overread

It should not:

- replace missing Methods text
- claim unshown mechanisms
- repeat every sentence from Results
- introduce unsupported claims

## Patterns

Motivation figure:

```latex
\caption{\textbf{Failure mode under [condition].} [Panel description] shows
[observable issue], motivating [paper problem] rather than proving [method].}
```

Framework figure:

```latex
\caption{\textbf{System overview.} Left: [hardware/roles]. Right: [information
flow or control loop]. The panels correspond to [Methods sections].}
```

Results table:

```latex
\caption{\textbf{Main results.} [Metric definition and comparison scope]. Higher
or lower is better for [metric].}
```

## Consistency Checks

- metric names match prose
- category names match table notes
- panel letters match text references
- caption title style is consistent
- abbreviations are defined once and reused
