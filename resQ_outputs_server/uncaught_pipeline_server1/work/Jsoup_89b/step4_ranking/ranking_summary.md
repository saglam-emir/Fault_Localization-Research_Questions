# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Attribute.java', 88), ('Attribute.java', 90)]

Ground_Truth_Answerable: True

- SBFL   ranked 4331 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | ConstrainableInputStream.java:67 | 0.447214 | `} catch (SocketTimeoutException e) {` |
| 1 | 11 | ConstrainableInputStream.java:68 | 0.447214 | `return 0;` |
| 1 | 11 | HttpConnection.java:840 | 0.447214 | `Validate.isTrue(executed, "Request must be executed (with .execute(), .get(), or .post() before getting response body");` |
| 1 | 11 | HttpConnection.java:841 | 0.447214 | `if (byteData == null) {` |
| 1 | 11 | HttpConnection.java:842 | 0.447214 | `Validate.isFalse(inputStreamRead, "Request has already been read (with .parse())");` |
| 1 | 11 | HttpConnection.java:844 | 0.447214 | `byteData = DataUtil.readToByteBuffer(bodyStream, req.maxBodySize());` |
| 1 | 11 | HttpConnection.java:845 | 0.447214 | `} catch (IOException e) {` |
| 1 | 11 | HttpConnection.java:846 | 0.447214 | `throw new UncheckedIOException(e);` |
| 1 | 11 | HttpConnection.java:848 | 0.447214 | `inputStreamRead = true;` |
| 1 | 11 | HttpConnection.java:849 | 0.447214 | `safeClose();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

