# Part 05 — Composition: The `Cohort` Class

## What you'll learn
- The difference between **inheritance** and **composition**
- How to make a class that **contains** objects of another class
- How to use `isinstance(...)` to validate object types

> 📖 As always, see `../GLOSSARY.md` for terms.

---

## Inheritance vs Composition

You've used **inheritance** in Parts 03 & 04: *"AdaStudent **is a** Person."*

This part uses **composition**: *"A Cohort **has** many AdaStudents."*

A useful test:
- "**is a**" → use inheritance
- "**has a**" / "**has many**" → use composition

A `Cohort` isn't a special kind of student — it's a *container* of students.

## Files in this folder

| File | What it's for |
|---|---|
| `person.py` | The `Person` class. |
| `students.py` | The `AdaStudent` class (so this folder isn't 200 lines long). |
| `starter.py` | The `Cohort` class with a worked example. |
| `challenge.py` | Your turn — get to **10+ total objects** across the activity. |
| `solution.md` | Hidden answers. |

## Step 1 — Run the starter

```bash
python starter.py
```

## Step 2 — Challenge

`challenge.py` walks you through:
- Creating extra students to reach **10+ total**
- Building a second cohort
- Searching, removing, and calculating averages

---

## What to take away

- Composition is when a class **contains** other objects.
- `isinstance(x, AdaStudent)` checks whether `x` is an `AdaStudent` (or a subclass of one) — useful for validation.
- A `Cohort` doesn't need to know *how* `AdaStudent` works internally — it just calls its methods (`student.name`, `student.get_average_grade()`).
