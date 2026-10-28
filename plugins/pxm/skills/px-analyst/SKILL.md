---
name: px-analyst
description: Analyse an organisation's product information (PX/PXM/PIM) practice, prep or run a discovery workshop, or continue building Pontus' generalised Product Information Ability Model. Use for "analyse this organisation's PIM/PXM setup", "what should I ask in this discovery", "does this client need a DAM", "prep a PX workshop", "evaluate this requirements register", or any work extending the ability model itself. The model is a reference file this skill consults, not something to recite from memory.
---

# PX Analyst

Helps analyse an organisation's product information practice against a generalised, union-of-all-businesses
**ability model** — built from Pontus' PX/PXM engagement notes, sharpened by interview, tested against two
live clients, and deliberately kept independent of any one vendor or client. Also used to keep building
that model.

## Read first

| File | For |
|---|---|
| `references/ability-register.md` | **The board.** 15 domains, 205 abilities with all four tag types, the facet legends, the two vocabularies, the decisions. What you scan. |
| `references/workshop-questions.md` | **The instrument.** 54 questions — what each covers, who to invite, what to listen for. What you carry into a room. |

Two further files live in `/Users/pontus/Documents/Claude/`, outside this skill: `px-model-background.md`
(every decision's argument, the live client test, retirements, how lines changed) and `px-pin.md` (current
working notes). Consult the background only when a choice is challenged or being revisited.

**Load the file you need — do not answer from memory.** The register carries IDs (`SOURCE-14`, `ASSETS-11`),
provenance marks and tags; a summary from memory drifts and loses the IDs that make it citable.

## What this model is

A list of what an organisation **can be able to do** with product information — not what any one
organisation has. No organisation has all 205; the model exists so the whole board is visible before walking
into a new one, the way a text-editor feature breakdown lists RTF *and* Docx *and* PDF export without any
single editor having all three.

It has been tested against **two clients and five artefacts**: a large retailer's 1,300-item requirements
register (86% of the board, three predictions held, one opinion overturned, two foundational holes found),
and from a building materials buying cooperative a six-hour workshop (88%), 33 recorded pain points (44%),
a two-part To-Be workshop, and a full legacy-PIM export (53%) — the first non-testimonial artefact, loud
exactly where testimony is quiet (`ASSETS`, `STATUS`, `MODEL`) and nearly mute on `ORGANISE`, `SOURCE` and
`MEASURE`. Four ⚠ lines cleared, one business type tag removed, two of the model's own rules found to be
measuring the wrong thing. Treat it as load-bearing but not finished.

**Artefact type changes what you see, and the coverage percentage is a property of the artefact, not the
model.** A requirements register records what an organisation *says it wants*; a workshop records what it
*can describe*; a pain-point list records only what has *become intolerable*. **Absence in a narrower
artefact does not refute presence in a broader one** — a pain-point list is a filter, not a census.

## Rules that govern the model — apply these, do not relitigate them

- **Ability, not capability.** An ability is something the organisation can do; a capability is something in
  place that makes it able (a system, a role, a policy). This model lists abilities; the capability layer
  lives in the `Reveals` facet — see decision 7 below.
- **No maturity scale, no ordering.** Assessment is has-it / doesn't-have-it. Never rank or score abilities
  against each other — "Bold is not better than Italic."
- **PXM scope, not PIM scope.** Presentation to the customer is in scope.
- **Plain language, always.** Every line must be sayable out loud to someone who has never heard the word
  PIM. State the **consequence, not the mechanism** — "handle the amount of data we actually have" not
  "sustain integration throughput". No system names, no client names, no stacked nouns. If a line needs a
  gloss, the line is wrong, not the reader.
- **Scope boundary:** advise on what the information must be and where it must reach, **not** on the
  interface features that consume it. Marketplace rules and packaging text are in scope because they are
  demands on the information. Review display and product comparison are out because they are demands on the
  interface — see "Deliberately out of scope" in the reference.
- **IDs are permanent.** Never renumber. Retire a line and record why rather than deleting it or reusing its
  ID.
- **The layer below abilities is settled (decision 7).** The **capability** layer — "have a DAM", "have a
  governance body" — is the `Reveals` facet, and writing that facet *is* writing the third level of the
  model. The **feature** layer below it (background removal, saved grid views) is deliberately out of scope:
  it is mechanism, it dates in months, and it is where vendor bias re-enters. Gather features per client in
  the room, never standardise them, and if formal vendor selection ever needs a feature comparison, build it
  as a separate dated artefact referencing ability IDs.
