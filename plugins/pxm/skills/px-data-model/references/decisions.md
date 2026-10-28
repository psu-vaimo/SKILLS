# The decision register

70 decisions in twelve areas. A data model is not a diagram, it is **this list of decisions**, and the
model is finished when every decision that matters for this client has been made, recorded and
attributed.

**The areas are in dependency order and that order is the method.** Each area needs the one above it
settled. The commonest way a model goes wrong is starting at `DESCRIBE`, because the attribute list is
what the data audit hands you and it looks like a head start. It is not: you cannot decide attributes
without families, families without variants, variants without knowing what a product *is*.

## How to read a row

| Column | Means |
|---|---|
| **Decided by** | `evidence` — the data settles it; run the audit check and read the answer. `judgement` — yours to make and defend; the data informs but does not decide. `client` — a business decision with commercial consequence that is not yours to make. Escalate it, and record who made it. |
| **Default** | What to assume when nothing argues otherwise. Not a recommendation — a starting position that makes the absence of a decision visible. |
| **Reversing** | What it costs to change after go-live. `rename` — a config change, no data moves. `remap` — values must be transformed, the shape holds. `remigrate` — records must be reloaded. `rebuild` — the model is genuinely different and everything downstream changes with it. |
| **Relates** | The `px-analyst` ability this decision serves. |

**Spend time in proportion to the `Reversing` column.** A `rebuild` decision deserves a workshop; a
`rename` decision deserves five minutes and a convention.

---

## UNIT — what is a product

Nothing else can be settled first, and this is the area clients assume is obvious. It is not obvious in
any business that sells in more than one form.

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `UNIT-01` | What the sellable unit is — what carries a price, an order line, a stock figure | client | the ERP's article | rebuild | `MODEL-02` |
| `UNIT-02` | What the marketed item is — what gets a page and a name a customer recognises | client | same as `UNIT-01` | rebuild | `MODEL-02` |
| `UNIT-03` | Which of the two the model anchors on, when they differ | judgement | anchor on sellable, present on marketed | rebuild | `MODEL-01` |
| `UNIT-04` | Whether individual physical items must be described, not only kinds of product | client | no | rebuild | `MODEL-20` |
| `UNIT-05` | What size of change makes something a different product rather than a changed one | judgement | the standard's identifier rules | remigrate | `MODEL-19` |
| `UNIT-06` | Whether packaging levels are products in their own right or levels of one product | evidence | levels of one product | rebuild | `MODEL-04` |
| `UNIT-07` | Whether services, spare parts, consumables and accessories are the same kind of thing as goods | judgement | same kind, different family | remigrate | `MODEL-02` |

*`UNIT-01` and `UNIT-02` diverge more often than anyone expects, and the model has to say which one it
is built on. A customer choosing a kitchen mixer chooses a marketed item; the warehouse ships a sellable
unit; a B2B buyer orders by the metre while the page sells a roll. **Follow the money and follow the
page** — what gets an order line, and what gets a URL.*

***Borrow GDSN's pattern rather than inventing one.** The trade item hierarchy does not force these
roles into a single "product type" enum. It carries them as separate booleans on each level — is this a
base unit, a consumer unit, an orderable unit, a despatch unit, an invoice unit — so one level can be
several of those at once, and the roles stay independent of where the level sits in the packaging
hierarchy. That is the right shape for `UNIT-01` through `UNIT-06` together: **model the roles as flags,
not as a type.** A single enum forces a false choice the first time something is both consumer-facing
and orderable, which is most of the time.*

*`UNIT-06` is where building materials, fasteners and FMCG all get difficult. One organisation models a
broom as a shaft and a brush head with separate identifiers inside one sellable unit; another treats a
pallet, a case and a piece as three products. Both are defensible. **Undeclared is not.** The external
answer worth borrowing is the classification standard's own rule on when a change requires a new
identifier — it is the closest thing to an industry position on what makes a product a different product.*

---

## THING — what else deserves its own existence

The area most often skipped, and the one that most reliably decides whether the model ages well. Getting
it wrong is invisible for a year and then expensive.

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `THING-01` | Which values need describing in their own right, and so become entities rather than options | judgement | option until proven otherwise | rebuild | `MODEL-05` |
| `THING-02` | Which things belong to a product without being products — documents, certificates, load tables | evidence | model them | remigrate | `MODEL-15` |
| `THING-03` | Whether assets are entities with their own attributes, or files with metadata | judgement | entities, if more than one type exists | remigrate | `ASSETS-06` |
| `THING-04` | Whether suppliers, brands and manufacturers are modelled objects or text on a product | evidence | modelled | remigrate | `MODEL-05` |
| `THING-05` | Whether an assortment is an entity, a tree, a channel or a flag | client | channel | rebuild | `CONTEXT-03` |
| `THING-06` | Whether bundles and kits are a product type, a relationship, or both | judgement | product type with relationships | rebuild | `MODEL-06` |

