# Why Object-Oriented Programming?

Now you've built classes, used inheritance, and composed objects together — let's zoom out and look at *why* OOP exists.

## What is OOP?

**Object-Oriented Programming (OOP)** is a way of organising code around **objects** rather than around functions. Each object bundles together:
- **Data** (its attributes — what it knows)
- **Behaviour** (its methods — what it can do)

## The Four Core Principles

### 1. Encapsulation
Bundling data and methods together, and controlling how the outside world accesses them.

> You used this in **Part 02** when you made `_name`, `_date_of_birth`, and `_place_of_birth` private and exposed them through `@property`.

### 2. Inheritance
Creating new classes based on existing ones, so you don't have to repeat yourself.

> You used this in **Parts 03 & 04** — `AdaStaff` and `AdaStudent` both inherit from `Person` and get `talk()` for free.

### 3. Polymorphism
Objects of different classes can be used in the same way if they share methods with the same name.

> Both an `AdaStaff` and an `AdaStudent` respond to `.talk()` — even though they're different classes. You can treat them the same when you only care about the behaviour they share.

### 4. Composition
Building complex objects by combining simpler ones.

> You used this in **Part 05** — a `Cohort` *has* a list of `AdaStudent` objects.

## Why bother?

| Benefit | What it means |
|---|---|
| **Modularity** | Code is broken into logical, reusable units. |
| **Reusability** | Classes can be reused and extended in new projects. |
| **Maintainability** | Changing one class doesn't break others. |
| **Real-world modelling** | Objects often map naturally to real-world things (people, cohorts, products, orders…). |

## A final matching exercise

Match each keyword to its definition. Check yourself against the glossary if needed.

**Keywords:** Class · Object · Method · Attribute · Instance

**Definitions:**
- A. The individual properties of an object
- B. A collection of data and its associated actions
- C. The blueprint for an object
- D. The associated actions of an object
- E. Every new object created from the same blueprint

<details>
<summary>Click for answers</summary>

- Class = **C**
- Object = **B**
- Method = **D**
- Attribute = **A**
- Instance = **E**

</details>

## 🎉 Well done!

You've successfully:
- Created multiple classes with inheritance
- Implemented encapsulation with getters and setters
- Used composition to build complex relationships
- Created 10+ objects
- Learned the fundamental principles of OOP
