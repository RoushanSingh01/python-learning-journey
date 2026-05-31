"""Generate a proverb from a list of inputs."""


def proverb(*lst, qualifier=None):
    """Return the proverb as a list of strings."""
    result = []

    for first, second in zip(lst, lst[1:]):
        result.append(
            f"For want of a {first} the {second} was lost."
        )

    if lst:
        if qualifier is not None:
            result.append(
                f"And all for the want of a {qualifier} {lst[0]}."
            )
        else:
            result.append(
                f"And all for the want of a {lst[0]}."
            )

    return result