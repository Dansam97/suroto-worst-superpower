import os

TEXT = "I can charge any phone to 100% just by staring at it, but it takes exactly as long as the charger."

MIN_CHARS = 1
MAX_CHARS = 140


def render():
    """Return the entry text as UTF-8 bytes, validated against the kit gate:
    1-140 characters, a single line, not only whitespace."""
    if not (MIN_CHARS <= len(TEXT) <= MAX_CHARS):
        raise ValueError("entry text outside the 1-140 character gate")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    return (TEXT + "\n").encode("utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(render())


if __name__ == "__main__":
    main()
