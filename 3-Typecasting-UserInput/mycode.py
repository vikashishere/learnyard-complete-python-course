# Basic User Input and Typecasting

name = input("What is your name? ")
print("Hello", name)

# Taking numeric input
age = input("Enter your age: ")
print("Next year, you will be", int(age) + 1)

# Full Example with Typecasting

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert string to int
sum_result = int(num1) + int(num2)

print(f"The sum of {num1} and {num2} is {sum_result}")

