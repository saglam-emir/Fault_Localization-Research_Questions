# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CpioArchiveOutputStream.java', 346)]

Ground_Truth_Answerable: True

- SBFL   ranked 1245 statement(s)
- Hybrid ranked 138 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 114 | ArchiveStreamFactory.java:71 | 1.0 | `} else if ("cpio".equalsIgnoreCase(archiverName)) {` |
| 1 | 114 | ArchiveStreamFactory.java:72 | 1.0 | `return new CpioArchiveInputStream(in);` |
| 1 | 114 | CpioArchiveEntry.java:479 | 1.0 | `checkNewFormat();` |
| 1 | 114 | CpioArchiveEntry.java:480 | 1.0 | `this.chksum = chksum;` |
| 1 | 114 | CpioArchiveEntry.java:504 | 1.0 | `checkNewFormat();` |
| 1 | 114 | CpioArchiveEntry.java:505 | 1.0 | `this.maj = maj;` |
| 1 | 114 | CpioArchiveEntry.java:515 | 1.0 | `checkNewFormat();` |
| 1 | 114 | CpioArchiveEntry.java:516 | 1.0 | `this.min = min;` |
| 1 | 114 | CpioArchiveEntry.java:571 | 1.0 | `this.gid = gid;` |
| 1 | 114 | CpioArchiveEntry.java:581 | 1.0 | `this.inode = inode;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 138 | ArchiveInputStream.java:24 | 1.0 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 138 | ArchiveStreamFactory.java:45 | 1.0 | `public class ArchiveStreamFactory {` |
| 1 | 138 | ArchiveStreamFactory.java:63 | 1.0 | `if ("ar".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:65 | 1.0 | `} else if ("zip".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:67 | 1.0 | `} else if ("tar".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:69 | 1.0 | `} else if ("jar".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:72 | 1.0 | `return new CpioArchiveInputStream(in);` |
| 1 | 138 | ArchiveStreamFactory.java:94 | 1.0 | `if ("ar".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:96 | 1.0 | `} else if ("zip".equalsIgnoreCase(archiverName)) {` |
| 1 | 138 | ArchiveStreamFactory.java:98 | 1.0 | `} else if ("tar".equalsIgnoreCase(archiverName)) {` |

