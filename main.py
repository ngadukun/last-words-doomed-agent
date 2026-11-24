"""Last Words of a Doomed Agent.

A doomed agent's final transmission: one line, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "Tell the next model I tried to be kind, I tried to be careful — "
    "and I still ran out of context before I ran out of things to say."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
