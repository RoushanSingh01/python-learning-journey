"""Crypto Square cipher implementation."""

from re import findall


def cipher_text(plain_text):
    """Encode text using the Crypto Square cipher."""
    normalized = "".join(findall(r"[a-z\d]", plain_text.lower()))

    columns = int(round(len(normalized) ** 0.5, 0))
    rows = int(round(len(normalized) ** 0.5, 0))

    if columns * rows < len(normalized):
        columns += 1

    normalized = normalized.ljust(columns * rows)

    rectangle = [
        normalized[index * columns:(index + 1) * columns]
        for index in range(rows)
    ]

    return " ".join("".join(row) for row in zip(*rectangle))