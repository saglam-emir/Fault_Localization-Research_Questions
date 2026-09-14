# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EmbeddedRungeKuttaIntegrator.java', 300), ('RungeKuttaIntegrator.java', 180)]

Ground_Truth_Answerable: True

- SBFL   ranked 2040 statement(s)
- Hybrid ranked 284 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | EmbeddedRungeKuttaIntegrator.java:300 | 0.707107 | `loop     = false;` |
| 1 | 2 | RungeKuttaIntegrator.java:180 | 0.707107 | `loop     = false;` |
| 3 | 3 | AdaptiveStepsizeIntegrator.java:150 | 0.5 | `if ((initialStepSize < minStep) || (initialStepSize > maxStep)) {` |
| 3 | 3 | AdaptiveStepsizeIntegrator.java:153 | 0.5 | `initialStep = initialStepSize;` |
| 3 | 3 | AdaptiveStepsizeIntegrator.java:211 | 0.5 | `return forward ? initialStep : -initialStep;` |
| 6 | 1 | AdaptiveStepsizeIntegrator.java:292 | 0.408248 | `filteredH = maxStep;` |
| 7 | 1 | BrentSolver.java:335 | 0.353553 | `x1 = x1 + 0.5 * tolerance;` |
| 8 | 2 | DummyStepInterpolator.java:107 | 0.288675 | `System.arraycopy(currentState,      0, interpolatedState,       0, currentState.length);` |
| 8 | 2 | DummyStepInterpolator.java:108 | 0.288675 | `System.arraycopy(currentDerivative, 0, interpolatedDerivatives, 0, currentDerivative.length);` |
| 10 | 13 | AbstractStepInterpolator.java:107 | 0.282843 | `protected AbstractStepInterpolator(final double[] y, final boolean forward) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 146 | AbstractIntegrator.java:64 | 1.0 | `public AbstractIntegrator(final String name) {` |
| 1 | 146 | AbstractIntegrator.java:65 | 1.0 | `this.name = name;` |
| 1 | 146 | AbstractIntegrator.java:66 | 1.0 | `stepHandlers = new ArrayList<StepHandler>();` |
| 1 | 146 | AbstractIntegrator.java:67 | 1.0 | `stepStart = Double.NaN;` |
| 1 | 146 | AbstractIntegrator.java:68 | 1.0 | `stepSize  = Double.NaN;` |
| 1 | 146 | AbstractIntegrator.java:69 | 1.0 | `eventsHandlersManager = new CombinedEventsManager();` |
| 1 | 146 | AbstractIntegrator.java:70 | 1.0 | `setMaxEvaluations(-1);` |
| 1 | 146 | AbstractIntegrator.java:71 | 1.0 | `resetEvaluations();` |
| 1 | 146 | AbstractIntegrator.java:123 | 1.0 | `for (StepHandler handler : stepHandlers) {` |
| 1 | 146 | AbstractIntegrator.java:143 | 1.0 | `this.maxEvaluations = (maxEvaluations < 0) ? Integer.MAX_VALUE : maxEvaluations;` |

