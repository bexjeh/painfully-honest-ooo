"""Painfully Honest Out-of-Office: write one honest auto-reply to entry.txt."""

import os

REPLY = (
    "I'm away until Monday, and this auto-reply is doing the saying no for me, "
    "since I've never once managed it in person \u2014 thank you for your "
    "patience, and I'll reply when I'm back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Write the reply exactly, with no trailing newline: the gate counts
    # every character in the file, so the file is the sentence and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
