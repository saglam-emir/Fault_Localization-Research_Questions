# Methodology Rationale / Metodoloji Gerekçesi

This document explains, cause-and-effect, why four corrections were made to the
`resQ_scripts/` pipeline, what pipeline defect or measurement gap each one
fixes, and what remains a disclosed, unfixed limitation rather than a bug. It
is written for anyone auditing the change history of this pipeline later.

Bu belge, `resQ_scripts/` pipeline'ında yapılan dört düzeltmenin neden
yapıldığını, her birinin hangi pipeline kusurunu veya ölçüm boşluğunu
düzelttiğini ve nelerin bir hata değil, açıkça belirtilmiş/çözülmemiş bir
kısıt olarak kaldığını neden-sonuç ilişkisiyle açıklar. Bu pipeline'ın
değişiklik geçmişini daha sonra denetleyecek herkes için yazılmıştır.

**Scope note / Kapsam notu:** all four changes are corrections to *our own*
orchestration code (`resQ_scripts/*.py`). No tool, library, or dependency
version (Slicer4J, Soot, Defects4J, the JVM) was upgraded, replaced, or
patched. — Dört değişikliğin tamamı *kendi* orkestrasyon kodumuza
(`resQ_scripts/*.py`) yapılan düzeltmelerdir. Hiçbir araç, kütüphane veya
bağımlılık sürümü (Slicer4J, Soot, Defects4J, JVM) yükseltilmedi,
değiştirilmedi veya yamanmadı.

---

## Step 1 — Re-running Csv_3b / JacksonXml_1b on the current pipeline
## Adım 1 — Csv_3b / JacksonXml_1b'nin güncel pipeline ile yeniden çalıştırılması

**Cause / Neden:** Git history showed Csv_3b and JacksonXml_1b were executed
on 2026-08-07 under commit `b1457e1`, *before* commit `3ecfc93` added the
`$stackN` trivial-slice retry (`slicer_runner._jimple_local_candidates`) and
the `ExceptionSite`/`criterion_kind` fallback. Csv_13b and JacksonXml_6b were
executed afterward, on the fixed code. The four targets were therefore not
directly comparable — any conclusion drawn from comparing all four together
risked attributing a code-version difference to a methodology difference.

Git geçmişi, Csv_3b ve JacksonXml_1b'nin, `$stackN` önemsiz-dilim (trivial
slice) yeniden deneme mekanizmasını (`slicer_runner._jimple_local_candidates`)
ve `ExceptionSite`/`criterion_kind` yedek mekanizmasını ekleyen `3ecfc93`
commit'inden *önce*, 2026-08-07 tarihinde `b1457e1` commit'i altında
çalıştırıldığını gösterdi. Csv_13b ve JacksonXml_6b ise bu düzeltmeden
*sonra* çalıştırılmıştı. Bu nedenle dört hedef doğrudan karşılaştırılabilir
değildi — dördünü birlikte karşılaştırarak çıkarılacak herhangi bir sonuç,
bir kod-sürümü farkını bir metodoloji farkı olarak yanlış yorumlama riski
taşıyordu.

**Effect / Etki:** confirmed directly. Re-running Csv_3b under the retry
mechanism alone (no other change) flipped its slice matrix from
`fail_side_empty=True` (every `Virtual_Fail` column covering zero statements,
all 176 ranked statements tied at Ochiai=0.0 — a tie-break artifact, not a
real ranking) to `fail_side_empty=False`, with real `CSVLexer.java` statements
now entering the ranking (e.g. `CSVLexer.java:169` at a genuine rank-1 tie).
JacksonXml_1b was unchanged by the re-run (SBFL top_rank=1/AP=0.6717, Hybrid
top_rank=125/AP=0.0, identical before and after) — expected, since its seed
variables (`result`, `svc`, `del`) are directly-declared locals that never
needed the retry mechanism in the first place.

