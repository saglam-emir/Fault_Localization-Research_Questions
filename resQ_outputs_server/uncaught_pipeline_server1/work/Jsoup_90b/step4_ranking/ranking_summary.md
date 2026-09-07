# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HttpConnection.java', 424)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HttpConnection.java', 424, '->', 407)]

Ground_Truth_Answerable: True

- SBFL   ranked 2047 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2047 | Attributes.java:33 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 2047 | Attributes.java:39 | 0.0 | `private static final String[] Empty = {};` |
| 1 | 2047 | Attributes.java:43 | 0.0 | `private int size = 0; // number of slots used (not capacity, which is keys.length` |
| 1 | 2047 | Attributes.java:44 | 0.0 | `String[] keys = Empty;` |
| 1 | 2047 | Attributes.java:45 | 0.0 | `String[] vals = Empty;` |
| 1 | 2047 | Attributes.java:49 | 0.0 | `Validate.isTrue(minNewSize >= size);` |
| 1 | 2047 | Attributes.java:50 | 0.0 | `int curSize = keys.length;` |
| 1 | 2047 | Attributes.java:51 | 0.0 | `if (curSize >= minNewSize)` |
| 1 | 2047 | Attributes.java:54 | 0.0 | `int newSize = curSize >= InitialCapacity ? size * GrowthFactor : InitialCapacity;` |
| 1 | 2047 | Attributes.java:55 | 0.0 | `if (minNewSize > newSize)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

