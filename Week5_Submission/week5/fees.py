"""Refactored tuition fee calculation, independent of presentation."""
from dataclasses import dataclass
from enum import IntEnum


class StudentType(IntEnum):
    """Supported student fee categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
    """A course and its credit hours."""

    hours: int


HOURLY_RATE = 350
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_FEE = 150
STUDENT_RATES = {
    StudentType.REGULAR: 1.0,
    StudentType.STAFF_CHILD: 0.5,
    StudentType.SCHOLARSHIP: 0.0,
}


def tuition_fee(courses, student_type, summer=False, discount=0, extras=()):
    """Calculate tuition while retaining the legacy calculation order."""
    rate = STUDENT_RATES[StudentType(student_type)]
    total = sum(course.hours * HOURLY_RATE * rate for course in courses)
    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_FEE
    total -= 0 if discount is None else discount
    return total + sum(extras)


def report(courses, student_type, summer=False, discount=0):
    """Return report text without printing it."""
    kind = StudentType(student_type)
    amount = tuition_fee(courses, kind, summer, discount)
    labels = {
        StudentType.REGULAR: "Student fee",
        StudentType.STAFF_CHILD: "Staff child fee",
        StudentType.SCHOLARSHIP: "Scholarship fee",
    }
    lines = [f"{labels[kind]}: {amount}"]
    if amount > HIGH_FEE_THRESHOLD:
        lines.append("High fee")
    return "\n".join(lines)


def process_all(students):
    """Calculate a fresh fee for every student, including scholarships."""
    return {
        student["name"]: tuition_fee(
            student["courses"], student["type"], student["summer"]
        )
        for student in students
    }
