"""Determine the best poker hand."""

CARD_ORDER = "--234567890JQKA"


def best_hands(hands):
    """Return all winning poker hands."""
    serialized_hands = serialize(hands)

    winning_rank = max(
        hand_rank(hand)
        for hand in serialized_hands
    )

    return [
        deserialize(hand)
        for hand in serialized_hands
        if hand_rank(hand) == winning_rank
    ]


def serialize(hands):
    """Convert hands into rank/suit tuples."""
    serialized_hands = []

    for hand in hands:
        serialized_hand = []

        for card in hand.split():
            serialized_hand.append(
                (card[-2], card[-1])
            )

        serialized_hands.append(
            serialized_hand
        )

    return serialized_hands


def deserialize(hand):
    """Convert tuples back to hand string."""
    return " ".join(
        "".join(
            ["10" if rank == "0" else rank, suit]
        )
        for rank, suit in hand
    )


def card_ranks(hand):
    """Return sorted card ranks."""
    ranks = [
        CARD_ORDER.index(rank)
        for rank, _suit in hand
    ]

    ranks.sort(reverse=True)

    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]

    return ranks


def hand_rank(hand):
    """Return the ranking of a poker hand."""
    ranks = card_ranks(hand)

    groups = [
        (ranks.count(rank), rank)
        for rank in set(ranks)
    ]

    groups.sort(reverse=True)

    counts, values = zip(*groups)

    is_straight = (
        len(counts) == 5
        and max(values) - min(values) == 4
    )

    is_flush = (
        len(
            {suit for _rank, suit in hand}
        )
        == 1
    )

    if is_straight and is_flush:
        return (8, values)

    if counts == (4, 1):
        return (7, values)

    if counts == (3, 2):
        return (6, values)

    if is_flush:
        return (5, values)

    if is_straight:
        return (4, values)

    if counts == (3, 1, 1):
        return (3, values)

    if counts == (2, 2, 1):
        return (2, values)

    if counts == (2, 1, 1, 1):
        return (1, values)

    return (0, values)