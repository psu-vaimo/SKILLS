# Section register — Discovery Report Template v3.0

Every section of the report. **Kind** is `standing` (same every client, from `boilerplate.md`) or
`discovered` (only exists because of a workshop, an audit or a test). **Done when** is the test used
to grade the section Draft vs Ready.

Placeholders: `<company name>`, `<vendor>`, `<platform>`, `<author>`, `<date>`, `<name of PM>`. Keep
the angle brackets for anything unanswered. **No worked example figures anywhere in this file** —
they get left in client documents.

---

## Front matter

`<company name>` · **PIM Discovery Report** · Version `0.1` · `<date>`
Report by `<author>`, Vaimo `<department>`, `<title of author>`, `<email to author>`.

Name the chosen platform on the cover, not only in the executive summary.
Versioning: `0.x` while drafting, `1.0` on client approval.

---

# Part A — About this document

## 1. Document Control — `standing`

Control tables only. No prose.

### 1.1 Version history
| Version | Date | Comments | Revised by |
|---|---|---|---|

### 1.2 Approval log
| Version | Date | Comments | Approved by |
|---|---|---|---|

### 1.3 Distribution
Who receives this document and in what form.

**Done when:** the version history reflects the versions that actually went to the client.

---

## 2. Executive Summary — `discovered`

**Purpose:** the only page the sponsor is guaranteed to read.

**Inputs:** 7.5 readiness verdict, 11.6 PoC results, 13.1 MVP, 14.5 readiness by area, 8.5 goals.

**Form:** one page. What the Discovery covered and concluded · the chosen platform and why · the
client's main goals in their own words · headline findings (data readiness, feasibility as proven by
the Happy Flow, the MVP recommendation) · what this commits the client to next and what it does not.

**Done when:** it leads on findings rather than aims; the platform is named; the goals match 8.5; the
conclusion matches 14.5; and someone who read only this page would not be surprised by section 11.6.

**Write this last.** Summarising an unfinished report produces the generic version.

---

## 3. Purpose, Scope and Basis — mostly `standing`

- **3.1 Purpose and status** — `standing`. What the document is for, and that it becomes the source of
  truth once signed.
- **3.2 Background** — `standing`. Why the organisation is doing this now.
- **3.3 In scope of the Discovery** — `standing` frame, per-engagement detail. Quote the signed SOW.
- **3.4 Out of scope of the Discovery** — `standing`, extend per engagement. Full data migration,
  production deployment, performance testing, licensing, infrastructure, training beyond workshops,
  ongoing support. These belong to a separate implementation agreement.
- **3.5 Client responsibilities** — `standing`. Change management, data quality, data cleansing and
  migration remain the client's.
- **3.6 Assumptions and collaboration principles** — `standing`, and **not optional**. Timely access to
  systems and stakeholders, agreed data extracts made available, active participation in workshops,
  feedback and approvals within agreed timeframes. Written as conditions on the conclusions, not as
  pleasantries.
- **3.7 Basis of this report** — `discovered`. Workshops held with dates and attendees, documents
  received, data extracts analysed.

**Done when:** 3.4 has any engagement-specific exclusion found in the workshops; 3.6 is present and
phrased as conditions; and 3.7 lists everything cited anywhere else in the report.

---

# Part B — How the Discovery ran

## 4. Project Set-up and Governance — `discovered`

People and decision rights in one section.

- **4.1 Vaimo team** — Project Manager · Business Consultant · Lead Developer. Role / Name / Description.
- **4.2 `<company name>` team** — Sponsor · Project Manager · Product Owner · SMEs.
- **4.3 `<vendor>` team** — Customer Success Manager · Functional Support · Technical Support.
- **4.4 Roles and responsibilities (RACI)** — responsible / accountable / consulted / informed, per
  Discovery stage.
