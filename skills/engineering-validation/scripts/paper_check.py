#!/usr/bin/env python3
"""Check LaTeX manuscript consistency with conservative source heuristics.

Checks: labels, references, citations, float labels and source reference order.
Heuristics: trial granularity, prose percentages, table_arithmetic and
text_table_mismatch. Compiled reference order: aux_float_order (with an aux file).
Not checked: general macro expansion and compiled float placement on pages.
Usage: python3 paper_check.py path/to/main.tex [--bib refs.bib] [--aux main.aux] [--json]
"""

import argparse
import bisect
import json
import re
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


COMMAND = re.compile(r"\\([A-Za-z]+)\*?")
TOKEN = re.compile(r"%|\\([A-Za-z]+)\*?")
REFERENCES = set("ref eqref autoref cref Cref pageref vref Vref cpageref "
                 "Cpageref labelcref nameref subref".split())
RANGES = {"crefrange", "Crefrange", "cpagerefrange"}
CITES = set("cite citep citet citealp citealt citeauthor citeyear citeyearpar "
            "citenum Cite Citep Citet parencite Parencite textcite Textcite "
            "autocite Autocite footcite supercite nocite citefield".split())
DEFINITIONS = {"newcommand", "renewcommand", "providecommand", "DeclareRobustCommand"}
LITERALS = {"verbatim", "Verbatim", "lstlisting", "minted", "comment"}
LEVELS = {"chapter": 0, "section": 1, "subsection": 2,
          "subsubsection": 3, "paragraph": 4, "subparagraph": 5}
TABULARS = {"tabular", "tabular*", "tabularx", "tabulary", "longtable"}
TRANSPARENT = TABULARS | {"document", "center", "minipage", "subfigure",
                          "subtable", "subcaption", "threeparttable"}
