# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonReader.java', 731)]

Ground_Truth_Answerable: True

- SBFL   ranked 2904 statement(s)
- Hybrid ranked 495 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonReader.java:673 | 0.147442 | `negative = true;` |
| 1 | 3 | JsonReader.java:674 | 0.147442 | `last = NUMBER_CHAR_SIGN;` |
| 1 | 3 | JsonReader.java:675 | 0.147442 | `continue;` |
| 4 | 1 | JsonReader.java:672 | 0.138675 | `if (last == NUMBER_CHAR_NONE) {` |
| 5 | 1 | JsonReader.java:820 | 0.129099 | `result = Long.toString(peekedLong);` |
| 6 | 1 | JsonReader.java:819 | 0.1 | `} else if (p == PEEKED_LONG) {` |
| 7 | 1 | JsonReader.java:816 | 0.099015 | `} else if (p == PEEKED_BUFFERED) {` |
| 8 | 1 | JsonReader.java:343 | 0.078087 | `p = doPeek();` |
| 9 | 3 | JsonReader.java:732 | 0.061085 | `peekedLong = negative ? value : -value;` |
| 9 | 3 | JsonReader.java:733 | 0.061085 | `pos += i;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | JsonReader.java:819 | 1.0 | `} else if (p == PEEKED_LONG) {` |
| 1 | 2 | JsonReader.java:820 | 1.0 | `result = Long.toString(peekedLong);` |
| 3 | 1 | JsonReader.java:816 | 0.707107 | `} else if (p == PEEKED_BUFFERED) {` |
| 4 | 2 | JsonReader.java:672 | 0.204124 | `if (last == NUMBER_CHAR_NONE) {` |
| 4 | 2 | JsonReader.java:675 | 0.204124 | `continue;` |
| 6 | 1 | JsonReader.java:670 | 0.196116 | `switch (c) {` |
| 7 | 1 | JsonReader.java:733 | 0.19245 | `pos += i;` |
| 8 | 5 | JsonReader.java:649 | 0.188982 | `boolean fitsInLong = true;` |
| 8 | 5 | JsonReader.java:663 | 0.188982 | `break;` |
| 8 | 5 | JsonReader.java:731 | 0.188982 | `if (last == NUMBER_CHAR_DIGIT && fitsInLong && (value != Long.MIN_VALUE || negative)) {` |