- **4.5 Steering committee and cadence** — Company / Name / Email, plus meeting interval.
- **4.6 Communication channels** — the tools this client will actually use.
- **4.7 Decisions and change requests** — how a decision is recorded, who approves a change, where
  change requests live.

**Done when:** every role has a real name or is explicitly marked unfilled; the Sponsor in 4.2 appears
in 4.5; and any unfilled role also appears as a risk in 14.2. An empty Sponsor row is a project risk,
not a formatting gap.

---

## 5. Discovery Timeline — `discovered`

**Purpose:** what happened, when, and what each milestone released. **Not a restatement of the
statement of work** — scope, activities and deliverables are defined in the signed SOW and this
section references it. Two documents describing the same scope in different words will drift, and the
signed one has to win.

- **5.1 Timeline at a glance** — Stage / Period / Key sessions / Milestone. Gantt or table, one page.
- **5.2 Stage 1 — Initiation.** Kick-off, governance and communication agreed, stakeholders and
  decision-makers named, goals and KPIs agreed. *Milestone: project initiation and plan approved.*
- **5.3 Stage 2 — Current state and data.** As-Is workshops and the legacy data audit, run in
  parallel; the audit does not wait for the workshops. *Milestone: current state documented and data
  readiness assessed.*
- **5.4 Stage 3 — Target state and prioritisation.** To-Be workshops, then MVP and phasing.
  *Milestone: target state and phasing validated.*
- **5.5 Stage 4 — Happy Flow.** Environments, mapping, connectors, end-to-end test. *Milestone: Happy
  Flow approved.*
- **5.6 Stage 5 — Report and hand-over.** Consolidation, drafting, client review, approval.
  *Milestone: Discovery Report approved.*
- **5.7 Milestones and acceptance** — Milestone / Planned / Actual / Confirmed by / Date confirmed.
  State the review window and what happens if no response arrives inside it.
- **5.8 Deviations from plan** — what moved, by how long, and what caused it. Plainly and without
  blame; the causes are usually availability and access, and those are the same causes that will
  affect the implementation.
- **5.9 Indicative implementation phases** — Build · Prepare · Launch, context only, marked **not
  contracted by this document**.

> **Environments belong at the start of the Discovery, not at stage 4.** Everything in stage 4 depends
> on them, they take real elapsed time to provision, and a holiday period or a licensing delay between
> initiation and the PoC stops the Discovery. This is the most common reason a Discovery finishes late
> — say it in 5.5 and again in 13.5.

**Done when:** every stage has a real date range; 5.7 has actual dates, not only planned ones; 5.8 is
present even if the answer is "nothing slipped"; and 5.7 agrees with 15.1.

---

# Part C — Findings: current state

## 6. Current State (As-Is) — `discovered` ★

Current product information landscape, workflows and system interactions.
**Framed on four verbs throughout: Create · Enrich · Edit · Delete.**

- **6.1 Organisation and commercial context** — the survey answers summarised, plus a Vaimo commentary
  that says what the numbers do not: which answers are surprising, inconsistent, or contradicted by a
  different stakeholder. Full question set in Appendix D.
- **6.2 Existing systems** — System / Role in the product process / Owner / Comments.
- **6.3 System map and product information flow (As-Is)** — diagram plus description.
- **6.4 Product information workflows (As-Is)** — one per workflow, each covering all four verbs.
- **6.5 Roles and ownership today** — who does what, and which attributes each role owns.
- **6.6 Level of automation (As-Is)** — Manual / Automated / Total steps, counted from 6.4.
- **6.7 Pain points ★** — Pain point / Impact / Where it occurs / Suggested direction. Each carries an
  ID. **The spine of the report.**
- **6.8 What works well today** — what not to break.

**Done when:** every system named anywhere in the report is in 6.2; every workflow covers Delete or
says why not; every pain point has an ID and traces to 12.1; 6.5 names actual people or roles; and 6.8
is not empty. An empty 6.8 means nobody asked. A thin 6.7 means a thin Discovery.

