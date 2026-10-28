---
name: pen
description: Read and edit Ord and markdown text files in GitHub repositories through the pen MCP server, and the only way to take notes. All notes go to the NOTES repo (psu-vaimo/NOTES) in Ord. Use when the user says "pen" (e.g. "pen a note", "pen this to X"), asks to take, write, update, or read notes, says "stash this" or asks what is stashed, meeting notes, decisions, todos, project facts or a daily plan, asks to write or read docs in a GitHub repo, or refers to a repo served by pen. Other skills (proj, daily, worklog, jira) hand all note reading and writing to this skill.
---

# pen

pen edits text files in GitHub repositories: Ord (preferred) and markdown (`.md`, `.markdown`). `.txt` and `.ord` files are Ord; a path with no extension gets `.txt`. Every edit is a real commit; nothing is staged. For how to write Ord itself, use the `ord` skill. Where notes go is in "Notes in NOTES" below.

## Before you start

- Every tool takes `repo` (`"name"` or `"owner/name"`). Notes always go to `psu-vaimo/NOTES` without asking. For anything else, if the user hasn't named a repo, ask.
- Single-repo mode: if the connector's instructions say the PAT reaches exactly one repository, `repo` is optional and defaults to it. Use that repository without asking.
- Starting work in a repo: call `overview(repo)` first. It returns the root index, `INDEX.txt`, `INDEX.ord` or `INDEX.md` (the map of what lives where), every file path with its size, and each text file's blob SHA.
- Text files are `.txt`, `.ord`, `.md` and `.markdown`. All tools read and search them the same way. In Ord files (`.txt`, `.ord`) the outline lists nodes with children; in markdown, headings.

## Reading

- `read_md` returns exact text, blob SHA, and an outline (headings, or Ord nodes with children) with line ranges. Batch with `paths:[...]` (up to 20) instead of one call per file. For a long file, `offset_lines` starts at a line; `max_bytes` caps the call.
- `list_md` lists files with blob SHAs. Use `outline:true` on a narrowed listing (40 files at most) to see sections without reading. `path_prefix` is a folder (`"docs"` means `docs/…`).
- `search_md(query)` finds literal text (not regex) across text files and returns path, line number and the line. Case-insensitive unless `case_sensitive:true`. It scans up to 400 files; narrow with `path_prefix`. Use it to find a phrase, name, `^id` or `[[link]]` instead of reading files hoping to find it.
- `check_links()` lists relative links that point at nothing. `check_links(target)` lists every link pointing at a file or folder, with the full line.
- `history` and `show_commit` answer who changed what and when.

## Writing
- `commit_edits` is the only way to edit. One call = one commit, all edits or none. Put every change in one call. Later edits see earlier ones.
- Pick the smallest operation:
  - `str_replace` for exact text changes. Copy `old_string` straight from `read_md` or `search_md` output, tabs included. `replace_all:true` replaces every match.
  - `edit_section` to replace, append, prepend, or delete a section by its heading, or in Ord by any node, leaves included. Address a node by its text, by a path (`"Guide > Install"`), by an index (`"Notes#2"`), or by its `^id` (`heading:"^milk"`). Marks may be left out: `"Call Bo"` finds `[ ] Call Bo [due:: 2026-10-22]`. In Ord, `content` is re-indented under the node at every depth in the file's own indentation, so write it unindented and use tabs or spaces for deeper levels. `append` on a leaf gives it its first child; `replace` changes the children only; `delete` removes the node and its children.
  - `move_node` (Ord only) to move a node with its children: `heading` is the node, `under` the new parent (omit for top level), `to` another existing file (omit for the same file), `mode` `"append"` (default, last child) or `"prepend"` (first child). Use it to file a task under Done or move a note from an inbox to a project.
  - `write` with `mode:"append"` to add to the end of a file.
  - `write` with `mode:"create"` (default) for new files. Fails if the file exists.
  - `write` with `mode:"overwrite"` only when rewriting a whole file.
  - `move` with `path` and `to` to rename or move a file. Keeps the content, never overwrites `to`; later edits in the same call can target the new path.
