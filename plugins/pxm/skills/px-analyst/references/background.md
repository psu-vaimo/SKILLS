# Product Information Ability Model — background

Everything that explains the register but is not needed with a client in front of you: the argument behind
each decision, the one live client test, every retired line and why, how individual lines changed, and the
counts history.

**The register itself is `ability-register.md`**; the workshop questions are `workshop-questions.md`;
current working notes are `pin.md`.

The habit worth keeping: several decisions in here were reversed once already because somebody questioned
them. Keeping the reasoning is what made that possible.

---

## How the register was built

**13 → 14: *ask them* is started, one domain deep — and it is far smaller than anyone thought.** Nine
questions cover all 21 `SOURCE` abilities **plus 22 more across eight other domains**: 43 abilities from 9
questions. The "205 questions" figure carried since draft 11.2 is wrong for the same reason the `Reveals`
estimate was — the facet is many-to-many. The whole register looks closer to **35 questions**.

`~hosts` is kept, with the reasoning recorded. No ability changed.

---

**12 → 13: the business-type facet is written.** Second of the eight. The four proposed types did not survive
contact with the register — the abilities that differentiate split on **two independent axes**, origin
(`~makes` · `~sources` · `~hosts`) and audience (`~direct` · `~indirect` · `~none`). 55 of 205 abilities
carry a type tag; the other 150 bite for everyone. No ability changed.

Two findings, one of them a correction to standing advice: **this facet scopes rather than narrows** — it is
not what makes the register walkable, which drafts 9–12 claimed. And `~hosts` owns exactly one ability
outright, which is worth knowing before relying on it.

---

**11.2 → 12: the `Reveals` facet is written.** First of the eight facets built, and the one decision 7 made
structural. Every ability tested against *what would this organisation have to acquire?* — yielding **31
capabilities**, tagged onto **120 of 205 abilities**, with 85 revealing nothing. No ability changed.

Three things came out of it that were not predicted: the register splits cleanly into **acquisition domains
and configuration domains**; the "well under half reveal something" estimate was wrong (it is 58%, corrected
in place); and five capabilities serve exactly one ability each — all five genuine point solutions, which is
the model's own warning rule working. `+damcheck` is retired into `+dam`.

---

**11.1 → 11.2: the reasoning behind decision 7.** Two questions the file gestured at but never answered —
why there are only ~20–30 capabilities behind 205 abilities, and why that layer is a facet rather than a
level between domain and ability. Both recorded under decision 7. Plus one finding: **`Reveals` and
cluster-type sibling tags are the same mechanism**, which should shorten the work when the facet is written.
No ability changed — still 205.

---

**11 → 11.1: decision 7.** The layer below abilities is settled. The capability layer is the `Reveals` facet
and always was; the feature layer (Bold, Italic) is deliberately out of scope, gathered per client and never
standardised. Closes a question left open since draft 2. No ability changed — still 205.

---

**10.1 → 11: notation only.** No ability was added, removed or reworded. Five changes to how the register is
written down:

1. **Domain identifiers spelled out** — `QUA-03` is now `QUALITY-03`. The three-letter codes were opaque to
   anyone who had not built them.
2. **Original domain names shown** in the domains table and section headings, in parentheses after the plain
   name.
3. **Sibling groups** — abilities that belong together now carry a shared `+tag`. See below.
4. **`[LU]` is now `[U]`.**
5. **Provenance marks share one bracket** — `[P] [Y]` is now `[P, Y]`.

**Old IDs still resolve.** The number never moved; only the prefix changed, so `QUA-03` and `QUALITY-03` are
the same ability and anything written against draft 10.1 or earlier maps mechanically. The mapping table is
at the foot of this section.

**One thing this fixed by accident.** `ORG` was both a domain code and a pillar name — the same string
meaning two different things on the same line, since draft 1. `ORGANISE` as the domain and `ORG` as the
pillar removes an ambiguity nobody had noticed.

---

**10 → 10.1: deletion.** A review of draft 10 found the one place the register had nothing to say —
*who may destroy product information, and what must be checked first*. Two abilities added, `QUALITY-16` and
`ORGANISE-26`. 203 → 205. A third candidate is raised for decision rather than added; see the `ORGANISE` commentary.

---

**Draft 9 → 10: first test against a live client artefact.** A consolidated business requirements register
from client **[Y]** — a large multi-market retailer of technical consumer goods, 150 consolidated
requirements rolling up 1,300 detailed items — was mapped onto the register. 86% of the board was exercised
by a client the model had never seen, in an industry none of the source material came from.

Changes in this draft:

- **23 abilities added** — 15 from the test's Tier 1, 6 from Tier 2, `ORGANISE-25` as the counterweight to
  `ORGANISE-21`, and `QUALITY-15` from the self-duplication finding. 180 → 203.
- **`ORGANISE-21` no longer stands alone.** [Y] is a considered counter-example; the line now has a partner and
  the "treat the ask with suspicion" framing is withdrawn.
- **A new provenance mark `[Y]`**, applied both to new lines and to existing lines that gained their first
  external corroboration.
- Three predictions confirmed, one arithmetic error corrected. See **What the [Y] test proved** below.

**What this is:** a union-of-all-businesses list of what an organisation can be *able to do* with product
information. No organisation has all of it — the point is to have the whole board visible when you walk into
a new one.

---

---

## Decision 7 — the layer below abilities

An early sketch had a third level under each ability, by analogy with a text-editor breakdown where the
leaves are Bold and Italic. It was deferred when decision 3 removed the maturity scale, and never resolved.
Resolved now, and the analogy turns out to mislead in a useful way.

**Your own definition puts a capability higher than Bold.** From `PX Terminology`: *a capability is something
in place to make the organisation capable of doing something else — used for IT capabilities such as "Have a
PIM"*. That is the **system** altitude. In the text-editor analogy the equivalent is not Bold, it is *have a
text editor*. Bold sits one level lower again, and is a different kind of thing.

|  | Capability — "have a PIM" | Feature — "Bold" |
|---|---|---|
| Examples | Have a DAM · an editorial team · a governance forum · a writer | Background removal on upload · rich-text fields · saved grid views |
| Roughly how many, behind 205 abilities | 20–30 | 600–1,000 |
| Shelf life | Years | Months |
| Vendor-neutral | Yes | No — it *is* the vendor's shape |

**The capability layer already exists: it is the `Reveals` facet.** *Wanting `ASSETS-11`, `ASSETS-12`,
`ASSETS-14` and `ASSETS-19` means you need a DAM* is an ability-to-capability statement at exactly the "have
a PIM" altitude. The hypotheses parked alongside it — `MODEL` revealing master data management beyond
products, `CONTENT` revealing a CMS or simply an unhired writer, `MEASURE` an analytics platform, `SOURCE` a
supplier portal, `ORGANISE-16` and `ORGANISE-19` a governance body that does not exist — are the rest of that
list. **Writing `Reveals` properly is writing the capability layer.** Nothing new needs inventing, and the
work is already on the pin.

**The feature layer stays out, for three reasons that are all reasons the register already relies on.**

*It is mechanism, and mechanisms date fastest.* That argument made AI a facet rather than a domain, and it
bites harder here: a feature list would be the most perishable thing in the register while looking exactly as
authoritative as the rest of it.

*It is where vendor bias re-enters.* A feature list is made of one or two vendors' shapes — whichever
products the author knows best. Draft 11 removed a vendor's name from the lineage; a feature layer would
quietly put it back as structure.

*It is the far side of the scope boundary* — advise on what the information must be and where it must reach,
not on the interface features that consume it.

And practically, features cost nothing to gather in the room. Nobody needs a checklist to discover that a
client wants saved grid views; they will say so unprompted.

**One exception, deliberately kept outside.** Formal vendor selection does need feature-level comparison.
Build it then as a **separate, dated artefact with a stated shelf life** — "feature comparison, valid Q3
2026" — referencing ability IDs rather than living inside the register. That keeps the perishable thing
perishable and this register durable.