Doğrudan doğrulandı. Csv_3b'yi yalnızca yeniden deneme mekanizması ile
(başka hiçbir değişiklik olmadan) yeniden çalıştırmak, dilim matrisini
`fail_side_empty=True` durumundan (her `Virtual_Fail` sütunu sıfır ifade
kapsıyor, sıralanan 176 ifadenin tamamı Ochiai=0.0'da berabere — gerçek bir
sıralama değil, bir eşitlik-bozma (tie-break) yapay sonucu) `fail_side_empty=False`
durumuna çevirdi; artık gerçek `CSVLexer.java` ifadeleri sıralamaya giriyor
(ör. `CSVLexer.java:169`, gerçek bir 1. sıra eşitliğinde). JacksonXml_1b bu
yeniden çalıştırmadan etkilenmedi (SBFL en iyi sıra=1/AP=0,6717, Hybrid en
iyi sıra=125/AP=0,0, öncesi ve sonrası aynı) — beklenen bir sonuçtu, çünkü
onun tohum (seed) değişkenleri (`result`, `svc`, `del`) doğrudan tanımlanmış
yerel değişkenlerdir ve zaten hiçbir zaman yeniden deneme mekanizmasına
ihtiyaç duymamıştı.

**No code change** — this step is a re-execution only. — **Kod değişikliği
yok** — bu adım yalnızca yeniden çalıştırmadır.

---

## Step 2 — Ground-truth answerability classifier
## Adım 2 — Gerçek-değer (ground-truth) cevaplanabilirlik sınıflandırıcısı

**Cause / Neden:** JacksonXml-6's official Defects4J patch is a pure-deletion
hunk: `ToXmlGenerator.writeBinary(Base64Variant, InputStream, int)` and its
two helper methods are entirely absent from the buggy checkout. `ground_truth.py`'s
existing pure-deletion fallback anchors such a hunk to the nearest surviving
context line — but for this bug those anchor lines (843-851, 866-867) turned
out, on direct inspection of the checked-out source, to be orphaned comments
and blank lines left over from the deleted method body: not executable
statements at all. The actual runtime exception
(`UnsupportedOperationException` in `GeneratorBase.writeBinary`) fires inside
`jackson-core`, a dependency jar outside `dir.src.classes` — out of scope for
this pipeline's instrumentation by design. No line-level technique, SBFL or
slicing, could ever rank these specific lines, regardless of its quality.

JacksonXml-6'nın resmi Defects4J yaması saf bir silme (pure-deletion) hunk'ıdır:
`ToXmlGenerator.writeBinary(Base64Variant, InputStream, int)` ve onun iki
yardımcı metodu, hatalı (buggy) checkout'ta tamamen yoktur. `ground_truth.py`'nin
mevcut saf-silme yedek mekanizması böyle bir hunk'ı en yakın hayatta kalan
bağlam (context) satırına sabitler — ancak bu hata için bu sabitleme
satırlarının (843-851, 866-867), checkout edilmiş kaynak kod doğrudan
incelendiğinde, silinen metod gövdesinden geriye kalan sahipsiz yorumlar ve
boş satırlar olduğu ortaya çıktı: bunlar hiç çalıştırılabilir ifade değil.
Gerçek çalışma zamanı istisnası (`GeneratorBase.writeBinary` içindeki
`UnsupportedOperationException`), `dir.src.classes` dışında bir bağımlılık
jar'ı olan `jackson-core` içinde ateşleniyor — bu, tasarım gereği bu
pipeline'ın enstrümantasyonunun kapsamı dışındadır. Kalitesi ne olursa olsun,
hiçbir satır-seviyesi teknik (SBFL veya dilimleme) bu spesifik satırları asla
sıralayamaz.

**Effect / Etki:** without a flag distinguishing this, JacksonXml-6 silently
counted as "both SBFL and Hybrid failed to find the bug" in any aggregate
score, for a reason that has nothing to do with either technique's quality —
a ground-truth representation problem being misread as a technique failure.

Bunu ayırt eden bir işaret olmadan, JacksonXml-6, herhangi bir toplu puanda
sessizce "hem SBFL hem de Hybrid hatayı bulamadı" olarak sayılıyordu; bu da
hiçbir tekniğin kalitesiyle ilgisi olmayan bir nedenden kaynaklanıyordu — bir
gerçek-değer (ground-truth) temsil sorunu, bir teknik başarısızlığı olarak
yanlış okunuyordu.

