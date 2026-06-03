"""Transpose a text matrix."""


def transpose(text):
    """Return the transposed representation of a multiline string."""
    lines = text.split("\n")

    max_length = max(len(line) for line in lines)

    result = [""] * max_length

    remaining_lines = len(lines)

    for line in lines:
        remaining_lines -= 1

        for index in range(max_length):
            if index >= len(line):
                if remaining_lines:
                    result[index] += " "
                continue

            result[index] += line[index]

    for index in range(max_length - 1, -1, -1):
        if not result[index].endswith(" "):
            break

        result[index] = result[index].rstrip()

    return "\n".join(result)