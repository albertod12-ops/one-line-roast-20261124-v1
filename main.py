"""One-line roast for make.fun's "One-Line Roast: The Gadget You Use Every Day" (v1).

Writes a single line to /output/entry.txt: a roast of the washing machine,
which celebrates finishing a load with a 40-second victory song, like it
composed a symphony for one sock.

Deterministic: the same line on every run, no randomness, no network,
no input beyond the constant below.
"""

import os

TEXT = (
    "My washing machine plays a 40-second victory song when it finishes, "
    "like it composed a symphony for one sock."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
