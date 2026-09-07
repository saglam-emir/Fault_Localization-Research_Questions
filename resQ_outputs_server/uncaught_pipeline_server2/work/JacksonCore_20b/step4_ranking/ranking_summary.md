# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonGenerator.java', 1330)]

Ground_Truth_Answerable: True

- SBFL   ranked 8781 statement(s)
- Hybrid ranked 114 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | JsonGenerator.java:1330 | 1.0 | `throw new JsonGenerationException("No native support for writing embedded objects",` |
| 1 | 2 | JsonProcessingException.java:127 | 1.0 | `@Override public String toString() { return getClass().getName()+": "+getMessage(); }` |
| 3 | 2 | JsonGenerationException.java:48 | 0.365148 | `super(msg, (JsonLocation) null);` |
| 3 | 2 | JsonGenerationException.java:49 | 0.365148 | `_processor = g;` |
| 5 | 26 | Base64Variant.java:127 | 0.188982 | `base64Alphabet.getChars(0, alphaLen, _base64ToAsciiC, 0);` |
| 5 | 26 | Base64Variant.java:128 | 0.188982 | `Arrays.fill(_asciiToBase64, BASE64_VALUE_INVALID);` |
| 5 | 26 | Base64Variant.java:129 | 0.188982 | `for (int i = 0; i < alphaLen; ++i) {` |
| 5 | 26 | Base64Variant.java:130 | 0.188982 | `char alpha = _base64ToAsciiC[i];` |
| 5 | 26 | Base64Variant.java:131 | 0.188982 | `_base64ToAsciiB[i] = (byte) alpha;` |
| 5 | 26 | Base64Variant.java:132 | 0.188982 | `_asciiToBase64[alpha] = i;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | CharTypes.java:158 | 1.0 | `int[] table = new int[128];` |
| 1 | 11 | CharTypes.java:162 | 1.0 | `table[i] = CharacterEscapes.ESCAPE_STANDARD;` |
| 1 | 11 | CharTypes.java:167 | 1.0 | `table['"'] = '"';` |
| 1 | 11 | CharTypes.java:168 | 1.0 | `table['\\'] = '\\';` |
| 1 | 11 | CharTypes.java:170 | 1.0 | `table[0x08] = 'b';` |
| 1 | 11 | CharTypes.java:171 | 1.0 | `table[0x09] = 't';` |
| 1 | 11 | CharTypes.java:172 | 1.0 | `table[0x0C] = 'f';` |
| 1 | 11 | CharTypes.java:173 | 1.0 | `table[0x0A] = 'n';` |
| 1 | 11 | CharTypes.java:174 | 1.0 | `table[0x0D] = 'r';` |
| 1 | 11 | CharTypes.java:175 | 1.0 | `sOutputEscapes128 = table;` |

