# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('RandomStringUtils.java', 245)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('RandomStringUtils.java', 245, '->', 234)]

Ground_Truth_Answerable: True

- SBFL   ranked 51 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | RandomStringUtils.java:253 | 0.57735 | `ch = (char) (random.nextInt(gap) + start);` |
| 2 | 6 | RandomStringUtils.java:163 | 0.5 | `return random(count, start, end, letters, numbers, null, RANDOM);` |
| 2 | 6 | RandomStringUtils.java:234 | 0.5 | `if (start == 0 && end == 0) {` |
| 2 | 6 | RandomStringUtils.java:247 | 0.5 | `char[] buffer = new char[count];` |
| 2 | 6 | RandomStringUtils.java:248 | 0.5 | `int gap = end - start;` |
| 2 | 6 | RandomStringUtils.java:250 | 0.5 | `while (count-- != 0) {` |
| 2 | 6 | RandomStringUtils.java:252 | 0.5 | `if (chars == null) {` |
| 8 | 3 | RandomStringUtils.java:225 | 0.447214 | `if (count == 0) {` |
| 8 | 3 | RandomStringUtils.java:227 | 0.447214 | `} else if (count < 0) {` |
| 8 | 3 | RandomStringUtils.java:230 | 0.447214 | `if (chars != null && chars.length == 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

