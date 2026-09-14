# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('X5455_ExtendedTimestamp.java', 529), ('X5455_ExtendedTimestamp.java', 530)]

Ground_Truth_Answerable: True

- SBFL   ranked 4085 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | X5455_ExtendedTimestamp.java:480 | 0.353553 | `public void setModifyJavaTime(final Date d) { setModifyTime(dateToZipLong(d)); }` |
| 1 | 6 | X5455_ExtendedTimestamp.java:523 | 0.353553 | `if (d == null) { return null; }` |
| 1 | 6 | X5455_ExtendedTimestamp.java:525 | 0.353553 | `return unixTimeToZipLong(d.getTime() / 1000);` |
| 1 | 6 | X5455_ExtendedTimestamp.java:529 | 0.353553 | `final long TWO_TO_32 = 0x100000000L;` |
| 1 | 6 | X5455_ExtendedTimestamp.java:530 | 0.353553 | `if (l >= TWO_TO_32) {` |
| 1 | 6 | X5455_ExtendedTimestamp.java:533 | 0.353553 | `return new ZipLong(l);` |
| 7 | 3 | X5455_ExtendedTimestamp.java:423 | 0.316228 | `bit0_modifyTimePresent = l != null;` |
| 7 | 3 | X5455_ExtendedTimestamp.java:424 | 0.316228 | `flags = (byte) (l != null ? (flags | MODIFY_TIME_BIT)` |
| 7 | 3 | X5455_ExtendedTimestamp.java:426 | 0.316228 | `this.modifyTime = l;` |
| 10 | 2 | ZipLong.java:88 | 0.267261 | `public ZipLong(int value) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

