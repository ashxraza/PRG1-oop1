# Glossary

Refer back to this any time you see a term you've forgotten.

| Term | Definition |
|---|---|
| **Class** | A blueprint or template for creating objects. Like a cookie cutter — it defines the shape and structure. |
| **Object** | An individual thing created from a class. Like cookies made from the same cutter — same structure, different values. |
| **Instance** | Another word for an object. Every new object created from a class is an *instance* of that class. |
| **Attribute** (or **Property**) | A piece of data that an object holds (e.g. `name`, `age`, `colour`). |
| **Method** | An action or function that an object can perform (e.g. `talk()`, `walk()`, `calculate()`). |
| **Constructor** | A special method (`__init__` in Python) that runs when a new object is created. It sets up the object's starting attributes. |
| **`self`** | A reference to the current object inside a method. It's how the object refers to itself. |
| **Encapsulation** | Bundling data and methods together, and controlling access to them (using getters and setters). |
| **Inheritance** | Creating a new class based on an existing one. The new class gets all the parent's attributes and methods for free. |
| **Composition** | Building a class that contains objects of another class (e.g. a `Cohort` contains `AdaStudent` objects). |
| **Polymorphism** | Objects of different classes can be used in the same way if they share methods with the same name. |
| **Getter** | A method that returns the value of a private attribute. In Python, often written using `@property`. |
| **Setter** | A method that lets you change the value of a private attribute, often with validation. Written with `@<name>.setter`. |
| **Private attribute** | An attribute intended to be used only inside the class. In Python, we signal this by starting the name with an underscore (e.g. `_name`). |
