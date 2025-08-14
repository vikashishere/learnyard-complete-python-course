# Syntax & Basic Example

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):  # Method Overriding
        print(f"{self.name} barks!")

dog = Dog("Buddy")
dog.speak()  # Buddy barks!


# Constructor Overloading (via Default Args): Python does not support traditional constructor 
# overloading like Java or C++. Instead, you simulate it using default parameters or *args/**kwargs.

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

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))        # 2
print(calc.add(2, 3))     # 5
print(calc.add(2, 3, 4))  # 9



# super() in Inheritance - Use super() to call methods from the parent class.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def start(self):
        super().start()  # Call parent method
        print(f"{self.model} is ready to drive!")

car = Car("Toyota", "Corolla")
car.start()



# Mini Project: Inheritance-Based School Management
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
