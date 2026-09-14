# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CompressorStreamFactory.java', 240), ('DeflateCompressorInputStream.java', 33), ('DeflateCompressorInputStream.java', 106)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/compressors/CompressorStreamFactory.java', 240), ('src/main/java/org/apache/commons/compress/compressors/deflate/DeflateCompressorInputStream.java', 33), ('src/main/java/org/apache/commons/compress/compressors/deflate/DeflateCompressorInputStream.java', 106)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 1780 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | CompressorException.java:37 | 1.0 | `super(message);` |
| 1 | 23 | CompressorStreamFactory.java:229 | 1.0 | `return new Pack200CompressorInputStream(in);` |
| 1 | 23 | CompressorStreamFactory.java:255 | 1.0 | `throw new CompressorException("No Compressor found for the stream signature.");` |
| 1 | 23 | InMemoryCachingStreamBridge.java:34 | 1.0 | `super(new ByteArrayOutputStream());` |
| 1 | 23 | LZMAUtils.java:78 | 1.0 | `return false;` |
| 1 | 23 | Pack200CompressorInputStream.java:56 | 1.0 | `this(in, Pack200Strategy.IN_MEMORY);` |
| 1 | 23 | Pack200CompressorInputStream.java:69 | 1.0 | `this(in, null, mode, null);` |
| 1 | 23 | Pack200CompressorInputStream.java:139 | 1.0 | `throws IOException {` |
| 1 | 23 | Pack200CompressorInputStream.java:140 | 1.0 | `originalInput = in;` |
| 1 | 23 | Pack200CompressorInputStream.java:141 | 1.0 | `streamBridge = mode.newStreamBridge();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

