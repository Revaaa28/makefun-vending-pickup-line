"""Vending machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt (the make.fun program/v1 contract for this bounty).
"""

LINE = "I've got 40 snacks and one crush \u2014 press B7, it's the crush."

# The kit's gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly here rather than
# shipping an entry the sealed scorer would refuse.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
assert LINE.strip(), "line must not be only white space"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
