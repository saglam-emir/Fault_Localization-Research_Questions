# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SingularValueDecompositionImpl.java', 162), ('SingularValueDecompositionImpl.java', 166), ('SingularValueDecompositionImpl.java', 176), ('SingularValueDecompositionImpl.java', 178), ('SingularValueDecompositionImpl.java', 171), ('SingularValueDecompositionImpl.java', 180), ('SingularValueDecompositionImpl.java', 248), ('SingularValueDecompositionImpl.java', 252), ('SingularValueDecompositionImpl.java', 261), ('SingularValueDecompositionImpl.java', 263), ('SingularValueDecompositionImpl.java', 256), ('SingularValueDecompositionImpl.java', 265)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('SingularValueDecompositionImpl.java', 162, '->', 161), ('SingularValueDecompositionImpl.java', 180, '->', 159), ('SingularValueDecompositionImpl.java', 248, '->', 247)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/linear/SingularValueDecompositionImpl.java', 176), ('src/main/java/org/apache/commons/math/linear/SingularValueDecompositionImpl.java', 261)]

- SBFL   ranked 971 statement(s)
- Hybrid ranked 109 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SingularValueDecompositionImpl.java:143 | 0.816497 | `--p;` |
| 2 | 3 | SingularValueDecompositionImpl.java:283 | 0.707107 | `if (cachedVt == null) {` |
| 2 | 3 | SingularValueDecompositionImpl.java:284 | 0.707107 | `cachedVt = getV().transpose();` |
| 2 | 3 | SingularValueDecompositionImpl.java:288 | 0.707107 | `return cachedVt;` |
| 5 | 8 | MatrixUtils.java:202 | 0.534522 | `final RealMatrix m = createRealMatrix(diagonal.length, diagonal.length);` |
| 5 | 8 | MatrixUtils.java:203 | 0.534522 | `for (int i = 0; i < diagonal.length; ++i) {` |
| 5 | 8 | MatrixUtils.java:204 | 0.534522 | `m.setEntry(i, i, diagonal[i]);` |
| 5 | 8 | MatrixUtils.java:206 | 0.534522 | `return m;` |
| 5 | 8 | SingularValueDecompositionImpl.java:182 | 0.534522 | `wData[i] = new double[p];` |
| 5 | 8 | SingularValueDecompositionImpl.java:217 | 0.534522 | `if (cachedS == null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | AbstractRealMatrix.java:43 | 1.0 | `protected AbstractRealMatrix() {` |
| 1 | 6 | AbstractRealMatrix.java:44 | 1.0 | `lu = null;` |
| 1 | 6 | Array2DRowRealMatrix.java:134 | 1.0 | `throws IllegalArgumentException, NullPointerException {` |
| 1 | 6 | Array2DRowRealMatrix.java:136 | 1.0 | `copyIn(d);` |
| 1 | 6 | BiDiagonalTransformer.java:127 | 1.0 | `return cachedU;` |
| 1 | 6 | SingularValueDecompositionImpl.java:196 | 1.0 | `return cachedU;` |
| 7 | 57 | AbstractRealMatrix.java:266 | 0.816497 | `final RealMatrix subMatrix =` |
| 7 | 57 | AbstractRealMatrix.java:603 | 0.816497 | `final int nRows = getRowDimension();` |
| 7 | 57 | AbstractRealMatrix.java:604 | 0.816497 | `final int nCols = getColumnDimension();` |
| 7 | 57 | AbstractRealMatrix.java:605 | 0.816497 | `final RealMatrix out = createMatrix(nCols, nRows);` |

