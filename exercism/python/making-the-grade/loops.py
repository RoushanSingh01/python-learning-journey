"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students."""
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Return scores greater than or equal to threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create grade thresholds for D to A."""
    interval = (highest - 40) // 4
    return [41 + interval * step for step in range(4)]


def student_ranking(student_scores, student_names):
    """Return formatted ranking list."""
    return [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1)
    ]


def perfect_score(student_info):
    """Return first student with perfect score."""
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []