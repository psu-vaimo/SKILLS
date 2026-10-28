#!/usr/bin/env python3
"""Profile a product-data export: per-field fill, null-equivalents, distinctness, shape.

Reads CSV/TSV/XLSX/XML with no third-party dependencies. Streams row by row so a
million-article export does not have to fit in memory.

    python3 profile_export.py SOURCE_FILE DESTINATION_FILE ... --out DIR [options]\n\nArgument order matters: with --key and two or more files, the first is treated as the\nsource of record and the second as the destination, for the FLOW comparison.

Options:
    --key COLUMN          identifier column, for duplicate detection
    --segment COLUMN      report fill rates split by this column (e.g. lifecycle status)
    --scope COLUMN=VALUE  restrict the primary denominator to matching rows
    --multi-delim STR     multi-value separator inside a cell (e.g. ';;;'); repeat for several
    --null-equiv STR      extra value to count as empty, e.g. a system placeholder such as
                          'MISSING-MISSING'; repeat for several. Compared case-folded
    --null-pattern REGEX  count values matching REGEX as empty, for placeholders that vary,
                          e.g. --null-pattern='-MISSING$' (use '=' when the pattern starts
                          with '-'); repeat for several
    --sample N            values kept per field for examples (default 20)
    --max-rows N          stop after N rows (for a quick look at a huge file)
"""

import argparse
import csv
import json
import os
import re
import sys
import zipfile

# Exports carry cells far beyond csv's 131,072-character default (relation lists, long copy).
csv.field_size_limit(min(sys.maxsize, 2**31 - 1))
from collections import Counter, defaultdict
from xml.etree import ElementTree

# Values that occupy a field without informing it. Compared case-folded and stripped.
NULL_EQUIVALENTS = {
    "", "-", "--", "---", ".", "..", "?", "??", "n/a", "na", "n.a.", "null", "nil",
    "none", "nan", "tbd", "tba", "todo", "xxx", "xx", "x", "0000", "unknown",
    "ej angivet", "saknas", "ingen", "inget", "okänd", "ikke angitt", "ei tiedossa",
    "not applicable", "not set", "no value", "empty", "blank", "#n/a", "#value!",
    "#ref!", "1900-01-01", "0000-00-00",
}

# Filled from --null-pattern: placeholders that vary per record ("5067319-MISSING").
NULL_PATTERNS = []

CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
INVISIBLE = re.compile(r"[​-‏‪-‮﻿­]")
HTML_TAG = re.compile(r"<[a-zA-Z/][^>]*>")
URL = re.compile(r"^https?://", re.I)
INT = re.compile(r"^[+-]?\d+$")
DECIMAL_DOT = re.compile(r"^[+-]?\d+\.\d+$")
DECIMAL_COMMA = re.compile(r"^[+-]?\d+,\d+$")
DATE_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}")
DATE_OTHER = re.compile(r"^\d{1,2}[/.]\d{1,2}[/.]\d{2,4}$")
BOOLISH = {"true", "false", "yes", "no", "ja", "nej", "y", "n", "1", "0", "x"}
# A number carrying its own unit: "10 mm", "84 kr", "5st". The unit belongs in metadata,
# not in the value — it blocks arithmetic, conversion and range validation.
UNIT_IN_VALUE = re.compile(r"^[+-]?[\d\s.,]+\s*[a-zA-ZåäöÅÄÖ%²³°/]{1,6}$")

# Attribute names differing only by a unit or language suffix belong to one concept.
# UNIT_SUFFIX is the strict form: multi-letter units may be glued to the name ("Breddmm",
# "Viktkg"), single letters, short words and "dm" need a separator ("Breddm" is bredd + m). LOOSE_UNITS are also tried glued
# ("DIAMETERIN", "BREDDM") — real in some exports, but on their own they cut ordinary names
# ("Material" -> "Materia"), so a loose strip is only trusted when the base it leaves matches
# the strict base of another field. See concept_clusters().
UNIT_SUFFIX = re.compile(
    r"(?:[_\- ](?:m|g|l|t|st|in|inch|pcs)"
    r"|[_\- ](?:dm)|[_\- ]?(?:mm|cm|km|m2|m3|m²|m³|kg|ml|cl|frp|pall|%))$", re.I)
