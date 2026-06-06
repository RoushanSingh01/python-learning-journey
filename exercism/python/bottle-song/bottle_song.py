"""Recite the Bottle Song."""

PLURAL_ITEMS = [
    "green bottle",
    "green bottles",
]

NUMBER_WORDS = [
    "no",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
]

VERSE_TEMPLATE = """{this_str_number} {this_item} hanging on the wall,
{this_str_number} {this_item} hanging on the wall,
And if {decrement_str_number} {decrement_item} should accidentally fall,
There'll be {next_str_number} {next_item} hanging on the wall."""


def create_verse(verse_number):
    """Create a single verse."""
    return VERSE_TEMPLATE.format(
        this_str_number=NUMBER_WORDS[verse_number],
        this_item=PLURAL_ITEMS[verse_number != 1],
        decrement_str_number="one",
        decrement_item="green bottle",
        next_str_number=NUMBER_WORDS[verse_number - 1].lower(),
        next_item=PLURAL_ITEMS[verse_number - 1 != 1],
    )


def recite(start, take=1):
    """Return the requested verses."""
    verses = [
        create_verse(verse_number)
        for verse_number in range(
            start,
            start - take,
            -1,
        )
    ]

    return "\n\n".join(verses).splitlines()