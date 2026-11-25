#!/usr/bin/env python3
"""Entry program for u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

Writes one single-line joke about a meeting that should have been an email
to /output/entry.txt. Deterministic: the exact same line on every run, with
no trailing newline, so the artifact is the joke and nothing else.
"""
import hashlib
import os
import sys

JOKE = "Our meeting about the email ended with a decision to hold another meeting to read the email."
EXPECTED_BYTES = 92
EXPECTED_SHA256 = "9c3cefac29d242d4dc6d3ec227d56f46f5c4f782e211f6443702862442249444"


def main():
    text = JOKE
    data = text.encode("utf-8")
    if not (1 <= len(data) <= 200):
        print(f"gate fail: {len(data)} bytes, need 1-200", file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"byte count mismatch: {len(data)} != {EXPECTED_BYTES}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: {digest}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    print(f"wrote /output/entry.txt: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