---

## 7. Data Audit and Data Readiness — `discovered` ★

An assessment of the data as it actually exists — not a disclaimer about whose problem it is. 3.5 says
data quality is the client's responsibility; this section says what that responsibility currently
amounts to, in evidence.

- **7.1 Data sources reviewed** — which extracts, from which systems, at what date and volume. The
  audit's conclusions are only as good as the extracts, so bound them here.
- **7.2 Data structure assessment** — how the data is organised today, structural patterns, degree of
  completeness.
- **7.3 Data quality observations** — by area, **with examples rather than adjectives**.
- **7.4 Risks and improvement recommendations** — what breaks on onboarding if untouched.
- **7.5 Data readiness verdict** — a plain judgement per area with the reasoning.
- **7.6 Open questions and trade-offs** — the choices only the client can make, each with its options,
  what each costs and the area it unblocks. Part of the report; answered after it (`data-audit`).

**Done when:** 7.1 bounds the analysis; 7.3 cites real examples; 7.5 gives a verdict per area; and the
verdict reaches 9's readiness column, 13.3 dependencies, 14.2 risks, 14.4 estimate and section 2.

This is the number that changes the implementation estimate. A verdict of "requires work" is the
client's work, and this is where that stops being a disclaimer and becomes concrete.

---

# Part D — Findings: target state

## 8. Target State (To-Be) — `discovered` ★

Same four verbs as section 6.

- **8.1 System map and product information flow (To-Be)** — diagram plus description.
- **8.2 Product information workflows (To-Be)** — one per workflow, all four verbs, each stating how
  the platform meets it.
- **8.3 Roles and ownership in the future process** — what changes for whom. Feeds 3.5.
- **8.4 Level of automation (To-Be)** — same denominator as 6.6, or say why the process changed.
- **8.5 Goals and KPIs** — Goal / Owner / KPI / As-Is baseline / Target. **One table, not two:** a goal
  and the number that proves it belong on the same row.
- **8.6 Insights and recommendations from comparable engagements** — marked as opinion, not finding.

**Done when:** every As-Is workflow in 6.4 has a counterpart or is explicitly retired; every KPI has a
baseline; every goal is attributable to a named stakeholder rather than to "the business"; and 8.4
shares a denominator with 6.6.

---

## 9. High Level Data Model — `discovered`

Overview only; detail goes to a separately approved data modelling file. Diagram if available.

| Area | Description | Basic assumption | Data readiness | Comment | Priority |
|---|---|---|---|---|---|

Areas: Channels · Category trees · Locales · Families · Currencies · Attribute groups · Attributes ·
Single products · Variant products · Bundle products · Assets · Asset families · Measurements ·
Associations · Rules · Reference entities · AI configurations · Workflows.

**9.2 Open model decisions** follow the table: question, options and trade-off, and the draft model's
proposal where one exists. Answered after the report, in the decision log and the data modelling file.

"Basic assumption" is an order-of-magnitude estimate; ranges are fine and honest. The readiness column
takes its judgement from 7.5 rather than carrying an independent guess.

**Done when:** every row has an assumption and a readiness value, or is explicitly "To be defined".

---

## 10. Integrations and Customisations — `standing` framing, `discovered` content

Both answer the same question: what has to be built that the platform does not already do.

- **10.1 Integration points** — direction, trigger (event / scheduled / manual), systems at both ends,
  phase.
- **10.2 Customisations** — what the platform does not do out of the box, whether it is built inside
  the platform or outside it, and which requirement it serves.
- **10.3 Deferred beyond the first phase** — named as deferred, not omitted.

**Done when:** everything crossing the PIM boundary in 8.1 appears in 10.1; every customisation traces
to a requirement in 12.1; and 10.3 is not empty by accident. An empty 10.3 usually means the
conversation did not happen.

---

# Part E — Validation

## 11. Happy Flow — Data Flow Proof of Concept — `discovered` ★★

