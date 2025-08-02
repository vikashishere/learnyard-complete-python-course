# ✅ Example 1: Without __main__

# utils.py
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # This runs even if you import utils.py

# main.py
import utils  # This will still print "Hello, Alice!"


# ✅ Example 2: With __main__
# utils.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")  # Only runs when you execute utils.py directly

# main.py
import utils  # No output from utils.py unless explicitly called
utils.greet("Bob")


# ✅ Example 3: Script with Test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Testing functions...")
    print(add(3, 4))        # Output: 7
    print(subtract(10, 5))  # Output: 5
