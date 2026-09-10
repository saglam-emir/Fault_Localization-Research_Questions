# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StrBuilder.java', 1776)]

Ground_Truth_Answerable: True

- SBFL   ranked 1324 statement(s)
- Hybrid ranked 373 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | StrBuilder.java:1184 | 0.408248 | `int len = (str == null ? 0 : str.length());` |
| 1 | 13 | StrBuilder.java:1185 | 0.408248 | `if (len > 0) {` |
| 1 | 13 | StrBuilder.java:1186 | 0.408248 | `int index = indexOf(str, 0);` |
| 1 | 13 | StrBuilder.java:1187 | 0.408248 | `while (index >= 0) {` |
| 1 | 13 | StrBuilder.java:1188 | 0.408248 | `deleteImpl(index, index + len, len);` |
| 1 | 13 | StrBuilder.java:1189 | 0.408248 | `index = indexOf(str, index);` |
| 1 | 13 | StrBuilder.java:1202 | 0.408248 | `int len = (str == null ? 0 : str.length());` |
| 1 | 13 | StrBuilder.java:1203 | 0.408248 | `if (len > 0) {` |
| 1 | 13 | StrBuilder.java:1204 | 0.408248 | `int index = indexOf(str, 0);` |
| 1 | 13 | StrBuilder.java:1205 | 0.408248 | `if (index >= 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | StrBuilder.java:1203 | 0.316228 | `if (len > 0) {` |
| 1 | 4 | StrBuilder.java:1204 | 0.316228 | `int index = indexOf(str, 0);` |
| 1 | 4 | StrBuilder.java:1205 | 0.316228 | `if (index >= 0) {` |
| 1 | 4 | StrBuilder.java:1206 | 0.316228 | `deleteImpl(index, index + len, len);` |
| 5 | 1 | StrBuilder.java:1202 | 0.288675 | `int len = (str == null ? 0 : str.length());` |
| 6 | 1 | StrBuilder.java:1747 | 0.213201 | `return indexOf(str, 0);` |
| 7 | 5 | StrBuilder.java:1775 | 0.182574 | `char[] thisBuf = buffer;` |
| 7 | 5 | StrBuilder.java:1778 | 0.182574 | `for (int i = startIndex; i < len; i++) {` |
| 7 | 5 | StrBuilder.java:1779 | 0.182574 | `for (int j = 0; j < strLen; j++) {` |
| 7 | 5 | StrBuilder.java:1780 | 0.182574 | `if (str.charAt(j) != thisBuf[i + j]) {` |

