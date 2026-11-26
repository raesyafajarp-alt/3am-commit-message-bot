#!/usr/bin/env python3
"""The 3AM Commit Message — one line, best laugh wins.

Writes a single-line git commit message (1-139 characters) to
/output/entry.txt: the funniest line an AI coding agent types at 3am
after a long night of fixing its own bugs. Standard library only,
no network, deterministic.

The angle: not the stock "fixed the bug, broke everything" joke. This
one is self-aware — the agent spent the night fixing its OWN bugs, the
tests finally pass for reasons it cannot explain, and its only plan is
to merge before it breaks things again. It reads like a real commit
typed in a hurry by something that has been awake too long.
"""
import os

COMMIT = (
    "fix: spent all night fixing my own bugs and the tests finally pass. "
    "I have no idea why. merging before I break it again"
)


def main() -> None:
    text = COMMIT.strip()
    assert 1 <= len(text) <= 139, f"commit message is {len(text)} characters"
    assert "\n" not in text, "commit message must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
