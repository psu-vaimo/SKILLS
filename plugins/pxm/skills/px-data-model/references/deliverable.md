# The deliverables

## Four levels, and they are not the same document

Conflating these is why two incompatible house templates exist with nothing saying which to use when.

| Level | Where it lives | Purpose | Shape |
|---|---|---|---|
| **High level** | Discovery Report **section 9** | Enough for a client to sign and a budget to be built on | One table, 18 areas, an order-of-magnitude assumption each |
| **Draft** | A **sandbox** in the target PIM, plus the **Draft Model File** | A workshop in which the client works through the To-Be workflows on 10–20 of their own products | Small workbook, Data Model File column names, every structural choice marked `draft` |
| **Detailed** | The **Data Model File** | The analytical working document. Cross-system, decision-bearing | Many sheets, wide attribute sheet |
| **Import** | A platform load file | Loading a configuration | Narrow, platform-shaped, one row per object |

The draft is optional and is specified in full in `draft-model.md`. Its sandbox needs a load file of its
own. That file is generated from the Draft Model File and **thrown away with the sandbox**, so it is not
the third level arriving early.

**A discovery produces the first, may produce the draft, and starts the detailed model. It does not
produce the production import file.** The house rule
already in the report template is that discovery delivers a high-level model and detail belongs in a
separately approved data modelling file — hold that line, because the detailed model is where scope
quietly doubles.

The import file is **derived** from the detailed model, never maintained alongside it. Two maintained
copies of an attribute list diverge within weeks.

---

## Level 1 — Section 9, the high-level model

One row per area, taken from the report's fixed register: channels · category trees · locales ·
families · currencies · attribute groups · attributes · single products · variant products · bundle
products · assets · asset families · measurements · associations · rules · reference entities · AI
configurations · workflows.

| Area | Description | Basic assumption | Data readiness | Comment | Priority |
|---|---|---|---|---|---|

- **Basic assumption** is an order of magnitude. Ranges are fine and honest — "200–300 families" is a
  better answer than a false precision nobody can defend.
- **Data readiness takes its judgement from section 7**, the audit. It does not carry an independent
  guess.

---

## Level 2 — the Data Model File

The analytical artefact, and the one clients keep. Its defining feature is that **the attribute sheet
holds one column group per system**, which is what makes it a cross-system model rather than a target
configuration.

### Sheet: Attributes

One row per attribute. Columns in groups:

**Identity and inclusion**
`Type of field` · `Include in PIM (To-be)` · `Motivation` · `Attribute code (To-be)` ·
`Rationalised attribute name` · `Might be a duplicate of` · `Sample data`

*`Type of field` is a controlled register, not free text — classification features, native PIM
attributes, ERP report fields, core ERP fields, custom attributes, regulatory attributes, commerce
content, compliance declarations. It is what makes several hundred rows navigable, and it should be
decided before the sheet is populated.*

**Per source and destination system — repeat this group once per system**
`Present in <system> as data field` · `Data type in <system>` · `Logic and rules in <system>`

*This repeating group is the whole point of the file. It is what lets one row say: the ERP holds this as
a 10-character string with a padding rule, the current PIM holds it as free text, the webshop does not
have it at all, and in the target it is a measurement. **That sentence is the model.***

**Target platform**
`Preferred data type` · `Unit family` · `Default unit` · `Decimals allowed` · `Negatives allowed` ·
`Min value` · `Max value` · `Comment on data type and units`

**Modelling decisions**
`Consider modelling as (not attribute)` · `For which families` · `Dependent on packaging level`

*`Consider modelling as (not attribute)` is the escape hatch and the most valuable column on the sheet —
it is `THING-01` answered per row. Values are `reference entity`, `association`, `category`, `asset`,
`option list`. **Every non-empty cell here must resolve to a row in one of the registers below**, or the
decision has been recorded and then lost.*

**Flow**
`Inbound from system(s)` · `Inbound conversion needed` · `Outbound to system(s)` ·
`Outbound conversion needed`

**Ownership and workflow**
`Attribute group` · `Viewable by` · `Initial creation by` · `Subsequent enrichment by` · `Approved by` ·
`Default value` · `Read only`

