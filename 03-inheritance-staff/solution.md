# Part 03 — Solution

> ⚠️ **Try the challenge first!**

<details>
<summary>Click to reveal the solution</summary>

```python
from person import Person


class AdaStaff(Person):
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)
        self._employee_id = employee_id
        self._department = department

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    def work(self):
        return f"{self.name} is working in the {self.department} department."

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"

    # TODO 4
    def change_department(self, new_department):
        old = self._department
        self._department = new_department
        return f"{self.name} moved from {old} to {new_department}."


# TODO 1
ben = AdaStaff("Ben Carter", "03/04/1990", "Bristol", "EMP003", "Operations")
priya = AdaStaff("Priya Patel", "18/02/1988", "Glasgow", "EMP004", "Curriculum")

# TODO 2
for staff in (ben, priya):
    print(staff.talk())
    print(staff.work())
    print(staff.get_employee_info())
    print("---")

# TODO 3
ben.name = "Ben Carter-Reed"
print(ben.talk())

# TODO 4
print(priya.change_department("Operations"))
```

</details>
