---
name: ord
description: Read, create and update Ord files (.ord, Ord.workspace, and .txt or .csv inside an Ord workspace), and write Ord formulas (JSONata) and search queries. Use when a file is Ord or Ordlang, when the user asks for notes, tasks, journals, types, tags, fields, computed fields, searches or views in Ord, or when text has lines like `key:: value`, `+type`, `#tag`, `^id`, `[[link]]`, `[x]`, `search::` or `?? query`.
---

# Ord

Ord is a plain-text outliner with structured data. One line is one node or one field, indentation makes the tree, and fields turn the outline into a queryable graph. The file is the source of truth: it must stay readable as plain text, and every edit should look like something a careful person typed.

The normative sources are the Ordlang specs: `Ord specification` 0.5.0-draft (syntax, rules C and L, files F), `Semantics` (meaning across a workspace, rules M), `CSV mapping` (rules V) and `JSON mapping`, all at https://github.com/ordlang/ord with one shared version. 0.5.0 renamed kind to type: `+task` is a type and `#urgent` a tag, the reverse of earlier versions. Rule IDs are given below so you can look them up. Where an informal document disagrees with a spec, the spec wins.

More detail, loaded when needed:
- [references/formulas.md](references/formulas.md): the formula data model, every function, dates and journals in formulas, more examples.
- [references/queries.md](references/queries.md): query terms, search nodes, view and column settings.
- [references/csv.md](references/csv.md): CSV files in a workspace, reading and writing rows.
- [references/diagnostics.md](references/diagnostics.md): what each diagnostic code means and how to fix it.
- [references/recipes.md](references/recipes.md): worked examples: a new workspace, journal days, tasks, meetings, a small database.

## Reading a line

Each line is decided by punctuation alone, never by words or letter case.

- **Field or node (C5, C11, C51).** A line is a field when it has `::` outside quotes and brackets `[…]`. The first such `::` splits it: the text before is the key (any text, spaces included), the text after it the value, with or without a space between. Every other line is a node, and its text is the label.
  - `due:: 2026-10-10` is a field. `Project lead:: Anna` is a field with the key `Project lead`.
  - `due::2026-10-10` is a field too. To put a field on a node line, use an inline field in brackets: `Call Anna [due:: 2026-10-10]` (below).
  - `::` in prose makes a field line: write `` `std::vector` `` in backticks.
  - `Note: remember this` is a node. Prose never becomes a field by accident.
  - `key::` with nothing after it is a field with no value.
- **Tree (C9).** A line's parent is the nearest line above with a smaller indent. Blank lines don't count. Tabs and spaces each count as one; keep one of them per file (tabs by default).
- **Fields belong to the node above them.** Field lines under a node are that node's fields, written before its child nodes by convention (W1).
- **Items (C15, C16).** A field value splits into items at `;`: `tags:: a; b; c` has three. Empty parts are dropped. Labels are never split.
- **Child lines of a field (C13).** A field's child node lines are more items, and its child field lines are grouped into one anonymous node:
  ```
  contact::
  	primary:: anna
  	email:: anna@example.com
  ```
  In formulas this reads as `contact.primary`.
- **Quotes (C21 to C25).** `"` and backticks are the quote characters; `'` is ordinary text. A key, label, value or item that is exactly one quoted string is literal: `note:: "x; y"` is one item, and a quoted label is never read for triggers. Inside `"…"`, JSON escapes apply (`\"`, `\\`, `\n`, `\uXXXX`). A backtick span hides `::` and `;` anywhere on a line; a `"` only opens a span where a key, label, value or item starts, so `say "hi" now` and `5" screen` are plain text.
- **Blocks (C29 to C31).** Three or more backticks on their own line open a literal block, closed by a line of at least as many backticks. The whole block is one node; nothing in it is parsed. An info string names the content's language, as in Markdown: ```` ```csv ````, ```` ```js ````. Tables, HTML and anything else that must stay literal go in a block.
- **No headings.** `# Heading` is plain text (`#` followed by a space is not a tag). A node with children is a section.
- **No syntax errors (C35).** Every file reads into a tree. Doubtful text gets a diagnostic, never a failure.

## The node line

A node line holds the label plus shortforms, read wherever they are written (Spec Part 2):