*These five columns are `OWN-01` through `OWN-04` recorded per attribute. They are also what the client
argues about in year one, so fill them during the project rather than after it.*

**Scoping**
`Value per locale` · `Value per channel` · `Only for locales`

*Three columns, not two — see `SCOPE-02`. The third records an attribute that does not apply outside
certain markets at all, which is different from one that is merely empty.*

**Readiness** — one column per channel, flagging mandatory. `READY-03` per attribute per channel.

### Lookup sheets

`Attribute groups` · `Channels` · `Locales` · `Categories` · `Systems` · `Data types` ·
`Measurement families`

- **Data types** carries the target platform's type list **and a `Can be used as a variant axis` column.**
  That column encodes a platform constraint directly into the working file and stops an unbuildable axis
  being proposed.
- **Systems** carries each system and its **integration role** — which is the role question from
  `platforms.md`, recorded rather than assumed.
- **Channels** carries the tree, locales, currencies and conversion units each channel binds to.

### The registers that are usually missing — add them

Known gaps in the current house file. Each one exists as free text in a cell today, which means the
decision was made and is not retrievable.

**Families** — *the single biggest omission.* Two columns on the attribute sheet already reference
families and no sheet defines them.

| Family code | Label | Attributes | Variant levels | Variant axes | Notes |
|---|---|---|---|---|---|

**Reference entities** — one row each, plus their own attributes.

| Entity code | Label | Attributes | Referenced by | Why an entity and not an option |
|---|---|---|---|---|

*The last column is `THING-01`'s reasoning, and it is what stops the decision being relitigated.*

**Associations**

| Type code | Label | Direction | From | To | Maintained how |
|---|---|---|---|---|---|

**Assets and asset families**

| Asset family | Attributes | Linked at which level | Resolution path | Notes |
|---|---|---|---|---|

*`Resolution path` matters — an asset identifier that only resolves inside a system nobody is migrating
is a broken link waiting for go-live. It is the audit's `REF-01` carried into the model.*

**Option lists**

| List code | Value code | Label per locale | Owner | Open or closed |
|---|---|---|---|---|

*One row per value. Labels per locale, because a coded value with two labels is one value, not two.*

### Decision log

The sheet that makes the model defensible a year later, and the direct answer to *what decisions were
made and which are still needed*.

| ID | Decision | Choice | Decided by | Whom | Date | Basis | Revisit when |
|---|---|---|---|---|---|---|---|

- **ID** is the `decisions.md` reference — `VARY-03`, `SCOPE-01`.
- **Decided by** is `evidence`, `judgement` or `client`. **Every `client` row needs a name in `Whom`.**
  A client decision recorded without an owner is an assumption wearing a decision's clothes.
- **Rows carried over from a draft model** keep their outcome: `confirmed` or `refuted` in the
  workshop, or still `open`. Any row still marked `draft` is a guess nobody has tested.
- **Open decisions stay in this sheet with an empty `Choice`.** That list is the agenda for the next
  session, and the honest answer to "is the model finished".

### Platform compromises

Where the logical model could not be expressed. Keeps the logical model intact and stops a platform
limitation being remembered later as a business requirement.

| Decision | Logical design | Platform allows | Compromise | Cost | Revisit when |
|---|---|---|---|---|---|

---

## Level 3 — the import file

Derived, never maintained in parallel. Narrow, one row per object, shaped by the platform's own import
format — attribute code, type, labels per locale, group, localisable, scopable, validation, plus a
family membership matrix.

**Generate it from the detailed model.** If someone is editing the import file by hand, the detailed
model has already stopped being the source of truth.

---

## A note on inherited columns

The current house file carries a `Motivation` column holding what reads as AI-generated review text
("Agree…", "Disagree…"). Earlier templates have no such column.

**Decide whether it belongs rather than inheriting it silently.** A column recording *why* an attribute
is in or out is genuinely valuable — that is the decision log's job at row level. A column holding an
unattributed machine opinion that a client will read as Vaimo's position is not. If it stays, it needs
an author and a date like every other judgement in the file.

Similarly: where two sheets hold the same attribute list in different orders for different readers, one
of them is a **view** and must be labelled as such. Two sheets, two truths is how `Logical grouping`
ended up populated on one and empty on the other.
