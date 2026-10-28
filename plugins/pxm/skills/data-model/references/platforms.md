# Platform expression

The logical model is decided first, in `decisions.md`. This file is how it gets built, and where it
cannot be.

## Verification status — read before quoting anything here

| Grade | Means |
|---|---|
| **Verified** | Read from vendor documentation. Safe to state, still worth confirming against the client's own version. |
| **Partner-gated** | Vendor documentation exists but sits behind a customer or partner login. Pull it with the Vaimo login before putting a number in a client document. |
| **Unverified** | General knowledge, not checked. **Do not put in a deliverable without confirming.** |

A wrong constraint is worse than a missing one: a missing constraint gets discovered in a workshop, a
wrong one sends a design in the wrong direction for a month. **Where this file and the client's instance
disagree, the instance wins** — versions differ, editions differ, and limits move.

## First: what role does this system play?

Before mapping anything, say what the system is *for*. Pushing a full model into a system that does not
need it is one of the most expensive habits in this work.

| Role | Needs | Typical |
|---|---|---|
| **System of record** | The whole model. It owns definitions, and the authoritative model lives here | ERP for commercial data, PIM for descriptive |
| **Enrichment workbench** | The model plus workflow, completeness and permissions | PIM |
| **Unification / delivery** | Identity resolution and an output shape. **Owns no definitions** | Occtoo, a data platform, a middleware layer |
| **Presentation / transaction** | Only what it must render, filter, search on and sell | Ecom, marketplace, app |

**An ecom platform needs what it must render and transact on, not the model.** Copying a PIM model into
a commerce platform is a standard failure: it doubles the maintenance surface, puts enrichment in the
wrong tool, and makes the commerce platform a second master nobody declared. Decide per system what it
needs to know, and write that down as part of the model.

---

## Logical concept → platform

| Logical | Akeneo | inriver | Commerce (typical) | Unification layer |
|---|---|---|---|---|
| Product | Product / Product Model | Product entity (by convention) | Product | Unified entity |
| Variant | Variant product under a family variant | Item entity linked to Product | Variant / configurable child | Unified entity |
| Family | **Family** (one per product) | *No equivalent* — Specification + FieldSet + Completeness Group | Attribute set | — |
| Attribute | Attribute | FieldType (bound to one EntityType) | Attribute | Field |
| Controlled list | Select attribute options | CVL | Dropdown options | — |
| Rich reference object | Reference Entity *(EE)* | Any EntityType | Option value only | Unified entity |
| Classification | Category tree | ChannelNode tree / CVL / Specification | Category | — |
| Channel | Channel *(value scope)* | Channel *(structure)* | Website / store view | Destination |
| Locale | Locale | LocaleString field | Store view | — |
| Association | Association type | LinkType | Related products | Link |
| Asset | Asset family *(EE)* | Resource entity | Media | Media entity |
| Completeness | Family-driven, per channel + locale | Completeness Group | *Usually absent* | — |

**The two biggest non-equivalences in that table** are `Family` and `Channel`, and both cause real
damage when a model is ported.

---

## Akeneo — *Verified*

**Product-centric and opinionated.** Family is the attribute contract and drives completeness
automatically. That is the strength and the constraint: the platform gives a great deal for free,
provided the model fits its shape.

**Hard constraints that change a design:**

- **Variant levels: one or two. There is no third.** Max 20 axes in total, max 10 per level.
- **A variant axis cannot be scopable or localizable.** This is the single most consequential constraint
  in the platform. An axis that legitimately varies by market cannot be an axis, and the design has to
  flatten into separate products instead.
- Allowed axis types include simple select, measurement, yes/no, number, reference entity link and
  identifier. **Multi select and reference-entity-multi are version-dependent** — vendor material
  conflicts. Verify on the client's instance before designing around either.
- **Product models have no completeness.** Only variant products do.
- One family per product. An attribute can be added to a family only once. A variant axis cannot be
  moved between levels afterwards.
- Attribute code and the unique flag are **immutable after creation**. Type changes are permitted only
  along a fixed matrix.
- No path from a simple product to a variant product — only the reverse. Getting `VARY-01` wrong in this
  direction costs a remigration.
- A child cannot remove a category or association inherited from its parent. Deleting a product model
  deletes every descendant.
- Select attributes degrade past roughly 100 options; Akeneo's own advice is to move to a reference
  entity.
- **A channel binds to exactly one category tree**, and that tree decides what exports on that channel.
  Products may sit in many categories and many trees. Envelope: around 100 channels, 300 channel × locale
  combinations.
- **Reference entities** *(Enterprise)*: max 1,000 entities, 100 attributes each, 100 options per
  attribute. Their attributes can be localizable and scopable — but records have **no completeness, no
  workflow, and cannot be categorised.** A reference entity is not a second product domain; do not design
  one as if it were.

**Edition gating matters at design time.** Reference entities, Asset Manager, the rules engine, workflow
and granular permissions are **Enterprise-only**. A Community-edition client cannot build a
reference-entity design at all, which means `THING-01` has a different answer depending on what they
bought. Establish the edition before modelling, not after.

