"""
Part 01 — Challenge
Practise creating classes and objects.

Complete each TODO. Run this file when you're done to test your work.
"""


class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth

    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."
    
    def introduce_age(self):
        return f"I was born on {self.date_of_birth}"


# TODO 1: Create a Person object representing yourself.
#         Call the variable `me`.
me = Person("Adarsh Radhesh", "09/07/2005", "Thrissur")

# TODO 2: Create a Person object for a fictional character of your choice.
lelouch = Person("Lelouch vi Britannia", "05/12/1999", "Tokyo")

# TODO 3: Print the result of calling .talk() on both objects.
print(me.talk())
print(lelouch.talk())


# TODO 4: Add a new method to the Person class called `introduce_age()`
#         that returns a string like:
#         "I was born on 01/01/2000."
#         (You'll need to scroll up and edit the class definition.)


# TODO 5: Call your new introduce_age() method on both objects and print the results.

print(me.introduce_age())
print(lelouch.introduce_age())