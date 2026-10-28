# The draft model

A small, real configuration in the client's PIM: **10–20 handpicked articles**, and only the families,
attributes, lists, roles and assets those articles need. It exists to run a workshop in which the
client walks their To-Be workflows on their own products, in the system they will use.

Without it, the To-Be workshop discusses an empty system in the abstract, and the rule from `SKILL.md`
applies twice over: **a conversation about workflow dies the moment it becomes abstract, exactly as a
conversation about structure does.** People cannot say who fills in a field they have never seen, or
what must be true before they hand a product on, until there is a product in front of them.

## What it is for, and what it is not

Two jobs, and both matter:

1. **Make the To-Be workflows testable.** Report section 8.2 describes them; the draft lets the people
   who will do each step do it on screen, in their role from 8.3, across Create · Enrich · Edit ·
   Delete. Gaps show up as somebody looking for something that is not there.
2. **Gather the decisions only the client can make**, while they are looking at a real product rather
   than a spreadsheet row: who owns each field, what "ready" means, who approves, what happens at end
   of life. These are mostly `client` rows in `decisions.md`, and they are the ones a modelling session
   usually guesses at.

It is **not** the detailed model, not the first sprint of the implementation, not a sales demo, and not
training. Each of those wants a different configuration, and a draft that tries to be one of them stops
doing its own job.

## Where it sits

| Level | Where it lives | Built from | Feeds |
|---|---|---|---|
| High level | Report section 9 | Audit (7), As-Is (6), To-Be (8) | The budget, and the draft |
| **Draft** | **A sandbox in the target PIM + the Draft Model File** | **Section 9, To-Be workflows (8.2, 8.3), audit profile** | **Decision log, 8.2/8.3 corrections, 12.1, the detailed model** |
| Detailed | The Data Model File | Everything above, plus the draft's results | The import file |
| Import | A platform load file | The detailed model | Production configuration |

**Timing:** after the To-Be workflows exist in draft and the platform (or the leading candidate) and its
edition are known. Before the Data Model File, because the draft's results fill in its ownership,
scoping and readiness columns.

**If the discovery runs a Happy Flow (section 11), pick the PoC product from the draft set.** It is
already chosen as representative, its data is already loaded, and its family already exists.

## The rule that makes it safe: a draft is a hypothesis, labelled as one

Configuring a platform means answering `rebuild` decisions (`UNIT`, `VARY`, `GROUP`) before they have
been decided, and working in platform primitives before the logical model is settled. That is the
opposite of the skill's first two rules. **It is acceptable only because the draft is disposable and
every structural choice in it is visibly provisional.** Hold to four things:

- **Every structural choice gets a decision-log row with status `draft`** and its `decisions.md` ID.
  Take the `Default` column unless the audit or the As-Is clearly argues otherwise. A draft is not the
  place for clever modelling. A clever draft gets defended instead of tested.
- **Write the Draft Model File first, then configure.** Even at fifteen products. Configure first and
  the platform's shape becomes the record of what was decided.
- **Say it out loud in the room.** Open the workshop by naming what is provisional. **The biggest risk
  of a draft is anchoring.** What a client sees configured they assume is decided, and "it is already in
  the system" becomes the argument for a family structure nobody chose.
- **Never promote it.** Production configuration is generated from the detailed model (`deliverable.md`,
  Level 3). If the sandbox instance will become the production instance, check the immutability traps
  in `platforms.md` *before the first attribute is created*. In Akeneo the attribute code and the unique
  flag cannot change, so either use a separate instance or settle `DESCRIBE-03` (the naming and coding
  convention) first. Draft codes that survive into production are draft decisions that nobody revisited.

## Picking the articles

**10–20.** Fewer cannot show the range of the assortment. More turns the workshop into data entry, and
the configuration effort grows faster than what you learn.

Pick for three things, and give each pick a stated reason:

**Width: the span of what is sold.**