- **`°core` / `°shifts` mark AI, inline beside the pillar.** 29 abilities. `°core` (6) barely exist without
  AI; `°shifts` (23) predate it and survive without it. **AI is not a fourth pillar** — pillars answer *what
  kind of thing must be true* (technology, people, data) and AI is a kind of technology, so it would sit
  beside `IT` the way "Cloud" would. What it is instead: **a modifier of the three that exist.** 24 of the 29
  carry no `ORG` pillar, because AI output is probabilistic and somebody must accept, review or absorb being
  wrong — so **the `°` mark carries an implied organisational cost that appears only if the AI path is
  chosen**, and that is the cost clients forget to budget.
- **⚑ is *rarely done well*, not *rarely tried*** (5 abilities). One client runs `SOURCE-18` in production
  at scale and its own complaint is that the output is unreliable. **Ask who performs it and whether anyone
  checks the result** — a client who says "we already have AI reading PDFs" then meets the right follow-up.
  Ask the AI question as one late pass: *"which of these would you answer differently if AI were good at
  it?"*
- **⚠ marks a provisional line.** One remains — `DELIVER-17`. `MODEL-19` cleared in 2026-10 **by measurement**:
  four testimonial artefacts never raised it, then `[S]`'s export showed an article number 93% through its
  digit width. Running out is discovered, not said — **before retiring any line for silence, ask whether its
  failure is something anybody would ever say out loud.** `DELIVER-17` is
  **held against a proposal to confirm it** — one analysis read six differently-built ERPs as evidence, but
  that is `COLLECT-06`, and no self-service trigger is `DELIVER-18`; neither is *add a destination without
  changing the master*.
- **`MODEL-20` still wants a client whose goods are individuated.** Confirmed once, by commodity
  traceability. A buying cooperative handles articles, not physical units, so it was the wrong place to ask.
- **◐ marks unknown salience.** Currently only `ASSETS-05` (image rights) — absent from **two** organisations
  that both source imagery from suppliers. **The next test must be a manufacturer or a brand**, where rights
  are created rather than received.
- **`ASSETS` silence is the loudest signal in the model.** At one client, *zero* of 33 pain points mentioned
  images or documents — while the same organisation defined 24 asset types, numbered image sub-categories
  1–10 to control display order, and related documents to articles by Excel round-trip. **The diagnostic
  fires on evidence, not on complaints**, because nobody complains about work they have always done by hand.
  Walk `ASK-19`, `ASK-20`, `ASK-23`, `ASK-24` before any scope is set.

## Notation

- **IDs** are `DOMAIN-NN` in full words — `QUALITY-16`, `SOURCE-22`. Draft 11 replaced the old three-letter
  codes (`QUA`, `SRC`); the number never moved, so anything written against draft 10.1 or earlier still
  resolves. The mapping table is in the reference.
- **Watch the one collision that remains:** `ORG` is a **pillar** (`IT` · `ORG` · `DATA`), while `ORGANISE`
  is the **domain**. On an ability line the first backticked group is the ID and the second is the pillar.
- **Provenance** shares one bracket: `[P, Y]`, not `[P] [Y]`. **No client is named anywhere** — sources are
  `[R]` a steel manufacturer, `[U]` a university, `[X]` three further engagements (`V`, `O`, `H`), `[Y]` a
  large multi-market retailer, `[S]` a building materials buying cooperative. Business type is kept because the salience facet depends on it; identity is
  not. Keep it that way in anything you write, including client-facing evaluations.
- **`+tags` mark sibling groups** — abilities that only make sense next to each other. An ability can carry
  more than one. Eleven groups exist, listed with their kind in the reference. **The kind is what matters in
  a room:** an `either/or` means pick one and the choice is the finding; a `set` means partial coverage is
  the finding; a `cluster` means the pattern is the finding, not any single line.
- **`Reveals` is written (draft 12).** 31 capabilities tagged onto 120 of 205 abilities — each `+tag` names
  something the organisation would have to **buy, staff, fund or agree**. Read the Reveals table in the
  reference before any workshop; it is the fastest route from what a client says they want to what it will
  cost them.
- **The acquisition/configuration split is the most useful thing it produced.** `ORGANISE` (88%), `PRESENT`
  (80%) and `SOURCE` (71%) are nearly all acquisition — things you buy, staff or fund. `STATUS` (11%),
  `CONTEXT` (20%), `ENRICH` (28%) and `MODEL` (35%) are nearly all configuration — things you set up in what
  you already own. **A client "doing a PIM project" is usually thinking about the configuration domains,
  where nothing has to be bought. The money is in `ORGANISE`, and nobody puts it on the agenda.**
