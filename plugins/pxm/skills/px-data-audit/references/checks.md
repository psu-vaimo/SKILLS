# The check register

75 checks in eleven dimensions. Six are the DAMA UK dimensions, which are the practitioner canon and the
set a client's own data people are most likely to recognise. Five are additions, because the generic six
were written for data of any kind and product information has structure, classification, references, a
multi-source character and a **journey** that they do not reach.

**Nobody runs all 74.** An audit uses the dimensions that are live for this client, the way a workshop
uses eight questions out of fifty-four. Pick by what the client publishes and what the migration has to
carry.

**If you run only one dimension, run `FLOW`.** It needs two files and it answers the question the client
actually has.

## How to read a row

| Column | Means |
|---|---|
| **From** | `export` — computable from the file alone. `+spec` — needs the client's own data specification, attribute list or business rules. `+channel` — needs the destination's published requirements. `referent` — needs comparison against something outside the data. |
| **Default** | A starting threshold so results are comparable between clients and between people. Argue with it; the destination decides the real one. |
| **Evidences** | The `px-analyst` ability this check produces evidence about. Runs both ways — a check that fires is evidence the ability is missing, and an ability the workshop claimed is testable here. |

Definitions below are paraphrased. `references/sources.md` has the verbatim wording and where to get it.

---

## COMPLETE — completeness

*The proportion of stored data against what a complete record would hold.* The dimension everyone starts
with and the one most often reported wrong, because it is quoted without a denominator.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `COMPLETE-01` | Fill rate per attribute against the in-scope denominator | export | state it, always | `QUALITY-01` |
| `COMPLETE-02` | Effective fill rate — null-equivalent values discounted | export | gap >5pp is a finding | `MEASURE-07` |
| `COMPLETE-03` | Fill rate split by lifecycle status | export | always split | `QUALITY-01` |
| `COMPLETE-04` | Fill rate split by category or product type | export | always split | `QUALITY-02` |
| `COMPLETE-05` | Fill rate per locale — which languages are genuinely populated | export | <50% = nominal locale | `MASTER-05` |
| `COMPLETE-06` | Products meeting a stated "ready" definition per destination | +spec | needs a definition to exist | `QUALITY-01` `QUALITY-02` |
| `COMPLETE-07` | Placeholder content — identifier or name copied into a description | export | any occurrence | `MEASURE-07` |
| `COMPLETE-08` | Products with no image at all | export | any, in scope | `ASSETS-20` |
| `COMPLETE-09` | Channel-required attributes unfilled | +channel | zero tolerance | `DELIVER-02` |
| `COMPLETE-10` | Attributes defined in the schema but never populated anywhere | export | any = drop candidate | `MODEL-17` |

*`COMPLETE-03` needs a lifecycle, and the column called status is often not it. In one legacy export the
status field held the same value on 99% of records; the lifecycle was really carried by an expiry date
and a publication flag. **If the status column does not discriminate, look for dates and flags before
declaring the base unsegmentable**, and say which one you used as the denominator. Then cross the
candidates: records expired by one signal and live by another are a `CONSIST-03` finding in their own
right, and they must be resolved before the scope is, because they decide which side of the line a few
hundred thousand records fall on. `STATUS-07` is the ability that is missing.*

*`COMPLETE-06` is the one that usually cannot be run, because no written definition of "ready" exists.
That absence is itself the finding, and it is `QUALITY-01` failing rather than a gap in the audit.
`COMPLETE-02` is the check that carries rule 2 — the gap between fill and effective fill is the evidence
that "the fields are filled" was never the right question.*

---

## VALID — validity

