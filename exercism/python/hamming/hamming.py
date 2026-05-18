def distance(strand_a, strand_b):
    """
    Compute the Hamming distance between two DNA strands.

    Raises:
        ValueError: If strands are not equal in length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(
        left != right
        for left, right in zip(strand_a, strand_b)
    )