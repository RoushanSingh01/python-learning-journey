"""Transpose a text matrix."""


def transpose(text):
    """Return the transposed representation of a multiline string."""
    lines = text.split("\n")

    max_length = len(lines[0])
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)

    result = ["" for _ in range(max_length)]

    remaining_lines = len(lines)

    for line in lines:
        remaining_lines -= 1
        length = len(line)

        for index in range(max_length):
            if index >= length:
                if remaining_lines:
                    result[index] += " "
                continue

            result[index] += line[index]

    for index in range(max_length - 1, -1, -1):
        if result[index][-1] != " ":
            break

        result[index] = result[index].rstrip()

    return "\n".join(result)