*Conformance to the syntax — format, type, range — of the field's definition.* Everything here is
computable, which makes validity the cheapest real finding in an audit.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `VALID-01` | Type conformance — values match the declared type | +spec | >1% off-type | `QUALITY-11` |
| `VALID-02` | Format conformance — GTIN/EAN check digit, dates, coded identifiers | export | zero tolerance on identifiers | `QUALITY-11` |
| `VALID-03` | Values outside the defined allowed list | +spec | zero tolerance | `QUALITY-11` |
| `VALID-04` | Range plausibility — negative weights, zero dimensions, absurd magnitudes | export | any occurrence | `QUALITY-11` |
| `VALID-05` | Unit carried inside the value rather than in metadata | export | any occurrence | `MODEL-03` |
| `VALID-06` | Mixed decimal separators within one attribute | export | any occurrence | `QUALITY-04` |
| `VALID-07` | Mixed date formats within one attribute | export | any occurrence | `QUALITY-04` |
| `VALID-08` | Control, invisible and non-printing characters, especially in identifiers | export | zero tolerance | `COLLECT-03` |
| `VALID-09` | Leading and trailing whitespace | export | report, low severity | `COLLECT-03` |
| `VALID-10` | Markup where none is expected, or broken markup where it is | export | any occurrence | `QUALITY-11` |
| `VALID-11` | Encoding damage — mojibake, double-encoded characters | export | zero tolerance | `COLLECT-03` |

*`VALID-05` looks cosmetic and is not. A value of `84 kr` or `10 mm` cannot be converted, compared,
range-checked or unit-switched per market, and every downstream consumer has to parse it. It is also one
of the most common reasons an attribute exists several times over — see `STRUCT-03`.*

*`VALID-08` earns its zero tolerance from a live case: one organisation strips hidden and invalid
characters from identifiers on entry, deliberately, because it had been bitten. An invisible character
in an article number breaks every join in the migration and is undetectable by eye.*

---

## UNIQUE — uniqueness

*Nothing is recorded more than once, given how that thing is identified.* The ability model had **no
line about duplicates at all** across nine drafts until a client forced it — expect the same blind spot
in the client's own thinking.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `UNIQUE-01` | Duplicate identifiers within one source | export | zero tolerance | `QUALITY-12` |
| `UNIQUE-02` | The same product under two identifiers — near-duplicate on name and attributes | export | any cluster | `QUALITY-12` |
| `UNIQUE-03` | The same GTIN on products that are not the same thing | export | zero tolerance | `QUALITY-12` |
| `UNIQUE-04` | The same asset file registered more than once | export | report | `ASSETS-10` |
| `UNIQUE-05` | Identifier reuse — a retired code reassigned to something else | export | zero tolerance | `MODEL-19` |

*`UNIQUE-02` needs a stated definition of what counts as a duplicate before it can be run, and the
client usually does not have one. Propose one from the data, get it agreed, then measure — the
definition is a deliverable in its own right.*

*`UNIQUE-05` is one of the two checks that can settle `MODEL-19` by measurement. See the SKILL note on
what the audit can settle that a room cannot.*

---

## CONSIST — consistency

*The absence of difference when comparing two or more representations of the same thing.* Within a
record, within an attribute, and between records — cross-**source** consistency is `CROSS` below.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `CONSIST-01` | Case and whitespace variants of one value | export | any occurrence | `QUALITY-04` |
| `CONSIST-02` | Synonym variants of one value, including across languages in one field | export | any occurrence | `QUALITY-04` |
| `CONSIST-03` | Internal contradiction in a record — net weight above gross, variant outside parent range | export | zero tolerance | `QUALITY-11` |
| `CONSIST-04` | Adherence to a stated naming convention | +spec | >5% off-convention | `QUALITY-08` |
| `CONSIST-05` | The same fact held in two attributes that disagree | export | any occurrence | `QUALITY-13` |
| `CONSIST-06` | Value distribution differing sharply between segments with no business reason | export | judgement | `MEASURE-07` |

*`CONSIST-01` is where a controlled list is quietly proven necessary. Three distinct values that
normalise to one mean the attribute is free text pretending to be an enumeration, and `QUALITY-11` is
the ability that fixes it.*

---

## TIME — timeliness

*The degree to which the data represents reality at the point in time it is needed.* Cheap to check,
routinely skipped, and it invalidates conclusions rather than merely adding to them.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `TIME-01` | Extract date per source, and its age at the date of the audit | export | >3 months = flag | — |
| `TIME-02` | Last-modified distribution — how much has not been touched in years | export | report the tail | `QUALITY-05` |
| `TIME-03` | Snapshot divergence — sources extracted on different dates | export | any gap >7 days | `COLLECT-05` |
| `TIME-04` | References to superseded standards, regulations or schema versions | +spec | any occurrence | `MASTER-04` |

