# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultDateTypeAdapter.java', 99), ('DefaultDateTypeAdapter.java', 100)]

Ground_Truth_Answerable: True

- SBFL   ranked 2719 statement(s)
- Hybrid ranked 213 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DefaultDateTypeAdapter.java:100 | 1.0 | `throw new JsonParseException("The date should be a string value");` |
| 2 | 1 | JsonParseException.java:42 | 0.534522 | `super(msg);` |
| 3 | 1 | DefaultDateTypeAdapter.java:49 | 0.5 | `this(dateType,` |
| 4 | 1 | DefaultDateTypeAdapter.java:99 | 0.447214 | `if (in.peek() != JsonToken.STRING) {` |
| 5 | 3 | TypeAdapter.java:259 | 0.365148 | `JsonReader reader = new JsonReader(in);` |
| 5 | 3 | TypeAdapter.java:260 | 0.365148 | `return read(reader);` |
| 5 | 3 | TypeAdapter.java:273 | 0.365148 | `return fromJson(new StringReader(json));` |
| 8 | 6 | DefaultDateTypeAdapter.java:40 | 0.353553 | `final class DefaultDateTypeAdapter extends TypeAdapter<Date> {` |
| 8 | 6 | DefaultDateTypeAdapter.java:74 | 0.353553 | `DefaultDateTypeAdapter(final Class<? extends Date> dateType, DateFormat enUsFormat, DateFormat localFormat) {` |
| 8 | 6 | DefaultDateTypeAdapter.java:75 | 0.353553 | `if ( dateType != Date.class && dateType != java.sql.Date.class && dateType != Timestamp.class ) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DefaultDateTypeAdapter.java:49 | 1.0 | `this(dateType,` |
| 1 | 5 | DefaultDateTypeAdapter.java:74 | 1.0 | `DefaultDateTypeAdapter(final Class<? extends Date> dateType, DateFormat enUsFormat, DateFormat localFormat) {` |
| 1 | 5 | DefaultDateTypeAdapter.java:78 | 1.0 | `this.dateType = dateType;` |
| 1 | 5 | DefaultDateTypeAdapter.java:79 | 1.0 | `this.enUsFormat = enUsFormat;` |
| 1 | 5 | DefaultDateTypeAdapter.java:80 | 1.0 | `this.localFormat = localFormat;` |
| 6 | 1 | TypeAdapter.java:119 | 0.57735 | `public abstract class TypeAdapter<T> {` |
| 7 | 207 | ArrayTypeAdapter.java:39 | 0.0 | `public static final TypeAdapterFactory FACTORY = new TypeAdapterFactory() {` |
| 7 | 207 | CollectionTypeAdapterFactory.java:39 | 0.0 | `public CollectionTypeAdapterFactory(ConstructorConstructor constructorConstructor) {` |
| 7 | 207 | CollectionTypeAdapterFactory.java:40 | 0.0 | `this.constructorConstructor = constructorConstructor;` |
| 7 | 207 | ConstructorConstructor.java:51 | 0.0 | `public ConstructorConstructor(Map<Type, InstanceCreator<?>> instanceCreators) {` |

