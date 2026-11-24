"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: "A", the kit's letter
for coffee. Coffee is the pick: it is the fuel of the all-night build
grind, the drink that keeps a builder going when the work runs past
midnight, while tea is the drink of slowing down. One byte, no newline.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def check_entry(path: str) -> bool:
    """Gate-check: entry.txt must be exactly 1 byte, one A-Z letter."""
    with open(path, "rb") as handle:
        raw = handle.read()
    return len(raw) == 1 and 65 <= raw[0] <= 90


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    if not check_entry(OUTPUT_PATH):
        raise SystemExit("gate check failed: entry.txt is not one A-Z letter")


if __name__ == "__main__":
    main()