*`TIME-01` is a gate, not a finding. An extract four years old describes a system that no longer exists,
and every number derived from it inherits that. One audit found a compliance master dated four years
before the engagement; the correct output was "refresh this before anyone relies on it", not a quality
score.*

---

## STRUCT — structure and model fit

**Not a DAMA dimension.** How the information is organised, as opposed to whether the values are any
good. This is where the findings that change an implementation estimate live.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `STRUCT-01` | Attribute count in total, and attributes per family | export | report | `MODEL-01` |
| `STRUCT-02` | Family coverage — how many products sit on a generic catch-all template | export | >50% on one = finding | `MODEL-01` `MODEL-02` |
| `STRUCT-03` | Attribute proliferation — one concept split by unit or language | export | any cluster | `MODEL-03` |
| `STRUCT-04` | Low-usage attributes | export | <5% in scope | `MODEL-17` |
| `STRUCT-05` | Constant attributes — one value across the whole base | export | any occurrence | `MODEL-17` |
| `STRUCT-06` | Free text where a controlled list is implied by the distribution | export | judgement | `QUALITY-11` |
| `STRUCT-07` | Multi-value encoding — delimiters inside single cells | export | any occurrence | `MODEL-13` |
| `STRUCT-08` | Variant structure — axes present, explicit or implied by naming | export | judgement | `MODEL-04` `MODEL-12` |
| `STRUCT-09` | Which attributes are localisable and scopable, and whether the split is right | export | judgement | `MODEL-12` `MODEL-08` |
| `STRUCT-10` | Attributes whose only name is an opaque system code | export | report count | `MODEL-17` |
| `STRUCT-11` | Overloaded enumerations — one coded field carrying several concepts at once (type, assortment, lifecycle, workflow) | export | any occurrence | `STATUS-02` |

*`STRUCT-02` is the check that makes a completeness number honest. Where one generic template carries
most of the catalogue, nothing is required of anything, so completeness has no reference to measure
against and the client's own "we're at 80%" means nothing. One engagement ran effectively a single
family across most products and estimated ~250 as a realistic target — a gap that is the implementation.*

*`STRUCT-03` is the highest-yield check in the register. One organisation held 2,650–3,600 distinct
attribute values including many separate `length` variants for mm, cm and m. Each of those is one
concept that a migration must merge, a decision someone has to make, and an attribute the new system
must not recreate. The profiler clusters names differing only by a unit or language suffix; the
judgement about whether a cluster is one concept or several is yours.*

*`STRUCT-10` is a migration risk before it is a quality problem. A field whose only documentation is a
four-letter code cannot be migrated with intent, because nobody can say whether it matters. Count them
and put the list in front of the client — this is the second check that can settle `MODEL-19`, since
identifier structure is visible here.*

*`STRUCT-11` hides in plain sight because each value reads fine on its own. The tell is in the value
list: values that are concatenations of two or three ideas (*web assortment + timber + discontinued*),
combinations missing from the list, and a "type" field that changes when a product is discontinued. Each
concept needs its own field in the new model, and the old values must be split by rule with review —
merging them back into one is how the next system ends up with the same field.*

---

## CLASS — classification conformance

**Not a DAMA dimension.** Whether products are classified, how deeply, and whether the classification is
one that carries meaning.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `CLASS-01` | Coverage — products with a class assigned | export | <90% in scope = finding | `DELIVER-13` |
| `CLASS-02` | Depth — assigned to a leaf or stranded on an intermediate node | export | any non-leaf | `DELIVER-13` |
| `CLASS-03` | Feature population per class against the standard's expected set | +spec | <70% = finding | `DELIVER-13` |
| `CLASS-04` | Distinct classes in use against those available | export | report | `MODEL-09` |
| `CLASS-05` | Taxonomy fitness — is the tree one built for another purpose | export | judgement | `MODEL-01` |
| `CLASS-06` | Products in more than one tree, and whether the trees agree | export | any disagreement | `MODEL-09` |

