# Basic if else

temp = 25

if temp > 30:
    print("Hot")
elif temp < 10:
    print("Cold")
else:
    print("Pleasant")


# for loop over list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())


# while loop example
    
counter = 1
while counter <= 5:
    print("Count:", counter)
    counter += 1

# using break and continue
    
# Using break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Using continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)



# Loop with else

for i in range(3):
    print("Try:", i)
else:
    print("No break occurred")
