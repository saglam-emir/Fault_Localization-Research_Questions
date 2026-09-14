# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CholeskyDecompositionImpl.java', 114), ('CholeskyDecompositionImpl.java', 115), ('CholeskyDecompositionImpl.java', 116), ('CholeskyDecompositionImpl.java', 137)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CholeskyDecompositionImpl.java', 137, '->', 132)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/linear/CholeskyDecompositionImpl.java', 115), ('src/java/org/apache/commons/math/linear/CholeskyDecompositionImpl.java', 116)]

- SBFL   ranked 411 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | AbstractRealMatrix.java:991 | 0.707107 | `final int nRows = getRowDimension();` |
| 1 | 17 | AbstractRealMatrix.java:992 | 0.707107 | `final int nCols = getColumnDimension();` |
| 1 | 17 | AbstractRealMatrix.java:993 | 0.707107 | `final StringBuffer res = new StringBuffer();` |
| 1 | 17 | AbstractRealMatrix.java:994 | 0.707107 | `String fullClassName = getClass().getName();` |
| 1 | 17 | AbstractRealMatrix.java:995 | 0.707107 | `String shortClassName = fullClassName.substring(fullClassName.lastIndexOf('.') + 1);` |
| 1 | 17 | AbstractRealMatrix.java:996 | 0.707107 | `res.append(shortClassName).append("{");` |
| 1 | 17 | AbstractRealMatrix.java:998 | 0.707107 | `for (int i = 0; i < nRows; ++i) {` |
| 1 | 17 | AbstractRealMatrix.java:999 | 0.707107 | `if (i > 0) {` |
| 1 | 17 | AbstractRealMatrix.java:1000 | 0.707107 | `res.append(",");` |
| 1 | 17 | AbstractRealMatrix.java:1002 | 0.707107 | `res.append("{");` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

