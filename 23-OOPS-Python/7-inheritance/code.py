"""
INHERITANCE IN PYTHON OOP
-------------------------
- Inheritance allows one class (child/derived) to reuse code from another class (parent/base).
- Benefits:
  * Code reuse
  * Easier maintenance
  * Models real-world relationships (IS-A relationship)
"""

# =========================================================
# Example 1: Simple Inheritance
# =========================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

# Cat class inherits from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")


# --- Demo ---
print("Example 1: Simple Inheritance")
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()   # Buddy barks!
cat.speak()   # Whiskers meows!


# =========================================================
# Example 2: Method Overloading
# =========================================================

class Person:
    def __init__(self, name="Unknown", age=None):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Alice", 25)
p2 = Person("Bob")
p3 = Person()

p1.display()  # Name: Alice, Age: 25
p2.display()  # Name: Bob, Age: None
p3.display()  # Name: Unknown, Age: None

# Method Overloading (Simulated in Python)
# Python does not support method overloading by argument count like some languages. Instead, use default values or *args.
# Another example below with Calculator class

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))        # 2
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9


# =========================================================
# Example 3: Using super() and Method Overriding
# =========================================================
class Vehicle:
    def __init__(self):
        self.brand = 'brand-X'
        self.warranty = '10yrs'

    def description(self):
        return f"Vehicle: {self.brand} {self.model}"

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, model, doors):
        # super() calls the parent constructor
        super().__init__()
        self.model = model
        self.doors = doors

    # Override description method
    def description(self):
        return f"Car: {self.brand} <--> {self.model}, {self.doors}-door, {self.warranty}-warranty"

# --- Demo ---
print("\nExample 2: super() and Method Overriding")
car = Car("mini", 4)
print(car.description())


# =========================================================
# Mini Project: Inheritance-Based School Management
# =========================================================
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def show(self):
        super().show()
        print(f"Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        super().show()
        print(f"Subject: {self.subject}")

s1 = Student("Ravi", "7th")
t1 = Teacher("Ms. Sinha", "Math")

s1.show()
print("---")
t1.show()
