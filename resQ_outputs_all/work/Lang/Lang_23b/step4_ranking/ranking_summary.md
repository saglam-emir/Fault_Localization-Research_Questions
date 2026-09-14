# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ExtendedMessageFormat.java', 73), ('ExtendedMessageFormat.java', 263), ('ExtendedMessageFormat.java', 269)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/text/ExtendedMessageFormat.java', 73), ('src/main/java/org/apache/commons/lang3/text/ExtendedMessageFormat.java', 263), ('src/main/java/org/apache/commons/lang3/text/ExtendedMessageFormat.java', 269)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 263 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 116 | ExtendedMessageFormat.java:151 | 0.258199 | `ArrayList<Format> foundFormats = new ArrayList<Format>();` |
| 1 | 116 | ExtendedMessageFormat.java:152 | 0.258199 | `ArrayList<String> foundDescriptions = new ArrayList<String>();` |
| 1 | 116 | ExtendedMessageFormat.java:153 | 0.258199 | `StringBuilder stripCustom = new StringBuilder(pattern.length());` |
| 1 | 116 | ExtendedMessageFormat.java:155 | 0.258199 | `ParsePosition pos = new ParsePosition(0);` |
| 1 | 116 | ExtendedMessageFormat.java:156 | 0.258199 | `char[] c = pattern.toCharArray();` |
| 1 | 116 | ExtendedMessageFormat.java:157 | 0.258199 | `int fmtCount = 0;` |
| 1 | 116 | ExtendedMessageFormat.java:158 | 0.258199 | `while (pos.getIndex() < pattern.length()) {` |
| 1 | 116 | ExtendedMessageFormat.java:159 | 0.258199 | `switch (c[pos.getIndex()]) {` |
| 1 | 116 | ExtendedMessageFormat.java:164 | 0.258199 | `fmtCount++;` |
| 1 | 116 | ExtendedMessageFormat.java:165 | 0.258199 | `seekNonWs(pattern, pos);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

