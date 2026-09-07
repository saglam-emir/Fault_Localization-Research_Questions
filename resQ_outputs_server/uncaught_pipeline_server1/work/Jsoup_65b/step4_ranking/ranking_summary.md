# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HtmlTreeBuilder.java', 360), ('HtmlTreeBuilder.java', 364), ('HtmlTreeBuilderState.java', 1036), ('HtmlTreeBuilderState.java', 1096)]

Ground_Truth_Answerable: True

- SBFL   ranked 2656 statement(s)
- Hybrid ranked 304 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | ConstrainableInputStream.java:18 | 0.94054 | `super(in, bufferSize);` |
| 1 | 29 | ConstrainableInputStream.java:19 | 0.94054 | `Validate.isTrue(maxSize >= 0);` |
| 1 | 29 | ConstrainableInputStream.java:20 | 0.94054 | `remaining = maxSize;` |
| 1 | 29 | ConstrainableInputStream.java:21 | 0.94054 | `capped = maxSize != 0;` |
| 1 | 29 | ConstrainableInputStream.java:26 | 0.94054 | `if (Thread.interrupted() || remaining < 0)` |
| 1 | 29 | ConstrainableInputStream.java:29 | 0.94054 | `final int read = super.read(b, off, len);` |
| 1 | 29 | ConstrainableInputStream.java:30 | 0.94054 | `if (capped) {` |
| 1 | 29 | ConstrainableInputStream.java:33 | 0.94054 | `return read;` |
| 1 | 29 | DataUtil.java:94 | 0.94054 | `if (input == null) // empty body` |
| 1 | 29 | DataUtil.java:97 | 0.94054 | `if (!(input instanceof ConstrainableInputStream))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 304 | Attributes.java:32 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 304 | Attributes.java:38 | 0.0 | `private static final String[] Empty = {};` |
| 1 | 304 | Attributes.java:42 | 0.0 | `private int size = 0; // number of slots used (not capacity, which is keys.length` |
| 1 | 304 | Attributes.java:43 | 0.0 | `String[] keys = Empty;` |
| 1 | 304 | Attributes.java:44 | 0.0 | `String[] vals = Empty;` |
| 1 | 304 | ChangeNotifyingArrayList.java:11 | 0.0 | `super(initialCapacity);` |
| 1 | 304 | ChangeNotifyingArrayList.java:24 | 0.0 | `onContentsChanged();` |
| 1 | 304 | ChangeNotifyingArrayList.java:25 | 0.0 | `return super.add(e);` |
| 1 | 304 | CharacterReader.java:33 | 0.0 | `reader = input;` |
| 1 | 304 | CharacterReader.java:34 | 0.0 | `charBuf = new char[sz > maxBufferLen ? maxBufferLen : sz];` |

