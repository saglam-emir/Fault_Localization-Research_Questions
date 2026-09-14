# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BisectionSolver.java', 72)]

Ground_Truth_Answerable: True

- SBFL   ranked 68 statement(s)
- Hybrid ranked 51 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | BisectionSolver.java:72 | 1.0 | `return solve(min, max);` |
| 2 | 1 | BisectionSolver.java:66 | 0.707107 | `return solve(f, min, max);` |
| 3 | 10 | BisectionSolver.java:79 | 0.5 | `clearResult();` |
| 3 | 10 | BisectionSolver.java:80 | 0.5 | `verifyInterval(min,max);` |
| 3 | 10 | BisectionSolver.java:85 | 0.5 | `int i = 0;` |
| 3 | 10 | BisectionSolver.java:86 | 0.5 | `while (i < maximalIterationCount) {` |
| 3 | 10 | BisectionSolver.java:87 | 0.5 | `m = UnivariateRealSolverUtils.midpoint(min, max);` |
| 3 | 10 | BisectionSolver.java:88 | 0.5 | `fmin = f.value(min);` |
| 3 | 10 | UnivariateRealSolverImpl.java:165 | 0.5 | `this.iterationCount = 0;` |
| 3 | 10 | UnivariateRealSolverImpl.java:166 | 0.5 | `this.resultComputed = false;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | BisectionSolver.java:52 | 0.27735 | `super(100, 1E-6);` |
| 2 | 12 | ConvergingAlgorithmImpl.java:61 | 0.229416 | `final double defaultAbsoluteAccuracy) {` |
| 2 | 12 | ConvergingAlgorithmImpl.java:62 | 0.229416 | `this.defaultAbsoluteAccuracy = defaultAbsoluteAccuracy;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:63 | 0.229416 | `this.defaultRelativeAccuracy = 1.0e-14;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:64 | 0.229416 | `this.absoluteAccuracy = defaultAbsoluteAccuracy;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:65 | 0.229416 | `this.relativeAccuracy = defaultRelativeAccuracy;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:66 | 0.229416 | `this.defaultMaximalIterationCount = defaultMaximalIterationCount;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:67 | 0.229416 | `this.maximalIterationCount = defaultMaximalIterationCount;` |
| 2 | 12 | ConvergingAlgorithmImpl.java:68 | 0.229416 | `this.iterationCount = 0;` |
| 2 | 12 | UnivariateRealSolverImpl.java:41 | 0.229416 | `protected boolean resultComputed = false;` |

