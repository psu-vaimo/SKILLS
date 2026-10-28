# 📌 Where we continue

*Working notes for the ability model. The register is `ability-register.md`, the questions are
`workshop-questions.md`, the reasoning is `background.md`.*

**State:** 15 domains · 205 abilities · 0 gaps · 54 workshop questions · 6 facets, 5 written. Tested against
two clients and **five artefacts**: `[Y]`'s 1,300-item requirements register, and from `[S]` a six-hour
discovery workshop, 33 recorded pain points, a two-part To-Be workshop (~6h10m combined), and now **a
full legacy-PIM export** — the first non-testimonial artefact (see below).

**Salience is the one unwritten facet, and it stays deferred by design.** It has to be learned in rooms, and
the instrument for getting into rooms is finished. Run the questions with two or three more clients and it
harvests itself.

---

## The `[S]` export — the fifth artefact, first non-testimonial (2026-10-05)

**What it is.** The complete export of `[S]`'s outgoing PIM, flattened and audited with `px-data-audit`:
3.4 million articles, 22,000 variant groupings, 520,000 image and 118,000 document records, and the old
system's own attribute definitions, class lists and value lists. It is **archaeology** in the audit
skill's sense — the system is being replaced — so its numbers size the migration, not `[S]`'s practice.
The engagement's audit handover holds the detail; what matters for the model is below.

**Mapped to the board 2026-10-05: 109 of 205, 53%** (held 65 · partial 38 · missing 6 · silent 96 — 105
at first mapping, four more once the audit's remaining checks ran; on 2026-10-06 the client's answers moved
`MODEL-19` to held and `DELIVER-09`/`DELIVER-16` to partial),
between the workshop's 88% and the pain points' 44%. **The shape is the finding: the data is loud where
testimony is quiet and quiet where it is loud** — `ASSETS` 80%, `ENRICH` 79%, `STATUS` 78%, `MODEL` 75%,
against `ORGANISE` 15%, `SOURCE` 19%, `MEASURE` 11%. The two artefact types are halves, not alternatives.
Reasoning in the background file; the per-ability table lives with the engagement's audit.

**`MODEL-19` — measured 2026-10-05, and it holds.** The trade-database article number that `[S]`'s ERP key
wraps is **7 digits and 93% consumed**: 3,380,556 values from 1,264,291 to 9,301,267, assigned in rising
sequence, the top growing ~276,000 a year. **9,999,999 is passed around 2029** — a lower bound, since the
database numbers for all its customers. The ERP pads it to 9 digits, so the ERP key itself has 99% headroom,
and nothing is reused (`UNIQUE-05` passes). So it is a **width rollover**, not a shortage: dated,
measurable, and exactly the kind of thing nobody raises because it has not happened yet. **First evidence
from any source but `[Y]`, from the artefact type predicted to find it.** **Decided 2026-10-05: ⚠ lifted,
`[S]` added.** Which `[S]` systems are 7-digit-bound is still worth asking — it decides the consequence, not
the line.

**`ASSETS` — the diagnostic's evidence, in the data.** 520,000 images with 24–39 metadata fields each
(categories, colour space, alt text), 99.98% resolvable to a file. Nobody at `[S]` complained about
assets, and the export shows a large asset estate, kept clean enough that nearly every record resolves. Same reading as the pain
points: **it fires on evidence, not complaints.** And for `ASSETS-05` ◐: the image records **do** carry
copyright and usage-terms fields, but they are filled on 0.3% (1,680) and 0.01% (70) of 520,000. A sourcing organisation
built the slots and left them empty — a fourth silence on rights, now in data rather than testimony. Still
needs a manufacturer.

**The part-owner audience is in the data model itself.** Article-type values name the part-owner web
assortment (`…delägare…`, about 8,500 articles), there is a partner-specific article record type (3,300),
and a partner register with chain order. Same client, so it adds no organisation — but it is a different
artefact *type* saying the same thing as the three testimonial ones. Still wait for a second cooperative
or franchise before proposing a value.

**Candidate: *know which of our recipients actually has each product* — corroborated by absence.**
Channel and programme membership is held as per-article flags (several customer programmes and a central
catalogue), and partner-specific article records cover 3,300 of 3.4 million articles. There is **no
relationship saying which part-owner carries which article** — the data version of the workshop's "vet vi
inte". Fourth `[S]` source; still one organisation.