- Before a `move` or `delete`, call `check_links(target:"<old path>")` and fix every link it lists in the same `commit_edits` call. A move does not fix links by itself.
- `expect_sha` is required for `delete` and `overwrite`. Get it from `overview`, `read_md` or `list_md`.
- Paths are repo-relative, with no leading slash. **Write new files as Ord with the `.txt` ending**; a path with no extension gets `.txt`. Use `.ord`, `.md` or `.markdown` only when the user asks for it or the file already has that ending. Keep an existing file's format.
- Write a short, specific commit message.
- If a commit fails, the batch is held as a `retry_ref`; once the cause is fixed, resend it with the exact call the error gives instead of retyping the edits.
- A rate-limit error says when GitHub's limit resets. Wait until then; don't retry in a loop.

## Ord in pen
The `ord` skill has the full rules, and https://ordlang.org the full syntax. The ones that matter most for edits:

- One line is one node; children are indented one tab deeper. No markdown headings: a node with children is a section.
- A field is `key:: value` on its own line, or `[key:: value]` in brackets on a node line. A line with `::` outside brackets and quotes is a field line, so put `::` in prose in backticks. Notes and prose are added as child lines. Use fields for data points, attributes you filter or compare on, references, and structured information repeated on several nodes.
- Change only the lines the edit needs. In `str_replace`, include the leading tabs in both strings, and indent new lines like their siblings. Prefer `edit_section` or `move_node`, which indent for you.
- Adding to a node: `edit_section` with `mode:"append"` and unindented `content` puts the lines last under it, at the right depth, even when the node has no children yet.
- To add something for today in a workspace with a journal, address the day node by its id, e.g. `heading:"^journal-2026-10-22"`. If it doesn't exist yet, add it in date order: with `journal:: month` (as in NOTES) under its ISO week (`^journal-2026-W43`) in `journal-2026-10.txt`, otherwise under its month (`^journal-2026-10`) in `journal-2026.txt`. Label the day `Weekday, Dth`, e.g. `Thursday, 22nd ^journal-2026-10-22`. Create the week, month or file if missing. The `ord` skill's recipes have the details.
- Commit results warn, without blocking, when an edit introduces mixed tabs and spaces, a line more than one level deeper than its parent, or a `note::`/`[note:: …]` field. Fix it in a follow-up commit.

## Repo conventions

- Each repo describes itself in its root index (`INDEX.txt`, `INDEX.ord` or `INDEX.md`), often with a folder index per folder. Whenever you add, move or delete a file, update the index that lists it in the same commit. Do this without asking the user; it is part of the edit. Write the entry in the index's own format.
- If a commit result ends with a note that no index was updated, update it right away in a follow-up commit.
- `create_repo` makes a new private repo seeded with `INDEX.txt`. Its `overview` is written in Ord and placed under a root node named after the repo, so write it unindented, as the landing page: what's here and where to go.

## Notes in NOTES

All note taking goes through this skill, into `psu-vaimo/NOTES`, in Ord. That covers meeting notes, decisions, tasks, open questions, contacts, project facts, daily plans and captures. Never write notes anywhere else: not a project repo, local files or memory. If the pen connector isn't available, use the git fallback below.

Start with `overview(repo:"NOTES")` and read the project file or journal file before adding to it.

**Layout.** Flat, everything at the root, no subfolders:

- `Ord.workspace`: types `+project`, `+task`, `+issue`, `+meeting`, and `journal:: month`.
- `INDEX.txt`: the map. Add a line when you add a file.
- `Issue_mapping.txt`: the user's rules that route recurring tasks and meetings to Jira issues. The worklog skill reads it.
- `Internal_tickets.txt`: the internal tickets for work that isn't for a client and isn't in the mapping. The worklog and jira skills read it.
- One file per project, named by project code, e.g. `ACME.txt`. Project codes, clients, Jira keys and people are only in these files. Look them up there, the skills only use placeholders.
- The journal: `journal-YYYY-MM.txt`, day nodes under ISO weeks, labelled `Monday, 26th ^journal-2026-10-26`.
- `stash.txt`: paused work, see "Stash" below.

**Project file.** The root node is the project, with its facts as fields, then sections created as needed:

