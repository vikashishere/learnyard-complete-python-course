# fstring basics
name = "Vikash"
age = 28
print(f"My name is {name} and I am {age} years old.")


# fstring with expression
a = 7
b = 3
print(f"{a} x {b} = {a * b}")

# fstring with formatting
price = 49.5678
print(f"Price: ₹{price:.2f}")  # ₹49.57


# Function with docstring
def square(n):
    """Returns the square of a number."""
    return n * n

print(square(4))           # 16
print(square.__doc__)      # Shows docstring


# using help with docstring
def greet(name):
    """Greets the person with the provided name."""
    print(f"Hello, {name}!")

help(greet)