**Fix implemented / Uygulanan düzeltme:** `ground_truth.classify_answerability`
marks a fault row unanswerable only when it is an approximate (pure-deletion)
anchor **and** its line never executed in *any* test, per the trace matrix's
full statement universe (the broadest "did this ever run" signal the
pipeline computes) — never for a genuine `+`-edited line, which always keeps
counting normally. Per-bug results are written to
`step4_ranking/ground_truth_answerability.csv` and a new, separate
`rq0_answerability.csv` (`Bug_Fully_Unanswerable` column) — deliberately
without touching `rq1.csv`-`rq5.csv`'s existing schemas. `ranking_summary.md`
now states `Ground_Truth_Answerable` up front. **Explicitly not implemented**:
substituting a "nearest call site" as a replacement ground-truth line for
unanswerable bugs — evaluated and rejected as under-specified, unstable
across different failing tests of the same bug, and conflating crash-site
localization with root-cause fault localization.

`ground_truth.classify_answerability`, bir hata satırını yalnızca hem
yaklaşık (saf-silme) bir sabitleme noktasıysa **hem de** satırı iz (trace)
matrisinin tam ifade evrenine göre (pipeline'ın hesapladığı en geniş "bu hiç
çalıştı mı" sinyali) *hiçbir* testte çalıştırılmamışsa cevaplanamaz olarak
işaretler — asla gerçek bir `+` ile düzenlenmiş satır için değil, bu her
zaman normal şekilde sayılmaya devam eder. Hata-bazlı sonuçlar
`step4_ranking/ground_truth_answerability.csv` dosyasına ve yeni, ayrı bir
`rq0_answerability.csv` dosyasına (`Bug_Fully_Unanswerable` sütunu) yazılır —
bilerek `rq1.csv`-`rq5.csv`'nin mevcut şemalarına dokunulmadan.
`ranking_summary.md` artık en başta `Ground_Truth_Answerable` durumunu
belirtiyor. **Kesinlikle uygulanmayan**: cevaplanamayan hatalar için yerine
geçecek bir gerçek-değer satırı olarak "en yakın çağrı noktasını" (call site)
kullanmak — bu değerlendirildi ve reddedildi çünkü yeterince
tanımlanmamıştır, aynı hatanın farklı başarısız testleri arasında kararsızdır
ve çökme-noktası (crash-site) yerelleştirmesini kök-neden hata
yerelleştirmesiyle karıştırır.

**Verified / Doğrulandı:** JacksonXml_6b → `Bug_Fully_Unanswerable=True` (10/10
fault lines - confirmed in the final `rq0_answerability.csv`). Csv_13b →
`Bug_Fully_Unanswerable=False`, 0/2 unanswerable (both lines are genuine live
edits). The classifier also generalized beyond its motivating case: Csv_3b
came back `Bug_Fully_Unanswerable=False` but **2/3** fault lines
unanswerable, and JacksonXml_1b `Bug_Fully_Unanswerable=False` but **1/6**
unanswerable - not whole-method deletions like JacksonXml-6, but pure-deletion
anchors that happened to land on a comment or brace-only line, which
Cobertura/Slicer4J structurally never report a hit for either. The bug-level
flag correctly stays `False` for both, since each still has at least one
genuinely live, coverable fault line counting normally toward RQ4/RQ5 - only
the specific dead anchor lines are excluded from being read as "the
technique missed a findable line."

JacksonXml_6b → `Bug_Fully_Unanswerable=True` (10/10 hata satırı - nihai
`rq0_answerability.csv`'de doğrulandı). Csv_13b → `Bug_Fully_Unanswerable=False`,
0/2 cevaplanamaz (her iki satır da gerçek, canlı düzenlemelerdir).
Sınıflandırıcı, kendisini motive eden durumun ötesine de genelleşti: Csv_3b
`Bug_Fully_Unanswerable=False` olarak döndü ama **3 satırdan 2'si**
cevaplanamazdı; JacksonXml_1b `Bug_Fully_Unanswerable=False` ama **6 satırdan
1'i** cevaplanamazdı - JacksonXml-6 gibi tüm metod silinmesi değil, ama
Cobertura/Slicer4J'nin yapısal olarak asla isabet bildirmediği bir yorum
veya sadece-parantez satırına denk gelen saf-silme sabitleme noktaları. Hata
seviyesindeki işaret her ikisinde de doğru şekilde `False` kalıyor, çünkü her
ikisinin de RQ4/RQ5'e normal şekilde katkıda bulunan en az bir gerçek, canlı,
kapsanabilir hata satırı hâlâ var - yalnızca belirli ölü sabitleme satırları
"teknik bulunabilir bir satırı kaçırdı" olarak okunmaktan hariç tutuluyor.

---

## Step 3 — Statement-level line normalization
## Adım 3 — İfade seviyesinde satır normalizasyonu

**Cause / Neden:** Csv-13's ground truth (from the official patch diff) is
`CSVFormat.java:319` — the line containing
`.withQuote(null).withRecordSeparator(LF);`, the tail of a fluent
builder-chain statement that starts on line 318
(`public static final CSVFormat MYSQL = DEFAULT.withDelimiter(TAB)...`).
javac's bytecode line-number table attributes the *entire* multi-line
statement's `putstatic` instruction to its **first** physical line, 318 — not
319. Both Cobertura (trace matrix) and Slicer4J report hits using that same
bytecode convention. Defects4J's diff-derived ground truth does not — it
reports wherever the literal patch text changed, which can be any physical
line of a multi-line statement. The two sides were therefore not
comparable for any multi-line statement without translating one convention
to the other.

Csv-13'ün gerçek değeri (resmi yama diff'inden), `.withQuote(null).withRecordSeparator(LF);`
satırını içeren `CSVFormat.java:319`'dur; bu, 318. satırda başlayan akıcı
(fluent) bir builder-zinciri ifadesinin (`public static final CSVFormat MYSQL = DEFAULT.withDelimiter(TAB)...`)
kuyruğudur. javac'nin bytecode satır-numarası tablosu, çok satırlı ifadenin
*tamamının* `putstatic` komutunu **ilk** fiziksel satırına, yani 318'e atfeder
— 319'a değil. Hem Cobertura (iz matrisi) hem de Slicer4J isabetleri bu aynı
bytecode kuralına göre bildirir. Defects4J'nin diff'ten türetilen gerçek
değeri ise bunu yapmaz — yamanın metni harfiyen nerede değiştiyse orayı
bildirir, bu da çok satırlı bir ifadenin herhangi bir fiziksel satırı
olabilir. Bu nedenle, iki taraf, bir kuralı diğerine çevirmeden çok satırlı
herhangi bir ifade için karşılaştırılabilir değildi.

**Effect / Etki:** Slicer4J's real hit at `CSVFormat.java:318` — the exact
same logical statement as the ground truth's line 319 — was being scored as
a **miss**, because Step 4's matching compared line numbers exactly.
Csv-13's Hybrid ranking looked meaningfully worse than it actually was for a
pure line-attribution-convention mismatch, not a real localization failure.

Slicer4J'nin `CSVFormat.java:318`'deki gerçek isabeti — gerçek değerin 319.
satırıyla tamamen aynı mantıksal ifade — Adım 4'ün eşleştirmesi satır
numaralarını birebir karşılaştırdığı için bir **kaçırma (miss)** olarak
puanlanıyordu. Csv-13'ün Hybrid sıralaması, gerçek bir yerelleştirme
başarısızlığından değil, saf bir satır-atfetme kuralı uyuşmazlığından dolayı
olduğundan çok daha kötü görünüyordu.

**Fix implemented / Uygulanan düzeltme:** `ground_truth.normalize_statement_line`
walks backward from a diff line while the preceding physical line does not
terminate a statement (doesn't end in `;`, `{`, `}`, or `*/`) and is not
itself blank/a comment — bounded to 10 lines of lookback so a
misidentification can never run away across unrelated code. Every fault row
now carries both the original `line` (kept for display/audit) and a
`statement_line` (used for all matching in `step4_ranking.py` and
`rq_writers._write_rq4`). `ranking_summary.md` shows both, explicitly listing
any line that shifted.

`ground_truth.normalize_statement_line`, bir diff satırından geriye doğru,
önceki fiziksel satır bir ifadeyi sonlandırmadığı sürece (`;`, `{`, `}` veya
`*/` ile bitmiyorsa) ve kendisi boş/bir yorum değilse yürür — yanlış bir
sınır tespitinin ilgisiz kodun içine kaçmaması için 10 satırlık bir geriye
bakış sınırıyla sınırlandırılmıştır. Artık her hata satırı hem orijinal
`line`'ı (görüntüleme/denetim için saklanır) hem de bir `statement_line`'ı
(`step4_ranking.py` ve `rq_writers._write_rq4` içindeki tüm eşleştirmelerde
kullanılır) taşır. `ranking_summary.md`, kayan herhangi bir satırı açıkça
listeleyerek her ikisini de gösterir.

**Verified / Doğrulandı:** `CSVFormat.java:319 -> 318` (Csv-13, the only
shift across all four targets). Regression-checked against Csv-3's
`Lexer.java:111` and Csv-13's own `CSVPrinter.java:139` (both single-line
statements, both confirmed unchanged) and against all of JacksonXml-1's and
JacksonXml-6's fault lines (none are multi-line statement continuations, none
shifted). This normalization alone (no slicing change) moved Csv-13's Hybrid
ranking from top_rank=3/AP=0.0 to top_rank=1/AP=0.5.

