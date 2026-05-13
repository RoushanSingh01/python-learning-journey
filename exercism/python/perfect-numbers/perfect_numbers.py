"""Determine whether a number is perfect, abundant, or deficient."""


def classify(number):
    """Return classification of a positive integer."""

    if number < 1:
        raise ValueError(
            "Classification is only possible for positive integers."
        )

    divisor_sum = sum(
        divisor
        for divisor in range(1, number)
        if number % divisor == 0
    )

    if divisor_sum > number:
        return "abundant"

    if divisor_sum < number:
        return "deficient"

    return "perfect"