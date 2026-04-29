"""
Part 03 — Starter
AdaStaff inherits from Person.
"""

from person import Person


class AdaStaff(Person):  # The (Person) means "AdaStaff inherits from Person"
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        # super() refers to the parent class. This line runs Person's __init__
        # so we don't have to set up name / date_of_birth / place_of_birth ourselves.
        super().__init__(name, date_of_birth, place_of_birth)

        # Now we add the AdaStaff-specific attributes
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


# ---- Try it out ----
teacher = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")

# Methods INHERITED from Person:
print(teacher.talk())
print(admin.talk())

# Methods NEW to AdaStaff:
print(teacher.work())
print(teacher.get_employee_info())
print(admin.work())
print(admin.get_employee_info())
