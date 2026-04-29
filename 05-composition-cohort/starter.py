"""
Part 05 — Starter
A Cohort contains AdaStudent objects (composition).
"""

from students import AdaStudent


class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self._students = []  # The list of AdaStudent objects

    def add_student(self, student):
        # isinstance() checks the object IS an AdaStudent (or subclass).
        # This stops someone accidentally adding a string or a Person etc.
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
        # Returns the AdaStudent object, or None if not found
        for student in self._students:
            if student.name.lower() == student_name.lower():
                return student
        return None

    def get_cohort_average(self):
        averages = [s.get_average_grade() for s in self._students if s.get_average_grade() > 0]
        if not averages:
            return 0
        return sum(averages) / len(averages)


# ---- Try it out ----
emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
sarah = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
michael = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")

# Add some grades
emma.add_grade(85); emma.add_grade(92)
sarah.add_grade(88); sarah.add_grade(91)
michael.add_grade(76); michael.add_grade(84); michael.add_grade(89)

# Build a cohort
dev2024a = Cohort("DEV2024A")
dev2024a.add_student(emma)
dev2024a.add_student(james)
dev2024a.add_student(sarah)
dev2024a.add_student(michael)

print(dev2024a.list_students())
print(f"Cohort average: {dev2024a.get_cohort_average():.1f}")

# Try adding something that's NOT an AdaStudent
dev2024a.add_student("not a student")  # Should be rejected