**Candidate: *tell a customer that something we already sold has changed in a way the law cares about*
— the trigger exists, the recipient does not.** 43,700 safety data sheet records carry a last update (96%),
a publish date (90%) and a version (71%), so a change is detectable. Nothing in the export links a sheet
to who bought the article — and nothing in it is transactional, so the link would have to come from the ERP.
That is precisely the gap the candidate describes, and it reinforces that this is the stronger of the two.

**Two abilities with fresh evidence.** `STATUS-02` (*track several kinds of status at the same time*): the
article-type field carries type, assortment, lifecycle and an enrichment rule in one value, which became
the audit's new `STRUCT-11` check. `STATUS-07` (*know where a product is in its life*): the status field is
the same value on 99% of articles, and the lifecycle actually lives in an expiry date and a web flag that
disagree on 268,000 articles. Both are `[S]` evidence lines, not new abilities.

**What the extract changed in the instruments** (applied 2026-10-05): `px-data-audit` gained a
transformation register, guidance on multi-part exports, derived and supplier-number keys, file-store
listings for `REF-01`, in-export schemas, a sensitive-content rule, the `STRUCT-11` check (75 checks now)
and profiler fixes. `px-data-model` gained notes on PIM-only identifiers (`LIFECYCLE-04`), hidden
assortments (`THING-05`) and mapping free features onto a standard (`DESCRIBE-04`).

---

## Open after draft 21

**⚠ down to one.** `DELIVER-17`. (`MODEL-19` cleared 2026-10-05 by measurement — see the `[S]` export section.)

`MODEL-19` has now gone unraised, or raised only indirectly, by several clients in a row — at some point
that is itself the answer, and retirement should be on the table rather than an indefinite wait. **The `[S]`
To-Be workshop is a fourth silence on it** — plenty of GLN/EAN/GTIN hierarchy discussion, never a running-out
concern. Same client as the other silences, so it doesn't add a new organisation, but the streak is now four
artefacts long.

**Measured 2026-10-05 — see the `[S]` export section above: the line holds, retirement is off the table.**
The paragraph below is kept as the reasoning that led to measuring rather than retiring.

**But hold the retirement until it has been measured.** All four silences are testimonial artefacts, and
running out of identifier space is not something an organisation says — it is something it discovers.
The data shows it directly: identifier format, the space that format allows, how much is consumed, and
whether retired codes get reused. `px-data-audit` makes that a two-check job (`UNIQUE-05`, `STRUCT-10`)
on extracts we are getting anyway. **A silence from an artefact type that could never have raised the
line is weak evidence** — retiring on it would be retiring for the wrong reason. Run the checks at the
next audit, then decide.

`DELIVER-17` is **held back against a proposal to confirm it**, which is worth knowing. `[S]`'s pain-point
analysis read PP13 as confirmation; the workshop analysis of the same client had already reasoned through
that row and rejected it — six ERPs built differently is `COLLECT-06`, and no self-service trigger is
`DELIVER-18`, neither of which is *add a destination without changing the master*. The same row is cited for
four abilities, which is a sign of stretching. **Overturn this if you disagree — it is a judgement call, not
a finding.**

**`MODEL-20` needs a client whose goods are individuated.** It was asked actively at `[S]` and that was the
wrong shape — a buying cooperative handles articles, not physical units. The confirmation from the workshop
stands; the active question moves on. **The To-Be workshop adds a sharper `[S]` example, not a new client**:
a broom with shaft and brush head as separate GTIN levels inside one sellable unit — worth keeping as the
illustrative case if the line's wording is ever revisited, but it doesn't change which client is needed next.

**`~hosts` is the live structural question.** It owns nothing outright since `MODEL-20` was untagged, and
shares all 17 of its abilities with `~sources`. The register's case for keeping it rests entirely on
`SOURCE-09` reading differently where there is no purchase order. That is still plausible and still
untested. **Decide it against the next marketplace or platform client, or fold it into `~sources`.**

**The part-owner audience gap keeps confirming, still on one client.** The To-Be workshop returns to it
repeatedly — central vs. regional agreements, delägare who can decline a central deal, an interest
organisation (byggmästarnas) that isn't wired into the PIM at all. Every mention reinforces the same reading
already on file: not `~direct`, not `~indirect`. Still `[S]` only; still wait for a second cooperative or
franchise before proposing a value.

