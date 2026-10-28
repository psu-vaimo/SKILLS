---
name: jira
description: Manage the user's Jira issues and time logging through the mcp-atlassian connector. Find the user's open work across ongoing projects, flag issues that need updating, add comments and worklogs, change statuses and check time against Tempo Planning. Use this whenever the user asks "what are my Jira tasks", "what's open on project X", "log 1h on X", "comment on the ticket", "move it to in progress", "what needs updating", "how much time is left on project Y this week", or runs the start or end of day routine, even if Jira isn't named. For rebuilding and logging a whole day's time from chats, calendar and Slack, use the worklog skill, which follows the rules here.
---

# Jira

The user works on client projects in Jira Server with Tempo. This skill covers finding work, keeping issues current and logging time. It writes to a system clients are billed from, so every write waits for the user's go-ahead.

## Tools

Use the mcp-atlassian connector (load it with `tool_search` if deferred): `jira_search`, `jira_get_issue`, `jira_get_transitions`, `jira_transition_issue`, `jira_add_comment`, `jira_add_worklog`, `jira_get_worklog`, `jira_update_issue`. If it isn't connected in this session, say so in one line and stop. Don't fall back to guessing.

## Rules

These come from the user and hold in every action:

1. **Epics are context, not tasks.** Exclude `issuetype = Epic` from task lists. Use an issue's epic only to explain what it belongs to.
2. **The user's tasks are assigned to them or unassigned.** Search both, within their ongoing projects only.
3. **Only issues with remaining estimate are workable.** An issue with no remaining estimate (empty or 0) is not something to work or log on. Flag it instead of logging. Internal tickets (INTERNAL*) are the exception: they usually have no estimate and no weekly plan.
4. **Tempo Planning caps each project per week.** The user is planned a set number of minutes per project per week. Don't propose logging that pushes a project over its plan without saying so.
5. **Logging time on a New or To-do issue moves it forward.** After logging, if status is New, transition to To-do, then In progress. If To-do, transition to In progress. Read the available transitions with `jira_get_transitions` each time, since names differ between projects.
6. **Confirm before writing.** Show what will be logged, commented or transitioned, then wait for "yes", "log it" or similar. Batch confirmations: one table, one go-ahead.

## Ongoing projects and common tickets

