"""Track and analyze high scores."""


class HighScores:
    """Store and analyze a player's scores."""

    def __init__(self, scores):
        """Initialize the score history."""
        self.scores = scores

    def latest(self):
        """Return the most recent score."""
        return self.scores[-1]

    def personal_best(self):
        """Return the highest score."""
        return max(self.scores)

    def personal_top_three(self):
        """Return the three highest scores."""
        return sorted(
            self.scores,
            reverse=True,
        )[:3]