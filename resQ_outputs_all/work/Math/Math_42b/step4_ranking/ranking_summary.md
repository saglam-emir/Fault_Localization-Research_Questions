# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexTableau.java', 413), ('SimplexTableau.java', 410)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('SimplexTableau.java', 410, '->', 403)]

Ground_Truth_Answerable: True

- SBFL   ranked 787 statement(s)
- Hybrid ranked 227 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | RealPointValuePair.java:68 | 0.258199 | `return (point == null) ? null : point.clone();` |
| 2 | 1 | SimplexTableau.java:347 | 0.25 | `columnsToDrop.add(col);` |
| 3 | 35 | Array2DRowRealMatrix.java:73 | 0.242536 | `throws DimensionMismatchException, NoDataException, NullArgumentException {` |
| 3 | 35 | Array2DRowRealMatrix.java:74 | 0.242536 | `copyIn(d);` |
| 3 | 35 | Array2DRowRealMatrix.java:261 | 0.242536 | `if (data == null) {` |
| 3 | 35 | Array2DRowRealMatrix.java:262 | 0.242536 | `if (row > 0) {` |
| 3 | 35 | Array2DRowRealMatrix.java:265 | 0.242536 | `if (column > 0) {` |
| 3 | 35 | Array2DRowRealMatrix.java:268 | 0.242536 | `MathUtils.checkNotNull(subMatrix);` |
| 3 | 35 | Array2DRowRealMatrix.java:269 | 0.242536 | `final int nRows = subMatrix.length;` |
| 3 | 35 | Array2DRowRealMatrix.java:270 | 0.242536 | `if (nRows == 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Precision.java:68 | 0.707107 | `return -1;` |
| 2 | 101 | AbstractLinearOptimizer.java:110 | 0.57735 | `this.function          = f;` |
| 2 | 101 | AbstractLinearOptimizer.java:111 | 0.57735 | `this.linearConstraints = constraints;` |
| 2 | 101 | AbstractLinearOptimizer.java:113 | 0.57735 | `this.nonNegative       = restrictToNonNegative;` |
| 2 | 101 | AbstractLinearOptimizer.java:118 | 0.57735 | `return doOptimize();` |
| 2 | 101 | Array2DRowRealMatrix.java:56 | 0.57735 | `data = new double[rowDimension][columnDimension];` |
| 2 | 101 | Array2DRowRealMatrix.java:74 | 0.57735 | `copyIn(d);` |
| 2 | 101 | Array2DRowRealMatrix.java:261 | 0.57735 | `if (data == null) {` |
| 2 | 101 | Array2DRowRealMatrix.java:274 | 0.57735 | `final int nCols = subMatrix[0].length;` |
| 2 | 101 | Array2DRowRealMatrix.java:278 | 0.57735 | `data = new double[subMatrix.length][nCols];` |