`CSVFormat.java:319 -> 318` (Csv-13, dört hedef arasındaki tek kayma). Csv-3'ün
`Lexer.java:111`'ine ve Csv-13'ün kendi `CSVPrinter.java:139`'una karşı
(ikisi de tek satırlı ifadeler, ikisinin de değişmediği doğrulandı) ve
JacksonXml-1 ile JacksonXml-6'nın tüm hata satırlarına karşı (hiçbiri çok
satırlı ifade devamı değil, hiçbiri kaymadı) regresyon kontrolü yapıldı. Tek
başına bu normalizasyon (dilimleme değişikliği olmadan) Csv-13'ün Hybrid
sıralamasını en iyi sıra=3/AP=0,0'dan en iyi sıra=1/AP=0,5'e taşıdı.

---

## Step 4 — Aliasing / heap-tracking retry widening
## Adım 4 — Takma ad (aliasing) / yığın-izleme yeniden deneme genişletmesi

**Cause / Neden:** `slicer_runner.py`'s own docstring already documented that
`-v <source-name>` almost never matches a real Jimple local (Slicer4J
prepends `$`, and Soot only assigns `$`-names to its own synthetic stack
temporaries) — mitigated by retrying with whatever `$stackN` tokens Slicer4J's
own trivial output shows being read/written **on the criterion's own source
line**. Concretely, for Csv-13's `assertEquals(expected, writer.toString())`:
`writer`'s actual content was populated several lines earlier by
`CSVPrinter printer = new CSVPrinter(writer, format); printer.printRecord(s);`
— a *different* local (`printer`), mutating `writer` via aliasing, whose
Jimple temp never appears on the assertion's own line. The existing retry's
candidate pool was therefore structurally blind to this entire pattern,
regardless of how many `$stackN` tokens it tried.

