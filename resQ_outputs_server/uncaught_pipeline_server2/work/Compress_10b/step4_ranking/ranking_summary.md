# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipFile.java', 808), ('ZipFile.java', 809), ('ZipFile.java', 842)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ZipFile.java', 842, '->', 808)]

Ground_Truth_Answerable: True

- SBFL   ranked 1277 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | ZipFile.java:321 | 1.0 | `return null;` |
| 1 | 4 | ZipFile.java:885 | 1.0 | `synchronized (archive) {` |
| 1 | 4 | ZipFile.java:886 | 1.0 | `archive.seek(loc++);` |
| 1 | 4 | ZipFile.java:887 | 1.0 | `return archive.read();` |
| 5 | 11 | ZipFile.java:324 | 0.707107 | `long start = offsetEntry.dataOffset;` |
| 5 | 11 | ZipFile.java:325 | 0.707107 | `BoundedInputStream bis =` |
| 5 | 11 | ZipFile.java:327 | 0.707107 | `switch (ze.getMethod()) {` |
| 5 | 11 | ZipFile.java:329 | 0.707107 | `return bis;` |
| 5 | 11 | ZipFile.java:838 | 0.707107 | `nameMap.remove(orig);` |
| 5 | 11 | ZipFile.java:839 | 0.707107 | `nameMap.put(ze.getName(), ze);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