### Why there are so few capabilities, and why they are not a level

Two questions fall out of decision 7: why roughly 20–30 capabilities behind 205 abilities, and why that layer
sits beside the register as a facet rather than between domain and ability. Recorded here because the answers
are load-bearing and the file otherwise only gestures at them.

**On the ratio — capabilities are lumpy, abilities are continuous.** You cannot buy 30% of a DAM. A
capability is a discrete acquisition: a system, a hired person, a standing forum, a budget line. The world
offers about a dozen kinds of system in this space — PIM, DAM, MDM, CMS, ERP, PLM, translation management,
syndication, analytics, supplier portal, workflow engine, taxonomy manager — and a handful of organisational
ones: a named owner, a team, a forum, a policy, a budget. That is close to the whole vocabulary. Abilities
are written at the grain of one sentence a person can answer yes or no to, which is far finer, and
deliberately so.

**The economics force the fanout.** A capability enabling exactly one ability would be a bad purchase —
nobody buys a system to do one thing. The ratio is therefore a property of what makes an acquisition worth
making, not an artefact of how the facet was written. Which hands the facet a diagnostic of its own: **a
capability that enables only one ability is a warning**. Either the ability is over-specified, or it is a
point solution that probably should not be bought.

**And the fanout is very uneven.** It is not 205 → 25. Probably well under half the register reveals anything
at all; the rest are things an organisation does with what it already has. `MODEL-14` — tell a one-way link
from one that points both ways — reveals nothing, because nobody buys a system for it. Closer to 80 abilities
clustering onto 25 capabilities, with 125 pointing at nothing. That is what the "where an ability reveals
nothing, record that too" guard is protecting.

**On why it is not a level, three reasons.**

*Structural.* It is many-to-many in both directions. `ASSETS-11` needs a DAM **and** an integration layer; a
DAM serves `ASSETS`, `DELIVER`, `PRESENT` and arguably `CONTENT`. A tree allows one parent, so a capability
level would force duplication — the same test that already disqualified Pillar, Business Goal and AI. Four
candidate levels rejected for one reason is no longer coincidence; it is the shape of the subject. **Almost
everything interesting about product information is a relation, not a containment.**

*Purpose.* Domains group abilities by what the business is trying to do. Capabilities group them by what you
would buy. Put capability in the middle and the tree reorganises around procurement — which is the
vendor-shaped model this register exists as an alternative to. It would become a product catalogue with
business language on top.

*Practical, and the one to lead with.* **A level is traversed on the way in. `Reveals` is computed on the way
out.** Walking domains and reading abilities aloud works because nobody has to name a system to ask the
question. A capability level would force "let us talk about your DAM requirements" *before* anything else,
reintroducing exactly the bad question the facet exists to replace. `Reveals` is an output, not an input.

### `Reveals` and cluster tags are the same mechanism

`+damcheck` — the sibling group over `ASSETS-11`, `ASSETS-12`, `ASSETS-14`, `ASSETS-19` — **is** the DAM
reveal. The cluster kind of sibling group and the `Reveals` facet are one mechanism under two names.

This should simplify the work when the facet is written: **a reveal is a cluster-type `+tag` plus one line
saying what the cluster points at.** It also explains why the tag notation already handles the two things a
reveal needs and a level could not provide — membership across domains, and one ability belonging to several
groups.

---

## Why AI is a facet

I argued in the first analysis that AI was a domain. That claim predates the language rule, and does not
survive it.

**It fails the consequence test.** "Let AI write product information" is a sentence about *how*. Written as a
consequence it becomes "produce usable text for forty thousand products without hiring forty writers" — and
the AI has disappeared from the sentence, which tells you it was never the ability.

**It is many-to-many with the tree.** AI touches translation, classification, asset tagging, text feedback,
extraction, quality reporting, recommendation and performance diagnosis — eight domains. That is the same
signature that disqualified Pillar and Business Goal as levels. A domain would force `ENRICH-11` to exist twice.

**Mechanisms date fastest.** Whether AI is good at translation changes yearly; the ability to translate does
not. A "Cloud" domain in a 2015 model would read badly today.

So AI is a **facet** — a mark on abilities where it changes the answer, useful as a second pass in a
workshop: *which of these would you answer differently if AI were good at it?* The facet can also carry the
note that a path is rarely taken in practice — see `SOURCE-18`.

Three things, though, are genuinely **new abilities** rather than old ones done a new way, and they get
ordinary homes: `PRESENT-18`, `DELIVER-15`, `QUALITY-10`.

---

---

## What the [Y] test proved

The register was mapped against a consolidated business requirements register from a large multi-market
retailer of technical consumer goods — 150 consolidated requirements over 1,300 detailed items, from an
industry none of the source material came from. **155 of 180 abilities were exercised: 86%.**

Discount that number before enjoying it. [Y] is an unusually large programme and lights up far more of the
board than an ordinary client would; a mid-size engagement might touch a third. The useful signal is not the
percentage but which lines went untouched, and why.

**Three predictions held.**

- The **DAM diagnostic** fired on three of its four triggers and matched an open decision already sitting in
  [Y]'s own key-design-decision list.
- The **business-type facet** predicted the `CONTENT` result exactly: a retailer, even one selling highly
  technical goods, does not carry the explain-the-specification burden — that sits upstream.
- The **attribution finding** was independently confirmed by another consultant cutting that exact
  requirement from a live register.

**Two holes were found that the corpus could not have surfaced** — `QUALITY-11` (what a valid value looks like)
and `QUALITY-12` (duplicates), with `QUALITY-13` (source precedence) close behind. All three are everyday problems
in any organisation taking data from more than one place. They were invisible for a structural reason:
discovery notes record pain points *as people articulate them*, and nobody says "we need attribute
validation rules" — they say "the data is a mess".

**One line met a real opponent.** `ORGANISE-21` carried an opinion and [Y] contradicted it for good reasons. That
is the most valuable output of the exercise, because it converted an opinion into a pair with a salience
rule attached.

**An unplanned confirmation of decision 1.** Seventeen of [Y]'s requirements were removed by their own
evaluator with the reason *"system function"* — reference entities, bulk actions, permission models, export
profiles. That is the **ability versus capability** line, drawn independently by a working consultant with
no knowledge of this model. Note the difference that remains: in this register those removed items are still
abilities the organisation has. The removal is a judgement about requirement-writing. But the line landing
in the same place is the strongest external evidence decision 1 has.

---

## The two source lists — reviewed, draft 19

`Serves` and `who cares` are the last two facets, and both draw on lists written in 2023, before this
register existed. Both were pulled from Tana and checked against the 205 abilities. **Neither survives as it
stands**, and the problems are different in each case.

### `Serves` — sixteen business-value statements

**Six of the sixteen are not business values.** They are abilities or capabilities, and they now live
properly elsewhere in the register:

| Listed as a value | What it actually is |
|---|---|
| *Enrich with high-quality product information* | `QUALITY-01` — an ability |
| *Enrich with product information from external databases* | `ENRICH-09` — an ability |
| *Enrich with product-level structure (variants)* | `MODEL-04` — an ability |
| *Enrich with catalog-level structure (categories)* | `MODEL-01`, `MODEL-07` — abilities |
| *Support PX team with a dedicated system* | `+pim` — a capability, and system-shaped |
| *Manage all sales channels in one place* | `MASTER-01` + `DELIVER-03` — abilities |

This matters more than tidiness. **Pointing an ability at one of these makes an ability serve another
ability**, which is circular and tells a client nothing. The list was written when the register did not
exist; the register has since absorbed six of its entries.

**Four more are one value with three examples.** *Reduce manual work with PX* plus *with file exports*,
*with file imports* and *with print* is a single value and a breakdown of it, not four values.

That leaves roughly **six genuine business values** out of sixteen — reduce manual work, reduce
time-to-market, increase order-completion, reduce returns, sell more by up-sell, sell more by cross-sell.
*Support Sales team* is a seventh but is audience-shaped rather than outcome-shaped and needs rewriting as a
consequence.

