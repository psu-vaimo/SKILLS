---
name: worklog
description: Rebuild the user's working day from Claude chats, Google Calendar, Gmail, Slack, the NOTES repo and Jira, match every block of work to a real Jira issue the user is allowed to log on (assigned to them or unassigned, not an epic, with remaining estimate, inside the weekly Tempo plan), show exactly what will be logged, then log it and move the issues to In progress. Use this whenever the user says "/worklog", asks what to log, wants to log time, fill the timesheet, book hours, or asks "how much time did I spend on X", even casually ("log today", "do my hours"). The daily skill runs it as part of the end of day. Start right away.
---

# Worklog

Rebuild the day, match each block to a Jira issue, show a transparent plan, log after one "yes".

Goal: few questions, full transparency. Make the best match yourself, show the evidence for it, and let the user correct the table instead of answering a questionnaire.

## Ground rules

- The user is a PIM consultant in the application design team. They cannot log on Project Management tickets, so never propose one.
- Every number is a reconstruction. Show what each row rests on so the user can correct it.
- Count the user's time, not Claude's. Tool calls cost the user nothing, reading and reviewing does.
- Never inflate or shrink the day. Never count the same minutes twice, never log what is already logged.
- A trace shows *when* something happened, not *how long* it took. Timestamps beat content.
- Never log on an issue that breaks the rules in "Loggable issues". Flag it instead.

## Invocation

| Argument | Period |
|---|---|
| nothing or `Today` | current date |
| `Yesterday` | previous date |
| `12.10.` or `2026-10-12` | that date (day.month) |
| `This week` or a range | those dates, one plan per day |

Take the date from system context. Use the calendar's time zone for local time.

**Day length**: 8 h, unless the user says otherwise for that day. Lunch and personal blocks are not working time. A day may land up to 1 h over or under, as long as not every day of the same week is off in the same direction. If every other day this week is already over (or under), bring this one within 8 h, or say which day to adjust.

## Step 1: Collect evidence

Search narrowly by date. Never read whole inboxes or channels. Never quote message contents, a reference like "#proj-x 14:05" is enough. Run independent lookups in parallel.

1. **Already logged**: `jira_search` with `worklogAuthor = currentUser() AND worklogDate = "YYYY-MM-DD"`, then `jira_get_worklog` per issue, keep only the user's entries for the date.
2. **Week so far** (for the plan check): `worklogAuthor = currentUser() AND worklogDate >= startOfWeek() AND worklogDate <= "YYYY-MM-DD"`, sum the user's minutes per Jira project.
3. **Claude chats**: `recent_chats` around the date with a few hours' margin (times are UTC), page until covered. Count the current chat from your own view. If a chat already holds an estimate for this date, reuse it and mark it "estimated in chat".
4. **Calendar** (Google Calendar): events for the date with time, title, attendee domains, response status, attached notes.
5. **Jira activity**: `issue in updatedBy(currentUser(), "YYYY-MM-DD", "YYYY-MM-DD+1")` with changelog, keep only the user's own changes and comments. Fallback: `(assignee = currentUser() OR reporter = currentUser()) AND updated >= "YYYY-MM-DD"`, filter changelog by author.
6. **Slack**: the user's sent messages only, `from:me on:YYYY-MM-DD`.
7. **Gmail**: sent only, `in:sent after:YYYY/MM/DD before:YYYY/MM/DD+1`.
8. **NOTES** (through the pen skill): `history` for commits on the date (their times are good anchors), the day node `^journal-YYYY-MM-DD`, and meeting notes dated that day in the project files. A task with a project is good evidence of what the work was about. NOTES is read only in this skill.

Missing source? Skip it and list it in the heading. If past-chat tools are missing, add one line: enable Settings > "Search and reference chats".

Limits to state when relevant: incognito chats, Teams and phone calls leave no trace.

## Step 2: Build the timeline

One local-time timeline for the day.

- **Meetings**: accepted ones become blocks of scheduled length. Tentative or unanswered ones become "attended?" rows. Declined, lunch and personal events are skipped.
- **Chats**: one block each, placed at the end of its window (see Step 3).
- **Loose traces**: Jira changes, Slack and email not explained by a chat. Cluster traces within about 10 min on the same topic into one block.
- **De-duplicate**: a trace produced inside a chat (posted comment, sent draft) belongs to that chat and pins its time. A meeting discussed in a chat counts once, as the meeting.
- **Overlaps**: if the user did active work for another topic during a meeting, carve those minutes out to the active work's issue and give the meeting the rest. Same project, no carve-out. If the carve-out exceeds half the meeting, mark the meeting "attended?". The same minute is never logged twice.