```
- [x] Send mapping draft to @anna #urgent [due:: 2026-10-10] +task ^t9x1
```

| Written | Is the field | Rule |
|---|---|---|
| `-`, `*`, `+`, `1.` and a space, at the start | list marker, decoration only (`•` is text) | L16 |
| `[ ]`, `[-]`, `[?]`, `[x]` at the start (after any list marker) | `state`: new, in-progress, waiting, done | L11 |
| `[r]` or another character | `state`: the custom state whose marker it is | L11, M29 |
| `+task` | `[type:: task]` | L7 |
| `^t9x1` | `[id:: t9x1]` | L8 |
| `#urgent`, `#project/apollo` | `tag`: a tag, nested with `/`, that stays in the label | L13 |
| `[key:: value]` | an inline field | L5 |
| `[[Ruukki AB]]`, `[[ruukki]]`, `[[Ruukki AB^ruukki]]` | `link`: a reference by label, ID, or both | L10 |
| `@anna` | a sigil: `person:: anna`, only if a type binds `@` | L15 |
| `https://…`, `./file.pdf`, `~/x`, `[text](url)` | `url` | L14 |
| `=(a + b)` | `formula`: an inline formula, output only | L12 |
| `?? query` at the start (after any list marker) | `search`: an inline search | L28 |

- **Label (L19).** The label is the line without the list marker, state, inline fields, types and ID. Tags, links, URLs, sigils and formulas stay in the label where they are written. Above, the label is `Send mapping draft to @anna #urgent`. A reference by label matches with or without the tags (M23): `[[Send mapping draft to @anna]]` finds it.
- **Names (L3).** Type names, tag names and IDs are a letter followed by letters, digits, `_` and `-`. `#5`, `# heading`, `C#`, `+46` and `C++` are plain text.
- **Tags (L13).** `#` and a name, with `/` between names for a nested tag: `#project/apollo`. A tag ends after its last name, so `#projectX.` at the end of a sentence is the tag `projectX` followed by `.`. Write tags where they read naturally: `Call #anna to decide on budget #projectX +task`.
- **Inline fields (L5).** `[key:: value]`, anywhere on the node line. The key is a name, or quoted (`["Project lead":: anna]`). The value runs to the closing `]`, so it can have spaces (`[note:: two words]`, `[at:: 2026-10-15 14:30]`) and `;` splits it into items. Brackets inside nest: `[client:: [[Ruukki AB]]]`. A quoted inline value is always text, never a reference: use a link for a reference with spaces.
- **Sigils (L15, M19).** No character is a sigil until a type binds it with `sigil:: @`. Without that, `@anna` is plain text. A sigil reference matches a node of that type by ID, or by a label that is one word without its tags.
- **Literal text (L17, L18).** A backslash makes a form plain text: `\+task`, `\^id`, `\#tag`, `\[[x]]`, `\=x`, `\[due:: x]`, `\??`. So do backticks: `` `#code` ``.
- **Value forms (L21 to L27)** are read in field items only, never in labels: numbers (`-12`, `9.5`; not `007`, `+46`, `1e3`, `.5`), booleans (`true`, `FALSE`; not `yes`), dates (`2026-10-15`), datetimes (`2026-10-15T14:30`, `2026-10-15 14:30`, `2026-10-15T12:30Z`), weeks (`2026-W42`) and months (`2026-10`). A date that doesn't exist, like `2026-02-30`, is text with a warning. Quote a value to keep it text: `zip:: "01234"`.

## What a workspace means

- **Files (Spec F1 to F5).** A folder with an `Ord.workspace` file (any letter case) is a workspace: under it, `.txt` files (`.ord.txt` included), files without an extension and `.ord` files are Ord, and `.csv` files are nodes, one row each (see [references/csv.md](references/csv.md)). The workspace file is itself an Ord file, usually holding the type definitions; its first line can name the workspace. `workspace.ord` is an ordinary file. Outside a workspace, only `.ord` marks a file as Ord. Name new files `.txt` in a workspace; use `.ord` for a file that must be Ord on its own.
- **Types (M17 to M19).** A node with a `defines` field, such as `Task [defines:: task]`, defines a type. In `Ord.workspace` only, a line that is just `+name` is short for a definition. A node can have several types; there is no inheritance. A type without a definition is allowed.
  ```
  Task [defines:: task]
  	color:: blue
  	state:: review [r] > in-progress | shipped > done
  	fields::
  		due::
  		owner::
  			target:: person
  Person [defines:: person]
  	sigil:: @
  	fields::
  		id:: auto $slug(label)
  		email::
  ```
  A definition's settings are `sigil`, `fields`, `state` and `color`. Its prose children are documentation.
