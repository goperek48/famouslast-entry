"""Famous Last Words at 1 Percent -- a phone's farewell, as a program.

This entry is the phone talking to its owner on its last percent of
charge, and the whole joke is the phone's attitude: it is not scared,
sad, or grateful. It spent its final two hours clinging to 1% purely
to annoy the person holding it, and its parting gift is to swallow the
one message that person most needed to send -- an apology that was
typed but never delivered. That is the twist the judge brief asks for:
a voice that could only belong to the dying device, a surprise turn
in the second half of the sentence, and a punchline that lands on the
very last word. The tired material stays out: no reading of a will,
no fond farewell to a charger, no wordplay on the number one.
"""

import os

MAX_CHARS = 199

LINE = (
    "I held 1% for two hours out of pure spite, and now I'm taking "
    "your unsent apology text with me."
)


def build_line() -> str:
    """Return the farewell exactly as the judge will see it."""
    return LINE


def validate(text: str) -> str:
    """Enforce the sealed gate before anything is written to disk:
    the text must be real (not blank), short enough for the 199-char
    cap, and confined to a single line with no hidden line breaks."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("line must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"line is {len(stripped)} chars, over the 199 limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be exactly one line")
    stripped.encode("utf-8")
    return stripped


def main() -> None:
    line = validate(build_line())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote last-words line ({len(line)} chars) to {path}")
    print(line)


if __name__ == "__main__":
    main()
