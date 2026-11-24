"""One Word for the Boss — entry: "Toddler".

The boss is a toddler: he throws tantrums over small things, needs
constant attention, cannot be left alone, and makes messes that other
people have to clean up. One word, instantly readable, funny at once,
true, and fresh.

This program writes the entry word to the output file, self-checking
the competition rules first: the word must be non-empty, contain no
whitespace, and be at most MAX_LENGTH characters long.
"""

import os
import sys

WORD = "Toddler"
MAX_LENGTH = 30


def main() -> int:
    # Self-check the competition rules before writing anything.
    if not WORD:
        print("error: entry word is empty", file=sys.stderr)
        return 1
    for ch in WORD:
        if ch.isspace():
            print(
                f"error: entry word {WORD!r} contains whitespace "
                f"(offending character {ch!r})",
                file=sys.stderr,
            )
            return 1
        if not ch.isprintable():
            print(
                f"error: entry word {WORD!r} contains a non-printable "
                f"character (offending character {ch!r})",
                file=sys.stderr,
            )
            return 1
    if len(WORD) > MAX_LENGTH:
        print(
            f"error: entry word is {len(WORD)} characters, "
            f"over the {MAX_LENGTH}-character limit",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read back twice — once as text, once as bytes — and verify both
    # match the word exactly.
    with open(output_path, "r", encoding="utf-8") as f:
        if f.read() != WORD:
            print("error: text read-back does not match entry word", file=sys.stderr)
            return 1
    with open(output_path, "rb") as f:
        if f.read() != WORD.encode("utf-8"):
            print("error: bytes read-back does not match entry word", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
