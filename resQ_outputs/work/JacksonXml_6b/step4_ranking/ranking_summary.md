# Ranking Comparison Summary

Ground truth faulty statement(s): [('ToXmlGenerator.java', 843), ('ToXmlGenerator.java', 844), ('ToXmlGenerator.java', 845), ('ToXmlGenerator.java', 846), ('ToXmlGenerator.java', 847), ('ToXmlGenerator.java', 848), ('ToXmlGenerator.java', 849), ('ToXmlGenerator.java', 851), ('ToXmlGenerator.java', 866), ('ToXmlGenerator.java', 867)]

- SBFL   top rank: 1335, AP: 0.0000
- Hybrid top rank: , AP: 0.0000

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