## inriver — *Verified, with gaps*

**A typed property graph with no privileged notion of a product.** Everything is an EntityType joined by
directional LinkTypes. It will model anything — suppliers, plants, regulatory dossiers, arbitrary variant
depth — without bending a product abstraction.

**The cost is that it gives you nothing for free**, and two constraints catch platform-neutral modellers:

- **A FieldType belongs to exactly one EntityType.** There is no shared attribute pool. A `Colour`
  attribute needed on both Product and Item is **two FieldTypes**, maintained separately. A neutral
  model's reusable attribute library does not map one-to-one, and the expansion step has to be planned
  and budgeted.
- **inriver has no per-channel attribute value scoping.** A Channel is a *structure* of ChannelNodes
  containing entities — not a scope for values, which is what a Channel is in Akeneo. Channel-specific
  content requires separate fields, separate entities, or transformation on the way out. **This is the
  most expensive misassumption when porting an Akeneo-shaped model**, because it is invisible until
  someone asks for a different description on one channel.

Further documented constraints:

- **No family construct.** What Akeneo does with one concept, inriver does with three unrelated ones:
  Specifications (category-varying fields), FieldSets (display scoping) and Completeness Groups
  (validation). Deciding how those three combine is the biggest implementation-design choice on an
  inriver project.
- **Variants are just links.** Nothing enforces axis uniqueness or a complete variant matrix. Freedom
  with no guardrails, so the governance has to come from the model rather than the platform.
- Data types: String, LocaleString, CVL, Boolean, DateTime, Integer, Double, XML, File. **There is no
  date-only type**, and File is reserved for the Resource entity.
- CVL values can be localised. Multivalue is a property of the FieldType, not the CVL, and a
  **multivalue CVL cannot be a parent CVL**. Past roughly 500 values, use a plain string field instead.
- CVL identifiers: max 31 characters, alphanumeric, cannot start with a digit.
- Entities per ChannelNode must stay under 2,000. A node uses either manual linking or a rule — never
  both, and once a rule exists manual linking is blocked. An auto-configured node handles one entity type.
- An entity belongs to **exactly one segment**, and segmentation once activated applies to all entity
  types.
- Completeness rules are **not supported over REST** — remoting or an inbound extension only.

**Model sprawl is inriver's dominant failure mode**, precisely because nothing stops it. Budget a naming
convention and an entity-type ceiling at the start.

**Partner-gated — pull before sizing:** maximum entity types, field types and link types; identifier
length rules beyond CVL; maximum channels; link depth; and whether link cardinality can be declared at
all. The "Optimizing the data model" and "Optimizing your Channels" articles hold these and need the
Vaimo login. **Do not put a sizing number in a client document from this file.**

## Occtoo — *Verified (docs.occtoo.com)*

Now presented as a **Product Orchestration Engine**; the older onboard/unify/experience wording is
largely gone. The blocks are **Source → Card → Catalog → Segment → Destination**, plus Media and Events.

- **Source** is a labelled bucket that enforces no schema — entries with an identifier and properties.
  Eight property types, and a property's type is **inferred from its first value** and then enforced
  strictly afterwards.
- **Card** is the model laid on top of the ingested data. **There are no built-in entity types** —
  Product, Media and Customer are all customer-defined cards. Unification happens by **shared identifier
  across sources**.
- **Relations are key-joins on indexed properties, not referential pointers.** Neither side may be the
  id, list-to-list is forbidden, and the relation identifier is immutable. **There is no native
  hierarchy or tree primitive** — a category tree is a card plus a relation, built by hand.
- **Catalog** handles products, variants and SKUs and does allow editing, but only where the card has
  *Allow enrichment* set for that property. Entries no source delivers can be hand-created. There is no
  draft state.

**It is a unification and delivery layer that has grown a thin authoring surface — it is not a PIM.**
No documented validation rules, required-field enforcement, completeness scoring, approval workflow or
channel readiness. The logical model *is* expressed here — cards, types, relations, languages — but as a
**projection**: authoritative values stay upstream and Occtoo adds a delta.

**So if you use Occtoo, you own two models**, and the engagement has to say which one is authoritative
for every attribute. `OWN-01` and `OWN-02` stop being hygiene and become the central decisions.

Two further findings that bite:

- **No documented merge or survivorship rule, and no source precedence.** Unification is by identifier,
  but what happens when two sources disagree about the same property is not specified. That makes
  `OWN-03` a design problem you have to solve outside the platform, not a setting.
- **Destination aliases are immutable once published, and languages cannot be changed after publish.**
  Decide `SCOPE-03` before the first publish, not after. Facets accept 1–999 values and slow the
  endpoint.

Entry and property ceilings are tenant-configured and unpublished — ask, do not assume.

## Commerce platforms — *Verified*

**Adobe Commerce.** EAV for products, categories and customers; sales and quote tables are flat.
Attribute → attribute group → attribute set, **one set per product**.

- **Configurable axis rules, per Adobe: scope must be Global, input type must be Dropdown, Visual Swatch
  or Text Swatch, Values Required must be Yes, and the attribute must be in the set.** An axis that
  varies per store view cannot be an axis — the same wall as Akeneo's non-scopable axis, arrived at by a
  different route.
