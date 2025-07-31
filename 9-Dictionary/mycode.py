# Dict has no indexing
# Dict is mutable dtype
# Dict keys - immutable; values - mutable
# Keys should be unique


# ✅ Basic Dictionary Operations
student = {
    "name": "Ananya",
    "age": 21,
    "course": "BCA"
}

# Access
print(student["name"])

# Add/Update
student["age"] = 22
student["city"] = "Delhi"

# Print all keys
print(student.keys())

# Print all values
print(student.values())

# Remove key
student.pop("course")

# Final dictionary
print(student)

# ---
# ✅ Using .get() Safely
data = {"x": 100}

print(data.get("x"))      # 100
print(data.get("y"))      # None
print(data.get("y", 0))   # Default: 0


# ---
# ✅ Looping through a Dictionary
marks = {
    "Math": 95,
    "Science": 89,
    "History": 76
}

for subject, score in marks.items():
    print(f"{subject}: {score}")


# ---
# ✅ Nested Dictionary
contacts = {
    "Alice": {"phone": "1234", "email": "alice@example.com"},
    "Bob": {"phone": "5678", "email": "bob@example.com"}
}

print(contacts["Bob"]["email"])