**And six gaps, all of them things the register now covers and the list cannot express:**

1. **Stay legal.** Five abilities and an entire capability (`+compliance`) — safety information, product
   passports, energy labels, restricted markets. Nothing in the list touches it, and it is the
   fastest-growing area of the subject since 2023.
2. **Reach a new market or channel without a project.** The whole `CONTEXT` domain, `DELIVER-02`,
   `DELIVER-17`, `+syndication`. Your older `Business value PIM` note had *expand into new markets* as a
   theme; it never reached this list.
3. **Stop being wrong in public.** `ORGANISE-22`, `QUALITY-16`, `ASSETS-05`, `PRESENT-10`. Wrong prices,
   wrong images, rights you did not have.
4. **Make the work bearable.** `ENRICH-01`, `CONTENT-01`, `CONTENT-02`, `ORGANISE-08`, `-09`, `-20`.
   Retention and onboarding speed. **Clients feel this most and articulate it least**, which is exactly the
   kind of thing a standard list should supply for them.
5. **Be found.** `PRESENT-03`, `PRESENT-18`, `+agentready`. Discoverability existed in 2023; being cited by
   an assistant did not.
6. **Know whether it worked.** The `MEASURE` domain. `MEASURE-08` says you cannot prove value — but being
   able to *argue* it convincingly is itself worth something.

**Verdict: rewrite before use.** Six entries retire into the register, four collapse to one, six are missing.
The finished list should be seven to twelve outcome-shaped statements, none of which names a system or an
activity.

### `Who cares` — five business roles

*Ecom mgr · Sales rep · Marketing mgr · End-customer · PIM mgr.*

**The most-served role in the entire register is missing.** Nobody on this list is *the person who enriches
products* — the editor, the contributor, whoever sits in front of the blank field. The `CONTENT` domain
exists for them (12 abilities), much of `ENRICH` (14), and `ORGANISE-05`, `-08`, `-09`. It is the single
largest constituency in the model and it is not on the list.

Six more are missing, ranked by how much of the register serves them:

| Missing role | Serves |
|---|---|
| **The supplier** | `SOURCE-10`, `-19`, `-24`, `-25` — an actor, not just a source |
| **The approver or owner** | `ORGANISE-14`, `-19`, `QUALITY-03`, `MASTER-06` |
| **Whoever owns the integrations** | most of `COLLECT` and `DELIVER`, `MODEL-17`, `-18` |
| **The compliance officer** | `+compliance`, five abilities |
| **The shop colleague** | `PRESENT-16` names them explicitly |
| **The merchandiser** | `MODEL-07`, `CONTEXT-03`, `-04`, `PRESENT-01`, `-02` |

**Two wording problems.** *PIM mgr* is system jargon and breaks the register's own language rule — name the
person by what they do, not by the tool they hold. *Ecom mgr* is channel-specific in a model that is
deliberately multi-channel; *whoever owns a channel* generalises it without losing anything.

**And the list is business-type-shaped without saying so.** All five are retailer-and-ecommerce roles. A
manufacturer's product manager, engineer or packaging designer appears nowhere — and since business type is
already a facet, roles probably want tagging by type too.

**Verdict: rewrite before use, and derive it rather than list it.** The 54 workshop questions already imply
their audiences — `ASK-12` is a question for whoever manages contributors, `ASK-11` for a sponsor, `ASK-31`
for compliance. **Working backwards from "who would have to be in the room to answer this?" produces an
evidence-based role list**, the same method that made `Reveals` cheap and correct.

### Why `who cares` earns its place anyway

Worth stating, because with five weak entries it would be fair to ask whether the facet is needed at all.
It is, and for a reason no other facet covers: **it decides who to invite.** A workshop with the right
questions and the wrong people in the room fails, and it fails in a way nobody notices until the report is
written. `Pillar` tells you what kind of thing is at stake, `business type` tells you whether to raise it at
all, `reveals` tells you what it will cost — none of them tells you whose diary to book.
---

---

## Line-by-line history, retirements and questioned lines

Commentary that lived under each domain: how lines were reworded, widened, split, retired or confirmed.

### `SOURCE`

*Five of the six interview-only lines in this domain gained external corroboration in draft 10. `SOURCE-15`
matters most: [Y] treats its own internal own-brand team **as a supplier**, routing them through the same
intake gateway — which is the sharpest possible confirmation that internal originators and external
suppliers are the same problem, and that renaming this domain in draft 5 was right.*

*On the five new lines: `SOURCE-22` is the one that relieves the constraint you identified in cluster 1.
`SOURCE-08` is having the capacity to chase suppliers; `SOURCE-22` is not needing it. `SOURCE-24` closes the other
half of self-service — [Y] calls the current state "supplier blindness", where a supplier can submit data
but cannot see what is already held about their own products. `SOURCE-25` is evidentiary and nobody asks for it
until the first argument.*

*`SOURCE-14` was reworded. It previously read "use what the supplier already has as the starting point", which
no organisation would ever answer no to — a truism, not an ability. The thing that is genuinely often absent
is the supplier's material being **in front of the person writing**: it arrives as a PDF in a purchasing
mailbox and never reaches the editor.*

*`SOURCE-10`, `SOURCE-19` and `SOURCE-15` now form a set: the supplier serves themselves, the internal originator
serves themselves, or somebody transcribes on their behalf. Most organisations need all three.*

**Retired**

- ~~`SOURCE-04` Get suppliers to deliver at all, in a form we can use~~ — false premise. Suppliers are
- ~~`SOURCE-07` Know where engineering data stops and commercial information starts~~ — not a real argument.

**Questioned**

- `SOURCE-05` Agree with a supplier what "complete" means before the first delivery — the interview suggests
- `SOURCE-06` Have the information ready when a product launches, not months after — never directly confirmed.

### `MASTER`

*`MASTER-06` now has three independent sources. It began as my inference in draft 1, was confirmed by [U]'s
"control which system owns which information", and appears in [Y] as a named foundational design decision
that the permission model depends on. An inferred line with three unrelated confirmations is as solid as
anything in the register.*

*But see `QUALITY-13`, added in draft 10. `MASTER-06` settles which system owns a whole **domain** of information.
It does not settle what happens when two sources both write to the same field — a different and far more
frequent problem, which had no home until now.*

### `MODEL`

**⚠ marks a Tier 2 line: real at [Y], not yet confirmed anywhere else.** These four were added on one
client's evidence. The model's own rule is that an ability should survive contact with an unlike
organisation before being trusted as generic, so treat them as provisional and watch whether the next test
raises them.

*`MODEL-17` may be the most consequential line added in draft 10. [Y] wants a new attribute live in about two
days with no IT change management. That is the difference between a data model that can evolve and one that
ossifies the day the project ends — and it connects directly to `ORGANISE-15`, getting IT time after the project
has closed. An organisation with `MODEL-17` needs far less of `ORGANISE-15`.*

*`MODEL-20` is the sharpest structural finding of the whole test and the one I am least sure of. [Y] lists
refurbished and box-damaged goods **one listing per physical unit, because each has unique damage to
describe and photograph**. Every other line in `MODEL` assumes a product record describes a kind of product,
not an individual object. If this generalises — and the second-hand and refurbished market is growing — it
is a hole in the foundations rather than a missing line. If it does not, it is one retailer's edge case.
Worth deliberately testing at the next opportunity.*

### `STATUS`

*`STATUS-06` and `STATUS-07` arrived from the PLM question. The boundary between engineering and commercial
information is clear for static data — the contested ground is entirely statuses, and it lands here. Both
were interview-only until [Y] confirmed them.*

*`STATUS-08` fills a gap the domain had carried since draft 3 without anyone noticing: every existing line
describes availability as a **state**, and none describes it as a **schedule**. [Y] needs embargo and launch
dates, pre-order windows with stock caps, and seasonal availability — a product fully prepared and held off
until an agreed moment. "Without anyone being there" is the load-bearing half of the sentence.*

