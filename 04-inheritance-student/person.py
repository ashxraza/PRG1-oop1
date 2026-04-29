"""
The Person class from Part 02.
Other files in this folder import it from here, so we don't have to repeat it.
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
