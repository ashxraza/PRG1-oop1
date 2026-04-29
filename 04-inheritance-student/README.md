# Part 04 — Inheritance: `AdaStudent`

## What you'll learn
- How a class can manage a **list-based** attribute (grades)
- Using methods to safely add to and read from that list
- Reinforcing inheritance from `Person`

> 📖 Reminder: see `../GLOSSARY.md` for any terms.

---

## The idea

Just like `AdaStaff`, an `AdaStudent` *is a* `Person`. They have all the basic Person attributes plus:
- A `student_id`
- A `course`
- A list of `grades`

The interesting bit this time is the **grades list**: we want to add grades one at a time, calculate an average, and prevent invalid grades being added.

## Files in this folder

| File | What it's for |
|---|---|
| `person.py` | The `Person` class (imported by the others). |
| `starter.py` | The `AdaStudent` class with a worked example. |
| `challenge.py` | Your turn — create lots of students. |
| `solution.md` | Hidden answers. |

## Step 1 — Run the starter

```bash
python starter.py
```

## Step 2 — Challenge

Open `challenge.py`. The challenge asks you to create **at least 4 more students** (so combined with the 2 in starter, you'll have 6+ student objects, plus the 2 staff from Part 03 — you're well on your way to 10 objects total!).

---

## What to take away

- A class can hold a **list** as an attribute and provide methods to manage it.
- Validation isn't only for setters — any method can check inputs (`add_grade` rejects invalid values).
- Helper methods like `get_average_grade()` keep calculations *inside* the class, where they belong.
