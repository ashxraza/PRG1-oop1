"""
The Cohort class from Part 05.
"""

from students import AdaStudent


class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self._students = []

    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self._students.append(student)
        else:
            print("Can only add AdaStudent objects to a cohort")

    def remove_student(self, student_name):
        for student in self._students:
            if student.name == student_name:
                self._students.remove(student)
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
