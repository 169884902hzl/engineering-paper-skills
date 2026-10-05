#!/usr/bin/env python3
"""Find private wording and distinctive terms in public repository text."""

import sys

sys.dont_write_bytecode = True

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {
    ".bib", ".bst", ".cfg", ".cls", ".css", ".csv", ".html", ".ini",
    ".js", ".json", ".jsonl", ".jsx", ".markdown", ".md", ".mdx",
    ".py", ".rst", ".sh", ".sql", ".sty", ".svg", ".tex", ".text",
    ".toml", ".ts", ".tsx", ".tsv", ".txt", ".xml", ".yaml", ".yml",
}
WORDS = re.compile(r"[^\W_]+", re.UNICODE)
LATEX_COMMANDS = re.compile(
    r"\\(?:begin|end)\s*\{[^{}]*\}|\\(?:[A-Za-z@]+\*?|[^\w\s])"
)
MARKDOWN_SYNTAX = (
    re.compile(r"(?<=\])\([^\n)]*\)"),
    re.compile(r"(?<=\])\[[^\]\n]*\]"),
    re.compile(r"(?m)^[ \t]*(?:`{3,}|~{3,})[^\n]*"),
    re.compile(r"</?[A-Za-z][\w:-]*(?:\s+[^>\n]*)?\s*/?>"),
)


class ScanError(Exception):
    """A failure with a message safe to display without input paths."""


def mask_syntax(match):
    """Remove syntax while keeping newline positions intact."""
    return re.sub(r"[^\n]", " ", match.group(0))


def tokenize(text):
    """Return lowercase alphanumeric words with their original line numbers."""
    text = LATEX_COMMANDS.sub(mask_syntax, text)
    for pattern in MARKDOWN_SYNTAX:
        text = pattern.sub(mask_syntax, text)
    tokens = []
    line = 1
    previous_end = 0
    for match in WORDS.finditer(text):
        line += text.count("\n", previous_end, match.start())
        tokens.append((match.group(0).lower(), line))
        previous_end = match.end()
    return tokens


def read_input(path, role):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        raise ScanError("Unable to read a {} input.".format(role)) from None


def read_private(path):
    if path.suffix.lower() != ".pdf":
        return read_input(path, "private")
    converter = shutil.which("pdftotext")
    if converter is None:
        print("Warning: skipped a private PDF; pdftotext is unavailable.",
              file=sys.stderr)
        return ""
    try:
        result = subprocess.run(
            [converter, "-enc", "UTF-8", str(path), "-"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
    except OSError:
        raise ScanError("Unable to extract a private PDF.") from None
    if result.returncode:
        raise ScanError("Unable to extract a private PDF.")
    return result.stdout.decode("utf-8", errors="replace")


def read_phrases(path, role):
    """Map normalized phrases to their spelling in a one-phrase-per-line file."""
    phrases = {}
    if path is not None:
        for line in read_input(path, role).splitlines():
            words = tuple(word for word, _ in tokenize(line))
            if words:
                phrases[words] = line.strip()
    return phrases


def phrase_spans(words, phrases):
    """Yield word intervals that match any of the supplied token tuples."""
    for size in sorted({len(phrase) for phrase in phrases}):
        for start in range(len(words) - size + 1):
            phrase = tuple(words[start:start + size])
            if phrase in phrases:
                yield start, start + size, phrase


def repo_files(paths, excluded):
    if paths is None:
        try:
            result = subprocess.run(
                ["git", "-C", str(ROOT), "ls-files", "--cached", "--others",
                 "--exclude-standard", "-z"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            )
        except OSError:
            raise ScanError("Unable to list repository files with Git.") from None
        if result.returncode:
            raise ScanError("Unable to list repository files with Git.")
        candidates = [ROOT / name.decode(sys.getfilesystemencoding(),
                                        errors="surrogateescape")
                      for name in result.stdout.split(b"\0") if name]
    else:
        candidates = []
        for value in paths:
            path = Path(value).resolve()
            if ROOT not in path.parents and path != ROOT:
                raise ScanError("Scan paths must be inside the repository.")
            if not path.exists():
                raise ScanError("A requested scan path does not exist.")
            candidates.extend(path.rglob("*") if path.is_dir() else [path])

    selected = set()
    for candidate in candidates:
        path = candidate.resolve()
        if path in excluded or ROOT not in path.parents:
            continue
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        # Deleted tracked files and directories are not part of the working text.
        if path.is_file():
            selected.add(path)
    return sorted(selected)


def scan(args):
    private_paths = [Path(value).resolve() for value in args.private]
    terms_path = Path(args.terms).resolve() if args.terms else None
    allow_path = Path(args.allow).resolve() if args.allow else None
    excluded = set(private_paths)
    excluded.update(path for path in (terms_path, allow_path) if path is not None)

    private_ngrams = set()
    for path in private_paths:
        words = [word for word, _ in tokenize(read_private(path))]
        for start in range(len(words) - args.n + 1):
            private_ngrams.add(tuple(words[start:start + args.n]))
    terms = read_phrases(terms_path, "terms")
    allowed = read_phrases(allow_path, "allow-list")

    hits = set()
    for path in repo_files(args.paths, excluded):
        text = read_input(path, "repository")
        if "\0" in text:
            continue
        tokens = tokenize(text)
        words = [word for word, _ in tokens]
        allowed_spans = [(start, end) for start, end, _
                         in phrase_spans(words, allowed)]
        for kind, phrases in (("ngram", private_ngrams), ("term", terms)):
            for start, end, phrase in phrase_spans(words, phrases):
                # A longer allowed phrase also covers the n-grams within it.
                if any(left <= start and end <= right
                       for left, right in allowed_spans):
                    continue
                match = " ".join(phrase) if kind == "ngram" else terms[phrase]
                hits.add((path.relative_to(ROOT).as_posix(), tokens[start][1],
                          kind, match))
    return [{"file": file, "line": line, "kind": kind, "match": match}
            for file, line, kind, match in sorted(hits)]


def positive_integer(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("n must be a positive integer") from None
    if number < 1:
        raise argparse.ArgumentTypeError("n must be a positive integer")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--private", nargs="+", required=True, metavar="FILE",
                        help="private text or PDF files (never listed in output)")
    parser.add_argument("--terms", metavar="TERMSFILE",
                        help="distinctive terms, one per line")
    parser.add_argument("--n", type=positive_integer, default=6,
                        help="word count per n-gram (default: 6)")
    parser.add_argument("--paths", nargs="+", metavar="PATH",
                        help="repository files or directories to scan")
    parser.add_argument("--allow", metavar="PHRASEFILE",
                        help="allowed phrases or terms, one per line")
    parser.add_argument("--json", action="store_true",
                        help="print a JSON list instead of file:line diagnostics")
    args = parser.parse_args(argv)
    try:
        hits = scan(args)
    except ScanError as exc:
        print("Error: {}".format(exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(hits, ensure_ascii=True, indent=2))
    else:
        for hit in hits:
            print("{file}:{line}: {kind}: {match}".format(**hit))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