`slicer_runner.py`'nin kendi docstring'i zaten `-v <kaynak-adı>`'nın neredeyse
hiçbir zaman gerçek bir Jimple yerel değişkenle eşleşmediğini belgelemişti
(Slicer4J başına `$` ekler ve Soot yalnızca kendi sentetik yığın geçicilerine
`$` adları atar) — bu, Slicer4J'nin kendi önemsiz (trivial) çıktısının
**kriter satırının kendisinde** okunduğunu/yazıldığını gösterdiği `$stackN`
belirteçleriyle yeniden deneyerek hafifletilmişti. Somut olarak, Csv-13'ün
`assertEquals(expected, writer.toString())` ifadesi için: `writer`'ın gerçek
içeriği birkaç satır önce `CSVPrinter printer = new CSVPrinter(writer, format); printer.printRecord(s);`
ile dolduruluyordu — `writer`'ı takma ad (aliasing) yoluyla değiştiren
*farklı* bir yerel değişken (`printer`); onun Jimple geçicisi asla assertion'ın
kendi satırında görünmüyor. Bu nedenle mevcut yeniden deneme mekanizmasının
aday havuzu, kaç tane `$stackN` belirteci denerse denesin, bu örüntünün
tamamına yapısal olarak kördü.

**Effect / Etki:** Csv-13's slice-based Hybrid matrix had exactly 2
statements total, neither of them from `CSVPrinter.java` — the actual buggy
class, which trace-based SBFL found without difficulty. The hybrid
approach's entire premise (assertion-variable-seeded backward slicing) was
silently failing on precisely the class of test pattern (an object mutated
via a wrapping object, then read back) that is common in this kind of
buffer/printer/parser code.

