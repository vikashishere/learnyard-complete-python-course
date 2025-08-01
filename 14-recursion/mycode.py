# factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive case

print(factorial(5))  # Output: 120


# fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8


# Sum of first n natural number
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15


# Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: olleh


# Countdown with recursion
def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


# Example of infinite recursion
def infinite():
    print("Calling again...")
    infinite()

# infinite()  # Don't run this! Will cause RecursionError


# Recursion vs Iterative

# ❌ Iterative Version
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# ✅ Recursive Version
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)
# 👉 Both are correct, but iterative solutions are often more memory-efficient due to no stack overhead.