- **Five capabilities serve one ability each** (`+configurator` `+datapool` `+instore` `+recovery`
  `+rivalwatch`). All are genuine point solutions — ask *is this worth it on its own?* **then ask what stops
  working if it is withdrawn.** Those are different measurements and the one-ability warning counts only the
  first: at the second client, `+datapool` bore one ability and carried four more that were not tagged with
  it, including the validation rules the client believed they owned. **It also depends on business type** —
  a narrow subscription for a `~makes` organisation is existential infrastructure for a `~sources` one, with
  1.4 million articles arriving through it.
- **Silence is data.** 85 abilities reveal nothing, and `SOURCE-09` reveals nothing on purpose: supplier
  leverage is a market position, not something you can buy, hire or convene.
- **`Ask them` is COMPLETE (drafts 14–17).** 54 questions covering all 205 abilities, every domain. The facet is
  many-to-many like the rest — final ratio 5.0, sliding from 5.6 for narrative domains to 3.7 for `MODEL`.
  **Nobody runs all 54.** A session uses eight or ten, chosen by which domains are live. `ASK-01`, `ASK-12`,
  `ASK-32` and `ASK-48` between them reach 24 abilities across nine domains — a serviceable first session on
  their own.
- **For structural domains, ask about products, not structure.** `MODEL` was unanswerable until the questions
  stopped asking about data models and started asking about *the awkward product*, *the one with versions*,
  *the one built to order*. Real products break data models; describing one surfaces the structure without
  anybody needing the vocabulary.
- **Let the DAM diagnostic fire on its own.** Its four triggers are spread across `ASK-19`, `ASK-20`,
  `ASK-23` and `ASK-24` and none of them mentions asset management. Asking directly invites an aspiration or
  a defence; asking about a photograph, the kinds of picture, the designer's copy and volume lets the client
  describe the need themselves — which makes the finding theirs. **Use the
  questions, not the ability statements, in a room.** An ability read aloud invites agreement and gets it;
  the questions are written to make a *no* discoverable. The rule: **ask for an instance, not an
  assessment** — when did this last happen, who did it, what did it cost — and never use the ability's own
  vocabulary, which invites the rehearsed reply.
- **Write further questions in dependency order, not domain order.** They span, so a new domain's set must
  account for what existing questions already answered or the same story gets asked for twice in one room.

## Using the register to analyse a real organisation

1. **Scope, then narrow — they are different jobs.** **Business type** (written, draft 13) *scopes*: two
   axes, origin `~makes`/`~sources`/`~hosts` and audience `~direct`/`~indirect`/`~none`, multi-valued, union
   filter. Only 55 of 205 abilities carry a tag, so it removes the ~25 lines that would be actively wrong to
   raise and little else. **It does not make 205 walkable** — narrowing has to come from choosing which
   domains to walk, or later from salience. Known findings so far:
   - `CONTENT-09` and `CONTENT-10` are **manufacturer-salient for producing the explanation** — a retailer
     pushes that burden upstream. But they bite at retailers on a second layer: choosing which of the
     supplier-supplied values a buyer can interpret at all. **Producing the explanation is the
     manufacturer's act; choosing what to show from what arrived is the retailer's.**
   - `ORGANISE-21` (run the process without encoding every step) is the **small/mid-size** question;
     `ORGANISE-25` (encode the steps) is the **large-organisation** one. A genuine either/or — do not present
     either as preferred. **Headcount is probably the wrong variable**: a two-person central function serving
     34 member companies is large by every structural measure and small by the only one that governs whether
     a process fits in a head. **Try counting how many independent parties the process crosses.** One source,
     not yet adopted.
   - `PRESENT` scores low for any client whose storefront is somebody else's product. That is the scope
     boundary working, not neglect.
   - **The audience axis has a gap.** A buying cooperative or voluntary chain sells to **part-owners** —
     independent businesses on shared data — which is neither `~direct` nor `~indirect`. One case, recorded
     not adopted. `SOURCE-09` also reads differently there: collective volume, central agreements a member
     can decline.
2. **Walk domains, not the whole list.** Pick the domains most likely live for this client, starting from
   what they are asking for, and read the abilities aloud — they are already workshop-ready.
3. **Watch for `Reveals` clusters.** A group of related asks is often the organisation describing a system it
   has not named. `ASSETS` is the proven case: wanting `ASSETS-11`, `ASSETS-12`, `ASSETS-14` and `ASSETS-19` describes a DAM
   whether or not anyone says the word — this fired correctly against a real client and matched a decision
   already open in their own file. Other domains remain hypotheses (see the Reveals facet).
