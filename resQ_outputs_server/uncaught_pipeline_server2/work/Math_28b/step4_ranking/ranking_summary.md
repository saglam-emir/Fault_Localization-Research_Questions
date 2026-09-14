# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexSolver.java', 119), ('SimplexSolver.java', 128), ('SimplexSolver.java', 138), ('SimplexSolver.java', 152)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('SimplexSolver.java', 128, '->', 113), ('SimplexSolver.java', 152, '->', 113)]

Ground_Truth_Answerable: True

- SBFL   ranked 773 statement(s)
- Hybrid ranked 260 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 30 | AbstractLinearOptimizer.java:128 | 1.0 | `throw new MaxCountExceededException(maxIterations);` |
| 1 | 30 | ArgUtils.java:45 | 1.0 | `if (o instanceof Object[]) {` |
| 1 | 30 | ArgUtils.java:46 | 1.0 | `for (Object oR : flatten((Object[]) o)) {` |
| 1 | 30 | ArgUtils.java:50 | 1.0 | `list.add(o);` |
| 1 | 30 | ExceptionContext.java:128 | 1.0 | `return getMessage(Locale.US);` |
| 1 | 30 | ExceptionContext.java:137 | 1.0 | `return getMessage(Locale.getDefault());` |
| 1 | 30 | ExceptionContext.java:147 | 1.0 | `return buildMessage(locale, ": ");` |
| 1 | 30 | ExceptionContext.java:171 | 1.0 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 30 | ExceptionContext.java:172 | 1.0 | `int count = 0;` |
| 1 | 30 | ExceptionContext.java:173 | 1.0 | `final int len = msgPatterns.size();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 260 | AbstractLinearOptimizer.java:74 | 0.0 | `protected AbstractLinearOptimizer() {` |
| 1 | 260 | AbstractLinearOptimizer.java:75 | 0.0 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 1 | 260 | AbstractLinearOptimizer.java:82 | 0.0 | `return nonNegative;` |
| 1 | 260 | AbstractLinearOptimizer.java:96 | 0.0 | `return function;` |
| 1 | 260 | AbstractLinearOptimizer.java:103 | 0.0 | `return Collections.unmodifiableCollection(linearConstraints);` |
| 1 | 260 | AbstractLinearOptimizer.java:108 | 0.0 | `this.maxIterations = maxIterations;` |
| 1 | 260 | AbstractLinearOptimizer.java:139 | 0.0 | `this.function          = f;` |
| 1 | 260 | AbstractLinearOptimizer.java:140 | 0.0 | `this.linearConstraints = constraints;` |
| 1 | 260 | AbstractLinearOptimizer.java:141 | 0.0 | `this.goal              = goalType;` |
| 1 | 260 | AbstractLinearOptimizer.java:142 | 0.0 | `this.nonNegative       = restrictToNonNegative;` |

