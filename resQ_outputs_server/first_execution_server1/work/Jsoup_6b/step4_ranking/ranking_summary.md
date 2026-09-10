# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Entities.java', 70), ('Entities.java', 72)]

Ground_Truth_Answerable: True

- SBFL   ranked 1072 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Parser.java:191 | 0.707107 | `value = tq.chompTo(SQ);` |
| 1 | 2 | Parser.java:301 | 0.707107 | `break;` |
| 3 | 4 | Parser.java:195 | 0.5 | `StringBuilder valueAccum = new StringBuilder();` |
| 3 | 4 | Parser.java:197 | 0.5 | `while (!tq.matchesAny("<", "/>", ">") && !tq.matchesWhitespace() && !tq.isEmpty()) {` |
| 3 | 4 | Parser.java:198 | 0.5 | `valueAccum.append(tq.consume());` |
| 3 | 4 | Parser.java:200 | 0.5 | `value = valueAccum.toString();` |
| 7 | 7 | Entities.java:58 | 0.447214 | `int base = m.group(2) != null ? 16 : 10; // 2 is hex indicator` |
| 7 | 7 | Entities.java:59 | 0.447214 | `charval = Integer.valueOf(num, base);` |
| 7 | 7 | Entities.java:61 | 0.447214 | `} // skip` |
| 7 | 7 | Parser.java:150 | 0.447214 | `isEmptyElement = true;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

