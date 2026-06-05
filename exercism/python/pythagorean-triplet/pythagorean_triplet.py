"""Find Pythagorean triplets with a given sum."""

from math import isqrt, sqrt


def triplets_with_sum(number):
    """Return all Pythagorean triplets whose sum equals number."""
    triplets = []

    lower_bound = int((sqrt(2) - 1) * number)

    for c in range(number // 2 - 1, lower_bound, -1):
        discriminant = (
            c * c
            - number * number
            + 2 * number * c
        )

        if discriminant < 0:
            continue

        root = isqrt(discriminant)

        if root * root != discriminant:
            continue

        a = (number - c - root) // 2
        b = (number - c + root) // 2

        triplets.append(
            [a, b, c]
        )

    return triplets