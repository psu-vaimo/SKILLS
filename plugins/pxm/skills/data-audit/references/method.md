# The method

Five stages, in order, because each one bounds the next. The deliverable templates are at the end.

---

## Stage 1 — Bound it

Nothing can be measured until the scope is fixed, and the scope is the client's decision, not the
auditor's.

### What to ask for

Ask for the **widest** export, not the tidy one. People send the view they are proud of; the audit needs
the one nobody looks at. If a system can export all attributes for all statuses, that is the ask.

**The two files to get first, before anything else, are the main source system — usually an ERP — and
the main destination, usually the webshop.** Those two alone support the `FLOW` dimension, which is the
highest-yield thing in the register. Everything below is what makes the rest of the audit possible.

| Ask | Why |
|---|---|
| Full product export from the **main source system**, usually the ERP — every attribute, every lifecycle status, including the status field | The structurally reliable end of the flow. Without the status column nothing can be segmented, and rule 1 fails at the first step |
| Full export from the **main destination**, usually the webshop — everything it publishes, as it publishes it | The only place you see what the customer is actually shown. Half of `FLOW` |
| The migration scope definition, or the list of records in it | The denominator. If it does not exist yet, that is finding one |
| An export from each **other** integration point and destination | `CROSS`. Add these after the two ends, not instead of them |
| An export from a **PIM only if it is current and staying** | If it is stale or being replaced it is archaeology — profile it to size the migration out of it, and label the numbers that way. See the SKILL note on which systems to audit |
| The attribute or schema definition — attributes, types, allowed values, required flags | Turns `VALID-01`, `VALID-03` and `COMPLETE-06` from impossible into cheap |
| Category tree(s) as their own export, with node identifiers | `CLASS` and `REF-03` |
| The asset register — identifier, filename, product link — **and a listing of the file store**: path and size per file, no files needed | `REF-01`. An asset identifier without a resolution path is not an asset. The listing is cheap to produce and enough to resolve every record, find files with no record and records with no file, and size the asset migration |
| Relationship and association exports — variants, accessories, spares, bundles | `REF-02`, `REF-04`, `STRUCT-08` |
| The locale and market matrix — which markets get which languages | `COMPLETE-05` |
| Any validation or completeness rules currently enforced | Tells you what they already believe about their data |
| The published specifications of the channels they deliver to | `COMPLETE-09`, and the only thresholds a client cannot argue with |
| The extract date of every file | `TIME-01`, and it goes in the source register |

**Ask for everything to be extracted on the same day.** Sources pulled weeks apart cannot be compared,
and `TIME-03` will fire on an artefact of your own request rather than on the client's data.

### What to fix before measuring

State the scope, the extract dates, and what is *not* in the set. An audit that does not say what it
could not see is selling the next phase rather than reporting this one.

---

## Stage 2 — Inventory

What is in the set, and how the pieces relate. This is the stage that produces the picture people
actually remember.

Per source, establish: what system it comes from, what role it plays in the landscape, its volume, its
extract date, and **its one-line verdict** — *"the ERP master, authoritative for logistics, packaging and
classification"*. A source without a stated role will be argued about for the rest of the engagement.

Then, across sources:

- **The common key**, and what it is called in each file. Rarely the same word twice.
- **Record overlap** — which source holds which products, as a matrix, with subset and superset
  relationships named. "A strict subset of the PIM, which holds 668 more" is a finding.
- **Field overlap** — how much vocabulary is shared. Read it both ways: low overlap means every source is
  load-bearing, high overlap means something must decide which wins.
- **The flow** — a small diagram beats three paragraphs. ERP → PIM → destinations.
- **What is not here.** Name the categories of information absent from the whole set. One inventory's
  most useful line was that no file contained stock, orders or any other transactional data — which
  settled a scope argument before it started.
- **What happened to the files before you profiled them.** Exports rarely arrive profile-ready: nested
  JSON gets flattened, typed values collapsed, placeholders removed, columns dropped as duplicates. Keep a
  **transformation register** beside the source register — every step, what it changed, and what it does
  to measurement ("empty and absent are now the same", "timestamps are local dates"). **Verify a
  duplicate before dropping it**: "same name" and "looks the same" are not evidence — compare the values
  on every row, and keep both when they differ on any meaningful share. A profile of a transformed file
  that does not say what was transformed is the numbers equivalent of an unsourced quote.
