"""
Part 02 — Challenge
Experiment with encapsulation by deliberately breaking the rules.

For each TODO, predict what will happen FIRST, then run the code to find out.
You may need to comment lines in/out one at a time to see each error.
"""


class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth
        self._place_of_birth = place_of_birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name or not new_name.strip():
            raise ValueError("Name cannot be empty")
        self._name = new_name.strip()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def place_of_birth(self):
        return self._place_of_birth

    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


# Create a Person to experiment with
person = Person("Alex Smith", "10/10/2003", "Cardiff")
print(person.talk())


# TODO 1: Change the person's name to "Alexandra Smith" using the setter.
#         Then print the new name.


# TODO 2: Try to set the name to an empty string "".
#         What error do you get? Wrap the line in try/except so the program continues.
#
# Example:
# try:
#     person.name = ""
# except ValueError as e:
#     print(f"Caught error: {e}")


# TODO 3: Try to change the date_of_birth.
#         (e.g. person.date_of_birth = "01/01/1999")
#         What kind of error happens, and why?
#         Wrap it in try/except so the program continues.


# TODO 4: Try to change the place_of_birth in the same way.
#         Same error?


# TODO 5: Add a NEW property to the class above called `age_in_years`
#         that calculates a (rough) age based on the year part of date_of_birth.
#         Hint: date_of_birth is a string like "01/01/2000".
#         You can split it on "/" and use the year. Use 2026 as "now".
#         Make it a getter only (no setter — your age isn't something you can just set!).
#         Then print person.age_in_years.