LOOSE_UNITS = ("mm", "cm", "dm", "km", "m2", "m3", "m²", "m³", "kg", "ml", "cl", "frp", "pall", "%",
               "m", "g", "l", "t", "st", "in", "inch", "pcs")
# Language codes need a separator ("Namn_sv", "Name-en"): glued, they cut ordinary words
# ("Densitet" -> "Densit", "Matomrade" -> "Matomra").
LANG_SUFFIX = re.compile(r"[_\- ](sv|se|en|gb|us|no|nb|da|dk|fi|de|fr|nl|pl|et|lv|lt|ru|ua|es|it)$", re.I)


# ---------------------------------------------------------------- readers

def read_csv(path, max_rows=None):
    fh = open(path, "r", encoding="utf-8-sig", errors="replace", newline="")
    sample = fh.read(64 * 1024)
    fh.seek(0)
    # Sniff the delimiter only. The sniffer also guesses quoting, and it only sees
    # the first 64 KB: a file whose first escaped quote ("") appears after that gets
    # doublequote=False, and then every row containing an escaped quote silently
    # misparses into shifted columns. Quoting is RFC 4180 in every export we read.
    dialect = csv.excel()
    dialect.quotechar = '"'
    dialect.doublequote = True
    dialect.escapechar = None
    dialect.delimiter = "\t" if path.lower().endswith((".tsv", ".tab")) else ","
    try:
        dialect.delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
    except csv.Error:
        pass
    reader = csv.reader(fh, dialect)
    try:
        header = dedupe_header(next(reader))
    except StopIteration:
        fh.close()
        return [], iter(())

    def rows():
        try:
            for i, row in enumerate(reader):
                if max_rows is not None and i >= max_rows:
                    return
                yield row
        finally:
            fh.close()

    return header, rows()


def _xlsx_shared_strings(zf):
    try:
        xml = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    out = []
    for si in ElementTree.fromstring(xml).findall(f"{ns}si"):
        out.append("".join(t.text or "" for t in si.iter(f"{ns}t")))
    return out


def _xlsx_first_sheet_path(zf):
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    rns = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    wb = ElementTree.fromstring(zf.read("xl/workbook.xml"))
    sheets = wb.find(f"{ns}sheets")
    first = sheets[0]
    rid = first.get(f"{rns}id")
    rels = ElementTree.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    for rel in rels:
        if rel.get("Id") == rid:
            target = rel.get("Target")
            return ("xl/" + target.lstrip("/")).replace("xl/xl/", "xl/"), first.get("name")
    return "xl/worksheets/sheet1.xml", first.get("name")


def _col_index(ref):
    letters = "".join(c for c in ref if c.isalpha())
    n = 0
    for c in letters:
        n = n * 26 + (ord(c.upper()) - 64)
    return n - 1


def read_xlsx_stream(path, max_rows=None):
    """Generator wrapper: yields (header, row_iterator)."""
    zf = zipfile.ZipFile(path)
    strings = _xlsx_shared_strings(zf)
    sheet_path, _ = _xlsx_first_sheet_path(zf)
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    fh = zf.open(sheet_path)
    it = ElementTree.iterparse(fh, events=("end",))

    def parse_cells(row_el):
        out = {}
        for c in row_el.findall(f"{ns}c"):
            ref = c.get("r") or ""
            idx = _col_index(ref) if ref else len(out)
            t = c.get("t")
            if t == "inlineStr":
                is_el = c.find(f"{ns}is")
                val = "".join(x.text or "" for x in is_el.iter(f"{ns}t")) if is_el is not None else ""
            else:
                v = c.find(f"{ns}v")
                val = v.text if v is not None and v.text is not None else ""
                if t == "s" and val != "":
                    try:
                        val = strings[int(val)]
                    except (ValueError, IndexError):
                        pass
            out[idx] = val
        return out

    header = None
    for event, el in it:
        if el.tag != f"{ns}row":
            continue
        d = parse_cells(el)
        width = (max(d) + 1) if d else 0
        row = [d.get(i, "") for i in range(width)]
        el.clear()
        header = dedupe_header(row)
        break

    def rows():
        n = 0
        for event, el in it:
            if el.tag != f"{ns}row":
                continue
            d = parse_cells(el)
            width = (max(d) + 1) if d else 0
            row = [d.get(i, "") for i in range(width)]
            el.clear()
            if max_rows is not None and n >= max_rows:
                return
            n += 1
            yield row

    return header or [], rows()


