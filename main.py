"""Painfully honest out-of-office auto-reply.

Writes a single one-sentence auto-reply to entry.txt under the
output directory named by MAKEFUN_OUTPUT_DIR (falling back to
/output, then to a local output directory), and prints it.
Standard library only; deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm away until Monday, and your email joins 412 unread messages "
    "I was already ignoring before I left \u2014 if it's urgent, please "
    "call Sara, who answers faster than I do."
)


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path("output")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert text.count("\n") == 0
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
