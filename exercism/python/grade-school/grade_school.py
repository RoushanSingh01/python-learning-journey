"""Grade school roster management."""


class School:
    """Store students by grade."""

    def __init__(self):
        """Initialize an empty school."""
        self.students = {}
        self.add_history = []

    def add_student(self, name, grade):
        """Add a student to a grade."""
        for student_names in self.students.values():
            if name in student_names:
                self.add_history.append(False)
                return

        self.students.setdefault(grade, []).append(name)
        self.add_history.append(True)

    def roster(self):
        """Return the full roster."""
        result = []

        for grade in sorted(self.students):
            result.extend(
                sorted(self.students[grade])
            )

        return result

    def grade(self, grade_number):
        """Return students in a grade."""
        return sorted(
            self.students.get(
                grade_number,
                [],
            )
        )

    def added(self):
        """Return add operation results."""
        return self.add_history