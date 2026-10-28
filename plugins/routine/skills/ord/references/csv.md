# CSV files in an Ord workspace

Rules: `Spec/CSV mapping` (V1 to V15), Semantics M14 to M16. Informative guide: `Semantics/Storage`.

Inside a workspace (a folder with `Ord.workspace`), every `.csv` file is part of the graph: each row after the header is a node, and each column a field. Use CSV for many rows of the same shape (time logs, line items, contacts); use `.ord` for prose and nesting.

```
id,type,label,parent,date,hours,tag
l1,timelog,Design work,i42,2026-10-20,3.5,
,timelog,Review,i42,2026-10-21,1,billable; urgent
```

## Reading

- **Format.** UTF-8, `,` between cells, `.` as the decimal point, RFC 4180 quoting (`"…"` with `""` for a quote). The first row is the header.
- **`label` column.** Its cell is the node's label, taken literally (V8): `Review +task #urgent` in a label cell is that text, with no type and no tag.
- **System columns.** `id`, `type`, `state`, `tag`, `parent` and `children` are ordinary fields with their usual meaning. Types come only from the `type` column, tags only from the `tag` column. All columns are optional.
- **Other cells** are read like a field value in a text file: split into items at `;`, with value forms (numbers, dates, booleans, weeks, months). Triggers, links, sigils, URLs and formulas in cells are text (V10), so `@anna` in a cell is just text; use a reference column instead.
- **Quotes inside a cell are backticks**, since `"` is CSV's own quote: `` `x; y` `` is one item.
- **References.** `parent`, `children` and reference columns (a field with `target`, or named after a sigil's type) hold IDs, without brackets. A label still resolves, but write IDs.
- **Hierarchy (M14 to M16).** CSV is flat. A `parent` cell places the row under that node; a `children` cell lists the rows a node owns, in order. Only a file's top-level nodes can be placed this way. `parent` and `children` must not contradict each other or loop.
- **Missing cells** are empty; extra cells are dropped, with a warning.

## Writing and editing

- **Edit, don't rewrite.** Change only the rows and cells the change needs; keep the column order, unknown columns, line endings and BOM.
- **New rows** go at the end, with a cell for every column (empty where there is no value).
- **New columns** go at the end of the header, with an empty cell in every existing row.
- **Several values** in one cell are joined with `; `, never split into columns or rows.
- **IDs are lazy.** A row needs an `id` only when something refers to it. Give it one by filling its cell (adding an `id` column if needed, empty for other rows).
- **Quoting.** Quote a cell in `"…"` (doubling inner quotes) when it holds `,`, `"` or a line break. Use backticks around an item that holds `;` but should stay one item.
- **Computed fields** are never columns.
- **Delete means archive** when the user means "remove from views": add `archived` to the row's `tag` cell.

## Converting

- **Text to CSV** works only for nodes without child nodes (or after turning them into `parent` references). The node line's forms become columns: `+task` fills `type`, `^t9x1` fills `id`, `[x]` fills `state` (`done`), `#urgent` fills `tag` (and leaves the label, since a label cell is literal), `%apollo` fills `project`, `[due:: 2026-10-10]` fills `due`. The `label` cell keeps the rest of the label. References become IDs.
- **CSV to text**: a row becomes a node line with field lines, or with its forms back on the line: `[x] Review +timelog ^l2` plus `date:: 2026-10-21`; a `tag` cell `billable` can go back into the label as `#billable`.
- `ord to-csv <file>` writes a flat Ord file as CSV; `ord dump --csv <file>` shows how a CSV file reads.

## Results blocks

A search with `computed::` gets a read-only fenced CSV block written by the tool under it. Don't edit it by hand, and don't create one yourself; it is regenerated. Reference columns there come in pairs: `client` (the label) and `client.id` (the ID).
