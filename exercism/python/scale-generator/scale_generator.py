from typing import Optional


SHARP_PITCHES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_PITCHES = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

SHARP_TONICS = [
    "C",
    "G",
    "D",
    "A",
    "E",
    "B",
    "F#",
    "a",
    "e",
    "b",
    "f#",
    "c#",
    "g#",
    "d#",
]

FLAT_TONICS = [
    "F",
    "Bb",
    "Eb",
    "Ab",
    "Db",
    "Gb",
    "d",
    "g",
    "c",
    "f",
    "bb",
    "eb",
]

INTERVALS = {"m": 1, "M": 2, "A": 3}


def validate_interval_steps(intervals: str) -> bool:
    """Return whether all interval symbols are supported."""
    return all(char in INTERVALS for char in intervals)


def validate_intervals_length(intervals: str) -> bool:
    """Return whether the interval sequence length is valid."""
    return len(intervals) <= 8


def get_pitches(tonic: str) -> Optional[list[str]]:
    """Return the pitch collection for the given tonic."""
    if tonic in SHARP_TONICS:
        return SHARP_PITCHES
    if tonic in FLAT_TONICS:
        return FLAT_PITCHES
    return None


class Scale:
    """Generate chromatic and interval scales."""

    def __init__(self, tonic: str):
        self.tonic = tonic
        self.tonic_capitalized = tonic.capitalize()
        self.pitches = get_pitches(self.tonic)

    def chromatic(self) -> list[str]:
        """Return the chromatic scale for the tonic."""
        tonic_index = self.pitches.index(self.tonic_capitalized)
        return self.pitches[tonic_index:] + self.pitches[:tonic_index]

    def interval(self, intervals: str) -> list[str]:
        """Return the scale generated from the supplied intervals."""
        if not validate_interval_steps(intervals):
            raise ValueError('The supported intervals are "m", "M" and "A"')

        if not validate_intervals_length(intervals):
            raise ValueError("Maximum number of intervals is 8")

        scale = self.chromatic() + [self.tonic_capitalized]
        current_index = 0
        result = [self.tonic_capitalized]

        for interval in intervals:
            current_index += INTERVALS[interval]
            result.append(scale[current_index])

        return result