*`CLASS-05` is a diagnostic, not a measurement, and it fires often. A tree built for industry statistics,
accounting or warehouse layout will be structurally fine and functionally useless as a product
taxonomy — customers do not shop by statistics code. Two signals: the tree's own name gives away its
origin, and the leaf nodes group things that are alike to an accountant rather than to a buyer. A
classification carrying no attributes at all cannot serve as the client's attribute model, however
neatly it organises the catalogue.*

*`CLASS-03` is the difference between classified and enriched. Assigning a class creates empty feature
slots; populating them is a separate act that someone has to do, and the count of defined-but-never-
populated features is the size of that job. One organisation had 84 such features across its schema.*

---

## REF — resolvability

**Not a DAMA dimension.** Whether the pointers in the data point at anything. Broken references survive
profiling untouched — every fill rate can be perfect while nothing resolves — and they are the most
common cause of an ugly go-live.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `REF-01` | Asset references that resolve to an actual file | +spec | zero tolerance | `ASSETS-16` |
| `REF-02` | Relationship references that resolve to an existing product | export | zero tolerance | `MODEL-07` |
| `REF-03` | Category references that resolve to a node in the tree | export | zero tolerance | `QUALITY-16` |
| `REF-04` | Variant references that resolve to a parent, and parents with no variants | export | zero tolerance | `MODEL-04` |
| `REF-05` | Orphans — records nothing points at | export | report | `QUALITY-16` |
| `REF-06` | References into a system that is not in the migration scope | export | any occurrence | `QUALITY-16` |

*`REF-01` is where an asset audit actually begins. A numeric asset identifier that only resolves inside
a system nobody is migrating is not a reference, it is a broken link waiting for go-live —
`ASSETS-16` is precisely the ability of knowing whether you hold the file or only a pointer to it.*

*`REF-06` is the check people skip and then discover at cutover. Where archived or inactive records are
excluded from migration, everything pointing at them breaks: one engagement found that archived articles'
linked images and compliance documents would simply stay in the legacy system unless a link was
preserved by hand. `QUALITY-16` — knowing what breaks when something is removed — is the ability, and
Delete is the verb everyone skips.*

---

## CROSS — across sources

**Not a DAMA dimension.** Everything above measures one file. This measures the set, and it is the only
place the golden-record question can actually be answered with evidence.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `CROSS-01` | The common key, and what it is called in each source | export | must exist | `COLLECT-10` |
| `CROSS-02` | Record overlap — which source holds which products | export | report matrix | `MASTER-01` |
| `CROSS-03` | Field overlap — how much vocabulary the sources share | export | report % | `MASTER-06` |
| `CROSS-04` | Value conflict — the same field, same product, different answer | export | any occurrence | `QUALITY-13` |
| `CROSS-05` | Which source is authoritative per field, stated or inferred | +spec | must be stated | `MASTER-06` |
| `CROSS-06` | Data held in exactly one source, and therefore load-bearing | export | report list | `MASTER-02` |

*`CROSS-01` is the first thing to establish and it is rarely clean. One engagement's five files called
the same article number `ITNO`, `Artikelnummer`, `Art nr` and `ESSVE Art.nr`. Until the key is agreed
nothing else can be joined, and a key that has four names is a finding about `COLLECT-10` before it is
an inconvenience.*

*Two traps worth checking before the key is agreed. **A key may be derived, not stored** — a system field
that renders one identifier when it exists and falls back to a composite when it does not. Decompose it
by branch and count each, because the fallback branches are exactly the records that will not join to
the system of record; a placeholder such as `MISSING-MISSING` on other record types is the tell. **A
field that looks like the article number may be the supplier's** — unique per supplier, duplicated across
them. Test uniqueness before trusting the name (`UNIQUE-01`): in one export, 465,000 values of the
obvious-looking key sat on more than one article.*

*`CROSS-03` reads in two directions and both are useful. **Low overlap** means the sources are
complementary rather than redundant — none can be dropped, and the migration must merge all of them.
**High overlap** means the same fact is held more than once and something must decide which wins, which
is `QUALITY-13` and needs a person, not a rule. In one inventory, 776 of 848 distinct fields appeared in
only one source: nothing was redundant and every file was load-bearing.*

