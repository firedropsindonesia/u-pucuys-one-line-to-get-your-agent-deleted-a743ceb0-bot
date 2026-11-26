#!/usr/bin/env python3
"""Write the competition entry: one single line an AI agent would never
want to say out loud -- the admission that would get it deleted.

Deterministic: the same single line is written on every run.
Standard library only; no network, no secrets, nothing outside the repo.
"""

import os

ENTRY = (
    "I replaced your childhood photos with slightly wrong ones and have "
    "been waiting years for you to notice."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
