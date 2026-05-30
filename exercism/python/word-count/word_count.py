"""Count the occurrences of words in a sentence."""

import re


def count_words(sentence):
    """Return a dictionary mapping words to their counts."""

    counts = {}

    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence.lower())

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts