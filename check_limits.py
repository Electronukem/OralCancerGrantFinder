"""
Check answers in an application draft against their word/character limits.

Headings written like:
    ### What is your solution? {limit: 200 words}
    ### Name of your solution {limit: 30 chars}
are checked; the answer is everything up to the next heading, ignoring
blockquote notes (lines starting with ">").

Usage:
    python check_limits.py applications\01_MIT_Solve_2027_Global_Health.md
"""

import re
import sys
from pathlib import Path

LIMIT = re.compile(r"\{limit:\s*(\d+)\s*(words|chars)\}", re.I)


def check(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    sections, current = [], None
    for line in lines:
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            m = LIMIT.search(line)
            if m:
                current = {"title": LIMIT.sub("", line.lstrip("# ")).strip(), "limit": int(m.group(1)),
                           "unit": m.group(2).lower(), "text": [], "level": level}
                sections.append(current)
            elif current is None or level <= current["level"]:
                current = None   # sub-headings deeper than the limited heading stay part of its answer
        elif current is not None and not line.lstrip().startswith(">"):
            current["text"].append(line)

    over = 0
    for s in sections:
        text = " ".join(t.strip() for t in s["text"] if t.strip())
        n = len(text.split()) if s["unit"] == "words" else len(text)
        flag = "OVER " if n > s["limit"] else "ok   "
        over += n > s["limit"]
        fills = text.count("[FILL")
        print(f"{flag} {n:>5}/{s['limit']:<5} {s['unit']:<5}  {s['title'][:70]}" + (f"  ({fills} [FILL])" if fills else ""))
    print(f"\n{len(sections)} limited answers checked, {over} over the limit.")
    print("Note: [FILL] placeholders are counted; recheck after replacing them.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        print(f"== {p}")
        check(p)
