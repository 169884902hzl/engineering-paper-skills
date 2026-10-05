#!/usr/bin/env python3
"""Run deterministic consistency checks against invented LaTeX projects."""

import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills/engineering-validation/scripts/paper_check.py"
FIXTURES = "tests/fixtures/"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def run(fixture, *extra):
    result = subprocess.run(
        [sys.executable, str(CHECKER), FIXTURES + fixture + "/main.tex", "--json", *extra],
        cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    require(not result.stderr, "Checker wrote to stderr: " + result.stderr)
    try:
        findings = json.loads(result.stdout)
    except ValueError:
        raise AssertionError("Checker did not return JSON: " + result.stdout)
    require(isinstance(findings, list), "JSON findings must be a list")
    for item in findings:
        require(set(item) == {"check", "severity", "file", "line", "message"},
                "Unexpected JSON schema: " + str(item))
        require(isinstance(item["line"], int) and item["line"] >= 1,
                "Finding has no valid source line: " + str(item))
        require("Fix: " in item["message"], "Finding has no fix hint: " + str(item))
    require(result.returncode == int(any(f["severity"] == "error" for f in findings)),
            "Exit status must be 1 exactly when an error is present")
    return result.returncode, findings


def check_fixtures():
    status, findings = run("paper_check")
    require(status == 1, "Flawed fixture must exit 1")
    expected = [
        ("duplicate_label", "error", "sections/introduction.tex", 2, "sec:shared"),
        ("duplicate_label", "error", "sections/method.tex", 2, "sec:shared"),
        ("undefined_reference", "error", "sections/introduction.tex", 4, "sec:absent"),
        ("missing_citation", "error", "sections/introduction.tex", 3, "missing_robot_study"),
        ("unreferenced_float", "warning", "sections/design.tex", 7, "fig:unused"),
        ("float_reference_order", "warning", "sections/experiments.tex", 4, "tab:outcomes"),
        ("trial_granularity", "warning", "tables/outcomes.tex", 6, "N=10"),
        ("uncited_bib_entry", "info", "refs.bib", 8, "unused_grasp_note"),
        ("prose_percentage_not_tabulated", "info", "sections/experiments.tex", 5, "80%"),
    ]
    expected_locations = Counter((c, s, FIXTURES + "paper_check/" + f, n)
                                 for c, s, f, n, _ in expected)
    actual = Counter((f["check"], f["severity"], f["file"], f["line"]) for f in findings)
    require(actual == expected_locations,
            "Unexpected fixture findings:\nExpected: " + str(expected_locations) + "\nActual: " + str(actual))
    for check, severity, file, line, token in expected:
        require(any(f["check"] == check and f["file"] == FIXTURES + "paper_check/" + file
                    and f["line"] == line and token in f["message"] for f in findings),
                "Missing finding detail: " + check + " " + token)
    status, clean = run("paper_check_clean")
    require(status == 0 and not clean, "Clean fixture must have no findings: " + str(clean))
    status, explicit = run("paper_check", "--bib", FIXTURES + "paper_check/refs.bib")
    require(status == 1 and explicit == findings, "Explicit bibliography changed fixture findings")


def check_edge_cases():
    # Load without leaving interpreter cache files in the skill directory.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("paper_check", CHECKER)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)

    def virtual(files):
        root = Path("virtual-paper").resolve()
        def read(path, **kwargs):
            name = path.relative_to(root).as_posix()
            if name not in files:
                raise FileNotFoundError(name)
            return files[name]
        with patch.object(Path, "read_text", read):
            return checker.check_paper(root / "main.tex")

    sample = r"""\section{Experiments}
Each object received three independent trials.
\input{sections/details}
\bibliography{refs}
"""
    details = r"""\subsection{Measurements}
See \cref{fig:first,tab:second}, \eqref{eq:valid}, and \citet[see][p. 2]{a,b}.
\begin{figure}\caption{Diagram}\label{fig:first}\end{figure}
\begin{table}\label{tab:second}\begin{tabular}{r}66.7\%\end{tabular}\end{table}
\label{eq:valid}
Observed success was 66.7\%. % Ignore 65\% and \ref{absent}.
"""
    findings = virtual({"main.tex": sample, "sections/details.tex": details,
                        "refs.bib": "@article{a, title={Invented A}}\n@article{b, title={Invented B}}"})
    require(not findings, "Nested sections, rounding, or optional citations failed: " + str(findings))
    for token, count in checker.WORDS.items():
        match = checker.TRIALS.search("Each condition used " + token + " repeated trials.")
        require(match and checker.WORDS[match.group(1)] == count,
                "Number word was not recognized: " + token)
    require(checker.TRIALS.search("Measured over 20 runs"), "Run-count pattern was not recognized")
    require(not checker.possible_percentage(65, 10), "65% must be impossible for ten trials")
    require(checker.possible_percentage(66.7, 3), "One-decimal trial rounding failed")

    bare = virtual({"main.tex": "\\section{Results}\n10 trials.\nSuccess was 65%.\n"})
    require(not any(f["check"] in {"trial_granularity", "prose_percentage_not_tabulated"}
                    for f in bare), "A TeX comment was treated as a percentage")
    require(any(f["check"] == "bibliography_skipped" for f in bare), "Missing bibliography was not reported")
    require(not any(f["severity"] == "error" for f in bare), "Warning-only document produced errors")
    no_label = virtual({"main.tex": "\\begin{figure*}\nDiagram.\n\\end{figure*}\n"})
    require(any(f["check"] == "float_no_label" and f["line"] == 1 for f in no_label),
            "Float without a label was not reported")
    cycle = virtual({"main.tex": "\\input{sections/loop}\n",
                     "sections/loop.tex": "\\input{main}\n"})
    require(any(f["check"] == "include_cycle" and f["file"].endswith("sections/loop.tex")
                and f["line"] == 1 for f in cycle), "Include cycle was not located")
    missing = virtual({"main.tex": "\\input{missing}\n"})
    require(any(f["check"] == "source_unreadable" and f["line"] == 1
                and f["severity"] == "info" and "not checked" in f["message"] for f in missing),
            "Missing source was not reported")


def check_regressions():
    """Each numbered review fix has a checked, on-disk regression project."""
    def expect(case, expected, *extra):
        _, findings = run("paper_check_edge/" + case, *extra)
        actual = Counter((f["check"], f["severity"], f["line"]) for f in findings)
        wanted = Counter((check, severity, line) for check, severity, line, _ in expected)
        require(actual == wanted, case + " findings differ: " + str(findings))
        for check, severity, line, token in expected:
            require(any(f["check"] == check and f["severity"] == severity
                        and f["line"] == line and token in f["message"] for f in findings),
                    case + " missing detail: " + token)

    # 1: All six definition forms and parameter keys are inert; a simple wrapper works.
    expect("01_macros", [])
    expect("01_macros/dynamic", [("key_not_checked", "info", 2, "not checked"),
                                 ("key_not_checked", "info", 2, "not checked"),
                                 ("undefined_reference", "info", 2, "not checked"),
                                 ("key_not_checked", "info", 3, "not checked"),
                                 ("undefined_reference", "info", 4, "not checked")])
    # 2: All five literal environments, inline literals and nested false blocks are inert.
    expect("02_literals", [])
    # 3: Following groups survive; both bare filename forms expand; external inputs are info.
    expect("03_inputs", [("source_unreadable", "info", 6, "not checked: input not found locally"),
                         ("input_not_checked", "info", 7, "not checked")])
    # 4: Distinct entries prove every whitelisted command is recognized; fields are not keys.
    expect("04_citations", [("missing_citation", "error", 7, "missing_field")])
    expect("04_citations/nocite", [])
    # 5: A percent-encoded URL cannot hide the later entries; non-entry types are skipped.
    expect("05_bib", [])
    # 6: Declared and explicit missing/unreadable files fail; only undeclared files skip.
    unavailable = [("bibliography_unavailable", "error", 1, "Cannot read bibliography")]
    expect("06_missing_bib", unavailable)
    expect("06_missing_bib/resource", unavailable)
    expect("06_missing_bib/undeclared", [("bibliography_skipped", "info", 1, "no bibliography")])
    expect("06_missing_bib/undeclared", unavailable, "--bib",
           FIXTURES + "paper_check_edge/06_missing_bib/absent.bib")
    expect("06_missing_bib/undeclared", unavailable, "--bib",
           FIXTURES + "paper_check_edge/06_missing_bib")
    # 7: Undefined keys prove recognition, including both range endpoints; listing keys resolve.
    refs = [(1, "vref"), (1, "Vref"), (1, "cpageref"), (2, "Cpageref"),
            (2, "labelcref"), (2, "nameref"), (3, "autoref"), (3, "subref"), (4, "hyperref")]
    refs += [(line, name + ":" + endpoint) for line, name in
             [(5, "crefrange"), (6, "Crefrange"), (7, "cpagerefrange")]
             for endpoint in ("first", "last")]
    expect("07_references", [("undefined_reference", "error", line, "'missing:" + name + "'")
                             for line, name in refs])
    # 8: Equation labels stay with equations, while three subfigure forms credit the parent.
    expect("08_attribution", [("float_no_label", "warning", 3, "Figure 1"),
                              ("unreferenced_float", "warning", 13, "fig:unreferenced")])
    # 9: Self-citations do not count; another caption affects both usage and reference order.
    expect("09_caption_refs", [("unreferenced_float", "warning", 1, "fig:self"),
                               ("float_reference_order", "warning", 8, "fig:a")])
    # 10: Only escaped and siunitx percentages count; comments and values over 100 do not.
    expect("10_percentages", [("trial_granularity", "warning", line, "N=10")
                              for line in (4, 5, 6, 7)])
    # 11: Success context, caption/nearest/parent precedence, ambiguity and exact precision.
    expect("11_granularity", [
        ("trial_granularity", "warning", 8, "N=25"),
        ("trial_granularity", "warning", 16, "N=10"),
        ("trial_granularity", "warning", 19, "N=10"),
        ("trial_granularity", "warning", 32, "12%"),
        ("trial_granularity", "warning", 36, "66%"),
        ("trial_granularity", "warning", 36, "66.66%"),
        ("trial_granularity", "warning", 36, "66.70%"),
        ("trial_granularity", "info", 23, "ambiguous trial count"),
        ("trial_granularity", "info", 27, "ambiguous trial count"),
    ])
    # 12: Numeric cells inherit percent units only in their column; unknown units skip claims.
    expect("12_table_units", [("prose_percentage_not_tabulated", "info", 2, "63%"),
                              ("prose_percentage_not_tabulated", "info", 2, "20%")])
    expect("12_table_units/unknown", [])
    # 13: Explicit group totals are checked; other aggregates need a denominator.
    expect("13_aggregation", [
        ("trial_granularity", "warning", 4, "N=50"),
        ("trial_granularity", "info", 6, "aggregated value; trial granularity not checked"),
        ("trial_granularity", "warning", 10, "N=50"),
        ("trial_granularity", "info", 13, "aggregated value; trial granularity not checked"),
        ("trial_granularity", "warning", 16, "N=50"),
        ("trial_granularity", "warning", 18, "N=50"),
        ("trial_granularity", "warning", 20, "N=10"),
        ("trial_granularity", "warning", 22, "N=10"),
        ("trial_granularity", "info", 24, "aggregated value; trial granularity not checked"),
    ])


def main():
    try:
        check_fixtures()
        check_edge_cases()
        check_regressions()
    except (AssertionError, OSError, ValueError) as exc:
        print("Paper check tests failed: " + str(exc), file=sys.stderr)
        return 1
    print("Paper check tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
