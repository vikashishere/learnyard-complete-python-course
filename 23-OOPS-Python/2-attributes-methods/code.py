# ✅ Example 1: Instance Attributes & Method

class Student:
    def __init__(self, name, grade):
        self.name = name         # instance attribute
        self.grade = grade       # instance attribute

    def introduce(self):         # method
        print(f"Hi, I'm {self.name} and I’m in grade {self.grade}.")


s1 = Student("Arjun", 8)
s2 = Student("Maya", 10)

s1.introduce()   # Hi, I'm Arjun and I’m in grade 8.
s2.introduce()   # Hi, I'm Maya and I’m in grade 10.



# ✅ Example 2: Class Attributes
class Car:
    wheels = 4  # class attribute

    def __init__(self, brand):
        self.brand = brand  # instance attribute

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)    # Toyota
print(car1.wheels)   # 4
print(car2.wheels)   # 4

# Modify class attribute (not common)
Car.wheels = 6
print(car1.wheels)   # 6



# ✅ Example 3: Multiple Methods
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")


