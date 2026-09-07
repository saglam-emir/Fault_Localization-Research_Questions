# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 10), ('DataUtil.java', 19), ('DataUtil.java', 87), ('DataUtil.java', 92), ('DataUtil.java', 161), ('DataUtil.java', 164), ('DataUtil.java', 165)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DataUtil.java', 87, '->', 85), ('DataUtil.java', 92, '->', 91), ('DataUtil.java', 164, '->', 159), ('DataUtil.java', 165, '->', 159)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/helper/DataUtil.java', 10)]

- SBFL   ranked 2281 statement(s)
- Hybrid ranked 7 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DataUtil.java:157 | 0.632456 | `if (contentType == null) return null;` |
| 1 | 5 | DataUtil.java:158 | 0.632456 | `Matcher m = charsetPattern.matcher(contentType);` |
| 1 | 5 | DataUtil.java:159 | 0.632456 | `if (m.find()) {` |
| 1 | 5 | DataUtil.java:160 | 0.632456 | `String charset = m.group(1).trim();` |
| 1 | 5 | DataUtil.java:161 | 0.632456 | `if (Charset.isSupported(charset)) return charset;` |
| 6 | 1 | DataUtil.java:19 | 0.542326 | `private static final Pattern charsetPattern = Pattern.compile("(?i)\\bcharset=\\s*\"?([^\\s;\"]*)");` |
| 7 | 5 | DataUtil.java:54 | 0.447214 | `ByteBuffer byteData = readToByteBuffer(in);` |
| 7 | 5 | DataUtil.java:55 | 0.447214 | `return parseByteData(byteData, charsetName, baseUri, Parser.htmlParser());` |
| 7 | 5 | Jsoup.java:118 | 0.447214 | `return DataUtil.load(in, charsetName, baseUri);` |
| 7 | 5 | TokeniserState.java:876 | 0.447214 | `t.error(this);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | DataUtil.java:19 | 0.0 | `private static final Pattern charsetPattern = Pattern.compile("(?i)\\bcharset=\\s*\"?([^\\s;\"]*)");` |
| 1 | 7 | DataUtil.java:157 | 0.0 | `if (contentType == null) return null;` |
| 1 | 7 | DataUtil.java:158 | 0.0 | `Matcher m = charsetPattern.matcher(contentType);` |
| 1 | 7 | DataUtil.java:159 | 0.0 | `if (m.find()) {` |
| 1 | 7 | DataUtil.java:160 | 0.0 | `String charset = m.group(1).trim();` |
| 1 | 7 | DataUtil.java:161 | 0.0 | `if (Charset.isSupported(charset)) return charset;` |
| 1 | 7 | DataUtil.java:166 | 0.0 | `return null;` |

