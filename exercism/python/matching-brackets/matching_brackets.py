"""Check whether brackets are correctly paired."""


BRACKET_PAIRS = {
    ")": "(",
    "}": "{",
    "]": "[",
}


def is_paired(input_string):
    """Return whether all brackets are correctly matched."""

    stack = []

    for char in input_string:
        if char in BRACKET_PAIRS.values():
            stack.append(char)

        elif char in BRACKET_PAIRS:
            if not stack or stack.pop() != BRACKET_PAIRS[char]:
                return False

    return not stack