*The test for `THING-01` is three questions, in order. **Does the value itself need describing?**
"Colour: red" is an option; a colour with a hex code, a swatch image, a marketing name in six languages
and a supplier is an entity. **Is it maintained independently of any product?** A brand has a logo, a
description and an owner whether or not a product references it. **Does more than one kind of thing point
at it?** If a brand is referenced by products, by campaigns and by suppliers, it is not a product
attribute.*

*One yes is usually enough. The failure mode is deferring — a text field called `Brand` is cheap on day
one and a `rebuild` in year two, because by then every product carries a string that has to be
reconciled against a list nobody kept.*

*`THING-05` is a genuine either/or and the choice has commercial consequences, which is why it is a
client decision. A buying cooperative where members carry different ranges needs something the model can
address directly; a single retailer usually does not.*

*Expect the assortment to be hidden. Legacy systems often encode it inside another field — a type value
such as *web assortment, discontinued*, or a set of per-customer flags. **Pull it out before deciding
`THING-05`**, along with any lifecycle or workflow meaning in the same values (the audit's `STRUCT-11`
finds these), or the decision gets made about a field that is really three.*

---

## VARY — how products differ from each other

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `VARY-01` | Which differences are variants, which are separate products, which are attribute values | judgement | variant if the customer chooses between them on one page | rebuild | `MODEL-04` |
| `VARY-02` | Which attributes are the variant axes | evidence | from value distribution per family | rebuild | `MODEL-04` |
| `VARY-03` | How many variant levels | judgement | one | rebuild | `MODEL-04` |
| `VARY-04` | Whether every product in a family shares the same axes | judgement | yes | rebuild | `MODEL-01` |
| `VARY-05` | What lives at the common level and what is variant-specific | evidence | common unless the data varies | remap | `MODEL-04` |
| `VARY-06` | Whether some combinations of axis values are invalid and must be prevented | client | no constraint | remap | `MODEL-11` |
| `VARY-07` | Whether a variant may exist without a parent, or a parent with no variants | judgement | no to both | remigrate | `MODEL-04` |

*`VARY-01`'s test is what the customer is doing, and it has external backing. **If they are choosing
between them on one page, they are variants. If they would never be compared side by side, they are
separate products.** Google's product feed rules state exactly this criterion for grouping variants, and
give the counter-examples: a jacket and trousers sold as a suit, or a set of bath accessories, are not
variants. `schema.org`'s ProductGroup says the same in modelling terms — the group is a template that is
not itself sold, and `variesBy` names the axes explicitly.*

***Do not confuse this with whether they are separately identified.** The GTIN Management Standard is
clear that each style × colour × size is a distinct trade item with its own identifier, so "they are
variants" and "they are one product" are not the same statement. Almost always each variant is its own
identified, transactable item; the variant decision is about **how those items are grouped and where
shared data lives**, not about whether they are distinct. Conflating the two produces either a
catalogue of orphans or a product model that cannot be ordered from.*

*`VARY-02` is one of the few decisions the data can genuinely settle. An axis candidate is an attribute
whose values vary within a group of products that are otherwise identical — which is measurable. Read
it from the profile rather than asking, then confirm.*

*`VARY-03` is where the platform bites hardest and where a logical model becomes unbuildable. Ask for
the real number of axes before choosing a platform, not after — see `platforms.md`. A client with three
genuine axes has a platform selection criterion, not a modelling problem.*

---

## GROUP — what groups products together

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `GROUP-01` | What a family groups — products described alike, not products sold alike | judgement | described alike | rebuild | `MODEL-01` |
| `GROUP-02` | How many families | evidence | from attribute co-occurrence in the audit | remigrate | `MODEL-01` |
| `GROUP-03` | How granular a family may be before it splits, or how sparse before it merges | judgement | see the test below | remigrate | `MODEL-01` |
| `GROUP-04` | Whether families derive from the classification standard or are independent of it | judgement | independent, mapped | remigrate | `MODEL-09` |
| `GROUP-05` | Whether a product may move between families, and what happens to values that no longer fit | judgement | allowed, values retained | remap | `MODEL-17` |
| `GROUP-06` | How attributes are grouped for the people who fill them in | judgement | by who maintains them | rename | `ORGANISE-05` |

