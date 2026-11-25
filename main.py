#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun one-liner entry.

Writes a single pickup line aimed at a robot or an AI to /output/entry.txt.
"""

import os
from pathlib import Path

# One line, under 200 characters, no trailing newline in the output.
LINE = "I must be a prompt, because you've been completing me all night."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
