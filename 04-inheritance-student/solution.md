# Part 04 — Solution

> ⚠️ **Try the challenge first!**

<details>
<summary>Click to reveal the solution</summary>

```python
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

    # TODO 5
    def highest_grade(self):
        if not self._grades:
            return None
        return max(self._grades)


emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")

# TODO 1
sarah = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
michael = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")
amina = AdaStudent("Amina Khan", "30/01/2003", "Leicester", "STU005", "Data Science")
tom = AdaStudent("Tom Edwards", "09/06/2002", "Sheffield", "STU006", "Product Management")

# TODO 2
emma.add_grade(85); emma.add_grade(92); emma.add_grade(78)
james.add_grade(70); james.add_grade(74); james.add_grade(80)
sarah.add_grade(88); sarah.add_grade(91); sarah.add_grade(95)
michael.add_grade(76); michael.add_grade(84); michael.add_grade(89)
amina.add_grade(82); amina.add_grade(77); amina.add_grade(90)
tom.add_grade(65); tom.add_grade(72); tom.add_grade(68)

students = [emma, james, sarah, michael, amina, tom]

# TODO 3
for student in students:
    print(f"{student.name}: {student.get_student_info()}")

# TODO 4
top_student = max(students, key=lambda s: s.get_average_grade())
print(f"Top student: {top_student.name} with average {top_student.get_average_grade():.1f}")

# TODO 5
print(f"Emma's highest grade: {emma.highest_grade()}")
print(f"James's highest grade: {james.highest_grade()}")
```

</details>
