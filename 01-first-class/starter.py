"""
Part 01 — Starter
Your first class: Person.

PREDICT what each print statement will output BEFORE running this file!
"""


class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        # These three are attributes of the object.
        # `self` means "this particular object".
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth

    def talk(self):
        # A method — an action this object can perform.
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


# Create two objects (instances) of the Person class
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")

# Use the objects
print(steve.talk())
print(aqil.talk())

# Access attributes directly
print(f"Name: {steve.name}")
print(f"Date of birth: {steve.date_of_birth}")
print(f"Place of birth: {steve.place_of_birth}")

# Attributes can be reassigned (we'll fix this in Part 02!)
steve.name = "Stephen Rich"
print(f"Updated name: {steve.name}")
