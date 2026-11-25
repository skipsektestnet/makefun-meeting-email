"""The Meeting That Should Have Been an Email: writes the entry text to /output/entry.txt.

Why this line: one sentence, a meeting that exists only to decide what the
meeting is about, and the punch lands on the last words — a follow-up booked
to decide when to decide. No setup, no explanation, every word earns its place.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'We spent forty minutes in a meeting deciding what the meeting was about, then booked a follow-up to decide when to decide it.'

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the bounty gate: 1-200 chars, single line."""
    assert text and not text.isspace(), "entry must not be empty"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, "entry length out of range"
    assert "\n" not in text, "entry must be a single line"
    return text


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
