#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a voicemail from the narrator's dead mother, ending on a
timestamp an hour in the future — dread earned by what it withholds
(she can finally see me; I will join her in an hour).
"""

import os

ENTRY = (
    # Verified: 112 characters, within the 1-200 gate; two runs
    # byte-identical (sha256 ba892fc5...ef8088).
    "My dead mother's voicemail ended with her saying she can "
    "finally see me, and the timestamp was an hour from now."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
