# Sources

Modelling-specific citations. For data *quality* dimensions, profiling and migration practice, use
`px-data-audit/references/sources.md` instead — that file is not duplicated here.

| Grade | Means |
|---|---|
| **Standard** | A standards body. Cite freely. |
| **Practitioner** | A recognised reference work. Cite as established practice. |
| **Vendor** | Platform documentation. Accurate about that platform, opinionated about modelling. |
| **Unverified** | Real and relevant, but a specific claim below could not be confirmed. Check before quoting. |

---

## What makes something a different product

**GS1 GTIN Management Standard, Release 1.1 (2023).** *Standard.*
`https://ref.gs1.org/standards/gtin-management/` — the decision tool at `gs1.org/1/gtinrules/` is
generated from it. **The single most useful external authority in this whole skill**, because it is a
ratified answer to a question clients argue about endlessly.

Three guiding principles — at least one must apply for a new identifier to be required: would a consumer
or trading partner be expected to distinguish it; is there a regulatory or liability disclosure
requirement; is there substantial supply-chain impact. Ten rules follow, with a base-unit versus
higher-level matrix. The ones that come up most: **any** change to declared net content; a dimensional
or gross weight change **over 20% on any axis**; adding or removing a certification mark; a primary
brand change; price printed on the pack.

Three details worth carrying into a workshop. **Each style × colour × size is a distinct trade item**
with its own identifier. **An English-only pack and a Spanish-only pack are two products, not a
translation.** And the standard names cumulative sub-20% changes made to avoid the rule as unacceptable
practice, which is useful when a client proposes exactly that.

It is explicitly a **minimum** — local regulation supersedes it and brand owners may go further.

**GDSN Trade Item Implementation Guide.** *Standard.* Packaging levels each carry their own identifier,
linked parent to child, with unit descriptors from base unit up to pallet. **The modelling lesson is the
role flags** — is it a base unit, a consumer unit, an orderable unit, a despatch unit, an invoice unit —
carried as independent booleans rather than as one product-type enum. Borrow that shape for `UNIT`.

**schema.org `ProductGroup`.** *Standard.* `https://schema.org/ProductGroup`. A group of products
varying "only in certain well-described ways"; the group is a template and **is not itself sold**.
`hasVariant` / `isVariantOf`, and **`variesBy`** — the published way to declare variant axes explicitly.

**Google Merchant Center `item_group_id`.** *Vendor, but effectively a rule.*
`https://support.google.com/merchants/answer/6324507`. Items belong to one group **only if the customer
can select between them on a single landing page** — the criterion behind `VARY-01`. Its
counter-examples are the useful part: a suit sold as jacket plus trousers, or a set of bath accessories,
are *not* variants.

---

## Attribute definition and governance

**IEC 61360-2 / ISO 13584-42.** *Standard.* One harmonised formal model, and the conceptual backbone
under eCl@ss. The load-bearing ideas: every element carries a globally unique, **versioned** identifier
(IRDI), **property definitions live independently of the classes that use them**, and class-to-property
assignment is a separate governed act. A property *type* has a definition, data type, unit and value
domain but **no value**; the value belongs to the instance.

That type/instance split is the same pattern as Fowler's knowledge level versus operational level, and
Hay's PRODUCT TYPE versus product instance. **It is the most useful single idea for PIM architecture**:
attribute definition and attribute value are different objects with different lifecycles and different
owners.

**eCl@ss.** *Standard.* `https://eclass.eu`. Monohierarchical, fixed four levels. Two mechanisms worth
stealing even off-platform: **Depending Properties** — a property valid only when another property holds
a given value, which is real conditional-attribute semantics; and **Enumeration Constraints** — the same
property reused across classes with a narrower permitted value set per class. **Both are the alternative
to cloning an attribute per family, which is the main driver of attribute proliferation.** Coded values
carry their own identifier and translations, so `Röd` and `Red` are one value with two labels, not two
strings. BASIC is a strict CSV-representable subset; ADVANCED is ISO 13584-conformant and adds blocks,
aspects and cardinality.

**ETIM.** *Standard.* `https://www.etim-international.com/classification/`. Deliberately flatter than
eCl@ss: product groups → classes, **each product in exactly one class**, each class with a fixed feature
set. Four feature types — **A** alphanumeric from a fixed list, **N** numeric, **L** logical, **R** range
— with units mandatory on numerics except counting features. All classes, features, values and units
have language-independent codes; only descriptions are language-dependent. **That A/N/L/R set plus
mandatory units is a workable minimum type system for any attribute register**, whatever the platform.

**ISO/IEC 11179.** *Standard.* The actual standard for attribute naming. **Part 3** carries the
metamodel and the object-class / property / representation-term structure that people mean when they say
"11179 naming". **Part 5 (2015)** is naming principles — note the title changed from the 2005 edition,
so cite the right one. **Part 4** covers how to formulate a definition. Cite this when a client asks what
to call their attributes. *Clause numbers unverified — the text is paywalled.*

