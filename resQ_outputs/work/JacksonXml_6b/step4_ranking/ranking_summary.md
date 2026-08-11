# Ranking Comparison Summary

Ground truth faulty statement(s): [('ToXmlGenerator.java', 843), ('ToXmlGenerator.java', 844), ('ToXmlGenerator.java', 845), ('ToXmlGenerator.java', 846), ('ToXmlGenerator.java', 847), ('ToXmlGenerator.java', 848), ('ToXmlGenerator.java', 849), ('ToXmlGenerator.java', 851), ('ToXmlGenerator.java', 866), ('ToXmlGenerator.java', 867)]

- SBFL   top rank: 1335, AP: 0.0000
- Hybrid top rank: 66, AP: 0.0000

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | XmlSerializerProvider.java:108 | 0.6742 | `} catch (Exception e) { // but wrap RuntimeExceptions, to get path information` |
| 1 | 4 | XmlSerializerProvider.java:109 | 0.6742 | `throw _wrapAsIOE(gen, e);` |
| 1 | 4 | XmlSerializerProvider.java:235 | 0.6742 | `if (e instanceof IOException) {` |
| 1 | 4 | XmlSerializerProvider.java:236 | 0.6742 | `return (IOException) e;` |
| 5 | 2 | XmlMapper.java:49 | 0.269903 | `this(new XmlFactory());` |
| 5 | 2 | XmlMapper.java:67 | 0.269903 | `this(xmlFactory, DEFAULT_XML_MODULE);` |
| 7 | 40 | DefaultXmlPrettyPrinter.java:60 | 0.25742 | `protected Indenter _arrayIndenter = new FixedSpaceIndenter();` |
| 7 | 40 | DefaultXmlPrettyPrinter.java:68 | 0.25742 | `protected Indenter _objectIndenter = new Lf2SpacesIndenter();` |
| 7 | 40 | DefaultXmlPrettyPrinter.java:77 | 0.25742 | `protected boolean _spacesInObjectEntries = true;` |
| 7 | 40 | DefaultXmlPrettyPrinter.java:89 | 0.25742 | `protected transient int _nesting = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JacksonXmlAnnotationIntrospector.java:34 | 0.476731 | `public JacksonXmlAnnotationIntrospector(boolean defaultUseWrapper) {` |
| 1 | 3 | JacksonXmlModule.java:65 | 0.476731 | `context.insertAnnotationIntrospector(_constructIntrospector());` |
| 1 | 3 | JacksonXmlModule.java:126 | 0.476731 | `return new JacksonXmlAnnotationIntrospector(_cfgDefaultUseWrapper);` |
| 4 | 1 | JacksonXmlModule.java:75 | 0.433861 | `super.setupModule(context);` |
| 5 | 61 | DefaultXmlPrettyPrinter.java:106 | 0.0 | `public DefaultXmlPrettyPrinter() { }` |
| 5 | 61 | FromXmlParser.java:50 | 0.0 | `EMPTY_ELEMENT_AS_NULL(true)` |
| 5 | 61 | FromXmlParser.java:62 | 0.0 | `int flags = 0;` |
| 5 | 61 | FromXmlParser.java:64 | 0.0 | `if (f.enabledByDefault()) {` |
| 5 | 61 | FromXmlParser.java:65 | 0.0 | `flags |= f.getMask();` |
| 5 | 61 | FromXmlParser.java:68 | 0.0 | `return flags;` |

