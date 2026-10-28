---
name: daily
description: Run the user's start of day or end of day routine across Jira, Gmail, Google Calendar, Slack and the user's NOTES repo. Use when the user types /daily, "start of day", "end of day", "good morning, let's start", "wrap up the day", "close the day", "what's on today and what needs a reply", or "plan tomorrow". Start right away. Takes precedence over the morning skill for these requests.
---

# Daily

Two routines, start and end of day. Pick one from the argument (`/daily start`, `/daily end`) or the time of day if none is given (before 12:00 local is start, otherwise end, and say which was picked). Get the date and time from `user_time_v0`.

Other skills do the detailed work, read them as needed:
- **jira** for Jira searches, status changes and project facts
- **worklog** for the day's time: rebuild, match, log
- **pen** for every read and write in NOTES (layout and where things go in its "Notes in NOTES"), with **ord** for the syntax
- **proj** for how projects are organised

Writes to Jira, NOTES, mail or Slack wait for the user's go-ahead. Collect everything first, show one summary, then ask once.

## Start of day

### 1. Collect

Run these and keep only what concerns today or needs action:

- **Jira:** jira skill's "Find my work" and "What needs updating". Only issues with remaining estimate count as workable.
- **Calendar:** today's events. Keep time, title, attendees' domains, the user's response. Skip declined and personal blocks.
- **Mail:** Gmail threads in the inbox from the last working day (since Friday on a Monday) where someone is waiting on the user: direct questions, requests, unanswered threads addressed to them. Skip newsletters, notifications and CC-only threads. Open each thread and skip it when the latest message is from the user, or the user has replied (including from Sent) after the message that asked them. Only keep a thread if someone wrote again after the user's reply and is waiting on them.
- **Slack:** mentions and DMs since the last working day that the user hasn't answered (search `to:me`, `@mentions`, then check the thread for a later reply from the user).
- **NOTES tasks:** every task not done (`[ ]` or `[-]` with `+task`) across NOTES, from `search_md("+task")` through pen, and anything on today's day node already (`^journal-YYYY-MM-DD`).
- **Stash:** every item under `^stash` in `stash.txt` (pen's "Stash").

Never quote message contents at length. A short reference ("Anna, client X, data import question") is enough.

### 2. Show

**Start of day, [Fri 23 Oct]**

**Meetings:** time, title, project, one line each.

**Jira, workable today:** key, summary, status, remaining. Then flagged issues from "What needs updating", one line each.

**Needs a reply:** one table for mail and Slack.

| From | Where | About | Project |
|---|---|---|---|

**Stash:** date, topic, project, one line each.

**NOTES, open tasks:** task, project, due. Overdue and due today first, then the rest by due date, undated last.

### 3. Propose and confirm

Propose in one list:
- a task per mail or Slack item still needing a reply (never for a thread the user already answered, and not when an open reply task for it already exists), `[ ] Reply to [who]: [topic] [due:: today's date] +task`, in the project file's Tasks when the project is clear, otherwise under today's day node
- today's meetings as one line each under today's day node, `09:00 ACME weekly sync`. Meeting notes go in the project file later, through pen.
- which stash items to lift today. Lifting follows pen's "Stash": move the item to today's day node or its project, or delete it once done.

Ask "add these?" and let the user drop items. Then write them through pen in one commit and report what was added.

## End of day

### 1. Time

Run the worklog skill for today. It rebuilds the day, checks remaining estimate and the week's Tempo plan, logs after the user's "log it" and moves New or To-do issues to In progress.

### 2. Jira status

From the issues the user touched today, propose the remaining status changes (In progress to Done or review) through the jira skill. Worklog already moved New and To-do. Confirm, then apply.

### 3. Done tasks

- Show NOTES tasks that were open and due today, plus the reply tasks created this morning. For each, check for evidence it's done (the user's sent mail or Slack reply, a Jira change). Propose marking those done (`[x]` through pen), ask about the rest.
- List what got done today in a few lines, so the user can check it against the time log.
- Offer to stash work that was started and not finished (pen's "Stash"). Delete or move stash items that were lifted and finished today.

### 4. Plan tomorrow

- Collect tomorrow's meetings, open NOTES tasks due tomorrow or still open from today, and workable Jira issues with the most urgency (due date, client waiting, week's plan not yet used).
- Propose a short plan: meetings, then up to five priorities. Keep it realistic against free time in the calendar.
- After the user's go-ahead, have pen write it under tomorrow's day node (`^journal-YYYY-MM-DD`, created if missing) as a "Plan" node with the priorities as children, linking existing tasks by label (`[[label]]`) instead of duplicating them. Don't add IDs to the plan or its children.

## Output

Direct and brief. Tables for lists, no long prose. Never use dashes as punctuation or semicolons. End each routine with at most one question.
