"""Utilities for isogram detection."""


def is_isogram(text: str) -> bool:
    letters = [char for char in text.lower() if char.isalpha()]
    return len(letters) == len(set(letters))