# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('IOContext.java', 274), ('IOContext.java', 279), ('IOContext.java', 284)]

Ground_Truth_Answerable: True

- SBFL   ranked 7143 statement(s)
- Hybrid ranked 258 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | IOContext.java:284 | 1.0 | `return new IllegalArgumentException("Trying to release buffer not owned by the context");` |
| 2 | 4 | IOContext.java:146 | 0.1066 | `_verifyAlloc(_readIOBuffer);` |
| 2 | 4 | IOContext.java:147 | 0.1066 | `return (_readIOBuffer = _bufferRecycler.allocByteBuffer(BufferRecycler.BYTE_READ_IO_BUFFER));` |
| 2 | 4 | IOContext.java:207 | 0.1066 | `if (buf != null) {` |
| 2 | 4 | IOContext.java:211 | 0.1066 | `_verifyRelease(buf, _readIOBuffer);` |
| 6 | 1 | IOContext.java:274 | 0.088388 | `if ((toRelease != src) && (toRelease.length <= src.length)) { throw wrongBuf(); }` |
| 7 | 10 | BufferRecycler.java:86 | 0.088045 | `return allocByteBuffer(ix, 0);` |
| 7 | 10 | BufferRecycler.java:90 | 0.088045 | `final int DEF_SIZE = byteBufferLength(ix);` |
| 7 | 10 | BufferRecycler.java:91 | 0.088045 | `if (minSize < DEF_SIZE) {` |
| 7 | 10 | BufferRecycler.java:92 | 0.088045 | `minSize = DEF_SIZE;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 258 | BufferRecycler.java:45 | 0.0 | `private final static int[] BYTE_BUFFER_LENGTHS = new int[] { 8000, 8000, 2000, 2000 };` |
| 1 | 258 | BufferRecycler.java:62 | 0.0 | `this(4, 4);` |
| 1 | 258 | BufferRecycler.java:71 | 0.0 | `protected BufferRecycler(int bbCount, int cbCount) {` |
| 1 | 258 | BufferRecycler.java:72 | 0.0 | `_byteBuffers = new byte[bbCount][];` |
| 1 | 258 | BufferRecycler.java:73 | 0.0 | `_charBuffers = new char[cbCount][];` |
| 1 | 258 | BufferRecycler.java:86 | 0.0 | `return allocByteBuffer(ix, 0);` |
| 1 | 258 | BufferRecycler.java:90 | 0.0 | `final int DEF_SIZE = byteBufferLength(ix);` |
| 1 | 258 | BufferRecycler.java:91 | 0.0 | `if (minSize < DEF_SIZE) {` |
| 1 | 258 | BufferRecycler.java:92 | 0.0 | `minSize = DEF_SIZE;` |
| 1 | 258 | BufferRecycler.java:94 | 0.0 | `byte[] buffer = _byteBuffers[ix];` |

