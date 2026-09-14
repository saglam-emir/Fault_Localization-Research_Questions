# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('GeneratorBase.java', 53), ('GeneratorBase.java', 434), ('GeneratorBase.java', 435), ('UTF8JsonGenerator.java', 910), ('UTF8JsonGenerator.java', 911), ('UTF8JsonGenerator.java', 912), ('UTF8JsonGenerator.java', 913), ('WriterBasedJsonGenerator.java', 687), ('WriterBasedJsonGenerator.java', 688), ('WriterBasedJsonGenerator.java', 689), ('WriterBasedJsonGenerator.java', 690)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/base/GeneratorBase.java', 53), ('src/main/java/com/fasterxml/jackson/core/base/GeneratorBase.java', 434)]

- SBFL   ranked 7136 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | WriterBasedJsonGenerator.java:485 | 1.0 | `int amount = _outputEnd;` |
| 1 | 7 | WriterBasedJsonGenerator.java:486 | 1.0 | `text.getChars(offset, offset+amount, _outputBuffer, 0);` |
| 1 | 7 | WriterBasedJsonGenerator.java:487 | 1.0 | `_outputHead = 0;` |
| 1 | 7 | WriterBasedJsonGenerator.java:488 | 1.0 | `_outputTail = amount;` |
| 1 | 7 | WriterBasedJsonGenerator.java:489 | 1.0 | `_flushBuffer();` |
| 1 | 7 | WriterBasedJsonGenerator.java:490 | 1.0 | `offset += amount;` |
| 1 | 7 | WriterBasedJsonGenerator.java:491 | 1.0 | `len -= amount;` |
| 8 | 12 | WriterBasedJsonGenerator.java:418 | 0.707107 | `writeRawLong(text);` |
| 8 | 12 | WriterBasedJsonGenerator.java:476 | 0.707107 | `int room = _outputEnd - _outputTail;` |
| 8 | 12 | WriterBasedJsonGenerator.java:478 | 0.707107 | `text.getChars(0, room, _outputBuffer, _outputTail);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | WriterBasedJsonGenerator.java:690 | 1.0 | `writeRaw(value.toPlainString());` |

