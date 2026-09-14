# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ContinuedFraction.java', 134), ('ContinuedFraction.java', 135), ('ContinuedFraction.java', 143), ('ContinuedFraction.java', 144), ('ContinuedFraction.java', 145), ('ContinuedFraction.java', 146), ('ContinuedFraction.java', 147), ('ContinuedFraction.java', 148), ('ContinuedFraction.java', 149), ('ContinuedFraction.java', 150), ('ContinuedFraction.java', 151), ('ContinuedFraction.java', 152), ('ContinuedFraction.java', 153), ('ContinuedFraction.java', 154), ('ContinuedFraction.java', 155), ('ContinuedFraction.java', 156), ('ContinuedFraction.java', 157), ('ContinuedFraction.java', 158), ('ContinuedFraction.java', 159), ('ContinuedFraction.java', 160), ('ContinuedFraction.java', 161), ('ContinuedFraction.java', 162), ('ContinuedFraction.java', 163), ('ContinuedFraction.java', 164), ('ContinuedFraction.java', 165), ('ContinuedFraction.java', 166), ('ContinuedFraction.java', 169), ('ContinuedFraction.java', 170), ('ContinuedFraction.java', 185), ('ContinuedFraction.java', 186), ('ContinuedFraction.java', 187), ('ContinuedFraction.java', 188), ('ContinuedFraction.java', 189)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ContinuedFraction.java', 151, '->', 150)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 152), ('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 157), ('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 158), ('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 162), ('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 165), ('src/main/java/org/apache/commons/math3/util/ContinuedFraction.java', 166)]

- SBFL   ranked 2677 statement(s)
- Hybrid ranked 174 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | ContinuedFraction.java:177 | 1.0 | `throw new ConvergenceException(LocalizedFormats.CONTINUED_FRACTION_NAN_DIVERGENCE,` |
| 1 | 8 | ConvergenceException.java:48 | 1.0 | `Object ... args) {` |
| 1 | 8 | ConvergenceException.java:49 | 1.0 | `getContext().addMessage(pattern, args);` |
| 1 | 8 | MathIllegalStateException.java:45 | 1.0 | `Object ... args) {` |
| 1 | 8 | MathIllegalStateException.java:46 | 1.0 | `context = new ExceptionContext(this);` |
| 1 | 8 | MathIllegalStateException.java:47 | 1.0 | `context.addMessage(pattern, args);` |
| 1 | 8 | MathIllegalStateException.java:69 | 1.0 | `this(LocalizedFormats.ILLEGAL_STATE);` |
| 1 | 8 | MathIllegalStateException.java:74 | 1.0 | `return context;` |
| 9 | 20 | ExceptionContext.java:128 | 0.707107 | `return getMessage(Locale.US);` |
| 9 | 20 | ExceptionContext.java:137 | 0.707107 | `return getMessage(Locale.getDefault());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 174 | ContinuedFraction.java:125 | 0.0 | `double hPrev = getA(0, x);` |
| 1 | 174 | ContinuedFraction.java:132 | 0.0 | `int n = 1;` |
| 1 | 174 | ContinuedFraction.java:133 | 0.0 | `double dPrev = 0.0;` |
| 1 | 174 | ContinuedFraction.java:134 | 0.0 | `double p0 = 1.0;` |
| 1 | 174 | ContinuedFraction.java:135 | 0.0 | `double q1 = 1.0;` |
| 1 | 174 | ContinuedFraction.java:136 | 0.0 | `double cPrev = hPrev;` |
| 1 | 174 | ContinuedFraction.java:139 | 0.0 | `while (n < maxIterations) {` |
| 1 | 174 | ContinuedFraction.java:140 | 0.0 | `final double a = getA(n, x);` |
| 1 | 174 | ContinuedFraction.java:141 | 0.0 | `final double b = getB(n, x);` |
| 1 | 174 | ContinuedFraction.java:143 | 0.0 | `double cN = a * hPrev + b * p0;` |

