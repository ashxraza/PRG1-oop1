"""
Part 04 — Starter
AdaStudent inherits from Person and manages a list of grades.
"""

from person import Person


class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []  # Start with an empty grades list

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def grades(self):
        # Return a *copy* so outside code can't accidentally modify our list
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


# ---- Try it out ----
emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")

# Inherited from Person
print(emma.talk())
# New on AdaStudent
print(emma.study())

# Add some grades
emma.add_grade(85)
emma.add_grade(92)
emma.add_grade(78)

# Try an invalid grade
emma.add_grade(150)  # Should be rejected!

print(emma.get_student_info())
print(james.get_student_info())  # James has no grades yet — average will be 0
