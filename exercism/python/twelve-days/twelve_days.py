"""Generate verses for The Twelve Days of Christmas song."""


def recite(start_verse, end_verse):
    """Return the requested verses of the song."""

    ordinals = [
        "first", "second", "third", "fourth",
        "fifth", "sixth", "seventh", "eighth",
        "ninth", "tenth", "eleventh", "twelfth",
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]

    verses = []

    for verse_number in range(start_verse, end_verse + 1):

        gift_text = gifts[0]

        if verse_number > 1:
            gift_text = "and " + gift_text

        for gift_index in range(1, verse_number):
            gift_text = gifts[gift_index] + gift_text

        verses.append(
            f"On the {ordinals[verse_number - 1]} day of Christmas "
            f"my true love gave to me: {gift_text}"
        )

    return verses