- Each variation is a **separate real simple product with its own SKU**.
- Scope runs global → website → store group → store view, but **catalogue price scope is Global or
  Website only, never store view.**
- Multiple root categories exist, but **each store group has exactly one root** — so multiple trees means
  multiple store groups, which is an infrastructure decision rather than a modelling one.
- Attribute code max 60 characters. **Adobe publishes no numeric limit** for attributes per set or
  configurable children; treat circulating figures as folklore.

**commercetools.** **Correction worth carrying:** commercetools now has genuine **product-level
attributes** — `level` on AttributeDefinition, GA December 2025. But they are supported by Product
Search and **not** by Product Projection Search, and every pre-2025 project is still on the legacy
`SameForAll` workaround. Check which the client is on before designing a parent level.

- **A Product's ProductType cannot be changed after it is selected.** The biggest downstream constraint
  in the platform — `GROUP-05` has no answer here.
- `changeAttributeConstraint` only ever **loosens** (SameForAll or Unique → None), never tightens.
- Nested attribute chains limited to 5 steps. Variants per product 100 (Classic) or 10,000 (Modular);
  categories per project 10,000; ProductTypes 1,000; attribute groups 100; **indexed attributes capped
  hard at 50 product + 50 variant.**

**Shopify.** **Still a maximum of 3 options per product** as of the 2026-07 API — the limit that most
often makes a design impossible. Variants 2,048 per product (legacy REST still caps at 100).

- **There is no merchant-defined category tree at all.** One fixed Shopify Standard Product Taxonomy
  category per product, plus Collections, which are flat with no true nesting. A design with a separate
  classification tree and navigation tree cannot be built.
- Metafields: 256 definitions per resource type per app, 50 pinned, 64KB values, list types max 128
  items. Metaobjects: 128 definitions per app, 1M entries each.

**Secondary platforms, briefly.** *Pimcore* — Classes and Data Objects, Field Collections, Objectbricks,
Classification Store for attribute breadth; variants are child objects with field-level inheritance;
each class is a MySQL table, so very wide classes hit row and column limits. *Salsify* — everything is a
record with enumerated properties, hierarchy via a parent id; its distinctive primitive is channel
**Readiness Reports**. *Struct PIM* — a product structure defines **two data models**, product-level and
variant-level, with variant groups as a middle tier.

## Immutability traps

The constraints that force a model to be right *before* go-live rather than iterated into shape. Check
every one of these against the design before build starts, because none of them can be walked back.

| Platform | Immutable once set |
|---|---|
| Akeneo | Attribute code, the unique flag, the two-way flag on an association type; a variant axis cannot move between levels |
| commercetools | A product's ProductType; attribute constraints only loosen |
| Occtoo | Destination aliases and languages, after first publish; relation identifiers |
| Adobe Commerce | Attribute code; an attribute's scope is painful rather than impossible |

**This table is the argument for spending real time on the `rebuild` decisions in `decisions.md`.** On
most platforms the expensive decisions are also the ones you are not allowed to revise.

---

## Where the same logical design must be built differently

The list to check a design against before promising it on a platform.

1. **Variant depth.** Akeneo caps at two levels; inriver has no cap because variation is just links;
   commerce platforms typically allow one. A three-level design fits none of them natively in Akeneo.
2. **Scoped variant axes.** Akeneo forbids a localizable or scopable axis; Adobe requires global scope on
   one. A market-varying axis is impossible in both and must flatten into separate products. **Ask for
   the real number of axes, and whether any of them varies by market, before the platform is chosen.**
3. **Channel means two different things.** Value scope in Akeneo, structure in inriver. Porting either
   way silently loses a capability.
4. **Attribute reuse.** One definition shared across families in Akeneo; one FieldType per EntityType in
   inriver, so the same attribute is defined repeatedly.
5. **Product-level attributes.** Akeneo and inriver have a genuine parent level; commercetools reportedly
   does not.
6. **Rich reference objects.** A first-class entity in inriver, a capped Enterprise feature in Akeneo, an
   option value in most commerce platforms. Where a brand needs its own enrichment, this decides the
   platform.
7. **Option-list size.** Akeneo degrades past ~100 and pushes to reference entities; inriver advises
   moving off CVL past ~500.
8. **Completeness.** Family-driven and automatic in Akeneo, assembled from three mechanisms in inriver,
   largely absent in commerce platforms.
9. **Edition gating.** In Akeneo a whole class of design is unavailable below Enterprise.
10. **Where the model lives at all.** A unification layer inverts the question — it projects a model it
    does not own.

## Recording the compromise

When the platform cannot express the logical design, **do not quietly change the logical model to fit.**
Record it:

| Logical decision | What the platform allows | Compromise taken | Cost | Revisit when |
|---|---|---|---|---|

Keeping the logical model intact is what makes the next platform migration possible, and what stops a
platform limitation being remembered a year later as a business requirement. It is also the honest
record of why the model looks the way it does, which is the question a new person asks first.
