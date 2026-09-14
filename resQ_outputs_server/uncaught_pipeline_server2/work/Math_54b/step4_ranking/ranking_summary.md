# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Dfp.java', 273), ('Dfp.java', 2319)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Dfp.java', 273, '->', 271)]

Ground_Truth_Answerable: True

- SBFL   ranked 2936 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Dfp.java:2119 | 0.27735 | `buffer[--q] = '-';` |
| 2 | 1 | Dfp.java:1041 | 0.258199 | `return result;` |
| 3 | 2 | Dfp.java:1234 | 0.229416 | `a.exp = b.exp;` |
| 3 | 2 | Dfp.java:2328 | 0.229416 | `exponent--;` |
| 5 | 47 | Dfp.java:576 | 0.223607 | `return new Dfp(getField(), x);` |
| 5 | 47 | Dfp.java:801 | 0.223607 | `return nans == INFINITE;` |
| 5 | 47 | Dfp.java:1105 | 0.223607 | `return exp * 4 - 4;` |
| 5 | 47 | Dfp.java:2305 | 0.223607 | `if (isInfinite()) {` |
| 5 | 47 | Dfp.java:2313 | 0.223607 | `if (isNaN()) {` |
| 5 | 47 | Dfp.java:2317 | 0.223607 | `Dfp y = this;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