- One from each major assortment or business area
- Each kind of product that will plausibly get its own family
- Each source that behaves differently: own ERP, supplier feed, trade database, typed by hand
- Each channel or market that needs something different

**Depth: the awkward ones that break a clean model.** Ask the client for these by description. They
always know which they are.

- A variant group with its real axes, and the one that does not fit the axes
- Sold or priced in a different unit than it is ordered or stocked in: by length, area, weight
- Packaging levels: piece, pack, pallet
- A kit, bundle or set
- Heavily regulated or documented: safety data, declarations, EPDs, certificates
- Many assets of different kinds
- An accessory or spare part, with the product it belongs to also in the set
- A product with rich data, to show the target, and one with poor data, to show the enrichment work
- A market-specific product or value, if more than one market exists

**Workflow coverage: every To-Be workflow in 8.2 needs an article it can run on.** Include at least:

- **One article that is not loaded at all**, to be created in the workshop. Create is the verb a
  pre-loaded sandbox cannot show.
- **One to retire**, with documents and relations pointing at it. Delete is the verb everyone skips
  (`LIFECYCLE-02`).
- One that arrives from an integration and is only enriched, never created, in the PIM.

**Draw them from the "same 50 products" set** (`SKILL.md`) where it exists, so each article has rows from
every system that holds it. **Check that every article actually exists in every source before
building.** Two exports of "the same" articles routinely disagree: an article in one and not the other,
a different product from the same supplier under a similar name. Settle that first, or the workshop
spends time on the export, not the workflow.

**Have the client confirm the list.** A useful prompt: *"Which products would you show a new colleague to
explain what is hard about your product information?"*

## What to configure

Only what the workshop needs to show. The ranges are typical, not targets.

| Area | Configure | Typically |
|---|---|---|
| Families | One per kind of product among the articles. Not one per article | 4–8 |
| Variants | At least one family variant on the real axes, if the client has variants at all | 1–2 |
| Attributes | Identifiers · enough per family that each is recognisable · what each 8.3 role owns · the fields arriving from the ERP (read-only) · what one channel requires to publish. **Not the bruttolista** | 40–100 |
| Attribute groups | By who maintains them (`GROUP-06`). The workshop is about roles, so each person should find their part on one tab | 4–8 |
| Option lists | Real values from the audit, for the lists the articles use | |
| Measurements | The unit families the articles need, with real units (`DESCRIBE-05`) | |
| Categories | A slice of the navigation tree covering the articles. Classification too, if one is adopted or mapped (`TREE-03`) | |
| Channels and locales | One or two channels, the locales really used. At least one localisable and one scopable attribute, so `SCOPE-02` has something to point at | |
| Assets | Real images and documents for the articles, from the export | |
| Associations | One or two types, between articles in the set (`RELATE-02` direction stated) | 1–2 |
| Roles and users | One per role in 8.3, with permissions approximating the To-Be | |
| Completeness | For one channel, so "ready" is visible on screen (`READY-03`) | |
| Workflow / approval | The To-Be approval steps, if the platform and edition support them. Otherwise simulate with a status attribute, and **record that as a platform compromise** | |

**Leave out:** integrations (that is the Happy Flow), more than one example rule, full translations,
every market, every family. Each of these costs a day and teaches the workshop nothing it would not
learn from one example.

**Load real data, never invented.** Use the values from the exports for the chosen articles. Load each
article in the state the To-Be expects at the moment its workflow starts: ERP fields filled as if the
integration ran, enrichment fields as the audit found them, including the empty ones. **Mark nothing
complete that is not.** A sandbox that looks finished invites admiration, not work.

Where the edition cannot express something the logical draft needs (a reference entity on a Community
edition, an axis that varies by market), record it in the platform compromises sheet as for the
detailed model. Do not quietly simplify the draft to fit.

## Running the workshop

A different shape from a modelling session: **the participants operate and the facilitator watches.**
Invite the people who will actually do each step, one per role in 8.3. Their managers alone will
describe the process as it is meant to work rather than as it does.

