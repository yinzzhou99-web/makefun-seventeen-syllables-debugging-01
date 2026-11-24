#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Stdlib only. Clears only the children of the output directory, never
the directory itself (the grader mounts it).
"""

import os
import sys

HAIKU = (
    "Breakpoint holds its breath\n"
    "the cursor blinks past midnight\n"
    "the bug: it was me\n"
)


def _clear_children(out_dir: str) -> None:
    """Remove everything inside out_dir, recursively, without touching it."""
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            _clear_children(path)
            os.rmdir(path)
        else:
            os.remove(path)


def _check(text: str) -> None:
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 3 or not all(line.strip() for line in lines):
        raise ValueError("haiku must be exactly three non-empty lines")
    if not 1 <= len(text) <= 200:
        raise ValueError("haiku must be 1-200 characters")


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    _clear_children(out_dir)
    _check(HAIKU)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)
    return 0


if __name__ == "__main__":
    sys.exit(main())
