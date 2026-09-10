# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArrayUtils.java', 3295), ('ArrayUtils.java', 3574)]

Ground_Truth_Answerable: True

- SBFL   ranked 4773 statement(s)
- Hybrid ranked 8 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | ArrayUtils.java:3292 | 0.57735 | `} else if (element != null) {` |
| 1 | 2 | ArrayUtils.java:3295 | 0.57735 | `type = Object.class;` |
| 3 | 4 | ArrayUtils.java:3290 | 0.333333 | `if (array != null){` |
| 3 | 4 | ArrayUtils.java:3298 | 0.333333 | `T[] newArray = (T[]) copyArrayGrow1(array, type);` |
| 3 | 4 | ArrayUtils.java:3299 | 0.333333 | `newArray[newArray.length - 1] = element;` |
| 3 | 4 | ArrayUtils.java:3300 | 0.333333 | `return newArray;` |
| 7 | 1 | ArrayUtils.java:3535 | 0.19245 | `return Array.newInstance(newArrayComponentType, 1);` |
| 8 | 1 | ArrayUtils.java:3529 | 0.174078 | `if (array != null) {` |
| 9 | 19 | ArrayUtils.java:54 | 0.031734 | `public static final Object[] EMPTY_OBJECT_ARRAY = new Object[0];` |
| 9 | 19 | ArrayUtils.java:58 | 0.031734 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | ArrayUtils.java:3290 | 1.0 | `if (array != null){` |
| 1 | 8 | ArrayUtils.java:3292 | 1.0 | `} else if (element != null) {` |
| 1 | 8 | ArrayUtils.java:3295 | 1.0 | `type = Object.class;` |
| 1 | 8 | ArrayUtils.java:3298 | 1.0 | `T[] newArray = (T[]) copyArrayGrow1(array, type);` |
| 1 | 8 | ArrayUtils.java:3299 | 1.0 | `newArray[newArray.length - 1] = element;` |
| 1 | 8 | ArrayUtils.java:3300 | 1.0 | `return newArray;` |
| 1 | 8 | ArrayUtils.java:3529 | 1.0 | `if (array != null) {` |
| 1 | 8 | ArrayUtils.java:3535 | 1.0 | `return Array.newInstance(newArrayComponentType, 1);` |

