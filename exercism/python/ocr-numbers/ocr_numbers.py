"""Convert OCR numbers into digits."""

DIGITS = {
    (
        " _ ",
        "| |",
        "|_|",
        "   ",
    ): "0",
    (
        "   ",
        "  |",
        "  |",
        "   ",
    ): "1",
    (
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ): "2",
    (
        " _ ",
        " _|",
        " _|",
        "   ",
    ): "3",
    (
        "   ",
        "|_|",
        "  |",
        "   ",
    ): "4",
    (
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ): "5",
    (
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ): "6",
    (
        " _ ",
        "  |",
        "  |",
        "   ",
    ): "7",
    (
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ): "8",
    (
        " _ ",
        "|_|",
        " _|",
        "   ",
    ): "9",
}


def convert(input_grid):
    """Convert OCR digits into a string representation."""
    lines = list(input_grid)

    if len(lines) % 4 != 0:
        raise ValueError(
            "Number of input lines is not a multiple of four"
        )

    if lines:
        for line in lines:
            if len(line) % 3 != 0:
                raise ValueError(
                    "Number of input columns is not a multiple of three"
                )

    results = []

    for block_start in range(0, len(lines), 4):
        block = lines[block_start:block_start + 4]

        digit_count = len(block[0]) // 3
        digits = []

        for digit_index in range(digit_count):
            start = digit_index * 3
            end = start + 3

            pattern = (
                block[0][start:end],
                block[1][start:end],
                block[2][start:end],
                block[3][start:end],
            )

            digits.append(
                DIGITS.get(pattern, "?")
            )

        results.append(
            "".join(digits)
        )

    return ",".join(results)