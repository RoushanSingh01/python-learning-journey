"""Generate unique robot names."""

from random import choice, randint
from string import ascii_uppercase


class Robot:
    """Represent a robot with a unique name."""

    used_names = set()

    def __init__(self):
        """Initialize the robot."""
        self.name = self._generate_name()

    @classmethod
    def _generate_name(cls):
        """Generate a unique robot name."""
        while True:
            name = (
                choice(ascii_uppercase)
                + choice(ascii_uppercase)
                + f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
            )

            if name not in cls.used_names:
                cls.used_names.add(name)
                return name

    def reset(self):
        """Assign a new unique name to the robot."""
        self.name = self._generate_name()