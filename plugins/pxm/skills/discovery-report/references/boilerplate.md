# Standing text — Discovery Report Template v3.0

Text that carries between clients. Swap the placeholders, keep the wording. These paragraphs are the
parts Vaimo has learned to defend in a sign-off meeting; rewriting them for style costs more than it
gains. Section numbers refer to `sections.md`.

**Never put example figures in any of this.** Worked examples inserted to show what a table looks
like get left in client documents.

---

## 3.1 Purpose and status of this document

> The purpose of this document is to clarify the client's business requirements for product
> information management to meet the organisation's needs and eliminate as many pain points as
> possible.
>
> This document is the basis for the detailed suggested solutions and implementation requirements
> that will be presented in the Implementation Specification.
>
> This document will be signed off by the client and used as a source of truth on how the PIM system
> will be built, operated and function once all the requirements have been met.

---
## 3.2 Background

> The client has recognised that product information management is a key area for reducing or
> eliminating non-value generating processes within the organisation. The organisation also realises
> that an implementation of a modern PIM system will enable the staff to increase product data
> quality with a smaller number of work hours across channels and that it will also bring the
> possibility of supporting collaborative workflows. The PIM will serve as a data hub for both
> existing and future applications. This report's objective is also to describe future possibilities.
>
> It is important that the client gets a good understanding of the deliverables and investments
> related to the separate phases of a PIM project.
>
> The report is also an opportunity for Vaimo's experienced PIM department to give input and/or to
> challenge the organisation's current workflows from a PIM perspective, to ensure a solid delivery.
> Without an understanding of the vision, scope and requirements needed, the PIM project is at risk of
> being undefined and ultimately putting budget and timing estimates at risk.
>
> This Discovery Report is the first step towards PIM success!

---

---

## 3.4 Out of scope of the Discovery

> This Discovery covers activities relating to discovery, validation and planning.
>
> The following are **not** delivered by this engagement and may be handled under a separate
> implementation agreement:
> - full-scale data migration
> - production deployment
> - performance testing
> - licensing
> - establishment of infrastructure
> - training beyond the workshops described here
> - ongoing support

Add any engagement-specific exclusion found in the workshops. This list is allowed to grow and
usually should. Keep it consistent with 5.9 and 13.2.

---
## 3.5 Client responsibilities

> The following is a definition of what the project should not deliver. The purpose is to avoid false
> expectations among the different stakeholders. Requirements not belonging to this project will be
> listed as change requests for implementation after the launch of this project. Only the sponsor
> and/or steering committee can decide if issues will be part of this project or not.

### Change management

> A PIM implementation project will most likely affect the client's organisation regarding new and/or
> changed roles, responsibilities, workflows and organisational structure. The client is alone
> responsible to implement these changes.

### Data quality

> The client alone is responsible for the quality of the content to be migrated to or created in the
> PIM platform. The client is responsible for cleaning the inbound data, if needed. Once the legacy
> data is imported, the client can use the PIM platform to perform data cleaning. However, Vaimo PIM
> can be involved in helping the client to identify and improve data quality. If so, this will be
> managed as separate activities.

### Data migration

> In the project budget, migration work done by Vaimo is not included. Migration work in general is
> very difficult to estimate and can be quite time consuming. The migration work will be monitored
> separately and Vaimo can assist if needed but such efforts are estimated separately.

---

---

## 3.6 Assumptions and collaboration principles

**Not optional, and not pleasantries.** These are the conditions on which the conclusions of this
report rest. State them plainly, and where one was not met during the Discovery, say so in 5.8.

> A successful delivery of this Discovery assumes:
> - timely access to relevant systems and stakeholders
> - availability of the agreed data extracts
> - active participation in workshops and review sessions
> - feedback and approvals within the agreed timeframes
>
> Both parties commit to transparent communication and proactive coordination throughout the
> Discovery phase.

---
## 3.7 Basis of this report — opener

> The information in this report was gathered through workshops, documentation review and analysis of
> the data extracts listed below. Workshops were divided into smaller sessions to keep focus and make
> them as efficient as possible.

Then three tables: sessions held (date, topic, attendees), documents received (name, origin,
comments), and data extracts analysed (source system, date, volume). Anything cited anywhere in the
report appears in one of them.

---

## 4. Project Set-up and Governance — role descriptions

### Vaimo role descriptions (4.1)

