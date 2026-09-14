# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('OpenMapRealVector.java', 349), ('OpenMapRealVector.java', 350), ('OpenMapRealVector.java', 351), ('OpenMapRealVector.java', 352), ('OpenMapRealVector.java', 374)]

Ground_Truth_Answerable: True

- SBFL   ranked 184 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 184 | FastMath.java:113 | 0.0 | `private static final double LN_QUICK_COEF[][] = {` |
| 1 | 184 | FastMath.java:126 | 0.0 | `private static final double LN_HI_PREC_COEF[][] = {` |
| 1 | 184 | FastMath.java:139 | 0.0 | `private static final double SINE_TABLE_A[] =` |
| 1 | 184 | FastMath.java:158 | 0.0 | `private static final double SINE_TABLE_B[] =` |
| 1 | 184 | FastMath.java:177 | 0.0 | `private static final double COSINE_TABLE_A[] =` |
| 1 | 184 | FastMath.java:196 | 0.0 | `private static final double COSINE_TABLE_B[] =` |
| 1 | 184 | FastMath.java:216 | 0.0 | `private static final double TANGENT_TABLE_A[] =` |
| 1 | 184 | FastMath.java:235 | 0.0 | `private static final double TANGENT_TABLE_B[] =` |
| 1 | 184 | FastMath.java:254 | 0.0 | `private static final long RECIP_2PI[] = new long[] {` |
| 1 | 184 | FastMath.java:275 | 0.0 | `private static final long PI_O_4_BITS[] = new long[] {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

