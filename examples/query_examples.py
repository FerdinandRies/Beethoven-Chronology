#!/usr/bin/env python3
"""Load the Beethoven chronology dataset and print a filtered timeline.

Usage:
    python3 examples/query_examples.py                  # all events
    python3 examples/query_examples.py 1800 1810        # a year range
    python3 examples/query_examples.py --category work  # one category

Standard library only; no dependencies.
"""
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "beethoven_chronology.csv"


def load():
    with DATA.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def year_of(row):
    return int(row["date"][:4])


def main(argv):
    rows = load()
    args = [a for a in argv if not a.startswith("--")]
    if "--category" in argv:
        cat = argv[argv.index("--category") + 1]
        rows = [r for r in rows if r["category"] == cat]
    elif len(args) == 2:
        lo, hi = int(args[0]), int(args[1])
        rows = [r for r in rows if lo <= year_of(r) <= hi]
    for r in rows:
        span = r["date"] + (f"..{r['date_end']}" if r["date_end"] else "")
        works = f" [{r['works']}]" if r["works"] else ""
        print(f"{span:<24} {r['event']}{works}")
    print(f"\n{len(rows)} events")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