*`GROUP-01` is the most common structural error in the whole register: **families built to mirror the
category tree.** Categories are for finding a product, families are for describing one, and the two
have no reason to agree. A garden table, a charcoal grill and a badminton net sit happily in one
category and share almost no attributes — that is the category working correctly, and it would make a
catastrophic family.*

*`GROUP-03`, as a working test: if most members of a family leave most of its attributes empty, the
family is too broad and completeness becomes meaningless. If two families differ by fewer than about
three attributes, they are too narrow and should merge with the difference carried as optional
attributes. Both halves matter — a client who has one generic family and a client who has 900 families
have the same underlying problem, which is that nobody decided what a family is for.*

*`GROUP-06` is not cosmetic, despite being a `rename`. It decides what an enricher sees on screen, and
grouping by maintainer rather than by subject is what makes a 200-attribute family workable.*

---

## DESCRIBE — the attributes themselves

Now, and not before. The bruttolista from the audit is the input to this area, not to the model as a
whole.

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `DESCRIBE-01` | Which attributes exist at all | evidence | bruttolista verdict `migrate` or `merge` | remigrate | `MODEL-03` |
| `DESCRIBE-02` | The type of each attribute | evidence | from the value profile | remap | `MODEL-03` |
| `DESCRIBE-03` | The naming and coding convention | judgement | agree one, apply it everywhere | rename | `QUALITY-08` |
| `DESCRIBE-04` | Whether an attribute is reused across families or duplicated per family | judgement | reuse | remap | `MODEL-01` |
| `DESCRIBE-05` | How units are handled — value and unit separately, or one attribute per unit | evidence | separate, with a unit family | remap | `MODEL-03` |
| `DESCRIBE-06` | Which values are calculated or derived rather than entered | judgement | entered unless a rule exists | remap | `ENRICH-03` |
| `DESCRIBE-07` | Where a fixed tag set is needed and where free text is right | judgement | fixed where it is filtered on | remap | `MODEL-13` |
| `DESCRIBE-08` | Validation per attribute — lengths, ranges, allowed characters, conditional requirements | judgement | from the audit's validity findings | rename | `QUALITY-11` |

*`DESCRIBE-05` is the decision that quietly creates attribute proliferation. One concept held as
`length_mm`, `length_cm` and `längd` is three attributes for one fact, and it happens because somebody
put the unit in the attribute name instead of in the value's metadata. **`weight_kg` is an anti-pattern**
— it blocks alternate-unit rendering and per-market conversion, and it is how a catalogue ends up
unable to answer "how heavy is this" in one query.*

*The standards all separate three things, and so should the model: the **quantity kind** (what is being
measured — length), the **unit** (how it is expressed — millimetres), and the **value**. Declare the
quantity kind on the attribute, carry the unit with the value, and store the unit as a UN/CEFACT
Recommendation 20 code while rendering the symbol. Fowler's Quantity pattern is the same rule at
implementation level: **never store a bare number for a measured attribute.** Decide unit families
first, then the attributes; where the platform has a measurement type, it has made the decision for you.*

*`DESCRIBE-04` looks obvious and is not. Reuse gives one definition and one translation; duplication
gives each family independent control and a maintenance problem that grows quadratically. Reuse unless
two families genuinely mean different things by the same word — in which case the real problem is
`DESCRIBE-03`.*

*Where a classification standard is adopted or mapped (`TREE-03`), reuse extends to it. A legacy
catalogue often carries a large free set of features next to the standard's — one export had about
2,400 — and many restate a standard feature in local words, with the unit in the name. **Map the free
features onto the standard's features first, and create a new attribute only for what is left.** Every
free feature that becomes its own attribute is a second definition of something the standard already
governs, and a translation and validation job the standard would have done for free.*

---

## VALUES — the controlled vocabularies

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `VALUES-01` | Which attributes take a controlled list rather than free text | evidence | list where distinct values are few and repeat | remap | `QUALITY-11` |
| `VALUES-02` | Where each list is mastered, and whether the PIM owns it | judgement | PIM, unless a standard owns it | remap | `MASTER-06` |
| `VALUES-03` | Whether list values are translated, and by whom | client | translated | remap | `MASTER-05` |
| `VALUES-04` | Who may add a value, and whether adding one is governed | client | governed | rename | `QUALITY-03` |
| `VALUES-05` | Whether a list value needs attributes of its own — which promotes it to `THING-01` | judgement | no | rebuild | `MODEL-05` |

*`VALUES-01` is answerable from the profile: an attribute whose distinct values collapse to a small set
once case and whitespace are normalised is a list that has not been declared. The audit's consistency
checks find these; this decision acts on them.*

