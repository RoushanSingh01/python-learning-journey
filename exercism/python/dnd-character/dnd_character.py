"""Generate a D&D character and ability scores."""

from random import randint


def modifier(score):
    """Calculate the ability modifier."""
    return (score - 10) // 2


class Character:
    """Represent a D&D character."""

    def __init__(self):
        abilities = (
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        )

        for ability in abilities:
            setattr(self, ability, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        """Generate an ability score."""
        return sum(
            sorted(randint(1, 6) for die_roll in range(4))[1:]
        )