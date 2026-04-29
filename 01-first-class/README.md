# Part 01 — Your First Class: `Person`

## What you'll learn
- What a **class** is and how to define one
- What **objects** (instances) are
- How a **constructor** (`__init__`) works
- How to define **attributes** and **methods**

> 📖 **New term?** Check `../GLOSSARY.md` any time.

---

## Step 1 — Predict

Open `starter.py` but **don't run it yet**. Read through the code, then answer these questions in your head (or on paper):

1. What will be printed by `print(steve.talk())`?
2. What will `print(f"Name: {steve.name}")` show?
3. After running `steve.name = "Stephen Rich"`, what does the `steve` object look like?
4. What does `aqil.place_of_birth` contain?

## Step 2 — Run

Now run `starter.py`:

```bash
python starter.py
```

Did your predictions match? If anything surprised you, that's a good thing — go back and read the code again to figure out why.

## Step 3 — Challenge

Open `challenge.py` and complete the tasks marked with `# TODO`. The file already imports the `Person` class for you.

## Step 4 — Check

When you're done, you can compare against `solution.md` — but **try the challenge yourself first!**

---

## What to take away

- A **class** (`Person`) is a blueprint.
- An **object** is a thing made from that blueprint (`aqil`, `steve`).
- The **constructor** `__init__` runs when you create the object — it's where you set up its starting attributes.
- `self` is how the object refers to its own attributes inside its methods.
