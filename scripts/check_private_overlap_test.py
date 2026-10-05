#!/usr/bin/env python3
"""Exercise private-overlap diagnostics using entirely invented material."""

import sys

sys.dont_write_bytecode = True

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/private_overlap"
TOOL = ROOT / "scripts/check_private_overlap.py"
PRIVATE = FIXTURES / "private.txt"
PUBLIC = FIXTURES / "repo_like.md"
CLEAN = FIXTURES / "clean.md"
TERMS = FIXTURES / "terms.txt"
ALLOW = FIXTURES / "allow.txt"
PUBLIC_NAME = PUBLIC.relative_to(ROOT).as_posix()
PHRASE = "silent lanterns trace curved paths beyond midnight"


def run(*options):
    return subprocess.run(
        [sys.executable, str(TOOL), "--private", str(PRIVATE),
         "--terms", str(TERMS)] + list(options),
        cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True, check=False,
    )


def main():
    result = run("--paths", str(PUBLIC), str(CLEAN), "--json")
    assert result.returncode == 1, (result.returncode, result.stderr)
    expected = [
        {"file": PUBLIC_NAME, "line": 3, "kind": "ngram",
         "match": "lanterns trace curved paths beyond midnight"},
        {"file": PUBLIC_NAME, "line": 3, "kind": "ngram",
         "match": "silent lanterns trace curved paths beyond"},
        {"file": PUBLIC_NAME, "line": 5, "kind": "term",
         "match": "VelvetCompass"},
    ]
    assert json.loads(result.stdout) == expected, result.stdout
    assert result.stderr == "", result.stderr

    result = run("--n", "7", "--paths", str(PUBLIC), str(CLEAN), "--json")
    assert result.returncode == 1, result.stderr
    assert json.loads(result.stdout) == [
        {"file": PUBLIC_NAME, "line": 3, "kind": "ngram", "match": PHRASE},
        expected[-1],
    ], result.stdout

    result = run("--paths", str(CLEAN), "--json")
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == [], result.stdout

    result = run("--paths", str(FIXTURES), "--allow", str(ALLOW), "--json")
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == [], result.stdout

    # Allowing only the term still reports the copied wording.
    result = run("--paths", str(PUBLIC), str(CLEAN),
                 "--allow", str(TERMS), "--json")
    assert result.returncode == 1, result.stderr
    assert json.loads(result.stdout) == expected[:-1], result.stdout

    result = run("--paths", str(PUBLIC), str(CLEAN))
    assert result.returncode == 1, result.stderr
    assert result.stdout == "".join(
        "{file}:{line}: {kind}: {match}\n".format(**hit) for hit in expected
    ), result.stdout
    assert str(PRIVATE) not in result.stdout, result.stdout
    assert PRIVATE.name not in result.stdout, result.stdout
    assert "Keep this source sentence" not in result.stdout, result.stdout

    result = run("--n", "0", "--paths", str(CLEAN), "--json")
    assert result.returncode == 2, result.returncode
    assert result.stdout == "", result.stdout
    assert str(PRIVATE) not in result.stderr, result.stderr

    print("Private overlap tests passed.")


if __name__ == "__main__":
    main()
