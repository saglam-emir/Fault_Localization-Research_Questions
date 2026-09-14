# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CategoryPlot.java', 2166), ('CategoryPlot.java', 2448), ('XYPlot.java', 2293), ('XYPlot.java', 2529)]

Ground_Truth_Answerable: True

- SBFL   ranked 14792 statement(s)
- Hybrid ranked 602 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 26 | CategoryPlot.java:2106 | 0.408248 | `return removeDomainMarker(marker, Layer.FOREGROUND);` |
| 1 | 26 | CategoryPlot.java:2122 | 0.408248 | `return removeDomainMarker(0, marker, layer);` |
| 1 | 26 | CategoryPlot.java:2139 | 0.408248 | `return removeDomainMarker(index, marker, layer, true);` |
| 1 | 26 | CategoryPlot.java:2158 | 0.408248 | `if (layer == Layer.FOREGROUND) {` |
| 1 | 26 | CategoryPlot.java:2159 | 0.408248 | `markers = (ArrayList) this.foregroundDomainMarkers.get(new Integer(` |
| 1 | 26 | CategoryPlot.java:2166 | 0.408248 | `boolean removed = markers.remove(marker);` |
| 1 | 26 | CategoryPlot.java:2378 | 0.408248 | `return removeRangeMarker(marker, Layer.FOREGROUND);` |
| 1 | 26 | CategoryPlot.java:2396 | 0.408248 | `return removeRangeMarker(0, marker, layer);` |
| 1 | 26 | CategoryPlot.java:2415 | 0.408248 | `return removeRangeMarker(index, marker, layer, true);` |
| 1 | 26 | CategoryPlot.java:2436 | 0.408248 | `if (marker == null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | LengthAdjustmentType.java:65 | 1.0 | `public static final LengthAdjustmentType CONTRACT` |
| 1 | 17 | LengthAdjustmentType.java:76 | 1.0 | `private LengthAdjustmentType(String name) {` |
| 1 | 17 | LengthAdjustmentType.java:77 | 1.0 | `this.name = name;` |
| 1 | 17 | Marker.java:115 | 1.0 | `private String label = null;` |
| 1 | 17 | Marker.java:173 | 1.0 | `float alpha) {` |
| 1 | 17 | Marker.java:185 | 1.0 | `this.paint = paint;` |
| 1 | 17 | Marker.java:186 | 1.0 | `this.stroke = stroke;` |
| 1 | 17 | Marker.java:187 | 1.0 | `this.outlinePaint = outlinePaint;` |
| 1 | 17 | Marker.java:188 | 1.0 | `this.outlineStroke = outlineStroke;` |
| 1 | 17 | Marker.java:189 | 1.0 | `this.alpha = alpha;` |

