"""Utilities for rotational cipher encoding."""


def rotate(text: str, key: int) -> str:
    """Encode text using rotational cipher."""

    result = []

    for char in text:
        if char.isupper():
            base = ord("A")
            rotated = chr((ord(char) - base + key) % 26 + base)
            result.append(rotated)

        elif char.islower():
            base = ord("a")
            rotated = chr((ord(char) - base + key) % 26 + base)
            result.append(rotated)

        else:
            result.append(char)

    return "".join(result)