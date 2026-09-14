# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EigenDecompositionImpl.java', 603), ('EigenDecompositionImpl.java', 905), ('EigenDecompositionImpl.java', 906), ('EigenDecompositionImpl.java', 1543)]

Ground_Truth_Answerable: True

- SBFL   ranked 1442 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | EigenDecompositionImpl.java:1509 | 0.57735 | `return;` |
| 1 | 15 | EigenDecompositionImpl.java:1529 | 0.57735 | `tType = -5;` |
| 1 | 15 | EigenDecompositionImpl.java:1530 | 0.57735 | `double s = 0.25 * dMin;` |
| 1 | 15 | EigenDecompositionImpl.java:1533 | 0.57735 | `final int np = nn - 2 * pingPong;` |
| 1 | 15 | EigenDecompositionImpl.java:1534 | 0.57735 | `double b1 = work[np - 2];` |
| 1 | 15 | EigenDecompositionImpl.java:1535 | 0.57735 | `double b2 = work[np - 6];` |
| 1 | 15 | EigenDecompositionImpl.java:1536 | 0.57735 | `final double gam = dN2;` |
| 1 | 15 | EigenDecompositionImpl.java:1537 | 0.57735 | `if (work[np - 8] > b2 || work[np - 4] > b1) {` |
| 1 | 15 | EigenDecompositionImpl.java:1540 | 0.57735 | `double a2 = (work[np - 8] / b2) * (1 + work[np - 4] / b1);` |
| 1 | 15 | EigenDecompositionImpl.java:1543 | 0.57735 | `if (end - start > 2) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

