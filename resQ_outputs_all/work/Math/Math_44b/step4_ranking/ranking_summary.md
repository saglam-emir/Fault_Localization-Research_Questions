# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('AbstractIntegrator.java', 280), ('AbstractIntegrator.java', 334), ('AbstractIntegrator.java', 343)]

Ground_Truth_Answerable: True

- SBFL   ranked 3597 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | AdaptiveStepsizeIntegrator.java:209 | 0.408248 | `if ((initialStepSize < minStep) || (initialStepSize > maxStep)) {` |
| 1 | 3 | AdaptiveStepsizeIntegrator.java:212 | 0.408248 | `initialStep = initialStepSize;` |
| 1 | 3 | AdaptiveStepsizeIntegrator.java:252 | 0.408248 | `return forward ? initialStep : -initialStep;` |
| 4 | 3 | FastMath.java:3373 | 0.267261 | `y += 1.0;` |
| 4 | 3 | FastMath.java:3375 | 0.267261 | `if (y == 0) {` |
| 4 | 3 | FastMath.java:3379 | 0.267261 | `return y;` |
| 7 | 1 | EventState.java:334 | 0.223607 | `handler.resetState(t, y);` |
| 8 | 2 | BracketingNthOrderBrentSolver.java:172 | 0.204124 | `nbPoints        = 2;` |
| 8 | 2 | BracketingNthOrderBrentSolver.java:173 | 0.204124 | `signChangeIndex = 1;` |
| 10 | 4 | AbstractIntegrator.java:340 | 0.196116 | `System.arraycopy(eventY, 0, y, 0, y.length);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

