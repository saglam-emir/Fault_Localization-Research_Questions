# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 70), ('DoubleMetaphone.java', 22), ('DoubleMetaphone.java', 244)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/codec/binary/StringUtils.java', 70), ('src/main/java/org/apache/commons/codec/language/DoubleMetaphone.java', 22)]

- SBFL   ranked 1333 statement(s)
- Hybrid ranked 111 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DoubleMetaphone.java:88 | 0.258199 | `return null;` |
| 1 | 2 | DoubleMetaphone.java:893 | 0.258199 | `return null;` |
| 3 | 1 | DoubleMetaphone.java:244 | 0.158114 | `return doubleMetaphone(value1, alternate).equals(doubleMetaphone(value2, alternate));` |
| 4 | 5 | DoubleMetaphone.java:86 | 0.119523 | `value = cleanInput(value);` |
| 4 | 5 | DoubleMetaphone.java:87 | 0.119523 | `if (value == null) {` |
| 4 | 5 | DoubleMetaphone.java:888 | 0.119523 | `if (input == null) {` |
| 4 | 5 | DoubleMetaphone.java:891 | 0.119523 | `input = input.trim();` |
| 4 | 5 | DoubleMetaphone.java:892 | 0.119523 | `if (input.length() == 0) {` |
| 9 | 6 | DoubleMetaphone.java:47 | 0.111803 | `private static final String[] SILENT_START =` |
| 9 | 6 | DoubleMetaphone.java:49 | 0.111803 | `private static final String[] L_R_N_M_B_H_F_V_W_SPACE =` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DoubleMetaphone.java:59 | 0.707107 | `private int maxCodeLen = 4;` |
| 1 | 2 | DoubleMetaphone.java:65 | 0.707107 | `super();` |
| 3 | 109 | Base32.java:67 | 0.0 | `private static final byte[] DECODE_TABLE = {` |
| 3 | 109 | Base32.java:81 | 0.0 | `private static final byte[] ENCODE_TABLE = {` |
| 3 | 109 | Base32.java:181 | 0.0 | `this(0, null, useHex, PAD_DEFAULT);` |
| 3 | 109 | Base32.java:281 | 0.0 | `super(BYTES_PER_UNENCODED_BLOCK, BYTES_PER_ENCODED_BLOCK, lineLength,` |
| 3 | 109 | Base32.java:283 | 0.0 | `if (useHex) {` |
| 3 | 109 | Base32.java:287 | 0.0 | `this.encodeTable = ENCODE_TABLE;` |
| 3 | 109 | Base32.java:288 | 0.0 | `this.decodeTable = DECODE_TABLE;` |
| 3 | 109 | Base32.java:290 | 0.0 | `if (lineLength > 0) {` |

