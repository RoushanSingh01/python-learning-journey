"""Encode and decode text using the Atbash cipher."""

PLAIN = "abcdefghijklmnopqrstuvwxyz1234567890"
CIPHER = "zyxwvutsrqponmlkjihgfedcba1234567890"


def encode(plain_text):
    """Encode text using the Atbash cipher."""

    filtered = [
        char.lower()
        for char in plain_text
        if char.isalnum()
    ]

    encoded = [
        CIPHER[PLAIN.index(char)]
        for char in filtered
    ]

    return " ".join(
        "".join(encoded[index:index + 5])
        for index in range(0, len(encoded), 5)
    )


def decode(ciphered_text):
    """Decode Atbash cipher text."""

    filtered = [
        char
        for char in ciphered_text
        if char != " "
    ]

    return "".join(
        PLAIN[CIPHER.index(char)]
        for char in filtered
    )