# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('RandomStringUtils.java', 230), ('RandomStringUtils.java', 232), ('RandomStringUtils.java', 238)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('RandomStringUtils.java', 238, '->', 231)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/RandomStringUtils.java', 230)]

- SBFL   ranked 46 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | RandomStringUtils.java:248 | 0.816497 | `ch = chars[random.nextInt(gap) + start];` |
| 2 | 10 | RandomStringUtils.java:225 | 0.707107 | `if (count == 0) {` |
| 2 | 10 | RandomStringUtils.java:227 | 0.707107 | `} else if (count < 0) {` |
| 2 | 10 | RandomStringUtils.java:228 | 0.707107 | `throw new IllegalArgumentException("Requested random string length " + count + " is less than 0.");` |
| 2 | 10 | RandomStringUtils.java:231 | 0.707107 | `if (start == 0 && end == 0) {` |
| 2 | 10 | RandomStringUtils.java:232 | 0.707107 | `if (!letters && !numbers) {` |
| 2 | 10 | RandomStringUtils.java:233 | 0.707107 | `end = Integer.MAX_VALUE;` |
| 2 | 10 | RandomStringUtils.java:240 | 0.707107 | `char[] buffer = new char[count];` |
| 2 | 10 | RandomStringUtils.java:241 | 0.707107 | `int gap = end - start;` |
| 2 | 10 | RandomStringUtils.java:243 | 0.707107 | `while (count-- != 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

