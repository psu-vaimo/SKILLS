# Ord recipes

Worked examples for common requests. Indentation is one tab per level.

## Start a workspace

Create `Ord.workspace` at the folder's root. Its first line names the workspace; the rest defines types and tag colors.

```
Home notes
+note
Task [defines:: task]
	color:: blue
	state:: someday [s] > waiting
	fields::
		due::
		owner::
			target:: person
		late:: =($exists(due) and due < $today() and state != "done")
Person [defines:: person]
	sigil:: @
	fields::
		id:: auto $slug(label)
		email::
		phone::
Project [defines:: project]
	sigil:: %
	color:: purple
	fields::
		status::
		open:: =($count(children[("task" in type) and state != "done"]))
Issue [defines:: issue]
	fields::
		issue type::
			options:: bug; feature
			claims:: options
#urgent [color:: red]
#waiting-on [color:: orange]
```

- `+note` alone defines the type `note` with no fields (workspace file only).
- `#urgent [color:: red]` sets a tag's color; the line isn't a node with that tag.
- `issue type` claims its options as tags: `Login fails #bug +issue` has `issue type:: bug`, not the tag `bug`. A field of your own can't be called `type`, which is reserved for the node's type.
- `sigil:: @` lets `@anna` mean `person:: anna`; `sigil:: %` lets `%apollo` mean `project:: apollo`.
- Add a `.txt` file per topic. Files without an extension, `.ord` and `.csv` files in the folder are part of the workspace too.

## Journal days

Day nodes are found by ID. The default layout is one file per year, `journal-2026.txt`, with months at the top level and days under them, both in date order:

```
October, 2026 ^journal-2026-10
	Wednesday, 21st ^journal-2026-10-21
		Called the plumber
	Thursday, 22nd ^journal-2026-10-22
		[ ] Buy tiles [due:: 2026-10-24] +task
		Meeting with @anna +meeting
			Agreed on the kitchen layout
			[ ] Send drawings to Anna +task
		?? [ ] +task @anna
```

- Label format: `Weekday, Dth` for days (`Monday, 1st`, `Tuesday, 2nd`, `Wednesday, 3rd`, `Friday, 11th`, `Saturday, 22nd`), `Month, YYYY` for months, in English.
- To add to today: find `^journal-YYYY-MM-DD`. If it is missing, add it under its month in date order; if the month is missing too, add the month at the top level of the year's file, in date order. Create `journal-YYYY.txt` at the workspace root if needed.
- With `journal:: month` in `Ord.workspace`, the file is `journal-2026-10.txt` and days sit under ISO weeks: `Week 43, 2026 ^journal-2026-W43`. A week belongs to the month of its Thursday.
- Write today's actual date; never `~today`.

## Tasks

```
[ ] Book electrician #urgent [due:: 2026-10-30] +task
[-] Paint the hallway +task
	owner:: anna
	Second coat on Saturday
[?] Quote from #ruukki #waiting-on +task
[x] Order tiles for #home/kitchen +task
[s] Build a sauna +task
```

- Complete: `[ ]` to `[x]`. Start: `[-]`. Waiting: `[?]`. Custom: the type's marker (`[s]`).
- Tags go in the text where they read naturally, and stay part of the label. `#home/kitchen` is a nested tag: `?? #home` finds it too.
- A due date goes inline when short (`[due:: 2026-10-30]`), a field line when the node already has field lines.
- Notes about the task are child lines, not fields.
- Open tasks anywhere: `?? +task ![x]`.

## Meeting notes

```
Kitchen planning @anna @erik +meeting
	date:: 2026-10-22
	Budget is 120 000 SEK
	Tiles: Anna prefers the grey ones
	Decisions
		Keep the old cabinets #decision
	Actions
		[ ] Erik gets two quotes [due:: 2026-10-29] +task
			owner:: erik
		[ ] Anna sends the drawings +task
			owner:: anna
```

`Tiles: Anna prefers…` is prose: one colon never makes a field.

## A small database

People and companies as nodes, invoices referring to them, line items as children:

```
Ruukki AB +company
	org-nr:: "556123-4567"
Invoice 42 +invoice
	client:: Ruukki AB
	date:: 2026-10-15
	Design work
		amount:: 1000
	Review
		amount:: 200
```

With `client` defined with `target:: company` and `net:: =($sum(children.amount))` on the invoice type, `Invoice 42` shows `net` = 1200. The quotes keep the org number as text. For hundreds of line items, move them to a CSV file with a `parent` column holding `i42`, and only then give the invoice that ID, `Invoice 42 +invoice ^i42`, since the rows refer to it (see csv.md).

## Converting Markdown to Ord

| Markdown | Ord |
|---|---|
| `# Heading` with paragraphs under it | `Heading` with the paragraphs indented one tab under it |
| `- item`, `1. item` | Keep the markers, or drop them; nesting is by tab |
| `- [ ] todo`, `- [x] done` | `- [ ] todo`, `- [x] done` (same) |
| `**Owner:** Anna` | `owner:: Anna`, when it is an attribute; else `Owner: Anna` as prose |
| `[text](url)` | Same; reads as a `url` |
| Tables, code | A fenced block, with an info string: ```` ```csv ```` |
| Front matter `key: value` | Field lines under the document's root node |

Bold, italics and headings don't structure Ord: nesting does.

## Promote a local field to a type

Fields can be written on any node before a type exists. When the same fields repeat, define the type and give it to the nodes:

```
Monstera
	watered:: 2026-10-01
	every:: 7
```

becomes `Monstera +plant` on each plant, plus in `Ord.workspace`:

```
Plant [defines:: plant]
	fields::
		watered::
		every::
		next:: =($date(watered, every))
		thirsty:: =(next <= $today())
```

Then `?? +plant =(thirsty)` lists the plants to water.
