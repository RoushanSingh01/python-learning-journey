"""Find the smallest and largest palindrome products."""


def palindrome(number):
    """Return whether a number is a palindrome."""
    text = str(number)
    return text == text[::-1]


def largest(min_factor, max_factor):
    """Return the largest palindrome and its factor pairs."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    factors_list = []

    for product in range(max_factor**2, min_factor**2 - 1, -1):
        if palindrome(product):
            for factor in range(min_factor, max_factor + 1):
                if (
                    product % factor == 0
                    and min_factor <= product // factor <= max_factor
                ):
                    factors_list.append(
                        [factor, product // factor]
                    )

        if factors_list:
            return product, factors_list

    return None, factors_list


def smallest(min_factor, max_factor):
    """Return the smallest palindrome and its factor pairs."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    factors_list = []

    for product in range(
        min_factor**2,
        (max_factor + 1) ** 2,
    ):
        if palindrome(product):
            for factor in range(min_factor, max_factor + 1):
                if (
                    product % factor == 0
                    and min_factor <= product // factor <= max_factor
                ):
                    factors_list.append(
                        [factor, product // factor]
                    )

        if factors_list:
            return product, factors_list

    return None, factors_list