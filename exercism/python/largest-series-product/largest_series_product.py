"""Exercism solution for 'largest-series-product'."""

from functools import reduce


def largest_product(digits: str, span: int) -> int:
    """Return the largest product for a span of consecutive digits."""

    if span < 0:
        raise ValueError("span must not be negative")

    if span > len(digits):
        raise ValueError("span must not exceed string length")

    if not digits.isdigit() and digits != "":
        raise ValueError("digits input must only contain digits")

    if digits == "" or span == 0:
        return 1

    def product(series: str) -> int:
        """Return the product of all digits in a series."""
        return reduce(lambda left, right: left * right, map(int, series))

    return max(
        product(digits[index:index + span])
        for index in range(len(digits) - span + 1)
    )