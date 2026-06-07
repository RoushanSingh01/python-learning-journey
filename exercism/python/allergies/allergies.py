"""Determine allergies from a score."""


class Allergies:
    """Represent a person's allergies."""

    INGREDIENTS = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        """Store the allergy score."""
        self.score = score

    def allergic_to(self, item):
        """Return whether the person is allergic to an item."""
        return bool(
            self.score & self.INGREDIENTS[item]
        )

    @property
    def lst(self):
        """Return all allergies."""
        return [
            allergy
            for allergy in self.INGREDIENTS
            if self.allergic_to(allergy)
        ]