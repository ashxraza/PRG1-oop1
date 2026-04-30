"""
Part 04 — Challenge
Create more students — you need at least 4 more so your total reaches 6+.
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
    def highest_grade(self):
        if not self._grades:
            return None
        return max(self._grades)


# We'll start you off with two students
emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")


# TODO 1: Create AT LEAST 4 more AdaStudent objects.
#         Use a mixture of courses (e.g. Software Development, Data Science,
#         Cybersecurity, Product Management).

nour = AdaStudent("Nour Miah", "13/01/2002", "Manchester", "STU003", "Project Management")
jamal = AdaStudent("Jamal Begum", "09/11/2001", "London", "STU004", "Aerospace Engineering")
inaya = AdaStudent("Inaya Raza", "31/03/2002", "Manchester", "STU005", "Accounting")
ayan = AdaStudent("Ayan Raza", "31/03/2002", "Manchester", "STU006", "Medicine")


# TODO 2: Add some grades (between 0 and 100) to each student.
#         Give each student at least 3 grades.

emma.add_grade(56); emma.add_grade(72); emma.add_grade(78)
james.add_grade(70); james.add_grade(74); james.add_grade(80)
nour.add_grade(70);nour.add_grade(80);nour.add_grade(87);
jamal.add_grade(40);jamal.add_grade(50);jamal.add_grade(65);
inaya.add_grade(80);inaya.add_grade(87);inaya.add_grade(95);
ayan.add_grade(63);ayan.add_grade(81);ayan.add_grade(92);

students = [emma, james, nour, jamal, inaya, ayan]

# TODO 3: Print the get_student_info() of every student so you can compare averages.

for student in students:
    print(f"{student.name}: {student.get_student_info()}")

# TODO 4: Find and print the name of the student with the highest average grade.
#         Hint: put all your students in a list and loop through it.



top_student = max(students, key=lambda s: s.get_average_grade())
print(f"Top student: {top_student.name} with average {top_student.get_average_grade():.1f}")


# TODO 5 (stretch): Add a new method `highest_grade()` to AdaStudent that returns
#         the student's highest grade, or None if they have no grades yet.
#         Test it on a couple of students.
print(f"Emma's highest grade: {emma.highest_grade()}")
print(f"James's highest grade: {james.highest_grade()}")
print(f"Nour's highest grade: {nour.highest_grade()}")
print(f"Jamal's highest grade: {jamal.highest_grade()}")
print(f"Inaya's highest grade: {inaya.highest_grade()}")
print(f"Ayan's highest grade: {ayan.highest_grade()}")