# 🧱 Without enumerate() (Manual Indexing)
fruits = ["apple", "banana", "cherry"]
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# 🔻 Problem:
# More lines of code
# Manually managing the index
    

# ✅ With enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# ✅ Changing the Start Index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# ✅ Use Case: Searching with Index
colors = ["red", "green", "blue", "green", "yellow"]
search_color = "green"

for idx, color in enumerate(colors):
    if color == search_color:
        print(f"Found '{search_color}' at index {idx}")


# ✅ Use Case: Conditional Update in a List
scores = [45, 67, 89, 55, 90]

# Add 5 bonus points to every student with index > 2
for i, score in enumerate(scores):
    if i > 2:
        scores[i] = score + 5

print(scores)  # Output: [45, 67, 89, 60, 95]


# ✅ Use Case: Enumerate Over String
word = "python"
for idx, char in enumerate(word):
    print(f"Character at position {idx} is {char}")
