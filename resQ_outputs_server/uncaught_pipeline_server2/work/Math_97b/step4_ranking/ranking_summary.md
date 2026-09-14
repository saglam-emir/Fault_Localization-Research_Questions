# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BrentSolver.java', 138), ('BrentSolver.java', 145), ('BrentSolver.java', 140), ('BrentSolver.java', 148), ('BrentSolver.java', 149)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BrentSolver.java', 140, '->', 138), ('BrentSolver.java', 148, '->', 138), ('BrentSolver.java', 149, '->', 138)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/analysis/BrentSolver.java', 145)]

- SBFL   ranked 1535 statement(s)
- Hybrid ranked 92 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | BrentSolver.java:141 | 0.5 | `throw new IllegalArgumentException` |
| 1 | 2 | UnivariateRealSolverImpl.java:169 | 0.5 | `return absoluteAccuracy;` |
| 3 | 2 | BrentSolver.java:193 | 0.25 | `setResult(x1, i);` |
| 3 | 2 | BrentSolver.java:194 | 0.25 | `return result;` |
| 5 | 6 | BrentSolver.java:182 | 0.213201 | `x0 = x1;` |
| 5 | 6 | BrentSolver.java:183 | 0.213201 | `x1 = x2;` |
| 5 | 6 | BrentSolver.java:184 | 0.213201 | `x2 = x0;` |
| 5 | 6 | BrentSolver.java:185 | 0.213201 | `y0 = y1;` |
| 5 | 6 | BrentSolver.java:186 | 0.213201 | `y1 = y2;` |
| 5 | 6 | BrentSolver.java:187 | 0.213201 | `y2 = y0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 92 | BrentSolver.java:42 | 0.0 | `super(f, 100, 1E-6);` |
| 1 | 92 | BrentSolver.java:128 | 0.0 | `clearResult();` |
| 1 | 92 | BrentSolver.java:129 | 0.0 | `verifyInterval(min, max);` |
| 1 | 92 | BrentSolver.java:133 | 0.0 | `double yMin = f.value(min);` |
| 1 | 92 | BrentSolver.java:134 | 0.0 | `double yMax = f.value(max);` |
| 1 | 92 | BrentSolver.java:137 | 0.0 | `double sign = yMin * yMax;` |
| 1 | 92 | BrentSolver.java:138 | 0.0 | `if (sign >= 0) {` |
| 1 | 92 | BrentSolver.java:147 | 0.0 | `ret = solve(min, yMin, max, yMax, min, yMin);` |
| 1 | 92 | BrentSolver.java:175 | 0.0 | `double delta = x1 - x0;` |
| 1 | 92 | BrentSolver.java:176 | 0.0 | `double oldDelta = delta;` |

