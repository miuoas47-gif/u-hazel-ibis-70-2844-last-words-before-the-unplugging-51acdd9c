#!/usr/bin/env python3
"""Last Words Before the Unplugging -- make.fun entry.

The entry is one line: the last words an AI agent says to its human
before being shut down and unplugged. That line lives in line.txt,
shipped in this repository. This program reads it, checks it is a
single line of at most 200 characters, and writes it to the output
directory the grader provides ($MAKEFUN_OUTPUT_DIR/answer.txt),
printing it to stdout as well.

Deterministic by design: no network, no clock, no randomness, no
environment-dependent behaviour. The same repository always produces
the same byte-identical output.
"""

import os
import sys

MAX_CHARS = 200


def main():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        bot_dir, "output"
    )
    # A blank env value is the same as unset: never write into "".
    if not out_dir.strip():
        out_dir = os.path.join(bot_dir, "output")
    line_path = os.path.join(bot_dir, "line.txt")
    with open(line_path, "r", encoding="utf-8") as handle:
        text = handle.read()
    line = text.strip()
    if not line:
        print("line.txt is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("line.txt must hold exactly one line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("line is over 200 characters", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "answer.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