## Step 3: Estimate

**Chat window**: sort the day's chats by last update. A chat's upper bound runs from the previous chat's last update to its own, narrowed by real timestamps inside it. Cut estimates that exceed the window unless chats clearly ran in parallel, and note it.

| Activity | Typical time |
|---|---|
| Collecting source material | 3 to 5 min |
| Reading an issue or requirement | 5 to 10 min |
| Reviewing a draft Claude wrote | 3 to 5 min per draft, once |
| Further revision round | 1 to 2 min |
| Quick reply or choice | 1 to 2 min |
| Reviewing a message or invite draft | 5 min |
| Setting up a meeting | 5 min |
| Reading meeting notes | 5 min |
| Loose Slack reply or Jira comment | 3 to 5 min |
| Loose email | 5 min |
| Issue created | 10 min |
| Status or field change only | 1 min |
| Meeting | scheduled length |

Count off-screen work a chat mentions ("I did the workshop", "attached the files").

## The NOTES repo

`psu-vaimo/NOTES` holds the user's project facts and notes, in Ord. Read it once per run, in Step 1, through the pen skill (layout in pen's "Notes in NOTES").

- **Access**: pen's `overview`, `read_md` and `search_md`. If pen isn't available, read NOTES through pen's git fallback. If that fails too, say so in one line, mark plans "plan ?", and continue without the project facts and the mapping file.
- **Project facts**: one file per project at the root, named by project code (e.g. `ACME.txt`). The `+project` node carries `key` (Jira project key) and `planned` (Tempo Planning minutes per week). The project code may differ from the Jira key, so match on `key`.
- **Mapping file**: `Issue_mapping.txt` at the root maps common tasks and meetings to Jira issues. It is the user's own routing, so it beats every other matching rule below.
- **Internal tickets**: `Internal_tickets.txt` at the root lists the internal tickets by kind of work, the defaults for AI tooling work, and tickets never to use.

## Step 4: Match blocks to issues

### Loggable issues

A client issue can take time only if **all** hold:

- assigned to the user, or unassigned,
- not an Epic (epics are context, use them to find the right child issue),
- not Done,
- remaining estimate > 0,
- the project still has room in this week's plan (see below),
- not a Project Management ticket.

Fetch candidates once per project the evidence points to, never across all of Jira:

```
project = KEY AND (assignee = currentUser() OR assignee is EMPTY)
AND issuetype != Epic AND statusCategory != Done AND remainingEstimate > 0
```

Fields: `summary,status,assignee,parent,timeestimate,timeoriginalestimate`.

### Matching, in order of confidence

0. **Mapping file**: the block matches an entry in `Issue_mapping.txt` (meeting title, recurring task). High. The target still has to pass the loggable checks, if it doesn't, flag it on the row.
1. **Key**: the block mentions the issue key (chat, commit, Slack, NOTES task, meeting title). High.
2. **Direct work**: the user changed or commented on the issue in that block. High.
3. **Epic or topic**: the block is about an epic or feature, pick the loggable child issue whose summary fits best. Medium, mark "?".
4. **Project only**: project is clear but no issue fits. Pick the loggable open issue that best covers general work for the project (meetings, coordination, design), never a Project Management ticket. If none fits, put the row in Unmatched and ask. Medium, mark "?".
5. **No match**: put the block in the "Unmatched" list. Do not invent a target.

Identify the project from issue keys, Slack channel, email recipients, attendee domains, meeting title or the project file a NOTES entry sits in.

Client work always stays on a client issue, never on an internal one.

### Constraints check

For each proposed row:

