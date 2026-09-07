# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('GroupImpl.java', 250), ('GroupImpl.java', 251), ('GroupImpl.java', 252), ('GroupImpl.java', 261), ('GroupImpl.java', 262)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('GroupImpl.java', 261, '->', 255)]

Ground_Truth_Answerable: True

- SBFL   ranked 1271 statement(s)
- Hybrid ranked 358 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | FileValidator.java:78 | 1.0 | `final FileValidator validator = new FileValidator();` |
| 1 | 9 | FileValidator.java:79 | 1.0 | `validator.setExisting(true);` |
| 1 | 9 | FileValidator.java:80 | 1.0 | `validator.setFile(true);` |
| 1 | 9 | FileValidator.java:81 | 1.0 | `return validator;` |
| 1 | 9 | FileValidator.java:122 | 1.0 | `for (final ListIterator i = values.listIterator(); i.hasNext();) {` |
| 1 | 9 | FileValidator.java:123 | 1.0 | `final String name = (String)i.next();` |
| 1 | 9 | FileValidator.java:124 | 1.0 | `final File f = new File(name);` |
| 1 | 9 | FileValidator.java:126 | 1.0 | `if ((existing && !f.exists())` |
| 1 | 9 | FileValidator.java:136 | 1.0 | `i.set(f);` |
| 10 | 10 | ArgumentImpl.java:251 | 0.707107 | `validator.validate(values);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | ArgumentBuilder.java:221 | 1.0 | `this.validator = newValidator;` |
| 1 | 19 | ArgumentBuilder.java:222 | 1.0 | `return this;` |
| 1 | 19 | DefaultOptionBuilder.java:165 | 1.0 | `this.description = newDescription;` |
| 1 | 19 | DefaultOptionBuilder.java:167 | 1.0 | `return this;` |
| 1 | 19 | DefaultOptionBuilder.java:176 | 1.0 | `this.required = newRequired;` |
| 1 | 19 | DefaultOptionBuilder.java:178 | 1.0 | `return this;` |
| 1 | 19 | FileValidator.java:59 | 1.0 | `public class FileValidator implements Validator {` |
| 1 | 19 | FileValidator.java:78 | 1.0 | `final FileValidator validator = new FileValidator();` |
| 1 | 19 | FileValidator.java:79 | 1.0 | `validator.setExisting(true);` |
| 1 | 19 | FileValidator.java:80 | 1.0 | `validator.setFile(true);` |

