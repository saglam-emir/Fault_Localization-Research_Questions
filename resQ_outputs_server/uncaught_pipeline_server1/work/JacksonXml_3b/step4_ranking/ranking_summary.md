# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FromXmlParser.java', 669), ('FromXmlParser.java', 671)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('FromXmlParser.java', 669, '->', 668)]

Ground_Truth_Answerable: True

- SBFL   ranked 1209 statement(s)
- Hybrid ranked 125 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | FromXmlParser.java:669 | 0.5 | `_currText = _xmlTokens.getText();` |
| 1 | 3 | FromXmlParser.java:670 | 0.5 | `_currToken = JsonToken.VALUE_STRING;` |
| 1 | 3 | FromXmlParser.java:671 | 0.5 | `break;` |
| 4 | 6 | FromXmlParser.java:603 | 0.223607 | `_binaryValue = null;` |
| 4 | 6 | FromXmlParser.java:604 | 0.223607 | `if (_nextToken != null) {` |
| 4 | 6 | FromXmlParser.java:617 | 0.223607 | `int token = _xmlTokens.next();` |
| 4 | 6 | FromXmlParser.java:620 | 0.223607 | `while (token == XmlTokenStream.XML_START_ELEMENT) {` |
| 4 | 6 | FromXmlParser.java:643 | 0.223607 | `switch (token) {` |
| 4 | 6 | FromXmlParser.java:692 | 0.223607 | `return null;` |
| 10 | 33 | FromXmlParser.java:35 | 0.169638 | `public enum Feature implements FormatFeature` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | FromXmlParser.java:603 | 1.0 | `_binaryValue = null;` |
| 1 | 4 | FromXmlParser.java:647 | 1.0 | `_mayBeLeaf = false;` |
| 1 | 4 | FromXmlParser.java:669 | 1.0 | `_currText = _xmlTokens.getText();` |
| 1 | 4 | FromXmlParser.java:670 | 1.0 | `_currToken = JsonToken.VALUE_STRING;` |
| 5 | 1 | XmlTokenStream.java:313 | 0.5 | `_textValue = _xmlReader.getAttributeValue(_nextAttributeIndex);` |
| 6 | 2 | FromXmlParser.java:537 | 0.408248 | `if (_mayBeLeaf) {` |
| 6 | 2 | FromXmlParser.java:545 | 0.408248 | `return (_currToken = JsonToken.FIELD_NAME);` |
| 8 | 12 | FromXmlParser.java:173 | 0.223607 | `_xmlTokens = new XmlTokenStream(xmlReader, ctxt.getSourceReference());` |
| 8 | 12 | XmlFactory.java:556 | 0.223607 | `sr = _xmlInputFactory.createXMLStreamReader(r);` |
| 8 | 12 | XmlFactory.java:557 | 0.223607 | `sr = _initializeXmlReader(sr);` |

