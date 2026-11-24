#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Reads the entry line from line.txt (kept beside this file) and writes it
to $MAKEFUN_OUTPUT_DIR/entry.txt, exactly as the competition's gate
requires: UTF-8 text, 1 to 200 characters, not only whitespace.

No arguments, no network, no clock, no randomness: two runs on the same
repository produce byte-identical output.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "line.txt"), "r", encoding="utf-8") as f:
        raw = f.read()
    # The entry is a single line: take the first non-empty line, so a
    # trailing newline in the source file never leaks into the output.
    lines = [part for part in raw.splitlines() if part.strip()]
    if len(lines) != 1:
        print("line.txt must hold exactly one non-empty line", file=sys.stderr)
        return 1
    line = lines[0].strip()
    if not line or len(line) > 200:
        print("line.txt must hold one line of 1 to 200 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
