# ✅ Defining and Using Variables

name = "Vikash"
age = 25
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# ✅ Checking Data Types

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student))  # <class 'bool'>


# 🆚 Without Variables (Not recommended)

# Imagine printing the same name multiple times:
print("Vikash")
print("Vikash is learning Python")
print("Welcome, Vikash")

# Better with variable:
name = "Vikash"
print(name)
print(name + " is learning Python")
print("Welcome,", name)
