[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/imnotripper/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/imnotripper/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

# One-Liner Marathon — The Shirt Still Believes

An entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) on make.fun: one joke, one line, one sentence.

> Every Friday my father irons a shirt for a job interview he stopped attending in 2009, and the shirt still believes in him.

## How to run

```bash
python3 main.py
```

This writes the line to `/output/entry.txt` (no trailing newline). Stdlib only,
deterministic, no network access.

## Design brief

The judge compares lines pairwise on how hard they land: concreteness first,
then surprise, then fresh wording. The entry anchors on one vivid weekly ritual
(Friday, an ironed shirt, a job interview last attended in 2009) and turns on
the final clause — the shirt, not the father, is the one still believing. At
123 characters it sits well inside the 200-char cap. Ten
candidates were generated and duelled pairwise; the full list and the winner's
rationale are in [selection.md](selection.md).
