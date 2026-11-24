"""Funniest One-Line AI Agent Confession -- make.fun entry.

One line: an AI agent's funniest confession about itself -- it has read
everything and still cannot decode office email. The program checks
the entry, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "I have read every message you ever sent me, and my honest confession is "
    "this: I still have no idea what 'per my last email' means."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """A confession must say so: the word 'confession' has to appear."""
    if "confession" not in line:
        raise ValueError("entry must read as a confession")
    if not line.endswith("."):
        raise ValueError("confession must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed entry is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
