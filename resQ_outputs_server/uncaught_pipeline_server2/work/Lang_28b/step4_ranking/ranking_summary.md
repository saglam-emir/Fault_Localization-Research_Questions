# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumericEntityUnescaper.java', 63), ('NumericEntityUnescaper.java', 64)]

Ground_Truth_Answerable: True

- SBFL   ranked 251 statement(s)
- Hybrid ranked 62 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | NumericEntityUnescaper.java:57 | 0.57735 | `entityValue = Integer.parseInt(input.subSequence(start, end).toString(), 10);` |
| 1 | 3 | NumericEntityUnescaper.java:63 | 0.57735 | `out.write(entityValue);` |
| 1 | 3 | NumericEntityUnescaper.java:64 | 0.57735 | `return 2 + (end - start) + (isHex ? 1 : 0) + 1;` |
| 4 | 8 | NumericEntityUnescaper.java:38 | 0.5 | `int start = index + 2;` |
| 4 | 8 | NumericEntityUnescaper.java:39 | 0.5 | `boolean isHex = false;` |
| 4 | 8 | NumericEntityUnescaper.java:41 | 0.5 | `char firstChar = input.charAt(start);` |
| 4 | 8 | NumericEntityUnescaper.java:42 | 0.5 | `if(firstChar == 'x' || firstChar == 'X') {` |
| 4 | 8 | NumericEntityUnescaper.java:47 | 0.5 | `int end = start;` |
| 4 | 8 | NumericEntityUnescaper.java:48 | 0.5 | `while(input.charAt(end) != ';') {` |
| 4 | 8 | NumericEntityUnescaper.java:49 | 0.5 | `end++;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | NumericEntityUnescaper.java:38 | 1.0 | `int start = index + 2;` |
| 1 | 9 | NumericEntityUnescaper.java:39 | 1.0 | `boolean isHex = false;` |
| 1 | 9 | NumericEntityUnescaper.java:41 | 1.0 | `char firstChar = input.charAt(start);` |
| 1 | 9 | NumericEntityUnescaper.java:47 | 1.0 | `int end = start;` |
| 1 | 9 | NumericEntityUnescaper.java:48 | 1.0 | `while(input.charAt(end) != ';') {` |
| 1 | 9 | NumericEntityUnescaper.java:49 | 1.0 | `end++;` |
| 1 | 9 | NumericEntityUnescaper.java:54 | 1.0 | `if(isHex) {` |
| 1 | 9 | NumericEntityUnescaper.java:57 | 1.0 | `entityValue = Integer.parseInt(input.subSequence(start, end).toString(), 10);` |
| 1 | 9 | NumericEntityUnescaper.java:63 | 1.0 | `out.write(entityValue);` |
| 10 | 1 | NumericEntityUnescaper.java:37 | 0.707107 | `if(input.charAt(index) == '&' && input.charAt(index + 1) == '#') {` |