1. **Frame.** What the sandbox is, what in it is provisional, and what you need from them: to try to do
   their job in it and say where it fails.
2. **Walk each To-Be workflow** from 8.2, on the article picked for it, verb by verb. The person who will
   do the step does it on screen.
3. **At each step, capture** who did it, what they needed that was not there, what was there that they
   did not need, and what they would expect to be true before handing on.
4. **When a structural question comes up, go to the awkward article.** Same rule as in `SKILL.md`: ask
   about products, not structure.
5. **Close by reading back** what was decided, who decided it, and what is still open.

Questions that map straight onto the decision register:

| Ask, on screen | Settles |
|---|---|
| *Who fills this in, and when?* | `OWN-01`, and the attribute's `Initial creation by` / `Subsequent enrichment by` |
| *Could you hand this on now? What is missing?* | `READY-01`, `READY-03` |
| *Who has to say yes before this goes live?* | `LIFECYCLE-01`; `ORGANISE-14` in `px-analyst` |
| *Where would this value come from, if nobody typed it?* | `OWN-01`, `DESCRIBE-06` |
| *Is this the same in every market, or just translated?* | `SCOPE-02` |
| *Would a customer choose between these on one page?* | `VARY-01` |
| *If someone changed this in the webshop, what should happen?* | `OWN-04` |
| *When this product is retired, what happens to its documents and relations?* | `LIFECYCLE-02`, `RELATE-05` |
| *Is there anything you looked for and did not find?* | `DESCRIBE-01` |

**What to watch for** matters more than what is said:

- **Workarounds invented on the spot**, such as a note in a description field or a second attribute
  used as a flag. Each is missing structure.
- **A step that needs another system open.** That is an integration or an ownership question.
- **Two roles who both think they own a field.** That is `OWN-03`, a `client` decision. Record it and
  escalate it. Do not resolve it in the room by whoever is louder.
- **Nobody claims a field.** Either it is not needed or it has no owner, and both are findings.

## What comes out

- **The decision log, updated.** Each `draft` row becomes `confirmed`, `refuted` (with what replaces
  it), or stays `open`. **A refuted draft decision is a result, not a failure.** It is what the
  workshop was for.
- **The ownership, scoping and readiness columns** filled for the draft's attributes. That is the seed of
  the Data Model File's Attributes sheet.
- **Corrections to 8.2 and 8.3**, and new pain points or requirements into 12.1, with the source given
  as the draft model workshop.
- **Notes per workflow:** step · role · expected · observed · gap.
- **What the draft did not test.** Fifteen articles say nothing about volume, about completeness at
  scale, or about the families that were not represented. State it, for the same reason section 11.6
  states what the Happy Flow did not prove.

## The Draft Model File

A small workbook. **Use the Data Model File's column names wherever they overlap**, so rows carry
straight over into the detailed model rather than being retyped.

| Sheet | Columns |
|---|---|
| **Articles** | Article · Source keys per system · Why chosen (width / depth / workflow) · Draft family · Workflows it carries · Decisions it tests · Data available |
| **Families** | Family code · Label · Articles · Variant levels · Variant axes · Decision IDs · Status |
| **Attributes** | Attribute code · Label · Type · Unit family · Families · Attribute group · Value per locale · Value per channel · Source system · Initial creation by · Approved by · Required for `<channel>` · Sample data · Status |
| **Option lists** | As in the Data Model File |
| **Roles** | Role · Role in 8.3 · Permissions · Workshop participant |
| **Workshop script** | Workflow (8.2) · Verb · Role · Article · Task · Expected result |
| **Decision log** | As in the Data Model File, plus **Status**: `draft` · `confirmed` · `refuted` · `open` |
| **Platform compromises** | As in the Data Model File |

**Every Articles row needs a reason in `Why chosen`.** An article picked because it was first in the
export teaches nothing.

Generate the sandbox's import file from this workbook, the same way the production import is generated
from the detailed model. It is disposable: delete it with the sandbox, and never edit it into a
production load file.
