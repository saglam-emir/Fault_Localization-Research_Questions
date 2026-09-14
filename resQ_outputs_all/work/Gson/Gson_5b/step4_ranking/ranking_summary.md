# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ISO8601Utils.java', 214)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ISO8601Utils.java', 214, '->', 207)]

Ground_Truth_Answerable: True

- SBFL   ranked 130 statement(s)
- Hybrid ranked 12 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 35 | DefaultDateTypeAdapter.java:106 | 1.0 | `} catch (ParseException e) {` |
| 1 | 35 | DefaultDateTypeAdapter.java:107 | 1.0 | `throw new JsonSyntaxException(json.getAsString(), e);` |
| 1 | 35 | ISO8601Utils.java:178 | 1.0 | `offset += 1;` |
| 1 | 35 | ISO8601Utils.java:179 | 1.0 | `int endOffset = indexOfNonDigit(date, offset + 1); // assume at least one digit` |
| 1 | 35 | ISO8601Utils.java:180 | 1.0 | `int parseEndOffset = Math.min(endOffset, offset + 3); // parse up to 3 digits` |
| 1 | 35 | ISO8601Utils.java:181 | 1.0 | `int fraction = parseInt(date, offset, parseEndOffset);` |
| 1 | 35 | ISO8601Utils.java:183 | 1.0 | `switch (parseEndOffset - offset) { // number of digits parsed` |
| 1 | 35 | ISO8601Utils.java:191 | 1.0 | `milliseconds = fraction;` |
| 1 | 35 | ISO8601Utils.java:193 | 1.0 | `offset = endOffset;` |
| 1 | 35 | ISO8601Utils.java:210 | 1.0 | `} else if (timezoneIndicator == '+' || timezoneIndicator == '-') {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | DefaultDateTypeAdapter.java:46 | 1.0 | `this(DateFormat.getDateTimeInstance(DateFormat.DEFAULT, DateFormat.DEFAULT, Locale.US),` |
| 1 | 12 | DefaultDateTypeAdapter.java:63 | 1.0 | `DefaultDateTypeAdapter(DateFormat enUsFormat, DateFormat localFormat) {` |
| 1 | 12 | DefaultDateTypeAdapter.java:64 | 1.0 | `this.enUsFormat = enUsFormat;` |
| 1 | 12 | DefaultDateTypeAdapter.java:65 | 1.0 | `this.localFormat = localFormat;` |
| 1 | 12 | DefaultDateTypeAdapter.java:81 | 1.0 | `if (!(json instanceof JsonPrimitive)) {` |
| 1 | 12 | JsonElement.java:33 | 1.0 | `public abstract class JsonElement {` |
| 1 | 12 | JsonPrimitive.java:64 | 1.0 | `public JsonPrimitive(String string) {` |
| 1 | 12 | JsonPrimitive.java:65 | 1.0 | `setValue(string);` |
| 1 | 12 | JsonPrimitive.java:94 | 1.0 | `if (primitive instanceof Character) {` |
| 1 | 12 | JsonPrimitive.java:100 | 1.0 | `$Gson$Preconditions.checkArgument(primitive instanceof Number` |

