# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TreeBuilder.java', 61), ('TreeBuilder.java', 65), ('TreeBuilder.java', 71)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/parser/TreeBuilder.java', 65)]

- SBFL   ranked 3097 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 51 | Document.java:477 | 0.57735 | `prettyPrint = pretty;` |
| 1 | 51 | Document.java:478 | 0.57735 | `return this;` |
| 1 | 51 | Element.java:410 | 0.57735 | `return (Element) super.before(node);` |
| 1 | 51 | Entities.java:97 | 0.57735 | `continue;` |
| 1 | 51 | HtmlTreeBuilder.java:245 | 0.57735 | `insertInFosterParent(node);` |
| 1 | 51 | HtmlTreeBuilder.java:287 | 0.57735 | `return next;` |
| 1 | 51 | HtmlTreeBuilder.java:506 | 0.57735 | `this.fosterInserts = fosterInserts;` |
| 1 | 51 | HtmlTreeBuilder.java:675 | 0.57735 | `Element lastTable = getFromStack("table");` |
| 1 | 51 | HtmlTreeBuilder.java:676 | 0.57735 | `boolean isLastTableParent = false;` |
| 1 | 51 | HtmlTreeBuilder.java:677 | 0.57735 | `if (lastTable != null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

