# Part 02 — Encapsulation: Getters and Setters

## What you'll learn
- Why we don't want every attribute to be freely changeable
- How to make attributes **private** (using `_underscore`)
- How to expose them safely with `@property` (getter) and `@<name>.setter`
- How to **validate** values when they're set

> 📖 Need a refresher on what "encapsulation" means? Check `../GLOSSARY.md`.

---

## The problem with Part 01

In Part 01, this worked fine:

```python
steve.name = "Stephen Rich"          # OK — people change names
steve.place_of_birth = "Birmingham"  # ⚠️ But you can't change where you were born!
steve.name = ""                      # ⚠️ And an empty name is nonsense.
```

Direct attribute access gives us **no protection**. Encapsulation lets us decide:
- Which attributes can be changed (and which are fixed forever)
- What rules new values must follow

## Step 1 — Read

Open `starter.py` and read through the new `Person` class carefully. Notice:
- Attributes now start with `_` to mark them as private
- `@property` defines a **getter**
- `@name.setter` defines a **setter** with validation
- `date_of_birth` and `place_of_birth` have getters but **no setters** — making them read-only

## Step 2 — Run

Run the starter:

```bash
python starter.py
```

## Step 3 — Experiment

Open `challenge.py` and try the experiments. You'll deliberately try to break things to see Python's protection in action.

## Step 4 — Check

Compare with `solution.md` once you've finished.

---

## What to take away

- A leading underscore (`_name`) is a convention meaning "don't touch this directly".
- `@property` makes a method *look* like an attribute when you read it.
- `@<name>.setter` runs your code whenever someone tries to *change* it — perfect for validation.
- No setter = **read-only**.
