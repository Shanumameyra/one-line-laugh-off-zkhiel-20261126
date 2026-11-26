#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes a single original joke line to entry.txt (and to /output/entry.txt
when the harness mounts it). Deterministic, no network, no randomness.
"""

import os

# The joke: one line, 91 characters, original.
JOKE = "I told my toddler babies come from the cloud. Now she asks Alexa for a little brother."


def main() -> None:
    text = JOKE + "\n"
    # Always write next to this script (local / repo copy).
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Also write where the harness reads it, when mounted.
    if os.path.isdir("/output"):
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()