The user keeps these in their NOTES repo. Read them through the pen skill before searching Jira (layout in pen's "Notes in NOTES"):

- **Ongoing projects:** the `+project` nodes with `status:: active`, one file per project. Take `key` (Jira project key) from each.
- **Common tickets:** `Issue_mapping.txt` routes recurring tasks and meetings to issues. Other internal work goes to the internal tickets listed in `Internal_tickets.txt`.

If a project has no `key` in NOTES, ask once, then have pen write it there. Don't keep projects, clients, Jira keys or ticket numbers inside this skill. They live in NOTES.

## Find my work

```
project in (KEYS) AND issuetype != Epic AND statusCategory != Done
AND (assignee = currentUser() OR assignee is EMPTY)
ORDER BY project, status, updated DESC
```

Request fields `summary,status,assignee,timeestimate,timeoriginalestimate,parent,customfield for epic link if present,updated,duedate`. Show one compact table grouped by project:

| Key | Summary | Status | Remaining | Note |
|---|---|---|---|---|

Mark unassigned issues "unassigned", and issues without remaining estimate "no estimate, not workable".

## What needs updating

Run this as part of the start or end of day, or when asked. Flag, don't fix:

- **In progress but untouched:** status In progress and `updated <= -5d`.
- **Logged on but not moved:** the user has worklogs on it (`worklogAuthor = currentUser()`) but status is still New or To-do.
- **Out of estimate:** open, the user's, and remaining estimate is 0 or empty. Propose an estimate notice (see "Estimate run out").
- **Overdue:** `duedate < now()` and not done.
- **Waiting on the user:** issues where someone else commented after their last activity (read the comments on the few candidates, not every issue).
- **No real description:** the description is empty, or holds only template boilerplate (headings or prompts such as "As a … I want …" or "Acceptance criteria" with nothing filled in). Request `description` for this check. Suggest a short description, two or three lines on what the issue covers and what done looks like, drafted from the summary, epic, comments and the project's NOTES.

List each with one line saying what update seems needed. Ask before changing anything.

## Log time

1. **Pick the ticket.** Client work goes to that client's ticket, never its Project Management ticket, which the user can't log on. Recurring work follows `Issue_mapping.txt`, other internal work `Internal_tickets.txt`, both in NOTES. If unsure, ask.
2. **Check the issue.** Remaining estimate must be above zero. If the time to log exceeds it, say so and ask whether to log anyway or pick another issue.
3. **Check the week's plan.** Sum the user's worklogs for that project this week:
   `project = KEY AND worklogAuthor = currentUser() AND worklogDate >= startOfWeek()`, then `jira_get_worklog` per issue, keeping only the user's entries from this week. Compare with the planned minutes for the project from Tempo Planning (see below). Show "logged / planned this week" for the project.
4. **Show and confirm.** One row per worklog: key, time, start, comment, then the status change it will trigger under rule 5.
5. **Write.** `jira_add_worklog` with `time_spent` in Jira format (`1h 30m`), `started` as local time with offset (get it from `user_time_v0`, e.g. `2026-10-22T09:00:00.000+0200`), and the comment. Avoid underscores in comments, the connector mangles them. Then apply rule 5 transitions.
6. **Report** what was written in a short table. The connector can't edit or delete worklogs, so tell the user which entry to fix by hand if a number was wrong.

Round each ticket's total for the day up to the next 15 minutes, and never log less than 30 minutes on a ticket. Time logging and administration have no ticket of their own, they are baked into the tickets the day's work went to.

## Tempo Planning

The planned minutes per project per week live in Tempo Planning (resource planning view), which mcp-atlassian can't read. In order:

1. Use planned numbers the user gave earlier in the conversation.
2. Use the `planned::` field (minutes per week) on the project in NOTES, read through pen.
3. Otherwise ask for the planned hours for the projects in question, and have pen write them to `planned::` in NOTES.

Never invent a plan. If it's unknown, show "plan ?" and still log once the user confirms.

## Estimate run out

When a client issue has no remaining estimate, or reaches 0 h with a worklog, tell the people who can raise it:

1. **Recipient.** Read `notify::` on the project in NOTES through pen: a Slack user (`@name`) or channel (`#channel`). If it's missing, ask once and have pen write it there.
2. **Draft** one short Slack message in the user's voice, in the language the project uses: issue key and summary, time spent against the original estimate, what work is still to come, and the ask (raise the estimate or point to another issue). One message per recipient, listing every issue that ran out.
3. **Confirm, then send** with the Slack connector. If Slack isn't connected, show the draft so the user can paste it.

Don't send the same notice twice for an issue. Search the channel or DM for the issue key first.

## Comments and status changes

- **Comment:** `jira_add_comment`. Draft it in the user's voice, short, in the language the ticket uses. Show the draft, post after go-ahead.
- **Description:** `jira_update_issue` with the `description` field. Keep it short, in the ticket's language, and replace boilerplate rather than adding below it. Show the draft, write after go-ahead.
- **Status:** `jira_get_transitions`, pick the transition matching what the user asked, `jira_transition_issue`. If the target status needs fields (resolution, comment), ask for them.
- **Assign to the user:** when the user starts on an unassigned issue, offer to assign it to them with `jira_update_issue`.

## Start and end of day

- **Start of day:** run Find my work and What needs updating, and return the workable issues for today alongside the other routine sources.
- **End of day:** the daily skill runs worklog, which rebuilds the day and logs by the rules here. Then apply the remaining status changes and list issues the user touched today so they can mark any done.
