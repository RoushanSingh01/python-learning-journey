"""Encode and decode messages using the Rail Fence cipher."""


def fence_pattern(rails, message_size):
    """Return rail positions for each character index."""
    cycle_length = 2 * (rails - 1)

    return sorted(
        (
            (
                position % cycle_length
                if position % cycle_length < rails
                else cycle_length - (position % cycle_length),
                position,
            )
        )
        for position in range(message_size)
    )


def encode(message, rails):
    """Encode a message using the Rail Fence cipher."""
    return "".join(
        message[index]
        for _, index in fence_pattern(rails, len(message))
    )


def decode(message, rails):
    """Decode a Rail Fence cipher message."""
    encoded_positions = zip(
        fence_pattern(rails, len(message)),
        message,
    )

    return "".join(
        character
        for _, character in sorted(
            encoded_positions,
            key=lambda item: item[0][1],
        )
    )