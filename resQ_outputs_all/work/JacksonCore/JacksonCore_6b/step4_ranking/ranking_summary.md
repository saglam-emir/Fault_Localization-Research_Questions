# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonPointer.java', 193), ('JsonPointer.java', 194)]

Ground_Truth_Answerable: True

- SBFL   ranked 76 statement(s)
- Hybrid ranked 47 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | JsonPointer.java:205 | 0.707107 | `return NumberInput.parseInt(str);` |
| 1 | 15 | NumberInput.java:68 | 0.707107 | `char c = s.charAt(0);` |
| 1 | 15 | NumberInput.java:69 | 0.707107 | `int len = s.length();` |
| 1 | 15 | NumberInput.java:70 | 0.707107 | `boolean neg = (c == '-');` |
| 1 | 15 | NumberInput.java:71 | 0.707107 | `int offset = 1;` |
| 1 | 15 | NumberInput.java:74 | 0.707107 | `if (neg) {` |
| 1 | 15 | NumberInput.java:80 | 0.707107 | `if (len > 9) {` |
| 1 | 15 | NumberInput.java:84 | 0.707107 | `if (c > '9' || c < '0') {` |
| 1 | 15 | NumberInput.java:87 | 0.707107 | `int num = c - '0';` |
| 1 | 15 | NumberInput.java:88 | 0.707107 | `if (offset < len) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | NumberInput.java:69 | 1.0 | `int len = s.length();` |
| 1 | 4 | NumberInput.java:89 | 1.0 | `c = s.charAt(offset++);` |
| 1 | 4 | NumberInput.java:93 | 1.0 | `num = (num * 10) + (c - '0');` |
| 1 | 4 | NumberInput.java:94 | 1.0 | `if (offset < len) {` |
| 5 | 4 | NumberInput.java:68 | 0.707107 | `char c = s.charAt(0);` |
| 5 | 4 | NumberInput.java:70 | 0.707107 | `boolean neg = (c == '-');` |
| 5 | 4 | NumberInput.java:87 | 0.707107 | `int num = c - '0';` |
| 5 | 4 | NumberInput.java:112 | 0.707107 | `return neg ? -num : num;` |
| 9 | 5 | JsonPointer.java:186 | 0.408248 | `final int len = str.length();` |
| 9 | 5 | JsonPointer.java:193 | 0.408248 | `for (int i = 0; i < len; ++i) {` |