Csv-13'ün dilim-tabanlı Hybrid matrisinde toplam tam olarak 2 ifade vardı ve
hiçbiri gerçek hatalı sınıf olan, iz-tabanlı SBFL'nin hiç zorlanmadan bulduğu
`CSVPrinter.java`'dan değildi. Hybrid yaklaşımının tüm önermesi (assertion
değişkeniyle tohumlanan geriye doğru dilimleme), tam olarak bu tür
tampon/yazıcı/ayrıştırıcı kodunda yaygın olan test örüntüsü sınıfında (sarmalayıcı
bir nesne aracılığıyla değiştirilen, sonra geri okunan bir nesne) sessizce
başarısız oluyordu.

**Fix implemented / Uygulanan düzeltme:** `java_ast.find_aliasing_seed_candidates`
statically scans the test method's own source, backward from the criterion
line (bounded lookback), for any local that was constructed/assigned from an
expression referencing the seed variable, and finds that local's last
call-receiver use before the criterion line. `step2_slicing.py` runs one
extra Slicer4J criterion per candidate found (bounded by
`ALIAS_SCAN_MAX_CANDIDATES`) and unions whatever it finds into the same
virtual column, deduplicated. All of this is orchestration-only — the same
Slicer4J binary, invoked more times with better-chosen seeds; no tool version
changed.

`java_ast.find_aliasing_seed_candidates`, kriter satırından geriye doğru
(sınırlı bir geriye bakışla) test metodunun kendi kaynak kodunu statik olarak
tarayarak, tohum değişkene atıfta bulunan bir ifadeden inşa edilmiş/atanmış
herhangi bir yerel değişkeni bulur ve o yerel değişkenin kriter satırından
önceki son çağrı-alıcısı (call-receiver) kullanımını tespit eder.
`step2_slicing.py`, bulunan her aday için bir ekstra Slicer4J kriteri
çalıştırır (`ALIAS_SCAN_MAX_CANDIDATES` ile sınırlanmış) ve bulduğu her şeyi
aynı sanal (virtual) sütuna, tekrarları eleyerek birleştirir. Bunların hepsi
yalnızca orkestrasyondur — aynı Slicer4J ikili dosyası, daha iyi seçilmiş
tohumlarla daha fazla kez çağrılır; hiçbir araç sürümü değişmedi.

**What this can and cannot fix, disclosed up front / Bunun neyi düzeltip
neyi düzeltemeyeceği, önceden açıklandı:** Slicer4J's demonstrated
interprocedural reach is a data-flow edge (a return value, or an
argument-to-parameter edge into a called method) — not a heap-mutation edge.
Whether this fix helps a given aliasing pattern depends on what the
candidate's relevant call actually exposes to Slicer4J's own backward walk,
which is empirical, not guaranteed by construction. This was verified, not
assumed, per fixture below.

Slicer4J'nin gösterdiği prosedürler-arası (interprocedural) erişim bir
veri-akışı kenarıdır (bir dönüş değeri veya çağrılan bir metoda argümandan-parametreye
bir kenar) — bir yığın-değiştirme (heap-mutation) kenarı değil. Bu
düzeltmenin belirli bir takma ad örüntüsüne yardımcı olup olmayacağı,
adayın ilgili çağrısının Slicer4J'nin kendi geriye doğru yürüyüşüne gerçekte
neyi açığa çıkardığına bağlıdır; bu, yapı gereği garanti edilen değil,
deneysel bir sonuçtur. Bu, varsayılmadı, aşağıdaki her bir örnek için
doğrulandı.

