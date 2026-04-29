# Part 06 — Solution

> ⚠️ **Try the challenge first!**

<details>
<summary>Click to reveal the solution</summary>

```python
from staff import AdaStaff
from students import AdaStudent
from cohort import Cohort


# TODO 1 — staff
alice = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
zara = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")

# TODO 2 — students
emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
sarah = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
michael = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")
amina = AdaStudent("Amina Khan", "30/01/2003", "Leicester", "STU005", "Data Science")
tom = AdaStudent("Tom Edwards", "09/06/2002", "Sheffield", "STU006", "Product Management")
chloe = AdaStudent("Chloe Reeves", "21/04/2003", "Cardiff", "STU007", "Software Development")
daniel = AdaStudent("Daniel Park", "11/08/2002", "Belfast", "STU008", "Cybersecurity")

# TODO 3 — grades
for student, grades in [
    (emma, [85, 92, 78]),
    (james, [70, 74, 80]),
    (sarah, [88, 91, 95]),
    (michael, [76, 84, 89]),
    (amina, [82, 77, 90]),
    (tom, [65, 72, 68]),
    (chloe, [95, 89, 91]),
    (daniel, [70, 74, 68]),
]:
    for g in grades:
        student.add_grade(g)

# TODO 4 — cohorts
dev_a = Cohort("DEV2024A")
for s in (emma, james, sarah, michael):
    dev_a.add_student(s)

dev_b = Cohort("DEV2024B")
for s in (amina, tom, chloe, daniel):
    dev_b.add_student(s)

# TODO 5 — report
for cohort in (dev_a, dev_b):
    print(f"=== {cohort.cohort_code} ===")
    print(cohort.list_students())
    print(f"Average: {cohort.get_cohort_average():.1f}\n")

# TODO 6 — staff summary
print("=== Staff ===")
for staff in (alice, zara):
    print(staff.work())

# TODO 7 — top student
def top_student(cohort):
    students = [cohort.search_student(s.split(" (")[0]) for s in cohort.list_students().split("\n")[1:-1]]
    students = [s for s in students if s]
    if not students:
        return None
    return max(students, key=lambda s: s.get_average_grade())

# Cleaner version using direct access (we'd normally add a .students property to Cohort):
def top_student_clean(cohort):
    # Add this property to Cohort:
    #   @property
    #   def students(self):
    #       return list(self._students)
    return max(cohort.students, key=lambda s: s.get_average_grade())

print(f"Top in DEV2024A: {top_student(dev_a).name}")
print(f"Top in DEV2024B: {top_student(dev_b).name}")
```

## Object count

- Staff: 2
- Students: 8
- Cohorts: 2

**Total: 12 objects** ✅

</details>
