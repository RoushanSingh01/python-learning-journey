"""Translate English words into Pig Latin."""


VOWELS = {"a", "e", "i", "o", "u"}
SPECIAL_CASES = {"xr", "yt"}


def translate_single_word(text):
    """Translate a single word into Pig Latin."""

    if text[0] in VOWELS or text[:2] in SPECIAL_CASES:
        return text + "ay"

    if text[1:3] == "qu":
        return text[3:] + text[0] + "quay"

    if text[:2] == "qu":
        return text[2:] + "quay"

    for index, char in enumerate(text):
        if char in VOWELS or (char == "y" and index > 0):
            return text[index:] + text[:index] + "ay"

    return None


def translate(text):
    """Translate a phrase into Pig Latin."""

    return " ".join(
        translate_single_word(word)
        for word in text.split()
    )