**Verified / Doğrulandı:**
- **Csv-13 (`writer`/`printer`)**: candidate found (`printer` @ its last
  call-receiver line). The extra criterion **did** reach into `CSVPrinter`'s
  own internals — `CSVPrinter.java:139` (`if (format.isQuoteCharacterSet()) {`),
  the *exact* ground-truth buggy line, now appears in the slice, alongside a
  legitimate dependency chain (`printAndQuote`, `quote = !(object instanceof Number)`,
  `format.isQuoteCharacterSet()`) closely matching what trace-based SBFL
  independently found. Slice universe grew from 2 to 59 statements. Final
  Hybrid ranking: **top_rank=1, AP=0.517** (from top_rank=3, AP=0.0
  originally); RQ4 `Fault_Inclusion_Rate`: **1.0** (from 0.0).
- **Csv-3 (`lexer`)**: **no candidate found** — `lexer` is used directly as
  a call receiver inline inside the assertion (`assertThat(lexer.nextToken(new Token()), ...)`),
  never handed to another local first, so this specific fix does not apply to
  it. Csv-3's remaining gap (fail-side slices reach `CSVLexer.java` but not
  the exact `Lexer.java:111-113` base-class lines) is Step 1's retry
  mechanism at work, not Step 4 — and is left as a disclosed, unfixed
  limitation.
- **JacksonXml-1 / JacksonXml-6**: no aliasing candidates found for either
  (`result`/`svc`/`del` and `xml` are direct assignments, not objects handed
  to a wrapping local) — confirmed no change, as expected; both remain
  exactly as characterized in Steps 1-3 above.

- **Csv-13 (`writer`/`printer`)**: aday bulundu (`printer`, son çağrı-alıcısı
  satırında). Ekstra kriter, `CSVPrinter`'ın kendi iç yapısına gerçekten
  ulaştı — tam olarak gerçek-değer hatalı satırı olan
  `CSVPrinter.java:139` (`if (format.isQuoteCharacterSet()) {`), artık
  dilimde görünüyor; iz-tabanlı SBFL'nin bağımsız olarak bulduğuyla yakından
  eşleşen meşru bir bağımlılık zincirinin (`printAndQuote`,
  `quote = !(object instanceof Number)`, `format.isQuoteCharacterSet()`)
  yanı sıra. Dilim evreni 2'den 59 ifadeye büyüdü. Nihai Hybrid sıralaması:
  **en iyi sıra=1, AP=0,517** (başlangıçtaki en iyi sıra=3, AP=0,0'dan);
  RQ4 `Fault_Inclusion_Rate`: **1,0** (0,0'dan).
- **Csv-3 (`lexer`)**: **aday bulunamadı** — `lexer`, assertion'ın içinde
  doğrudan bir çağrı-alıcısı olarak satır içinde kullanılıyor
  (`assertThat(lexer.nextToken(new Token()), ...)`), önce başka bir yerel
  değişkene hiç verilmiyor, bu nedenle bu spesifik düzeltme ona uygulanmıyor.
  Csv-3'ün kalan boşluğu (başarısız-taraf dilimleri `CSVLexer.java`'ya
  ulaşıyor ama tam olarak `Lexer.java:111-113` temel sınıf satırlarına
  ulaşmıyor) Adım 4 değil, Adım 1'in yeniden deneme mekanizmasının işidir —
  ve açıkça belirtilmiş, düzeltilmemiş bir kısıt olarak bırakılmıştır.
- **JacksonXml-1 / JacksonXml-6**: ikisi için de takma ad adayı bulunamadı
  (`result`/`svc`/`del` ve `xml` doğrudan atamalardır, bir sarmalayıcı yerel
  değişkene verilen nesneler değildir) — beklendiği gibi hiçbir değişiklik
  olmadığı doğrulandı; ikisi de yukarıdaki Adım 1-3'te tanımlandığı gibi
  kalmaya devam ediyor.

---

## What remains open (deferred as Step 5) / Neler açık kalıyor (Adım 5 olarak ertelendi)

JacksonXml-1's Virtual_Fail slice (seeded directly and correctly on the real
failing assertion) is substantial (81 statements) and genuinely walks through
`FromXmlParser`, `XmlTokenStream`, and `WrapperHandlingDeserializer` — but
does not reach the exact buggy branch (`FromXmlParser.java:550-553`). The
bug is a wrong branch taken inside a token-stream state machine, causing one
fewer `list.add()` call than expected; backward **data**-dependency slicing
of the (wrong) observed value has no edge encoding "a call that should have
happened one more time but didn't." This is a genuine, real, in-scope
statement (unlike JacksonXml-6's dead comments) — fixable in principle by
deeper interprocedural **control**-dependence propagation, but a
substantially larger undertaking than Steps 1-4, and is deliberately left
open pending evaluation of these results.

JacksonXml-1'in Virtual_Fail dilimi (doğrudan ve doğru şekilde gerçek
başarısız assertion üzerine tohumlanmış) hatırı sayılır büyüklüktedir (81
ifade) ve gerçekten `FromXmlParser`, `XmlTokenStream` ve
`WrapperHandlingDeserializer` içinden geçer — ama tam olarak hatalı dala
(`FromXmlParser.java:550-553`) ulaşmaz. Hata, bir token-stream durum makinesi
içinde alınan yanlış bir daldır ve beklenenden bir eksik `list.add()`
çağrısına neden olur; gözlemlenen (yanlış) değerin geriye doğru **veri**-bağımlılığı
dilimlemesinde, "bir kez daha gerçekleşmesi gerekip de gerçekleşmeyen bir
çağrıyı" kodlayan hiçbir kenar yoktur. Bu (JacksonXml-6'nın ölü yorumlarının
aksine) gerçek, canlı, kapsam-içi bir ifadedir — daha derin
prosedürler-arası **kontrol**-bağımlılığı yayılımıyla ilke olarak
düzeltilebilir, ancak Adım 1-4'ten önemli ölçüde daha büyük bir girişimdir ve
bu sonuçların değerlendirilmesini bekleyerek bilerek açık bırakılmıştır.

