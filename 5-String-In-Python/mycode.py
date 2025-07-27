# String Indexing and Slicing

text = "Programming"

print(text[0])     # 'P'
print(text[-1])    # 'g'
print(text[3:8])   # 'gramm'
print(text[::-1])  # 'gnimmargorP'


# String Operations

a = "Hello"
b = "World"

print(a + " " + b)       # Concatenation
print(a * 3)             # Repetition
print("o" in a)          # Membership
print(len(b))            # Length


# String Methods

message = "  Learn Python!  "

print(message.lower())       # '  learn python!  '
print(message.strip())       # 'Learn Python!'
print(message.replace("Python", "Coding"))  # '  Learn Coding!  '
print(message.find("n"))     # Index of first 'n'
print(message.count("n"))    # Count of 'n'
print(message.startswith(" "))  # True
print(message.endswith("!  "))  # True


# Split and Join

csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")     # ['apple', 'banana', 'cherry']

sentence = " ".join(fruits)      # 'apple banana cherry'
print(sentence)


# 🆚 Before Slicing vs After Slicing

# ❌ Without slicing (manual character access):
word = "Python"
# print first 3 letters
print(word[0] + word[1] + word[2])  # 'Pyt'

# ✅ With slicing:
print(word[:3])  # 'Pyt'