*`STATUS-09` sits between markets and compliance. It is here rather than in `CONTEXT` because it is a control on
whether something may be sold at all, not a variation in how it is described.*

### `ENRICH`

*`ENRICH-09` stretches further than its wording suggests, and survives unchanged because of it. [Y] pulls from
commercial data pools **and** from a regulator's own database for energy-label content. "External product
database" covers a public authority as readily as a paid syndicator — worth knowing when the line comes up
in a compliance conversation.*

*`ENRICH-14` is confirmed in an unexpected form: [Y] needs an accelerated path for same-day launches driven by
a supplier's embargo lifting, not by a customer waiting at a counter. The ability is the same — bypass the
normal sequence when something cannot wait — and the wording holds for both.*

### `CONTENT`

> Helping a person produce good content. Distinct from `ENRICH`, which improves information mechanically. Here
> the constraint is a human being with a blank page and a deadline.


*`CONTENT-09`–`CONTENT-11` are pure human judgement with no technical component. They had nowhere else to go, which
is the strongest argument that this domain is real.*

*You named what each one is actually about: `CONTENT-09` is **relevance**, `CONTENT-10` is **clarity**, `CONTENT-11` is
**feeling**. With **distinctiveness** (`QUALITY-09`) these are the four qualities of content that completeness
does not measure. See the quality-axis note below — your answers resolved it.*

**Salience finding from [Y], draft 10.** `CONTENT-09`, `CONTENT-10` and `CONTENT-12` are all **absent** from [Y]'s
register, despite [Y] selling highly technical products across 1,300 requirements. This is not an oversight
— it is the business-type facet behaving exactly as predicted. A retailer buys supplier copy and worries
about tone and scale; the burden of explaining what a specification means to a buyer sits upstream with the
manufacturer. Mark `CONTENT-09` and `CONTENT-10` as **manufacturer-salient, low-salience for retailers** when the
salience facet is written.*

### `ASSETS`

*`ASSETS-02` was widened. It previously said "at any level", meaning levels of the product structure. [R]'s
material is more specific: an asset attaches to a single product, to a group of products, or to one
attribute — three different things, and the third is the one people forget.*

**Why this domain is worth its length.** You raised it, and the reason is diagnostic rather than
descriptive. A PIM has asset features; a DAM is a separate system with a separate budget and a separate
argument to win. **The way you find out which one an organisation needs is by walking this list.** An
organisation that wants `ASSETS-11`, `ASSETS-12`, `ASSETS-14` and `ASSETS-19` is describing a DAM whether or not anyone
in the room has said the word. One that only wants `ASSETS-02` and `ASSETS-03` is not.

That makes `ASSETS` the first domain in the register with an explicit second job: it is a set of abilities, and
it is also a decision instrument. Worth remembering when the *ask them* facet gets written — these questions
carry more weight than their number suggests.

**Tested against [Y] in draft 10, and it fired correctly.** [Y] hits three of the four triggers — `ASSETS-11`,
`ASSETS-12`, `ASSETS-14` — and their own key-design-decision list carries an unresolved *"native DAM versus the
separate DAM we already run"*. The register predicted, from requirements alone, a decision that was already
open in their file. First evidence that the Reveals facet does real work rather than merely sounding as
though it should.

`ASSETS-19` was the miss: nothing in 1,300 requirements covers getting assets to people working in layout and
design tools, even though [Y] produces print and in-store material. Ask about it rather than assuming it is
handled elsewhere.

**◐ `ASSETS-05` is absent from [Y], and that is worth watching.** A retailer whose imagery arrives entirely
from suppliers and data pools carries real licensing exposure, and not one of 1,300 requirements mentions
it. Two readings: either retailers systematically overlook image rights — which would make this a
high-value question precisely because nobody asks it — or it is a brand and manufacturer concern that
belongs at low salience for retailers. One more client settles it. `◐` marks a line whose salience is
genuinely unknown.

*Provenance note: most of what your graph holds on assets is [A] feature vocabulary — asset families,
asset manager, asset transformations, asset collections — rather than abilities. The abilities here were
recovered from [R]'s DAM theme and its as-is notes, from scattered client observations, and from you.
`ASSETS-14` is the generic form of "asset transformations"; `ASSETS-13` of "auto-assign image role"; `ASSETS-18` of
[R]'s document-management arrangement.*

### `QUALITY`

**Two of these are holes the model could not have found on its own, and they are the most important result
of the [Y] test.**

*`QUALITY-11` — nothing in the register said what a **valid value** looks like. `QUALITY-01` covers completeness
(is the field filled), `COLLECT-03` covers catching bad data as it arrives (did the transfer bring rubbish).
Neither covers formats, ranges, allowed characters, or "if this, then that is required". [Y] has it
explicitly, down to stripping hidden and invalid characters from identifiers on entry.*

*`QUALITY-12` — **the register had no ability about duplicates at all.** Not one line, across nine drafts. Every
organisation taking data from more than one source will eventually hold the same product twice, and [Y]
needs it three ways: a duplicate definition, governed unique identifiers, and the same item arriving from
two suppliers under different codes.*

*`QUALITY-13` is the subtlest of the three. `MASTER-06` decides which system owns a whole **domain** of
information; `QUALITY-13` decides what happens when two sources write to the **same field** — which is a
different question and a far more frequent one. [Y] hits it three separate times: a staging area with
control over what may be overwritten, update workflows that review changed attributes before accepting them,
and the master protecting its own enriched values against a supplier re-submission.*

**Why the corpus missed all three.** Discovery notes record pain points *as people articulate them*, and
nobody says "we need attribute validation rules" — they say "the data is a mess". It took a formal
requirements register, written in a different register of language, to surface problems that everybody has
and nobody phrases. That is a lesson about method as much as about content; see the pin.

*`QUALITY-14` will matter more, not less, as `ENRICH-06` spreads. [Y] requires AI-generated values to be flagged as
such. Once a machine and a person can both write the same field, "who wrote this" becomes a property of the
data.*

**`QUALITY-16` closes the register's blind spot on removal, added in 10.1.** Everything nearby was about
*keeping*: `MODEL-10` keeps old versions, `QUALITY-06` restores an earlier state, `QUALITY-07` protects a value from
being edited, `ORGANISE-23` recovers after loss. Nothing described what has to be true before something is taken
away — which category, bundle, assortment, related-product link, asset or live feed still points at it.
Delete a category tree and orphan three thousand products; delete a product and break the bundle that
contained it. This is the everyday version of a problem the register only had in its schema form.

*Note the pairing with `MODEL-18` ⚠, and keep them distinct. `MODEL-18` is knowing what breaks when you change
the **shape** — remove an attribute, restructure a tree. `QUALITY-16` is knowing what breaks when you remove an
**instance** — this product, this category node, this asset. Different questions, different people, usually
different answers.*

*`QUALITY-15` is `QUALITY-09` turned inward, and it came from [Y] having the concern in a form the model did not
anticipate. `QUALITY-09` is about looking identical to **competitors**; `QUALITY-15` is about looking identical to
**yourself** across your own channels, which search engines penalise. The second is the more common problem
for anyone running several channels, and it is the one an organisation can actually measure without outside
data — which is the objection that has always dogged `QUALITY-09`.*

### `ORGANISE`

*`ORGANISE-22` is a genuine hole and an embarrassing one to have carried for nine drafts. The register had **no
feedback path from the people who find errors** — store colleagues, the contact centre, customers. Every
domain described getting information in, improving it, and sending it out; none described what happens when
somebody downstream says "this is wrong". [Y] routes data defects and support tickets into measured fix
workflows and closes the loop by notifying whoever raised it.*

*`ORGANISE-23` — recovery — was likewise absent entirely. `QUALITY-06` covers going back to how one record looked;
nothing covered losing the lot, or undoing a bulk action that touched forty thousand products.*

