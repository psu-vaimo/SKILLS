---
name: proj
description: How the user works in a project. Read at the start of any project work, in Claude Code, Cowork or chat. Use when the user types /proj, opens or sets up a project repo, asks "how do we work here", starts a new client project, asks where notes or project facts go, writes meeting notes, decisions or todos for a project, asks for a project's Jira key, planned time or dates, or when a skill should be improved. Covers the daily routine, repo layout, notes (always through the pen skill into the NOTES repo, in Ord), time logging and keeping skills up to date.
---

# Proj

How work is organised across all of the user's projects. Follow it unless the user says otherwise for a specific project.

## Rhythm

- Run **/daily** every morning (`/daily start`) and every afternoon (`/daily end`). The end of day runs **/worklog**.
- Log time **every day** with **/worklog**, on its own or through `/daily end`. Time is billed to clients, so a missed day is real lost money and work. If the day ends without a worklog, say so.

## Repos

- **One repo per project.** It holds working docs, deliverables and sometimes project-specific skills.
- **Shared skills come in as a git submodule** in each project repo. Update the submodule to get the latest skills (`git submodule update --remote`), and commit skill changes inside the submodule, not as copies in the project repo.
- **Project repos hold no notes and no project facts.** Those go in NOTES (below). If you find notes or facts in a project repo, propose moving them.

## Notes

Notes are important. They are the memory of every project and the source for status, time logging and planning.

- **Who writes:** the **/pen** skill, always. Hand every note to it, never write notes another way (no files in the project repo). When the pen connector is missing, pen's git fallback commits to NOTES.
- **Where:** the shared repo https://github.com/psu-vaimo/NOTES, one file per project named by project code (e.g. `ACME.txt`), plus a monthly journal for day-bound items.
- **Format:** Ord (https://ordlang.org). pen follows the **/ord** skill for syntax.
- **Read before writing.** pen adds to the project's existing file instead of creating a new one.

What goes in notes: meeting notes, decisions, todos, open questions, client contacts, and project facts. pen's "Notes in NOTES" section has the layout and where each thing goes.

### Project facts

Each project has its facts as fields on the project node at the top of its NOTES file, never in the project repo:

- `key`: Jira project key
- `planned`: Tempo Planning minutes per week
- `start`, `end`: dates
- `manager`: the project manager on the user's side
- `client`, `status`, and contacts under a Contacts section

daily, jira and worklog read them from there. When a fact changes, have pen update the field. If a fact is missing when you need it, ask, then have pen write it.

## Skills

Skills improve as part of ordinary work. Always keep changing and developing them:

- When the user corrects how something is done, or you repeat the same workaround, update the skill that should have known, in the shared skills repo (`psu-vaimo/SKILLS`).
- Keep skills generic. No client names, project codes, Jira keys, ticket numbers or colleagues' names in a skill. Those go in NOTES, and the skill says where to look them up. Examples use placeholders such as `ACME`.
- Keep changes small and say what changed in one line. Commit in the submodule with a message like `daily: check Slack threads since last end of day`.
- If no skill covers a recurring task, propose a new one.
- Ask before large rewrites, not before small fixes.
