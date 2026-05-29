"""Generate all contiguous substrings of a given length."""


def slices(series, length):
    """Return all contiguous slices of the requested length."""

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    result = []

    for start_index in range(len(series) - length + 1):
        result.append(series[start_index:start_index + length])

    return result