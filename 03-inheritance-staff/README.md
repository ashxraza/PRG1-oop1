# Part 03 — Inheritance: `AdaStaff`

## What you'll learn
- What **inheritance** is and why it saves you work
- How to use `super().__init__(...)` to reuse the parent's setup
- How a child class can *add* new attributes and methods on top of the parent

> 📖 Need a refresher? See `../GLOSSARY.md`.

---

## The idea

A member of staff at Ada **is a person** — they have all the same things (name, date of birth, place of birth) plus some extra things (employee ID, department).

Rather than copy and paste everything from `Person`, we say:

> "`AdaStaff` *inherits from* `Person`. It gets everything Person has, plus what we add."

That's what `class AdaStaff(Person):` means.

## Files in this folder

| File | What it's for |
|---|---|
| `person.py` | The `Person` class from Part 02 (we import it — no need to retype it). |
| `starter.py` | The new `AdaStaff` class with a worked example. |
| `challenge.py` | Your turn — create more staff members. |
| `solution.md` | Hidden answers. |

## Step 1 — Run the starter

```bash
python starter.py
```

Notice the staff object can use `talk()` (inherited from `Person`) AND its own new methods like `work()`.

## Step 2 — Challenge

In `challenge.py` you'll create more `AdaStaff` objects and use both inherited and new methods.

---

## What to take away

- `class Child(Parent):` makes `Child` inherit from `Parent`.
- `super().__init__(...)` calls the parent's constructor so you don't have to redo its setup.
- Child classes can have **extra** attributes and methods on top of what they inherit.
