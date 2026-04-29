# Part 02 — Solution

> ⚠️ **Try the challenge first!**

<details>
<summary>Click to reveal the solution</summary>

```python
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

    # TODO 5
    @property
    def age_in_years(self):
        year_of_birth = int(self._date_of_birth.split("/")[2])
        return 2026 - year_of_birth

    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."


person = Person("Alex Smith", "10/10/2003", "Cardiff")
print(person.talk())

# TODO 1
person.name = "Alexandra Smith"
print(person.name)

# TODO 2
try:
    person.name = ""
except ValueError as e:
    print(f"Caught error: {e}")

# TODO 3
try:
    person.date_of_birth = "01/01/1999"
except AttributeError as e:
    print(f"Caught error: {e}")

# TODO 4
try:
    person.place_of_birth = "Birmingham"
except AttributeError as e:
    print(f"Caught error: {e}")

# TODO 5
print(f"Age: {person.age_in_years}")
```

## What's going on with the errors?

- **TODO 2** raises a `ValueError` because *we* chose to raise it inside our setter. We wrote the rule.
- **TODO 3 & 4** raise an `AttributeError` because there's *no setter at all*. Python won't let you assign to a property that only has a getter. That's how you make something truly read-only.

</details>
