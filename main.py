#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry "A" (coffee).

The gate requires /output/entry.txt to hold exactly one character,
so this program writes a single byte, "A", and nothing else:
no newline, no word, no explanation, no punctuation.

"A" names coffee. Coffee is the bolder, more vivid, truer pick in the
coffee-against-tea argument: the house's standing answer.
"""

import os

LETTER = "A"  # A for coffee.


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path) or "."
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Self-check the gate: the file must hold exactly one character,
    # the chosen letter, and nothing else.
    with open(path, "rb") as f:
        written = f.read()
    assert written == LETTER.encode("utf-8"), (
        "gate violated: entry.txt holds %r, expected exactly %r"
        % (written, LETTER.encode("utf-8"))
    )


if __name__ == "__main__":
    main()
