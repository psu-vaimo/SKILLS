# Ord diagnostics

Every file reads; problems are diagnostics with a code, a severity and a position (C35 to C37). A code is the rule that gives it, so look it up in the Spec (C, L), Semantics (M) or CSV mapping (V). Codes starting with `ord/` belong to the Ordlang implementation. Run `ord index <dir>` after editing: it prints `file:line:col: severity [code] message`.

Fix every error you caused. Fix warnings you caused unless the user wants the text as written.

## Syntax (Spec)

| Code | Means | Usual fix |
|---|---|---|
| `C3.1`, `C3.2` | An odd whitespace character (NBSP, U+3000) starts a line or touches `::` | Replace it with a space or tab |
| `C22` | `\` in `"…"` not followed by an escape | Write `\\`, or use backticks |
| `C29` | A block is never closed | Add the closing fence, as long as the opening one |
| `C49` | Bytes that aren't UTF-8 | Re-save the file as UTF-8 |
| `L8` | Two `^id` on one node line | Keep one |
| `L10` | `[[` without `]]` | Close the link, or write `\[[` |
| `L11` | A state marker like `[r]` that no type defines | Use a built-in marker, or define the custom state on the type |
| `L12` | A formula's `(` is never closed | Balance the parentheses |
| `L26` | A date, week or month out of range: `2026-02-30` | Fix the date, or quote it to keep it text |

## Workspace (Semantics)

| Code | Means | Usual fix |
|---|---|---|
| `M10` | A second `label`, `id` or `state` on one node | Remove one, e.g. a `state::` line under a `[x]` node |
| `M14.1`, `M14.2` | A CSV `parent`/`children` cell names a node owned by indentation, or the two disagree | Point at a top-level node, or make the cells agree |
| `M15` | An ownership loop through `parent`/`children` cells | Break the loop |
| `M17.1`, `M17.2` | A `defines` value isn't a name, or a type is defined twice | Rename, or merge the definitions |
| `M19.1`, `M19.2` | A `sigil` that can't be one (letter, digit, `#`, `^`, `+` …), or bound twice | Pick another character |
| `M20.1` | Two nodes share an ID | Rename one ID and its references |
| `M20.3` | An ID isn't a name (`^12`) | Start it with a letter |
| `M22.1` | A reference's ID matches no node | Fix the ID, or add it to the intended node |
| `M22.2` | `[[Label^id]]` whose label no longer matches | Update the label in the link |
| `M22.3` | Text that is one node's ID and another's label; the ID wins | Use `[[^id]]` or `[["Label"]]` to say which |
| `M23.1` | A label matches no node (of the target types), with or without its tags | Fix the spelling, create the node, or reference by ID |
| `M23.2` | A label matches several nodes | Reference by ID |
| `M26` | A state that is neither built in nor defined by the node's types | Use a defined state or define it |
| `M27.1`, `M28.1`, `M28.2` | A malformed custom state, or a marker built in or already used | Fix the type's `state` setting |
| `M39` | `key:: =(…)` on an ordinary node | Move the formula to the type's `fields::`, or put an inline `=(…)` in the label |
| `M40` | Error: a value fails its field's `valid` check | Fix the value (it is kept as written) |
| `M46` | A value is none of the field's `options` | Use an option, or add it to `options` |
| `M44.1`, `M44.2` | A computed field is in, or depends on, a cycle | Break the cycle in the type formulas |
| `M44.3` | A formula fails, e.g. a generator outside `auto` | Fix the formula; check with `ord eval` |

## CSV (CSV mapping)

| Code | Means |
|---|---|
| `V5.1` to `V5.3` | A stray `"`, text after a quoted cell, or an unclosed quoted cell |
| `V11.1`, `V11.2` | A row with fewer or more cells than the header |
| `V11.3`, `V11.4` | A second `label` column, or a column without a name |

## Implementation (`ord/`)

| Code | Means | Usual fix |
|---|---|---|
| `ord/undefined-type` | A hint: a type with no definition | Fine to leave; define it when it gets fields. If a tag was meant, write `#name` |
| `ord/sigil-type` | `@x` resolves to a node that isn't of the sigil's type | Point at the right node, or give it the type |
| `ord/outlier` | A value unlike the field's other values (text among dates) | Fix the value, or quote it if it is meant as text |
| `ord/computed-value` | A value written for a field the type computes; it is ignored | Remove the value |
| `ord/formula-conflict` | Two types of one node compute a field differently | Make the definitions agree, or rename one field |
| `ord/missing-file` | A path in a label points at no file | Fix the path |
| `ord/machine-path` | An absolute path that only works on one machine | Use a path relative to the file |
| `ord/results-*` | A results document can't be written back (conflict, changed columns, duplicate ID) | Reopen the results from the search |

## Mistakes that give no diagnostic

These read fine but mean something else. Check for them yourself:

- `due: 2026-10-10` (one colon) is a node, not a field.
- `Call note::two words` or `Call note:: two words` (an inline field without brackets) makes the whole line a field with the key `Call note`. Write `Call [note:: two words]`.
- `Use std::vector` in prose is a field line too; put the code in backticks: ``Use `std::vector` ``.
- `=$sum(x)` is text; write `=($sum(x))`.
- `@anna` without a type that binds `@` is text.
- `+urgent` makes a type; a tag is `#urgent`. `#task` is a tag; a type is `+task` (the reverse of Ord before 0.5.0).
- `type:: bug` as a field of your own sets the node's type; name the field something else, such as `issue type`.
- `#client.` at the end of a sentence is the tag `client` and a full stop; `#123` and `C#` are not tags.
- `• item` is a node labelled `• item`; list markers are `-`, `*`, `+`, `1.`.
- `~today` in a file is text, not a date.
- `days-left` in a formula is `days - left`; write `` `days-left` ``.
