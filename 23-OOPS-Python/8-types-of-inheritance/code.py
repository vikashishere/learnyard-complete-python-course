# 1️⃣ Single Inheritance -> A single child class inherits from one parent class.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


# 2️⃣ Multiple Inheritance -> A child class inherits from more than one parent class.
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def hobbies(self):
        print("Cooking, Painting")

class Child(Father, Mother):  # Multiple inheritance
    def play(self):
        print("Playing Football")

c = Child()
c.skills()
c.hobbies()
c.play()


# 3️⃣ Multilevel Inheritance -> A class inherits from a class that itself inherits from another class. A → B → C.
class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's Car")

class Child(Parent):  # Multilevel inheritance
    def bike(self):
        print("Child's Bike")

c = Child()
c.house()
c.car()
c.bike()


# 4️⃣ Hierarchical Inheritance -> Multiple child classes inherit from a single parent class.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bike(Vehicle):
    def ride(self):
        print("Riding a bike")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()


# 5️⃣ Hybrid Inheritance -> Combination of multiple types of inheritance.
# Often includes multiple + multilevel + hierarchical together.
class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):  # Hybrid Inheritance (Multilevel + Multiple)
    def show_D(self):
        print("Class D")

d = D()
d.show_A()  # Inherited from A
d.show_B()  # From B
d.show_C()  # From C
d.show_D()  # Own