**`ORGANISE-26` is the governance half of the deletion gap, added in 10.1.** `QUALITY-16` is the check; this is the
authority and the friction. Most organisations have never decided it — anyone who can edit can usually also
delete, and nothing stands between a tired person and an irreversible action. [Y] is explicit: irreversible
deletes restricted to break-glass accounts, sitting alongside a defined retention and housekeeping policy.

*Why `ORGANISE` and not `QUALITY`: this is a decision about who holds a power, which puts it beside `ORGANISE-19` (who is
allowed to decide) rather than beside the data-integrity lines. `ORGANISE-03` gives people access to what concerns
them; `ORGANISE-26` says that destroying is not an ordinary kind of access.*

**A third candidate, raised for decision rather than added.** [Y]'s material contains a distinct third
element the review comment did not name: **archive versus destroy, and for how long a deleted thing stays
recoverable.** They require defined criteria for archiving against full deletion based on likely future use,
a six-month window in which a deleted product can be reactivated or its code reused, and a retention policy
with a seven-year floor for financially-regulated services. Deletion is not binary — there is a state between
in-use and gone, and the criteria and the window are real decisions organisations get wrong.

It is well evidenced but it is one client, and it is arguably `MODEL-10` (keeping old versions) seen from the
other end, or `STATUS-07` (lifecycle) extended past discontinuation. **Your call**, and the three plausible
wordings are: *"Decide what is archived and what is destroyed"* · *"Say how long something stays recoverable
after it is deleted"* · *"Delete what we are obliged to delete, when we are obliged to"* — that last one is a
different ability again, since retention law sometimes compels removal rather than permitting it.

*`ORGANISE-24` is naming **concepts**, where `QUALITY-08` is naming **products**. [Y] is harmonising several legacy
status vocabularies into one and maintaining a legacy-to-future glossary as a change-management instrument
in its own right. Two people using the same word for different things is a cheaper problem to fix early than
late.*

*`ORGANISE-09` gained the `IT` pillar — a safe place to learn is a second environment, not only a curriculum.*

**On funding.** `ORGANISE-17` and `ORGANISE-18` are a pair, and you were clear which one is common. Product information
rarely funds itself; it gets funded as a **dependency of e-commerce**, on the argument that automating
product launches matters to the web. That makes `ORGANISE-18` the ability most organisations actually exercise,
and it has a consequence worth stating: when the thing you are attached to stops caring, the funding goes,
regardless of how well the work is going.

**On what is actually missing after a project.** People are usually there — product information teams have
staff. What disappears is **IT time** (`ORGANISE-15`) and what rarely existed in the first place is a **standing
forum between departments** (`ORGANISE-16`). Both were invisible in the source material because engagement notes
are written while the project still has both.

**On workflow — revised in draft 10.** `ORGANISE-21` used to stand alone and carried an opinion: most workflow is
implicit, it *should* stay that way, and a client asking for encoded workflow was to be treated "with some
suspicion" as a human impulse rather than a requirement.

[Y] is a considered counter-example. They want deeply encoded workflow — named steps with allotted times,
timestamping for compliance, condition-triggered starts, chained milestone sub-workflows spanning teams,
conditional skips, a guarantee of never returning past a completed milestone — and they want it against hard
targets: lead time 21 → 14 → 10 days, manual tasks from roughly 80% down to 30%, rework held near 5%. That
is not an impulse. It is an organisation whose process no longer fits in anyone's head.

So `ORGANISE-21` keeps its place and gains a partner, `ORGANISE-25`. **The pair is a genuine either/or that a workshop
has to resolve, and the register no longer prejudges it.** Implicit workflow is cheaper, more adaptable, and
survives reorganisation; encoded workflow is auditable, measurable, and does not depend on everyone
remembering. Which one is right is a question about size, and about how much of the process any single
person can still hold.

That yields a **salience** rule worth recording: `ORGANISE-21` is the question to raise with a small or mid-size
organisation, `ORGANISE-25` with a large one. Your own instinct here was calibrated on the clients you have had,
and [Y] sits at the far end of that range.

The "suspicion" framing is withdrawn. The impulse to encode collaboration into a system is real, but so is
the requirement, and the register should not decide in advance which one it is looking at. `ORGANISE-14`
(sign-off) remains the case where encoding earns its place regardless of size.

### `DELIVER`

*`DELIVER-13` and `DELIVER-14` were `[W]` lines — researched, never seen in the wild. [Y] validates both: attributes
checked against industry standards, and governed unique identifiers as a foundation requirement.*

*⚠ `DELIVER-17` and `DELIVER-18` are Tier 2, added on one client's evidence. `DELIVER-17` is [Y]'s abstraction-layer
requirement — a hub that owns per-system routing so that adding a consumer touches only the hub and never
the master. `DELIVER-18` separates **timeliness** from **correctness**: `COLLECT-05` covers staying in step,
nothing covered how fast. Both may be artefacts of an organisation with dozens of consuming systems.*

*`DELIVER-09` was split. It previously read "produce print material and PDFs from the same information", which
collapsed two different things your own `Standard Activities` node keeps apart: generating a datasheet with
nobody involved, and giving a designer live information to build a catalogue from. The first is automation;
the second is a working relationship with a design team. An organisation can easily have one and not the
other.*

### `PRESENT`

*`PRESENT-10` survives on unusual grounds, worth recording as a precedent. Logically it is derivable — if
`MASTER-01` and `DELIVER-03` are in place, consistency largely falls out. It stays because clients ask for it by
name and recognise it as the outcome they wanted. **The register tolerates a derived ability when the
organisation names it.** That rule may apply elsewhere; nothing else currently claims it.*

*Draft 10 vindicates that call. [Y] writes it as a requirement in almost the model's own words — consistent,
accurate product data across all channels and physical touchpoints, so customers see coherent information
everywhere. A line kept purely because clients name it was, in fact, named.*

**`PRESENT` scored lowest of all fifteen domains against [Y] — nine of fifteen — and that is the scope boundary
working, not the model failing.** The misses are `PRESENT-04`, `PRESENT-06`, `PRESENT-08`, `PRESENT-09`, `PRESENT-12` and
`PRESENT-17`: page layouts, sub-pages, self-filling teasers, publishing as web content rather than PDFs, and
packaging text. Most came from [U] and are **editorial-site** abilities. [Y] runs a commerce platform where
page composition belongs to the storefront — which is exactly the line the register draws in *Deliberately
out of scope*. Expect `PRESENT` to score low for any client whose storefront is somebody else's product, and do
not read it as neglect.

*`PRESENT-18` is the other `[W]` line confirmed by [Y], through a requirement for "AI/LLM discoverability". A
line added from research in draft 4, before any client had asked for it, turned up in a real register
sixteen months later.*

**Retired**

- ~~`PRESENT-13` Tell the product's story, not only its specifications~~ — **moved to `CONTENT-11`**. Storytelling is
- ~~`PRESENT-14` Show ratings, reviews and customer photos next to the product~~ — **out of scope**, see below.
- ~~`PRESENT-15` Let customers compare similar products side by side~~ — **out of scope**, see below.

### `MEASURE`

*`MEASURE-09` pairs with `MEASURE-08`. [Y] explicitly decides that the clock starts when a product leaves supplier
intake, excluding supplier wait time — a boundary decision, made before any measuring, that determines
whether the resulting numbers can be argued with. Without it, cycle-time figures are contestable in both
directions and therefore useless in the business case `MEASURE-08` describes.*

*`MEASURE-08` replaces a gap that asked for something nobody can do. The business case for product information is
**always** built on proxies — hours saved, time to market, returns avoided — and no client has ever
demonstrated what a specific change earned. Pretending otherwise would have put an unachievable line in the
register and quietly made every organisation fail it.*

