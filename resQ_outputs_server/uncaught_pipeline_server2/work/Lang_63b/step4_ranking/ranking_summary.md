# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DurationFormatUtils.java', 306), ('DurationFormatUtils.java', 318), ('DurationFormatUtils.java', 319), ('DurationFormatUtils.java', 320), ('DurationFormatUtils.java', 321), ('DurationFormatUtils.java', 322), ('DurationFormatUtils.java', 323), ('DurationFormatUtils.java', 324), ('DurationFormatUtils.java', 313), ('DurationFormatUtils.java', 432), ('DurationFormatUtils.java', 433), ('DurationFormatUtils.java', 434), ('DurationFormatUtils.java', 435), ('DurationFormatUtils.java', 436), ('DurationFormatUtils.java', 437), ('DurationFormatUtils.java', 438), ('DurationFormatUtils.java', 439), ('DurationFormatUtils.java', 440), ('DurationFormatUtils.java', 441), ('DurationFormatUtils.java', 442), ('DurationFormatUtils.java', 443)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DurationFormatUtils.java', 313, '->', 305)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/time/DurationFormatUtils.java', 432), ('src/java/org/apache/commons/lang/time/DurationFormatUtils.java', 440), ('src/java/org/apache/commons/lang/time/DurationFormatUtils.java', 442), ('src/java/org/apache/commons/lang/time/DurationFormatUtils.java', 443)]

- SBFL   ranked 495 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | DurationFormatUtils.java:306 | 1.0 | `days += 31;` |
| 1 | 7 | DurationFormatUtils.java:312 | 1.0 | `months -= 1;` |
| 1 | 7 | DurationFormatUtils.java:315 | 1.0 | `months += 12;` |
| 1 | 7 | DurationFormatUtils.java:316 | 1.0 | `years -= 1;` |
| 1 | 7 | DurationFormatUtils.java:437 | 1.0 | `int newdiff = startValue - endValue;` |
| 1 | 7 | DurationFormatUtils.java:438 | 1.0 | `end.add( field, newdiff );` |
| 1 | 7 | DurationFormatUtils.java:439 | 1.0 | `return newdiff;` |
| 8 | 12 | DurationFormatUtils.java:247 | 0.707107 | `return formatPeriod(startMillis, endMillis, format, true, TimeZone.getDefault());` |
| 8 | 12 | DurationFormatUtils.java:330 | 0.707107 | `if (Token.containsTokenWithValue(tokens, M)) {` |
| 8 | 12 | DurationFormatUtils.java:331 | 0.707107 | `months += 12 * years;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

