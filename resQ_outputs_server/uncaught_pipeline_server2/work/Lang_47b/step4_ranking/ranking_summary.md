# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StrBuilder.java', 1186), ('StrBuilder.java', 1230)]

Ground_Truth_Answerable: True

- SBFL   ranked 1370 statement(s)
- Hybrid ranked 397 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StrBuilder.java:158 | 0.516398 | `return nullText;` |
| 2 | 4 | StrBuilder.java:1183 | 0.333333 | `if (width > 0) {` |
| 2 | 4 | StrBuilder.java:1184 | 0.333333 | `ensureCapacity(size + width);` |
| 2 | 4 | StrBuilder.java:1185 | 0.333333 | `String str = (obj == null ? getNullText() : obj.toString());` |
| 2 | 4 | StrBuilder.java:1186 | 0.333333 | `int strLen = str.length();` |
| 6 | 4 | StrBuilder.java:1227 | 0.288675 | `if (width > 0) {` |
| 6 | 4 | StrBuilder.java:1228 | 0.288675 | `ensureCapacity(size + width);` |
| 6 | 4 | StrBuilder.java:1229 | 0.288675 | `String str = (obj == null ? getNullText() : obj.toString());` |
| 6 | 4 | StrBuilder.java:1230 | 0.288675 | `int strLen = str.length();` |
| 10 | 1 | StrBuilder.java:98 | 0.096561 | `this(CAPACITY);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StrBuilder.java:107 | 0.122169 | `super();` |
| 2 | 1 | StrBuilder.java:98 | 0.083333 | `this(CAPACITY);` |
| 3 | 1 | StrBuilder.java:111 | 0.083189 | `buffer = new char[initialCapacity];` |
| 4 | 394 | ArrayUtils.java:123 | 0.0 | `public static final char[] EMPTY_CHAR_ARRAY = new char[0];` |
| 4 | 394 | StrBuilder.java:121 | 0.0 | `super();` |
| 4 | 394 | StrBuilder.java:122 | 0.0 | `if (str == null) {` |
| 4 | 394 | StrBuilder.java:125 | 0.0 | `buffer = new char[str.length() + CAPACITY];` |
| 4 | 394 | StrBuilder.java:126 | 0.0 | `append(str);` |
| 4 | 394 | StrBuilder.java:137 | 0.0 | `return newLine;` |
| 4 | 394 | StrBuilder.java:147 | 0.0 | `this.newLine = newLine;` |

