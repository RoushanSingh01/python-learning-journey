"""Sum all unique multiples below a limit."""


def sum_of_multiples(limit, multiples):
    """Return the sum of unique multiples below the given limit."""

    valid_multiples = [multiple for multiple in multiples if multiple != 0]

    return sum(
        {
            number
            for number in range(limit)
            for multiple in valid_multiples
            if number % multiple == 0
        }
    )