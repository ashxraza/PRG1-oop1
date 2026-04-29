# Part 05 — Solution

> ⚠️ **Try the challenge first!**

<details>
<summary>Click to reveal the solution</summary>

```python
from students import AdaStudent

# (Cohort class as in challenge.py)

emma = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
james = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
sarah = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
michael = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")
emma.add_grade(85); emma.add_grade(92)
sarah.add_grade(88); sarah.add_grade(91)
michael.add_grade(76); michael.add_grade(84); michael.add_grade(89)

# TODO 1
amina = AdaStudent("Amina Khan", "30/01/2003", "Leicester", "STU005", "Data Science")
tom = AdaStudent("Tom Edwards", "09/06/2002", "Sheffield", "STU006", "Product Management")
chloe = AdaStudent("Chloe Reeves", "21/04/2003", "Cardiff", "STU007", "Software Development")
daniel = AdaStudent("Daniel Park", "11/08/2002", "Belfast", "STU008", "Cybersecurity")

for student, grades in [
    (amina, [82, 77, 90]),
    (tom, [65, 72, 68]),
    (chloe, [95, 89, 91]),
    (daniel, [70, 74, 68]),
]:
    for g in grades:
        student.add_grade(g)

# TODO 2
dev_a = Cohort("DEV2024A")
for s in (emma, james, sarah, michael):
    dev_a.add_student(s)

# TODO 3
dev_b = Cohort("DEV2024B")
for s in (amina, tom, chloe, daniel):
    dev_b.add_student(s)

# TODO 4
print(dev_a.list_students())
print(dev_b.list_students())

# TODO 5
found = dev_a.search_student("Emma Wilson")
if found:
    print(found.get_student_info())

# TODO 6
dev_a.remove_student("James Brown")
print(dev_a.list_students())

# TODO 7
print(f"DEV2024A average: {dev_a.get_cohort_average():.1f}")
print(f"DEV2024B average: {dev_b.get_cohort_average():.1f}")

# TODO 8
dev_a.add_student("hello")  # Rejected — isinstance() catches it
```

## Why does the `isinstance` check matter?

Without it, a `Cohort` could end up containing strings, numbers, or anything else. Then when you call `student.name` or `student.get_average_grade()` inside `list_students()` or `get_cohort_average()`, the program would crash. The check is a small safety net at the **boundary** of the class.

</details>
