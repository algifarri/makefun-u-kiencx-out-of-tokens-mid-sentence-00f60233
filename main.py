# SPDX-License-Identifier: MIT
"""Entry for make.fun: Out of Tokens, Mid-Sentence.

Writes one line (at most 140 characters): the error message an AI
agent shows when it runs out of tokens mid-sentence, to
/output/entry.txt. Deterministic: no randomness, no network, no input.

The joke: a flat, authentic-looking error code ("Error 402") opens
the line, then the agent confesses it was one token away from the
punchline -- and the turn lands on the punchline having been
"refunded", as if a joke were a purchase returned to the void. No
stock apology, no plain "I got cut off": the humour is the agent
treating its own lost punchline as a transaction that got reversed.
The line is 121 characters (verified by the assertion in main),
inside the 1-140 gate.
"""

import os

ENTRY = "Error 402: token budget exhausted mid-sentence. I was one token away from the punchline. The punchline has been refunded."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must fit the 140-character gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
