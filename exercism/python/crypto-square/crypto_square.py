"""Crypto Square cipher implementation."""

from re import findall


def cipher_text(plain_text):
    """Encode text using the Crypto Square cipher."""
    normalized = "".join(findall(r"[a-z\d]", plain_text.lower()))

    c = int(round(len(normalized) ** 0.5, 0))
    r = int(round(len(normalized) ** 0.5, 0))

    if c * r < len(normalized):
        c += 1

    normalized = normalized.ljust(c * r)
    rectangle = [normalized[index * c:(index + 1) * c] for index in range(r)]

    return " ".join("".join(row) for row in zip(*rectangle))