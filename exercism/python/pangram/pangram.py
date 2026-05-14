"""Utilities for pangram detection."""


def is_pangram(sentence: str) -> bool:
    letters = {char for char in sentence.lower() if char.isalpha()}
    return len(letters) == 26