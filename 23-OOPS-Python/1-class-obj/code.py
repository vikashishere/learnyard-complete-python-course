# ✅ Step 1: Define a Class
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def greet(self):  # method
        print(f"Hi, my name is {self.name} and I’m {self.age} years old.")

# __init__ is a constructor method, called when an object is created.
# self refers to the instance (object) of the class.
# name and age are attributes of the object.
# greet() is a method (function inside class).
        

# ✅ Step 2: Create Objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.greet()  # Output: Hi, my name is Alice and I’m 25 years old.
person2.greet()  # Output: Hi, my name is Bob and I’m 30 years old.

# You can also access or update object properties directly:
print(person1.name)      # Alice
person1.age = 26         # Update age
print(person1.age)       # 26
