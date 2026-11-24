"""Dad Joke Showdown entry (Sparta, round 2).

One-line sports dad joke: a concrete setup with real numbers, then a
sharp, closed punchline. Standard library only.
"""

import os
import sys

# Design: concrete sports setup (a father's first 10K, real numbers for
# distance, time, age and bragging time) with a sharp, closed punchline
# and no hanging question. One line, 200 characters max.
TEXT = "Dad ran his first 10K in 52 minutes at 58 years old, then bragged for 3 hours straight. The only marathon he ever finished was the story about it."


def main():
    if not TEXT:
        print("error: TEXT is empty", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("error: TEXT must be a single line", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print("error: TEXT is %d characters, over the 200 limit" % len(TEXT), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT + "\n":
        print("error: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print("entry written: %d characters, 1 line" % len(TEXT))
    print("output: %s" % out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