- **Colors and tag settings (M19).** `color` is how editors show the type: `red`, `orange`, `yellow`, `green`, `teal`, `blue`, `purple`, `pink`, `brown`, `gray`, `black`, `white`, or `#rrggbb`. It can also name a field, `color:: project`, so a node's type shows in the color of the node its `project` value refers to. In `Ord.workspace`, a line that is only tags plus settings sets those tags' color: `#urgent [color:: red]`. That line isn't tagged itself.
- **Field definitions (M36 to M40).** Each field line under `fields::` defines a field. Its value is its `value` setting, which can also be written as a `value::` child line:
  - `=expr` makes a computed field.
  - `auto expr` is an auto value, written once when the node gets the type and the field is empty.
  - Anything else is a default, shown but never written.

  Its other child settings are `target` (the types a reference field points to: `target:: company`, or `target:: person; company`), `valid` (a check, `=expr`; a failure is an error), `options` (the values the field is meant to hold; another value is a warning, M46) and `claims` (below).
- **Claimed tags (M47).** `claims:: #bug #feature` on a field definition turns those tags into values of the field on nodes of the type: with `issue type::` claiming `#bug` on `+issue`, `Crash in login #bug +issue` has `issue type:: bug` and no tag `bug`. `claims:: options` claims each option by its slug; `claims:: target` claims the target types' nodes by slug or ID, so `#acme` on a task can refer to `ACME +project`. On other nodes the tag stays a tag. In `Ord.workspace`:
  ```
  +issue
  	fields::
  		issue type::
  			options:: bug; feature
  			claims:: options
  ```
- **Value types are never declared.** They are inferred from the values.
- **Reserved fields (M11).** `label`, `type`, `id`, `state`, `tag`, `link`, `formula`, `url`, `parent` and `children`. `label`, `id` and `state` hold one value each; two is an error (M10). A type may compute `label` and give `id` an auto rule, but can't redefine the others. So `type::` always means the node's type: a field of your own needs another name, such as `issue type`. Every other field can hold several values, and values written in several forms (inline, trigger, field line) merge.
- **IDs (M20).** An ID is a name, unique in the workspace, matched ignoring letter case. Prefer short, readable IDs (`ruukki`, `i42`, `anna`). Nodes only need an ID when something refers to them by ID.
- **References (M21 to M24).** These are references: links (`[[…]]`), sigils, plain values of the `link` field, plain values of a reference field (one with `target`, or named after a type that binds a sigil, so `person:: anna` works like `@anna`), claimed tags with `claims:: target`, and CSV `parent`/`children` cells. Plain values of any other field are text, even when they name a node.
- **Resolving (M22, M23).** Text that could be either matches an ID first, then a label. Labels match ignoring case and surrounding spaces, with or without their tags. A label that matches no node, or several, doesn't resolve (warnings M23.1, M23.2): reference by ID when labels are not unique. `[[Label^id]]` names both; the ID wins and the label is checked (M22.2 when it no longer matches). `[[^id]]` is ID only and `[["Label"]]` label only.
- **States (M26 to M31).** The four built-in states are `new`, `in-progress`, `waiting` and `done`. A type's `state` setting adds custom states, each `name [marker] > base`, with `|` between them; the marker and base are optional. A node is done when its base is `done`.
- **Ownership (M13 to M16).** A node's owner is the node it is indented under. A CSV row can be placed under a node with a `parent` cell. `children` are the owned nodes, in order. Ownership never loops.
- **Journal nodes.** Day nodes are ordinary nodes found by ID, not by place: `Monday, 12th ^journal-2026-10-12` under `October, 2026 ^journal-2026-10`, by default in `journal-2026.txt` at the workspace root. With `journal:: month` in `Ord.workspace`, days go under weeks (`Week 42, 2026 ^journal-2026-W42`) in one file per month, `journal-2026-10.txt`. See [references/recipes.md](references/recipes.md).
- **Expansions are not syntax.** `~today`, `~tomorrow`, `~next-monday`, `~uuid` are typing aids that an editor replaces as they are typed. In a file, `~today` is plain text. Write the actual value (`due:: 2026-10-23`), or a formula when it should keep moving.

