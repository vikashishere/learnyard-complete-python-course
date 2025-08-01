# A simple func
def say_hello():
    print("Hello, World!")

say_hello()


# Func with one arg
def square(num):
    return num * num

print(square(4))  # Output: 16


# Func with default arg
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()             # Welcome, Guest!
greet("Vikash")     # Welcome, Vikash!


# *args example
def total_marks(*scores):
    print(f"Total: {sum(scores)}")

total_marks(85, 90, 88)  # Total: 263


# *kwargs example
def student_profile(**details):
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

student_profile(name="Anjali", grade="A", age=15)



# mixing all types
def show_data(name, *marks, age=18, **info):
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Age: {age}")
    print("Extra Info:")
    for k, v in info.items():
        print(f"  {k}: {v}")

show_data("Vikash", 87, 92, 79, age=20, city="Ranchi", course="Python")
