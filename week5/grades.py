"""Convert a numeric score into a letter grade."""

MIN_SCORE = 0
MAX_SCORE = 100
GRADE_A = 90
GRADE_B = 80
GRADE_C = 70
GRADE_D = 60


def letter_grade(score):
    """Return A, B, C, D or F for a score between 0 and 100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")
    if score >= GRADE_A:
        return "A"
    if score >= GRADE_B:
        return "B"
    if score >= GRADE_C:
        return "C"
    if score >= GRADE_D:
        return "D"
    return "F"
