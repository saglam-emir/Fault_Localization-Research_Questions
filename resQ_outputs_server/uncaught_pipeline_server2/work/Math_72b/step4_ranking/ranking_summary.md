# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BrentSolver.java', 115), ('BrentSolver.java', 127)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/analysis/solvers/BrentSolver.java', 127)]

- SBFL   ranked 2930 statement(s)
- Hybrid ranked 109 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | BrentSolver.java:115 | 1.0 | `setResult(yMin, 0);` |
| 1 | 4 | BrentSolver.java:116 | 1.0 | `return result;` |
| 1 | 4 | BrentSolver.java:184 | 1.0 | `setResult(max, 0);` |
| 1 | 4 | BrentSolver.java:185 | 1.0 | `ret = max;` |
| 5 | 10 | BrentSolver.java:102 | 0.57735 | `clearResult();` |
| 5 | 10 | BrentSolver.java:103 | 0.57735 | `verifySequence(min, initial, max);` |
| 5 | 10 | BrentSolver.java:106 | 0.57735 | `double yInitial = f.value(initial);` |
| 5 | 10 | BrentSolver.java:107 | 0.57735 | `if (Math.abs(yInitial) <= functionValueAccuracy) {` |
| 5 | 10 | BrentSolver.java:113 | 0.57735 | `double yMin = f.value(min);` |
| 5 | 10 | BrentSolver.java:114 | 0.57735 | `if (Math.abs(yMin) <= functionValueAccuracy) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | BrentSolver.java:102 | 1.0 | `clearResult();` |
| 1 | 8 | BrentSolver.java:103 | 1.0 | `verifySequence(min, initial, max);` |
| 1 | 8 | BrentSolver.java:106 | 1.0 | `double yInitial = f.value(initial);` |
| 1 | 8 | BrentSolver.java:107 | 1.0 | `if (Math.abs(yInitial) <= functionValueAccuracy) {` |
| 1 | 8 | BrentSolver.java:113 | 1.0 | `double yMin = f.value(min);` |
| 1 | 8 | BrentSolver.java:114 | 1.0 | `if (Math.abs(yMin) <= functionValueAccuracy) {` |
| 1 | 8 | BrentSolver.java:115 | 1.0 | `setResult(yMin, 0);` |
| 1 | 8 | BrentSolver.java:185 | 1.0 | `ret = max;` |
| 9 | 7 | BrentSolver.java:180 | 0.707107 | `if (Math.abs(yMin) <= functionValueAccuracy) {` |
| 9 | 7 | BrentSolver.java:183 | 0.707107 | `} else if (Math.abs(yMax) <= functionValueAccuracy) {` |

