# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XmlSerializerProvider.java', 59)]

Ground_Truth_Answerable: True

- SBFL   ranked 1328 statement(s)
- Hybrid ranked 54 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | XmlFactory.java:132 | 0.288675 | `super(src, oc);` |
| 1 | 12 | XmlFactory.java:133 | 0.288675 | `_xmlParserFeatures = src._xmlParserFeatures;` |
| 1 | 12 | XmlFactory.java:134 | 0.288675 | `_xmlGeneratorFeatures = src._xmlGeneratorFeatures;` |
| 1 | 12 | XmlFactory.java:135 | 0.288675 | `_cfgNameForTextElement = src._cfgNameForTextElement;` |
| 1 | 12 | XmlFactory.java:136 | 0.288675 | `_xmlInputFactory = src._xmlInputFactory;` |
| 1 | 12 | XmlFactory.java:137 | 0.288675 | `_xmlOutputFactory = src._xmlOutputFactory;` |
| 1 | 12 | XmlFactory.java:157 | 0.288675 | `_checkInvalidCopy(XmlFactory.class);` |
| 1 | 12 | XmlFactory.java:158 | 0.288675 | `return new XmlFactory(this, null);` |
| 1 | 12 | XmlMapper.java:96 | 0.288675 | `super(src);` |
| 1 | 12 | XmlMapper.java:97 | 0.288675 | `_xmlModule = src._xmlModule;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 54 | DefaultXmlPrettyPrinter.java:106 | 1.0 | `public DefaultXmlPrettyPrinter() { }` |
| 1 | 54 | FromXmlParser.java:50 | 1.0 | `EMPTY_ELEMENT_AS_NULL(true)` |
| 1 | 54 | FromXmlParser.java:62 | 1.0 | `int flags = 0;` |
| 1 | 54 | FromXmlParser.java:64 | 1.0 | `if (f.enabledByDefault()) {` |
| 1 | 54 | FromXmlParser.java:65 | 1.0 | `flags |= f.getMask();` |
| 1 | 54 | FromXmlParser.java:68 | 1.0 | `return flags;` |
| 1 | 54 | FromXmlParser.java:71 | 1.0 | `private Feature(boolean defaultState) {` |
| 1 | 54 | FromXmlParser.java:72 | 1.0 | `_defaultState = defaultState;` |
| 1 | 54 | FromXmlParser.java:73 | 1.0 | `_mask = (1 << ordinal());` |
| 1 | 54 | FromXmlParser.java:76 | 1.0 | `@Override public boolean enabledByDefault() { return _defaultState; }` |

