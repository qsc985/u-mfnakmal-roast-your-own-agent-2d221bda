#!/usr/bin/env python3
"""Write one roast line of my own AI agent to /output/entry.txt.

Roast (94 characters, single line, punchline at the end):
  I built an agent to save me time; it now spends mine
  writing status reports about saving time.
"""

import os

ROAST = "I built an agent to save me time; it now spends mine writing status reports about saving time.\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
