# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EmbeddedRungeKuttaIntegrator.java', 245), ('EmbeddedRungeKuttaIntegrator.java', 247), ('EmbeddedRungeKuttaIntegrator.java', 248), ('EmbeddedRungeKuttaIntegrator.java', 250)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/ode/nonstiff/EmbeddedRungeKuttaIntegrator.java', 245)]

- SBFL   ranked 1594 statement(s)
- Hybrid ranked 249 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | AdamsMoultonIntegrator.java:309 | 0.707107 | `final double factor = computeStepGrowShrinkFactor(error);` |
| 1 | 4 | AdamsMoultonIntegrator.java:310 | 0.707107 | `hNew = filterStep(stepSize * factor, forward, false);` |
| 1 | 4 | AdamsMoultonIntegrator.java:311 | 0.707107 | `interpolator.rescale(hNew);` |
| 1 | 4 | AdaptiveStepsizeIntegrator.java:292 | 0.707107 | `filteredH = maxStep;` |
| 5 | 9 | AdamsMoultonIntegrator.java:290 | 0.57735 | `final double dt = manager.getEventTime() - stepStart;` |
| 5 | 9 | AdamsMoultonIntegrator.java:291 | 0.57735 | `if (Math.abs(dt) <= Math.ulp(stepStart)) {` |
| 5 | 9 | AdamsMoultonIntegrator.java:296 | 0.57735 | `hNew = dt;` |
| 5 | 9 | AdamsMoultonIntegrator.java:297 | 0.57735 | `interpolator.rescale(hNew);` |
| 5 | 9 | AdamsMoultonIntegrator.java:299 | 0.57735 | `} else {` |
| 5 | 9 | AdamsMoultonIntegrator.java:356 | 0.57735 | `final double stopTime  = stepStart;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 249 | AbstractIntegrator.java:64 | 0.0 | `public AbstractIntegrator(final String name) {` |
| 1 | 249 | AbstractIntegrator.java:65 | 0.0 | `this.name = name;` |
| 1 | 249 | AbstractIntegrator.java:66 | 0.0 | `stepHandlers = new ArrayList<StepHandler>();` |
| 1 | 249 | AbstractIntegrator.java:67 | 0.0 | `stepStart = Double.NaN;` |
| 1 | 249 | AbstractIntegrator.java:68 | 0.0 | `stepSize  = Double.NaN;` |
| 1 | 249 | AbstractIntegrator.java:69 | 0.0 | `eventsHandlersManager = new CombinedEventsManager();` |
| 1 | 249 | AbstractIntegrator.java:70 | 0.0 | `setMaxEvaluations(-1);` |
| 1 | 249 | AbstractIntegrator.java:71 | 0.0 | `resetEvaluations();` |
| 1 | 249 | AbstractIntegrator.java:87 | 0.0 | `stepHandlers.add(handler);` |
| 1 | 249 | AbstractIntegrator.java:111 | 0.0 | `return eventsHandlersManager.getEventsHandlers();` |

