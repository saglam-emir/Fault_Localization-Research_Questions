# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('KMeansPlusPlusClusterer.java', 175)]

Ground_Truth_Answerable: True

- SBFL   ranked 449 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | MathUtils.java:1914 | 1.0 | `public static enum OrderDirection {` |
| 1 | 3 | MathUtils.java:1916 | 1.0 | `INCREASING,` |
| 1 | 3 | MathUtils.java:1918 | 1.0 | `DECREASING` |
| 4 | 15 | KMeansPlusPlusClusterer.java:69 | 0.57735 | `this(random, EmptyClusterStrategy.LARGEST_VARIANCE);` |
| 4 | 15 | KMeansPlusPlusClusterer.java:134 | 0.57735 | `return clusters;` |
| 4 | 15 | KMeansPlusPlusClusterer.java:175 | 0.57735 | `int sum = 0;` |
| 4 | 15 | KMeansPlusPlusClusterer.java:176 | 0.57735 | `for (int i = 0; i < pointSet.size(); i++) {` |
| 4 | 15 | KMeansPlusPlusClusterer.java:177 | 0.57735 | `final T p = pointSet.get(i);` |
| 4 | 15 | KMeansPlusPlusClusterer.java:178 | 0.57735 | `final Cluster<T> nearest = getNearestCluster(resultSet, p);` |
| 4 | 15 | KMeansPlusPlusClusterer.java:179 | 0.57735 | `final double d = p.distanceFrom(nearest.getCenter());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

