# ✅ Example 1: Basic Try-Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# ✅ Example 2: Handling Multiple Exception Types
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion to integer!")



# ✅ Example 3: Using finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file or cleaning up resources.")



# ✅ Example 4: Raise a Built-in Exception
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age can't be negative.")



# ✅ Example 5: Raise a Custom Exception
class PasswordTooShortError(Exception):
    pass

password = input("Enter password: ")

if len(password) < 6:
    raise PasswordTooShortError("Password must be at least 6 characters.")



# ✅ Example 6: Full Try-Except-Else-Finally Flow
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Not a valid number!")
else:
    print("Success! Result:", result)
finally:
    print("Execution completed.")
    