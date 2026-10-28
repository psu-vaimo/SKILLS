---
name: vaimo-pim-discovery-report
description: Write, review or fill in a Vaimo PIM Discovery Report — the client-signed output of a PIM discovery. Use for "let's write section 11", "draft the executive summary", "what sections are still weak", "turn these workshop notes into the As-Is section", "write up the happy flow", "review this discovery report", "which pain points have no requirement", or any drafting against the Discovery Report structure. Section numbers and names are fixed by the template; the skill consults the section register rather than inventing structure.
---

# Vaimo PIM Discovery Report

The Discovery Report is the deliverable of a Vaimo PIM Discovery. It is **signed off by the client**
and then used as the source of truth for what the PIM will be. It is not the Implementation
Specification — it states *what must be true*, not *how it will be built*.

Structure comes from **Discovery Report Template v3.0**: 15 sections in six parts, plus five
appendices. Numbering is fixed.

| Part | Sections |
|---|---|
| A — About this document | 1 Document Control · 2 Executive Summary · 3 Purpose, Scope and Basis |
| B — How the Discovery ran | 4 Project Set-up and Governance · 5 Discovery Timeline |
| C — Findings: current state | 6 Current State (As-Is) · 7 Data Audit and Data Readiness |
| D — Findings: target state | 8 Target State (To-Be) · 9 High Level Data Model · 10 Integrations and Customisations |
| E — Validation | 11 Happy Flow — Data Flow Proof of Concept |
| F — Conclusions and next | 12 Requirements · 13 Prioritisation, MVP and Phasing · 14 Project Outlook · 15 Approval and Rights |
| Appendices | A Glossary · B PIM Concepts · C Platform data model definitions · D Discovery survey · E Happy Flow evidence |

## Read first

| File | For |
|---|---|
| `references/sections.md` | The register: every section and subsection — purpose, where the content comes from, what form it takes, and the done-when test. Also the table skeletons and the cross-reference map. |
| `references/boilerplate.md` | Standing text that carries between clients — glossary, purpose, scope and responsibilities, Akeneo and inriver data model definitions. Reuse near-verbatim; don't rewrite it per client. |
| `references/v22-mapping.md` | Only when handling a report written on the old v2.2 structure: what moved where, and how to migrate one. |

**Load `sections.md` before drafting or reviewing anything.** Section numbers are how the client,
the PM and the signed document all refer to content; guessing one sends the reader to the wrong page.

## The two kinds of section

Every section is one or the other, and the difference decides how much work it is:

- **Standing** — the text is the same for every client, give or take the platform. Sections 3.1, 3.2,
  3.4, 3.5, 5's framing, 15.1, 15.2, and appendices A, B and C. Pull from `boilerplate.md`, swap the
  placeholders, move on. Do not agonise over these and do not "improve" them unprompted — they are
  the parts the client has learned to skim and Vaimo has learned to defend.
- **Discovered** — the content only exists because someone sat in a workshop, ran an audit, or built
  a connector. Sections 2, 4, 6, 7, 8, 9, 10, 11, 12, 13 and 14. **This is the entire value of the
  document.** Everything here must trace to something a named person said, a system that exists, a
  data extract that was analysed, or a test that was run.

A report that is thick with standing text and thin on 6, 7 and 11 has not been earned. When asked
"what's weak", weigh discovered sections heavily and standing sections at almost nothing.

## Rules

**Never invent client facts.** No number, system name, headcount, SKU count, revenue figure, or
stakeholder goal goes in unless it came from the client. If a slot has no answer, write the
placeholder and flag it — an invented plausible number survives into a signed document and then into
a budget. Placeholders stay in `<angle brackets>`.

**No worked examples in the template.** Example figures put in to show what a table looks like get
left in client documents. An empty cell is better than a plausible invented one.

**Requirements are business requirements, not solutions.** Section 12 must say what needs to be true,
never how to configure it. The moment a requirement names an attribute type, a connector or a screen,
it has crossed into the Implementation Specification. Push back on it.

**The pain point is the spine.** Every pain point in 6.7 traces forward to a requirement in 12.1 and,
where measurable, to a KPI in 8.5. Requirements with no pain point behind them are somebody's wish
list. Pain points with no requirement are the client discovering at sign-off that their problem is
not being solved. Run this trace whenever reviewing.

**Four verbs, three sections.** Create · Enrich · Edit · Delete is the lens for 6.4, 8.2 and 11.5.
Walk each one per verb. **Delete is the verb everyone skips** and the one that causes trouble at
go-live — a product that cannot be retired cleanly is a data quality problem that grows.

**Say what is out of scope, and what you need.** 3.4 and 3.5 state what the engagement does not
deliver and what remains the client's responsibility. 3.6 states what Vaimo needs *from* the client
for the conclusions to hold. Both halves, every time.

