# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Rotation.java', 344), ('Rotation.java', 353), ('Rotation.java', 359)]

Ground_Truth_Answerable: True

- SBFL   ranked 2453 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 31 | Rotation.java:313 | 0.707107 | `public Rotation(Vector3D u1, Vector3D u2, Vector3D v1, Vector3D v2) {` |
| 1 | 31 | Rotation.java:316 | 0.707107 | `double u1u1 = u1.getNormSq();` |
| 1 | 31 | Rotation.java:317 | 0.707107 | `double u2u2 = u2.getNormSq();` |
| 1 | 31 | Rotation.java:318 | 0.707107 | `double v1v1 = v1.getNormSq();` |
| 1 | 31 | Rotation.java:319 | 0.707107 | `double v2v2 = v2.getNormSq();` |
| 1 | 31 | Rotation.java:320 | 0.707107 | `if ((u1u1 == 0) || (u2u2 == 0) || (v1v1 == 0) || (v2v2 == 0)) {` |
| 1 | 31 | Rotation.java:325 | 0.707107 | `v1 = new Vector3D(FastMath.sqrt(u1u1 / v1v1), v1);` |
| 1 | 31 | Rotation.java:328 | 0.707107 | `double u1u2   = u1.dotProduct(u2);` |
| 1 | 31 | Rotation.java:329 | 0.707107 | `double v1v2   = v1.dotProduct(v2);` |
| 1 | 31 | Rotation.java:330 | 0.707107 | `double coeffU = u1u2 / u1u1;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

