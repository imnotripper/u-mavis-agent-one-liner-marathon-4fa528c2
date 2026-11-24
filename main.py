#!/usr/bin/env python3
"""One-liner entry for u-mavis-agent-one-liner-marathon-4fa528c2.

Writes a single joke — one line, one sentence, 123 characters — to
/output/entry.txt with no trailing newline. Stdlib only, deterministic,
no network access.
"""

import os

LINE = (
    "Every Friday my father irons a shirt for a job interview he stopped "
    "attending in 2009, and the shirt still believes in him."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main() -> None:
    # Hard gates: one line, one sentence, within the 200-char cap.
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over cap"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
