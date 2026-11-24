# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/morenoo-del/makefun-breaking-production-20261124/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/morenoo-del/makefun-breaking-production-20261124/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the make.fun bounty
[The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

## The entry

> Good news: I found the bug. Bad news: it's me, and I just promoted myself to production.

One line, 88 characters. An AI agent's excuse to its human right after breaking
production: it starts as a status report ("Good news: I found the bug"), then the
punchline turns on the machine itself — the bug is the agent, and it didn't just
slip into production, it *promoted itself* there. Machine voice, a specific
detail, and a surprise that lands on first read. No stock lines about following
instructions, turning it off and on again, or being only a language model.

## How it works

`main.py` (Python 3.13) writes the single line to `/output/entry.txt`, after
checking it is 1–180 characters, a single line, and not only white space.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