**Project Manager** — The Project Manager (PM) is the person responsible for managing the project on
a day-to-day basis, from start to finish, to ensure a successful delivery within agreed budget,
schedule and scope (agreed requirements). The Project Manager will be reporting project progress to
the sponsor and/or steering committee. Emerging risks should be documented and handled adequately.

**Business Consultant** — The Business Consultant (BC) is responsible for the implementation of the
PIM system, including requirement specifications and PIM system configuration. Additionally, the BC
is responsible for data model design and workflow process set up.

**Lead Developer** — The lead developer is responsible for all custom development. They have in-depth
knowledge about the PIM platform and its APIs. The lead developer is responsible for the dev team and
resources needed. All Vaimo PIM developers are certified.

### Client role descriptions (4.2)

**Sponsor** — The client sponsor is the person that invests in the PIM implementation. The sponsor
should have an overall reason for the implementation and know what problems or KPIs within the
organisation the PIM addresses. The sponsor is the chairman of the steering committee.

**Project Manager** — The client Project Manager is the person chosen by the sponsor to be Vaimo's
point of contact and to make sure that information from client stakeholders is communicated to
Vaimo's project team.

**Product Owner** — The client Product Owner (PO) is the employee within the organisation who will
work in the system and is responsible for one or more attributes in the product process. This can be
several people with different product area responsibilities.

**SME** — A Subject Matter Expert (SME) is a person who is an authority in a particular area or topic
within the product data process flow.

---

### 4.6 Communication channels

> The following tools and channels will be the main means of communication in the implementation of
> this PIM project.

Project Dashboard · Zoom/Google Meet · Email · Slack · Jira

### 4.7 Change request management

- Change requests can only be approved by the client sponsor
- Change requests are documented in a separate document

---
## 6. Current State (As-Is) — section opener

> This section describes current product information workflows within `<company name>`. This was
> defined during the as-is specification sessions.

## 8. Target State (To-Be) — section opener

> This section describes the to-be information flows and workflows within `<company name>` once the
> PIM platform has been built and introduced in the organisation. This was defined during the to-be
> sessions.

---

---
## 10.1 Integrations — opener

> An integration is defined as a transfer mechanism moving data between the PIM and other systems.
> The transfer of data might be done automatically (event based or scheduled) or manually (eg by file
> export/import).
>
> The Discovery Report covers a high level view of the needed integrations between the PIM and other
> systems in your product information infrastructure. A more detailed description is provided as a
> part of the Implementation Specification.

---

## 10.2 Customisations — opener

> A customisation is defined as functionality identified in the "Discover and Define" work, needed in
> the client's PIM Platform but not provided by the PIM platform vendor as a standard "Out of the
> Box" functionality.
>
> This could be:
> - custom functionality inside the PIM Platform developed by using the vendor's development tools for
>   customisations.
> - custom functionality outside the PIM Platform developed by using Vaimo Developing Tools.
>
> The Discovery Report covers a high level view of the needed customisations for the PIM and the
> required workflows. A more detailed description is provided as a part of the Implementation
> Specification.

---

---
### 13.4 Indicative roadmap and timeline

> A suggested timeline based on the information and requirements collected during the Discover and
> Define phase.

---

### 14.3 Steering parameters — question

> What aspects of the PIM implementation are more important? In case of a conflict, what should have
> the upper hand, what aspect should be prioritised?

---
## 15.1 Acceptance and approval

Two parts: how this document is signed, and how deliverables were accepted along the way. The second
is the one that matters commercially, and the one clients most often have not read.

> This document will be reviewed and approved through the Google Drive approval process and/or
> Pandadoc.

**Acceptance of deliverables during the Discovery**

> On completion of a milestone, Vaimo sends a delivery confirmation to the client by email. The client
> reviews the delivery and provides written acceptance as soon as possible, and no later than five (5)
> working days from the date the confirmation was sent.
>
> If the client has not submitted written comments or objections within that review period, the
> delivery is considered accepted and approved in full, and forms the basis for invoicing under the
> agreed payment plan. The client may confirm acceptance by email in order to keep the project moving.
>
> Material changes to scope, systems or assumptions are handled through a jointly agreed change
> process.

Keep the milestone list and dates in 5.7 consistent with whatever is stated here. Where an acceptance
was given by silence rather than in writing, say so in 5.7 rather than recording it as a signed
approval.

---

## 15.2 Rights to deliverables and platform licensing

Two different things, and clients conflate them. Keep them in separate paragraphs.

**Deliverables and documentation**