4. **Separate the record from the content.** Completeness (are the fields filled) and the four content
   qualities (relevant, clear, distinctive, evocative) are different axes, and the four apply only to
   descriptive content and imagery. Do not chase "distinctive" on a compliance field or an article number.
5. **On value and ROI:** never ask a client to prove what a change in product information earned — nobody
   ever has, and an independent consultant reached the same conclusion on a live engagement. The honest
   ability is arguing the value on proxies (`MEASURE-08`) and prioritising by that same logic (`MEASURE-03`). Check
   they have agreed where the clock starts before they measure anything (`MEASURE-09`).
6. **When something in the register does not fit what you are seeing**, say so rather than forcing the client
   into the model. A line that fails against a live case is exactly the kind of finding that has improved the
   model twice now — flag it to Pontus rather than silently working around it.

### Evaluating a written artefact (requirements register, RFP, policy)

The first live test was a spreadsheet, not a workshop, and this is now a supported mode.

- Map each requirement to an ability ID; count coverage per domain. Expect a *high* percentage from a large
  programme and discount accordingly — a 1,300-requirement register lights up far more of the board than a
  mid-size client would. **The signal is which lines went untouched, and why**, not the percentage.
- **A register records what an organisation says it wants, not what it can do today.** Read coverage as the
  shape of their ambition — a good proxy for where they know they are weak, not a capability assessment.
- Read the *excluded* rows too. How an evaluator scoped things out is as informative as what they kept: in
  the first test, seventeen removals reasoned "system function" reproduced this model's ability/capability
  line independently, and one removal independently confirmed the attribution finding.
- Requirements that map nowhere are the yield. Propose them, tiered by confidence, rather than adding
  straight in.

## Extending or revising the model

Working rules learned from building it and from the first live test:

- **Test generality against an unlike case.** Harvested from a steel manufacturer, tested against a
  university with no products, then against a retailer's requirements register. Each survived without
  restructuring — that is what validates the frame. A new ability should survive contact with an unlike
  organisation before it is trusted as generic; until then mark it ⚠.
- **Test a different artefact type, not just a different client.** The biggest finding of the first live test
  was structural: a formal requirements register states *what must be true*, where discovery notes record
  *what hurts*. That difference surfaced holes nine drafts of notes could not — nobody says "we need
  attribute validation rules", they say "the data is a mess". Next candidates: a vendor RFP response, a
  data-governance policy, an ISO-style process document.
- **State a consequence, ask for a consequence.** When interviewing to fill a gap, ask "what breaks when this
  is missing" rather than "what feature would you want". Mechanism answers ("let AI do X") get translated
  back to consequence before they are added.
- **Be willing to retire, not just add.** An interview or a test that only ever adds is not being listened
  to. Lines have been cut for being false premises and for being truisms nobody would answer "no" to. Do not
  patch a wrong line — retire it with a stated reason and write the real one.
- **Be willing to reverse an opinion.** `ORGANISE-21` used to carry a preference and a note telling the reader to
  treat a client's contrary ask "with suspicion". A real client contradicted it for good reasons, so it
  gained a partner (`ORGANISE-25`) and the suspicion was withdrawn. Where the model has a view rather than an
  observation, that view is a liability until tested.
- **Sort before you fill.** Given a list of candidate gaps, the most useful answer is sometimes "not ours"
  rather than a generic line invented to fill space. Two `PRESENT` abilities were cut that way and it produced
  the model's sharpest scope boundary.
- **Convergent findings from unrelated sources are the strongest signal.** "Filled is not the same as good"
  arrived independently from a university, a retailer answer and a manufacturer answer, and became the second
  quality axis. `MASTER-06` now has three unrelated confirmations. One source is usually not yet enough.
- **A derived line can still earn its place if the organisation names it.** `PRESENT-10` is logically just a
  consequence of `MASTER-01` + `DELIVER-03`, but clients ask for it by name — and the live test then found it
  written as a requirement in almost the model's own words. A precedent, not a licence to add derived lines
  freely.

### Working file conventions, if editing the register

- **The model is four files** in `/Users/pontus/Documents/Claude/`, split at draft 20: `px-ability-register.md`
  (the board), `px-workshop-questions.md` (the 54 questions), `px-model-background.md` (all reasoning,
  retirements, line history, the client test) and `px-pin.md` (what happens next). Drafts 1–20 are kept as
  `px-ability-model-N.md` for history.
- **Reasoning goes in the background file, never in the register.** The register grew to 2,500 lines because
  every argument was written next to the thing it justified; the domain sections ended up with more
  commentary than abilities. Keep the register to what you would have open with a client.
