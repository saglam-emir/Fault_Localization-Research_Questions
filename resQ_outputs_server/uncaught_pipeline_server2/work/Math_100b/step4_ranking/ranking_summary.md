# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('AbstractEstimator.java', 166), ('AbstractEstimator.java', 202), ('AbstractEstimator.java', 207)]

Ground_Truth_Answerable: True

- SBFL   ranked 604 statement(s)
- Hybrid ranked 208 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | EstimatedParameter.java:59 | 1.0 | `boolean bound) {` |
| 1 | 4 | EstimatedParameter.java:60 | 1.0 | `this.name  = name;` |
| 1 | 4 | EstimatedParameter.java:61 | 1.0 | `estimate   = firstEstimate;` |
| 1 | 4 | EstimatedParameter.java:62 | 1.0 | `this.bound = bound;` |
| 5 | 1 | SimpleEstimationProblem.java:58 | 0.707107 | `return (EstimatedParameter[]) parameters.toArray(new EstimatedParameter[parameters.size()]);` |
| 6 | 10 | AbstractEstimator.java:162 | 0.57735 | `updateJacobian();` |
| 6 | 10 | AbstractEstimator.java:165 | 0.57735 | `final int rows = problem.getMeasurements().length;` |
| 6 | 10 | AbstractEstimator.java:166 | 0.57735 | `final int cols = problem.getAllParameters().length;` |
| 6 | 10 | AbstractEstimator.java:167 | 0.57735 | `final int max  = cols * rows;` |
| 6 | 10 | AbstractEstimator.java:168 | 0.57735 | `double[][] jTj = new double[cols][cols];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 208 | AbstractEstimator.java:38 | 0.0 | `protected AbstractEstimator() {` |
| 1 | 208 | AbstractEstimator.java:48 | 0.0 | `this.maxCostEval = maxCostEval;` |
| 1 | 208 | AbstractEstimator.java:57 | 0.0 | `return costEvaluations;` |
| 1 | 208 | AbstractEstimator.java:73 | 0.0 | `incrementJacobianEvaluationsCounter();` |
| 1 | 208 | AbstractEstimator.java:74 | 0.0 | `Arrays.fill(jacobian, 0);` |
| 1 | 208 | AbstractEstimator.java:88 | 0.0 | `++jacobianEvaluations;` |
| 1 | 208 | AbstractEstimator.java:99 | 0.0 | `if (++costEvaluations > maxCostEval) {` |
| 1 | 208 | AbstractEstimator.java:104 | 0.0 | `cost = 0;` |
| 1 | 208 | AbstractEstimator.java:107 | 0.0 | `double residual = wm.getResidual();` |
| 1 | 208 | AbstractEstimator.java:109 | 0.0 | `cost += wm.getWeight() * residual * residual;` |