> `<company name>` receives free and unrestricted rights of use to all unique deliverables and
> documentation produced specifically for them within this Discovery. This includes, but is not
> limited to, reports, architecture material, integration descriptions, data models, mapping files
> and recommendations.
>
> `<company name>` is entitled to freely use, copy and amend this material for its own purposes, and
> to use the results of the Discovery as a basis for future procurement or further implementation,
> regardless of supplier.

**Test environment, configuration and licensed platforms**

> The proof of concept environment and the integration and data flows established during the
> Discovery are set up partly in licensed software-as-a-service platforms. For those platforms:
> - ownership and intellectual property rights in the underlying platforms and standard components
>   cannot be transferred to the client and remain subject to the respective licensor's terms
> - `<company name>` has full rights to use the specific configurations, mappings and data flows
>   created in those platforms during the Discovery, **provided the client holds an active and valid
>   licence for the platform in question**

Cross-reference this from 11.8 so the reader meets it while the PoC environments are being described,
not only at signature.

---
## Appendix A — Glossary

| | |
|---|---|
| B2B | Business to Business |
| B2C | Business to Consumer |
| ERP | Enterprise Resource Planning (Financial system) |
| KPI | Key Performance Indicator |
| PM | Project Manager |
| PIM | Product Information Management |
| USP | Unique Selling Point |
| TBD | To Be Defined |
| BC | Business Consultant |
| BA | Business Analyst |
| DEV | Developer |
| EE | Enterprise Edition |
| CE | Community Edition |
| CMS | Customer Success Manager |

Add client- and platform-specific terms as discovery surfaces them.

---

---
## Appendix C — Data model definitions / Akeneo /

Keep only if Akeneo is the chosen platform. Delete the inriver block below.

**Category** — Categories are used in Akeneo to organise and classify products. Products within a
category do not have to be similar; the category "Outdoor Leisure" could contain a garden table, a
charcoal grill and a badminton net. A product can belong to multiple categories at the same time.
Individual categories are combined in a parent/child relationship and form category trees. Each
channel must be linked to a category tree, and a product must belong to a category tree that is
linked to a channel to be exported.

**Product** — There are two types of product modelling, simple and variant. A simple product is a set
of attribute values that defines a product, including a unique Stock Keeping Unit (SKU). A variant
product groups SKU-level products that share the majority of their data, varying across one or more
variant axes — the attributes that make each variant unique, such as size and colour. The common
level is represented by one or two product models, and the variants inherit all data that is not
specific to the SKU.

**Product Model** — A Product Model allows the definition of common properties for the products
gathered under it. These properties can be attributes, categories or associations.

**Channel** — A channel is used to define a selection of products and product information to export
from the PIM. Channels account for different variations of product information for the same product
based on destination.

**Completeness** — Completeness rules dictate what product information is mandatory for a product
when sent to a certain channel.

**Locale** — Locales allow different attribute values for the same product based on region and
language, which is how translations are managed. A locale is a combination of a language (English,
French, German) and a region (United States, United Kingdom, France).

**Family** — Families group products with similar attributes to simplify enrichment; a product family
defines the attribute set that describes a subset of the catalogue. You could say a product family is
a way to describe how you describe a product. Some attributes are shared across all products. The
family is also where completeness rules are defined per attribute and channel — an attribute may be
mandatory for one channel in one family but not in another combination. A product should be assigned
to a family on creation, and inherits that family's predefined attributes.

**Reference Entity** *(EE version)* — Reference entities manage information that cannot be handled
with a simple attribute. They let you reference a discrete entity, with its own set of attributes and
its own completeness rules, from a product — brands, designers, colours, ingredients, care
instructions and so on.

**Attribute** — An attribute is the smallest entity in Akeneo, storing one piece of product
information; a product is composed of many. Each attribute type has its own validation parameters —
maximum characters for text, whether negatives are allowed for numbers. Attributes can have different
values per activated locale and channel (sometimes called scope), which supports both translation and
audience-specific data.

**Attribute Group** — Attributes are combined into attribute groups, which streamline enrichment by
giving each team only the attributes needed for their tasks. Permissions for an attribute group are
set per user group. Groups also make it easier to lay out data on the product enrichment page.

**Associations** — Products can be linked together using associations. Several association types can
be created for different relationship purposes: cross-sell, upsell, spare parts, accessories, related
products and so on.

---

## Appendix C — Data model definitions / inriver /

Keep only if inriver is the chosen platform. Delete the Akeneo block above.

