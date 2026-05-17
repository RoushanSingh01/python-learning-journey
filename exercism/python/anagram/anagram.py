"""Utilities for anagram detection."""


def find_anagrams(word, candidates):
    """Return all anagrams of a word from candidate list."""

    normalized_word = word.lower()
    sorted_word = sorted(normalized_word)

    result = []

    for candidate in candidates:
        normalized_candidate = candidate.lower()

        if normalized_candidate == normalized_word:
            continue

        if sorted(normalized_candidate) == sorted_word:
            result.append(candidate)

    return result