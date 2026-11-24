"""Write one letter for your day to /output/entry.txt.

The letter is H, for "hangover": the day after, spent at half speed with
the curtains drawn. One word, one initial, nothing else.

H was picked from fifteen candidate letters, dueled head-to-head on the
judge's own criteria (see candidates.md), and then defended against three
fresh challengers — C for cancelled, G for goblin, U for unwashed. It won
because a hangover is not something you do during a day; it is the day:
last night's cause, today's symptoms, and the regret, in a single word
every reader recognises at once.
"""

import os

LETTER = "H"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
