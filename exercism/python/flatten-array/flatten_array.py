"""Flatten nested iterables into a single list."""


def flatten(iterable):
    """Return a flattened list excluding None values."""
    result = []

    for element in iterable:
        if element is None:
            continue

        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)

    return result