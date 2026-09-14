# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultPrettyPrinter.java', 255)]

Ground_Truth_Answerable: True

- SBFL   ranked 11067 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DefaultPrettyPrinter.java:255 | 0.316228 | `return new DefaultPrettyPrinter(this);` |
| 2 | 2 | ByteSourceJsonBootstrapper.java:151 | 0.243432 | `int i16 = ((_inputBuffer[_inputPtr] & 0xFF) << 8)` |
| 2 | 2 | ByteSourceJsonBootstrapper.java:153 | 0.243432 | `if (checkUTF16(i16)) {` |
| 4 | 1 | ByteSourceJsonBootstrapper.java:525 | 0.239046 | `return false;` |
| 5 | 116 | ByteQuadsCanonicalizer.java:222 | 0.134595 | `private ByteQuadsCanonicalizer(int sz, boolean intern, int seed, boolean failOnDoS) {` |
| 5 | 116 | ByteQuadsCanonicalizer.java:223 | 0.134595 | `_parent = null;` |
| 5 | 116 | ByteQuadsCanonicalizer.java:224 | 0.134595 | `_seed = seed;` |
| 5 | 116 | ByteQuadsCanonicalizer.java:225 | 0.134595 | `_intern = intern;` |
| 5 | 116 | ByteQuadsCanonicalizer.java:226 | 0.134595 | `_failOnDoS = failOnDoS;` |
| 5 | 116 | ByteQuadsCanonicalizer.java:228 | 0.134595 | `if (sz < MIN_HASH_SIZE) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

