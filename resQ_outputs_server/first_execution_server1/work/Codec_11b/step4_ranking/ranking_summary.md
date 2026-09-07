# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('QuotedPrintableCodec.java', 70), ('QuotedPrintableCodec.java', 71), ('QuotedPrintableCodec.java', 73), ('QuotedPrintableCodec.java', 114), ('QuotedPrintableCodec.java', 120), ('QuotedPrintableCodec.java', 132), ('QuotedPrintableCodec.java', 144), ('QuotedPrintableCodec.java', 152), ('QuotedPrintableCodec.java', 178), ('QuotedPrintableCodec.java', 179), ('QuotedPrintableCodec.java', 180), ('QuotedPrintableCodec.java', 181), ('QuotedPrintableCodec.java', 182), ('QuotedPrintableCodec.java', 183), ('QuotedPrintableCodec.java', 184), ('QuotedPrintableCodec.java', 189), ('QuotedPrintableCodec.java', 175), ('QuotedPrintableCodec.java', 177), ('QuotedPrintableCodec.java', 187), ('QuotedPrintableCodec.java', 195), ('QuotedPrintableCodec.java', 199), ('QuotedPrintableCodec.java', 200), ('QuotedPrintableCodec.java', 229), ('QuotedPrintableCodec.java', 235)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('QuotedPrintableCodec.java', 187, '->', 183)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 70), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 71), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 73), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 120), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 132), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 144), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 152), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 175), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 177), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 195), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 199), ('src/main/java/org/apache/commons/codec/net/QuotedPrintableCodec.java', 200)]

- SBFL   ranked 210 statement(s)
- Hybrid ranked 4 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | QuotedPrintableCodec.java:405 | 0.57735 | `return this.charset;` |
| 2 | 1 | QuotedPrintableCodec.java:91 | 0.527046 | `this(CharEncoding.UTF_8);` |
| 3 | 1 | Utils.java:44 | 0.516398 | `throw new DecoderException("Invalid URL encoding: not a valid digit (radix " + URLCodec.RADIX + "): " + b);` |
| 4 | 2 | QuotedPrintableCodec.java:101 | 0.5 | `super();` |
| 4 | 2 | QuotedPrintableCodec.java:102 | 0.5 | `this.charset = charset;` |
| 6 | 1 | QuotedPrintableCodec.java:300 | 0.424264 | `return encode(pString, getDefaultCharset());` |
| 7 | 7 | QuotedPrintableCodec.java:62 | 0.422577 | `private static final BitSet PRINTABLE_CHARS = new BitSet(256);` |
| 7 | 7 | QuotedPrintableCodec.java:77 | 0.422577 | `for (int i = 33; i <= 60; i++) {` |
| 7 | 7 | QuotedPrintableCodec.java:78 | 0.422577 | `PRINTABLE_CHARS.set(i);` |
| 7 | 7 | QuotedPrintableCodec.java:80 | 0.422577 | `for (int i = 62; i <= 126; i++) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | QuotedPrintableCodec.java:296 | 0.774597 | `if (pString == null) {` |
| 2 | 3 | QuotedPrintableCodec.java:91 | 0.745356 | `this(CharEncoding.UTF_8);` |
| 2 | 3 | QuotedPrintableCodec.java:101 | 0.745356 | `super();` |
| 2 | 3 | QuotedPrintableCodec.java:102 | 0.745356 | `this.charset = charset;` |

