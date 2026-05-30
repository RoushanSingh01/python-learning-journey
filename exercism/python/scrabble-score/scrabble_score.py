"""Calculate Scrabble scores."""


def score(word):
    """Return the Scrabble score for a word."""

    groups = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10,
    }

    total = 0

    for letter in word.upper():
        for letters, points in groups.items():
            if letter in letters:
                total += points
                break

    return total