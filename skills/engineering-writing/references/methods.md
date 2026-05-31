# Methods

Use this for English Methods sections in engineering papers.

## Core Rule

Methods should define a reader path. It should not read like a module directory.

## Recommended Order

1. Overview: roles, inputs, outputs, and component order.
2. Main object, signal, model, or formulation: why it appears first.
3. Mechanism blocks: one bottleneck per subsection.
4. Execution, training-to-deployment bridge, safety, or operating condition.

## Overview Worksheet

The first paragraph should answer:

- What problem does the method address?
- What are the system roles?
- What is the input and output?
- Which components form the loop?
- Why are the components ordered this way?

Use two to four sentences. Avoid:

```text
This section is organized as follows ...
```

unless the venue explicitly requires a roadmap sentence after the reader path.

## Main Object or Signal Opening

Before formulas, write why the object matters:

```text
Both [downstream component A] and [downstream component B] depend on [main
signal/model]. We therefore first define [object] before describing [modules].
```

This prevents formulas from appearing without motivation.

## Derivation or Algorithm Block

Use this order:

1. observable inputs
2. target variable or object
3. transformation, model, or algorithm
4. approximation or assumption
5. output
6. downstream use
7. residual error or boundary

Do not claim that the derivation proves a system-level result unless Experiments
also test it.

## Mechanism Block

Each block should follow:

```text
problem it solves -> variable/procedure -> operating condition -> connection to
next component
```

If perception, control, training, and safety all appear in one block, split it.

## Execution or Deployment Block

For systems papers, close Methods by returning to how the method runs:

- phases
- confidence or validity gates
- fallback behavior
- timeout or failure state
- safety monitors
- operating envelope

Safety should rejoin the main loop. It should not be a detached threshold note.

## Formatting

- Use consistent run-in headings when the paper style uses them.
- Use one term per concept across Methods, figures, captions, and results.
- Do not coin a term unless the paper formally needs it and uses it repeatedly.

## Minimum Methods Card

Before writing formulas, fill:

| Block | Reader question | Evidence or downstream use | Boundary |
|---|---|---|---|
| Overview | How do I read this system? |  |  |
| Main object/signal | What is being formalized? |  |  |
| Mechanism 1 | What bottleneck is solved? |  |  |
| Execution/safety | How does it run and fail? |  |  |

## Detailed Methods Worksheet

Use this when a Methods section risks becoming a module directory.

| Block | Required question | Must include | Must avoid |
|---|---|---|---|
| Overview | How should the reader traverse the system? | roles, inputs, outputs, component order | table of contents without reader path |
| Main object/signal | What object is formalized first and why? | downstream dependency and notation role | formula before motivation |
| Data or observation | What is observed and what is assumed? | observable inputs, noise/validity limits | hidden sensors or unprovided data |
| Mechanism block | Which bottleneck does this block solve? | variable/procedure, operating condition, link to next block | combining perception/control/training/safety in one paragraph |
| Algorithm or derivation | How is the output produced? | input, transformation, assumption, output, downstream use | claiming system-level proof without experiments |
| Gate/fallback | When does the method stop, switch, or degrade? | confidence gate, timeout, invalid state, recovery | detached threshold note |
| Execution closure | How does the method run in deployment? | phases, rates if known, safety/monitoring, operating envelope | new claims not evaluated later |

Every subsection should close by telling the reader why the next subsection is
needed.