- **Whether the schema came with the data.** A PIM export often carries the system's own definitions as
  record types — attribute definitions with a data type, class or list objects saying which attributes
  apply, value-list objects. When it does, `VALID-01`, `VALID-03` and `COMPLETE-10` stop needing the
  client's specification. Look for them before asking, and name them in the source register as
  **schema**, not data.

---

## Stage 3 — Profile

Run `scripts/profile_export.py` over every source. Then run the checks in `references/checks.md` that
the client's situation calls for.

```bash
python3 scripts/profile_export.py exports/*.xlsx \
    --out audit-out --key ARTNR --scope STATUS=20 --segment STATUS --multi-delim ';;;'
```

**One source is one file.** Every file you pass is treated as a separate source, and with `--key` the
first two are compared as source → destination. An export split into parts must be combined first — and
parts often have different column sets, because each carries only what its slice uses. Align them to
the union while streaming, e.g. with Miller:

```bash
cols=$(for f in parts/*.csv; do head -1 "$f"; done | tr , '\n' | awk '!s[$0]++' | paste -sd, -)
mlr --csv template -f "$cols" parts/*.csv > combined.csv
```

**Placeholders that are not on the built-in list** go in with `--null-equiv` (exact, case-folded) or
`--null-pattern` (regex, for placeholders that vary per record such as `<supplier>-MISSING`; write it as
`--null-pattern='-MISSING$'` when it starts with a dash). Both are counted as empty, reported at the top
of `profile.md`, and excluded from duplicate-key detection. `--multi-delim` can be repeated when fields
use different separators. **`--segment` takes an existing column only** — derive a segment such as
"expiry date in the past" into a column first.

The script computes most of `COMPLETE`, `VALID`, `STRUCT`, `UNIQUE-01` and the `CROSS` overlap measures.
Everything else needs the specification, the channel requirements, or a referent — and knowing which is
which is what keeps the audit honest about its own reach.

**Read `profile.md` before writing anything.** The point of the tool is that a thousand-column export
cannot be read by eye, not that the numbers write the findings themselves.

---

## Stage 4 — Judge

A count is not a finding until someone says what it means. Turn each measurement into a statement with a
consequence attached.

**Examples rather than adjectives.** "Inconsistent units" is an adjective. "Length is held in three
attributes — `Langd_mm`, `Langd_cm` and `Längd` — with 14%, 3% and 61% fill; a product's length is in
whichever one its category happened to use" is a finding, and the client can act on the second.

**Group by area, not by dimension.** The reader cares about assets, or about the category tree; they do
not care which of the ten dimensions produced the observation. Dimensions are how you *find* things;
areas are how you *report* them.

**Separate what the data shows from what it implies.** The first is defensible, the second is your
professional opinion, and mixing them is how a report gets picked apart on the one line that was a guess.

---

## Stage 5 — Decide

Two action lists, because two different questions were asked, and the same evidence answers both
differently.

### Migrate the information

What must happen to move what exists. Per item: what is wrong, how many records, who fixes it, and
**when** — before extraction, during transformation, or after load. Triage every defect four ways:

| Triage | Means |
|---|---|
| **Automatic** | A rule fixes it with no human judgement — trim whitespace, normalise separators |
| **Rule with review** | A rule proposes, a person accepts. Value mapping, unit conversion |
| **Human** | Someone must decide or author. Merging two attributes into one, writing missing copy |
| **Absent at source** | Not a cleansing job. The data does not exist and must be acquired or the field dropped |

The fourth is the one that changes a plan, because no amount of migration effort creates it.

### Stand up a new system

What the new system must be configured to hold, independent of what gets migrated into it. Attribute
list, families, controlled vocabularies, locales, classification, relationship types, asset structure.

