# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DoubleMetaphone.java', 455)]

Ground_Truth_Answerable: True

- SBFL   ranked 446 statement(s)
- Hybrid ranked 3 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DoubleMetaphone.java:604 | 0.707107 | `result.appendAlternate('R');` |
| 2 | 11 | DoubleMetaphone.java:130 | 0.5 | `index = handleH(value, result, index);` |
| 2 | 11 | DoubleMetaphone.java:131 | 0.5 | `break;` |
| 2 | 11 | DoubleMetaphone.java:452 | 0.5 | `if ((contains(value, 0 ,4, "VAN ", "VON ") || contains(value, 0, 3, "SCH")) || contains(value, index + 1, 2, "ET")) {` |
| 2 | 11 | DoubleMetaphone.java:455 | 0.5 | `} else if (contains(value, index + 1, 4, "IER")) {` |
| 2 | 11 | DoubleMetaphone.java:458 | 0.5 | `result.append('J', 'K');` |
| 2 | 11 | DoubleMetaphone.java:460 | 0.5 | `index += 2;` |
| 2 | 11 | DoubleMetaphone.java:462 | 0.5 | `index += 2;` |
| 2 | 11 | DoubleMetaphone.java:463 | 0.5 | `result.append('K');` |
| 2 | 11 | DoubleMetaphone.java:512 | 0.5 | `if ((index == 0 || isVowel(charAt(value, index - 1))) &&` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | DoubleMetaphone.java:87 | 1.0 | `value = cleanInput(value);` |
| 1 | 3 | DoubleMetaphone.java:921 | 1.0 | `if (input == null) {` |
| 1 | 3 | DoubleMetaphone.java:924 | 1.0 | `input = input.trim();` |

