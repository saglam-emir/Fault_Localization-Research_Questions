# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('OpenMapRealMatrix.java', 50)]

Ground_Truth_Answerable: True

- SBFL   ranked 8396 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | OpenMapRealMatrix.java:49 | 0.105409 | `super(rowDimension, columnDimension);` |
| 1 | 4 | OpenMapRealMatrix.java:50 | 0.105409 | `this.rows = rowDimension;` |
| 1 | 4 | OpenMapRealMatrix.java:51 | 0.105409 | `this.columns = columnDimension;` |
| 1 | 4 | OpenMapRealMatrix.java:52 | 0.105409 | `this.entries = new OpenIntToDoubleHashMap(0.0);` |
| 5 | 13 | OpenIntToDoubleHashMap.java:100 | 0.090167 | `this(DEFAULT_EXPECTED_SIZE, missingEntries);` |
| 5 | 13 | OpenIntToDoubleHashMap.java:117 | 0.090167 | `final double missingEntries) {` |
| 5 | 13 | OpenIntToDoubleHashMap.java:118 | 0.090167 | `final int capacity = computeCapacity(expectedSize);` |
| 5 | 13 | OpenIntToDoubleHashMap.java:119 | 0.090167 | `keys   = new int[capacity];` |
| 5 | 13 | OpenIntToDoubleHashMap.java:120 | 0.090167 | `values = new double[capacity];` |
| 5 | 13 | OpenIntToDoubleHashMap.java:121 | 0.090167 | `states = new byte[capacity];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

