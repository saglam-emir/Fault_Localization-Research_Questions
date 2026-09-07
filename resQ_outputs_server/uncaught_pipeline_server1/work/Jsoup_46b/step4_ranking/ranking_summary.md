# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Entities.java', 118)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Entities.java', 118, '->', 117)]

Ground_Truth_Answerable: True

- SBFL   ranked 3115 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Document.java:402 | 0.57735 | `this.escapeMode = escapeMode;` |
| 1 | 5 | Document.java:403 | 0.57735 | `return this;` |
| 1 | 5 | Entities.java:115 | 0.57735 | `if (escapeMode != EscapeMode.xhtml)` |
| 1 | 5 | Entities.java:118 | 0.57735 | `accum.append(c);` |
| 1 | 5 | Entities.java:119 | 0.57735 | `break;` |
| 6 | 3 | DataUtil.java:53 | 0.408248 | `ByteBuffer byteData = readToByteBuffer(in);` |
| 6 | 3 | DataUtil.java:54 | 0.408248 | `return parseByteData(byteData, charsetName, baseUri, Parser.htmlParser());` |
| 6 | 3 | Jsoup.java:118 | 0.408248 | `return DataUtil.load(in, charsetName, baseUri);` |
| 9 | 11 | DataUtil.java:146 | 0.333333 | `Validate.isTrue(maxSize >= 0, "maxSize must be 0 (unlimited) or larger");` |
| 9 | 11 | DataUtil.java:147 | 0.333333 | `final boolean capped = maxSize > 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

