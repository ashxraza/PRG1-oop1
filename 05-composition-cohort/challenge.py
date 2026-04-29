"""
Part 05 — Challenge
Build out cohorts and reach 10+ total objects.
"""

from students import AdaStudent


class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self._students = []

    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self._students.append(student)
            print(f"Added {student.name} to {self.cohort_code}")
        else:
            print("Can only add AdaStudent objects to a cohort")

    def remove_student(self, student_name):
        for student in self._students:
            if student.name == student_name:
                self._students.remove(student)
                print(f"Removed {student_name} from {self.cohort_code}")
                return
        print(f"Student '{student_name}' not found in {self.cohort_code}")

    def list_students(self):
        if not self._students:
            return f"No students in {self.cohort_code}"
        result = f"Students in {self.cohort_code}:\n"
        for student in self._students:
            result += f"- {student.name} ({student.course})\n"
        return result

    def search_student(self, student_name):
        for student in self._students:
            if student.name.lower() == student_name.lower():
                return student
        return None

    def get_cohort_average(self):
        averages = [s.get_average_grade() for s in self._students if s.get_average_grade() > 0]
        if not averages:
            return 0
        return sum(averages) / len(averages)


# Some students to start you off
emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
sarah = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
michael = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")

emma.add_grade(85); emma.add_grade(92)
sarah.add_grade(88); sarah.add_grade(91)
michael.add_grade(76); michael.add_grade(84); michael.add_grade(89)


# TODO 1: Create at least 4 more AdaStudent objects so you have 8+ in total.
#         Give them grades.


# TODO 2: Create a first Cohort called "DEV2024A" and add the first 4 students to it.


# TODO 3: Create a second Cohort called "DEV2024B" and add the rest of your students to it.


# TODO 4: Print the list of students in each cohort.


# TODO 5: Use search_student() to find one of your students by name and print their info.


# TODO 6: Remove a student from one cohort, then print the cohort list again to confirm.


# TODO 7: Print the average grade of each cohort.


# TODO 8 (stretch): Try to add a string (e.g. "hello") to a cohort.
#         What happens? Why is the isinstance() check important?
