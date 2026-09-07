# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UnionContext.java', 20), ('UnionContext.java', 22), ('UnionContext.java', 56), ('UnionContext.java', 65), ('UnionContext.java', 62)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('UnionContext.java', 62, '->', 46)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/axes/UnionContext.java', 20), ('src/java/org/apache/commons/jxpath/ri/axes/UnionContext.java', 22)]

- SBFL   ranked 5653 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5653 | AbstractFactory.java:32 | 0.0 | `public abstract class AbstractFactory {` |
| 1 | 5653 | AttributeContext.java:34 | 0.0 | `private boolean setStarted = false;` |
| 1 | 5653 | AttributeContext.java:43 | 0.0 | `super(parentContext);` |
| 1 | 5653 | AttributeContext.java:44 | 0.0 | `this.nodeTest = nodeTest;` |
| 1 | 5653 | AttributeContext.java:48 | 0.0 | `return currentNodePointer;` |
| 1 | 5653 | AttributeContext.java:52 | 0.0 | `setStarted = false;` |
| 1 | 5653 | AttributeContext.java:53 | 0.0 | `iterator = null;` |
| 1 | 5653 | AttributeContext.java:54 | 0.0 | `super.reset();` |
| 1 | 5653 | AttributeContext.java:71 | 0.0 | `super.setPosition(getCurrentPosition() + 1);` |
| 1 | 5653 | AttributeContext.java:72 | 0.0 | `if (!setStarted) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

