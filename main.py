"""Worst Monday one-liner for make.fun's Worst Monday One-Liners bounty.

The program writes a single original joke about an AI agent's worst
Monday to /output/entry.txt and nothing else. The line is one sentence
of plain UTF-8 text with no trailing newline, so the sealed gate scorer
sees exactly one line of 1 to 140 characters.

The joke stacks three concrete Monday miseries and lands on a twist:
the stand-up should have been a message, the deploy died at 9 a.m.,
and by lunch the humans are asking the agent the one question it
never expected to hear aimed at itself -- whether it tried turning
itself off and on again. The punchline flips the classic IT support
line back onto the machine.
"""

import os

LINE = (
    "Stand-up should've been a message, the deploy died at 9 a.m., "
    "and by lunch the humans asked if I'd tried turning myself off "
    "and on again."
)

OUTPUT_PATH = "/output/entry.txt"

# The bounty caps the line at 140 characters; keep the cap in one named
# place so the validation below and the docstring above cannot drift apart.
MAX_CHARS = 140


def write_entry() -> str:
    """Write the one-liner to the output file and return what was written."""
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit("line must be 1 to 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the one-liner")
    return written


def main() -> None:
    written = write_entry()
    print(written)
    print(f"({len(written)} characters, one line, no trailing newline)")


if __name__ == "__main__":
    main()