**Confirmed independently in draft 10 — the model's strongest single validation.** [Y]'s register contains a
requirement to track conversion uplift, returns by brand and SKU, and average order value against
pre-go-live baselines, to evidence content-quality gains. **Another consultant, with no knowledge of this
model, marked that requirement `Remove`.** The attribution call was the most contested decision in the whole
build, and somebody reached the same conclusion from the opposite direction on a live engagement. What
survived in [Y]'s register is pure proxy — lead-time reduction, manual-task ratio, rework rate, defect-fix
turnaround — which is `MEASURE-08` and `MEASURE-03` describing a real business case.

*The honest ability has two halves, and `MEASURE-03` carries the second: argue the value, and then **prioritise
by the same logic you argued with** — worst information first, highest return rates, and making the best
sellers better. `MEASURE-03` was widened from the [A] original to say so.*

**Retired**

- ~~`[GAP]` Show what a change in product information actually earned~~ — **not achievable**. Replaced by
- ~~`[GAP]` Compare ourselves against last year, or against others~~ — **removed**. Harder still, and nobody

---

---

## Counts

| | Draft 3 | Draft 4 | Draft 9 | Draft 10 | Draft 10.1 | Draft 11 | Draft 18 |
|---|---|---|---|---|---|---|---|
| Domains | 14 | 15 (one proposed) | 15 | 15 | 15 | 15 | 15 |
| Abilities sourced | 62 | 108 | 180 | 203 | 205 | 205 | **205** |
| Still `[GAP]` | 22 | 16 | 0 | 0 | 0 | 0 | **0** |
| Retired | — | — | 7 | 7 | 7 | 7 | 7 |
| Provisional ⚠ | — | — | — | 6 | 6 | 6 | 6 |
| Sibling groups | — | — | — | — | — | 11 | 10 |
| Decisions settled | 5 | 5 | 5 | 6 | 6 | 6 | 7 |
| Facets written | 1 | 1 | 1 | 1 | 1 | 1 | **5 of 6** |
| Capabilities revealed | — | — | — | — | — | — | 31 |
| Type-tagged abilities | — | — | — | — | — | — | 55 of 205 |
| Workshop questions | — | — | — | — | — | — | 54, covering 205 |
| AI-marked abilities | — | — | — | — | — | — | **29** |

*Draft 11 changed no counts — it was a notation pass. The numbers repeat deliberately, as evidence that
nothing was lost in a rename that touched every line in the file.*

Draft 18 by domain: `SOURCE` 21 · `COLLECT` 10 · `MIGRATE` 4 · `MASTER` 6 · `MODEL` 20 · `STATUS` 9 ·
`CONTEXT` 5 · `ENRICH` 14 · `CONTENT` 12 · `ASSETS` 20 · `QUALITY` 16 · `ORGANISE` 26 · `DELIVER` 18 ·
`PRESENT` 15 · `MEASURE` 9.

**Added in 10.1:** `QUALITY-16` (know what breaks when we delete something) and `ORGANISE-26` (say who is allowed to
destroy information, and make it hard to do by mistake). Both from a review of draft 10, both corroborated
by [Y]. One further candidate — archive versus destroy, and the recoverable window — is raised in the `ORGANISE`
commentary awaiting a decision.

**The 23 added in draft 10:** `SOURCE-21`–`25` · `MODEL-17`–`20` ⚠ · `STATUS-08`–`09` · `QUALITY-11`–`15` ·
`ORGANISE-22`–`25` · `DELIVER-17`–`18` ⚠ · `MEASURE-09`.

⚠ marks the six **provisional** lines — added on [Y]'s evidence alone, not yet confirmed by an unlike
organisation. `MODEL-17`, `MODEL-18`, `MODEL-19`, `MODEL-20`, `DELIVER-17`, `DELIVER-18`.

*Arithmetic note: the [Y] evaluation report said Tier 1 was "fourteen lines" and projected 194 abilities.
Both were wrong — Tier 1 listed fifteen lines, and 180 + 23 = 203. Recounted here line by line.*

Plus two vocabularies that are not abilities: **eight kinds of product information**, and the **four content
qualities** mapped onto them.

`ORGANISE` 25, `SOURCE` 21, `ASSETS` 20 and `MODEL` 20 are now the largest domains. `ORGANISE` growing again is consistent:
across three drafts it has taken material from an interview, from a university, and now from a retailer's
programme governance. It keeps being where the work either survives or does not.

Retired, with reason: 2 false premises (`SOURCE-04`, `SOURCE-07`), 1 moved domain (`PRESENT-13`→`CONTENT-11`), 2 out of
scope (`PRESENT-14`, `PRESENT-15`), 1 unachievable (attribution), 1 removed (benchmarking).

---

## Draft 21 — client [S], the workshop test

**What was tested.** A six-hour As-Is discovery workshop at [S], a building materials buying cooperative:
a two-person central product information function serving 34 independently owned member companies across
six ERPs and just over a million articles. Origin `~sources ~hosts ~makes`, audience `~direct ~indirect`.
The union covers essentially the whole board — the second client in a row for whom business type scopes
away nothing, which is worth watching.

**Coverage: 181 of 205, 88%.** Higher than [Y]'s 86% and it means less. [Y] was a 1,300-line requirements
register; this was six hours of unstructured conversation in a federated organisation doing almost
everything at once. The number is a property of the room, not of the model. What the silences said matters
more, and they clustered cleanly enough to be worth recording as a pattern rather than a list.

**The artefact type turned out not to be new.** The intention was to test something other than discovery
notes — an RFP response, a governance policy. A workshop transcript is discovery notes with worse spelling.
Those three candidates are still open and the model still has one artefact type behind it, not two.

### Three ⚠ lines cleared

`MODEL-20`, `MODEL-17` and `DELIVER-18` each got a second source, and all three were raised unprompted.

`MODEL-20` is the one that matters, and it arrived by a route nobody predicted. The pin recorded that it
deserved an active question rather than passive waiting, on the grounds that if it held it was a hole in
`MODEL`'s foundations rather than a missing line. It held. [Y] needed it to list individual second-hand
goods. [S] needs it because a length of timber cut to an industry-standard dimension carries a different
climate footprint depending on the sawmill and the haulier's fuel, while the article number records only
the dimension. Safety data sheets produced the same shape independently within the same session: the
obligation attaches to the batch. Two organisations with nothing in common reaching the same line is the
strongest evidence the model accepts, and it now stands on convergence rather than on one client.

That forced the `~hosts` question. [S] does carry `~hosts`, so the tag was not falsified — but the timber
case has nothing to do with hosting third-party listings, and would bite at a pure manufacturer just as
hard. Keeping the tag would have kept the line out of every manufacturer conversation. It came off. The
consequence is that `~hosts` now owns no ability outright and shares all 17 with `~sources`, which weakens
the case the register made for keeping the value at all. That case rested on `SOURCE-09` reading
differently when there is no purchase order to lean on — still true, still unmeasured. Left standing,
flagged in the pin.

`MODEL-17` and `DELIVER-18` were both straightforward. [S] named being unable to change the shape of their
own information as the cause of their present situation: locked into a system, told it was being shut down,
and no further investment made after that. And they run both halves of `DELIVER-18` side by side today —
immediate push for most changes, an overnight run for name changes — so they were describing a difference
they live with rather than a preference they hold.

### Three that did not clear

`MODEL-18`, `MODEL-19` and `DELIVER-17` stay ⚠. Worth recording *how* they failed to clear, because the
three are not alike.

`MODEL-19` — running out of identifiers — was not raised at all, by anyone, in six hours. That is now
several clients in a row. It may simply be rare.

`MODEL-18` came close without arriving. The room spent real time on what breaks when a supplier deletes
data upstream, and on refusing to accept wholesale deletion — but that is `QUALITY-16`, removing an
instance, not `MODEL-18`, changing the shape. The pair held up under pressure, which is a quiet
confirmation that separating them was right.

