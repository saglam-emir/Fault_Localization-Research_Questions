# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('W3CDom.java', 22), ('W3CDom.java', 73), ('W3CDom.java', 85), ('W3CDom.java', 78), ('W3CDom.java', 81), ('W3CDom.java', 116), ('W3CDom.java', 144)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/helper/W3CDom.java', 22), ('src/main/java/org/jsoup/helper/W3CDom.java', 78), ('src/main/java/org/jsoup/helper/W3CDom.java', 116)]

- SBFL   ranked 1921 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 31 | ConstrainableInputStream.java:94 | 1.0 | `remaining -= read;` |
| 1 | 31 | ConstrainableInputStream.java:96 | 1.0 | `outStream.write(readBuffer, 0, read);` |
| 1 | 31 | HtmlTreeBuilderState.java:20 | 1.0 | `return true; // ignore whitespace` |
| 1 | 31 | HtmlTreeBuilderState.java:22 | 1.0 | `tb.insert(t.asComment());` |
| 1 | 31 | HtmlTreeBuilderState.java:74 | 1.0 | `return true;` |
| 1 | 31 | HtmlTreeBuilderState.java:102 | 1.0 | `tb.insert(t.asCharacter());` |
| 1 | 31 | HtmlTreeBuilderState.java:103 | 1.0 | `return true;` |
| 1 | 31 | HtmlTreeBuilderState.java:203 | 1.0 | `tb.insert(t.asCharacter());` |
| 1 | 31 | HtmlTreeBuilderState.java:549 | 1.0 | `tb.reconstructFormattingElements();` |
| 1 | 31 | HtmlTreeBuilderState.java:551 | 1.0 | `tb.insert(startTag);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

