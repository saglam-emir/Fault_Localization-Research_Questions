# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UnsafeAllocator.java', 23), ('UnsafeAllocator.java', 48), ('UnsafeAllocator.java', 71), ('UnsafeAllocator.java', 90), ('UnsafeAllocator.java', 110)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/UnsafeAllocator.java', 23), ('gson/src/main/java/com/google/gson/internal/UnsafeAllocator.java', 71), ('gson/src/main/java/com/google/gson/internal/UnsafeAllocator.java', 90), ('gson/src/main/java/com/google/gson/internal/UnsafeAllocator.java', 110)]

- SBFL   ranked 2374 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UnsafeAllocator.java:48 | 0.239046 | `return (T) allocateInstance.invoke(unsafe, c);` |
| 2 | 7 | UnsafeAllocator.java:30 | 0.138013 | `public abstract class UnsafeAllocator {` |
| 2 | 7 | UnsafeAllocator.java:39 | 0.138013 | `Class<?> unsafeClass = Class.forName("sun.misc.Unsafe");` |
| 2 | 7 | UnsafeAllocator.java:40 | 0.138013 | `Field f = unsafeClass.getDeclaredField("theUnsafe");` |
| 2 | 7 | UnsafeAllocator.java:41 | 0.138013 | `f.setAccessible(true);` |
| 2 | 7 | UnsafeAllocator.java:42 | 0.138013 | `final Object unsafe = f.get(null);` |
| 2 | 7 | UnsafeAllocator.java:43 | 0.138013 | `final Method allocateInstance = unsafeClass.getMethod("allocateInstance", Class.class);` |
| 2 | 7 | UnsafeAllocator.java:44 | 0.138013 | `return new UnsafeAllocator() {` |
| 9 | 2366 | $Gson$Preconditions.java:38 | 0.0 | `if (obj == null) {` |
| 9 | 2366 | $Gson$Preconditions.java:41 | 0.0 | `return obj;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UnsafeAllocator.java:48 | 1.0 | `return (T) allocateInstance.invoke(unsafe, c);` |

