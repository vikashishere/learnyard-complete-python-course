# ✅ Basic Illustration
x = 10  # Global variable

def show():
    y = 5  # Local variable
    print("Inside function - x:", x)
    print("Inside function - y:", y)

show()
print("Outside function - x:", x)
# print("Outside function - y:", y)  # ❌ Error: y is not defined globally



# ⚠️ Shadowing and the global keyword - If you assign to a variable inside a function, 
# Python will treat it as local by default, even if there's a global variable with the same name.
count = 0  # Global variable

def update_count():
    global count  # Tells Python to use the global variable
    count += 1

update_count()
print("Count after update:", count)  # Output: 1



# Without the global keyword:
count = 0

def update_count():
    count = 1  # Local variable with the same name, does NOT modify global
    print("Inside function - count:", count)

update_count()
print("Outside function - count:", count)  # Still 0



# 😵 Common Mistakes
# Forgetting to use global when modifying a global variable → leads to creating a local copy unintentionally.
# Assuming local variables are available outside the function.