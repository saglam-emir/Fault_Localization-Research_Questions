# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XmlSerializerProvider.java', 205), ('XmlSerializerProvider.java', 204)]

Ground_Truth_Answerable: True

- SBFL   ranked 1233 statement(s)
- Hybrid ranked 53 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | XmlSerializerProvider.java:69 | 0.5 | `_serializeXmlNull(gen);` |
| 1 | 5 | XmlSerializerProvider.java:70 | 0.5 | `return;` |
| 1 | 5 | XmlSerializerProvider.java:204 | 0.5 | `if (jgen instanceof ToXmlGenerator) {` |
| 1 | 5 | XmlSerializerProvider.java:205 | 0.5 | `_initWithRootName((ToXmlGenerator) jgen, ROOT_NAME_FOR_NULL);` |
| 1 | 5 | XmlSerializerProvider.java:207 | 0.5 | `super.serializeValue(jgen, null);` |
| 6 | 6 | ToXmlGenerator.java:808 | 0.353553 | `} else if (checkNextIsUnwrapped()) {` |
| 6 | 6 | ToXmlGenerator.java:811 | 0.353553 | `if (_xmlPrettyPrinter != null) {` |
| 6 | 6 | ToXmlGenerator.java:815 | 0.353553 | `_xmlWriter.writeEmptyElement(_nextName.getNamespaceURI(), _nextName.getLocalPart());` |
| 6 | 6 | XmlSerializerProvider.java:250 | 0.353553 | `String ns = name.getNamespace();` |
| 6 | 6 | XmlSerializerProvider.java:251 | 0.353553 | `if (ns == null || ns.isEmpty()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | JacksonXmlModule.java:72 | 0.288675 | `super.setupModule(context);` |
| 2 | 3 | JacksonXmlAnnotationIntrospector.java:34 | 0.242536 | `public JacksonXmlAnnotationIntrospector(boolean defaultUseWrapper) {` |
| 2 | 3 | JacksonXmlModule.java:61 | 0.242536 | `context.insertAnnotationIntrospector(_constructIntrospector());` |
| 2 | 3 | JacksonXmlModule.java:123 | 0.242536 | `return new JacksonXmlAnnotationIntrospector(_cfgDefaultUseWrapper);` |
| 5 | 49 | DefaultXmlPrettyPrinter.java:106 | 0.0 | `public DefaultXmlPrettyPrinter() { }` |
| 5 | 49 | FromXmlParser.java:49 | 0.0 | `int flags = 0;` |
| 5 | 49 | FromXmlParser.java:55 | 0.0 | `return flags;` |
| 5 | 49 | JacksonXmlModule.java:30 | 0.0 | `protected boolean _cfgDefaultUseWrapper = JacksonXmlAnnotationIntrospector.DEFAULT_USE_WRAPPER;` |
| 5 | 49 | JacksonXmlModule.java:40 | 0.0 | `protected String _cfgNameForTextElement = FromXmlParser.DEFAULT_UNNAMED_TEXT_PROPERTY;` |
| 5 | 49 | JacksonXmlModule.java:50 | 0.0 | `super("JacksonXmlModule", PackageVersion.VERSION);` |