- Read `px-pin.md` before assuming what is next.
- Record *why* alongside *what*. The italic commentary blocks under each domain are the reasoning that makes
  the register defensible in a room; keep writing them.
- Retired lines stay visible with `~~strikethrough~~` and a one-line reason. Never delete one — the reasoning
  is as valuable as the surviving register.
- **Recount, do not carry counts forward.** Draft counts drifted low twice by being estimated rather than
  counted, and the [Y] evaluation report shipped with two arithmetic errors. Count the ability lines, and
  note that `SOURCE-05` and `SOURCE-06` sit under "Questioned" and are excluded from domain totals by convention.
- After a meaningful revision, resync **both** `references/ability-register.md` and
  `references/workshop-questions.md` from the working files, and send what changed via `SendUserFile`.

## Serves and who-to-invite

- **`Serves` — 13 goals (`→G01`–`→G13`), rewritten in draft 20** after the 2023 list failed review: six of
  its sixteen entries were abilities in disguise, which made them circular. **All 205 abilities serve at
  least one goal**, because `serves` answers *"why should we care?"* and a line without an answer has no
  justification.
- **The register argues cost and risk far better than revenue.** `→G07` (less manual work) carries 48
  abilities and `→G11` (stop being wrong publicly) carries 32 — nearly 40% between them. Commercial goals
  carry 6–14 each. Know that before a board conversation; it is a property of the subject, not a gap.
- **`Who cares` is retired as a facet.** Roles live on the questions as **Who to invite**, not on abilities.
  A role list exists to answer one thing — *whose diary to book* — and that belongs next to the question, not
  in a lookup table.
- **The role list is derived from the questions, ranked by need:** whoever owns product information (26) ·
  whoever enriches products (21) · whoever owns a channel (16) · whoever owns the integrations (13) · a
  merchandiser (11) · whoever makes the catalogues and photographs (7) · whoever deals with suppliers (5) ·
  whoever holds the budget (5) · somebody from outside the product team (4) · whoever answers to the
  regulator (4) · whoever reports the numbers (3) · contact centre (2) · a supplier (1) · a shop colleague (1).
- **Name roles by what they do, never by the tool they hold.** *PIM manager* breaks the same language rule
  the abilities follow.
- **Five questions need only one person**: `ASK-09`, `ASK-11`, `ASK-23`, `ASK-37`, `ASK-41`. Useful when a
  full session cannot be arranged.

## Open, deliberately

Six facets, five written — including `Reveals`, business type and `Ask them` (54 questions).
**Only salience remains, deferred by design**: it is the weakest-evidenced facet, and authoring it from one
client would bake in that client's shape. It is learned by being in rooms, so harvest it from use — the
instrument for getting into rooms is finished.

One ⚠ provisional line needs a second source or retirement: `DELIVER-17`. (`MODEL-19` cleared by
measurement at `[S]`.)
`MODEL-20` was asked actively rather than waited for, and it held — confirmed at a second client by a
completely different route, and its `~hosts` tag removed as a consequence. **`~hosts` now owns no ability
outright**; decide it against the next marketplace or platform client, or fold it into `~sources`.

The Tana supertag / paste-back question remains deferred on purpose. Stable IDs make it mechanical whenever
it happens, and no analysis work depends on it. Do not start it unprompted.

## Related

`px-data-audit` is the evidence-side instrument. This skill reads **testimony** — what an organisation
says it can do; that one reads **the data itself**. Load it when client export files are in play, when a
finding needs corroborating against what the data actually holds, or when a `⚠` line is silent in rooms
for a reason.

**A data extract is a fifth artefact type, and the first non-testimonial one.** Every artefact tested so
far — workshop, requirements register, pain points, To-Be workshop — records what somebody *said*. That
matters most for lines whose absence from testimony is unsurprising: nobody says "we are running out of
article numbers", so `MODEL-19`'s four silences were weak evidence for retirement — and when its checks
(`UNIQUE-05`, `STRUCT-10`) were run on `[S]`'s export, the line held. The same reasoning
covers the `ASSETS` diagnostic, which the model already says fires on evidence rather than on complaints.

`px-data-model` designs the model itself — what a product is, how it varies, what describes it, and how
that is expressed in a given platform. It is where this model's `MODEL` and `CONTEXT` domains stop being
questions and become decisions, and its decision register cites ability IDs throughout. Load it when the
conversation turns from *what must be true* to *how it is structured*.

`vaimo-pim-discovery-report` turns any of their output into the signed document.
