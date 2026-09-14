# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BracketingNthOrderBrentSolver.java', 235), ('BracketingNthOrderBrentSolver.java', 238)]

Ground_Truth_Answerable: True

- SBFL   ranked 2328 statement(s)
- Hybrid ranked 113 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | ExceptionContext.java:128 | 1.0 | `return getMessage(Locale.US);` |
| 1 | 19 | ExceptionContext.java:137 | 1.0 | `return getMessage(Locale.getDefault());` |
| 1 | 19 | ExceptionContext.java:147 | 1.0 | `return buildMessage(locale, ": ");` |
| 1 | 19 | ExceptionContext.java:171 | 1.0 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 19 | ExceptionContext.java:172 | 1.0 | `int count = 0;` |
| 1 | 19 | ExceptionContext.java:173 | 1.0 | `final int len = msgPatterns.size();` |
| 1 | 19 | ExceptionContext.java:174 | 1.0 | `for (int i = 0; i < len; i++) {` |
| 1 | 19 | ExceptionContext.java:175 | 1.0 | `final Localizable pat = msgPatterns.get(i);` |
| 1 | 19 | ExceptionContext.java:176 | 1.0 | `final Object[] args = msgArguments.get(i);` |
| 1 | 19 | ExceptionContext.java:177 | 1.0 | `final MessageFormat fmt = new MessageFormat(pat.getLocalizedString(locale),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | AllowedSolution.java:41 | 1.0 | `public enum AllowedSolution {` |
| 1 | 2 | AllowedSolution.java:62 | 1.0 | `RIGHT_SIDE,` |
| 3 | 111 | AbstractUnivariateRealSolver.java:59 | 0.0 | `super(relativeAccuracy, absoluteAccuracy, functionValueAccuracy);` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:93 | 0.0 | `this.absoluteAccuracy = absoluteAccuracy;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:94 | 0.0 | `this.relativeAccuracy = relativeAccuracy;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:95 | 0.0 | `this.functionValueAccuracy = functionValueAccuracy;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:110 | 0.0 | `return searchMin;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:116 | 0.0 | `return searchMax;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:122 | 0.0 | `return searchStart;` |
| 3 | 111 | BaseAbstractUnivariateRealSolver.java:128 | 0.0 | `return absoluteAccuracy;` |

