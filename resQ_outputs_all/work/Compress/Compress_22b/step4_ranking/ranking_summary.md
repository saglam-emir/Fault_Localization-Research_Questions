# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BZip2CompressorInputStream.java', 67), ('BZip2CompressorInputStream.java', 135), ('BZip2CompressorInputStream.java', 199), ('BZip2CompressorInputStream.java', 205), ('BZip2CompressorInputStream.java', 211), ('BZip2CompressorInputStream.java', 212), ('BZip2CompressorInputStream.java', 215), ('BZip2CompressorInputStream.java', 216), ('BZip2CompressorInputStream.java', 222), ('BZip2CompressorInputStream.java', 223), ('BZip2CompressorInputStream.java', 226), ('BZip2CompressorInputStream.java', 227), ('BZip2CompressorInputStream.java', 232), ('BZip2CompressorInputStream.java', 853), ('BZip2CompressorInputStream.java', 871), ('BZip2CompressorInputStream.java', 913), ('BZip2CompressorInputStream.java', 942)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BZip2CompressorInputStream.java', 205, '->', 204), ('BZip2CompressorInputStream.java', 211, '->', 210), ('BZip2CompressorInputStream.java', 215, '->', 214), ('BZip2CompressorInputStream.java', 222, '->', 221), ('BZip2CompressorInputStream.java', 226, '->', 225)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 205), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 211), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 212), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 215), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 216), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 853), ('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 913)]

- SBFL   ranked 2891 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | BZip2CompressorInputStream.java:384 | 0.707107 | `throw new IOException("unexpected end of stream");` |
| 1 | 3 | BZip2CompressorOutputStream.java:772 | 0.707107 | `aFreq -= mtfFreq[ge--];` |
| 1 | 3 | BlockSort.java:371 | 0.707107 | `med = eclass[fmap[lo]];` |
| 4 | 78 | BZip2CompressorOutputStream.java:227 | 0.57735 | `yy++;` |
| 4 | 78 | BZip2CompressorOutputStream.java:440 | 0.57735 | `final byte[] block = dataShadow.block;` |
| 4 | 78 | BZip2CompressorOutputStream.java:441 | 0.57735 | `block[lastShadow + 2] = ch;` |
| 4 | 78 | BZip2CompressorOutputStream.java:442 | 0.57735 | `block[lastShadow + 3] = ch;` |
| 4 | 78 | BZip2CompressorOutputStream.java:443 | 0.57735 | `block[lastShadow + 4] = ch;` |
| 4 | 78 | BZip2CompressorOutputStream.java:444 | 0.57735 | `this.last = lastShadow + 3;` |
| 4 | 78 | BZip2CompressorOutputStream.java:446 | 0.57735 | `break;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

