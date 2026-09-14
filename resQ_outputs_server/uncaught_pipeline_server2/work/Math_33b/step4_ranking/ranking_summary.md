# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexTableau.java', 338)]

Ground_Truth_Answerable: True

- SBFL   ranked 803 statement(s)
- Hybrid ranked 236 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Relationship.java:59 | 0.707107 | `return GEQ;` |
| 2 | 2 | SimplexTableau.java:406 | 0.57735 | `coefficients[i] = 0;` |
| 2 | 2 | SimplexTableau.java:407 | 0.57735 | `continue;` |
| 4 | 3 | Relationship.java:57 | 0.447214 | `switch (this) {` |
| 4 | 3 | SimplexTableau.java:261 | 0.447214 | `return new LinearConstraint(constraint.getCoefficients().mapMultiply(-1),` |
| 4 | 3 | SimplexTableau.java:339 | 0.447214 | `columnsToDrop.add(i);` |
| 7 | 1 | SimplexTableau.java:226 | 0.27735 | `matrix.setEntry(row, getSlackVariableOffset() + slackVar++, -1); // excess` |
| 8 | 10 | Pair.java:63 | 0.25 | `return key;` |
| 8 | 10 | PointValuePair.java:67 | 0.25 | `final double[] p = getKey();` |
| 8 | 10 | PointValuePair.java:68 | 0.25 | `return p == null ? null : p.clone();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Precision.java:90 | 0.5 | `return 0;` |
| 2 | 3 | Precision.java:89 | 0.447214 | `if (equals(x, y, eps)) {` |
| 2 | 3 | Precision.java:265 | 0.447214 | `return equals(x, y, 1) || FastMath.abs(y - x) <= eps;` |
| 2 | 3 | Precision.java:314 | 0.447214 | `return isEqual && !Double.isNaN(x) && !Double.isNaN(y);` |
| 5 | 232 | AbstractLinearOptimizer.java:74 | 0.0 | `protected AbstractLinearOptimizer() {` |
| 5 | 232 | AbstractLinearOptimizer.java:75 | 0.0 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 5 | 232 | AbstractLinearOptimizer.java:82 | 0.0 | `return nonNegative;` |
| 5 | 232 | AbstractLinearOptimizer.java:96 | 0.0 | `return function;` |
| 5 | 232 | AbstractLinearOptimizer.java:103 | 0.0 | `return Collections.unmodifiableCollection(linearConstraints);` |
| 5 | 232 | AbstractLinearOptimizer.java:108 | 0.0 | `this.maxIterations = maxIterations;` |

