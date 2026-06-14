"""
Exercism solution for "tournament"
"""

from collections import Counter, defaultdict
from operator import itemgetter
from typing import List, Sequence, Tuple, Union

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}

Cell = Union[str, int]
Row = Tuple[str, Cell, Cell, Cell, Cell, Cell]


def tally(results: Sequence[str]) -> List[str]:
    """
    Tally a football tournament.
    """
    teams: defaultdict[str, Counter[str]] = defaultdict(Counter)

    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1

    table: List[Row] = []
    for team, record in sorted(teams.items()):
        wins, draws, losses = record["win"], record["draw"], record["loss"]
        matches = wins + draws + losses
        points = 3 * wins + draws
        table.append((team, matches, wins, draws, losses, points))

    table.sort(key=itemgetter(-1), reverse=True)

    table.insert(0, ("Team", "MP", "W", "D", "L", "P"))
    return [ROW_FORMAT.format(*row) for row in table]