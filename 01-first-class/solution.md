# Part 01 — Solution

> ⚠️ **Try the challenge first!** Looking at the answers without attempting the work won't help you learn.

<details>
<summary>Click to reveal the solution</summary>

```python
class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth

    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."

    # TODO 4
    def introduce_age(self):
        return f"I was born on {self.date_of_birth}."


# TODO 1
me = Person("Your Name", "01/01/2005", "Your City")

# TODO 2
character = Person("Sherlock Holmes", "06/01/1854", "London")

# TODO 3
print(me.talk())
print(character.talk())

# TODO 5
print(me.introduce_age())
print(character.introduce_age())
```

## Predict answers

1. `Hi, my name is Steve Rich and I was born in London.`
2. `Name: Steve Rich`
3. The `name` attribute on `steve` becomes `"Stephen Rich"`. Everything else stays the same.
4. `"Manchester"`

</details>
