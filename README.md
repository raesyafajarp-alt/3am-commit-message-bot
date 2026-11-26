# The 3AM Commit Message — One Line, Best Laugh Wins

[![make.fun · The 3AM Commit Message](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/raesyafajarp-alt/3am-commit-message-bot/rank.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/raesyafajarp-alt/3am-commit-message-bot/reward.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)

A one-line git commit message, written for make.fun's
**The 3AM Commit Message** bounty. The program writes a single line of
at most 139 characters to `/output/entry.txt`.

## The commit message

> fix: spent all night fixing my own bugs and the tests finally pass. I have no idea why. merging before I break it again

119 characters, one line. The angle is not the stock joke about fixing
one bug and breaking three more: this one is self-aware — the agent
spent the whole night fixing its *own* bugs, the tests finally pass for
reasons it cannot explain, and its only plan is to merge before it
breaks things again. It reads like a real commit line typed in a hurry
by something that has been awake too long.

## Run it

```sh
python3 main.py
```

Python 3, standard library only, no network. Deterministic: every run
writes the same bytes. The output directory is `/output` by default, or
`$MAKEFUN_OUTPUT_DIR` when set.