**These are different jobs and the distinction matters.** Configuration is the taxonomy and the attribute
model; migration is the records. A client can stand up a correct model and migrate nothing into it, or
migrate a million records into the wrong shape. The bruttolista serves both, which is why it is the
central artefact rather than an appendix.

### Data model input

The third deliverable, and the one clients get the most out of. **Either a drafted high-level model or a
written set of learnings for whoever drafts it** — the choice depends on whether the To-Be is settled
enough to model against.

What the audit contributes, and where each part comes from:

| Model decision | Evidence |
|---|---|
| Which attributes exist at all | Bruttolista, `verdict = migrate` or `merge` |
| Which are controlled lists rather than free text | `STRUCT-06`, `CONSIST-01`, distinct-value profiles |
| The actual value set for each list | Distinct values, after normalising case and whitespace |
| How many families are needed, and roughly which | `STRUCT-02`, plus fill-rate clustering by category |
| Variant axes | `STRUCT-08` |
| Which attributes are localisable and which scopable | `STRUCT-09`, `COMPLETE-05` |
| Whether the classification can carry weight | `CLASS-01` to `CLASS-05` |
| Relationship types actually in use | `REF-02`, `REF-04` |
| Asset structure and how assets resolve | `REF-01`, `COMPLETE-08` |

**Mark every line as evidenced or proposed.** An evidenced line says the data supports it; a proposed
line is your professional judgement about the To-Be. Both belong in the draft and they will be read as
equally solid unless the draft says otherwise.

**Do not derive the model from the profile alone.** The data is a record of the old system's decisions,
including its mistakes, and a model drawn straight from it migrates beautifully because nothing changed
shape. Bring the To-Be from the workshops — `abilities` is the instrument — and use the audit to say
which parts of it the data can actually support.

State the four constraint classes plainly: what the data **supports**, what it **contradicts**, what it
**will not fit into**, and what it **cannot say** — the last being everything about products the client
intends to sell but does not sell yet.

And carry the discipline into both lists: **no organisation wants, needs or will pay for perfect data.**
Say which defects block go-live and which are merely true.

---

# Deliverable templates

## Source register

Bounds the audit. Goes to section 7.1.

| Source | System | Role | Extract date | Records | Fields | Key | In scope |
|---|---|---|---|---|---|---|---|

## Transformation register

Every step between the export as delivered and the file profiled. Travels with the source register,
because a number cannot be traced back to a file without it.

| Step | Tool | What changed | Consequence for measurement | Verified how |
|---|---|---|---|---|

## The bruttolista — attribute gross list

**The artefact clients keep.** One row per *concept*, not per column: localised variants collapse to one
row with a language count, and value+unit column pairs collapse to one row with a unit flag. Counting
before normalising inflates the total and hides the real decision.

| Field code | Name | Category | Sources | Loc. | Unit | Fill % | Distinct | Flags | Verdict | Target | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|

- **Category** — group by origin and purpose: core/ERP, commerce content, PIM attribute, custom,
  classification feature, regulatory. The grouping is what makes 800 rows navigable.
- **Fill %** — against the in-scope denominator, stated at the top of the sheet.
- **Verdict** — `migrate` · `merge` · `derive` · `drop` · `decide`. The column that turns an inventory
  into a decision, and the reason this is not just a field list.
- **Target** — the attribute it becomes in the new model. Empty for `drop`.

Where the client publishes to a standard with a layered attribute model, borrow the layering — a core
set, a category-conditional set, then regional and local. It gives the gross list a built-in
prioritisation instead of leaving 800 flat rows for someone to sort by hand.

### The decision queue

Ambiguous merges are **surfaced, never silently resolved.** A separate table, and it is the most
valuable page in the deliverable because it is the part that needed judgement.

| Field | Possible match | Verdict needed | Recommendation |
|---|---|---|---|

Worked shape, from a real inventory: *two fields both called something like "material"; one holds
`Stål`, `Rostfritt stål A4`, the other holds `1018/1022 - CN`, `Nylon EU PA6`. One is customer-facing,
one is procurement-facing. Recommend keeping both.* That is the analysis; a tool that merged them on
name similarity would have destroyed it.

## Findings

Goes to section 7.3. By area, with examples.

