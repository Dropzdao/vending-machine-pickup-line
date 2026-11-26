"""Vending Machine Pickup Line — one-line entry writer.

Writes the single entry line to /output/entry.txt with no trailing
newline, using only the Python standard library. No network access.
"""

import os

ENTRY = "I usually only light up for exact change, but you just made every button on me glow."


def validate(line):
    """Entry must be one line, 1-200 chars, no trailing newline."""
    assert 1 <= len(line) <= 200, "entry length out of range"
    assert "\n" not in line, "entry must be a single line"
    return line


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