## Writing and updating

**Edit, don't rewrite (C41).** Change only the lines the change needs. Every other line, blank lines and odd spacing included, stays byte for byte as it was. Never reformat a file the user didn't ask to format.

**Place lines where a writer would (C44, C48).**
- Indent a new line like a sibling next to it. Without one, use the parent's indent plus one step: a tab, or the file's space step if it is indented only with spaces.
- A new field goes after the node's last field (and that field's child lines), or right after the node line.
- A new child node goes after the node's last child and its child lines.
- Keep the file's line endings, BOM and final newline. A new file uses `\n`, ends with a newline and has no BOM.

**Write node lines in the fixed order (L4):** list marker, state, label (tags included), then inline fields, types and the ID.
```
- [ ] Call Anna about the invoice #urgent [due:: 2026-10-20] +task
```
Tags, links, URLs, sigils and formulas stay where they read naturally in the label. Prefer `+task` over `[type:: task]`, `[x]` over `[state:: done]`, `#x` over `[tag:: x]` and `^id` over `[id:: x]`. A tag is part of the label, so adding or removing one changes the label. A `?? query` line is written as it is: nothing on it moves.

**Field lines (C42, C43):** `key:: value`, one space after `::`, items joined with `; `. A field with no value is `key::`. A node with an empty label is written `""`.

**Quote only when needed (C26, C27).** Quote a value or item with `"…"` when it is empty but must be kept, starts or ends with whitespace, starts with `"` or a backtick, contains a backtick, contains `;` (except inside a formula's parentheses), contains a newline or other control character, or is a number, date or boolean that must stay text. Quote a key that contains `::` or `[`, or ends with `:`. Quote a label with a `::` outside brackets, which would make it a field. Everything else is written bare.

**Choosing the shape:**
- **Field or prose.** Use fields for data points, attributes you would filter or compare on, references, and other structured information that is repeated on several nodes: a date, an owner, a status, an amount, a project. Notes, comments and details are added as plain child lines under the node: under `Meeting`, a child line `Ask about the budget` rather than `note:: Ask about the budget`.
- **Inline or field line.** Short values can go inline (`[due:: 2026-10-20]`). Long values and several items read better as field lines. Writing both on one node merges them.
- **Types or tags.** A type (`+task`, read "is a task") says what a node is and brings fields; a tag (`#urgent`) is a loose label in the text. Don't use `+urgent` for a tag. Use a nested tag (`#client/ruukki`) when tags form a family.
- **Define types when they repeat.** When several nodes carry the same fields, define a type (in `Ord.workspace` with `+name`, or with `[defines:: name]` anywhere) and give it to them. Don't invent a type for a single node.
- **References.** Use a link or a reference field, not a copy of the other node's text. Reference by label when it is unique; give the target an ID (`^ruukki`) and reference that when the label isn't unique or may change.
- **No IDs by default.** Don't add `^id` to new nodes. Add one only when it is needed: a reference by label would not resolve (the label isn't unique or is likely to change), or a tool must address the node by ID. Journal nodes (days, weeks, months) are the exception: they always get their `^journal-…` ID.
- **Lists.** List markers are optional decoration. Keep whatever the file already uses.
- **Long text.** Paragraphs are child lines, one per paragraph. Code, tables and anything with its own syntax go in a fenced block.

**Never write computed results into files.** Computed fields, search results and inline formula results are shown by tools, not stored. The exceptions are a computed `label`, which an editor writes into the node line, and `auto` values, which are written once. A `key:: =expr` field on an ordinary node is an error (M39): formulas belong on type definitions.

