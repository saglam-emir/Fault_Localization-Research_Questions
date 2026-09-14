# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Frequency.java', 303)]

Ground_Truth_Answerable: True

- SBFL   ranked 102 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Frequency.java:303 | 1.0 | `return getCumPct((Comparable<?>) v);` |
| 1 | 2 | Frequency.java:342 | 1.0 | `return getPct(Long.valueOf(v));` |
| 3 | 1 | Frequency.java:331 | 0.707107 | `return getPct(Long.valueOf(v));` |
| 4 | 2 | Frequency.java:386 | 0.57735 | `return getCumFreq(((Integer) v).longValue());` |
| 4 | 2 | Frequency.java:444 | 0.57735 | `return getCumFreq(Long.valueOf(v));` |
| 6 | 3 | Frequency.java:177 | 0.5 | `addValue(Long.valueOf(v));` |
| 6 | 3 | Frequency.java:320 | 0.5 | `return (double) getCount(v) / (double) sumFreq;` |
| 6 | 3 | Frequency.java:408 | 0.5 | `return getSumFreq();    // v is comparable, but greater than the last value` |
| 9 | 18 | Frequency.java:142 | 0.447214 | `freqTable.put(obj, Long.valueOf(count.longValue() + 1));` |
| 9 | 18 | Frequency.java:218 | 0.447214 | `result += iterator.next().longValue();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

