# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BigFraction.java', 306), ('Fraction.java', 215)]

Ground_Truth_Answerable: True

- SBFL   ranked 6315 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 20 | ExceptionContext.java:128 | 0.816497 | `return getMessage(Locale.US);` |
| 1 | 20 | ExceptionContext.java:137 | 0.816497 | `return getMessage(Locale.getDefault());` |
| 1 | 20 | ExceptionContext.java:147 | 0.816497 | `return buildMessage(locale, ": ");` |
| 1 | 20 | ExceptionContext.java:171 | 0.816497 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 20 | ExceptionContext.java:172 | 0.816497 | `int count = 0;` |
| 1 | 20 | ExceptionContext.java:173 | 0.816497 | `final int len = msgPatterns.size();` |
| 1 | 20 | ExceptionContext.java:174 | 0.816497 | `for (int i = 0; i < len; i++) {` |
| 1 | 20 | ExceptionContext.java:175 | 0.816497 | `final Localizable pat = msgPatterns.get(i);` |
| 1 | 20 | ExceptionContext.java:176 | 0.816497 | `final Object[] args = msgArguments.get(i);` |
| 1 | 20 | ExceptionContext.java:177 | 0.816497 | `final MessageFormat fmt = new MessageFormat(pat.getLocalizedString(locale),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

