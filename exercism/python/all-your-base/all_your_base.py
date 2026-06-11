"""Convert a number between arbitrary bases."""


def rebase(input_base, digits, output_base):
    """Convert digits from one base to another."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if any(digit < 0 for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    number = sum(
        digit * input_base**index
        for index, digit in enumerate(reversed(digits))
    )

    if number == 0:
        return [0]

    new_digits = []

    while number:
        number, digit = divmod(number, output_base)
        new_digits.insert(0, digit)

    return new_digits