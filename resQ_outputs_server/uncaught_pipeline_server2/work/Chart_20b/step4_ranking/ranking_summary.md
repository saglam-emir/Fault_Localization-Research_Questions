# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ValueMarker.java', 95)]

Ground_Truth_Answerable: True

- SBFL   ranked 12816 statement(s)
- Hybrid ranked 69 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Marker.java:265 | 0.258199 | `return this.outlinePaint;` |
| 2 | 1 | Marker.java:238 | 0.111111 | `return this.stroke;` |
| 3 | 1 | Marker.java:211 | 0.105409 | `return this.paint;` |
| 4 | 1 | ValueMarker.java:107 | 0.103695 | `return this.value;` |
| 5 | 2 | ValueMarker.java:95 | 0.059235 | `super(paint, stroke, paint, stroke, alpha);` |
| 5 | 2 | ValueMarker.java:96 | 0.059235 | `this.value = value;` |
| 7 | 22 | LengthAdjustmentType.java:59 | 0.053376 | `public static final LengthAdjustmentType NO_CHANGE` |
| 7 | 22 | LengthAdjustmentType.java:63 | 0.053376 | `public static final LengthAdjustmentType EXPAND` |
| 7 | 22 | LengthAdjustmentType.java:67 | 0.053376 | `public static final LengthAdjustmentType CONTRACT` |
| 7 | 22 | LengthAdjustmentType.java:78 | 0.053376 | `private LengthAdjustmentType(String name) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | ValueMarker.java:95 | 0.5 | `super(paint, stroke, paint, stroke, alpha);` |
| 1 | 2 | ValueMarker.java:96 | 0.5 | `this.value = value;` |
| 3 | 23 | LengthAdjustmentType.java:67 | 0.179605 | `public static final LengthAdjustmentType CONTRACT` |
| 3 | 23 | LengthAdjustmentType.java:78 | 0.179605 | `private LengthAdjustmentType(String name) {` |
| 3 | 23 | LengthAdjustmentType.java:79 | 0.179605 | `this.name = name;` |
| 3 | 23 | Marker.java:117 | 0.179605 | `private String label = null;` |
| 3 | 23 | Marker.java:175 | 0.179605 | `float alpha) {` |
| 3 | 23 | Marker.java:187 | 0.179605 | `this.paint = paint;` |
| 3 | 23 | Marker.java:188 | 0.179605 | `this.stroke = stroke;` |
| 3 | 23 | Marker.java:189 | 0.179605 | `this.outlinePaint = outlinePaint;` |

