"""Clock implementation."""


class Clock:
    """Represent a 24-hour clock."""

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)