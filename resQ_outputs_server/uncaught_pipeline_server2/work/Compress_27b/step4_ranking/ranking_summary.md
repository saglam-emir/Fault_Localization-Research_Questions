# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 133), ('TarUtils.java', 134), ('TarUtils.java', 135), ('TarUtils.java', 136)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TarUtils.java', 135, '->', 134)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 136)]

- SBFL   ranked 3124 statement(s)
- Hybrid ranked 15 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarUtils.java:134 | 0.5 | `throw new IllegalArgumentException(` |
| 2 | 5 | TarUtils.java:118 | 0.288675 | `start++;` |
| 2 | 5 | TarUtils.java:247 | 0.288675 | `String string = new String(buffer, offset, length);` |
| 2 | 5 | TarUtils.java:249 | 0.288675 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 2 | 5 | TarUtils.java:250 | 0.288675 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 2 | 5 | TarUtils.java:251 | 0.288675 | `return s;` |
| 7 | 2 | ArchiveStreamFactory.java:77 | 0.151523 | `public class ArchiveStreamFactory {` |
| 7 | 2 | ArchiveStreamFactory.java:123 | 0.151523 | `private String entryEncoding = null;` |
| 9 | 1 | TarUtils.java:112 | 0.121268 | `return 0L;` |
| 10 | 1 | TarUtils.java:149 | 0.076249 | `return result;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | TarUtils.java:103 | 0.0 | `long    result = 0;` |
| 1 | 15 | TarUtils.java:104 | 0.0 | `int     end = offset + length;` |
| 1 | 15 | TarUtils.java:105 | 0.0 | `int     start = offset;` |
| 1 | 15 | TarUtils.java:111 | 0.0 | `if (buffer[start] == 0) {` |
| 1 | 15 | TarUtils.java:112 | 0.0 | `return 0L;` |
| 1 | 15 | TarUtils.java:116 | 0.0 | `while (start < end){` |
| 1 | 15 | TarUtils.java:117 | 0.0 | `if (buffer[start] == ' '){` |
| 1 | 15 | TarUtils.java:118 | 0.0 | `start++;` |
| 1 | 15 | TarUtils.java:128 | 0.0 | `byte trailer = buffer[end - 1];` |
| 1 | 15 | TarUtils.java:129 | 0.0 | `while (start < end && (trailer == 0 || trailer == ' ')) {` |