**Two salience findings waiting on a second source.** `CONTENT-09`/`CONTENT-10` biting at retailers on the
selection layer rather than the authoring layer; and `+workflow` deciding on parties-crossed rather than
headcount. Both recorded in the background, neither adopted. **The To-Be workshop reinforces `+workflow`
again, still at `[S]`**: nearly every governance thread — new-supplier onboarding, central/local enrichment
sign-off, category-tree changes — comes back to how many independent delägare a process crosses, not to the
two-person central team's headcount. Third time this reads the same way at one client; still needs a
different organisation to move from recorded to adopted.

**One new candidate ability, provisional — not yet added to the register.** *Give suppliers back something
about how their own products are performing.* The To-Be workshop raises this twice, unprompted, as a lever
for getting better supplier data: sales or performance statistics handed back to a supplier as an incentive,
the reverse direction of everything in `MEASURE` (which is the organisation learning about its own
catalogue). Not `SOURCE-09` (that's leverage as a market position); this is a concrete exchange mechanism.
One source, one mention pair — too thin to add. Worth testing for whether it recurs before drafting a line.

**Two candidate abilities, both held back — now with a third `[S]` artefact behind each, still one client.**

*Know which of our recipients actually has each product.* Surfaced independently by all three `[S]`
artefacts now — the To-Be workshop again: only a loosely-worded contract naming product groups, no live link
to which delägare actually carries which article, repeated "vet vi inte" when asked. Three sources, one
organisation. Test against a single-entity retailer — a federated cooperative may be the only shape where
the master cannot see its own consumers.

*Tell a customer that something we already sold has changed in a way the law cares about.* Safety data sheet
updates reaching named B2B buyers inside a statutory window. `DELIVER-12` is pull, `DELIVER-04` is produce
and retain — **neither is notify after the sale**. Now three `[S]` sources — recalls, safety data sheet
renewals, and the To-Be workshop's explicit ask for a notification when a supplier updates something after
the sale. Still the stronger of the two, and the mechanism is now more concrete: a flag that fires when
post-sale supplier information changes, distinct from either pull ability already on the register.

**`ASSETS-05` ◐ needs a manufacturer.** Two sourcing retailers have now been silent on image rights, and the
To-Be workshop is a third silence at `[S]` itself — extensive asset-architecture discussion, never rights or
permission to use. Confirms the point rather than adding to it: stop asking `[S]`, the next test has to be a
manufacturer or brand.

**A fifth artefact is now in reach, and it is the first non-testimonial one.** Client export files —
`px-data-audit`, built 2026-09-09, is the instrument. Every artefact type tested so far records what
somebody *said*: a register states what an organisation wants, a workshop what it can describe, a
pain-point list what has become intolerable. An extract states what *is*, and it cannot rehearse an
answer or decline to mention something.

**The expected yield is on lines whose silence is unsurprising** — `MODEL-19` above, and the `ASSETS`
diagnostic the register already says fires on evidence rather than complaints. Two live engagements are
in scope for the first test: `[S]`, whose 7.5 verdict is still pending its extracts, and a second where
an audit shipped ahead of the method. **Harvest the coverage percentage from the first one properly** —
it will not be comparable to the workshop and register numbers, and that difference is the finding, the
same way the pain-point list's 44% was.

**Artefact type is now two, and the second one taught something.** A pain-point register is genuinely
different from discovery notes: it records only what has become intolerable, so it covers less (44% against
88%) and its silences mean something specific. **The rule it produced: absence in a narrower artefact does
not refute presence in a broader one.** The To-Be workshop is a fourth artefact but not a third *type* — it's
discovery-shaped like the first `[S]` session, just aimed at future state — so it doesn't add a new row to
this rule, only more weight to the two shapes already known. A vendor RFP response, a data-governance policy
and an ISO-style process document all remain untried.

**The third deletion line** — archive versus destroy, and how long something stays recoverable — is still a
decision rather than research. Three candidate wordings are in the background file.

**Tana supertag / paste-back:** still deferred on purpose. Stable IDs keep it mechanical whenever it happens.
