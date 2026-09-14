# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ByteQuadsCanonicalizer.java', 925), ('ByteQuadsCanonicalizer.java', 984)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ByteQuadsCanonicalizer.java', 984, '->', 983)]

Ground_Truth_Answerable: True

- SBFL   ranked 7219 statement(s)
- Hybrid ranked 1015 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ByteQuadsCanonicalizer.java:1109 | 0.707107 | `q[0] = oldHashArea[offset];` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1110 | 0.707107 | `addName(name, q, 1);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1111 | 0.707107 | `break;` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1124 | 0.707107 | `if (len > q.length) {` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1128 | 0.707107 | `int qoff = oldHashArea[offset+1];` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1129 | 0.707107 | `System.arraycopy(oldHashArea, qoff, q, 0, len);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1130 | 0.707107 | `addName(name, q, len);` |
| 8 | 1 | ByteQuadsCanonicalizer.java:373 | 0.67082 | `public int bucketCount() { return _hashSize; }` |
| 9 | 4 | ByteQuadsCanonicalizer.java:914 | 0.632456 | `offset = _spilloverEnd;` |
| 9 | 4 | ByteQuadsCanonicalizer.java:915 | 0.632456 | `_spilloverEnd += 4;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 20 | JsonToken.java:108 | 0.5 | `VALUE_FALSE("false", JsonTokenId.ID_FALSE),` |
| 1 | 20 | JsonToken.java:114 | 0.5 | `VALUE_NULL("null", JsonTokenId.ID_NULL),` |
| 1 | 20 | UTF8StreamJsonParser.java:780 | 0.5 | `_matchToken("null", 1);` |
| 1 | 20 | UTF8StreamJsonParser.java:781 | 0.5 | `t = JsonToken.VALUE_NULL;` |
| 1 | 20 | UTF8StreamJsonParser.java:1796 | 0.5 | `final byte[] input = _inputBuffer;` |
| 1 | 20 | UTF8StreamJsonParser.java:1797 | 0.5 | `final int[] codes = _icLatin1;` |
| 1 | 20 | UTF8StreamJsonParser.java:1810 | 0.5 | `i = input[_inputPtr++] & 0xFF;` |
| 1 | 20 | UTF8StreamJsonParser.java:1811 | 0.5 | `if (codes[i] != 0) {` |
| 1 | 20 | UTF8StreamJsonParser.java:1819 | 0.5 | `i = input[_inputPtr++] & 0xFF;` |
| 1 | 20 | UTF8StreamJsonParser.java:1820 | 0.5 | `if (codes[i] != 0) {` |

