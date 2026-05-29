"""Encode and decode strings using run-length encoding."""


def decode(string):
    """Decode a run-length encoded string."""

    count = ""
    result = []

    for character in string:

        if character.isdigit():
            count += character

        elif count:
            result.append(character * int(count))
            count = ""

        else:
            result.append(character)

    return "".join(result)


def encode(string):
    """Encode a string using run-length encoding."""

    if not string:
        return ""

    result = []
    previous_character = string[0]
    count = 0

    for character in string:

        if character == previous_character:
            count += 1

        else:

            if count == 1:
                result.append(previous_character)
            else:
                result.append(f"{count}{previous_character}")

            previous_character = character
            count = 1

    if count == 1:
        result.append(previous_character)
    else:
        result.append(f"{count}{previous_character}")

    return "".join(result)