SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_sublist(small, large):
    """Return whether small is a contiguous sublist of large."""

    length = len(small)

    for index in range(len(large) - length + 1):
        if large[index:index + length] == small:
            return True

    return False


def sublist(list_one, list_two):
    """Compare two lists and determine their relationship."""

    if list_one == list_two:
        return EQUAL

    if is_sublist(list_one, list_two):
        return SUBLIST

    if is_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL