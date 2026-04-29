"""
Part 02 — Starter
The Person class, now with encapsulation.

Read the comments carefully — there's a lot of new syntax here, but each
piece does a small, specific job.
"""


class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        # The leading underscore is a convention meaning "private".
        # Outside code shouldn't touch these directly — it should use
        # the getters and setters below.
        self._name = name
        self._date_of_birth = date_of_birth
        self._place_of_birth = place_of_birth

    # ---------- name: getter + setter (so it CAN be changed, with validation) ----------
    @property
    def name(self):
        # This is the GETTER. It runs whenever someone reads `person.name`.
        return self._name

    @name.setter
    def name(self, new_name):
        # This is the SETTER. It runs whenever someone writes `person.name = ...`.
        # We use it to validate the new value before accepting it.
        if not new_name or not new_name.strip():
            raise ValueError("Name cannot be empty")
        self._name = new_name.strip()

    # ---------- date_of_birth: getter only (read-only) ----------
    @property
    def date_of_birth(self):
        return self._date_of_birth

    # ---------- place_of_birth: getter only (read-only) ----------
    @property
    def place_of_birth(self):
        return self._place_of_birth

    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


# ---- Try it out ----
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")

print(steve.talk())
print(f"Name: {steve.name}")
print(f"Date of birth: {steve.date_of_birth}")
print(f"Place of birth: {steve.place_of_birth}")

# We CAN still change the name — but the setter will validate it.
steve.name = "Stephen Rich"
print(f"Updated name: {steve.name}")