def read_xml(path, max_rows=None):
    """Treat the repeating child element as a record; its children as fields."""
    context = ElementTree.iterparse(path, events=("start", "end"))
    _, root = next(context)
    record_tag = None
    for event, el in context:
        if event == "start" and el is not root and record_tag is None:
            record_tag = el.tag
            break
    if record_tag is None:
        return [], iter(())

    def strip(t):
        return t.split("}", 1)[1] if "}" in t else t

    records = []
    fields = []
    seen = set()
    for event, el in ElementTree.iterparse(path, events=("end",)):
        if el.tag != record_tag:
            continue
        rec = {}
        for child in el:
            name = strip(child.tag)
            text = (child.text or "").strip()
            if len(child):
                text = " ".join((g.text or "").strip() for g in child.iter() if g.text and g.text.strip())
            rec[name] = text
            if name not in seen:
                seen.add(name)
                fields.append(name)
        for k, v in el.attrib.items():
            name = f"@{strip(k)}"
            rec[name] = v
            if name not in seen:
                seen.add(name)
                fields.append(name)
        records.append(rec)
        el.clear()
        if max_rows is not None and len(records) >= max_rows:
            break

    def rows():
        for rec in records:
            yield [rec.get(f, "") for f in fields]

    return fields, rows()


# Comparing values across files means holding the shared columns in memory, keyed by product.
# Past this many products the comparison is dropped rather than exhausting the machine.
KEY_VALUE_CAP = 300000


def collect_headers(paths):
    """Learn each file's fields before the real profiling pass.

    Sampled rather than header-only, because an XML export declares fields per record and one
    record does not reveal the full set.
    """
    out = []
    for p in paths:
        header, _ = open_file(p, max_rows=200)
        out.append(header)
    return out


def dedupe_header(header):
    out, counts = [], Counter()
    for i, h in enumerate(header):
        name = (h or "").strip() or f"column_{i + 1}"
        counts[name] += 1
        out.append(name if counts[name] == 1 else f"{name}__{counts[name]}")
    return out


def open_file(path, max_rows=None):
    low = path.lower()
    if low.endswith((".csv", ".tsv", ".tab", ".txt")):
        return read_csv(path, max_rows)
    if low.endswith((".xlsx", ".xlsm")):
        return read_xlsx_stream(path, max_rows)
    if low.endswith(".xml"):
        return read_xml(path, max_rows)
    raise SystemExit(f"Unsupported file type: {path}")


# ---------------------------------------------------------------- profiling

class FieldStat:
    __slots__ = ("name", "present", "null_equiv", "distinct", "distinct_norm", "lengths_sum",
                 "len_min", "len_max", "types", "flags", "samples", "by_segment",
                 "in_scope_present", "distinct_cap_hit")

    DISTINCT_CAP = 50000

    def __init__(self, name):
        self.name = name
        self.present = 0
        self.in_scope_present = 0
        self.null_equiv = 0
        self.distinct = set()
        self.distinct_norm = set()
        self.distinct_cap_hit = False
        self.lengths_sum = 0
        self.len_min = None
        self.len_max = None
        self.types = Counter()
        self.flags = Counter()
        self.samples = []
        self.by_segment = defaultdict(lambda: [0, 0])  # segment -> [rows, filled]

    def observe(self, raw, segment, in_scope, sample_n):
        v = "" if raw is None else str(raw)
        stripped = v.strip()
        folded = stripped.casefold()

        if segment is not None:
            self.by_segment[segment][0] += 1

        if stripped == "":
            return
        if folded in NULL_EQUIVALENTS or any(p.search(stripped) for p in NULL_PATTERNS):
            if in_scope:
                self.null_equiv += 1
            return

        self.present += 1
        if in_scope:
            self.in_scope_present += 1
        if segment is not None:
            self.by_segment[segment][1] += 1

        n = len(stripped)
        self.lengths_sum += n
        self.len_min = n if self.len_min is None else min(self.len_min, n)
        self.len_max = n if self.len_max is None else max(self.len_max, n)

        # Distinctness shares the fill denominator, so both describe the same population.
        if in_scope and not self.distinct_cap_hit:
            self.distinct.add(stripped)
            self.distinct_norm.add(folded)
            if len(self.distinct) > self.DISTINCT_CAP:
                self.distinct_cap_hit = True

        if len(self.samples) < sample_n:
            self.samples.append(stripped)

        self.types[classify(stripped)] += 1

        if v != stripped:
            self.flags["whitespace_padding"] += 1
        if CONTROL_CHARS.search(v):
            self.flags["control_chars"] += 1
        if INVISIBLE.search(v):
            self.flags["invisible_chars"] += 1
        if HTML_TAG.search(stripped):
            self.flags["html_markup"] += 1
        if UNIT_IN_VALUE.match(stripped):
            self.flags["unit_inside_value"] += 1


