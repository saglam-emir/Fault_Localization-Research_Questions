# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 446)]

Ground_Truth_Answerable: True

- SBFL   ranked 330 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Base64.java:339 | 0.57735 | `buf = new byte[8192];` |
| 1 | 3 | Base64.java:340 | 0.57735 | `pos = 0;` |
| 1 | 3 | Base64.java:341 | 0.57735 | `readPos = 0;` |
| 4 | 1 | Base64.java:262 | 0.534522 | `this(lineLength, lineSeparator, false);` |
| 5 | 1 | Base64InputStream.java:107 | 0.5 | `return singleByte[0] < 0 ? 256 + singleByte[0] : singleByte[0];` |
| 6 | 2 | Base64.java:447 | 0.471405 | `System.arraycopy(lineSeparator, 0, buf, pos, lineSeparator.length);` |
| 6 | 2 | Base64.java:448 | 0.471405 | `pos += lineSeparator.length;` |
| 8 | 36 | Base64.java:324 | 0.408248 | `return this.buf != null;` |
| 8 | 36 | Base64InputStream.java:47 | 0.408248 | `private final byte[] singleByte = new byte[1];` |
| 8 | 36 | Base64InputStream.java:90 | 0.408248 | `super(in);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

