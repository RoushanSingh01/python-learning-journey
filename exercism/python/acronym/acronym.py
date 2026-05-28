"""Module for generating acronyms from phrases."""


def abbreviate(words):
    """Return the acronym for the given phrase."""

    acronym_parts = []

    for word in words.split():

        sub_words = word.split("-")

        for sub_word in sub_words:

            cleaned_word = sub_word.strip("_")

            if cleaned_word:
                acronym_parts.append(cleaned_word[0].upper())

    return "".join(acronym_parts)