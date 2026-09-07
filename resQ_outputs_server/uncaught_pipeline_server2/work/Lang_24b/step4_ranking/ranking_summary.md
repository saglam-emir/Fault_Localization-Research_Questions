# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 1413)]

Ground_Truth_Answerable: True

- SBFL   ranked 918 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 65 | NumberUtils.java:457 | 0.333333 | `throw new NumberFormatException("A blank string is not a valid number");` |
| 1 | 65 | NumberUtils.java:464 | 0.333333 | `return null;` |
| 1 | 65 | NumberUtils.java:480 | 0.333333 | `throw new NumberFormatException(str + " is not a valid number.");` |
| 1 | 65 | NumberUtils.java:492 | 0.333333 | `mant = str.substring(0, expPos);` |
| 1 | 65 | NumberUtils.java:521 | 0.333333 | `throw new NumberFormatException(str + " is not a valid number.");` |
| 1 | 65 | NumberUtils.java:532 | 0.333333 | `} catch (NumberFormatException nfe) {` |
| 1 | 65 | NumberUtils.java:543 | 0.333333 | `} catch (NumberFormatException nfe) {` |
| 1 | 65 | NumberUtils.java:548 | 0.333333 | `} catch (NumberFormatException e) {` |
| 1 | 65 | NumberUtils.java:553 | 0.333333 | `throw new NumberFormatException(str + " is not a valid number.");` |
| 1 | 65 | NumberUtils.java:586 | 0.333333 | `} catch (NumberFormatException nfe) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

