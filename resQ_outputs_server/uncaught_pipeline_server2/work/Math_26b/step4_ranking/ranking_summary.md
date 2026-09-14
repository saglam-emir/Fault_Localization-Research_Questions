# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Fraction.java', 181), ('Fraction.java', 209)]

Ground_Truth_Answerable: True

- SBFL   ranked 2923 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Fraction.java:182 | 0.707107 | `throw new FractionConversionException(value, a0, 1l);` |
| 1 | 3 | Fraction.java:210 | 0.707107 | `throw new FractionConversionException(value, p2, q2);` |
| 1 | 3 | FractionConversionException.java:53 | 0.707107 | `super(LocalizedFormats.FRACTION_CONVERSION_OVERFLOW, value, p, q);` |
| 4 | 2 | ConvergenceException.java:48 | 0.5 | `Object ... args) {` |
| 4 | 2 | ConvergenceException.java:49 | 0.5 | `getContext().addMessage(pattern, args);` |
| 6 | 2 | MathIllegalStateException.java:69 | 0.267261 | `this(LocalizedFormats.ILLEGAL_STATE);` |
| 6 | 2 | MathIllegalStateException.java:74 | 0.267261 | `return context;` |
| 8 | 3 | MathIllegalStateException.java:45 | 0.25 | `Object ... args) {` |
| 8 | 3 | MathIllegalStateException.java:46 | 0.25 | `context = new ExceptionContext(this);` |
| 8 | 3 | MathIllegalStateException.java:47 | 0.25 | `context.addMessage(pattern, args);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

