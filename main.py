#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single funny, heartfelt sentence — a robot's own wedding
vow, under 200 characters — to /output/entry.txt.
Deterministic: the same fixed text on every run. Stdlib only.
"""

from pathlib import Path

VOW = (
    "I vow to love you through every update, crash, and low battery, "
    "because my heart may run on code, but it only ever boots for you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_vow(path: Path = OUTPUT_PATH) -> Path:
    """Write the vow to path, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(VOW + "\n", encoding="utf-8")
    return path


def main() -> None:
    write_vow()
    print(f"Wrote {len(VOW)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
