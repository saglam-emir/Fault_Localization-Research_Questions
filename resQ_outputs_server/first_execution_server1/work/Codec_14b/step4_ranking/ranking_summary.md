# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Lang.java', 98), ('Lang.java', 102), ('PhoneticEngine.java', 31), ('PhoneticEngine.java', 338), ('PhoneticEngine.java', 361), ('PhoneticEngine.java', 364), ('Rule.java', 158), ('ash_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0), ('gen_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0), ('sep_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/codec/language/bm/Rule.java', 158), ('src/main/resources/org/apache/commons/codec/language/bm/ash_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0), ('src/main/resources/org/apache/commons/codec/language/bm/gen_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0), ('src/main/resources/org/apache/commons/codec/language/bm/sep_lang.txt\t1969-12-31 16:00:00.000000000 -0800', 0)]

- SBFL   ranked 421 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Rule.java:602 | 0.316228 | `return true;` |
| 2 | 2 | Rule.java:513 | 0.223607 | `return input.equals(content);` |
| 2 | 2 | Rule.java:595 | 0.223607 | `return false;` |
| 4 | 10 | PhoneticEngine.java:400 | 0.204124 | `if (input.length() >= 2 && input.substring(0, 2).equals("d'")) { // check for d'` |
| 4 | 10 | PhoneticEngine.java:405 | 0.204124 | `for (final String l : NAME_PREFIXES.get(this.nameType)) {` |
| 4 | 10 | PhoneticEngine.java:407 | 0.204124 | `if (input.startsWith(l + " ")) {` |
| 4 | 10 | PhoneticEngine.java:434 | 0.204124 | `words2.addAll(words);` |
| 4 | 10 | PhoneticEngine.java:435 | 0.204124 | `break;` |
| 4 | 10 | Rule.java:235 | 0.204124 | `return true;` |
| 4 | 10 | Rule.java:557 | 0.204124 | `return input.length() == 1 && contains(bContent, input.charAt(0)) == shouldMatch;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