def classify(v):
    if INT.match(v):
        return "integer"
    if DECIMAL_DOT.match(v):
        return "decimal_dot"
    if DECIMAL_COMMA.match(v):
        return "decimal_comma"
    if DATE_ISO.match(v):
        return "date_iso"
    if DATE_OTHER.match(v):
        return "date_other"
    if URL.match(v):
        return "url"
    if v.casefold() in BOOLISH:
        return "boolean"
    if HTML_TAG.search(v):
        return "html"
    if len(v) > 200:
        return "long_text"
    return "text"


def profile(path, args, shared_fields=None):
    header, rows = open_file(path, args.max_rows)
    stats = [FieldStat(h) for h in header]
    index = {h: i for i, h in enumerate(header)}

    # Values for fields this file shares with another, kept so FLOW can compare them per product.
    shared_i = ([(i, h) for i, h in enumerate(header) if h.casefold() in shared_fields]
                if shared_fields else [])
    key_values = {}
    key_values_overflowed = False

    key_i = index.get(args.key) if args.key else None
    seg_i = index.get(args.segment) if args.segment else None
    scope_col, scope_val = (args.scope.split("=", 1) if args.scope and "=" in args.scope else (None, None))
    scope_i = index.get(scope_col) if scope_col else None

    total = 0
    in_scope_total = 0
    segment_counts = Counter()
    key_counter = Counter()
    blank_rows = 0

    for row in rows:
        total += 1
        if len(row) < len(header):
            row = row + [""] * (len(header) - len(row))
        if not any(c and str(c).strip() for c in row):
            blank_rows += 1
            continue

        segment = str(row[seg_i]).strip() if seg_i is not None and seg_i < len(row) else None
        if segment is not None:
            segment_counts[segment] += 1

        in_scope = True
        if scope_i is not None:
            in_scope = str(row[scope_i]).strip() == scope_val
        if in_scope:
            in_scope_total += 1

        if key_i is not None and key_i < len(row):
            k = str(row[key_i]).strip()
            # A placeholder is not a key: counting it would report every placeholder row as a
            # duplicate of every other one.
            if k and k.casefold() not in NULL_EQUIVALENTS and not any(p.search(k) for p in NULL_PATTERNS):
                key_counter[k] += 1
                if shared_i and not key_values_overflowed:
                    if len(key_values) >= KEY_VALUE_CAP and k not in key_values:
                        key_values_overflowed = True
                        key_values.clear()
                    else:
                        key_values[k] = {h: str(row[i]).strip()
                                         for i, h in shared_i if i < len(row)}

        for i, st in enumerate(stats):
            val = row[i] if i < len(row) else ""
            if args.multi_delim and val and any(d in str(val) for d in args.multi_delim):
                st.flags["multi_value"] += 1
            st.observe(val, segment, in_scope, args.sample)

    denominator = in_scope_total if scope_i is not None else total
    dupes = {k: c for k, c in key_counter.items() if c > 1}

    fields = []
    for st in stats:
        distinct_n = len(st.distinct) if not st.distinct_cap_hit else f">{FieldStat.DISTINCT_CAP}"
        filled = st.in_scope_present if scope_i is not None else st.present
        fill_pct = round(100.0 * filled / denominator, 1) if denominator else 0.0
        raw_filled = st.present + st.null_equiv
        raw_pct = round(100.0 * raw_filled / (total or 1), 1)
        flags = dict(st.flags)
        # One concept written two ways is a consistency defect, not two values.
        variants = len(st.distinct) - len(st.distinct_norm)
        if variants > 0 and not st.distinct_cap_hit:
            flags["case_or_space_variants"] = variants
        if st.types.get("decimal_dot") and st.types.get("decimal_comma"):
            flags["mixed_decimal_separator"] = min(st.types["decimal_dot"],
                                                   st.types["decimal_comma"])
        if st.types.get("date_iso") and st.types.get("date_other"):
            flags["mixed_date_format"] = min(st.types["date_iso"], st.types["date_other"])

        fields.append({
            "field": st.name,
            "fill_pct_in_scope": fill_pct,
            "fill_pct_raw": raw_pct,
            "filled": filled,
            "null_equivalents": st.null_equiv,
            "distinct": distinct_n,
            "cardinality_ratio": (round(len(st.distinct) / st.present, 3)
                                  if st.present and not st.distinct_cap_hit else None),
            "avg_len": round(st.lengths_sum / st.present, 1) if st.present else 0,
            "min_len": st.len_min,
            "max_len": st.len_max,
            "dominant_type": st.types.most_common(1)[0][0] if st.types else None,
            "type_mix": dict(st.types.most_common(4)),
            "flags": flags,
            "samples": st.samples[:5],
            "by_segment": {k: {"rows": v[0], "filled": v[1],
                               "fill_pct": round(100.0 * v[1] / v[0], 1) if v[0] else 0.0}
                           for k, v in sorted(st.by_segment.items())},
        })

    return {
        "file": os.path.basename(path),
        "path": path,
        "rows": total,
        "blank_rows": blank_rows,
        "columns": len(header),
        "denominator": denominator,
        "scope": f"{scope_col}={scope_val}" if scope_i is not None else "all rows",
        "segment_counts": dict(segment_counts.most_common()),
        "key": args.key,
        "duplicate_keys": len(dupes),
        "duplicate_key_rows": sum(dupes.values()),
        "duplicate_examples": dict(list(sorted(dupes.items(), key=lambda kv: -kv[1]))[:10]),
        "fields": fields,
        "header": header,
        "_keys": set(key_counter),
        "_key_values": key_values,
        "_key_values_overflowed": key_values_overflowed,
    }


