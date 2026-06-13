"""Generate valid Killer Sudoku cage combinations."""

from itertools import combinations as itertools_combinations


def combinations(target, size, exclude):
    """Return all valid combinations matching the target sum."""
    candidates = [
        value
        for value in range(1, min(target, 9) + 1)
        if value not in exclude
    ]

    return [
        list(combo)
        for combo in itertools_combinations(candidates, size)
        if sum(combo) == target
    ]