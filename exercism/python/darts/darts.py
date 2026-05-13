"""Calculate dart game scores based on distance from center."""


def score(x_coordinate, y_coordinate):
    """Return score based on dart distance from board center."""

    distance_squared = x_coordinate**2 + y_coordinate**2

    if distance_squared <= 1:
        return 10

    if distance_squared <= 25:
        return 5

    if distance_squared <= 100:
        return 1

    return 0