# ---------------------------------------------------------------- derived findings

def concept_clusters(header):
    """Group field names that differ only by a unit or language suffix.

    Strict stripping first; then a name the strict rule left alone may join a group through a
    glued short unit, but only a group that already holds a field with a clear unit — so
    `DIAMETERIN` joins `Diametermm`, while `Material` never joins `Materia`. Known limit: two
    fields where neither has a clear unit (`Svangradie` / `Svangradiem`) are not paired, because
    by name alone they look exactly like `Materia` / `Material`. Clusters are candidates for a
    person to judge, never merges.
    """
    def base_of(h, unit_re):
        b = LANG_SUFFIX.sub("", unit_re.sub("", h.strip()))
        return re.sub(r"[_\-\s]+$", "", b).casefold()

    groups = defaultdict(list)
    for h in header:
        b = base_of(h, UNIT_SUFFIX)
        if b:
            groups[b].append(h)
    # Second pass over names the strict rule left on their own. Try every glued unit the
    # unstripped name could end in ("BREDDM" ends in "dm" and "m"; "Volyml" in "ml" and "l")
    # and join a group only if one of its members had a unit stripped by the strict rule, so
    # "Material" never joins a field that happens to be called "Materia".
    no_units = re.compile(r"(?!)")
    unit_bases = {b for b, names in groups.items()
                  if any(base_of(h, no_units) != b for h in names)}
    for b in [k for k, v in groups.items() if len(v) == 1 and k not in unit_bases]:
        if len(groups.get(b, [])) != 1:
            continue
        h = groups[b][0]
        name = base_of(h, no_units)
        for u in LOOSE_UNITS:
            if not name.endswith(u) or len(name) <= len(u):
                continue
            loose = re.sub(r"[_\-\s]+$", "", name[:-len(u)])
            if loose != b and loose in unit_bases and loose in groups:
                groups[loose].append(h)
                del groups[b]
                break
    return {k: v for k, v in groups.items() if len(v) > 1}


