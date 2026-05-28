"""Module for converting numbers into spoken English."""


ONES = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

SCALES = ["", "thousand", "million", "billion"]


def say(number):
    """Convert a number into spoken English."""

    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    parts = []
    scale_index = 0

    while number > 0:

        chunk = number % 1000

        if chunk:

            words = say_under_thousand(chunk)

            scale = SCALES[scale_index]

            if scale:
                parts.append(f"{words} {scale}")
            else:
                parts.append(words)

        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))


def say_under_thousand(number):
    """Convert a number below one thousand into words."""

    parts = []

    hundreds = number // 100
    remainder = number % 100

    if hundreds:
        parts.append(f"{ONES[hundreds]} hundred")

    if 10 <= remainder <= 19:
        parts.append(TEENS[remainder])

    else:

        tens = remainder // 10
        ones = remainder % 10

        if tens:

            tens_word = TENS[tens]

            if ones:
                tens_word += f"-{ONES[ones]}"

            parts.append(tens_word)

        elif ones:
            parts.append(ONES[ones])

    return " ".join(parts)