# Example1
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7


# Example2
square = lambda x: x * x
print(square(5))  # Output: 25

# Example3
data = [(1, 4), (2, 1), (3, 5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(2, 1), (1, 4), (3, 5)]

# Example4
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # Output: [1, 4, 9, 16]


# Example5
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # Output: [2, 4, 6]


# Example6
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24


# 🔄 Comparison: Normal Function vs Lambda

# ❌ Using def
def double(x):
    return x * 2
print(double(3))  # Output: 6

# ✅ Using lambda
double = lambda x: x * 2
print(double(3))  # Output: 6
# 👉 Lambda version is shorter but less descriptive. Use it only when clarity is not sacrificed.