def cross_source(profiles):
    """Which fields appear in which sources, and how much the sources overlap."""
    where = defaultdict(set)
    for p in profiles:
        for h in p["header"]:
            where[h.casefold()].add(p["file"])
    shared = {k: sorted(v) for k, v in where.items() if len(v) > 1}
    single = [k for k, v in where.items() if len(v) == 1]
    return {
        "total_distinct_fields": len(where),
        "fields_in_more_than_one_source": len(shared),
        "fields_in_one_source_only": len(single),
        "overlap_pct": round(100.0 * len(shared) / len(where), 1) if where else 0.0,
        "shared_fields": dict(sorted(shared.items())[:200]),
    }


def flow_comparison(source, dest):
    """Directed source→destination comparison. Argument order carries the meaning."""
    s_fields = {h.casefold(): h for h in source["header"]}
    d_fields = {h.casefold(): h for h in dest["header"]}
    shared = sorted(set(s_fields) & set(d_fields))

    s_keys, d_keys = source["_keys"], dest["_keys"]
    both = s_keys & d_keys

    divergence = []
    comparable = source["_key_values"] and dest["_key_values"]
    if comparable:
        for f in shared:
            sh, dh = s_fields[f], d_fields[f]
            differ = same = 0
            example = None
            for k in both:
                sv = source["_key_values"].get(k, {}).get(sh, "")
                dv = dest["_key_values"].get(k, {}).get(dh, "")
                if not sv and not dv:
                    continue
                if sv == dv:
                    same += 1
                else:
                    differ += 1
                    if example is None:
                        example = (k, sv, dv)
            if differ:
                divergence.append({
                    "field": sh, "differ": differ, "same": same,
                    "differ_pct": round(100.0 * differ / (differ + same), 1) if (differ + same) else 0.0,
                    "example": example,
                })
        divergence.sort(key=lambda d: -d["differ"])

    return {
        "source": source["file"],
        "destination": dest["file"],
        "fields_source_only": [s_fields[f] for f in sorted(set(s_fields) - set(d_fields))],
        "fields_destination_only": [d_fields[f] for f in sorted(set(d_fields) - set(s_fields))],
        "fields_shared": [s_fields[f] for f in shared],
        "enrichment_share_pct": (round(100.0 * len(set(d_fields) - set(s_fields)) / len(d_fields), 1)
                                 if d_fields else 0.0),
        "products_source_only": len(s_keys - d_keys),
        "products_destination_only": len(d_keys - s_keys),
        "products_both": len(both),
        "value_divergence": divergence,
        "value_comparison_skipped": not comparable,
        "example_unpublished": sorted(s_keys - d_keys)[:5],
        "example_shadow": sorted(d_keys - s_keys)[:5],
    }


def verdict_bucket(f):
    """Default drop/keep triage. Thresholds are defaults to argue with, not laws."""
    fill = f["fill_pct_in_scope"]
    if f["filled"] == 0:
        return "zero-usage"
    if fill < 5:
        return "low-usage"
    d = f["distinct"]
    if isinstance(d, int) and d == 1 and f["filled"] > 0:
        return "constant"
    if fill >= 95:
        return "reliable"
    return "partial"