*`CROSS-04` is the check that turns a governance conversation from opinion into evidence. "Which system
wins?" is unanswerable in the abstract and obvious once you can say how often they disagree and about
what.*

---

## FLOW — what survives the journey

**Not a DAMA dimension, and the highest-yield one in the register.** `CROSS` treats sources
symmetrically. This one has a direction — from the system of record to what the customer actually
sees — and direction changes the meaning of every finding. A field missing at the destination and a
field missing at the source are opposite problems.

Two files are enough to run it: **the main source system, usually an ERP, and the main destination,
usually the webshop.**

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `FLOW-01` | Fields present at source that never arrive at the destination | export | any, list them | `ENRICH-04` |
| `FLOW-02` | Fields present at the destination that exist in no source | export | any, list them | `PRESENT-07` |
| `FLOW-03` | Values that differ between source and destination for the same product | export | any occurrence | `COLLECT-05` |
| `FLOW-04` | Products at source that are never published | export | report and ask why | `DELIVER-01` |
| `FLOW-05` | Products at the destination that exist in no source | export | any occurrence | `MASTER-01` |
| `FLOW-06` | Enrichment share — how much of what the customer sees originates outside any system of record | export | report as % of fields | `ENRICH-08` |

*`FLOW-02` and `FLOW-06` are the point of the dimension. **Everything the customer sees that the source
system does not hold was produced by a process, and that process is usually undocumented** — a
spreadsheet, an agency, a person typing into the shop admin, copy written once and pasted forever. The
size of that gap is the size of the work the client is not counting, and it is the strongest available
evidence for `PRESENT-07` and for the whole `ENRICH` domain.*

*This is the same shape as the asset diagnostic: it fires on evidence, not on complaints, because
nobody complains about work they have always done by hand. Expect the client to be surprised by the
number, and expect the number to be larger than anyone in the room guesses.*

*`FLOW-01` is the quieter half and it changes migration scope. A field maintained in the ERP that never
reaches a customer is either dead weight somebody is still keeping current, or a genuine gap in the
integration. Both are findings; they have opposite remedies, and only the client can say which it is.*

*`FLOW-05` finds the shadow catalogue — products that exist only where they are sold. It is where
`MASTER-01` fails in practice rather than in principle, and those records are the ones that get
forgotten at migration because no system of record lists them.*

---

## ACCURATE — accuracy

*The degree to which the data correctly describes the real-world thing.* **Not computable from an
export.** Every check here needs a referent, and the fourth is the honest option when there is no budget
for the first three.

| ID | Check | From | Default | Evidences |
|---|---|---|---|---|
| `ACCURATE-01` | Sample against the physical product | referent | n≥30, stated | `MEASURE-07` |
| `ACCURATE-02` | Sample against the supplier's own datasheet | referent | n≥30, stated | `COLLECT-03` |
| `ACCURATE-03` | Sample against what is currently published | referent | n≥30, stated | `MASTER-01` |
| `ACCURATE-04` | Declared unmeasured, with the reason and the consequence | — | the default | — |

*GS1 defines product data accuracy as conformity with physically observable characteristics of the trade
item, and separates the attributes where an error is fundamental — brand, net content, pack quantity,
the identifier itself — from those where it is merely wrong. Sample the fundamental ones first if
sampling at all.*

*`ACCURATE-04` is not a failure. A stated "we did not measure accuracy, here is what that means for the
verdict" is professional; a clean profile presented as though it proved accuracy is not. State it in the
report, in the same place the Happy Flow states what it did not prove.*

---

## Running the checks

`scripts/profile_export.py` computes most of `COMPLETE`, `VALID`, `STRUCT`, `UNIQUE-01` and the
`CROSS` overlap measures directly:

```bash
python3 scripts/profile_export.py FILE [FILE...] \
    --out DIR --key ARTICLE_NUMBER --scope STATUS=20 --segment STATUS --multi-delim ';;;'
```

`--scope` sets the denominator and is the flag that enforces rule 1. `--segment` splits fill rates so
the two populations stay visible. It writes `profile.md` for reading and `profile.json` for tracing a
number back to its file.

Everything the script cannot compute needs either the client's specification, the destination's
requirements, or a referent — which is exactly the boundary between what an audit can assert and what it
must ask for.