**GS1 Global Data Model.** *Standard.* Four layers — global core, global category, regional category,
country/local — resolved per product category, with **highest layer wins** when an attribute sits
differently in two categories. The canonical precedent for separating a core attribute set from category
sets and treating market-specific attributes as their own layer rather than as more columns on the base.
Currently scoped to five FMCG categories.

---

## Units

**UN/CEFACT Recommendation 20.** *Standard.* Rev 6 (2009) at
`https://unece.org/sites/default/files/2023-10/Rec20_Rev6e_2009.pdf`; later revisions exist — *Rev 17
(2021) probable, unconfirmed*. Three-character codes for units of measure in international trade, and
the list that GDSN, EDI and IEC 62720 all reference. **Store the Rec 20 code, render the symbol.**

**QUDT.** *Standard.* `https://www.qudt.org/`. Separates **QuantityKind** (what is measured) from
**Unit** (how it is expressed) from the **value**, with dimension vectors for conversion. **OM 2.0**
handles non-ratio scales such as Celsius more cleanly. The practical rule: the attribute declares a
quantity kind, the value carries a unit, and the unit resolves to a Rec 20 or UCUM code.

**Martin Fowler, *Analysis Patterns* (1996).** *Practitioner.* Free chapter redraws at
`https://martinfowler.com/apsupp/uml.html`. **Chapter 3** holds Quantity, Unit, Compound Unit and
Conversion Ratio — the canonical argument for **never storing a bare number** for a measured attribute.
**Chapter 2** holds the knowledge level / operational level split.

---

## Taxonomy

**W3C SKOS Reference (2009).** *Standard.* `https://www.w3.org/TR/skos-reference/`. Four things it
settles that come up in every taxonomy argument:

- **Polyhierarchy is explicitly allowed** — a concept may have any number of broader concepts.
- `skos:broader` is deliberately **not transitive**, which is what lets you model a directed graph
  without inference exploding.
- **Collections are disjoint from Concepts** — the standard's own answer to "is this a real category or
  just a grouping for display?"
- **Mapping properties** (`exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`) are the documented
  way to align a navigation tree with an external classification **without merging them**. Borrow the
  distinction even where nothing in the stack speaks RDF.

**ANSI/NISO Z39.19-2005 (R2010).** *Standard.* Free from NISO. Equivalence, hierarchical and associative
relationships; polyhierarchy; faceted vocabularies. **ISO 25964** covers thesauri and interoperability.

**Heather Hedden, *The Accidental Taxonomist*, 3rd ed. (2022).** *Practitioner.* The standard
practitioner text; the third edition emphasises the SKOS concept model over the older thesaurus term
model and adds a chapter on ontologies. *Chapter-level claims unverified.*

---

## Reference data models

**Len Silverston, *The Data Model Resource Book* Vol. 1** (rev. ed., Wiley 2001). *Practitioner.*
**Chapter 3, "Products"** — Product Definition, Product Category, Product Identification Codes, Product
Features, **Product Feature Interaction**, Unit of Measure, Suppliers and Manufacturers, Product Pricing
and Price Component, **Product to Product Associations**, Products and Parts. Chapter 4 is Ordering.
*The Good / Service subtype naming is widely cited but unverified.*

**David Hay, *Data Model Patterns: Conventions of Thought* (1996).** *Practitioner.* **Chapter 4,
"Things of the Enterprise"** — Products and Product Types, Inventory, Structure. **Chapter 12** is the
one to cite for attribute-bag modelling: *Variable Length Records* is Hay's treatment of the EAV
pattern. His own formulation of the core distinction: a product type is "the definition of it, such as
you would see in a catalogue", against a product instance as a physical example — which is `UNIT-04`
exactly.

**Hay, *Enterprise Model Patterns* (2011)** — Chapter 6 Assets, Chapter 9 the Thing / Thing Type
meta-pattern. **Berson & Dubov, *Master Data Management and Data Governance*, 2nd ed.** — Chapter 7
Master Data Modeling. **DAMA-DMBOK2 Chapter 10**, Reference and Master Data. *All three verified as
relevant; chapter numbers for the last two confirmed only via secondary indexes.*

---

## On EAV

**Nadkarni et al., JAMIA (1999, 2000).** *Practitioner, peer-reviewed.* The canonical treatment of
entity-attribute-value as a legitimate design for sparse, heterogeneous, schema-volatile data — **with a
class and relationship layer supplying metadata governance over the raw triples** — plus the companion
paper on its performance costs.

**The honest position for product data:** no standard settles EAV versus fixed schema, and the question
is the wrong one. eCl@ss, ETIM and the Global Data Model are all **governed EAV** — a property register
plus class-to-property assignment — and so are Akeneo and commercetools. **What matters is not EAV
versus fixed schema but whether the attribute set is governed and typed**: identified, versioned, with a
declared data type, unit and value domain, and an explicit assignment to the classes that use it. An
ungoverned fixed schema rots just as fast, it simply rots in columns.
