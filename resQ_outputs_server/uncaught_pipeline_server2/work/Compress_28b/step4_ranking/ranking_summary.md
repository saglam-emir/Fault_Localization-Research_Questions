# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveInputStream.java', 583), ('TarArchiveInputStream.java', 586), ('TarArchiveInputStream.java', 588)]

Ground_Truth_Answerable: True

- SBFL   ranked 6440 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | TarArchiveInputStream.java:227 | 0.5 | `return null;` |
| 1 | 2 | TarArchiveInputStream.java:586 | 0.5 | `hasHitEOF = true;` |
| 3 | 13 | TarArchiveEntry.java:985 | 0.138675 | `offset += ATIMELEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:986 | 0.138675 | `offset += CTIMELEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:987 | 0.138675 | `offset += OFFSETLEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:988 | 0.138675 | `offset += LONGNAMESLEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:989 | 0.138675 | `offset += PAD2LEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:990 | 0.138675 | `offset += SPARSELEN_GNU;` |
| 3 | 13 | TarArchiveEntry.java:991 | 0.138675 | `isExtended = TarUtils.parseBoolean(header, offset);` |
| 3 | 13 | TarArchiveEntry.java:992 | 0.138675 | `offset += ISEXTENDEDLEN_GNU;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

