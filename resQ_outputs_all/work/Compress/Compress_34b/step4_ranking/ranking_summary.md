# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('X7875_NewUnix.java', 58), ('X7875_NewUnix.java', 146)]

Ground_Truth_Answerable: True

- SBFL   ranked 3600 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | X7875_NewUnix.java:122 | 0.707107 | `this.gid = ZipUtil.longToBig(l);` |
| 1 | 2 | X7875_NewUnix.java:146 | 0.707107 | `return getLocalFileDataLength();` |
| 3 | 8 | X7875_NewUnix.java:95 | 0.5 | `public long getUID() { return ZipUtil.bigToLong(uid); }` |
| 3 | 8 | X7875_NewUnix.java:105 | 0.5 | `public long getGID() { return ZipUtil.bigToLong(gid); }` |
| 3 | 8 | X7875_NewUnix.java:113 | 0.5 | `this.uid = ZipUtil.longToBig(l);` |
| 3 | 8 | ZipUtil.java:136 | 0.5 | `if (big.bitLength() <= 63) { // bitLength() doesn't count the sign bit.` |
| 3 | 8 | ZipUtil.java:137 | 0.5 | `return big.longValue();` |
| 3 | 8 | ZipUtil.java:155 | 0.5 | `if (l < Integer.MIN_VALUE) {` |
| 3 | 8 | ZipUtil.java:157 | 0.5 | `} else if (l < 0 && l >= Integer.MIN_VALUE) {` |
| 3 | 8 | ZipUtil.java:162 | 0.5 | `return BigInteger.valueOf(l);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