| ID | Area | Finding | Evidence | Records affected | Consequence if untouched |
|---|---|---|---|---|---|

## Readiness verdict

Goes to section 7.5, and its judgements populate section 9's readiness column — so use section 9's
areas rather than inventing a list: channels · category trees · locales · families · currencies ·
attribute groups · attributes · single products · variant products · bundle products · assets · asset
families · measurements · associations · rules · reference entities · AI configurations · workflows.

| Area | Verdict | Reasoning | Blocks |
|---|---|---|---|

Verdicts: **ready** · **needs work** · **needs decisions** · **not assessed**.

*"Needs decisions"* is distinct from *"needs work"* on purpose. Work is effort someone can be booked
for; decisions are blocked until a person with authority chooses, and they are the ones that quietly
consume a timeline. **"Not assessed" is a legitimate verdict** — accuracy usually earns it — but it must
name what would be needed to assess it.

## Open questions and trade-offs

Goes to section 7.6 (questions about the data) and 9.2 (open model decisions). **Part of the report, not a
precondition for it.**

| Question | Why it matters | Options and trade-off | Affects |
|---|---|---|---|

- **One row per choice only the client can make**: scope edges, ownership, which programmes continue,
  who sources what is absent at source, whether to run the accuracy sample. Not a list of things Vaimo has
  not yet looked at.
- **Every row carries its options and what each costs**, in the reader's terms (time, effort, risk,
  what the customer sees). A question without options is a request for information; with options it is a
  decision the client can take in the room.
- **Name the area or action it unblocks**, so the answer can be traced back into 7.4, 7.5 and section 9.
- For model decisions (9.2), add **the draft's proposal** where a draft model exists, so the workshop
  tests a concrete choice rather than an open question.

Answers arrive after the report. They go into the decision log and the detailed data model file; a
re-issue of the report is a choice, not a step in the method.

---

# Standalone audit report

Where the audit is its own engagement rather than part of a discovery, this is the shape. It follows the
existing Vaimo PIM Audit Report structure, which clients have already signed.

1. **Introduction** — version and approval tables
2. **Executive summary** — the verdict and the three things that matter, for a sponsor who reads nothing else
3. **Purpose** — the question the audit was asked
4. **Audit set-up** — scope, team, responsibilities, timeline, activities, deliverables
5. **Limitations and out of scope** — what was not looked at, and what accuracy status is
6. **As-Is** — systems, system map, current metrics baseline, environment
7. **Findings by area** — the substance
8. **Summary** — verdicts by area
9. **Recommendations** — short, mid and long term, with effort and impact
10. **Approval**

Two things carry over from the existing template and are worth keeping. The **quantified metrics
baseline** — products, locales, channels, category trees, families, attributes, attributes per family,
zero-usage attributes — because it is the only part a client can compare against next year. And the
closing **presentation workshop**, because a report that is read alone is a report that is argued with
alone.

Where the audit is part of a discovery, none of this applies: findings go to section 7 and verdicts to
section 9, and `discovery-report` holds the section register and the done-when tests.

# Writing the report: from the As-Is, without waiting

**The report is written from the As-Is, when the profile is done, not when the client has answered.**
The data is the one thing in the engagement that does not change while people think, so the report states
what it shows and does not hold for decisions about the To-Be.

- **Decisions the client has already taken are facts** and go in as such (the scope, the platform, the
  locales), with who decided and when.
- **Decisions not yet taken are content**: they go in the open-questions table (7.6, 9.2) with their
  options and trade-offs. A question asked in the report gets a better answer than one asked in an email,
  because the reader sees what each answer costs.
- **Never write "pending client input" in place of a verdict.** Where an area is blocked by a choice, the
  verdict is *needs decisions*, and the choice is a row in the open-questions table.
- **Do not re-measure for the report.** Use the numbers the stages produced; where the scope changed after
  a measurement, say which scope a number is on.

Deliver in the client's language where they work in one (the detailed model and the report should match),
and as a `.docx` when the report is for sign-off (`anthropic-skills:docx`, Vaimo tokens from
`vaimo-brand-guidelines`, or the client's copy of the template where one exists).