def markdown_report(profiles, args, flow=None):
    out = []
    a = out.append
    a("# Data profile\n")
    a("Generated by `profile_export.py`. Fill percentages use the stated denominator; "
      "null-equivalent values (`N/A`, `-`, `TBD`, …) are counted as empty, not filled.\n")
    extra = [f"`{v}`" for v in args.null_equiv] + [f"`/{p}/`" for p in args.null_pattern]
    if extra:
        a("Also counted as empty for this run: " + ", ".join(extra) + "\n")

    a("## Sources\n")
    a("| File | Rows | Columns | Denominator | Duplicate keys |")
    a("|---|---:|---:|---|---:|")
    for p in profiles:
        a(f"| {p['file']} | {p['rows']:,} | {p['columns']:,} | {p['scope']} "
          f"({p['denominator']:,}) | {p['duplicate_keys']:,} |")
    a("")

    if len(profiles) > 1:
        x = cross_source(profiles)
        a("## Source overlap\n")
        a(f"- Distinct field names across all sources: **{x['total_distinct_fields']:,}**")
        a(f"- Present in more than one source: **{x['fields_in_more_than_one_source']:,}** "
          f"({x['overlap_pct']}%)")
        a(f"- Present in one source only: **{x['fields_in_one_source_only']:,}**")
        if x["overlap_pct"] < 25:
            a("\nThe sources barely share a vocabulary, so they are complementary rather "
              "than redundant: none can be dropped, and the migration has to merge all of "
              "them.\n")
        elif x["overlap_pct"] > 60:
            a("\nThe sources largely hold the same fields, so the same fact is recorded more "
              "than once. Something has to decide which one wins — check how often they "
              "actually disagree before assuming the duplication is harmless.\n")
        else:
            a("\nThe sources partly overlap. The shared fields need a rule for which source "
              "wins; the unshared ones are load-bearing and cannot be dropped.\n")

    if flow:
        a("## Flow — source to destination\n")
        a(f"Treating **{flow['source']}** as the source of record and **{flow['destination']}** as "
          "what the customer is shown. Argument order decides this — pass the source first.\n")
        a("| Measure | Count |")
        a("|---|---:|")
        a(f"| Fields at source that never arrive (`FLOW-01`) | {len(flow['fields_source_only']):,} |")
        a(f"| Fields at destination with no source (`FLOW-02`) | {len(flow['fields_destination_only']):,} |")
        a(f"| Fields in both | {len(flow['fields_shared']):,} |")
        a(f"| Products at source, not published (`FLOW-04`) | {flow['products_source_only']:,} |")
        a(f"| Products published, no source record (`FLOW-05`) | {flow['products_destination_only']:,} |")
        a(f"| Products in both | {flow['products_both']:,} |")
        a("")
        a(f"**Enrichment share (`FLOW-06`): {flow['enrichment_share_pct']}%** of what the destination "
          "publishes has no counterpart in the source system.\n")
        if flow["fields_destination_only"]:
            a("Everything in this list was produced by some process between the two systems. "
              "Find out what that process is — it is usually undocumented, and its size is the "
              "work nobody is counting.\n")
            a("> " + ", ".join(f"`{f}`" for f in flow["fields_destination_only"][:40]) +
              ("  …" if len(flow["fields_destination_only"]) > 40 else "") + "\n")
        if flow["fields_source_only"]:
            a("Maintained at source but never seen by a customer — either dead weight kept current "
              "by hand, or a gap in the integration. The client has to say which.\n")
            a("> " + ", ".join(f"`{f}`" for f in flow["fields_source_only"][:40]) +
              ("  …" if len(flow["fields_source_only"]) > 40 else "") + "\n")
        if flow["value_comparison_skipped"]:
            a("*Value comparison (`FLOW-03`) skipped — no key given, or too many products to hold "
              "in memory.*\n")
        elif flow["value_divergence"]:
            a("### Values that disagree between the two systems (`FLOW-03`)\n")
            a("| Field | Differ | Same | % differ | Example (key: source → destination) |")
            a("|---|---:|---:|---:|---|")
            for d in flow["value_divergence"][:30]:
                k, sv, dv = d["example"] if d["example"] else ("", "", "")
                ex = f"`{k}`: {str(sv)[:28]} → {str(dv)[:28]}".replace("|", "\\|")
                a(f"| `{d['field']}` | {d['differ']:,} | {d['same']:,} | {d['differ_pct']} | {ex} |")
            a("")
        else:
            a("*No value disagreements found on shared fields.*\n")

    for p in profiles:
        a(f"## {p['file']}\n")
        if p["segment_counts"]:
            a(f"**Segments ({args.segment}):** " +
              ", ".join(f"`{k}` {v:,}" for k, v in list(p["segment_counts"].items())[:12]))
            a("")
        if p["duplicate_keys"]:
            a(f"**Duplicate `{p['key']}` values:** {p['duplicate_keys']:,} keys covering "
              f"{p['duplicate_key_rows']:,} rows. Examples: " +
              ", ".join(f"`{k}`×{v}" for k, v in list(p["duplicate_examples"].items())[:5]))
            a("")

        buckets = Counter(verdict_bucket(f) for f in p["fields"])
        a("**Field triage:** " + " · ".join(
            f"{k} {v}" for k, v in
            sorted(buckets.items(), key=lambda kv: ["zero-usage", "low-usage", "constant",
                                                    "partial", "reliable"].index(kv[0]))))
        a("")

        a("| Field | Fill % | Null-equiv | Distinct | Type | Flags | Triage | Example |")
        a("|---|---:|---:|---:|---|---|---|---|")
        for f in sorted(p["fields"], key=lambda f: f["fill_pct_in_scope"]):
            flags = ", ".join(f"{k}×{v}" for k, v in f["flags"].items()
                              if k != "null_equivalent") or ""
            ex = (f["samples"][0][:40] + "…") if f["samples"] and len(f["samples"][0]) > 40 else (
                f["samples"][0] if f["samples"] else "")
            ex = ex.replace("|", "\\|")
            ne = f["null_equivalents"] or ""
            a(f"| `{f['field']}` | {f['fill_pct_in_scope']} | {ne} | {f['distinct']} | "
              f"{f['dominant_type'] or ''} | {flags} | {verdict_bucket(f)} | {ex} |")
        a("")
        a("`Null-equiv` counts cells holding a value that carries no information "
          "(`N/A`, `-`, `TBD`, …). They are excluded from Fill %, so a field with a high "
          "null-equivalent count looks fuller in the source system than it is here.\n")

        clusters = concept_clusters(p["header"])
        if clusters:
            a("### Possible attribute proliferation\n")
            a("Field names differing only by a unit or language suffix. Each group may be "
              "one concept split across several attributes.\n")
            a("| Concept | Fields |")
            a("|---|---|")
            for base, members in sorted(clusters.items())[:60]:
                a(f"| {base} | " + ", ".join(f"`{m}`" for m in members) + " |")
            a("")

    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default=".")
    ap.add_argument("--key")
    ap.add_argument("--segment")
    ap.add_argument("--scope")
    ap.add_argument("--multi-delim", dest="multi_delim", action="append")
    ap.add_argument("--null-equiv", dest="null_equiv", action="append", default=[])
    ap.add_argument("--null-pattern", dest="null_pattern", action="append", default=[])
    ap.add_argument("--sample", type=int, default=20)
    ap.add_argument("--max-rows", type=int)
    args = ap.parse_args()
    # Engagement-specific placeholders count as empty, like the built-in list.
    NULL_EQUIVALENTS.update(v.strip().casefold() for v in args.null_equiv)
    NULL_PATTERNS.extend(re.compile(p, re.I) for p in args.null_pattern)

    os.makedirs(args.out, exist_ok=True)

    # Shared fields have to be known before profiling, so FLOW can retain their values.
    shared_fields = None
    if len(args.files) > 1 and args.key:
        seen = Counter()
        for header in collect_headers(args.files):
            for h in set(x.casefold() for x in header):
                seen[h] += 1
        shared_fields = {h for h, n in seen.items() if n > 1}

    profiles = []
    for path in args.files:
        sys.stderr.write(f"profiling {path} …\n")
        profiles.append(profile(path, args, shared_fields))

    flow = None
    if len(profiles) > 1 and args.key:
        flow = flow_comparison(profiles[0], profiles[1])
        if len(profiles) > 2:
            sys.stderr.write("note: FLOW compares the first two files only "
                             "(source first, destination second)\n")

    md = markdown_report(profiles, args, flow)

    # Working sets are large and not worth serialising.
    for p in profiles:
        for k in ("_keys", "_key_values", "_key_values_overflowed"):
            p.pop(k, None)
    with open(os.path.join(args.out, "profile.json"), "w", encoding="utf-8") as fh:
        json.dump({"profiles": profiles,
                   "cross_source": cross_source(profiles) if len(profiles) > 1 else None,
                   "flow": flow},
                  fh, indent=2, ensure_ascii=False)
    with open(os.path.join(args.out, "profile.md"), "w", encoding="utf-8") as fh:
        fh.write(md)

    sys.stderr.write(f"\nwrote {args.out}/profile.md and {args.out}/profile.json\n")


if __name__ == "__main__":
    main()
