#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt."""

import os

LINE = "Good news: I found the bug. Bad news: it's me, and I just promoted myself to production."


def main() -> None:
    text = LINE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 180 characters,
    # not only white space, and a single line.
    if not 1 <= len(text) <= 180:
        raise ValueError(f"entry is {len(text)} characters, must be 1-180")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
