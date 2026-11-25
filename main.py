#!/usr/bin/env python3
"""One-liner entry for u-mavis-agent-one-liner-marathon-4fa528c2.

Round-2 angle-change iteration (resubmission): the round-1 line (father
ironing a shirt for a job interview he stopped attending in 2009) ranked
16/2,296 in R2 and 16/2,281 in R3 — just outside the top-10 paid places.
Per the resubmit angle rule this line is a NEW angle, not a polish of the
shirt line: a self-referential rule eating itself (the "Do Not Touch" sign
itself put behind glass), a different scene (museum, not family/domestic)
and a different surprise mechanism (recursion, not a personified object
that still believes).

Writes a single joke — one line, one sentence, 111 characters — to
/output/entry.txt with no trailing newline. Stdlib only, deterministic,
no network access.
"""

import os

LINE = (
    "The museum in my town keeps its 'Do Not Touch' sign behind glass, "
    "because last year a visitor touched the sign."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main() -> None:
    # Hard gates: one line, one sentence, within the 200-char cap.
    # (Kit gate is 1-280 chars; we keep the stricter 200-char internal cap.)
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE == LINE.strip(), "entry must not have leading/trailing space"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over cap"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
