"""Convert integers to Roman numerals."""


def roman(number):
    """Return the Roman numeral representation of a number."""

    numerals = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    place_value = 1
    result = ""

    while number > 0:

        digit = number % 10
        number //= 10

        if digit <= 3:
            result = numerals[place_value] * digit + result

        elif digit == 4:
            result = (
                numerals[place_value]
                + numerals[5 * place_value]
                + result
            )

        elif digit <= 8:
            result = (
                numerals[5 * place_value]
                + numerals[place_value] * (digit - 5)
                + result
            )

        else:
            result = (
                numerals[place_value]
                + numerals[10 * place_value]
                + result
            )

        place_value *= 10

    return result