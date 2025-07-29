# Greet the user by name and calculate age

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2025 - birth_year

print(f"Hello {name}, you are {age} years old!")


# ✅ Introducing a Bug and Fixing It
# age_calculator_bug.py

name = input("Name: ")
birth_year = input("Birth Year: ")

age = 2025 - birth_year      # TypeError here!
print(name + " is " + age + " years old")

# ✅ Fixed Version:
birth_year = int(input("Birth Year: "))  # Convert to int
age = 2025 - birth_year
print(f"{name} is {age} years old")


# ✅ Using Print Debugging
num = input("Enter a number: ")
print("You entered:", num)

num = int(num)
print("After conversion:", num)

result = num * 10
print("Final result:", result)