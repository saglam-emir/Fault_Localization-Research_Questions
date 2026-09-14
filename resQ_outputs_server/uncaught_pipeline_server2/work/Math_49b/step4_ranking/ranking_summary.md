# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('OpenMapRealVector.java', 345), ('OpenMapRealVector.java', 358), ('OpenMapRealVector.java', 370), ('OpenMapRealVector.java', 383)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/linear/OpenMapRealVector.java', 358), ('src/main/java/org/apache/commons/math/linear/OpenMapRealVector.java', 383)]

- SBFL   ranked 2292 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | LocalizedFormats.java:367 | 1.0 | `ResourceBundle bundle =` |
| 1 | 11 | LocalizedFormats.java:374 | 1.0 | `} catch (MissingResourceException mre) {` |
| 1 | 11 | LocalizedFormats.java:380 | 1.0 | `return sourceFormat;` |
| 1 | 11 | MathRuntimeException.java:40 | 1.0 | `public class MathRuntimeException extends RuntimeException implements MathThrowable {` |
| 1 | 11 | MathRuntimeException.java:132 | 1.0 | `return new MessageFormat(pattern.getLocalizedString(locale), locale).format(arguments);` |
| 1 | 11 | MathRuntimeException.java:373 | 1.0 | `return new ConcurrentModificationException() {` |
| 1 | 11 | MathRuntimeException.java:381 | 1.0 | `return buildMessage(Locale.US, pattern, arguments);` |
| 1 | 11 | MathRuntimeException.java:387 | 1.0 | `return buildMessage(Locale.getDefault(), pattern, arguments);` |
| 1 | 11 | OpenIntToDoubleHashMap.java:216 | 1.0 | `if (states[index] == FREE) {` |
| 1 | 11 | OpenIntToDoubleHashMap.java:217 | 1.0 | `return false;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

