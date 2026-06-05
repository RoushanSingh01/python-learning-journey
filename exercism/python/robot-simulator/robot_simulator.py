"""Robot simulator implementation."""

NORTH, SOUTH, EAST, WEST = 0, 180, 90, 270


class Robot:
    """Simulate a robot moving on a grid."""

    def __init__(self, direction=NORTH, x=0, y=0):
        """Initialize robot position and direction."""
        self._x = x
        self._y = y
        self.direction = direction

        self._instructions = {
            "A": self.advance,
            "L": self.turn_left,
            "R": self.turn_right,
        }

    @property
    def coordinates(self):
        """Return current coordinates."""
        return (self._x, self._y)

    def advance(self):
        """Move one step forward."""
        moves = {
            NORTH: (0, 1),
            SOUTH: (0, -1),
            EAST: (1, 0),
            WEST: (-1, 0),
        }

        delta_x, delta_y = moves[self.direction]

        self._x += delta_x
        self._y += delta_y

    def turn_left(self):
        """Turn the robot left."""
        self.direction = (self.direction - 90) % 360

    def turn_right(self):
        """Turn the robot right."""
        self.direction = (self.direction + 90) % 360

    def move(self, instructions):
        """Execute a sequence of instructions."""
        for instruction in instructions:
            self._instructions[instruction]()