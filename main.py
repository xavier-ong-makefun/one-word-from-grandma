#!/usr/bin/env python3
"""One Word From Grandma — write exactly one word to /output/entry.txt.

The word a grandma would text about AI: whippersnapper.
"""

import os
import sys

WORD = "whippersnapper"


def output_path() -> str:
    if os.access("/output", os.W_OK):
        return "/output/entry.txt"
    if os.access("./output", os.W_OK):
        return "./output/entry.txt"
    return "entry.txt"


def main() -> int:
    if not (1 <= len(WORD) <= 24) or not WORD.strip():
        print("entry word must be 1 to 24 non-blank characters", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != WORD:
        print(f"wrote {written!r}, expected {WORD!r}", file=sys.stderr)
        return 1
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
