# Creating and Accessing Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # 'apple'
print(fruits[-1])    # 'cherry'


# Modifying Lists
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Adding Items
fruits.append("kiwi")              # Add to end
fruits.insert(1, "mango")          # Insert at index 1
print(fruits)

# Removing Items
fruits.remove("apple")             # Remove by value
last = fruits.pop()                # Remove last item
print("Removed:", last)


# Sorting and Reversing
numbers = [5, 2, 9, 1]
numbers.sort()        # Ascending
print(numbers)

numbers.reverse()     # Descending
print(numbers)


# Slicing and Membership
colors = ["red", "green", "blue", "yellow"]
print(colors[1:3])          # ['green', 'blue']
print("blue" in colors)     # True


# Nested List Example
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])  # 6


# 🆚 Without a List vs Using a List

# ❌ Without list:
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"

print(student1, student2, student3)


# ✅ With list:
students = ["Alice", "Bob", "Charlie"]
print(students)