*`VALUES-04` sounds like governance trivia and is the reason lists rot. An open list with no owner
becomes free text within eighteen months, at which point `VALUES-01` has to be decided again with more
data and less goodwill.*

---

## SCOPE — what information is allowed to vary by

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `SCOPE-01` | Which dimensions information may vary along at all | client | language and channel | rebuild | `CONTEXT-01` |
| `SCOPE-02` | Per attribute, whether it is translated or genuinely different per market | judgement | see the test below | remap | `CONTEXT-05` |
| `SCOPE-03` | The locale list, and what a locale means here — language, or language plus market | judgement | language plus market | remigrate | `CONTEXT-02` |
| `SCOPE-04` | The channel list, and what distinguishes a channel from a market | judgement | channel is a destination | remigrate | `DELIVER-08` |
| `SCOPE-05` | What happens when a market-specific value is missing — fall back, or publish nothing | client | fall back to a default | remap | `CONTEXT-02` |
| `SCOPE-06` | Which products belong to which market or assortment | client | all, unless excluded | remap | `CONTEXT-04` |

*`SCOPE-02` is a **three-way** test, and almost everybody collapses it into two at least once:*

- ***If the difference is in the thing itself, it is a different product.** The GTIN rules settle this —
  an English-only pack and a Spanish-only pack of the same goods are two products, not one product with
  two translations.*
- ***If the difference is in the regulated or commercial data about the thing, it is a market-scoped
  value.** A certification, a legal disclaimer, a price, an image showing a local plug. Someone with
  market knowledge has to decide it.*
- ***If the difference is only in the wording, it is a translation.** A competent translator could
  produce it from the source without knowing the market.*

*Marking the middle kind as translatable sends it to a translation agency, which is how a client ends up
publishing a Swedish certification claim in German.*

*There is a fourth state worth declaring separately: an attribute that **does not apply at all** outside
certain markets — a cold-resistance rating only meaningful in the north, a tax field only for one
country. Akeneo models this as locale-specific, distinct from both localizable and scopable. Where the
platform supports it, use it; where it does not, an attribute that is empty for most of the catalogue by
design will otherwise be read as a completeness failure forever.*

*`SCOPE-01` is `rebuild` and deserves the weight. Every dimension multiplies the number of values that
can exist, and the cost is paid by whoever has to fill them in. Adding a dimension later is a
restructure; declining one is cheap. Be conservative here in a way it is safe to be nowhere else.*

---

## TREE — classification and hierarchy

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `TREE-01` | How many trees exist, and the stated purpose of each | judgement | one per purpose | remigrate | `MODEL-09` |
| `TREE-02` | Which tree drives customer navigation | client | the commerce tree | remap | `PRESENT-05` |
| `TREE-03` | Which standard is adopted, which is mapped to, and which is ignored | client | map, do not adopt | remap | `DELIVER-13` |
| `TREE-04` | Whether a product may sit at several nodes, and in several trees | judgement | several nodes, several trees | remap | `MODEL-09` |
| `TREE-05` | Whether a node carries attributes or defaults that products inherit | judgement | no | remigrate | `MODEL-16` |
| `TREE-06` | Whether products may sit on non-leaf nodes, and how deep the tree goes | judgement | leaf only | remap | `MODEL-09` |

*`TREE-01`'s rule is **one tree per purpose, name the purpose, and map between them rather than merging
them.** There are usually three and they are genuinely different in shape as well as in use:*

- ***Classification** — external and monohierarchical (ETIM, eCl@ss, GPC). Its job is to decide which
  attributes apply.*
- ***Navigation** — per channel, polyhierarchical, built on how shoppers think. Facets come from
  attributes, not from this tree.*
- ***Internal** — buying, planning, reporting. Usually monohierarchical, because finance needs
  roll-ups that do not overlap.*

*Serving all three from one tree is the most common taxonomy failure, and the audit's `CLASS-05` detects
it: a tree whose own name gives away its origin, whose leaves group things that are alike to an
accountant rather than to a buyer.*

*SKOS is the documented mechanism for holding them together — its mapping relations exist precisely to
align two schemes without collapsing them, it blesses polyhierarchy explicitly, and its Collection
construct is the right home for a grouping that is only a display label rather than a real category.
Borrow the distinction even when nothing in the stack speaks RDF.*

*`TREE-05` is `remigrate` and usually answered no, but it is worth asking deliberately because when it
is right it removes a great deal of manual work. Category-level defaults are powerful and they make
provenance murky — a value nobody typed, that changes when somebody moves a product.*

---

