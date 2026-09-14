# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationGreaterThan.java', 19), ('CoreOperationGreaterThan.java', 20), ('CoreOperationGreaterThan.java', 33), ('CoreOperationGreaterThan.java', 34), ('CoreOperationGreaterThan.java', 35), ('CoreOperationGreaterThan.java', 36), ('CoreOperationGreaterThanOrEqual.java', 19), ('CoreOperationGreaterThanOrEqual.java', 20), ('CoreOperationGreaterThanOrEqual.java', 34), ('CoreOperationGreaterThanOrEqual.java', 35), ('CoreOperationGreaterThanOrEqual.java', 36), ('CoreOperationGreaterThanOrEqual.java', 37), ('CoreOperationLessThan.java', 19), ('CoreOperationLessThan.java', 20), ('CoreOperationLessThan.java', 33), ('CoreOperationLessThan.java', 34), ('CoreOperationLessThan.java', 35), ('CoreOperationLessThan.java', 36), ('CoreOperationLessThanOrEqual.java', 19), ('CoreOperationLessThanOrEqual.java', 20), ('CoreOperationLessThanOrEqual.java', 34), ('CoreOperationLessThanOrEqual.java', 35), ('CoreOperationLessThanOrEqual.java', 36), ('CoreOperationLessThanOrEqual.java', 37), ('CoreOperationRelationalExpression.java', 19), ('CoreOperationRelationalExpression.java', 20), ('CoreOperationRelationalExpression.java', 33), ('CoreOperationRelationalExpression.java', 42), ('CoreOperationRelationalExpression.java', 43), ('CoreOperationRelationalExpression.java', 44), ('CoreOperationRelationalExpression.java', 45), ('CoreOperationRelationalExpression.java', 46), ('CoreOperationRelationalExpression.java', 47), ('CoreOperationRelationalExpression.java', 48)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 19), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 20), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 33), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 42), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 43), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 44), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 45), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 46), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 47), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 48)]

- SBFL   ranked 4006 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | BasicTypeConverter.java:59 | 1.0 | `return true;` |
| 1 | 14 | BasicTypeConverter.java:173 | 1.0 | `return object;` |
| 1 | 14 | CollectionPointer.java:48 | 1.0 | `super(parent);` |
| 1 | 14 | CollectionPointer.java:49 | 1.0 | `this.collection = collection;` |
| 1 | 14 | CollectionPointer.java:78 | 1.0 | `return index == WHOLE_COLLECTION ? ValueUtils.getValue(collection)` |
| 1 | 14 | CollectionPointer.java:97 | 1.0 | `if (valuePointer == null) {` |
| 1 | 14 | CollectionPointer.java:98 | 1.0 | `if (index == WHOLE_COLLECTION) {` |
| 1 | 14 | CollectionPointer.java:99 | 1.0 | `valuePointer = this;` |
| 1 | 14 | CollectionPointer.java:107 | 1.0 | `return valuePointer;` |
| 1 | 14 | InfoSetUtil.java:62 | 1.0 | `return String.valueOf(object);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