**The Happy Flow's honest paragraph is mandatory.** Section 11.6 must say what the PoC did **not**
prove. One product proves nothing about ten thousand, and a report that omits this is selling the
implementation rather than reporting the Discovery.

**Quote the SOW, don't paraphrase it.** Where the report describes scope or deliverables, quote the
signed statement of work. Paraphrase is how two documents about one engagement end up disagreeing,
and the signed one wins.

**Plain language.** The audience is a sponsor who does not work in PIM. State the consequence, not
the mechanism. Same house rule as the `px-analyst` skill.

## Writing one section

When asked "let's write section X":

1. Look it up in `references/sections.md` — take its purpose, its inputs and its form.
2. Say what inputs you have and what is missing, before drafting. If the inputs aren't in the
   conversation, ask for the workshop notes, the data extract, or the test log rather than producing
   generic filler.
3. Draft in the form the register specifies. A section whose form is a table gets a table; prose
   wrapped around a missing table is not a draft.
4. Mark every unfilled slot as `<placeholder>` and list them after the draft.
5. Check the section's cross-references and say if a sibling section now needs updating.

If a section is standing text, say so and produce it from `boilerplate.md` in one step — don't
interview the user about content the template already fixes.

## Reviewing — "what's still weak"

Grade each section into one of four states, and report by state, worst first:

| State | Means |
|---|---|
| **Empty** | Nothing but template placeholders |
| **Placeholder** | Structure present, client facts still `<in brackets>` |
| **Draft** | Real client content, but fails at least one done-when test in the register |
| **Ready** | Passes its done-when test and its cross-references agree |

Two things make this useful rather than a checklist recital:

- **Weight discovered sections, discount standing ones.** Say so explicitly — "Appendix C is Ready
  because it is boilerplate, that is not progress."
- **Report the traces, not just the states.** Pain points without requirements, requirements without
  pain points, KPIs with no As-Is baseline, an automation figure in 6.6 and 8.4 that doesn't match
  the KPI in 8.5, a data readiness verdict in 7.5 that never reaches 13.3 or 14.4, a Happy Flow with
  no "what it did not prove", an out-of-the-box steering preference in 14.3 next to a long 10.2, and
  "Overall" green in 14.5 above a red row. These are the findings people act on.

**The four sections that decide whether the report was worth the fee are 6, 7, 11 and 13.** Current
state, data readiness, proof it works, and what to build first. If those are thin, say so plainly
regardless of how polished the rest looks.

## Structural facts worth knowing

- **11 is load-bearing.** The Happy Flow PoC is always in scope for a Vaimo PIM Discovery. Section 2
  leans on it, 12 takes requirements from 11.7, and 13 phases around what it proved.
- **12 is the only home for requirements.** Nothing restates them. If a draft has a second
  requirements list somewhere, that is a defect to fix, not a summary to keep in sync.
- **5 is a timeline, not a scope restatement.** Stages, milestones, acceptance dates, and an honest
  record of what slipped and why.
- **Environments belong at the start.** 5.5 flags this: everything in the Happy Flow depends on
  environments that take real elapsed time to provision, and a gap between initiation and PoC is the
  most common reason a Discovery finishes late.
- **Appendix C keeps one platform only.** Leaving both Akeneo and inriver in signals the platform
  decision was not really made.

## Output

Draft in Markdown by default — it reviews faster and pastes into anything. When a real `.docx` is
wanted, use the `anthropic-skills:docx` skill and start from the client's copy of the template so the
Vaimo styling, header and footer survive; do not rebuild the document from scratch.

The v2.2 source document lives at `/Users/pontus/Downloads/Discovery Report Template v2.2.docx`.
There is no v3.0 `.docx` yet — the structure lives in `references/sections.md` and in the Tana outline.

## Related

`px-analyst` holds the generalised Product Information Ability Model. It is the better instrument for
*finding* what to put in sections 6, 8 and 12 — its questions are written to make a "no" discoverable,
and its `Reveals` facet turns a cluster of client asks into the system they have not named yet. Load
it when the discovery itself is being planned or when requirements need sharpening; this skill is for
turning the result into the document.

`px-data-model` produces **section 9**, and holds the rule this template states but does not explain:
section 9 is the *high-level* model, and detail belongs in the separately approved data modelling file.
It is the skill to load for any modelling question, for a data model workshop, and before promising a
client anything a platform may not be able to express.

`px-data-audit` is what produces **section 7**, and its per-area verdicts are what section 9's readiness
column takes its judgement from. Load it whenever 7 or 9 is being written, whenever a data readiness
verdict is needed, or when client export files arrive. It also carries the rule this document depends on
and most reports get wrong: **a completeness figure is meaningless without its denominator**, and the
denominator is the migration scope, not the file.
