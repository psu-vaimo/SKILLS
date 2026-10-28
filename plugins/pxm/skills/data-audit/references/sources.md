# Sources

Graded, because an audit gets argued with and the citation is what settles it. **Check the grade before
quoting a number to a client.**

| Grade | Means |
|---|---|
| **Standard** | A standards body or chartered institution. Cite freely. |
| **Canon** | Practitioner reference work. Cite as established practice, not as law. |
| **Vendor** | Commissioned by someone selling a product. Usable for framing a business case, never as evidence. |
| **Unsubstantiated** | Widely repeated, no primary source found. Do not cite. |

---

## The dimension frameworks

**DAMA UK — *The Six Primary Dimensions for Data Quality Assessment* (2013).** *Standard.*
The set to anchor on. Completeness · Uniqueness · Timeliness · Validity · Accuracy · Consistency, each
with a definition, a reference, a measure, a scope, a unit and worked pseudo-code. The canonical copy is
member-gated; a full public PDF is at
`https://files.fluxicon.com/Cafe/The-Six-Primary-Dimensions-for-Data-Quality-Assessment.pdf`

**The per-dimension table schema is the reusable part**, more than the six words: Title · Definition ·
Reference · Measure · Scope · Unit of Measure · Type of Measure · Related dimension · Optionality ·
Example · Pseudo-code. A rule register built on those columns is one a client can audit you on.

It also states plainly that **accuracy cannot be assessed from the data alone** — which is where rule 3
comes from, and the professional cover for either scoping accuracy out or pricing a physical audit in.
Its seven-step approach (identify critical data items → select dimensions and weights → define good and
bad ranges → apply → review → remediate → repeat) is a defensible spine for the whole exercise.

**ISO 8000-8:2015 — syntactic, semantic and pragmatic quality.** *Standard.*
The best framing device in the whole reading list, and the clearest way to say "filled is not the same
as good" to a client: syntactic conformance is proven by verification, semantic correspondence to the
concept by verification, pragmatic fitness for a purpose only by validation. Free preview:
`https://cdn.standards.iteh.ai/samples/60805/be8fc414189e4e4b8383282034f68746/ISO-8000-8-2015.pdf`

Use it in the narrative, not as the measurement backbone. **ISO 8000-110** requires master data to carry
semantic encoding resolvable to a data dictionary — the justification for demanding a specification
before auditing. ECCMA stewards much of the series; treat ECCMA's own material as advocacy.

**ISO/IEC 25012:2008.** *Standard.* Fifteen characteristics, split **inherent** (accuracy,
completeness, consistency, credibility, currentness) from **system-dependent** (availability,
portability, recoverability), with a middle group that is both. That split is genuinely useful for a PIM
audit: inherent is the product content, system-dependent is what the stack does to it — and only the
first survives a migration. Paywalled; summary at `https://iso25000.com`.

**DAMA DMBOK2 chapter 13.** *Canon.* Nine dimensions, and it says openly that its list is one of
several competing sets — useful when a client's data team arrives with a different one. Chapter 8
justifies profiling before mapping.

**Danette McGilvray, *Ten Steps to Quality Data* (2nd ed., 2021).** *Canon.* The better practitioner fit
for product data: her dimensions include Data Specifications, Data Coverage, Presentation Quality and
Transactability, which reach attribute schemas, catalogue coverage and whether the customer can actually
buy — things the generic six do not.

**DAMA NL — *How to Select the Right Dimensions of Data Quality* (2020).** *Canon.* Catalogues sixty
dimensions with a four-step selection procedure. Its value is not the sixty; it is that it makes
*choosing* six a defensible act rather than an arbitrary one.
`https://dama-nl.org/wp-content/uploads/2020/11/How-to-Select-the-Right-Dimensions-of-Data-Quality-v1.1-d.d.-14-Nov-2020.pdf`

---

## Profiling

**Abedjan, Golab & Naumann — *Profiling relational data: a survey*, The VLDB Journal 24(4) (2015).**
*Canon (peer-reviewed).* The academic taxonomy: single-column (cardinalities, patterns, type inference,
value distributions), multi-column (correlations, outliers), and dependency discovery (unique column
combinations → key candidates; inclusion dependencies → foreign keys).

**The dependency layer is the part worth reading**, because in a PIM it is what exposes broken
variant→parent, product→category and product→asset relationships — the `REF` dimension. The
"structure / content / relationship discovery" framing common in vendor material maps onto this but is
analyst marketing; cite Abedjan.

---

## Product-data-specific

**GS1 GDSN Data Quality Metric Report User Guide (2023).** *Standard.* The most directly copyable thing
found anywhere: someone has already designed the per-attribute product-data scorecard. Columns are
attribute · number of items · number complete · % complete · values with no errors · values with errors
(hard — data will not flow) · values with warnings · % accurate · extract date, subtotalled by category.
`https://www.gs1.org/docs/gdsn/support/data-quality-accuracy-and-completeness-user-guide.pdf`