**The section that changes what this report is.** Everything else is analysis and agreement; this is
where a real product was pushed through the real intended systems and either worked or did not.

The claim it makes and must support: **at least one real product travels the whole defined flow —
created, enriched, edited and deleted — through configured integrations, and here is the evidence.**

- **11.1 Scope of the PoC** — which product and why it is representative · which systems the flow
  crosses, in order · which verbs are in the test and which were excluded, with reasons · what the PoC
  deliberately does **not** attempt (volume, performance, production data, edge cases).
- **11.2 Structure and value mapping** — field-level mapping (source field, target field,
  transformation, rule owner) · value mapping and controlled vocabularies · business rules the client
  validated, and the ones that turned out to be assumptions · mapping gaps, both directions.
- **11.3 Inbound connector** — what was built, against which interface, how it is triggered ·
  configuration and where it lives · what is production-grade and what is scaffolding.
- **11.4 Outbound connector** — same structure as 11.3 · which consuming systems were included, and
  which were stubbed or skipped.
- **11.5 End-to-end test** — test cases, one per verb, expected vs actual · the product's state at each
  hop, **evidenced** (screenshots or exports, not assertions) · defects and workarounds.
- **11.6 Results and observations** — what the flow proved · **what it did not prove** · surprises and
  what they imply for 14.4.
- **11.7 Scaling considerations** — what has to change between this flow and a production one: volume,
  error handling, monitoring, retries, security. Which of those become requirements in 12 and which
  become implementation work.
- **11.8 Environments and access** — which environments were established, on whose licences, what
  happens to them afterwards. Cross-reference 15.2.

**Done when:** the chosen product is justified; all four verbs are tested or excluded with a reason;
11.5 carries real evidence; **11.6 states what the PoC did not prove**; and 11.7's findings appear in
12 or 13.

> **11.6's honest paragraph is mandatory and is the one most likely to be dropped.** A PoC that
> validated one product says nothing about ten thousand. A report that omits this is selling the
> implementation rather than reporting the Discovery.

---

# Part F — Conclusions and what happens next

## 12. Requirements — `discovered` ★

**The one canonical home for requirements.** Written here once, referenced from everywhere else. A
requirement restated in a second place will eventually contradict itself.

### 12.1 Requirements register
| ID | Name | Priority | Can be met by the platform | Pain point addressed | Source |
|---|---|---|---|---|---|

IDs are `BR01` onward and are **never renumbered once the document has been shared** — they get quoted
in change requests, budgets and the Implementation Specification.

### 12.2 Requirement descriptions
One block per requirement: Name / Priority / Description / Resources needed / Dependencies / Suggested
acceptance test.

**Done when:** every pain point in 6.7 is covered; every requirement has a source; every "cannot be
met" answer is routed to 3.4, to 13.2 or to a change request; and every block has an acceptance test a
client could actually run.

The acceptance test is the most-skipped and most-valuable field. A requirement nobody can verify is a
requirement nobody can sign off.

Requirements state what must be true, never how to configure it. The moment one names an attribute
type, a connector or a screen, it has crossed into the Implementation Specification.

---

## 13. Prioritisation, MVP and Phasing — `discovered` ★

Priorities on a list are not a plan. This turns them into a first release with a boundary.

- **13.1 MVP scope** — what the first release contains and, explicitly, what it does not.
- **13.2 Subsequent phases** — what is deferred, in what order, what each phase unlocks.
- **13.3 Dependencies and sequencing** — including anything from 7 that must be fixed before
  onboarding.
- **13.4 Indicative roadmap and timeline** — gantt or similar, marked indicative.
- **13.5 Preconditions for the timeline to hold** — resource availability on named dates, decision and
  signing deadlines, milestone acceptance without delay, any external deadline such as an end-of-life
  date on the system being replaced. **State these as conditions, so a slipped timeline has a
  documented cause.**
