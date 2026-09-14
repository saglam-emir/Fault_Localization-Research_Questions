# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ShapeList.java', 111)]

Ground_Truth_Answerable: True

- SBFL   ranked 13455 statement(s)
- Hybrid ranked 13 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | AbstractObjectList.java:212 | 0.5 | `result = HashUtilities.hashCode(result, this.objects[0]);` |
| 1 | 14 | AbstractObjectList.java:213 | 0.5 | `if (size > 1) {` |
| 1 | 14 | AbstractObjectList.java:214 | 0.5 | `result = HashUtilities.hashCode(result, this.objects[size - 1]);` |
| 1 | 14 | AbstractObjectList.java:215 | 0.5 | `if (size > 2) {` |
| 1 | 14 | AbstractObjectList.java:216 | 0.5 | `result = HashUtilities.hashCode(result,` |
| 1 | 14 | ShapeList.java:121 | 0.5 | `return super.hashCode();` |
| 1 | 14 | ShapeList.java:137 | 0.5 | `Shape shape = getShape(i);` |
| 1 | 14 | ShapeList.java:138 | 0.5 | `if (shape != null) {` |
| 1 | 14 | ShapeList.java:139 | 0.5 | `stream.writeInt(i);` |
| 1 | 14 | ShapeList.java:140 | 0.5 | `SerialUtilities.writeShape(shape, stream);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | ShapeList.java:105 | 0.408248 | `if (obj == this) {` |
| 1 | 2 | ShapeList.java:108 | 0.408248 | `if (!(obj instanceof ShapeList)) {` |
| 3 | 10 | AbstractObjectList.java:68 | 0.316228 | `private int size = 0;` |
| 3 | 10 | AbstractObjectList.java:71 | 0.316228 | `private int increment = DEFAULT_INITIAL_CAPACITY;` |
| 3 | 10 | AbstractObjectList.java:77 | 0.316228 | `this(DEFAULT_INITIAL_CAPACITY);` |
| 3 | 10 | AbstractObjectList.java:86 | 0.316228 | `this (initialCapacity, initialCapacity);` |
| 3 | 10 | AbstractObjectList.java:95 | 0.316228 | `protected AbstractObjectList(int initialCapacity, int increment) {` |
| 3 | 10 | AbstractObjectList.java:96 | 0.316228 | `this.objects = new Object[initialCapacity];` |
| 3 | 10 | AbstractObjectList.java:97 | 0.316228 | `this.increment = increment;` |
| 3 | 10 | AbstractObjectList.java:132 | 0.316228 | `this.size = Math.max(this.size, index + 1);` |

