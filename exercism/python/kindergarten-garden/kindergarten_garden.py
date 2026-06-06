"""Assign plants to students in a kindergarten garden."""

DEFAULT_STUDENTS = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
)

PLANTS = {
    "C": "Clover",
    "G": "Grass",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    """Represent a kindergarten garden."""

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        """Initialize the garden layout."""
        self.lines = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        """Return the plants assigned to a student."""
        start_index = self.students.index(student) * 2

        return [
            PLANTS[row[column]]
            for row in self.lines
            for column in (
                start_index,
                start_index + 1,
            )
        ]