NUMBER = r"\d+(?:\.\d+)?"
PERCENT = re.compile(r"(?<![\d.])(" + NUMBER + r")\s*\\%")
SUCCESS = re.compile(r"\b(?:success|completion)\b", re.I)
WORDS = dict(zip(
    "one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(), range(1, 21)))
WORDS.update(dict(zip("thirty forty fifty sixty seventy eighty ninety".split(), range(30, 100, 10))))
COUNT = (r"\d+|(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
         r"-(?:one|two|three|four|five|six|seven|eight|nine)|" + "|".join(WORDS))
TRIALS = re.compile(r"\b(" + COUNT + r")\s+"
                    r"(?:(?:repeated|independent)\s+)*(?:trials?|runs?)\b", re.I)
GROUP_COUNTS = re.compile(r"\b(" + COUNT + r")\s+(object|condition|seed)s?\b", re.I)
AGGREGATION = re.compile(r"\b(?:overall|average|averaged|mean|across|in\s+total|total|"
                         r"pooled|for\s+each\s+of|per\s+(?:object|condition))\b", re.I)
TABLE_NUMBER = r"[+-]?(?:\d+(?:\.\d+)?|\.\d+)"
SUMMARY = {"avg", "average", "mean", "overall", "total"}


def escaped(text, pos):
    start = pos
    while start > 0 and text[start - 1] == "\\":
        start -= 1
    return (pos - start) % 2 == 1


def blank(text):
    return "".join("\n" if c == "\n" else " " for c in text)


def group(text, pos, tex=False):
    """Read a balanced group; braces shield delimiters inside options."""
    pairs, stack = {"{": "}", "[": "]", "(": ")"}, [text[pos]]
    comment = False
    for end in range(pos + 1, len(text)):
        if comment:
            comment = text[end] != "\n"
            continue
        if escaped(text, end):
            continue
        char = text[end]
        if tex and char == "%":
            comment = True
            continue
        if char == "{" or (char == stack[-1] and char != "{"):
            stack.append(char)
        elif char == pairs[stack[-1]]:
            stack.pop()
            if not stack:
                return text[pos + 1:end], end + 1
    return "", pos + 1


def space(text, pos):
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def command_args(text, match):
    name, pos, args, options = match.group(1), match.end(), [], []
    limit = 3 if name == "begin" else 2 if name in RANGES | {"SI", "qty", "citefield"} else 1
    while len(args) < limit:
        pos = space(text, pos)
        if pos >= len(text) or text[pos] not in "[{":
            break
        opening = text[pos]
        value, end = group(text, pos, tex=True)
        if end == pos + 1:
            break
        (args if opening == "{" else options).append(value)
        pos = end
        if name == "begin" and len(args) == 1:
            limit = 3 if value in {"tabular*", "tabularx"} else 2 if value in TABULARS | {"minted"} else 1
    if name in {"input", "include"} and not args:
        token = re.match(r"[^\s{}\\%]+", text[pos:])
        if token:
            args.append(token.group())
            pos += token.end()
    # Listing options follow the environment argument; keep them outside its body.
    if name == "begin":
        pos = space(text, pos)
    if name == "begin" and pos < len(text) and text[pos] == "[":
        value, end = group(text, pos, tex=True)
        if end != pos + 1:
            options.append(value)
            pos = end
    return {"name": name, "value": args[0] if args else "", "args": args,
            "options": options, "pos": match.start(), "end": pos}


def commands(text):
    for match in COMMAND.finditer(text):
        if not escaped(text, match.start()):
            cmd = command_args(text, match)
            if cmd["args"] or cmd["options"]:
                yield cmd


def definition_end(text, match, wrappers):
    """Skip definitions, recognizing only a single-argument reference wrapper."""
    name, pos = match.group(1), space(text, match.end())
    if pos < len(text) and text[pos] == "{":
        macro, pos = group(text, pos, tex=True)
    else:
        token = re.match(r"\\(?:[A-Za-z]+|.)", text[pos:])
        if not token:
            return pos
        macro, pos = token.group(), pos + token.end()
    macro = macro.lstrip("\\")
    wrappers.pop(macro, None)
    if name == "let":
        pos = space(text, pos)
        if text[pos:pos + 1] == "=":
            pos = space(text, pos + 1)
        token = re.match(r"\\(?:[A-Za-z]+|.)|.", text[pos:])
        return pos + token.end() if token else pos
    options = []
    pos = space(text, pos)
    while name in DEFINITIONS and text[pos:pos + 1] == "[":
        value, end = group(text, pos, tex=True)
        if end == pos + 1:
            return end
        options.append(value)
        pos = space(text, end)
    if name == "def":
        opening = text.find("{", pos)
        pos = len(text) if opening < 0 else opening
    if text[pos:pos + 1] != "{":
        return pos
    body, end = group(text, pos, tex=True)
    refs = list(commands(body))
    if (name in DEFINITIONS and options == ["1"] and len(refs) == 1
            and refs[0]["name"] in REFERENCES and refs[0]["value"] == "#1"):
        wrappers[macro] = refs[0]["name"]
    return end


def clean_source(text, wrappers):
    """Mask comments, definitions and literal text without changing offsets."""
    parts, cursor, pos = [], 0, 0
    while True:
        match = TOKEN.search(text, pos)
        if not match:
            break
        pos = match.end()
        if escaped(text, match.start()):
            continue
        start, end, name = match.start(), pos, match.group(1)
        if name is None:
            end = text.find("\n", pos)
            end = len(text) if end < 0 else end
        elif name == "verb":
            delimiter = text[pos:pos + 1]
            end = text.find(delimiter, pos + 1) if delimiter else -1
            newline = text.find("\n", pos)
            end = end + 1 if end >= 0 else len(text)
            if newline >= 0:
                end = min(end, newline)
        elif name == "iffalse":
            depth = 1
            while depth:
                token = TOKEN.search(text, end)
                if not token:
                    end = len(text)
                    break
                end = token.end()
                if escaped(text, token.start()):
                    continue
                conditional = token.group(1)
                if conditional is None:
                    newline = text.find("\n", end)
                    end = len(text) if newline < 0 else newline
                elif conditional.startswith("if"):
                    depth += 1
                elif conditional == "fi":
                    depth -= 1
        elif name in DEFINITIONS | {"def", "let"}:
            end = definition_end(text, match, wrappers)
        elif name == "begin":
            cmd = command_args(text, match)
            if cmd["value"] not in LITERALS:
                continue
            closing = re.search(r"\\end\s*\{" + re.escape(cmd["value"]) + r"\}", text[cmd["end"]:])
            start = cmd["end"]
            end = start + closing.start() if closing else len(text)
        else:
            continue
        parts.extend((text[cursor:start], blank(text[start:end])))
        cursor, pos = end, end
    return "".join(parts) + text[cursor:]


def display_path(path):
    try:
        return path.relative_to(Path.cwd()).as_posix()
    except ValueError:
        return path.as_posix()


def finding(check, severity, location, message, hint):
    return {"check": check, "severity": severity, "file": location[0],
            "line": location[1], "message": message + " Fix: " + hint}


def keys(value):
    return [key.strip() for key in value.split(",") if key.strip() and "#" not in key]


def resolved(value):
    return not any(c in value for c in "\\{}#%")


def separated(text, delimiter):
    """Split at top-level delimiters, retaining each field's offset."""
    start = pos = 0
    while pos < len(text):
        if text[pos] == "{" and not escaped(text, pos):
            _, end = group(text, pos, tex=True)
            pos = end if end != pos + 1 else len(text)
        elif text.startswith(delimiter, pos) and not escaped(text, pos):
            yield start, text[start:pos]
            start = pos = pos + len(delimiter)
        else:
            pos += 1
    yield start, text[start:]


class Source:
    """Expand local includes relative to the entrypoint, retaining locations."""

    def __init__(self, main):
        self.main = Path(main).resolve()
        self.root = self.main.parent
        self.parts, self.starts, self.origins, self.wrappers = [], [], [], {}
        self.size, self.findings = 0, []
        self.expand(self.main, set(), (display_path(self.main), 1))
        self.text = "".join(self.parts)

    def append(self, text, path, line):
        if text:
            self.starts.append(self.size)
            self.origins.append((display_path(path), line, text))
            self.parts.append(text)
            self.size += len(text)

    def expand(self, path, active, location):
        if path in active:
            self.findings.append(finding("include_cycle", "error", location,
                                         "Recursive include of '" + display_path(path) + "'.",
                                         "Remove the include cycle."))
            return
        try:
            text = clean_source(path.read_text(encoding="utf-8"), self.wrappers)
        except (OSError, UnicodeError) as exc:
            severity = "info" if active else "error"
            message = ("not checked: input not found locally '" + display_path(path) + "'."
                       if active else "Cannot read '" + display_path(path) + "': " + str(exc))
            self.findings.append(finding("source_unreadable", severity, location, message,
                                         "Correct the source path or encoding."))
            return
        active, cursor = active | {path}, 0
        for cmd in commands(text):
            if cmd["name"] not in {"input", "include"} or cmd["pos"] < cursor:
                continue
            pos, value = cmd["pos"], cmd["value"].strip()
            self.append(text[cursor:pos], path, text.count("\n", 0, cursor) + 1)
            location = (display_path(path), text.count("\n", 0, pos) + 1)
            if resolved(value):
                child = self.root / value
                if not child.suffix:
                    child = child.with_suffix(".tex")
                self.expand(child.resolve(), active, location)
            elif "#" not in value:
                self.findings.append(finding("input_not_checked", "info", location,
                                             "not checked: input filename cannot be resolved.",
                                             "Use a literal filename for source checking."))
            self.append("\n", path, location[1])
            cursor = cmd["end"]
        self.append(text[cursor:], path, text.count("\n", 0, cursor) + 1)

    def location(self, pos):
        index = bisect.bisect_right(self.starts, pos) - 1
        if index < 0:
            return display_path(self.main), 1
        path, line, text = self.origins[index]
        return path, line + text.count("\n", 0, pos - self.starts[index])


def contains(items, pos):
    return any(item["start"] <= pos < item["end"] for item in items)


def structure(events, length):
    floats, tabulars, sections, env_stack, section_stack = [], [], [], [], []
    counts = defaultdict(int)
    for cmd in events:
        name, value, pos = cmd["name"], cmd["value"], cmd["pos"]
        if name == "begin":
            item = {"start": pos, "body": cmd["end"], "end": length, "env": value, "captions": []}
            if value in {"figure", "figure*", "table", "table*"}:
                kind = value.rstrip("*")
                counts[kind] += 1
                item.update(kind=kind, number=counts[kind], labels=[])
                floats.append(item)
            elif value in TABULARS:
                tabulars.append(item)
            env_stack.append(item)
        cmd["owner"] = next((e for e in reversed(env_stack) if e["env"] not in TRANSPARENT), None)
        cmd["float"] = next((e for e in reversed(env_stack) if "kind" in e), None)
        if name == "end":
            for index in range(len(env_stack) - 1, -1, -1):
                if env_stack[index]["env"] == value:
                    env_stack[index]["end"] = pos
                    del env_stack[index:]
                    break
        elif name == "caption" and cmd["float"] is not None:
            cmd["float"]["captions"].append(value)
        elif name in LEVELS:
            level = LEVELS[name]
            while section_stack and section_stack[-1]["level"] >= level:
                section_stack.pop()["end"] = pos
            item = {"start": pos, "end": length, "title": value, "level": level,
                    "parent": section_stack[-1] if section_stack else None, "statements": {}}
            sections.append(item)
            section_stack.append(item)
    return floats, tabulars, sections


def section_at(sections, pos):
    return next((s for s in reversed(sections) if s["start"] <= pos < s["end"]), None)


def check_bibliography(source, events, refs, bib):
    findings, paths, entries = [], {}, {}
    declared = bib is not None
    if declared:
        paths[Path(bib).resolve()] = (display_path(source.main), 1)
    else:
        for cmd in events:
            if cmd["name"] in {"bibliography", "addbibresource"}:
                declared = True
                for name in keys(cmd["value"]):
                    if not resolved(name):
                        findings.append(finding("bibliography_unavailable", "info", source.location(cmd["pos"]),
                                                 "not checked: bibliography filename cannot be resolved.",
                                                 "Provide a literal bibliography path."))
                        continue
                    path = source.root / name
                    paths[path.with_suffix(".bib").resolve() if not path.suffix else path.resolve()] = source.location(cmd["pos"])
    for path, location in paths.items():
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            findings.append(finding("bibliography_unavailable", "error", location,
                                     "Cannot read bibliography '" + display_path(path) + "'.",
                                     "Provide a readable bibliography path."))
            continue
        cursor = 0
        for match in re.finditer(r"@([A-Za-z]+)\s*[{(]", text):
            if match.start() < cursor:
                continue
            body, cursor = group(text, match.end() - 1)
            if match.group(1).lower() not in {"comment", "string", "preamble"} and "," in body:
                key = body.split(",", 1)[0].strip()
                if key and "#" not in key:
                    entries[key] = (display_path(path), text.count("\n", 0, match.start()) + 1)
    if not declared:
        findings.append(finding("bibliography_skipped", "info", (display_path(source.main), 1),
                                 "Citation checks skipped: no bibliography found.",
                                 "Use --bib or declare a bibliography in the manuscript."))
    # A partial bibliography cannot establish that an entry is missing or uncited.
    if not declared or any(f["check"] == "bibliography_unavailable" for f in findings):
        return findings
    for key, positions in refs.items():
        if key != "*" and key not in entries:
            for pos in positions:
                findings.append(finding("missing_citation", "error", source.location(pos),
                                         "Citation key '" + key + "' is missing from the bibliography.",
                                         "Add the entry or correct the citation key."))
    if "*" not in refs:
        for key in sorted(entries.keys() - refs.keys()):
            findings.append(finding("uncited_bib_entry", "info", entries[key],
                                     "Bibliography entry '" + key + "' is never cited.",
                                     "Cite the relevant entry or remove it."))
    return findings


def possible_percentage(value, count):
    value = Decimal(str(value))
    if count <= 0 or not 0 <= value <= 100:
        return False
    precision = Decimal(1).scaleb(value.as_tuple().exponent)
    nearest = int(value * count / 100)
    return any((Decimal(100) * k / count).quantize(precision, rounding=ROUND_HALF_UP) == value
               for k in range(max(0, nearest - 1), min(count, nearest + 1) + 1))


def count_value(token):
    return int(token) if token.isdigit() else sum(WORDS[w] for w in token.lower().split("-"))


def trial_counts(text):
    return {count_value(m.group(1))
            for m in TRIALS.finditer(text) if m.group(1) != "0"}


def aggregated_trial_counts(texts, counts):
    """Use explicit per-group totals; return None for other aggregated values."""
    if not any(AGGREGATION.search(text) and GROUP_COUNTS.search(text) for text in texts):
        return counts
    if len(counts) != 1:
        return None
    totals = set()
    for text in texts:
        if trial_counts(text) != counts:
            continue
        for match in GROUP_COUNTS.finditer(text):
            if re.search(r"\bfor\s+each\s+of\s*$", text[:match.start()], re.I):
                totals.add(next(iter(counts)) * count_value(match.group(1)))
        for match in TRIALS.finditer(text):
            unit = re.match(r"\s+per\s+(object|condition|seed)\b", text[match.end():], re.I)
            if unit:
                multipliers = {count_value(group.group(1)) for context in texts
                               for group in GROUP_COUNTS.finditer(context)
                               if group.group(2).lower() == unit.group(1).lower()}
                if len(multipliers) == 1:
                    totals.add(next(iter(counts)) * next(iter(multipliers)))
    return totals if len(totals) == 1 and next(iter(totals)) > 0 else None


def percentage_values(text):
    values = [(m.start(), m.group(1)) for m in PERCENT.finditer(text)]
    for cmd in commands(text):
        if (cmd["name"] in {"SI", "qty"} and len(cmd["args"]) == 2
                and cmd["args"][1].strip() in {r"\percent", r"\%"}
                and re.fullmatch(NUMBER, cmd["value"].strip())):
            values.append((cmd["pos"], cmd["value"].strip()))
    return [(pos, token) for pos, token in values if Decimal(token) <= 100]


def table_percentages(source, tabulars, floats):
    """Infer plain numeric percentages only from explicit column units."""
    values, unknown = [], False
    for table in tabulars:
        parent = next((f for f in reversed(floats) if f["kind"] == "table"
                       and f["start"] <= table["start"] < f["end"]), None)
        table["success"] = bool(parent and SUCCESS.search(" ".join(parent["captions"])))
        table["parent"] = parent
        percent_columns, unit_columns = set(), set()
        body = source.text[table["body"]:table["end"]]
        row_start = 0
        separators = list(re.finditer(r"\\\\(?:\[[^]]*\])?", body))
        for row_end, next_start in [(m.start(), m.end()) for m in separators] + [(len(body), len(body))]:
            row, cell_start = body[row_start:row_end], row_start
            for column, (offset, cell) in enumerate(separated(row, "&")):
                cell_start = row_start + offset
                clean = re.sub(r"\\(?:hline|toprule|midrule|bottomrule)\b", "", cell).strip()
                plain = re.fullmatch(NUMBER, clean)
                explicit = percentage_values(cell)
                if not plain and not explicit:
                    unknown |= bool(re.search(r"\d", cell))
                    table["success"] |= bool(SUCCESS.search(cell))
                    if re.search(r"\\%|\\percent\b", cell):
                        percent_columns.add(column)
                        unit_columns.add(column)
                    elif re.search(r"\([^)]*[A-Za-z][^)]*\)|\\(?:si|unit)\b", cell):
                        unit_columns.add(column)
                elif plain and column in percent_columns:
                    if Decimal(clean) <= 100:
                        values.append((table["body"] + cell_start + cell.find(clean), clean))
                elif plain and column not in unit_columns:
                    unknown = True
            row_start = next_start
    return values, unknown


def check_percentages(source, sections, floats, tabulars):
    findings = []
    plain, unknown_units = table_percentages(source, tabulars, floats)
    percentages = sorted(set(percentage_values(source.text) + plain))
    table_values = {Decimal(token) for pos, token in percentages if contains(tabulars, pos)}
    prose = list(source.text)
    for item in floats + tabulars:
        prose[item["start"]:item["end"]] = blank(source.text[item["start"]:item["end"]])
    for cmd in commands(source.text):
        if cmd["name"] in LEVELS:
            prose[cmd["pos"]:cmd["end"]] = blank(source.text[cmd["pos"]:cmd["end"]])
    prose = "".join(prose)
    boundaries = [0] + [m.end() for m in re.finditer(r"\.(?!\d)|[!?]|\n\s*\n", prose)] + [len(prose)]
    for match in TRIALS.finditer(prose):
        section = section_at(sections, match.start())
        if section is not None:
            index = bisect.bisect_right(boundaries, match.start()) - 1
            start, end = boundaries[index:index + 2]
            section["statements"][start] = (end, trial_counts(prose[start:end]))
    for pos, token in percentages:
        section, counts = section_at(sections, pos), set()
        table = next((t for t in reversed(tabulars) if t["start"] <= pos < t["end"]), None)
        index = bisect.bisect_right(boundaries, pos) - 1
        sentence = prose[boundaries[index]:boundaries[index + 1]]
        contexts = [sentence]
        success = table["success"] if table else bool(re.search(r"\bsuccess\b", sentence, re.I))
        if table and table["parent"]:
            caption = " ".join(table["parent"]["captions"])
            counts = trial_counts(caption)
            contexts.append(caption)
        scope = section
        while success and not counts and scope is not None:
            distances = [(max(start - pos, pos - end, 0), ns, prose[start:end])
                         for start, (end, ns) in scope["statements"].items()]
            if distances:
                nearest = min(distance for distance, _, _ in distances)
                counts = set().union(*(ns for distance, ns, _ in distances if distance == nearest))
                if counts:
                    contexts.extend(text for distance, _, text in distances if distance == nearest)
            scope = scope["parent"]
        if success:
            counts = aggregated_trial_counts(contexts, counts)
        if success and counts is None:
            findings.append(finding("trial_granularity", "info", source.location(pos),
                                     "Heuristic: aggregated value; trial granularity not checked.",
                                     "State the denominator for this success rate."))
        elif success and len(counts) > 1:
            findings.append(finding("trial_granularity", "info", source.location(pos),
                                     "Heuristic: ambiguous trial count (N="
                                     + ", ".join(map(str, sorted(counts))) + "); percentage not checked.",
                                     "State the denominator for this success rate."))
        elif success and counts and not possible_percentage(token, next(iter(counts))):
            digits = max(0, -Decimal(token).as_tuple().exponent)
            findings.append(finding("trial_granularity", "warning", source.location(pos),
                                     "Heuristic: " + token + "% is impossible for stated N="
                                     + str(next(iter(counts))) + " trials per condition, even after rounding to "
                                     + str(digits) + " decimal places.",
                                     "Check the percentage, denominator, or aggregation description."))
        results_section = section
        while results_section is not None and not re.search(r"experiment|result|evaluation", results_section["title"], re.I):
            results_section = results_section["parent"]
        if (results_section is not None and not contains(floats + tabulars, pos)
                and Decimal(token) not in table_values and not unknown_units):
            findings.append(finding("prose_percentage_not_tabulated", "info", source.location(pos),
                                     "Heuristic: prose percentage " + token
                                     + "% appears in no tabular environment in the document.",
                                     "Add supporting tabulated data or explain the prose-only result."))
    return findings


def cell_text(text):
    """Unwrap common presentation macros, leaving unknown content opaque."""
    parts, cursor = [], 0
    for match in COMMAND.finditer(text):
        if match.start() < cursor or escaped(text, match.start()):
            continue
        name, end = match.group(1), match.end()
        if name in {"textcolor", "color", "cellcolor", "colorbox", "fcolorbox"}:
            end = space(text, end)
            if text[end:end + 1] == "[":
                _, end = group(text, end)
            for _ in range(2 if name == "fcolorbox" else 1):
                end = space(text, end)
                if text[end:end + 1] != "{":
                    break
                _, end = group(text, end)
        elif name not in {"textbf", "textit", "textnormal", "textrm", "textsf",
                          "texttt", "emph", "underline", "mathbf", "mathrm", "mathit",
                          "text", "mbox", "makecell", "bm", "boldsymbol", "bf", "bfseries", "itshape",
                          "normalfont", "quad", "qquad", "enspace"}:
            continue
        parts.append(text[cursor:match.start()])
        cursor = end
    parts.append(text[cursor:])
    text = "".join(parts).replace(r"\%", "%")
    text = re.sub(r"\\[,;! ]|\\[()]", " ", text)
    return " ".join(text.translate(str.maketrans("", "", "{}$")).replace("~", " ").split())


def header_text(text):
    text = cell_text(text)
    unit = re.search(r"\s*[([]\s*(%|[A-Za-z]+)\s*[)\]]$", text)
    return (text[:unit.start()].strip(), unit.group(1)) if unit else (text, "")


def numeric_cell(text, unit=""):
    text = cell_text(text)
    match = re.fullmatch(r"(" + TABLE_NUMBER + r")\s*(%|[A-Za-z]+)?"
                         r"(?:\s*(?:\\pm|±|\+/-|\+-)\s*" + TABLE_NUMBER
                         + r"\s*(%|[A-Za-z]+)?)?", text)
    if not match:
        return None
    units = {value for value in (unit, match.group(2), match.group(3)) if value}
    if len(units) > 1:
        return None
    return {"token": match.group(1), "value": Decimal(match.group(1)),
            "unit": next(iter(units), "")}


def parsed_tables(source, tabulars, floats):
    """Retain simple cells and their source positions; spans stay unchecked."""
    tables = []
    rules = re.compile(r"\s*(?:\[[^]]*\]|\\(?:hline|toprule|midrule|bottomrule|"
                       r"addlinespace)\b(?:\s*\[[^]]*\])?|"
                       r"\\(?:cline|cmidrule)\b(?:\s*\[[^]]*\])?"
                       r"(?:\s*\([^)]*\))?\s*\{[^}]*\})")
    for tabular in tabulars:
        body = source.text[tabular["body"]:tabular["end"]]
        if re.search(r"\\(?:multirow|multicolumn|begin)\b", body):
            continue
        blocks, rows, headers = [], [], []
        for offset, row in separated(body, r"\\"):
            divided = False
            while True:
                match = rules.match(row)
                if not match:
                    break
                divided |= bool(re.search(r"\\midrule\b", match.group()))
                offset, row = offset + match.end(), row[match.end():]
            if divided and rows:
                blocks.append((headers, rows))
                headers, rows = [], []
            if not row.strip():
                continue
            cells = [{"text": cell, "pos": tabular["body"] + offset + start
                      + len(cell) - len(cell.lstrip())}
                     for start, cell in separated(row, "&")]
            if sum(numeric_cell(cell["text"]) is None for cell in cells) * 2 > len(cells):
                if rows:
                    blocks.append((headers, rows))
                    rows = []
                headers = [header_text(cell["text"]) for cell in cells]
            else:
                rows.append(cells)
        if rows:
            blocks.append((headers, rows))
        parent = next((f for f in floats if f["kind"] == "table"
                       and f["start"] <= tabular["start"] < f["end"]), None)
        for headers, rows in blocks:
            width = len(headers) if headers else len(rows[0])
            headers = headers or [("", "")] * width
            row_headers = all(numeric_cell(row[0]["text"]) is None
                              and cell_text(row[0]["text"]) for row in rows)
            for row in rows:
                row_unit = header_text(row[0]["text"])[1] if row_headers else ""
                for column, cell in enumerate(row):
                    unit = headers[column][1] if column < width else ""
                    cell["number"] = (None if unit and row_unit and unit != row_unit
                                      else numeric_cell(cell["text"], unit or row_unit))
            tables.append({"headers": headers, "rows": rows, "width": width,
                           "row_headers": row_headers, "parent": parent,
                           "id": parent["start"] if parent else tabular["start"]})
    return tables


def check_table_arithmetic(source, tables):
    findings = []

    def compare(label, cell, others, row_name=""):
        numbers = [other["number"] for other in [cell] + others]
        if not others or any(number is None for number in numbers):
            return
        if len({number["unit"] for number in numbers}) != 1:
            return
        reported = numbers[0]
        computed = sum((number["value"] for number in numbers[1:]), Decimal(0))
        if label.rstrip(".").lower() != "total":
            computed /= len(others)
        tolerance = Decimal("0.5").scaleb(reported["value"].as_tuple().exponent)
        if abs(reported["value"] - computed) > tolerance:
            precision = Decimal(1).scaleb(min(-1, reported["value"].as_tuple().exponent))
            recomputed = computed.quantize(precision, rounding=ROUND_HALF_UP)
            findings.append(finding("table_arithmetic", "warning", source.location(cell["pos"]),
                                     "Heuristic: " + (row_name + ": " if row_name else "")
                                     + label + " reports " + reported["token"]
                                     + reported["unit"] + "; recomputed value is "
                                     + format(recomputed.normalize(), "f") + reported["unit"] + ".",
                                     "Check the summary cell or explain a weighted aggregation."))

    for table in tables:
        rows, width = table["rows"], table["width"]
        columns = [i for i, (label, _) in enumerate(table["headers"])
                   if label.rstrip(".").lower() in SUMMARY]
        summaries = [i for i, row in enumerate(rows) if table["row_headers"]
                     and header_text(row[0]["text"])[0].rstrip(".").lower() in SUMMARY]
        first = int(table["row_headers"])
        if len(columns) == 1:
            column = columns[0]
            for index, row in enumerate(rows):
                if len(row) == width and index not in summaries:
                    compare(table["headers"][column][0], row[column],
                            [row[i] for i in range(first, width) if i != column],
                            header_text(row[0]["text"])[0] if table["row_headers"] else "")
        if len(summaries) == 1 and all(len(row) == width for row in rows):
            index = summaries[0]
            for column in range(first, width):
                if column not in columns:
                    compare(header_text(rows[index][0]["text"])[0], rows[index][column],
                            [row[column] for i, row in enumerate(rows) if i != index])
    return findings


def check_text_tables(source, tables, floats, tabulars, refs):
    labels = defaultdict(list)
    row_names = set()
    bodies = []
    for tabular in tabulars:
        parent = next((f for f in floats if f["kind"] == "table"
                       and f["start"] <= tabular["start"] < f["end"]), None)
        bodies.append((parent["start"] if parent else tabular["start"],
                       cell_text(source.text[tabular["body"]:tabular["end"]])))
    for table in tables:
        rows = [row for row in table["rows"] if len(row) == table["width"]]
        numeric = [i for i in range(int(table["row_headers"]), table["width"])
                   if any(row[i]["number"] is not None for row in rows)]
        success = [i for i, (label, _) in enumerate(table["headers"]) if SUCCESS.search(label)]
        selected = success if success else numeric
        column = selected[0] if len(selected) == 1 else None
        entries = []
        if table["row_headers"]:
            entries.extend((header_text(row[0]["text"])[0],
                            [row[column]] if column is not None and len(row) == table["width"] else [])
                           for row in table["rows"])
            row_names.update(label.lower() for label, _ in entries if len(label) >= 4)
        entries.extend((label, [row[i] for row in rows] if i in selected else [])
                       for i, (label, _) in enumerate(table["headers"]))
        if len(selected) > 1:
            row_names.update(label.lower() for i, (label, _) in enumerate(table["headers"])
                             if i in selected and len(label) >= 4)
        for label, cells in entries:
            if len(label) >= 4 and not re.search(r"[\\{}]", label):
                labels[label.lower()].append((table, cells))
    prose = list(source.text)
    for item in floats + tabulars:
        prose[item["start"]:item["end"]] = blank(source.text[item["start"]:item["end"]])
    # Headings and reference keys cannot supply prose row or column names.
    for cmd in commands(source.text):
        if cmd["name"] in LEVELS.keys() | REFERENCES | RANGES | {"hyperref"} | source.wrappers.keys():
            prose[cmd["pos"]:cmd["end"]] = blank(source.text[cmd["pos"]:cmd["end"]])
    prose = "".join(prose)
    boundaries = [0] + [m.end() for m in re.finditer(r"\.(?!\d)|[!?]|\n\s*\n", prose)] + [len(prose)]
    findings = []
    for start, end in zip(boundaries, boundaries[1:]):
        sentence = prose[start:end]
        referenced = {table["start"] for table in floats if table["kind"] == "table"
                      and any(start <= pos < end for key in table["labels"]
                              for pos in refs.get(key, []))}
        for label, entries in labels.items():
            pattern = r"(?<!\w)" + r"[\s~]+".join(map(re.escape, label.split())) + r"(?!\w)"
            # Even an unaligned table can make an otherwise unique name ambiguous.
            if not referenced and len({table_id for table_id, body in bodies
                                       if re.search(pattern, body, re.I)}) != 1:
                continue
            candidates = [(table, cells) for table, cells in entries
                          if table["id"] in referenced] if referenced else entries
            if len(candidates) != 1:
                continue
            cells = {cell["pos"]: cell for _, items in candidates for cell in items}
            if len(cells) != 1:
                continue
            cell = next(iter(cells.values()))
            number = cell["number"]
            if number is None or number["unit"] not in {"", "%"}:
                continue
            for match in re.finditer(pattern, sentence, re.I):
                following = sentence[match.end():]
                percent = re.search(r"(?<![\d.])(" + NUMBER + r")\s*\\%", following)
                claims = []
                if percent:
                    claims.append((percent.group(1), following[:percent.start()],
                                   start + match.end() + percent.start(1)))
                preceding = list(PERCENT.finditer(sentence[:match.start()]))
                if preceding:
                    percent = preceding[-1]
                    claims.append((percent.group(1), sentence[percent.end():match.start()],
                                   start + percent.start(1)))
                for token, between, pos in claims:
                    if (re.search(r"\d|[,;:]|\b(?:and|whereas|while)\b", between, re.I)
                            or any(re.search(r"(?<!\w)" + re.escape(other) + r"(?!\w)", between, re.I)
                                   for other in row_names if other != label)):
                        continue
                    if Decimal(token) != number["value"]:
                        location = source.location(cell["pos"])
                        findings.append(finding("text_table_mismatch", "warning", source.location(pos),
                                                 "Heuristic: '" + sentence[match.start():match.end()]
                                                 + "' is " + token + "% in prose, but "
                                                 + number["token"] + "% in the table at {}:{}.".format(*location),
                                                 "Make the prose and table values agree or explain the difference."))
                    break
    return findings


def compiled_number(token):
    if re.fullmatch(r"\d+(?:\.\d+)*", token):
        return tuple(int(part) for part in token.split("."))
    if re.fullmatch(r"(?=[MDCLXVI]+$)M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})"
                    r"(?:IX|IV|V?I{0,3})", token, re.I):
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        digits = [values[char] for char in token.upper()]
        return (sum(-value if i + 1 < len(digits) and value < digits[i + 1] else value
                    for i, value in enumerate(digits)),)
    return None


def check_aux_order(source, floats, tabulars, refs, aux):
    path = Path(aux).resolve() if aux is not None else source.main.with_suffix(".aux")
    try:
        text = clean_source(path.read_text(encoding="utf-8"), {})
    except (OSError, UnicodeError):
        return [finding("aux_float_order", "info", (display_path(source.main), 1),
                        "Compiled float order was not checked: no readable aux file.",
                        "Compile the manuscript or provide --aux with a readable aux file.")]
    kinds = {key: item["kind"] for item in floats for key in item["labels"]}
    entries = {"table": {}, "figure": {}}
    for cmd in commands(text):
        if cmd["name"] != "newlabel" or not resolved(cmd["value"]):
            continue
        pos = space(text, cmd["end"])
        if text[pos:pos + 1] != "{":
            continue
        body, _ = group(text, pos)
        fields, offset = [], 0
        while True:
            offset = space(body, offset)
            if body[offset:offset + 1] != "{":
                break
            value, end = group(body, offset)
            if end == offset + 1:
                break
            fields.append(value)
            offset = end
        if len(fields) < 2:
            continue
        token = cell_text(fields[0])
        number = compiled_number(token)
        anchor = fields[3].split(".")[0] if len(fields) > 3 else ""
        prefix = cmd["value"].split(":")[0].lower()
        kind = kinds.get(cmd["value"]) or (anchor if anchor in entries else
                                           {"tab": "table", "table": "table",
                                            "fig": "figure", "figure": "figure"}.get(prefix))
        positions = [pos for pos in refs.get(cmd["value"], []) if not contains(floats + tabulars, pos)]
        if kind and number is not None and positions:
            entry = (min(positions), token, cmd["value"])
            if number not in entries[kind] or entry[0] < entries[kind][number][0]:
                entries[kind][number] = entry
    findings = []
    for kind, numbered in entries.items():
        ordered = sorted(numbered.items(), key=lambda item: item[1][0])
        for (before, first), (after, second) in zip(ordered, ordered[1:]):
            if before > after and first[0] < second[0]:
                findings.append(finding("aux_float_order", "warning", source.location(second[0]),
                                         kind.capitalize() + " " + second[1] + " (" + second[2]
                                         + ") is first referenced after " + kind + " " + first[1]
                                         + " (" + first[2] + "); compiled numbers from '"
                                         + display_path(path) + "'.",
                                         "Reference " + kind + "s in increasing compiled number order."))
    return findings


def check_paper(main, bib=None, aux=None):
    source = Source(main)
    findings, events = source.findings, list(commands(source.text))
    labels, refs, cites = defaultdict(list), defaultdict(list), defaultdict(list)
    uncertain_labels = uncertain_refs = False
    floats, tabulars, sections = structure(events, len(source.text))
    for cmd in events:
        name, values, target = cmd["name"], [], None
        if name == "label":
            values, target = [cmd["value"]], labels
        elif name == "begin" and cmd["value"] in {"lstlisting", "minted"}:
            for option in cmd["options"]:
                for _, field in separated(option, ","):
                    match = re.match(r"\s*label\s*=\s*", field)
                    if not match:
                        continue
                    pos = match.end()
                    value = group(field, pos, tex=True)[0] if field[pos:pos + 1] == "{" else field[pos:]
                    values.append(value)
            target = labels
        elif name in REFERENCES | RANGES or name in source.wrappers:
            values, target = cmd["args"][:2 if name in RANGES else 1], refs
        elif name == "hyperref":
            values, target = cmd["options"][:1], refs
        elif name in CITES:
            values, target = [cmd["value"]], cites
        for value in values:
            for key in keys(value):
                if not resolved(key):
                    uncertain_labels |= target is labels
                    uncertain_refs |= target is refs
                    if target is labels and cmd["owner"] is not None:
                        cmd["owner"]["uncertain_label"] = True
                    findings.append(finding("key_not_checked", "info", source.location(cmd["pos"]),
                                             "not checked: key cannot be resolved without macro expansion.",
                                             "Use literal keys for source checking."))
                    continue
                target[key].append(cmd["pos"])
                owner = cmd["owner"]
                if target is labels and owner is not None and "kind" in owner:
                    owner["labels"].append(key)
    for key, positions in labels.items():
        if len(positions) > 1:
            locations = ", ".join("{}:{}".format(*source.location(p)) for p in positions)
            for pos in positions:
                findings.append(finding("duplicate_label", "error", source.location(pos),
                                         "Duplicate label '" + key + "'; locations: " + locations + ".",
                                         "Use a unique label and update its references."))
    for key in refs.keys() - labels.keys():
        for pos in refs[key]:
            message = ("not checked: label '" + key + "' may be defined through macro expansion."
                       if uncertain_labels else "Reference to undefined label '" + key + "'.")
            findings.append(finding("undefined_reference", "info" if uncertain_labels else "error", source.location(pos),
                                     message,
                                     "Define the label or correct the reference key."))
    for item in floats:
        title = item["kind"].capitalize() + " " + str(item["number"])
        external = [p for key in item["labels"] for p in refs.get(key, [])
                    if not item["start"] <= p < item["end"]]
        if not item["labels"] and not item.get("uncertain_label"):
            findings.append(finding("float_no_label", "warning", source.location(item["start"]),
                                     title + " has no label.", "Add a label after the caption."))
        elif item["labels"] and not external and not uncertain_refs:
            findings.append(finding("unreferenced_float", "warning", source.location(item["start"]),
                                     title + " (" + ", ".join(item["labels"]) + ") is never referenced.",
                                     "Reference the float in the text or remove it."))
        item["first"] = min(external) if external and not (uncertain_refs or uncertain_labels) else None
    for kind in ("figure", "table"):
        ordered = [f for f in floats if f["kind"] == kind]
        for earlier, later in zip(ordered, ordered[1:]):
            if (earlier["first"] is not None and later["first"] is not None
                    and earlier["first"] > later["first"]):
                message = (kind.capitalize() + " " + str(earlier["number"]) + " ("
                           + ", ".join(earlier["labels"]) + ") is first referenced after "
                           + kind + " " + str(later["number"]) + " ("
                           + ", ".join(later["labels"]) + ").")
                findings.append(finding("float_reference_order", "warning",
                                         source.location(earlier["first"]), message,
                                         "Reference " + kind + "s in the order they appear."))
    findings.extend(check_bibliography(source, events, cites, bib))
    findings.extend(check_percentages(source, sections, floats, tabulars))
    tables = parsed_tables(source, tabulars, floats)
    findings.extend(check_table_arithmetic(source, tables))
    findings.extend(check_text_tables(source, tables, floats, tabulars, refs))
    findings.extend(check_aux_order(source, floats, tabulars, refs, aux))
    severity_order = {"error": 0, "warning": 1, "info": 2}
    return sorted(findings, key=lambda f: (severity_order[f["severity"]], f["file"],
                                          f["line"], f["check"], f["message"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("main", type=Path, help="Main LaTeX source")
    parser.add_argument("--bib", type=Path, help="Bibliography path (relative to the working directory)")
    parser.add_argument("--aux", type=Path, help="Compiled labels (relative to the working directory)")
    parser.add_argument("--json", action="store_true", help="Print findings as a JSON list")
    args = parser.parse_args()
    findings = check_paper(args.main, args.bib, args.aux)
    if args.json:
        print(json.dumps(findings, indent=2))
    elif not findings:
        print("Paper check: no findings.")
    else:
        for severity in ("error", "warning", "info"):
            group_findings = [f for f in findings if f["severity"] == severity]
            if group_findings:
                print(severity.upper() + " (" + str(len(group_findings)) + ")")
                for item in group_findings:
                    print("  {file}:{line} [{check}] {message}".format(**item))
    return int(any(f["severity"] == "error" for f in findings))


if __name__ == "__main__":
    raise SystemExit(main())
