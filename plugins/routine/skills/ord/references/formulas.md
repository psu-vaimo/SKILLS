# Ord formulas (JSONata)

Rules: Semantics M36 to M45. Informative guide: `Semantics/Formulas`.

A formula is a JSONata 2.x expression written as `=(…)` (M41, Spec L12). Always wrap it in parentheses: `=` must be followed by a letter, `!` or `(`, so `=$sum(x)` is text and `=($sum(x))` a formula. Inside the parentheses, `;` doesn't split a field's items (C15), so `=($a := 2; $a * 3)` is one value.

## Where formulas go

| Where | Written | Notes |
|---|---|---|
| Computed field, on a type | `total:: =($sum(children.amount))` under `fields::` | Shown by tools, never written into nodes |
| Auto value, on a type | `id:: auto $slug(label)`, `code:: auto "T-" & $seq(3)` | Written once, when the node gets the type and the field is empty |
| Computed label, on a type | `label:: =(first & " " & last)` | Written into the node line by editors, after which the line's tags stay (M38); don't edit it by hand |
| Check, under a field definition | `valid:: =($value in ["low", "high"])` | A result that isn't true is the error M40; the value stays |
| Inline, in a label | `Total =(a + b)` | Output only |
| Search filter, template column, footer | `=(due < $today())` | Output only, see queries.md |

Not on ordinary nodes: `x:: =(1 + 1)` on a node that isn't a type definition is the error M39 and isn't evaluated. Move the formula to the type's `fields::`, or write an inline `=(…)` in the label.

## The data model a formula sees

- `$` is the current node, so bare names are its fields: `due`, `hours`, `client`.
- `$root` is the graph root; its `children` are each file's root node.
- A field with one value is that value; several values are an array.
- Numbers are numbers. Booleans are booleans. Dates, datetimes, weeks and months are ISO text, so `due < $today()` compares correctly.
- System fields: `label` (with its tags), `id`, `type` (an array of types), `state`, `tag` (the tags, nested ones as `project/apollo`), `parent` and `children` (child nodes, not field items).
- A reference field's value is the node it refers to: `client.label`, `owner.email`.
- A field with field children is an object: with `contact::` holding `primary:: anna` on a child line, `contact.primary` is `anna`. Steps continue through references only when the field is a reference field, so `contact.primary.email` reaches Anna's email only if `primary` has `target:: person` or is named after a sigil's type.
- Keys that aren't plain JSONata names go in backticks: `` `Project lead`.email ``. That includes every key with a `-`: `days-left` reads as `days - left`, so write `` `days-left` ``. Prefer keys without `-` for fields that other formulas use.
- A field with only a default (a plain `value`) is empty to formulas; defaults are never written.
- Everything else is JSONata: mapping `children.(price * qty)`, filtering `children[state != "done"]`, `&` for text, `+` for numbers only, `and`, `or`, `$not()`, `? :`, `in`, array literals `[…]`, `$x := …` bindings, and `$`-functions.

## Ord's functions (M42, M43)

| Function | Gives |
|---|---|
| `$node(text)` | The node with that ID, else that label, like a link. `$node("^i42")` matches the ID only. `$node("i42").gross` |
| `$today()` | Today's date, local: `2026-10-22` |
| `$now()` | The date and time, local: `2026-10-22T14:30` |
| `$date(text, days?)` | A date from ISO text or a date name, shifted by whole days: `$date(due, 7)`, `$date("tomorrow")`, `$date("next-monday")` |
| `$date(period)` | A period name gives all its dates: `due in $date("this-week")` |
| `$days(a, b?)` | Whole days from a to b, or from today to a: `$days(due)` |
| `$format(x, picture)` | A number or date with a JSONata picture: `$format(1234.5, "#,##0.00")` gives `1,234.50` |
| `$slug(text)` | A slug (M45): lowercase, accents removed, other runs to `-`, leading digits dropped. `"Åsa Öberg!"` gives `asa-oberg` |
| `$first(x)`, `$last(x)` | The first or last value |
| `$seq(n)` | Auto only: the type's next number, padded to n digits |
| `$uuid()`, `$id()`, `$sid()` | Auto only: a UUID, six random characters, the label's slug plus a short random suffix (`buy-milk-y7k`) |

Date names: `today`, `tomorrow`, `yesterday`, `monday` to `sunday` (the next one, today included), `this-monday`, `next-monday`, `last-monday` and so on, and the periods `this-week`, `next-week`, `last-week`, and the same for `month` and `year`. Weeks start on Monday (ISO 8601).

JSONata's built-ins work as usual: text (`$uppercase`, `$lowercase`, `$substring`, `$contains`, `$split`, `$join`, `$replace`, `$trim`, `$pad`, `$match`, `$length`, `$string`), numbers (`$sum`, `$count`, `$average`, `$min`, `$max`, `$round`, `$floor`, `$ceil`, `$abs`, `$number`, `$formatNumber`) and lists (`$exists`, `$distinct`, `$sort`, `$reverse`, `$map`, `$filter`, `$reduce`).

## Rules

- **Date arithmetic.** Dates are text, so `due + 7` doesn't work. Use `$date(due, 7)` and `$days(start, end)`.
- **Purity.** Formulas are pure. Only `$today()`, `$now()` and `$date()` with a date name follow the clock; their dependents recalculate at day change (`$now()` on a timer).
- **Generators only in `auto`.** `$seq`, `$uuid`, `$id` and `$sid` would change on every evaluation, so they are errors in live formulas, queries and search settings.
- **No `~` in formulas.** Use `$date("tomorrow")`, not `~tomorrow`.
- **Errors and cycles (M44).** A failing formula (M44.3), a cycle (M44.1) or a dependency on a cycle (M44.2) leaves the field empty with a diagnostic. Cycles are per node, so `hours:: =($sum(children.hours))` on a tree is fine.
- **`valid` checks.** `$value` is the field's value, a list when it has several; `$values` is always all of them. `=($count($values) = 1)` checks a single value.

## Examples

All checked against the implementation.

```
Invoice [defines:: invoice]
	fields::
		client::
			target:: company
		net:: =($sum(children.amount))
		gross:: =(net * 1.25)
		code:: auto "INV-" & $seq(3)
Task [defines:: task]
	fields::
		due::
		late:: =($exists(due) and due < $today() and state != "done")
		days-left:: =($days(due))
		this-week:: =(due in $date("this-week"))
		priority::
			valid:: =($value in ["low", "medium", "high"])
Plant [defines:: plant]
	fields::
		watered::
		every::
		next:: =($date(watered, every))
		thirsty:: =(next <= $today())
Person [defines:: person]
	sigil:: @
	fields::
		id:: auto $slug(label)
		label:: =(first & " " & last)
		initials:: =($uppercase($substring(first, 0, 1) & $substring(last, 0, 1)))
```

More one-liners:

- `=($count(children[state = "done"]))`: done children
- `=($node("i42").gross)`: a field on another node
- `=("task" in type)`: has the type (`type` is a list, so use `in`, not `=`)
- ``=(`days-left` < 3)``: a hyphenated field, in backticks
- `=($count(children[("task" in type) and state != "done"]))`: open tasks under this node
- `=(parent.label)`: the owner's label
- `=($node("journal-" & $today()))`: today's journal node
- `=($sum(children.(price * qty)))`: a sum of products
- `=($format(net, "#,##0.00") & " SEK")`: formatted text

## Checking a formula

`ord eval --node <id|label> '<expr>' <dir>` prints the result on that node; the expression can be bare or `=(…)`. `ord graph --today 2026-10-22 <dir>` and `ord index <dir>` report formula diagnostics.