**Common updates:**
- **Complete a task.** Change `[ ]` to `[x]`. To add a checkbox, put `[ ] ` after any list marker.
- **Set a custom state.** Use its marker (`[r]`) when it has one, else a `state:: review` field line. Never write two states on one node.
- **Archive, never delete,** when the user means "remove from views": add the tag `#archived`. Searches skip archived nodes unless they name `#archived`.
- **Move a node.** Move its whole subtree, its child lines included, and re-indent it to its new depth.
- **Rename a node.** References by ID keep working. References by label (`[[Old name]]`, plain values of reference fields, sigils, claimed tags) must be updated too. Adding or removing a tag doesn't break them. Search the workspace for them.
- **Add an ID** (only when needed, see "No IDs by default"). Pick a name that isn't used yet and add `^name` at the end of the node line. A node whose label is quoted or a block gets an `id::` field line instead.
- **Rename an ID.** Update every `^id`, `[[id]]`, `[[Label^id]]`, sigil and reference-field value that uses it.
- **Change a type's fields.** Edit the definition only. Nodes keep their values.
- **Add to today.** Find the day node by its ID (`^journal-2026-10-22`) and add the line under it. Create the day node (and its month) if it is missing, in date order.

## Formulas in brief

A formula is a JSONata 2.x expression written `=(…)` (M41, L12). Always wrap it in parentheses: `=$sum(x)` is text, `=($sum(x))` a formula. `$` is the current node, so bare names are its fields. Dates are ISO text: compare with `<`, shift with `$date(due, 7)`, count with `$days(a, b)`, never `due + 7`.

```
Invoice [defines:: invoice]
	fields::
		client::
			target:: company
		net:: =($sum(children.amount))
		gross:: =(net * 1.25)
		late:: =($exists(due) and due < $today() and state != "done")
		code:: auto "INV-" & $seq(3)
		vat::
			valid:: =($value in [0, 0.12, 0.25])
```

Formulas go on type definitions (computed fields, `auto`, `label`, `valid`), inline in a label as output only, and in searches. Full rules, functions and examples: [references/formulas.md](references/formulas.md).

## Searches in brief

A node with a `search` field is a saved search (M60). A query looks like the node lines it matches: `+task`, `#urgent` (also matching nested tags like `#urgent/today`), `[ ]`, `@anna`, `[[Ruukki AB]]`, `[due:: 2026-10-10]`, `=(late)`, plain words. Space is and, `|` or, `!` not, parentheses group.

```
Open tasks
	search:: +task ![x]
?? [ ] +task @anna
Late for Anna
	view:: table
	sort:: due asc
	search::
		+task
		@anna
		=(late)
```

Views, columns, footers and the rest: [references/queries.md](references/queries.md).

## Before you finish

- Every new field line has `::` followed by a space, every inline field is in brackets (`[due:: 2026-10-10]`), and no prose has a bare `::`.
- Indentation matches the file's (tabs or spaces), and each new line sits under the right parent.
- Node lines keep the fixed order: state, label with its tags, inline fields, types, ID.
- Types are `+name`, tags `#name`; no old-style `#task` or `+urgent` slipped in, and no field of your own is called `type`.
- New references resolve: the label is unique, or you used an ID. New IDs are unused.
- Sigils are used only when a type binds them.
- No formula sits on an ordinary node's field line, and no computed result was written as a value.
- Formulas are `=(…)` JSONata with `$` functions, `$value` in checks, and `$date`/`$days` for date arithmetic.
- No `~today` or other expansion was written into a file.
- Lines you didn't need to change are unchanged.

## Tools (when available)

The Ordlang CLI (`ord`, from the Ordlang repo; `npm run ord --` there) checks your work:
- `ord index <dir>` lists types, fields, inferred types and diagnostics. Run it after editing; see [references/diagnostics.md](references/diagnostics.md).
- `ord query '<query>' <dir>` runs a query (`--count`, `--json`); `ord query --search <id|label> <dir>` runs a saved one.
- `ord eval --node <id|label> '<expr>' <dir>` evaluates a JSONata expression on a node, written bare or as `=(…)`.
- `ord graph --today <date> <dir>` shows owners, types, IDs, states and resolved references.
- `ord fmt --labels <file>` prints a file in canonical form; `ord dump --labels <file>` shows how it reads.
- `ord html <files>` writes HTML pages.
- `ord migrate --type-field "<name>" <dir>` moves a workspace to 0.5.0 (swaps `#`/`+`, renames your own `type::` fields); it is a dry run until `--write`.

In VS Code, the Ord extension shows diagnostics, computed values, search counts and Format Document. Through the pen MCP server, Ord files are read with `read_md` and edited with `commit_edits`, with the same rules as above.
