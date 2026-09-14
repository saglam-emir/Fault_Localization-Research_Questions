# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('RectangularCholeskyDecomposition.java', 69), ('RectangularCholeskyDecomposition.java', 79), ('RectangularCholeskyDecomposition.java', 82), ('RectangularCholeskyDecomposition.java', 83), ('RectangularCholeskyDecomposition.java', 84), ('RectangularCholeskyDecomposition.java', 90), ('RectangularCholeskyDecomposition.java', 91), ('RectangularCholeskyDecomposition.java', 92), ('RectangularCholeskyDecomposition.java', 93), ('RectangularCholeskyDecomposition.java', 128), ('RectangularCholeskyDecomposition.java', 124)]

Ground_Truth_Answerable: True

- SBFL   ranked 1133 statement(s)
- Hybrid ranked 86 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 33 | AbstractRealMatrix.java:97 | 0.816497 | `MatrixUtils.checkSubtractionCompatible(this, m);` |
| 1 | 33 | AbstractRealMatrix.java:99 | 0.816497 | `final int rowCount    = getRowDimension();` |
| 1 | 33 | AbstractRealMatrix.java:100 | 0.816497 | `final int columnCount = getColumnDimension();` |
| 1 | 33 | AbstractRealMatrix.java:101 | 0.816497 | `final RealMatrix out = createMatrix(rowCount, columnCount);` |
| 1 | 33 | AbstractRealMatrix.java:102 | 0.816497 | `for (int row = 0; row < rowCount; ++row) {` |
| 1 | 33 | AbstractRealMatrix.java:103 | 0.816497 | `for (int col = 0; col < columnCount; ++col) {` |
| 1 | 33 | AbstractRealMatrix.java:104 | 0.816497 | `out.setEntry(row, col, getEntry(row, col) - m.getEntry(row, col));` |
| 1 | 33 | AbstractRealMatrix.java:108 | 0.816497 | `return out;` |
| 1 | 33 | AbstractRealMatrix.java:241 | 0.816497 | `return walkInColumnOrder(new RealMatrixPreservingVisitor() {` |
| 1 | 33 | AbstractRealMatrix.java:256 | 0.816497 | `this.endRow = endRow;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 52 | AbstractRealMatrix.java:99 | 0.707107 | `final int rowCount    = getRowDimension();` |
| 1 | 52 | AbstractRealMatrix.java:100 | 0.707107 | `final int columnCount = getColumnDimension();` |
| 1 | 52 | AbstractRealMatrix.java:101 | 0.707107 | `final RealMatrix out = createMatrix(rowCount, columnCount);` |
| 1 | 52 | AbstractRealMatrix.java:241 | 0.707107 | `return walkInColumnOrder(new RealMatrixPreservingVisitor() {` |
| 1 | 52 | AbstractRealMatrix.java:256 | 0.707107 | `this.endRow = endRow;` |
| 1 | 52 | AbstractRealMatrix.java:257 | 0.707107 | `columnSum   = 0;` |
| 1 | 52 | AbstractRealMatrix.java:258 | 0.707107 | `maxColSum   = 0;` |
| 1 | 52 | AbstractRealMatrix.java:263 | 0.707107 | `columnSum += FastMath.abs(value);` |
| 1 | 52 | AbstractRealMatrix.java:264 | 0.707107 | `if (row == endRow) {` |
| 1 | 52 | AbstractRealMatrix.java:265 | 0.707107 | `maxColSum = FastMath.max(maxColSum, columnSum);` |