`DELIVER-17` was the near miss. [S] adds destinations constantly — six ERPs, digital signage, shelf labels,
one member's own subscription, a national-account contract — and debated at length whether to map outbound
per receiver or push the mapping downstream. But that argument is `DELIVER-08` and `MODEL-08`. Nobody said
they could not add a destination without touching the master. An analysis that only ever confirms is not
listening, so this one is recorded as not confirmed.

### An opinion that was half wrong

The `CONTENT` salience note said `CONTENT-09` and `CONTENT-10` are manufacturer-salient because a retailer
pushes the explain-the-specification burden upstream. [S] pushes it upstream and still owns the problem.
They hold 2,650 attribute values that arrived from suppliers, and spent twenty minutes arguing about
whether *can be hung on a rack* belonged in front of a customer — with one participant admitting they could
not decode one of their own attribute abbreviations. That is relevance and clarity exactly, at a retailer.

The distinction that survives: **producing the explanation is the manufacturer's act; choosing what to show
from what arrived is the retailer's.** The `~makes` tags stay for now on one source. If a second retailer
produces the same argument, the honest fix is probably a new line for the selection act rather than
untagging these two, because the two acts need different people and different evidence.

### A rule that met a case it does not cover

The `+workflow` salience rule reads size: `ORGANISE-21` for a small or mid-size organisation, `ORGANISE-25`
for a large one. [S] is large by every structural measure and small by the only one that governs whether a
process fits in a head — two people hold it, and it does still fit, barely. Proposed replacement variable:
how many independent parties the process crosses. A federated organisation is large by that measure even
when its centre is tiny, and [S]'s process crosses 34 balance sheets. One source; recorded rather than
adopted.

### The ⚑ mark, qualified

`SOURCE-18` — extracting product information from documents written for another purpose — is marked ⚑
because it is discussed constantly and attempted rarely. At [S] it runs in production at scale, and has for
years: their industry data pool parses supplier declaration PDFs to pull climate figures, and their own
staff read product descriptions and key attributes in by hand. What the client cannot answer is whether any
given value landed in the right field, which is a different complaint from *we have not tried it*.

So the mark may be tracking who performs the work rather than whether it happens. An organisation can be
consuming document extraction it did not build, cannot inspect, and does not trust. Register note amended
to ask who performs it before discounting the answer.

### The point-solution rule counts one thing and needs two

`+datapool` was one of the five capabilities serving a single ability, and it passed the *is this worth it
on its own?* test as a genuine narrow purchase. At [S] it is the floor the business stands on: roughly
eighty per cent of all enrichment arrives through it, along with imagery and its type tags, environmental
assessments, climate data, hazard information, and — this is the part nobody had noticed — the validation
rules that decide when a product is fit to publish. Four abilities not tagged `+datapool` stop working if
the subscription ends.

Which is not hypothetical: the pool is being replaced by an industry successor that has said it will pass
supplier data through unvalidated. The client believes they own `QUALITY-01` and `QUALITY-11`. They rent
them, and the lease is ending.

**Generalised finding: how many abilities a capability bears and how much collapses without it are
different measurements.** The one-ability warning counts only the first. Both questions now stated in the
register.

### Candidate ability — proposed, not added

**"Know what the systems we deliver to are actually using."**

[S]'s most expensive single problem: activating a supplier centrally pulls in ten thousand articles, of
which perhaps a hundred are ever sold, and the two-person team enriches against the ten thousand because
nothing tells them which articles any member has switched on. The information exists — every member's ERP
signals it into the integration layer on the way to the storefront. It has simply never been read back.
The room worked this out for themselves mid-session and it is the cheapest available win in the engagement.

Where the model sits on it: `CONTEXT-04` is *controlling* which products belong to an assortment, which is
the outbound direction. `COLLECT` is inbound from source systems. `MEASURE` is about performance, not usage.
The gap is that **every `DELIVER` line points outward**, and there is no line for the master learning from
its consumers.

Held back deliberately. One source, and the model's own rule is that a candidate survives contact with an
unlike organisation before it is trusted as generic — a federated cooperative may be the only shape where
the master genuinely cannot see its own consumers. Test against a single-entity retailer before adding.
Probable home `MEASURE` or `DELIVER` if it survives.

### Recorded, no change

- `ASSETS-05` ◐ — absent a second time, from a second organisation whose imagery arrives entirely from
  suppliers. Two absences of the same shape sharpen the question without settling it. Next test must be a
  manufacturer or a brand.
- Business type scoped away nothing for the second client running. Both were doing almost everything. If a
  third does the same, the facet's claim to prevent embarrassment is worth re-examining — it may only earn
  its keep against genuinely single-shape organisations, which may be rarer than assumed.

---

## Draft 22 — client [S], the pain-point register

**A second artefact from the same client**, and the first time the model has been read against two different
source types describing one organisation. [Y] contributed a requirements register; [S] has now contributed a
six-hour workshop (draft 21) *and* 33 recorded pain points in the client's own graph. Comparing what each
surfaced is the most interesting result here, and it is a finding about method rather than about product
information.

**Coverage: 91 of 205, 44%** — against 88% for the workshop and 86% for [Y]'s requirements register. The
number is not a defect. **A pain-point list records what hurts now**, which is a third thing again: a
requirements register records what an organisation says it wants, a workshop records what it can describe,
and a pain-point list records only what has already become intolerable. Read the coverage as the shape of
their attention, not the shape of their practice.

### The two artefacts disagreed, and that is the useful part

Three ⚠ lines were assessed differently by the workshop and by the pain-point register — same client, same
month.

| Line | Workshop (draft 21) | Pain points (draft 22) | Resolution |
|---|---|---|---|
| `MODEL-20` | Confirmed — timber traceability, batch-level safety data | Never raised; "they handle articles, not individual items" | **Confirmation stands.** Silence in a narrower artefact is not refutation |
| `MODEL-18` | Near miss — the deletion discussion was `QUALITY-16`, not this | Confirmed — old category trees with surviving relations | **⚠ lifted.** New evidence the workshop did not surface |
| `DELIVER-17` | Near miss — nobody said they could not add a destination | Confirmed — six ERPs built separately | **⚠ kept.** See below |

**The general rule this produced: absence in a narrower artefact does not refute presence in a broader one.**
A pain-point list is a filter, not a census. `MODEL-20` was confirmed by specific evidence — a length of
timber carrying a different climate footprint by sawmill and haulier — and the fact that nobody wrote a pain
point about it means only that it has not yet become intolerable.

`DELIVER-17` is the one held back, and deliberately. The pain-point analysis cites the same row (PP13) for
four separate abilities, which is a sign of stretching, and the workshop had already reasoned through this
exact question and rejected it: six ERPs built differently is `COLLECT-06`, and no self-service trigger is
`DELIVER-18`. Neither is *add a destination without changing the master*. **An analysis that only ever
confirms is not listening** — the register's own rule, invoked here against a proposal to confirm.

### Confirmations

- **`ENRICH-13`** — third source, and near-verbatim: *"we cannot make exceptions so that only certain fields
  are not updated by the rules — it is either exception from updating entirely, or everything updates."*
  That is *steer the work field by field, not only product by product*, returned from an independent source.
- **`QUALITY-13`** — second source, and from an unlike organisation. Environmental data colliding between
  four schemes with no agreed rule for which wins, resolved ad hoc by the product team.
- **`QUALITY-11`**, **`MEASURE-09`**, **`SOURCE-18`**, **`ENRICH-09`** each gained `[S]`.

`MEASURE-09` is worth singling out: the client stated it themselves, unprompted — they have no baseline and
no consistent way to measure throughput or time to market. The model's position is that value cannot be
proven and the honest ability is arguing it well; this client had already arrived at the same place.

### `ASSETS` — zero of twenty, and the diagnostic fired anyway

**Not one of 33 pain points mentions images or documents.** The same organisation defines 24 asset types,
numbers image sub-categories 1–10 purely to control display order, relates documents to articles by hand or
by Excel round-trip, and keeps safety data sheets in an external service.

