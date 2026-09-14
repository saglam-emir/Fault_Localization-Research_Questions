# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonPointer.java', 193)]

Ground_Truth_Answerable: True

- SBFL   ranked 77 statement(s)
- Hybrid ranked 29 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | NumberInput.java:91 | 1.0 | `return Integer.parseInt(s);` |
| 2 | 12 | JsonPointer.java:204 | 0.707107 | `return NumberInput.parseInt(str);` |
| 2 | 12 | NumberInput.java:68 | 0.707107 | `char c = s.charAt(0);` |
| 2 | 12 | NumberInput.java:69 | 0.707107 | `int len = s.length();` |
| 2 | 12 | NumberInput.java:70 | 0.707107 | `boolean neg = (c == '-');` |
| 2 | 12 | NumberInput.java:71 | 0.707107 | `int offset = 1;` |
| 2 | 12 | NumberInput.java:74 | 0.707107 | `if (neg) {` |
| 2 | 12 | NumberInput.java:80 | 0.707107 | `if (len > 9) {` |
| 2 | 12 | NumberInput.java:84 | 0.707107 | `if (c > '9' || c < '0') {` |
| 2 | 12 | NumberInput.java:87 | 0.707107 | `int num = c - '0';` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | JsonPointer.java:26 | 0.0 | `protected final static JsonPointer EMPTY = new JsonPointer();` |
| 1 | 29 | JsonPointer.java:55 | 0.0 | `protected JsonPointer() {` |
| 1 | 29 | JsonPointer.java:56 | 0.0 | `_nextSegment = null;` |
| 1 | 29 | JsonPointer.java:57 | 0.0 | `_matchingPropertyName = "";` |
| 1 | 29 | JsonPointer.java:58 | 0.0 | `_matchingElementIndex = -1;` |
| 1 | 29 | JsonPointer.java:59 | 0.0 | `_asString = "";` |
| 1 | 29 | JsonPointer.java:67 | 0.0 | `_nextSegment = next;` |
| 1 | 29 | JsonPointer.java:95 | 0.0 | `if (input.charAt(0) != '/') {` |
| 1 | 29 | JsonPointer.java:98 | 0.0 | `return _parseTail(input);` |
| 1 | 29 | JsonPointer.java:160 | 0.0 | `return _nextSegment;` |

