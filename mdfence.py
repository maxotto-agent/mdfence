#!/usr/bin/env python3
"""mdfence: lint fenced code blocks in Markdown (unclosed fences, missing language)."""
import argparse
import re
import sys

FENCE = re.compile(r"^( {0,3})(`{3,}|~{3,})\s*([^`\s]*)[^`]*$")


def lint(text, require_lang=False):
    """Return a list of (line_number, message)."""
    problems = []
    open_fence = None  # (char, length, line)
    for n, line in enumerate(text.splitlines(), 1):
        m = FENCE.match(line)
        if not m:
            continue
        marks, info = m.group(2), m.group(3)
        if open_fence is None:
            open_fence = (marks[0], len(marks), n)
            if require_lang and not info:
                problems.append((n, "code fence has no language"))
        elif marks[0] == open_fence[0] and len(marks) >= open_fence[1] and not info:
            open_fence = None
    if open_fence:
        problems.append((open_fence[2], "unclosed code fence"))
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--require-lang", action="store_true",
                    help="flag opening fences without a language tag")
    args = ap.parse_args(argv)
    bad = 0
    for path in args.files:
        with open(path, encoding="utf-8") as f:
            for n, msg in lint(f.read(), args.require_lang):
                print(f"{path}:{n}: {msg}")
                bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
