# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PolygonsSet.java', 136)]

Ground_Truth_Answerable: True

- SBFL   ranked 1621 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | AVLTree.java:167 | 1.0 | `return null;` |
| 1 | 9 | PolygonsSet.java:135 | 1.0 | `final BSPTree<Euclidean2D> tree = getTree(false);` |
| 1 | 9 | PolygonsSet.java:136 | 1.0 | `if ((Boolean) tree.getAttribute()) {` |
| 1 | 9 | PolygonsSet.java:330 | 1.0 | `return null;` |
| 1 | 9 | PolyhedronsSet.java:83 | 1.0 | `super(boundary);` |
| 1 | 9 | SubLine.java:56 | 1.0 | `/** Create a sub-line from a segment.` |
| 1 | 9 | SubLine.java:57 | 1.0 | `* @param segment single segment forming the sub-line` |
| 1 | 9 | SubLine.java:139 | 1.0 | `` |
| 1 | 9 | SubLine.java:140 | 1.0 | `` |
| 10 | 4 | FastMath.java:2480 | 0.707107 | `final double denom = 1d / (1d + (xa + xb) * (TANGENT_TABLE_A[idx] + TANGENT_TABLE_B[idx]));` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