`ASSETS-11` is entirely absent, `ASSETS-13` is solved with a naming trick, `ASSETS-18` is in production. The
DAM diagnostic fires on all of it — **on evidence, with no complaint attached**. That is a sharper version of
the rule already in the register: the questions exist precisely because nobody complains about work they have
always done by hand. Silence here means normalised manual effort or genuinely low priority, and those lead to
opposite scopes.

### `+datapool` — the salience facet gets its first concrete case

Draft 21 recorded that the one-ability warning counts what a capability bears but not what collapses without
it. This client sharpens it into a business-type rule: **1.4 million articles arrive through the data pool,
and replacing it is a project in its own right that also removes the inbound validation.** A narrow
subscription for a `~makes` organisation is existential infrastructure for a `~sources` one. That is the
first time the salience facet has had a specific case to rest on rather than an assertion.

### The audience axis does not fit a buying cooperative

`~sources` on origin is clear. On audience, neither `~direct` nor `~indirect` describes selling to
**part-owners** — independent businesses running their own storefronts on shared data. It is visible in
`PRESENT` scoring 2 of 15 while the distribution question stays entirely live, and in `SOURCE-09` reading
differently: collective volume, but central agreements a member can decline. **One case. Recorded, not
adopted** — wait for a second chain or franchise.

### Candidates

**Confirmed as a second surfacing, still one client.** *Know which of our recipients actually has each
product* appeared independently in both the workshop and the pain-point register. It remains held back
because both sources are the same organisation, and a federated cooperative may be the only shape where the
master genuinely cannot see its own consumers. Test against a single-entity retailer.

**New, and compelling.** *Tell a customer that something we already sold has changed in a way the law cares
about.* Safety data sheet updates that must reach named B2B buyers within a statutory window. `DELIVER-12`
is *show the required safety information in every listing* — a pull ability. `DELIVER-04` covers producing
and retaining the documents. **Neither covers notifying somebody after the sale**, against a named recipient,
inside a legal deadline. One source; proposed rather than added; probable home `DELIVER` with `+compliance`.

**Watch.** *Mark information that nobody updates as having gone stale* — `QUALITY-05` and `ENRICH-12` sit
close and may already cover it; possibly a rewording rather than a new line. And *run and re-run our own data
flows without asking the vendor*, which may be `ORGANISE-15`, `DELIVER-18` and `MODEL-17` acting together.

### Recorded, no change

- `MODEL-20` was asked actively at the wrong client. A buying cooperative handles articles, not individual
  physical units. The active question still needs a client whose goods are individuated.
- `MODEL-19` touched only indirectly. Now several clients without a direct hit.

---

## Client [S], the export — the fifth artefact and the first that is not testimony (2026-10-05)

**What was tested.** The full export of [S]'s outgoing PIM — 3.4 million articles, 22,442 variant
groupings, 520,000 image and 118,000 document records, and the system's own attribute definitions, class
lists and value lists — audited with `px-data-audit` and mapped per ability. No register change; this
section records the test.

**Verdicts had to be redefined for data.** An extract records what *is*, so the scale is held (done and
used) · partial (structure exists, barely used or self-contradicting) · missing (shown not done) · silent
(an extract cannot say). That is still has-it / doesn't-have-it — partial is a *has it badly*, not a rung.

**Coverage: 105 of 205, 51%** at first mapping (held 66, partial 33, missing 6, silent 100), **109 (53%)**
once the audit's remaining checks ran the same day — `MODEL-14`, `QUALITY-16`, `COLLECT-03` and `CONTEXT-05`
moved from silent to partial. On 2026-10-06 the client's answers re-scored three lines without changing
coverage (now held 65, partial 38): `MODEL-19` partial → held, because no system is 7-digit-bound; and
`DELIVER-09`/`DELIVER-16` held → partial, because the print engine exists but is unused. That a silent line can be moved by running a check is itself the difference from
testimony: a room's silence stays silent. Between the workshop (88%) and the
pain points (44%), and comparable to neither: it is the first number that is a property of a system rather
than of a conversation.

### The shape inverts testimony

The data speaks most about `ASSETS` (80%), `ENRICH` (79%), `STATUS` (78%) and `MODEL` (75%), and least about
`MEASURE` (11%), `ORGANISE` (15%) and `SOURCE` (19%). Testimony runs the other way: people talk readily about
governance, suppliers and value, and not at all about images. **The two artefact types are halves, not
alternatives**, and the split follows the register's acquisition/configuration line broadly — the data
sees what is configured and is blind to what is bought, staffed or agreed. A discovery that runs only one
of them misses a predictable half of the board.

### Outcome classes against drafts 21 and 22

**Corroborates.** The `ASSETS` diagnostic fired on evidence a third time (12 abilities held, image
categories and numbered sub-categories, 145,296 images reused across articles; zero pain points).
`QUALITY-13` — supplier and trade-database descriptions both kept, differing on 89%; four classification
schemes side by side. `ENRICH-09` — trade-database fields on every article. The ten-thousand-articles
problem — 76% of the base is past its expiry date and still there.

**Refines.** `MODEL-17`: the workshop named being unable to change the shape of their own information; the
data shows ~2,650 definitions created in-house in 2019–2023 (the rest a 2025 ETIM import). The ability was
present and used freely enough to proliferate — what was missing was governance over it (`QUALITY-04`
missing). **A complaint can be real and still name the wrong object**, and only a non-testimonial artefact
can show which. `QUALITY-01`/`QUALITY-11` "rented from the pool": the export holds validation structures of
its own, so the rental is probably of *enforcement*, not of the rules — narrow the draft 21 finding.

**Reveals.** No lifecycle exists as such (`STATUS-07` missing — one status value on 99.3%, the real signal
split between an expiry date and a web flag that disagree on 268,189 articles). Short descriptions are a
mechanical cut of the long ones (`CONTENT-04` missing). One image stands in on 17,480 articles. The variant
groupings have no identity outside the PIM. None of these was said, and none could have been — people do
not report what their system does by default.

### What it means for the model

- **No line failed.** Nothing in the export needed an ability the register lacks, and no new candidate
  arose. Two oddities map nowhere (integration credentials on partner records; a register of URL objects)
  and both look like scope edges rather than holes.
- **`MODEL-19` was measured the same day, and holds** — see the next section.
- **The verdict scale is worth keeping for the next extract.** Partial carried a third of the evidence:
  structures that exist and are not used are the most common thing an archaeology export shows, and a
  binary scale would have hidden them as either held or missing.

### `MODEL-19` measured — the silence was the wrong instrument

Four testimonial artefacts, two clients, no direct hit, and retirement had been on the table. The export
settled it in one pass. [S]'s ERP key wraps a trade-database article number that is **seven digits and 93%
consumed** — 3,380,556 values between 1,264,291 and 9,301,267, assigned in rising sequence, the frontier
advancing about 276,000 a year. At that pace it passes 9,999,999 around 2029, and that is a lower bound
because the database numbers for all of its customers, not only this one. The ERP pads the number to nine
digits, so the ERP itself has room; nothing has been reused. What is coming is a **width rollover**: every
label, rule, integration and field that assumes seven digits breaks on the same day, and nobody in the
organisation has said so because nothing has broken yet.

**The method lesson is the important one.** An ability whose failure is *discovered* rather than *felt* will
read as silence in every testimonial artefact, however many are collected — four silences were not four
pieces of evidence, they were one instrument used four times. The pin's rule, *a silence from an artefact
type that could never have raised the line is weak evidence*, is now confirmed by the case that prompted it.
Worth generalising beyond `MODEL-19`: before retiring any line for silence, ask whether its failure mode is
one anybody would ever say out loud.

**Register status: ⚠ lifted and `[S]` added, 2026-10-05**, on Pontus' decision. The line's consequence —
something actually breaking — still depends on which systems are seven-digit-bound, which only [S] can
answer; that is a question for the engagement, not a condition on the line. One ⚠ remains: `DELIVER-17`.