- **13.6 Documented assumptions and risks behind the phasing.**

**Done when:** 13.1 has an explicit exclusion list; 13.3 reflects 7.5; and 13.5 names dates and owners
rather than describing good intentions.

---

## 14. Project Outlook — `discovered`

- **14.1 Success factors** — measurable statements referencing 8.5.
- **14.2 Risks** — this client's risks. Anything unfilled in section 4, and any "requires work" in 7.5,
  appears here.
- **14.3 Steering parameters** — which aspect wins in a conflict: on-time delivery vs full scope · keep
  the scope vs allow new ideas · budget vs functionality · out of the box vs customisations.
- **14.4 Revised estimate** — how the Discovery changed the original view of cost and duration, and
  what drove the change.
- **14.5 Readiness by area** — Area / Status / Risk, covering timeline, budget, scope, data quality and
  each of the three teams, plus Overall.
- **14.6 Open questions and recommendations** — what is still unknown, who owns finding out, by when.

**Done when:** 14.2 is specific to this client; 14.4 states a direction and a cause; 14.5 has a status
and a risk on every row with Overall no greener than its worst row; and 14.6 is not empty.

An out-of-the-box preference in 14.3 next to a long 10.2 is a contradiction to raise before sign-off,
not after. A Discovery that produced no open questions was not a Discovery. 14.5 is the honest health
read, it is the section most often softened, and softening it is what makes a later meeting go badly.

---

## 15. Approval and Rights — `standing`

- **15.1 Acceptance process** — how deliverables are confirmed, the review window, what happens if no
  response arrives inside it. Consistent with 5.7.
- **15.2 Rights to deliverables and platform licensing** — the client's rights to the documentation
  produced, and the separate position of licensed platforms: configurations and mappings made during
  the Discovery are the client's to use, but only while the underlying licences are active, and the
  platforms themselves are not transferable. Cross-referenced from 11.8.
- **15.3 Signatures.**

**Done when:** 15.1 names the mechanism actually used for this client and matches 5.7.

---

# Appendices

- **A — Glossary.** Every abbreviation used anywhere in the report, including client- and
  platform-specific ones. Standard set in `boilerplate.md`.
- **B — PIM concepts.** The orientation diagram for readers who have never seen a PIM. An image, not
  paragraphs.
- **C — Platform data model definitions.** Akeneo, inriver or other — **keep only the chosen
  platform**. Leaving two in signals the platform decision was not really made.
- **D — Discovery survey.** Full question set and answers; summarised in 6.1. Question list in
  `boilerplate.md`.
- **E — Happy Flow evidence.** Test case detail, mapping tables and screenshots supporting section 11.

---

## Cross-reference map — check these when reviewing

| This | must agree with |
|---|---|
| 2 Executive Summary | 7.5, 11.6, 13.1, 14.5 |
| 2 goals | 8.5 |
| 3.3 in scope | the signed SOW, and the stages in 5 |
| 3.7 basis | everything cited anywhere |
| 4.2 Sponsor | 4.5 |
| 4 unfilled roles | 14.2 |
| 5.7 acceptance | 15.1 |
| 6.2 systems | 6.3, 6.4, 8.1, 10.1 |
| 6.4 workflows | 8.2 |
| 6.6 / 8.4 automation | the automation KPI in 8.5, sharing a denominator |
| 6.7 pain points | 12.1 |
| 7.5 readiness | 9 readiness column, 13.3, 14.2, 14.4, 2 |
| 8.1 PIM boundary crossings | 10.1 |
| 10.2 customisations | 12.1 |
| 11.7 scaling | 12, 13.2 |
| 11.8 environments | 15.2 |
| 12.1 "cannot be met" | 3.4, 13.2, or a change request |
| 13.5 preconditions | 14.2 |
| 14.3 out-of-the-box preference | the length of 10.2 |
| Appendix C | the platform named in 2 |
