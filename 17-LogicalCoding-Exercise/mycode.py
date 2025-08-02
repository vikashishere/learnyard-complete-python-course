# ✅ Example 1: FizzBuzz (Classic)
# Print numbers from 1 to 100:
# Print "Fizz" if divisible by 3
# Print "Buzz" if divisible by 5
# Print "FizzBuzz" if divisible by both

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ✅ Example 2: Palindrome Check (String Reversal)
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# ✅ Example 3: Prime Number Check
num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# ✅ Example 4: Armstrong Number
# A number is Armstrong if the sum of its digits raised to the power of number of digits equals the number.
# Example: 153 → 1³ + 5³ + 3³ = 153
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
if sum([d ** power for d in digits]) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# ✅ Example 5: Swap Two Variables Without Temp
a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b)
