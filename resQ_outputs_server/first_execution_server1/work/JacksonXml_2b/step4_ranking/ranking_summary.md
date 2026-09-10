# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XmlTokenStream.java', 62), ('XmlTokenStream.java', 325), ('XmlTokenStream.java', 324), ('XmlTokenStream.java', 327), ('XmlTokenStream.java', 330), ('XmlTokenStream.java', 333), ('XmlTokenStream.java', 340), ('XmlTokenStream.java', 506)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('XmlTokenStream.java', 324, '->', 311), ('XmlTokenStream.java', 327, '->', 325), ('XmlTokenStream.java', 340, '->', 311)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/dataformat/xml/deser/XmlTokenStream.java', 62), ('src/main/java/com/fasterxml/jackson/dataformat/xml/deser/XmlTokenStream.java', 506)]

- SBFL   ranked 1167 statement(s)
- Hybrid ranked 125 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | XmlTextDeserializer.java:92 | 0.288675 | `Object bean = _valueInstantiator.createUsingDefault(ctxt);` |
| 1 | 3 | XmlTextDeserializer.java:93 | 0.288675 | `_xmlTextProperty.deserializeAndSet(jp, ctxt, bean);` |
| 1 | 3 | XmlTextDeserializer.java:94 | 0.288675 | `return bean;` |
| 4 | 13 | XmlBeanDeserializerModifier.java:99 | 0.182574 | `return new XmlTextDeserializer(deser, textProp);` |
| 4 | 13 | XmlTextDeserializer.java:46 | 0.182574 | `super(delegate);` |
| 4 | 13 | XmlTextDeserializer.java:47 | 0.182574 | `_xmlTextProperty = prop;` |
| 4 | 13 | XmlTextDeserializer.java:48 | 0.182574 | `_xmlTextPropertyIndex = prop.getPropertyIndex();` |
| 4 | 13 | XmlTextDeserializer.java:49 | 0.182574 | `_valueInstantiator = delegate.getValueInstantiator();` |
| 4 | 13 | XmlTextDeserializer.java:54 | 0.182574 | `super(delegate);` |
| 4 | 13 | XmlTextDeserializer.java:55 | 0.182574 | `_xmlTextPropertyIndex = textPropIndex;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | JacksonXmlModule.java:72 | 0.288675 | `super.setupModule(context);` |
| 2 | 3 | JacksonXmlAnnotationIntrospector.java:34 | 0.171499 | `public JacksonXmlAnnotationIntrospector(boolean defaultUseWrapper) {` |
| 2 | 3 | JacksonXmlModule.java:61 | 0.171499 | `context.insertAnnotationIntrospector(_constructIntrospector());` |
| 2 | 3 | JacksonXmlModule.java:123 | 0.171499 | `return new JacksonXmlAnnotationIntrospector(_cfgDefaultUseWrapper);` |
| 5 | 121 | DefaultXmlPrettyPrinter.java:60 | 0.0 | `protected Indenter _arrayIndenter = new FixedSpaceIndenter();` |
| 5 | 121 | DefaultXmlPrettyPrinter.java:68 | 0.0 | `protected Indenter _objectIndenter = new Lf2SpacesIndenter();` |
| 5 | 121 | DefaultXmlPrettyPrinter.java:106 | 0.0 | `public DefaultXmlPrettyPrinter() { }` |
| 5 | 121 | DefaultXmlPrettyPrinter.java:457 | 0.0 | `public FixedSpaceIndenter() { }` |
| 5 | 121 | DefaultXmlPrettyPrinter.java:500 | 0.0 | `public Lf2SpacesIndenter() { }` |
| 5 | 121 | ElementWrapper.java:28 | 0.0 | `_parent = parent;` |