## RELATE — how products point at each other

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `RELATE-01` | Which relationship types exist, and what each means | client | accessories, spare parts, replaces | remap | `MODEL-07` |
| `RELATE-02` | Whether each type points one way or both | judgement | one way, stated | remap | `MODEL-14` |
| `RELATE-03` | Whether relations are maintained by hand or derived from classification | judgement | by hand, derived where possible | remap | `MODEL-16` |
| `RELATE-04` | What a relation may point at — a product, a variant, a model, an entity | judgement | any level, declared per type | remigrate | `MODEL-07` |
| `RELATE-05` | Whether a superseded product keeps pointing at its replacement after it is retired | client | yes | remap | `QUALITY-16` |

*`RELATE-02` is small and catches people out. "Accessory" one way is not the same statement as
"accessory" both ways — a screwdriver bit is an accessory to a drill, while the drill is not an
accessory to the bit. Declaring the direction per type prevents a category of nonsense on the page that
nobody notices until a customer does.*

---

## READY — what must be true, and when

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `READY-01` | What "ready" means, stated per channel | client | per channel, written down | rename | `QUALITY-01` |
| `READY-02` | Whether readiness differs by lifecycle state as well as by channel | judgement | yes | rename | `QUALITY-02` |
| `READY-03` | Which attributes are required, in which family, for which channel | judgement | from channel specifications | rename | `QUALITY-01` |
| `READY-04` | Whether readiness measures the record being filled or the content being good | judgement | filled, with content measured separately | remap | `MEASURE-07` |

*All four are `rename`, which makes this the cheapest area to get wrong and therefore the one worth
deciding properly — there is no excuse for deferring a decision that costs nothing to revise. Where a
channel publishes its own specification, `READY-03` is already written and the client cannot argue with
it.*

*`READY-04` keeps the audit's second rule alive inside the model: a completeness score that counts
`N/A` as filled will report a healthy catalogue forever.*

---

## OWN — who masters what

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `OWN-01` | Which system masters each attribute | client | ERP for commercial, PIM for descriptive | remap | `MASTER-06` |
| `OWN-02` | What the PIM explicitly does not own | judgement | state it | remap | `MASTER-01` |
| `OWN-03` | What happens when two sources write the same field | client | source precedence, written per field | remap | `QUALITY-13` |
| `OWN-04` | Which fields may be edited downstream, and whether the edit survives a resync | client | no downstream edits | remap | `MASTER-01` |
| `OWN-05` | Who may change the model itself, and how | client | governed, named role | rename | `MODEL-17` |

*`OWN-04` is the decision that produces the most support tickets in year one. Somebody edits a
description in the webshop, the next sync overwrites it, and the business concludes the PIM is broken.
Decide it per field, write it down, and make the read-only fields visibly read-only in whichever system
is not the master.*

*`OWN-02` is worth stating as its own line rather than inferring it from `OWN-01`. A model that never
says what it excludes gets asked to hold stock levels, prices and order history within a year.*

---

## LIFECYCLE — what happens over time

| ID | Decision | Decided by | Default | Reversing | Relates |
|---|---|---|---|---|---|
| `LIFECYCLE-01` | The states a product moves through, and who moves it | client | draft, active, discontinued | remap | `STATUS` domain |
| `LIFECYCLE-02` | What happens at end of life — archived, deleted, or retained and hidden | client | archived, retained | remigrate | `QUALITY-16` |
| `LIFECYCLE-03` | Whether previous versions of values and documents are kept, and for how long | client | kept for regulated content | remigrate | `MODEL-10` |
| `LIFECYCLE-04` | The identifier scheme, and whether retired identifiers are ever reused | client | never reused | rebuild | `MODEL-19` |
| `LIFECYCLE-05` | How a change to the model itself is assessed before it is made | judgement | impact assessed, then changed | rename | `MODEL-18` |

*`LIFECYCLE-02` is the verb everyone skips, in the model as much as in the workflow. A product that
cannot be retired cleanly becomes a data quality problem that grows, and everything pointing at it —
assets, relations, category memberships — breaks quietly at the moment it is removed. Decide it here,
and check it against the audit's `REF-05` and `REF-06`.*

*`LIFECYCLE-04` is `rebuild` and usually gets three minutes. It deserves more: identifier schemes
outlive every other decision in this register, including the platform.*

*Check which levels the scheme actually covers. Where the marketed item (`UNIT-02`) is a PIM-only
grouping over ERP articles, it has **no identifier outside the PIM at all** — in a legacy export that
shows up as a placeholder where the key should be. The new system then has to create and own that
identifier, which makes it a `LIFECYCLE-04` decision for the PIM, not an inheritance from the ERP. Decide
its format, and that it is never reused, before migrating the groupings, or the migration will invent one
per run.*
