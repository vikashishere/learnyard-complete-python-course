# Without Threading (Sequential)
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for ch in 'abcde':
        print(f"Letter: {ch}")
        time.sleep(1)

print_numbers()
print_letters()


# With threading.Thread
import time
import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for ch in 'abcde':
        print(f"Letter: {ch}")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")


# 🛠 Bonus: Thread with Arguments
def greet(name):
    print(f"Hello {name}")

t = threading.Thread(target=greet, args=("Vikash",))
t.start()
t.join()


# 😵 Common Pitfalls
# Modifying shared data between threads without locks can lead to race conditions.
# GIL (Global Interpreter Lock) makes true parallelism impossible for CPU-bound code.
# Use threading.Lock() if multiple threads are accessing/modifying shared resources.

# 🔐 Example with Lock
import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    for _ in range(100000):
        with lock:
            count += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", count)
# Without the lock, the final count might be incorrect due to race conditions.