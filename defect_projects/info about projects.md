# Info About Projects

Defects4J (v2.x) buggy-version checkouts under `defect_projects/`.

Each project has its own directory (e.g. `defect_projects/Lang`), and each
buggy version is checked out into its own subfolder named
`<lowerFirstLetter+rest>_<id>b` (e.g. `defect_projects/Lang/lang_1b`,
`defect_projects/Csv/csv_13b`).

Only **active** bug IDs are included (deprecated bug IDs excluded).

| Project | Buggy versions |
|---|---|
| Chart | 26 |
| Cli | 39 |
| Closure | 174 |
| Codec | 18 |
| Collections | 4 |
| Compress | 47 |
| Csv | 16 |
| Gson | 18 |
| JacksonCore | 26 |
| JacksonDatabind | 112 |
| JacksonXml | 6 |
| Jsoup | 93 |
| JxPath | 22 |
| Lang | 64 |
| Math | 106 |
| Mockito | 38 |
| Time | 26 |
| **Total** | **835** |

Generated with [resQ_scripts/checkout_all_defects4j.sh](../resQ_scripts/checkout_all_defects4j.sh).
