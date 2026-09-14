# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PearsonsCorrelation.java', 171)]

Ground_Truth_Answerable: True

- SBFL   ranked 515 statement(s)
- Hybrid ranked 98 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | PearsonsCorrelation.java:68 | 1.0 | `this(new BlockRealMatrix(data));` |
| 2 | 70 | Beta.java:54 | 0.447214 | `return regularizedBeta(x, a, b, DEFAULT_EPSILON, Integer.MAX_VALUE);` |
| 2 | 70 | Beta.java:121 | 0.447214 | `if (Double.isNaN(x) || Double.isNaN(a) || Double.isNaN(b) || (x < 0) ||` |
| 2 | 70 | Beta.java:125 | 0.447214 | `} else if (x > (a + 1.0) / (a + b + 2.0)) {` |
| 2 | 70 | Beta.java:128 | 0.447214 | `ContinuedFraction fraction = new ContinuedFraction() {` |
| 2 | 70 | Beta.java:134 | 0.447214 | `if (n % 2 == 0) { // even` |
| 2 | 70 | Beta.java:135 | 0.447214 | `m = n / 2.0;` |
| 2 | 70 | Beta.java:136 | 0.447214 | `ret = (m * (b - m) * x) /` |
| 2 | 70 | Beta.java:139 | 0.447214 | `m = (n - 1.0) / 2.0;` |
| 2 | 70 | Beta.java:140 | 0.447214 | `ret = -((a + m) * (a + b + m) * x) /` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | BlockRealMatrix.java:1238 | 1.0 | `final int iBlock = row    / BLOCK_SIZE;` |
| 1 | 8 | BlockRealMatrix.java:1239 | 1.0 | `final int jBlock = column / BLOCK_SIZE;` |
| 1 | 8 | BlockRealMatrix.java:1240 | 1.0 | `final int k      = (row    - iBlock * BLOCK_SIZE) * blockWidth(jBlock) +` |
| 1 | 8 | BlockRealMatrix.java:1242 | 1.0 | `return blocks[iBlock * blockColumns + jBlock][k];` |
| 1 | 8 | PearsonsCorrelation.java:68 | 1.0 | `this(new BlockRealMatrix(data));` |
| 1 | 8 | PearsonsCorrelation.java:162 | 1.0 | `int nVars = correlationMatrix.getColumnDimension();` |
| 1 | 8 | PearsonsCorrelation.java:163 | 1.0 | `double[][] out = new double[nVars][nVars];` |
| 1 | 8 | PearsonsCorrelation.java:175 | 1.0 | `return new BlockRealMatrix(out);` |
| 9 | 20 | BlockRealMatrix.java:154 | 0.707107 | `blockColumns = (columns + BLOCK_SIZE - 1) / BLOCK_SIZE;` |
| 9 | 20 | BlockRealMatrix.java:156 | 0.707107 | `if (copyArray) {` |

