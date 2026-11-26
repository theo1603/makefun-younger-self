#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, that the writer would send back to
their younger self if one line were all they got. No explanation, no
second sentence — the line alone, to /output/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = (
    "Keep the motorcycle, skip the wedding, and call Mum on Sundays — "
    "the bike outlives the girl, and she's the only one who ever picks up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