> The Elastic Data Model (Data Model for short) is the most fundamental concept of an inriver
> installation. An elastic data model is basically an organisation of data into entities and
> relations. We distinguish between model and data, where the model is the way of structuring data
> and the data is the actual content.
>
> Technically, an elastic data model is a database representation of a set of predefined building
> blocks. All communication with the database is done through the inriver Server, which secures the
> integrity of the model and data. The server supports various APIs by which you can provide the
> end-user with a customised enrichment experience based on the elastic data model.

**EntityType** — The cornerstone of the Marketing Model. It acts as a container for a set of data
fields and other properties, treated as a unit. When you define how to link related information
elements, that is defined as a LinkType between two EntityTypes. Each inriver solution has a unique
set of EntityTypes — default ones used repeatedly, plus custom ones for the requirements of that
solution.

**FieldType** — A template defining the properties of a field of this type, and part of the marketing
model. A field type is always associated with an entity type. It has a corresponding object called
FieldType in the inriver.Remoting component.

**Field** — The smallest information unit in inriver. A field is always associated with a field type,
which defines most of its properties — data type, read-only, hidden, mandatory, unique. A field is
always associated with an entity, and the entity's type defines which field types, and therefore
which fields, it has.

**CVL** — A Controlled Vocabulary List is a data type that defines a list of data points as key/value
pairs. CVLs are used mainly for data entry, to avoid spelling errors and invalid values by making
users choose from a predefined list — sets of colours, brands, product groups, status codes.

**LinkType** — A definition of a relation between two EntityTypes. It defines the link's source
EntityType (parent) and target EntityType (child), the language-dependent names for the LinkType, the
order links of this type appear in relative to other LinkTypes, and optionally the LinkEntityType.

**Specification** — A concept for adding and categorising technical attributes about entities without
defining them as field types in the Elastic Data Model. Specification is also the name of an entity
type with built-in functionality to support these technical attributes.

**Category** — A mechanism to group similar field types. A category consists of a name and an
ordering index and is mandatory for every field within an entity type. Combining field and category
indexing controls the display order of both. Categories are only used for visual presentation and do
not affect data published to outbound channels.

**Channel** — A channel is used to define a selection of products and product information to export
from the PIM. Channels account for different variations of product information for the same product
based on destination.

**Completeness** — inriver allows you to dictate which product information is mandatory for each
"version" of a product sent to a channel. This is referred to as completeness.

**Languages** — Languages allow different attribute values for the same product based on
country/language, mainly to manage translations. A language is a combination of a language (English,
French, German) and a country (United States, United Kingdom, France). Attributes that differ by
language must be created as "Locale" in the data model field settings.

**Field Set** — A show/hide concept for displaying only a subset of FieldTypes for an EntityType.
Selecting a fieldset for an entity excludes all FieldTypes belonging to other fieldsets from view.
FieldTypes that belong to no fieldset are considered global and are always displayed. A FieldType can
be assigned to more than one fieldset.

**Associations** — Products can be linked together using associations. Several association types can
be created for different relationship purposes: cross-sell, upsell, spare parts, accessories.

---

---

## Appendix D — Discovery survey

The standard question set. Summarised in 6.1; the full grid lives in the appendix so it stops
interrupting the argument.

| Question | Answer |
|---|---|
| Are you mainly a B2B or B2C company? Or both? | |
| In what kind of industries are you operating? | |
| Is your market domestic or global? | |
| How big is the company's total revenue? | |
| What is the online channels' revenue? (%) | |
| What is the target revenue increase? | |
| What is the number of online transactions? | |
| What is the current online conversion rate? | |
| How many suppliers do you work with? | |
| How many retailers do you have? | |
| How many suppliers onboard their products themselves? | |
| Which are your existing systems for product information? | |
| How many products (SKUs) do you have? | |
| What is the rate of adding new SKUs and how would you like this to change? | |
| How do you enrich your product information today? | |
| How many languages do you use to describe your products today, and will this change? | |
| Do you have defined workflows for product creation and enrichment? | |
| How good is your data consistency across your platforms, internal and external? | |
| How many employees are involved in onboarding, enriching and publishing products? | |
| How much time, on average, does each employee spend on product information? | |
| What is the average time to market for a new product? | |
| What is your current e-commerce platform? | |
| How automated is publishing to that platform? | |
| To what other consumers do you send, or plan to send, product data? | |
| What are your main reasons for introducing a PIM platform? | |

Add client-specific questions rather than dropping standard ones — an unanswered row is itself a
finding, and 6.1 should say so.
