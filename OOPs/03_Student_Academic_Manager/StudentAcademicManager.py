from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class Semester(Enum):
    FALL = "Fall"
    SPRING = "Spring"
    WINTER = "Winter"


class Gender(Enum):
    MALE = "M"
    FEMALE = "F"


@dataclass
class CourseRecord:
    course_code: str
    course_name: str
    grade: Optional[int]  # None if not graded yet
    credit: int
    year: int
    semester: Semester


class Student:
    """
    Student Academic Manager
    """

    GRADE_A = 90
    GRADE_B = 80
    GRADE_C = 70
    GRADE_D = 60

    GPA_A = 4.0
    GPA_B = 3.0
    GPA_C = 2.0
    GPA_D = 1.0
    GPA_F = 0.0

    def __init__(self, name: str, age: int, gender: Gender, student_id: int) -> None:
        self._name: str = name
        self._age: int = age
        self._gender: Gender = gender
        self._student_id: int = student_id
        self._courses: Dict[str, CourseRecord] = {}

    # ----- Properties -----
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, value: Gender) -> None:
        self._gender = value

    @staticmethod
    def _grade_to_gpa(grade: int) -> float:
        if grade >= Student.GRADE_A:
            return Student.GPA_A
        elif grade >= Student.GRADE_B:
            return Student.GPA_B
        elif grade >= Student.GRADE_C:
            return Student.GPA_C
        elif grade >= Student.GRADE_D:
            return Student.GPA_D
        else:
            return Student.GPA_F

    # ----- Functional Methods -----
    def add_course(self, course: CourseRecord) -> None:
        if course.course_code in self._courses:
            print(f"Course {course.course_code} already exists.")
            return
        self._courses[course.course_code] = course

    def calculate_gpa(self) -> float:
        total_points = 0.0
        total_credits = 0

        for course in self._courses.values():
            if course.grade is None:
                continue
            points = self._grade_to_gpa(course.grade)
            total_points += points * course.credit
            total_credits += course.credit

        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)

    def generate_transcript(self) -> str:
        lines = [
            f"Transcript for {self.name} (ID: {self._student_id})",
            "-" * 60,
            f"{"Course":<10}{"Name":<20}{"Grade":<10}{"Credits":<10}{"Semester":<10}{"Year":<5}",
        ]
        for course in self._courses.values():
            grade_str = str(course.grade) if course.grade is not None else "In Progress"
            lines.append(
                f"{course.course_code:<10}{course.course_name:<20}{grade_str:<10}{course.credit:<10}{course.semester.value:<10}{course.year:<5}"
            )
        lines.append("-" * 60)
        lines.append(f"GPA: {self.calculate_gpa():.2f}")
        return "\n".join(lines)

    def has_completed(self, course_code: str) -> bool:
        course = self._courses.get(course_code)
        return (
            course is not None
            and course.grade is not None
            and course.grade >= self.GRADE_D
        )

    def progress(self) -> str:
        total_courses = len(self._courses)
        completed = sum(1 for c in self._courses.values() if c.grade is not None)
        return f"{completed}/{total_courses} courses completed."

    def enforce_prerequisite(
        self, target_course_code: str, prerequisite_course_code: str
    ) -> None:
        if not self.has_completed(prerequisite_course_code):
            raise ValueError(
                f"Cannot enroll in {target_course_code} —"
                f" prerequisite {prerequisite_course_code}"
            )

    def get_courses_by_semester(
        self, year: int, semester: Semester
    ) -> Dict[str, CourseRecord]:
        return {
            code: c
            for code, c in self._courses.items()
            if c.year == year and c.semester == semester
        }


def main():
    student = Student("Alice", 20, Gender.FEMALE, 101)

    student.add_course(CourseRecord("CS101", "Intro to CS", 85, 3, 2023, Semester.FALL))
    student.add_course(CourseRecord("MATH101", "Calculus", 92, 4, 2023, Semester.FALL))
    student.add_course(
        CourseRecord("ENG101", "English", None, 2, 2024, Semester.SPRING)
    )  # In progress

    print(student.generate_transcript())
    print(student.progress())
    print(student.get_courses_by_semester(2023, Semester.FALL))


if __name__ == "__main__":
    main()
