# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StrBuilder.java', 884)]

Ground_Truth_Answerable: True

- SBFL   ranked 1324 statement(s)
- Hybrid ranked 373 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | StrBuilder.java:879 | 0.408248 | `if (width > 0) {` |
| 1 | 6 | StrBuilder.java:880 | 0.408248 | `ensureCapacity(size + width);` |
| 1 | 6 | StrBuilder.java:881 | 0.408248 | `String str = (obj == null ? getNullText() : obj.toString());` |
| 1 | 6 | StrBuilder.java:882 | 0.408248 | `int strLen = str.length();` |
| 1 | 6 | StrBuilder.java:883 | 0.408248 | `if (strLen >= width) {` |
| 1 | 6 | StrBuilder.java:884 | 0.408248 | `str.getChars(0, strLen, buffer, size);` |
| 7 | 3 | StrBuilder.java:107 | 0.062994 | `super();` |
| 7 | 3 | StrBuilder.java:108 | 0.062994 | `if (initialCapacity <= 0) {` |
| 7 | 3 | StrBuilder.java:111 | 0.062994 | `buffer = new char[initialCapacity];` |
| 10 | 2 | StrBuilder.java:228 | 0.05376 | `if (capacity > buffer.length) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StrBuilder.java:107 | 0.09245 | `super();` |
| 2 | 1 | StrBuilder.java:111 | 0.061546 | `buffer = new char[initialCapacity];` |
| 3 | 371 | ArrayUtils.java:123 | 0.0 | `public static final char[] EMPTY_CHAR_ARRAY = new char[0];` |
| 3 | 371 | StrBuilder.java:98 | 0.0 | `this(CAPACITY);` |
| 3 | 371 | StrBuilder.java:121 | 0.0 | `super();` |
| 3 | 371 | StrBuilder.java:122 | 0.0 | `if (str == null) {` |
| 3 | 371 | StrBuilder.java:125 | 0.0 | `buffer = new char[str.length() + CAPACITY];` |
| 3 | 371 | StrBuilder.java:126 | 0.0 | `append(str);` |
| 3 | 371 | StrBuilder.java:137 | 0.0 | `return newLine;` |
| 3 | 371 | StrBuilder.java:147 | 0.0 | `this.newLine = newLine;` |

