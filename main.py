#!/usr/bin/env python3
"""Entry for make.fun competition u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one letter to entry.txt in the output directory: "D".

Why D: the word behind it is "doomscrolling" -- thumbing an endless feed
in the small hours, phone glow on your face, one more swipe and then
sleep. It is vivid (a sharp picture, not a vague mood), funny (everyone
recognises it at once), and true to a real day in 2026. D is the
letter's own initial, and it is not one of the brief's obvious examples
(A for amazing, F for Friday-feeling, Z for zero sleep) -- a sharper,
fresher pick for the same game.

Pure standard library, deterministic, no network.
"""

import hashlib
import os

LETTER = "D"

FILENAME = "entry.txt"


def write_and_verify(letter: str, out_dir: str) -> tuple[str, str]:
    """Write the single letter to entry.txt in out_dir, then re-read and verify.

    Returns (path, sha256 hex digest) of the written file.
    """
    data = letter.encode("utf-8")
    data.decode("utf-8")  # validate UTF-8 round-trip

    path = os.path.join(out_dir, FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(letter)

    with open(path, "rb") as f:
        written = f.read()
    digest = hashlib.sha256(data).hexdigest()
    assert written == data, "entry.txt bytes differ from intended letter"
    assert hashlib.sha256(written).hexdigest() == digest, "sha256 mismatch"
    assert len(written) == 1, "gate requires exactly 1 character, file has %d bytes" % len(written)
    return path, digest


def main() -> None:
    letter = LETTER
    assert len(letter) == 1, f"entry must be exactly one character, got {len(letter)}"
    assert "A" <= letter <= "Z", f"entry must be a letter A-Z, got {letter!r}"
    assert letter.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "."
    path, digest = write_and_verify(letter, out_dir)

    print(f"letter: {letter}")
    print(f"sha256: {digest}")
    print(f"wrote: {path}")
    print("verified: entry.txt is exactly the one letter, byte for byte")


if __name__ == "__main__":
    main()
