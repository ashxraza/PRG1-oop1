# Part 06 — Final Challenge: Putting It All Together

You've built each piece individually. Now use them all at once.

## What's in this folder

| File | What it's for |
|---|---|
| `person.py` | The `Person` base class. |
| `staff.py` | The `AdaStaff` class. |
| `students.py` | The `AdaStudent` class. |
| `cohort.py` | The `Cohort` class. |
| `challenge.py` | The starter file for your final scenario. |
| `solution.md` | Hidden solution. |

> **Notice the structure.** A real Python project keeps related classes in their own files and imports them where needed. That's exactly what we're doing here.

## The scenario

You're building a tiny "school management" script for Ada. By the end of `challenge.py` you should have:

- ✅ At least **2 staff members** (`AdaStaff`)
- ✅ At least **8 students** (`AdaStudent`) — bringing your total objects to **10+**
- ✅ At least **2 cohorts** (`Cohort`) populated with students
- ✅ A short report printed to the terminal showing each cohort, its students, and its average

## Step 1 — Open `challenge.py`

Follow the TODOs in order. Each one builds on the last.

## Step 2 — Run it

```bash
python challenge.py
```

## Step 3 — Reflect

Once your script runs cleanly, open `../WHY_OOP.md` and read it. Each principle there should now feel familiar — you've used every one of them.

## ✅ Final checklist

- [ ] I can define **Class**, **Object**, **Constructor**, **Method**, and **Attribute**
- [ ] I have built **Person**, **AdaStaff**, **AdaStudent**, and **Cohort**
- [ ] I have created at least **10 objects** total
- [ ] I understand **inheritance** (AdaStaff and AdaStudent inherit from Person)
- [ ] I understand **composition** (Cohort contains AdaStudent objects)
- [ ] I understand **encapsulation** and why we use getters/setters
- [ ] I can explain what Object-Oriented Programming means
