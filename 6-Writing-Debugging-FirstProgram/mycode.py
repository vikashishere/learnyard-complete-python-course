# --------------------------------------------
# 💬 COMMENTS, PRINT STATEMENTS & ESCAPE SEQUENCES
# --------------------------------------------

# This program greets the user and does some basic math
print("Welcome to the Python Playground!\nLet's get to know you first...")  # \n creates a new line

# --------------------------------------------
# 🧠 VARIABLES, DATA TYPES, TYPECASTING & USER INPUT
# --------------------------------------------

# Ask user for their name and age
name = input("Enter your name: ")  # Always returns a string
age = int(input("Enter your age: "))  # Typecast to integer

# Display a personalized message using escape sequences
print("Hello", name + "! You're", age, "years old.\nLet's do some quick math! 😊")

# --------------------------------------------
# ➕ ARITHMETIC, COMPARISON & LOGICAL OPERATORS
# --------------------------------------------

# Ask for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
sum_result = num1 + num2
product = num1 * num2
division = num1 / num2

# Comparison
is_equal = num1 == num2
is_greater = num1 > num2

# Logical example
both_positive = (num1 > 0) and (num2 > 0)

print("\n🔢 Results:")
print("Sum:", sum_result)
print("Product:", product)
print("Division:", division)
print("Are both numbers equal?", is_equal)
print("Is the first number greater?", is_greater)
print("Are both numbers positive?", both_positive)

# --------------------------------------------
# 🔤 STRINGS: SLICING, OPERATIONS & METHODS
# --------------------------------------------

# Play with user’s name
print("\n🎭 String Fun:")
print("Your name in uppercase:", name.upper())
print("Your name reversed:", name[::-1])  # slicing to reverse
print("First 3 letters of your name:", name[:3])

# String operations
greeting = "Hello, " + name + "!"
print(greeting.replace("Hello", "Hi"))  # Replace part of the string

print("\nThanks for playing, " + name + "! Goodbye! 👋")
