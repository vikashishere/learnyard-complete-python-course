# ✅ 1. Writing to a File ('w' mode)
file = open("notes.txt", "w")
file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.close()
# Creates notes.txt or overwrites if it exists.


# ✅ 2. Appending to a File ('a' mode)
file = open("notes.txt", "a")
file.write("This is an appended line.\n")
file.close()
# 🔹 Adds content without deleting previous lines.


# ✅ 3. Reading from a File ('r' mode)
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


# ✅ 4. Reading Line-by-Line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())


# ✅ 5. Writing with 'with' block (recommended)
with open("newfile.txt", "w") as file:
    file.write("Python makes file handling easy!")
# 🔹 with block auto-closes the file after use.


# ✅ 6. Reading with .readlines() and .readline()
# Read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Read one line at a time
with open("notes.txt", "r") as file:
    print(file.readline())  # Reads first line


# ⚠️ What if the file doesn’t exist?
file = open("nofile.txt", "r")  # Raises FileNotFoundError

# Use try-except to handle:
try:
    with open("nofile.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
