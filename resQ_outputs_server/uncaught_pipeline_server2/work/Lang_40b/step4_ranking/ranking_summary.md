# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 1048)]

Ground_Truth_Answerable: True

- SBFL   ranked 4091 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | StringUtils.java:1045 | 0.25 | `if (str == null || searchStr == null) {` |
| 1 | 2 | StringUtils.java:1048 | 0.25 | `return contains(str.toUpperCase(), searchStr.toUpperCase());` |
| 3 | 1 | StringUtils.java:1018 | 0.204124 | `return str.indexOf(searchStr) >= 0;` |
| 4 | 1 | StringUtils.java:1015 | 0.176777 | `if (str == null || searchStr == null) {` |
| 5 | 4087 | AggregateTranslator.java:36 | 0.0 | `public AggregateTranslator(CharSequenceTranslator... translators) {` |
| 5 | 4087 | AggregateTranslator.java:37 | 0.0 | `this.translators = translators;` |
| 5 | 4087 | AggregateTranslator.java:47 | 0.0 | `for (CharSequenceTranslator translator : translators) {` |
| 5 | 4087 | AggregateTranslator.java:48 | 0.0 | `int consumed = translator.translate(input, index, out);` |
| 5 | 4087 | AggregateTranslator.java:49 | 0.0 | `if(consumed != 0) {` |
| 5 | 4087 | AggregateTranslator.java:50 | 0.0 | `return consumed;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

