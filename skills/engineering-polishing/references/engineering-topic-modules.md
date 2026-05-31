# Engineering Topic Modules

Use only when the source clearly supports the topic. Do not force a module onto
unrelated material.

## Multi-Scale, Multi-Physics, or Mechanism

Clarify:

- why coupling is needed
- what is coupled
- which metric or phenomenon the coupling explains
- what evidence supports the interpretation
- where the explanation stops

## Model, Algorithm, or Optimization

Organize around:

- object
- variables
- constraints
- objective
- solver or procedure
- validation
- boundary

Do not invent solver details when the source only states the method name.

## Control or Closed-Loop System

Organize around:

- observation
- feedback signal
- control law
- execution system
- stability or real-time condition if provided
- error metric
- safety or failure state

Avoid claiming stability or robustness unless the paper actually analyzes or
tests it.

## Data-Driven Monitoring or Prediction

Organize around:

- data source
- task objective
- model role
- generalization regime
- interpretability or uncertainty if provided
- validation metric

Do not imply generalization beyond the evaluated split or platform.

## Materials, Interface, or Micro-Mechanism

Organize around:

- structure or interface feature
- performance effect
- interaction mechanism
- dynamic behavior
- theoretical boundary
- validation method

## Process, Manufacturing, or Test

Organize around:

- object requirement
- process principle
- motion/contact/error mechanism
- equipment realization
- precision or quality metric
- validation condition
