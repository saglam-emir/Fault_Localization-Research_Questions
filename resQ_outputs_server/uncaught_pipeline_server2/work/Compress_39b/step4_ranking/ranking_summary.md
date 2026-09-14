# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArchiveUtils.java', 31), ('ArchiveUtils.java', 273)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/utils/ArchiveUtils.java', 31)]

- SBFL   ranked 3873 statement(s)
- Hybrid ranked 22 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | ArchiveUtils.java:273 | 0.258199 | `final char[] chars = s.toCharArray();` |
| 1 | 11 | ArchiveUtils.java:274 | 0.258199 | `final int len = chars.length;` |
| 1 | 11 | ArchiveUtils.java:275 | 0.258199 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 11 | ArchiveUtils.java:276 | 0.258199 | `for (int i = 0; i < len; i++) {` |
| 1 | 11 | ArchiveUtils.java:277 | 0.258199 | `final char c = chars[i];` |
| 1 | 11 | ArchiveUtils.java:278 | 0.258199 | `if (!Character.isISOControl(c)) {` |
| 1 | 11 | ArchiveUtils.java:279 | 0.258199 | `Character.UnicodeBlock block = Character.UnicodeBlock.of(c);` |
| 1 | 11 | ArchiveUtils.java:280 | 0.258199 | `if (block != null && block != Character.UnicodeBlock.SPECIALS) {` |
| 1 | 11 | ArchiveUtils.java:281 | 0.258199 | `sb.append(c);` |
| 1 | 11 | ArchiveUtils.java:282 | 0.258199 | `continue;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | ArchiveUtils.java:273 | 1.0 | `final char[] chars = s.toCharArray();` |
| 1 | 9 | ArchiveUtils.java:275 | 1.0 | `final StringBuilder sb = new StringBuilder();` |
| 1 | 9 | ArchiveUtils.java:276 | 1.0 | `for (int i = 0; i < len; i++) {` |
| 1 | 9 | ArchiveUtils.java:277 | 1.0 | `final char c = chars[i];` |
| 1 | 9 | ArchiveUtils.java:278 | 1.0 | `if (!Character.isISOControl(c)) {` |
| 1 | 9 | ArchiveUtils.java:279 | 1.0 | `Character.UnicodeBlock block = Character.UnicodeBlock.of(c);` |
| 1 | 9 | ArchiveUtils.java:280 | 1.0 | `if (block != null && block != Character.UnicodeBlock.SPECIALS) {` |
| 1 | 9 | ArchiveUtils.java:281 | 1.0 | `sb.append(c);` |
| 1 | 9 | ArchiveUtils.java:287 | 1.0 | `return sb.toString();` |
| 10 | 13 | ArchiveUtils.java:75 | 0.0 | `buffer1 = expected.getBytes(CharsetNames.US_ASCII);` |