---

## Summary of verified numbers / Doğrulanmış sayıların özeti

These are the final, confirmed figures from the single fully-corrected
pipeline run (all 4 targets, Steps 1-4 applied together), read directly from
`resQ_outputs/rq0_answerability.csv`, `rq4.csv`, and `rq5.csv`:

Bunlar, tam düzeltilmiş tek bir pipeline çalıştırmasından (4 hedefin tamamı,
Adım 1-4 birlikte uygulanmış) elde edilen, doğrudan
`resQ_outputs/rq0_answerability.csv`, `rq4.csv` ve `rq5.csv`'den okunan nihai,
doğrulanmış rakamlardır:

| Target | SBFL Top_Rank / AP | Hybrid Top_Rank / AP | RQ4 Fault_Inclusion_Rate | Bug_Fully_Unanswerable |
|---|---|---|---|---|
| Csv_3b | 1 / 0.3333 | 58 / 0.0016 | 0.0 | False (2/3 fault lines unanswerable) |
| Csv_13b | 37 / 0.0158 | **1 / 0.5172** | **1.0** | False (0/2 unanswerable) |
| JacksonXml_1b | 1 / 0.6717 | 125 / 0.0000 | 0.0 | False (1/6 fault lines unanswerable) |
| JacksonXml_6b | 1335 / 0.0000 | 66 / 0.0000 | 0.0 | **True** (10/10 - excluded from primary scoring) |

Before-this-session comparison, where a genuine before/after exists (Csv_13b
and Csv_3b's degenerate-tie fix; JacksonXml_1b and JacksonXml_6b were not
touched by any of Steps 2-4's mechanics, see each step's "Verified" section
above for why):

Bu oturumdan önceki durumla karşılaştırma, gerçek bir öncesi/sonrası
bulunduğu yerlerde (Csv_13b ve Csv_3b'nin yozlaşmış-eşitlik düzeltmesi;
JacksonXml_1b ve JacksonXml_6b, Adım 2-4'ün mekanizmalarından hiçbiri
tarafından etkilenmedi, nedeni için yukarıdaki her adımın "Doğrulandı"
bölümüne bakın):

| Target | Metric | Before | After |
|---|---|---|---|
| Csv_13b | Hybrid Top_Rank / AP | 3 / 0.0000 | **1 / 0.5172** |
| Csv_13b | RQ4 Fault_Inclusion_Rate | 0.0 | **1.0** |
| Csv_3b | Hybrid fail_side_empty | True (degenerate 176-way 0.0 tie) | False (real ranking, still poor) |
| Csv_3b | Hybrid Top_Rank / AP | 1 (tie-break artifact) / 0.0019 | 58 (real ranking) / 0.0016 |