Note how it defines the two words: **completeness is populated-or-not; accuracy is conformity to the
standard's validation rules.** That is a narrower sense of accuracy than DAMA's, and worth being explicit
about which one a report means.

**GS1 Data Quality Framework — Brand Owners (2015).** *Standard.* Defines product data accuracy as
conformity with **physically observable** characteristics of the trade item, and separates *Foundational*
attributes — brand name, net content, pack quantity, the identifier — from *Fundamental* ones such as
dimensions and weight. Sample the foundational ones first.
`https://www.gs1.org/sites/default/files/docs/gs1_dataquality_bestpractice_framework_brandowners.pdf`

**GS1 Global Data Model.** *Standard.* Four layers — Global Core, Global Category, Regional, Local. The
layering is the bit to borrow: it gives an attribute gross list a built-in prioritisation instead of a
flat dump. GS1 publishes an attribute analysis tool that is itself a gap-analysis instrument.

**GDSN validation rules** are machine-readable and downloadable from `https://navigator.gs1.org/gdsn/`,
so real rules can be run against a client export on day one. The rule anatomy — rule ID, structured
`if/then` statement, business-friendly error message, prerequisite and impacted attributes, pass and
fail examples — is a template worth adopting for client-specific rules even where GDSN does not apply.

**Classification standards.** *Standard.*
- **ETIM** — class → feature → value → unit, typed and multilingual. Gives a per-class expected feature
  list, which makes "% of expected features populated" a defensible completeness measure in electrical,
  HVAC and building.
- **eCl@ss** — four-level hierarchy, ~48,000 classes, >23,000 properties.
- **UNSPSC** — segment/family/class/commodity, and it **carries no attributes at all.** A client using
  it as their attribute model is `CLASS-05` firing.
- **GPC** — brick-level attributes, drives Global Data Model applicability.

**Channel specifications as thresholds.** *Standard, in effect.* Google Merchant Center's product data
specification and Amazon's style guides impose required fields, length limits and image rules. They are
objective bars a client cannot argue with, because they are not yours. Use them for `COMPLETE-09`.

---

## Migration

**John Morris, *Practical Data Migration* (PDMv2), BCS.** *Standard (chartered body).* The only
independent published migration methodology. Two workstreams, nine modules; the three that matter here
are **Landscape Analysis** (time-boxed profiling and discovery, deliberately not planned in advance),
**Gap Analysis & Mapping**, and **Data Quality Rules** — where the rule register is described as the
glue holding the technical and business streams together. Progress is tracked as **Migration
Readiness**, which is the same idea as the readiness verdict.

Its principles are worth quoting to a client directly: business first, engage the experts, fit-for-purpose
quality, measure everything — and **no organisation wants, needs or will pay for perfect quality data.**
Free citable statement: `https://www.bcs.org/articles-opinion-and-research/data-migration-better-than-planning`

**Microsoft Success by Design** — *Canon.* Useful for one distinction it makes cleanly: **configuration
data** (taxonomy, attribute sets) versus **migration data** (the records). That separation is stage 5's
two action lists.

**On the migration failure statistic — correct the record.** The primary source is Bloor Research, *Data
Migration*, Philip Howard, 2007, and it says **more than 60%** of migration projects overrun on time
and/or budget. The 80% and 84% figures in wide circulation are not in it and could not be substantiated.
Cite 60%, and note that the Bloor paper was vendor-sponsored.

---

## The business case — handle with care

**Nearly every "better content sells more" number in circulation is a vendor-commissioned
stated-preference survey.** People reporting what they think they would do is not evidence of what they
do. Salsify, 1WorldSync, Akeneo, inriver and Shotfarm have all published such studies; use them to frame
a conversation, never to support a claim of causation, and say what they are.

**The exception worth citing: GS1 UK (2018).** *Standard.* A record-level comparison of supplier-held
against retailer-held product data found inconsistency in **over 80% of cases**, with poor data
management costing grocery suppliers up to **£21bn a year**. It compares actual records rather than
asking people questions, which makes it methodologically far stronger than the rest.
`https://www.gs1uk.org/insights/press-releases/28022018-poor-data-management-costing-grocery-suppliers-up-to-21bn-each-year`

**Unsubstantiated — do not cite.** The frequently second-hand GS1 US / Nielsen product-content study.
No primary source was found for it.

---

## What no source provides

There is **no published model for estimating cleansing effort.** The nearest structure is the ONC/CMS
PDDQ Framework, which prioritises by cost of fix, level of effort, business impact and benefit. The
four-way triage in `method.md` — automatic, rule with review, human, absent at source — is original,
and defensible as an extension of Morris's defect triage plus PDDQ's effort and impact axes. Present it
as method, not as citation.
