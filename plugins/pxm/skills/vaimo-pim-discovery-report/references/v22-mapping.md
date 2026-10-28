# Migrating a v2.2 report to v3.0

Load this **only** when handling a report written on the old 19-section v2.2 structure — an
in-flight engagement, or an old report being reused as a reference. New reports use v3.0 and never
need this file.

## Where each v2.2 section went

| v2.2 | v3.0 |
|---|---|
| 1 Introduction | 1 Document Control, plus a distribution list |
| 2 Executive Summary | 2, rewritten to lead on findings rather than aims |
| 3 Document Purpose | 3.1 |
| 3.1 Background Information | 3.2 |
| 4 PIM Concepts | Appendix B |
| 5 Glossary | Appendix A |
| 6 Project Set-up (who) | 4, merged with the governance half of 16 |
| 6.4 Documentation reference | 3.7 Basis of this report |
| 7 Project Setup (what happens) | 5, rewritten as a Discovery timeline with milestones. Scope detail now references the signed SOW instead of restating it |
| 8 Limitations | split — 3.4 out of scope, 3.5 client responsibilities, and the new 3.6 assumptions |
| 9 As Is | 6, with the survey grid moved to Appendix D and roles and ownership added as 6.5 |
| 9.1 PIM Survey Comments | 6.1 summary + Appendix D full grid |
| 9.5 Current Pain Points | 6.7 — now the only place pain points are listed |
| 10 To Be | 8 |
| 10.3 High Level Requirements | 12 |
| 10.4 KPIs + 10.5 Stakeholders' Goals | 8.5, merged into one table |
| 11 / 12 platform glossaries | Appendix C |
| 13 High Level Data Model | 9 |
| 14 Integrations + 15 Customisations | 10 |
| 16 Project Execution | split — governance to 4, timeline to 13.4, the rest to 14 |
| 17 Conclusions | dissolved. Its content already exists in 6.7, 8.5 and 12 |
| 18 Summary and Conclusions | 14.5 |
| 19 Approval | 15 |

## What has no v2.2 equivalent

These are additions, not moves. A v2.2 report being migrated will have nothing to paste into them,
and that gap is the point of the migration.

- **7 Data Audit and Data Readiness** — v2.2 treated data quality only as a liability disclaimer (8.2)
  and one column in the data model table
- **11 Happy Flow — Data Flow Proof of Concept** — no v2.2 home at all
- **13 Prioritisation, MVP and Phasing** — v2.2 had priority columns but nothing defining a first release
- **3.6 Assumptions and collaboration principles** — v2.2 stated what Vaimo would not deliver, never
  what it needed from the client
- **4.4 RACI**, **5.7 milestones and acceptance**, **5.8 deviations from plan**
- **6.5 / 8.3 roles and ownership**
- **14.4 revised estimate** — v2.2 promised to find budget deviations in its executive summary and gave
  the finding nowhere to live
- **14.6 open questions and recommendations**
- **15.2 rights to deliverables and platform licensing**

## Why the structure changed

- **The template stopped matching what is sold.** The Discovery runs current-state work, a legacy data
  audit, target-state definition, a Happy Flow proof of concept and the report. v2.2 had sections for
  two of those. The PoC is a quarter of the invoice and had nowhere to be written up.
- **v2.2 said the same thing twice.** Pain points in 9.5 and 17.1; requirements in 10.3, 17.3 and 17.4;
  conclusions in 17 and 18. Every duplicate is a chance for the two copies to disagree before sign-off.
- **Limitations were one-sided.** What Vaimo will not deliver, with no statement of what it needs.
- **Reference material sat in the middle of the argument.** Glossary, PIM concepts and two platform
  dictionaries between purpose and findings.
- **There was no lens.** v3.0 frames 6.4, 8.2 and 11.5 on the same four verbs — Create · Enrich · Edit
  · Delete — which makes gaps visible. Deletion appeared nowhere in v2.2.

## Migrating one in flight

1. Requirements first. Collapse 10.3, 17.3 and 17.4 into a single register at 12, keeping the `BR`
   IDs unchanged — they are quoted elsewhere and must never be renumbered.
2. Pain points second. 9.5 and 17.1 become 6.7; keep whichever wording is sharper.
3. Then move the reference material to appendices, which is mechanical.
4. Then confront the gaps: 7, 11 and 13 will be empty. If the engagement did the work, write them. If
   it did not, say so explicitly rather than leaving the sections out — a missing data audit is a
   finding about the Discovery, not a formatting choice.