- **Remaining estimate**: if the logged time would exceed the issue's remaining estimate, cap it at the remaining time and move the excess to Unmatched with "estimate exhausted". Every client issue that is at 0 h, or reaches 0 h with this log, gets an estimate notice (jira skill, "Estimate run out").
- **Weekly plan**: planned minutes per project mirror Tempo Planning, which no connector reaches. Take them from the `planned::` field (minutes per week, e.g. `planned:: 600`) in the project's file in `NOTES` (see "The NOTES repo"). Compare planned minutes against "week so far" + today's proposal. If over, cap at the plan and move the excess to Unmatched with "over plan". If the repo can't be reached or the file has no `planned::` field, show "plan ?" on the row and continue, do not block.

### Internal work

Work that is not for a client goes to the issue the NOTES mapping file names. If the mapping file has no entry, use `Internal_tickets.txt` in NOTES (read only when a block is internal). If a block fits nothing there, propose the closest ticket with "?". If an internal ticket would get less than 30 min, fold it into the nearest related internal row rather than rounding it up. Tooling work done for one client's delivery goes to that client. Internal tickets are exempt from the remaining-estimate rule and the weekly plan check, they usually have no estimate. They still must not be epics or Done.

## Step 5: Round and fill

- Fold time logging and other administration (including runs of this skill) into the day's other rows, spread over them by their share of the day. It never gets a row or ticket of its own.
- Sum blocks per issue, round each **issue total** up to the next 15 min step. Never round per block.
- Never log less than 30 min on an issue. Fold a total under 30 min into a related row on the same project or kind of work first. Only if there is none, round it up to 30 min.
- If rounding pushes the day more than 1 h over its length, or over at all when every other day this week is already over, trim the least-anchored rows first and say so.
- **Unaccounted** = day length minus (already logged + proposed). Show it as one row. Do not fill it on your own. Up to 1 h unaccounted is fine, under the same weekly rule as above.
- If the total is over the day length before rounding, recheck overlaps before showing anything.

## Step 6: Show the plan

Exactly this layout. Keep prose to a minimum.

**Worklog, Fri 23 Oct 2026, 8 h day, sources: chats 6, calendar, Jira, Slack, Gmail, NOTES**

| Issue | Status change | Work (worklog comment) | Time | Start |
|---|---|---|---|---|
| ACME-142 Product import mapping | To-do → In progress | Mapping review, client questions | 1 h 30 min | 09:15 |
| ACME-150 Weekly sync | none | Weekly sync | 30 min | 10:00 |
| INT-12 Internal meetings | none | Team bi-weekly | 45 min | 13:00 |
| **Total to log** | | | **2 h 45 min** | |

Already logged today: list or "none".
Unaccounted: x h y min.

**Checks** (one line per issue where it matters):
ACME-142: remaining 6 h → 4 h 30 min after logging. ACME plan this week 600 min, used 420, after logging 510.

**Evidence** (one row per block, unrounded):

| Block | Issue | Min | Basis |
|---|---|---|---|
| Chat: import mapping 08:50-10:05 | ACME-142 | 55 | key in chat |
| Slack #proj-acme 11:10-11:20 | ACME-142 | 10 | loose trace, confirm |
| Meeting: ACME weekly 10:00-10:30 | ACME-150 | 30 | mapping file |

**Unmatched**: blocks with no loggable issue, with the reason (no estimate, over plan, no open issue, attended?).

**Questions**: only what blocks logging, at most two, use `ask_user_input_v0` when available. Typical: an unmatched block over 15 min, an "attended?" meeting. Everything marked "?" is a proposal the user can just accept.

End with: "Reply **log it** to log the table above, or correct any row."

## Step 7: Log

Only after an explicit go-ahead. Corrections count as go-ahead only if the user also says to log.

Per row:

1. `jira_add_worklog` with `time_spent` (e.g. `1h 30m`), `started` at the first block's local start with offset (`2026-10-23T09:15:00.000+0300`), and the Work text as `comment`. Do not pass `remaining_estimate`, Jira reduces it automatically.
2. Status: if the issue is **New**, transition to To-do, then In progress. If it is **To-do**, transition to In progress. Use `jira_get_transitions` to find the transition ids. Other statuses stay as they are.

Worklog comments: write identifiers without underscores (the connector turns them into Markdown).

Then report in one short table: issue, time logged, new remaining estimate, status now. For each client issue now at 0 h, propose the estimate notice from the jira skill and send it after the user's go-ahead. If anything failed, say which row and why. The connector cannot edit or delete worklogs, so for later corrections tell the user which entry to change by hand in Tempo.
