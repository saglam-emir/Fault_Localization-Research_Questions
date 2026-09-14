# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CMAESOptimizer.java', 540)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CMAESOptimizer.java', 540, '->', 529)]

Ground_Truth_Answerable: True

- SBFL   ranked 1555 statement(s)
- Hybrid ranked 46 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 30 | ExceptionContext.java:137 | 1.0 | `return getMessage(Locale.getDefault());` |
| 1 | 30 | ExceptionContext.java:147 | 1.0 | `return buildMessage(locale, ": ");` |
| 1 | 30 | ExceptionContext.java:171 | 1.0 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 30 | ExceptionContext.java:172 | 1.0 | `int count = 0;` |
| 1 | 30 | ExceptionContext.java:173 | 1.0 | `final int len = msgPatterns.size();` |
| 1 | 30 | ExceptionContext.java:174 | 1.0 | `for (int i = 0; i < len; i++) {` |
| 1 | 30 | ExceptionContext.java:175 | 1.0 | `final Localizable pat = msgPatterns.get(i);` |
| 1 | 30 | ExceptionContext.java:176 | 1.0 | `final Object[] args = msgArguments.get(i);` |
| 1 | 30 | ExceptionContext.java:177 | 1.0 | `final MessageFormat fmt = new MessageFormat(pat.getLocalizedString(locale),` |
| 1 | 30 | ExceptionContext.java:179 | 1.0 | `sb.append(fmt.format(args));` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 46 | AbstractConvergenceChecker.java:38 | 1.0 | `private static final double DEFAULT_RELATIVE_THRESHOLD = 100 * Precision.EPSILON;` |
| 1 | 46 | AbstractConvergenceChecker.java:45 | 1.0 | `private static final double DEFAULT_ABSOLUTE_THRESHOLD = 100 * Precision.SAFE_MIN;` |
| 1 | 46 | AbstractConvergenceChecker.java:64 | 1.0 | `public AbstractConvergenceChecker() {` |
| 1 | 46 | AbstractConvergenceChecker.java:65 | 1.0 | `this.relativeThreshold = DEFAULT_RELATIVE_THRESHOLD;` |
| 1 | 46 | AbstractConvergenceChecker.java:66 | 1.0 | `this.absoluteThreshold = DEFAULT_ABSOLUTE_THRESHOLD;` |
| 1 | 46 | BaseAbstractMultivariateOptimizer.java:44 | 1.0 | `protected final Incrementor evaluations = new Incrementor();` |
| 1 | 46 | BaseAbstractMultivariateOptimizer.java:66 | 1.0 | `protected BaseAbstractMultivariateOptimizer(ConvergenceChecker<PointValuePair> checker) {` |
| 1 | 46 | BaseAbstractMultivariateOptimizer.java:67 | 1.0 | `this.checker = checker;` |
| 1 | 46 | BaseAbstractMultivariateSimpleBoundsOptimizer.java:66 | 1.0 | `super(checker);` |
| 1 | 46 | BitsStreamGenerator.java:35 | 1.0 | `public BitsStreamGenerator() {` |

