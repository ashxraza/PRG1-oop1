"""
Part 03 — Challenge
Create more AdaStaff members and explore inheritance.
"""

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
    
    def change_department(self, new_department):
        old = self._department
        self._department = new_department
        return f"{self.name} moved from {old} to {new_department}."


# TODO 1: Create TWO more AdaStaff objects with different details.
#         (Different names, departments, employee IDs.)

Henry = AdaStaff("Henry Hart", "19/07/2002", "Miami", "STAFF-01", "Physcology")
Miles = AdaStaff("Miles Morales", "28/04/2008", "New York", "STAFF-02", "Safeguarding")

# TODO 2: For each of your two staff members, print:
#         - their .talk() result (inherited from Person)
#         - their .work() result (defined in AdaStaff)
#         - their .get_employee_info() result

for staff in (Henry, Miles):
    print(staff.talk())
    print(staff.work())
    print(staff.get_employee_info())
    print("---")


# TODO 3: One of your staff members has just got married and changed their name.
#         Use the setter to update their name, then print .talk() again to confirm.

Henry.name = "Henry Hart-Chalamet"
print(Henry.talk())


# TODO 4 (stretch): Add a new method to AdaStaff called `change_department(new_department)`
#         that updates the department and returns a confirmation string like:
#         "Alice Johnson moved from Education to Operations."
#         Test it on one of your staff members.
print(Miles.change_department("Defence"))