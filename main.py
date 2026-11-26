#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review a dog gives the mailman to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = "One star. He shoves bills through my slot at 7 a.m., ignores my bark, and has the nerve to leave \u2014 zero treats, zero belly rubs, would not recommend."


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
