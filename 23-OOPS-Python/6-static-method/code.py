# static_method_demo.py

"""
Part 1: Understanding Static Methods in Python OOP
--------------------------------------------------
- Instance methods (self): work with object data
- Class methods (cls): work with class-level data
- Static methods: don't need self or cls. Behave like normal functions but
  are grouped inside a class for logical reasons.

Use @staticmethod decorator when:
- The method is related to the class but doesn’t need object/class data.
"""

class MathHelper:
    # Instance method (needs self)
    def square(self, x):
        return x * x

    # Class method (needs cls)
    @classmethod
    def describe(cls):
        return "This class helps with math operations"

    # Static method (no self, no cls)
    @staticmethod
    def add(a, b):
        return a + b


# --- Demo ---
helper = MathHelper()
print("Square of 4 (instance method):", helper.square(4))
print("Class description (class method):", MathHelper.describe())
print("Add two numbers (static method):", MathHelper.add(5, 7))
# Notice: We can call add() using class itself, no object required!


"""
Part 2: Mini Project - Using Static Method as a Counter
-------------------------------------------------------
We will create a class `User`. Every time we create a new user object,
we want to assign a unique user ID. We'll use a static method to manage
the counter of IDs.
"""

class User:
    counter = 0   # class variable to keep track of total users

    def __init__(self, name):
        # assign unique id by calling static method
        self.id = User._generate_id()
        self.name = name

    @staticmethod
    def _generate_id():
        """
        Static method that increments the counter
        and returns a new unique ID.
        """
        User.counter += 1
        return User.counter


# --- Demo ---
u1 = User("Alice")
u2 = User("Bob")
u3 = User("Charlie")

print(f"{u1.name} has ID {u1.id}")
print(f"{u2.name} has ID {u2.id}")
print(f"{u3.name} has ID {u3.id}")

# The counter has increased each time we created a new User object
print("Total Users created:", User.counter)