```
ACME +project
	key:: ACMEPIM
	planned:: 600
	status:: active
	notify:: #proj-acme
	client:: Acme AB
	manager:: Jane Doe
	start:: 2026-09-01
	end:: 2026-12-31
	Meetings
		Weekly sync 2026-10-23 #ACME [date:: 2026-10-23] +meeting
			Data import moves to week 45
	Decisions
	Tasks
		[ ] Send mapping draft to Anna #ACME [due:: 2026-10-26] +task
	Questions
	Contacts
```

- `key` is the Jira project key, `planned` the Tempo Planning minutes per week (a number), `status` is `active`, `paused` or `closed`, `manager` the project manager on the user's side, `notify` the Slack user (`@name`) or channel (`#channel`) to tell when an issue runs out of estimate.
- When a fact changes, edit the field. Git keeps the old value.
- If a fact another skill needs is missing, ask the user, then write it here.

**Where things go.**

- Anything about one project goes in its project file, under the matching section: meeting notes, decisions, tasks, questions, contacts, facts.
- Day-bound things go under the day node in the journal: the daily plan, the day's meetings, captures, and tasks with no clear project (`[ ] Reply to Anna: invoice [due:: 2026-10-23] +task`).
- A task is `[ ] label #ACME +task` with `[due:: …]`. Complete it with `[x]`.
- Every typed node (`+task`, `+meeting`, `+issue`, …) whose type has a `project` field gets the project tag, `#ACME`, wherever it sits, in the project file too. Leave it off only when there is no clear project.
- Prefer shortforms to fields: `#ACME` not `[project:: ACME]`, `@anna` not `owner:: anna`. See the `ord` skill's "Shortforms over fields".
- To point at a task or meeting from the journal, link it by label, `[[Send mapping draft to Anna]]`, instead of copying it.
- Don't add `^id` to new nodes. Add one only when necessary, e.g. a link target whose label isn't unique. Journal nodes always get their `^journal-…` ID.
- Commit messages name the project or the day: `ACME: notes from weekly sync 2026-10-23`, `journal: plan for 2026-10-24`.

## Stash

Work that is interrupted, paused or has to continue another time goes to `stash.txt` in NOTES, so a later session can pick it up.

- When a session stops before the work is done, suggest stashing it. The user can also ask, e.g. "stash this".
- `stash.txt` has one root node, `Stash ^stash`. Add each item with `edit_section` append on `heading:"^stash"`, as one node `YYYY-MM-DD topic`, plus the project tag (`#ACME`) when the project is clear. Children say where it stopped, what is done, the open questions and the next step, enough for a session with no other context.
- Lifting an item: when the work is picked up, delete its node if it is finished in that session, otherwise move it where it belongs with `move_node`, e.g. to the project's Tasks or today's day node. A lifted item never stays in the stash.
- Commit messages: `stash: <topic>` and `stash: lift <topic>`.

## Git fallback

When the pen connector isn't connected, work on a git clone of `psu-vaimo/NOTES` instead. Say so in one line, then follow every other rule in this skill: Ord, the layout, index updates, one commit per change, the commit message style.

- Use an existing clone if the session has one, otherwise `git clone https://github.com/psu-vaimo/NOTES`. Pull before editing.
- `overview` is `INDEX.txt` plus `git ls-files`. `read_md` is reading the file, `search_md` is `grep -rn`, `history` is `git log`.
- Edit only the lines the change needs, with tabs for indentation, as `str_replace` would. Check that no line mixes tabs and spaces or sits more than one level deeper than its parent.
- Commit all edits of one change in one commit, then push. Push to the branch the session assigns, otherwise to `main`. If the push is rejected, pull with rebase and push again.
- If git can't reach the repo either, show the Ord lines that would have been written and stop.

## Interpreting requests

- "stash this" means add the current work to the stash, see "Stash".
- "pen X", "note X" or "take a note" means write X to NOTES, in the project file when the project is clear, otherwise under today's day node.
- "pen X to file" means append to that file unless the user asks to replace it. In Ord, "add X under Y" means `edit_section` append on node Y, and "move X to Y" means `move_node` with `under:"Y"`.
- If the target file or wording is unclear, make a sensible choice and say what you did, or ask if it matters.

## After a commit

Report the file path and the short commit SHA with its link. Don't re-read the file to confirm; the commit result is the confirmation.
