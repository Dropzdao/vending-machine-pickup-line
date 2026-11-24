#!/usr/bin/env python3
"""Vending machine pickup line entry for make.fun.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt.
"""

import os

ENTRY = "I usually only light up for exact change, but you just made every button on me glow."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
