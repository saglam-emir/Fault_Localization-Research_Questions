# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BitInputStream.java', 85), ('BitInputStream.java', 98), ('BitInputStream.java', 99), ('BitInputStream.java', 101), ('BitInputStream.java', 108)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/utils/BitInputStream.java', 98), ('src/main/java/org/apache/commons/compress/utils/BitInputStream.java', 99)]

- SBFL   ranked 2099 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | BitInputStream.java:93 | 0.316228 | `bitsCached <<= 8;` |
| 1 | 3 | BitInputStream.java:94 | 0.316228 | `bitsCached |= nextByte;` |
| 1 | 3 | BitInputStream.java:105 | 0.316228 | `bitsOut = (bitsCached >> (bitsCachedSize - count)) & MASKS[count];` |
| 4 | 5 | BitInputStream.java:90 | 0.272166 | `if (byteOrder == ByteOrder.LITTLE_ENDIAN) {` |
| 4 | 5 | BitInputStream.java:96 | 0.272166 | `bitsCachedSize += 8;` |
| 4 | 5 | BitInputStream.java:101 | 0.272166 | `if (byteOrder == ByteOrder.LITTLE_ENDIAN) {` |
| 4 | 5 | BitInputStream.java:107 | 0.272166 | `bitsCachedSize -= count;` |
| 4 | 5 | BitInputStream.java:108 | 0.272166 | `return bitsOut;` |
| 9 | 3 | BitInputStream.java:85 | 0.262613 | `while (bitsCachedSize < count) {` |
| 9 | 3 | BitInputStream.java:86 | 0.262613 | `final long nextByte = in.read();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

