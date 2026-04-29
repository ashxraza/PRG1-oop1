"""
The AdaStudent class from Part 04, kept in its own file so we can import it.
"""

from person import Person


class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def grades(self):
        return list(self._grades)

    def study(self):
        return f"{self.name} is studying {self.course}."

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print(f"Grade {grade} is invalid — must be between 0 and 100.")

    def get_average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    def get_student_info(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Course: {self.course}, "
            f"Average: {self.get_average_grade():.1f}"
        )
