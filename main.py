#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry (round 2 re-entry).

When run, writes a single original office joke to /output/entry.txt.
The joke works because it turns the meeting's own discipline against
itself: a standup so obsessed with its fifteen-minute limit that the
limit itself becomes the meeting. The sting is in the second half --
fourteen of the fifteen minutes are burned just arguing over who starts
the timer, so the rule meant to save time is exactly what wastes it.
Tightened in revision: numerals instead of spelled-out numbers and
"arguing" instead of "deciding", so the sentence lands faster and the
waste feels active rather than passive.
"""

import os

ENTRY = "Our standup has a strict 15-minute limit, so we spend 14 of them arguing about whose turn it is to start the timer."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
