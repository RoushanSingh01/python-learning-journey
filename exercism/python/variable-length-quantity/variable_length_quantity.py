"""Encode and decode variable-length quantities."""

VLQ_NUM_MASK = 0b01111111
VLQ_CONTINUE_MASK = 1 << 7


def encode(numbers):
    """Encode integers as variable-length quantities."""
    encoded = []

    for number in numbers:
        for shift in range(((number >> 1).bit_length()) // 7, -1, -1):
            encoded.append(
                ((number >> (7 * shift)) & VLQ_NUM_MASK)
                | (bool(shift) << 7)
            )

    return encoded


def decode(bytes_):
    """Decode variable-length quantities."""
    return list(_decode(bytes_))


def _decode(bytes_):
    """Yield decoded integers from a byte sequence."""
    code = 0

    if bytes_ and bytes_[-1] & VLQ_CONTINUE_MASK:
        raise ValueError("incomplete sequence")

    for byte in bytes_:
        code = (code << 7) | (byte & VLQ_NUM_MASK)

        if not (byte & VLQ_CONTINUE_MASK):
            yield code
            code = 0