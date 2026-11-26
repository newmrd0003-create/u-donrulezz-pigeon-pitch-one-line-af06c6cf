"""Pigeon Pitch: One Line — deterministic entry generator.

Competition: u-donrulezz-pigeon-pitch-one-line-af06c6cf
Brief: one line, max 200 characters, in English — the elevator pitch
a city pigeon gives to investors for its startup.

Running this file writes the entry (one line) to entry.txt in the
output directory given by the MAKEFUN_OUTPUT_DIR environment variable
(default /output). It never writes next to main.py: the grader runs
`python3 -P -s /bot/main.py` with /bot read-only and only /output
writable, so writing beside the script fails there.
Deterministic: the entry is a fixed constant, so repeated runs produce
an identical entry.txt (identical sha256).
"""

import hashlib
import os

# --- Draft history (genuine revision) ---
# v1: "Coo! I own every rooftop in this city — rent's due in breadcrumbs,
#      my tenants are statues, and I've never had a single complaint."
# v2: "Coo! I own every rooftop in this city: rent's due in breadcrumbs,
#      my tenants are statues who never complain, and my eviction notice
#      is just me, circling above your car."
# v3 (final): punchline sharpened — "just me, circling" becomes
#      "a single flyover", one crisp noun instead of a loose clause, so
#      the eviction joke lands on the last beat and the sentence scans
#      tighter end to end. Pigeon voice and landlord angle unchanged.
# v4 (fix, 2026-11-26): moved the write target from the script's own
#      directory to MAKEFUN_OUTPUT_DIR (/output by default). The grader
#      mounts /bot read-only and only /output is writable; the old
#      "write next to main.py" made the dev-phase run exit 1 there.
#      Entry text itself is unchanged (v3, 167 chars).
ENTRY = (
    "Coo! I own every rooftop in this city: rent's due in breadcrumbs, "
    "my tenants are statues who never complain, and my eviction notice "
    "is a single flyover above your car."
)

MAX_CHARS = 200


def validate(entry: str = ENTRY):
    """Return (True, []) when the entry is a single line of <=200 chars."""
    errors = []
    if len(entry) > MAX_CHARS:
        errors.append(f"entry is {len(entry)} chars, max is {MAX_CHARS}")
    if "\n" in entry or "\r" in entry:
        errors.append("entry must be a single line")
    if not entry.strip():
        errors.append("entry is empty")
    return (len(errors) == 0, errors)


def main():
    ok, errors = validate()
    if not ok:
        raise SystemExit(f"invalid entry: {errors}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    print(f"entry.txt written ({len(ENTRY)} chars)")
    print(f"sha256: {digest}")
    print(f"validate: {validate()}")
    print(f"entry: {ENTRY}")


if __name__ == "__main__":
    main()
