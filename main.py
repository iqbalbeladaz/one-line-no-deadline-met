#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun bounty entry.

Writes one single-line joke excusing a missed deadline to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR). Deterministic: the same
bytes on every run, no input, no randomness, no network. Standard
library only.

The line: the excuse is recursive — the work was skipped to write the
apology for skipping the work, and the apology itself is late too. The
entry *is* the apology it describes, so the joke lands on the reader
twice: once as the excuse, once as the artifact. It names the deadline
up front, reads like something a cornered person would actually say,
and the punch ("the apology is late too") is the last word.
"""

import os
from pathlib import Path

ENTRY = (
    "I missed the deadline because I spent all week writing the apology "
    "for missing it \u2014 and the apology is late too."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line — the judge reads one line,
# so a stray newline would break the entry. Refuse to write anything
# that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
