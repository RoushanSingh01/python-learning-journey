"""Compute the integer square root of a perfect square."""


def square_root(number):
    """Return the square root of the given perfect square."""

    left, right = 0, number

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == number:
            return mid

        if square < number:
            left = mid + 1
        else:
            right = mid - 1

    return None