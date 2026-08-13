# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FromXmlParser.java', 512), ('FromXmlParser.java', 514), ('FromXmlParser.java', 550), ('FromXmlParser.java', 551), ('FromXmlParser.java', 552), ('FromXmlParser.java', 553)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/dataformat/xml/deser/FromXmlParser.java', 512)]

- SBFL   top rank: 1, AP: 0.6717
- Hybrid top rank: 125, AP: 0.0000

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | FromXmlParser.java:550 | 0.57735 | `_currToken = JsonToken.END_ARRAY;` |
| 1 | 4 | FromXmlParser.java:551 | 0.57735 | `_parsingContext = _parsingContext.getParent();` |
| 1 | 4 | FromXmlParser.java:552 | 0.57735 | `_namesToWrap = _parsingContext.getNamesToWrap();` |
| 1 | 4 | FromXmlParser.java:553 | 0.57735 | `return _currToken;` |
| 5 | 2 | FromXmlParser.java:305 | 0.471405 | `_xmlTokens.repeatStartElement();` |
| 5 | 2 | FromXmlParser.java:954 | 0.471405 | `return true;` |
| 7 | 1 | XmlTokenStream.java:448 | 0.408248 | `_currentWrapper = _currentWrapper.getParent();` |
| 8 | 6 | JacksonXmlAnnotationIntrospector.java:138 | 0.365148 | `_cfgDefaultUseWrapper = b;` |
| 8 | 6 | XmlMapper.java:124 | 0.365148 | `AnnotationIntrospector ai0 = getDeserializationConfig().getAnnotationIntrospector();` |
| 8 | 6 | XmlMapper.java:125 | 0.365148 | `for (AnnotationIntrospector ai : ai0.allIntrospectors()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | DefaultXmlPrettyPrinter.java:60 | 0.235702 | `protected Indenter _arrayIndenter = new FixedSpaceIndenter();` |
| 1 | 4 | DefaultXmlPrettyPrinter.java:68 | 0.235702 | `protected Indenter _objectIndenter = new Lf2SpacesIndenter();` |
| 1 | 4 | DefaultXmlPrettyPrinter.java:457 | 0.235702 | `public FixedSpaceIndenter() { }` |
| 1 | 4 | DefaultXmlPrettyPrinter.java:500 | 0.235702 | `public Lf2SpacesIndenter() { }` |
| 5 | 62 | ElementWrapper.java:28 | 0.204124 | `_parent = parent;` |
| 5 | 62 | ElementWrapper.java:29 | 0.204124 | `_wrapperName = wrapperLocalName;` |
| 5 | 62 | ElementWrapper.java:30 | 0.204124 | `_wrapperNamespace = (wrapperNamespace == null) ? "" : wrapperNamespace;` |
| 5 | 62 | ElementWrapper.java:40 | 0.204124 | `return new ElementWrapper(parent, wrapperLocalName, wrapperNamespace);` |
| 5 | 62 | FromXmlParser.java:172 | 0.204124 | `_nextToken = JsonToken.START_OBJECT;` |
| 5 | 62 | FromXmlParser.java:173 | 0.204124 | `_xmlTokens = new XmlTokenStream(xmlReader, ctxt.getSourceReference());` |

