# Ord queries and search nodes

Rules: Semantics M60 to M64. Informative guide: `Semantics/Queries and Views`.

## Search nodes

A node with a `search` field is a saved search (M60). Its other fields configure how it is shown. Results are never written into the file.

Three ways to write one:

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

- **Single line.** The whole query is the value of `search`.
- **Multi-line.** `search::` with one condition per child line. Each line is put in parentheses and the lines are joined with and, so a line may hold `|` freely: `#red | #blue`.
- **Inline (L28).** `?? query` on its own line, after any list marker, is a search node with an empty label. Nothing after `??` is read as a form, so the line gets no type, tags or ID. Good for quick searches in a journal day. View settings go on child lines as usual. Don't also add `search::` lines under it: they combine with and, but it isn't recommended. `??x` and `\??` are text. A search without a label is named by its query, e.g. in its results document.

Editors never turn a `search::` line into `??` or the reverse, so keep the form the file uses.

## Query terms (M61, M62)

A query looks like the node lines it matches.

| Term | Matches nodes |
|---|---|
| `+task` | of that type |
| `#urgent` | with that tag, or a tag nested under it: `#project` matches `#project/apollo` |
| `#project/apollo` | with that nested tag (or one nested under it) |
| `[ ]`, `[-]`, `[?]`, `[x]` | in that built-in state, or with that base: `[x]` also matches custom states based on done, `[-]` a `review` state based on in-progress |
| `[r]` | in the custom state whose marker is `r` |
| `@anna` | with a field referring to that node (needs a type that binds `@`) |
| `[[Ruukki AB]]`, `[[ruukki]]` | with a field referring to that node, by label or ID |
| `[key:: value]` | with a `key` value equal to the text, ignoring case: `[client:: ruukki]`, `[due:: 2026-10-10]`, `[client:: Ruukki AB]` |
| `=(expr)` | where the JSONata formula is true for the node |
| `word`, `"two words"` | whose label contains it, ignoring case |

- **Combining.** A space means and, `|` means or, parentheses group, and `!` negates a term or group: `+task (#red | #blue) ![x] !@erik`, `!(#urgent | [r]) +task`.
- **Archived nodes (M63).** Nodes tagged `archived` are left out unless the query names `#archived`.
- **Filters are formulas.** There are no bracket filters or comparison operators in the query itself: write `=(due < $today() and hours > 2)`. Formulas in queries may use `$today()`, `$date("this-week")` and the rest, but not generators (`$uuid()` and friends). See formulas.md.
- **Hyphenated keys in filters** need backticks: ``=(`days-left` < 3)``.

Not yet available: structural operators such as `child-of()` and `has-parent()`.

## View settings (M64)

| Setting | Value |
|---|---|
| `view` | `table`, `list`, `board` or `calendar` |
| `columns` | one child field line per column (below) |
| `sort` | a field and `asc` or `desc`: `sort:: due asc` |
| `group` | a field to group by: `group:: project`; a board groups by it, e.g. `state` |
| `footer` | `=expr` over the visible rows, also shown as group subtotals: `footer:: =($sum(hours))` |
| `computed` | `csv` (the default, also for an empty `computed::`): the tool writes a read-only fenced CSV copy of the results under the search |

### Columns

`columns::` holds one field line per column:

```
Hours this month
	view:: table
	sort:: date desc
	search:: +timelog =(date in $date("this-month"))
	columns::
		label::
		date::
			format:: short
		client::
		hours::
		days-ago:: =($days(date, $today()))
			header:: Days ago
			width:: 8
	footer:: =($sum(hours))
```

- `key::` shows a field. `key:: =expr` is a template column, computed per row, output only.
- A column's child lines are its settings: `header`, `width`, `format`.
- Headers come from the key (`days-ago` shows as Days ago) unless `header` is set.
- Without `columns`, a table shows `label`, the fields of the matched types, and the other fields present on the matching nodes.

## How tools use searches

- In VS Code, a CodeLens on each search shows its result count and opens an editable results document (a CSV in `.ord/results/`). Edits there write back to the source nodes; deleting a row archives the node; new rows go under today's journal node and get the types and tags the query requires (not those inside or-groups).
- `ord query '<query>' <dir>` runs a query; `--count` prints the number of matches, `--json` the matches as JSON.
- `ord query --search <id|label> <dir>` runs a saved search by its ID or label. A `??` search is named by its query text.

## Writing searches well

- Put the search where the user will look for it: a project node, the workspace file, or today's journal day for a quick `??`.
- Prefer types, tags and states over word matches; words only search labels.
- Use `![x]` for "not done": it also covers custom states based on done.
- When a filter repeats, move it to a computed field on the type (`late:: =(…)`) and query `=(late)`.
- Don't write results, counts or dates computed from the query into the file.
