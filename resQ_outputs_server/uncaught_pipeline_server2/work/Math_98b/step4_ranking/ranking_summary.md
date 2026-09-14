# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BigMatrixImpl.java', 991), ('RealMatrixImpl.java', 779)]

Ground_Truth_Answerable: True

- SBFL   ranked 1833 statement(s)
- Hybrid ranked 26 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | BigMatrixImpl.java:986 | 0.408248 | `if (v.length != this.getColumnDimension()) {` |
| 1 | 19 | BigMatrixImpl.java:989 | 0.408248 | `final int nRows = this.getRowDimension();` |
| 1 | 19 | BigMatrixImpl.java:990 | 0.408248 | `final int nCols = this.getColumnDimension();` |
| 1 | 19 | BigMatrixImpl.java:991 | 0.408248 | `final BigDecimal[] out = new BigDecimal[v.length];` |
| 1 | 19 | BigMatrixImpl.java:992 | 0.408248 | `for (int row = 0; row < nRows; row++) {` |
| 1 | 19 | BigMatrixImpl.java:993 | 0.408248 | `BigDecimal sum = ZERO;` |
| 1 | 19 | BigMatrixImpl.java:994 | 0.408248 | `for (int i = 0; i < nCols; i++) {` |
| 1 | 19 | BigMatrixImpl.java:995 | 0.408248 | `sum = sum.add(data[row][i].multiply(v[i]));` |
| 1 | 19 | BigMatrixImpl.java:997 | 0.408248 | `out[row] = sum;` |
| 1 | 19 | RealMatrixImpl.java:774 | 0.408248 | `final int nRows = this.getRowDimension();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 26 | BigMatrixImpl.java:56 | 0.707107 | `protected BigDecimal data[][] = null;` |
| 1 | 26 | BigMatrixImpl.java:61 | 0.707107 | `protected BigDecimal lu[][] = null;` |
| 1 | 26 | BigMatrixImpl.java:64 | 0.707107 | `protected int[] permutation = null;` |
| 1 | 26 | BigMatrixImpl.java:67 | 0.707107 | `protected int parity = 1;` |
| 1 | 26 | BigMatrixImpl.java:70 | 0.707107 | `private int roundingMode = BigDecimal.ROUND_HALF_UP;` |
| 1 | 26 | BigMatrixImpl.java:73 | 0.707107 | `private int scale = 64;` |
| 1 | 26 | BigMatrixImpl.java:138 | 0.707107 | `public BigMatrixImpl(BigDecimal[][] d, boolean copyArray) {` |
| 1 | 26 | BigMatrixImpl.java:139 | 0.707107 | `if (copyArray) {` |
| 1 | 26 | BigMatrixImpl.java:145 | 0.707107 | `final int nRows = d.length;` |
| 1 | 26 | BigMatrixImpl.java:149 | 0.707107 | `final int nCols = d[0].length;` |

